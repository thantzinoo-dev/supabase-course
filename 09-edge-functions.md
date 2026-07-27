# 09 — Edge Functions

## ဒီ chapter မှာ ဘာတွေ လုပ်မှာလဲ

- Edge Function လိုမလိုဆုံးဖြတ်မယ်
- authenticated `increment-recipe-views` endpoint ရေးမယ်
- Flutter/Next.js ကနေ invoke လုပ်မယ်

## ဘယ်အချိန်လိုလဲ

CRUD + RLS နဲ့ပြီးရင် client က database ကိုတိုက်ရိုက်သုံးပါ။ အောက်ကအချိန်မှာ Edge Function သုံးပါ:

- Stripe/webhook ကို verify လုပ်ရတဲ့အချိန်
- secret API key (OpenAI, Resend) လိုတဲ့အချိန်
- multiple-step trusted business logic လိုတဲ့အချိန်
- rate limit, email, image processing လိုတဲ့အချိန်

Edge Function က globally distributed, Deno-compatible TypeScript server code ပါ။ Client ထဲမှာ secret မထည့်ရဖို့ server boundary ပေးတာပါ။

## Function create and deploy

```bash
supabase functions new increment-recipe-views
supabase functions serve increment-recipe-views
supabase functions deploy increment-recipe-views
```

`supabase/functions/increment-recipe-views/index.ts`:

```ts
import { createClient } from 'npm:@supabase/supabase-js@2'

Deno.serve(async (req) => {
  const authHeader = req.headers.get('Authorization')
  if (!authHeader) return Response.json({ error: 'Unauthorized' }, { status: 401 })

  const supabase = createClient(
    Deno.env.get('SUPABASE_URL')!,
    Deno.env.get('SUPABASE_ANON_KEY')!,
    { global: { headers: { Authorization: authHeader } } }
  )

  const { recipeId } = await req.json()
  if (typeof recipeId !== 'string') {
    return Response.json({ error: 'recipeId is required' }, { status: 400 })
  }

  const { error } = await supabase.rpc('increment_recipe_views', { recipe_id: recipeId })
  if (error) return Response.json({ error: error.message }, { status: 400 })
  return Response.json({ ok: true })
})
```

Function ထဲက client ကို caller ရဲ့ `Authorization` header နဲ့ create လုပ်ရင် RLS အောက်ကပဲ query လုပ်တယ်။ `service_role` ကိုမလိုအပ်ဘဲ မသုံးပါနဲ့။

RPC SQL function:

```sql
alter table public.recipes add column view_count integer not null default 0;

create function public.increment_recipe_views(recipe_id uuid)
returns void language sql security invoker
as $$
  update public.recipes
  set view_count = view_count + 1
  where id = recipe_id and is_published = true;
$$;
```

`security invoker` က caller RLS ကိုလေးစားတယ်။ Security definer function ရေးရင် attack surface တိုးလို့ database security နားလည်ပြီးမှသုံးပါ။

## Client invoke

```dart
final response = await supabase.functions.invoke(
  'increment-recipe-views',
  body: {'recipeId': recipeId},
);
```

```ts
const { data, error } = await supabase.functions.invoke('increment-recipe-views', {
  body: { recipeId },
})
```

Signed-in user call တွေအတွက် `verify_jwt` default on ထားပါ။ Webhook လို third party က user JWT မပို့နိုင်တဲ့ case မှာသာ config ထဲ `verify_jwt = false` လုပ်ပြီး function code ထဲမှာ provider signature ကိုကိုယ်တိုင်စစ်ပါ။

## ညီလေး — သတိထားရမယ့်

- Publishable key ကို `Authorization: Bearer ...` အနေနဲ့မပို့ပါနဲ့; key က JWT မဟုတ်ဘူး။ SDK ကိုသုံးရင် header handling လုပ်ပေးတယ်။
- Heavy/long job ကို request ထဲမလုပ်ပါနဲ့။ Background task/queue ကိုစဉ်းစားပါ။
- Secrets ကို `supabase secrets set NAME=value` နဲ့ထားပြီး `Deno.env.get('NAME')` နဲ့ဖတ်ပါ။

## လေ့ကျင့်ခန်း

Function ကို local serve လုပ်ပြီး Flutter app ကနေ invoke စမ်းပါ။ Bad `recipeId` ပို့ရင် 400, valid published recipe ပို့ရင် `{ ok: true }` ရအောင်စစ်ပါ。

<< Previous: [08 Realtime](./08-realtime.md) | Next: [10 Migrations](./10-migrations-and-local-dev.md) >>
