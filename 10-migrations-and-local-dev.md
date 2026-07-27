# 10 — Migrations and Local Development

## ဒီ chapter မှာ ဘာတွေ လုပ်မှာလဲ

- dashboard SQL edit ကနေ migration workflow ကိုရွှေ့မယ်
- schema ကို Git history ထဲထည့်မယ်
- local Supabase workflow သိမယ်

## ဘာကြောင့် migration လိုလဲ

Dashboard မှာ table ပြင်လိုက်ရင် "ဘယ်နေ့ ဘာပြင်ခဲ့လဲ", teammate machine မှာဘယ်လိုပြန်တင်မလဲ မသိတော့ဘူး။ Migration က ordered SQL files ပါ။ Git commit လို database schema history ဖြစ်တယ်။

## CLI workflow

```bash
npx supabase init
npx supabase login
npx supabase link --project-ref your-project-ref
npx supabase migration new create_mont_tae_schema
```

နောက်ဆုံး command က `supabase/migrations/<timestamp>_create_mont_tae_schema.sql` ဖန်တီးတယ်။ Module 03/04 SQL ကို ဒီ file ထဲထားပါ။

```bash
# local Docker stack
npx supabase start
npx supabase db reset

# remote linked project သို့ pending migrations apply
npx supabase db push
```

Migration ကို edit ချင်ရင် shared/remote မှာ apply မလုပ်ရသေးခင်ပဲပြင်ပါ။ Apply ပြီးသား migration ကို rewrite မလုပ်ပါနဲ့; new corrective migration ဖန်တီးပါ။

## Seed data

Local demo data အတွက် `supabase/seed.sql` ထားပါ:

```sql
-- Auth users seed လုပ်တာကို နောက်မှထည့်ပါ။
-- Stable lookup/category data ကသာ seed.sql အတွက် အဆင်ပြေတယ်။
insert into public.recipes (author_id, title, description)
select id, 'Demo recipe', 'Local demo data'
from public.profiles
limit 1;
```

`supabase db reset` က local database ကိုပြန်တည်ဆောက်ပြီး migrations နဲ့ seed ကို run တယ်။ Production ကို reset မလုပ်ပါနဲ့။

## Practical discipline

1. Change လိုရင် migration အသစ်ဖန်တီး။
2. Local မှာ reset/test။
3. App tests run။
4. SQL ကို code review/Git commit။
5. Remote `db push`။

Dashboard က SQL Explorer/debugging အတွက်ကောင်းတယ်။ Team schema source-of-truth မဖြစ်သင့်ဘူး။

## ညီလေး — သတိထားရမယ့်

- `supabase start` Docker လိုတယ်။ Docker မရှိသေးရင် remote-first နဲ့စပြီး later local dev သို့ပြောင်းလို့ရတယ်။
- Generated TypeScript types ကို schema ပြောင်းတိုင်း regenerate လုပ်ပါ: `supabase gen types typescript --linked > src/types/database.ts`။
- Secrets, `.env`, downloaded database dump ကို Git ထဲမထည့်ပါနဲ့။

## လေ့ကျင့်ခန်း

`add_recipe_view_count` migration အသစ်ဖန်တီးပြီး Module 09 ရဲ့ `view_count` schema ကို migration file ထဲပြောင်းပါ။

<< Previous: [09 Edge Functions](./09-edge-functions.md) | Next: [11 Production](./11-deploy-and-production-checklist.md) >>
