# 07 — Storage for Recipe Media

## ဒီ chapter မှာ ဘာတွေ လုပ်မှာလဲ

- Storage bucket create လုပ်မယ်
- user တစ်ယောက်ကို ကိုယ့် folder ထဲပဲ upload ခွင့်ပေးမယ်
- Flutter ကနေ recipe image upload လုပ်မယ်
- public URL နဲ့ private signed URL ကို ခွဲသိမယ်

## Bucket design

Mont-Tae recipe cover image တွေ လူတိုင်းမြင်ရမယ်ဆိုတော့ `recipe-images` ကို **public bucket** လုပ်မယ်။ Public က "file URL ကိုသိသူ download လုပ်လို့ရ" ဆိုတာပါ; upload/delete က RLS policy နဲ့ပဲ အုပ်ချုပ်ရသေးတယ်။

Dashboard -> Storage -> New bucket:

```text
Name: recipe-images
Public bucket: enabled
Allowed MIME types: image/jpeg, image/png, image/webp
File size limit: 5 MB
```

App code က bucket create မလုပ်ပါနဲ့။ Infrastructure/schema setup မှာ dashboard သို့ migration နဲ့တစ်ခါတည်းလုပ်ပါ။

## Storage RLS policies

Storage files metadata က `storage.objects` table မှာရှိတယ်။ `recipe-images/<user-id>/<recipe-id>.jpg` layout သုံးမယ်။ Folder first segment ကို auth user UUID နဲ့စစ်မယ်။

```sql
create policy "users upload own recipe images"
on storage.objects for insert to authenticated
with check (
  bucket_id = 'recipe-images'
  and (storage.foldername(name))[1] = (select auth.uid()::text)
);

create policy "users update own recipe images"
on storage.objects for update to authenticated
using (
  bucket_id = 'recipe-images'
  and owner_id = (select auth.uid())
)
with check (
  bucket_id = 'recipe-images'
  and (storage.foldername(name))[1] = (select auth.uid()::text)
);

create policy "users delete own recipe images"
on storage.objects for delete to authenticated
using (
  bucket_id = 'recipe-images'
  and owner_id = (select auth.uid())
);
```

Public bucket ဆိုလို့ `select` policy မလိုဘူး။ Private bucket ဆိုရင် file download/list အတွက် `select` policy ထည့်ရမယ်။ `upsert: true` နဲ့ overwrite လုပ်ရင် `insert` တင်မက `select` နဲ့ `update` policy လည်းလိုတယ်။

## Flutter image upload

`image_picker` နဲ့ image ရပြီးသားဆိုပါစို့:

```dart
import 'dart:io';
import 'package:image_picker/image_picker.dart';

Future<String> uploadCoverImage({
  required XFile image,
  required String recipeId,
}) async {
  final user = supabase.auth.currentUser;
  if (user == null) throw StateError('Sign in first');

  final extension = image.name.split('.').last.toLowerCase();
  final path = '${user.id}/$recipeId/cover.$extension';

  await supabase.storage.from('recipe-images').upload(
    path,
    File(image.path),
    fileOptions: const FileOptions(upsert: false),
  );

  return path;
}
```

Web Flutter မှာ `File(image.path)` မအလုပ်လုပ်နိုင်ဘူး။ bytes နဲ့ `uploadBinary` သုံးပါ:

```dart
final bytes = await image.readAsBytes();
await supabase.storage.from('recipe-images').uploadBinary(
  path,
  bytes,
  fileOptions: const FileOptions(contentType: 'image/jpeg'),
);
```

Upload ပြီးမှ returned `path` ကို `recipes.cover_image_path` ထဲသိမ်းပါ။ Full URL ကို database မှာမသိမ်းတာက bucket/domain ပြောင်းလည်း data migration မလိုဖို့ပါ။

```dart
final publicUrl = supabase.storage
    .from('recipe-images')
    .getPublicUrl(recipe['cover_image_path'] as String);
```

## Correct create flow

1. Recipe ကို draft အဖြစ် insert လုပ်ပြီး returned `id` ယူပါ။
2. `$userId/$recipeId/cover.jpg` path ကို upload လုပ်ပါ။
3. Recipe row ကို `cover_image_path` နဲ့ update လုပ်ပါ။
4. Error ဖြစ်ရင် orphan file/row ကို cleanup လုပ်ဖို့ plan ရှိပါ။

Transaction တစ်ခုထဲမှာ client က Storage + database request နှစ်ခုကို atomic မလုပ်နိုင်ဘူး။ MVP မှာ best effort လုပ်; production မှာ abandoned upload cleanup job သို့ Edge Function စဉ်းစားပါ။

## Next.js upload note

Browser client က `File` ကိုတင်နိုင်တယ်:

```ts
const file = input.files?.[0]
if (!file) return

const path = `${user.id}/${recipeId}/cover-${crypto.randomUUID()}.webp`
const { error } = await supabase.storage
  .from('recipe-images')
  .upload(path, file, { contentType: file.type, upsert: false })
if (error) throw error
```

Server က secret key သုံးပြီး arbitrary user upload မလုပ်ပါနဲ့။ Client upload + Storage RLS က user ownership ကို policy နဲ့အတည်ပြုတာက ရိုးရှင်းပြီး secure ဖြစ်တယ်။

## ငဲ့ညီ/မ လေး — သတိထားရမယ့်

- Filename ကို user input ပေးသလို တိုက်သုံးမနေပါနဲ့; random/controlled path သုံးပါ။
- MIME type client ပို့တဲ့ဟာကို 100% မယုံပါနဲ့။ Allowed MIME types/size limits bucket မှာထားပါ; sensitive system မှာ server-side file validation ပါထည့်ပါ။
- Private image အတွက် `getPublicUrl()` မသုံးပါနဲ့။ `createSignedUrl(path, seconds)` သုံးပါ။

## လေ့ကျင့်ခန်း

Recipe draft တစ်ခု create, cover image upload, `cover_image_path` update လုပ်ပါ။ Browser incognito မှာ public URL ကိုဖွင့်လို့ရတာစစ်ပါ။ ပြီးရင် အခြား account နဲ့ first user folder ကို upload/delete မလုပ်နိုင်တာစစ်ပါ။

<< Previous: [06 Auth](./06-auth-deep-dive.md) | Next: [08 Realtime](./08-realtime.md) >>
