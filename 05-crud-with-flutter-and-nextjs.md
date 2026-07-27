# 05 — CRUD with Flutter and Next.js

## ဒီ chapter မှာ ဘာတွေ လုပ်မှာလဲ

- `select`, `insert`, `update`, `delete` ကို Flutter/TypeScript နှစ်ဖက်နဲ့ရေးမယ်
- relation data ကို one request နဲ့ယူမယ်
- RLS-aware recipe create flow ဆောက်မယ်

## Read recipes

### Flutter

```dart
final recipes = await supabase
    .from('recipes')
    .select('id, title, description, cover_image_path, prep_minutes, created_at, profiles(display_name, avatar_path)')
    .eq('is_published', true)
    .order('created_at', ascending: false)
    .range(0, 19);
```

`profiles(...)` က foreign key relationship ကို embed လုပ်တာပါ။ N+1 query မလုပ်ဘဲ recipe 20 ခုနဲ့ author data ကို request တစ်ခါတည်းရတယ်။

### Next.js Server Component

```tsx
import { createClient } from '@/lib/supabase/server'

export default async function RecipesPage() {
  const supabase = await createClient()
  const { data: recipes, error } = await supabase
    .from('recipes')
    .select('id, title, cover_image_path, profiles(display_name)')
    .eq('is_published', true)
    .order('created_at', { ascending: false })
    .range(0, 19)

  if (error) throw new Error(error.message)
  return <pre>{JSON.stringify(recipes, null, 2)}</pre>
}
```

## Filter patterns

```dart
// Flutter
await supabase.from('recipes').select().ilike('title', '%mont%');
await supabase.from('recipes').select().inFilter('id', recipeIds);
await supabase.from('recipes').select().eq('author_id', userId);
```

```ts
// TypeScript
await supabase.from('recipes').select().ilike('title', '%mont%')
await supabase.from('recipes').select().in('id', recipeIds)
await supabase.from('recipes').select().eq('author_id', userId)
```

`ilike` က case-insensitive search ပါ။ User input ကို `%${query}%` ထည့်မယ်ဆိုရင် empty query ကို အရင် handle လုပ်ပါ; full scan မတော်တဆမလုပ်စေချင်ဘူး။

## Create recipe

RLS policy က `author_id == auth.uid()` စစ်တယ်။ Current authenticated user ကို SDK ကနေယူပြီး payload မှာထည့်ပါ။

```dart
Future<void> createRecipe({
  required String title,
  required String description,
  required List<Map<String, String>> ingredients,
  required List<String> steps,
}) async {
  final user = supabase.auth.currentUser;
  if (user == null) throw StateError('Please sign in first.');

  await supabase.from('recipes').insert({
    'author_id': user.id,
    'title': title.trim(),
    'description': description.trim(),
    'ingredients': ingredients,
    'steps': steps,
    'is_published': false,
  });
}
```

```ts
'use server'

import { createClient } from '@/lib/supabase/server'

export async function createRecipe(formData: FormData) {
  const supabase = await createClient()
  const { data: { user } } = await supabase.auth.getUser()
  if (!user) throw new Error('Please sign in first.')

  const { error } = await supabase.from('recipes').insert({
    author_id: user.id,
    title: String(formData.get('title') ?? '').trim(),
    description: String(formData.get('description') ?? '').trim(),
    ingredients: [],
    steps: [],
  })
  if (error) throw new Error(error.message)
}
```

Client-side validation UX အတွက်ရှိသင့်တယ်။ ဒါပေမဲ့ database `check` constraint နဲ့ RLS က final security/validity layer ပါ။ Client validation ကို bypass လုပ်လို့ရတယ်။

## Update and delete

```dart
// Only succeeds for recipe author because RLS enforces it.
await supabase
    .from('recipes')
    .update({'title': 'Updated title', 'is_published': true})
    .eq('id', recipeId);

await supabase.from('recipes').delete().eq('id', recipeId);
```

```ts
const { error } = await supabase
  .from('recipes')
  .update({ is_published: true })
  .eq('id', recipeId)

if (error) throw error
```

Update/delete query မှာ `.eq('id', recipeId)` မပါရင်? RLS ရှိရင် own rows အကုန် update/delete လုပ်နိုင်တယ်။ Filter ကို မမေ့ပါနဲ့။

## Return inserted row

Supabase insert/update က performance အတွက် row data ပြန်မပေးတာ default ပါ။ Create ပြီး ID လိုရင် `.select().single()` ကို chain လုပ်ပါ။

```dart
final recipe = await supabase.from('recipes').insert({
  'author_id': supabase.auth.currentUser!.id,
  'title': 'မုန့်လုံးရေပေါ်',
  'description': 'Sweet rice dumplings',
}).select().single();

final recipeId = recipe['id'] as String;
```

## Error handling

```dart
try {
  await createRecipe(/* ... */);
} on PostgrestException catch (error) {
  // constraint, RLS, query errors
  debugPrint('Database error: ${error.message}');
  rethrow;
} on AuthException catch (error) {
  debugPrint('Auth error: ${error.message}');
  rethrow;
}
```

Production UI မှာ raw database error ကို user ကိုမပြပါနဲ့။ Log full error, UI မှာ "Could not save recipe. Try again." လို actionable message ပြပါ။

## ညီလေး — သတိထားရမယ့်

- `select('*')` prototype မှာ OK, production list page မှာ လိုတဲ့ columns ပဲရွေးပါ။
- `.single()` က 0 or >1 row ဖြစ်ရင် error ပေးတယ်။ optional result အတွက် `.maybeSingle()` သုံးပါ။
- Browser/client request မှာ pagination မပါရင် data ကြီးလာတဲ့နေ့ app နှေးမယ်။ `.range()` ထည့်တဲ့ habit လုပ်ပါ။

## လေ့ကျင့်ခန်း

Flutter မှာ published recipe list page တစ်ခုရေးပါ။ Empty, loading, error, data state လေးခုလုံး UI ရှိအောင်လုပ်ပါ။

<< Previous: [04 RLS](./04-row-level-security.md) | Next: [06 Auth](./06-auth-deep-dive.md) >>
