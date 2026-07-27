# 12 — Next Steps and Resources

## ဒီ chapter မှာ ဘာတွေ လုပ်မှာလဲ

- ဒီ course ပြီးရင် ဘာကိုဆက်သင်မလဲ
- Mont-Tae ကို real app အဖြစ်တိုးဖို့ roadmap
- Useful Supabase resources

## မင်းအခုရထားတာ

ဒီ course ပြီးရင် မင်းမှာ:

- Postgres schema + foreign keys + constraints
- Auth + profile trigger
- RLS-enforced Flutter/Next.js CRUD
- Storage image upload
- Realtime comments
- Edge Function basics
- migrations-first workflow

ဒီ foundation က app အများကြီးအတွက်တူတူသုံးလို့ရတယ်။ Recipe app ကို notes app, marketplace, booking, chat app ပြောင်းတာက schema/business rules ပဲပြောင်းတာ။

## Mont-Tae v2 roadmap

1. **Categories/tags**: `categories`, `recipe_categories` junction table. JSON array မထားဘဲ many-to-many relation practice လုပ်ပါ။
2. **Likes/bookmarks**: `(user_id, recipe_id)` composite unique constraint နဲ့ duplicate like မဖြစ်အောင်လုပ်ပါ။
3. **Full text search**: Postgres generated `tsvector`, GIN index, RPC search function ကိုလေ့လာပါ။
4. **Notifications**: comment insert database trigger + Edge Function/queue. Notification delivery ကို request path မှာမကြာအောင်ထားပါ။
5. **Admin moderation**: report table, role claim, tightly-scoped admin function. `is_admin` boolean ကို client payload ကနေ မယုံပါနဲ့။
6. **Offline Flutter UX**: local cache, optimistic update, retry queue. Supabase က network backend ဖြစ်လို့ offline behavior ကို app က design လုပ်ရတယ်။

## Deep topics

| Topic | ဘာကြောင့်လေ့လာ |
|---|---|
| Postgres indexes + `EXPLAIN` | data တက်လာရင် query မြန်ဖို့ |
| Database functions/RPC | atomic logic ကို database မှာထားဖို့ |
| pg_cron / Queues | scheduled/background work |
| pgvector | semantic search / AI recommendations |
| Supabase branches | isolated staging databases |
| Flutter state management | auth/data/realtime UI ကို maintainable ဖြစ်ဖို့ |
| Next.js SSR | SEO, secure server rendering, auth cookies |

## Official resources

- [Supabase Docs](https://supabase.com/docs)
- [Supabase Flutter reference](https://supabase.com/docs/reference/dart/introduction)
- [Supabase JavaScript reference](https://supabase.com/docs/reference/javascript/introduction)
- [Supabase GitHub](https://github.com/supabase/supabase)
- [PostgreSQL documentation](https://www.postgresql.org/docs/)
- [Supabase Discord](https://discord.supabase.com/)

Docs ကိုမေးခွန်းနဲ့ဖတ်ပါ။ "RLS ဘာလဲ" လို့အကျယ်မရှာဘဲ "Supabase storage policy user folder authenticated" လို့ exact search လုပ်ရင် ဖြေရှင်းချက်မြန်တယ်။

## Final big-bro advice

Supabase ကို magic backend လို့မမြင်ပါနဲ့။ Postgres, SQL, auth session, security policy, HTTP/WebSocket ဆိုတဲ့ real backend concepts တွေကို convenient tools နဲ့ပေးထားတာပါ။

မင်းက Express ရေးဖူးတာ အားနည်းချက်မဟုတ်ဘူး။ API, auth, DB ကိုခွဲစဉ်းစားတတ်ပြီးသားဆိုတော့ Supabase ရဲ့ "auto API" ကို ပိုသေချာနားလည်နိုင်တယ်။ အရေးကြီးတာက RLS ကို controller authorization လိုသဘောထားပြီး လေးလေးနက်နက်စစ်ဖို့ပါ။

**Next practical action:** Module 03 SQL ကို development Supabase project မှာ run, Module 04 RLS apply, Flutter မှာ sign-up + recipe create screen လုပ်ပါ။ Stuck ဖြစ်ရင် error message အပြည့်အစုံနဲ့ current SQL policy ကိုယူပြီး debug လုပ်ပါ။

<< Previous: [11 Production](./11-deploy-and-production-checklist.md) | [Back to course index](./README.md) >>
