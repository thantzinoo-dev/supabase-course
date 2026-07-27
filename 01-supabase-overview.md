# 01 — Supabase Overview ဆိုတာဘာလဲ

## ဒီ chapter မှာ ဘာတွေ လုပ်မှာလဲ

- Supabase ဆိုတာဘာလဲ၊ ဘယ်လို အလုပ်လုပ်လဲ
- Firebase နဲ့ ဘယ်နေရာကွက်လဲ၊ ဘယ်တွေတူလဲ
- Express + Postgres ကို ကိုယ်တိုင် ဆောက်ရင် ဘာတွေ လုပ်ရတာလဲ Supabase က အစားထုတ်ပေးလဲ
- Supabase ရဲ့ architecture အတိအကျ — ဘာတွေ service တွေ ရှိလဲ
- မင်းရဲ့ `Supabase.initialize()` က အရေးအကြီးဆုံး pipeline ရဲ့ ဘယ်နေရာမှာ ပါလဲ

---

## Supabase ဆိုတာဘာလဲ

Supabase ဆိုတာ **open-source Backend-as-a-Service (BaaS)** ပါ။ အဓိကက managed Postgres database တစ်ခု ပေးပြီး၊ အပေါ်မှာ auth, storage, realtime, Edge Functions စတဲ့ backend tools တွေကို တစ်နေရာတည်းမှာ ပေးထားတာပါ။

အရေးကြီးဆုံးအချက်က **Postgres ကို hide မလုပ်ဘူး** ဆိုတာပါ။ SQL ရေးချင်ရင် ရေးလို့ရတယ်၊ database features အပြည့်သုံးလို့ရတယ်။ အဲဒီအပေါ်မှာ Firebase လို လွယ်လွယ်သုံးနိုင်တဲ့ SDK နဲ့ dashboard ကို ထပ်ပေးထားတာပါ။

---

## Supabase vs Firebase

| Feature | Firebase | Supabase |
|---------|----------|----------|
| Database | Cloud Firestore (NoSQL) | **Postgres (SQL)** |
| Auth | Firebase Auth | **GoTrue (JWT-based)** |
| Storage | Cloud Storage | **S3-compatible Storage** |
| Realtime | Realtime Database | **Realtime (WebSocket, Elixir)** |
| Functions | Cloud Functions | **Edge Functions (Deno)** |
| Query Language | SDK-specific | **SQL (any client, any language)** |
| Open Source | မဟုတ်ဘူး | **100% open source** |
| Self-host | မရဘူး | **ရတယ်** |

အကြီးဆုံးကွာခြားချက်က **Firebase က NoSQL** ပါ၊ **Supabase က Postgres** ပါ။ ဒါကြောင့်:

- Express.js နဲ့ SQL သုံးဖူးရင် Supabase ကိုဝင်ရတာ ပိုလွယ်မယ်။ SQL နဲ့ precise query ရေးနိုင်တယ်။ Firebase မှာတော့ NoSQL data modeling ကို သီးသန့်စဉ်းစားရတယ်။
- **Relations** (foreign key, join) ကို native support လုပ်တယ်။ Firestore မှာတော့ reference/document query တွေကို ကိုယ်တိုင်ပိုစီမံရတယ်။
- **Migrations** ရှိတယ်။ Schema ကို version control လုပ်နိုင်တယ်။

---

## Supabase vs Express + Postgres DIY

မင်းက Express.js နဲ့ API ရေးဖူးပြီး Postgres အတွေ့အကြုံနည်းသေးတယ်ဆိုရင် Supabase က ဘာတွေကို အစားထိုးပေးလဲ ကြည့်ရအောင်:

### မင်း DIY လုပ်ရင် လုပ်ရတာတွေ

```
User → Express API → Controller → Service → ORM/Query Builder → Postgres
```

- CRUD endpoint တွေ ရေးရမယ် (GET /recipes, POST /recipes, ...)
- Auth middleware ရေးရမယ် (JWT verify, refresh token)
- File upload handler ရေးရမယ် (multer/s3)
- WebSocket server ရေးရမယ် (socket.io)
- Server အသစ် deploy လုပ်ရမယ်
- Database backup, scaling, monitoring လုပ်ရမယ်

### Supabase ကို သုံးရင်

```
User → Supabase Client SDK → Kong API Gateway → {PostgREST, GoTrue, Realtime, Storage, Edge Functions} → Postgres
```

ဒီ infrastructure အလုပ်အများစုကို Supabase က managed service အဖြစ်ပေးလို့ မင်းက **business logic** ကို ပိုအာရုံစိုက်နိုင်တယ်။

| မင်း ရေးရမှာမရတဲ့ | Supabase က အစားထုတ်ပေးတာ |
|---|---|
| CRUD REST endpoints | **PostgREST** — table တိုင်းကို auto REST API ဖြစ်နေပြီ |
| Auth (signup, login, OAuth, JWT) | **GoTrue** — built in |
| File upload | **Storage API** — S3-compatible |
| Realtime/WebSocket | **Realtime** — Postgres changes stream |
| Database management UI | **Studio (Dashboard)** |
| Server deployment | Managed Supabase infrastructure |
| Scaling | Supabase platform tooling |

**သတိထားရမယ့်:** Supabase က Express ကို **အပြည့်အဝ အစားမထုတ်ပါ**။ Complex business logic တွေ၊ custom validation တွေ၊ third-party API integration တွေ ရှိရင် **Edge Functions** မှာ ရေးရမယ်။ ဒါက Module 9 မှာ ပြောပါမယ်။

---

## Supabase Architecture

Supabase project တစ်ခုမှာ အောက်ပါ service တွေ ပါတယ်:

```
                        ┌─────────────────────────────────┐
                        │          Kong (API Gateway)      │
                        └──────────┬──────────────────────┘
                                   │
       ┌───────────┬────────┬───────┼───────┬──────────┬───────────┐
       ▼           ▼        ▼       ▼       ▼          ▼           ▼
   ┌───────┐ ┌────────┐ ┌──────┐ ┌────────┐ ┌─────────┐ ┌───────────┐
   │GoTrue │ │PostgREST│ │Realtime│ │Storage │ │Functions│ │postgres_  │
   │(Auth) │ │ (API)  │ │       │ │        │ │ (Deno)  │ │  meta     │
   └───┬───┘ └───┬────┘ └──┬───┘ └───┬────┘ └────┬────┘ └─────┬─────┘
       │         │         │         │           │            │
       └─────────┴─────────┴─────────┴───────────┴────────────┘
                                   │
                            ┌──────▼──────┐
                            │   Postgres   │
                            │  (Database)  │
                            └─────────────┘
```

ဒီ service တွေကို အရမ်း သိထားဖို့ လိုပါ:

### 1. Postgres (Database)

Supabase ရဲ့ **core** ပါ။ အပေါ်က service တွေအားလုံးက Postgres နဲ့ချိတ်ထားတယ်။ မင်းက SQL query run လုပ်နိုင်တယ်၊ schema ပြင်နိုင်တယ်၊ Postgres capabilities ကို တိုက်ရိုက်သုံးနိုင်တယ်။

### 2. PostgREST (REST API)

ဒါက မင်းအတွက် အရေးအကြီးဆုံး service ပါ။ **Table တိုင်းကို automatic REST API ဖန်တီးပေးတယ်။** မင်း `recipes` table ဖန်တီးလိုက်ရင် `GET /rest/v1/recipes` လို endpoint ရှိနေပြီ။ Basic CRUD endpoint တွေကို ကိုယ်တိုင်ရေးစရာမလိုဘူး။

ဒါကြောင့် မင်းရဲ့ Express `router.get('/recipes', ...)` တွေ မရေးတော့ဘဲ အလုပ်လုပ်နေတာပါ။

### 3. GoTrue (Auth)

JWT-based authentication service ပါ। Email/password, magic link, OAuth (Google, Apple, GitHub စသဖြင့်) တွေကို အိမ်နဲ့ ကူညီတယ်। ပြီးတော့ `auth.uid()`  function ကို Postgres RLS မှာ သုံးနိုင်တယ် — ဒါက Module 4 မှာ ပြောပါမယ်။

### 4. Realtime (WebSocket)

Elixir နဲ့ ရေးထားတဲ့ WebSocket server ပါ။ Postgres မှာ data ပြောလိုက်တာနဲ့ client တွေကို **real-time** ပြောပေးတာပါ။ ဒီ course မှာ comment feed တစ်ခု live လုပ်မယ် — လူတစ်ယောက် comment ရေးလိုက်တော့ ချက်ချင်း ပေါ်သွားမယ်။

### 5. Storage (File Upload)

S3-compatible object storage ပါ။ File တွေ upload လုပ်ပါ၊ public/private buckets တွေ သတ်မှတ်ပါ၊ metadata တွေကိုတော့ Postgres မှာ သိန်ပါ။ Recipe ပုံတွေ upload လုပ်တာ ဒါကို သုံးမယ်။

### 6. Edge Functions (Deno)

Serverless function တွေ ပါ။ TypeScript/JavaScript နဲ့ ရေးပါ။ **Custom business logic** တွေ လုပ်ရတာဖြစ်ပါတယ် — ဥပမာ view count တွေ increment လုပ်တာ၊ email ပြောတာ၊ webhook တွေ handle လုပ်တာ။

### 7. Kong (API Gateway)

အပေါ်က service တွေ အကြားမှာ ပါတယ်။ Routing, rate limiting, auth header parsing စသဖြင့် လုပ်ပေးတာပါ။ မင်းက ကိုယ်တိုင် ကျေးဇူးတင်ရမယ်အရာ မဟုတ်ဘူး — ဒါက အိမ်နဲ့ အလုပ်လုပ်နေပြီ။

---

## မင်းရဲ့ Flutter App က ဘယ်နေရာမှာ ပါလဲ

မင်း `Supabase.initialize()` လုပ်ထားပြီး `dotenv` နဲ့ key တွေ load လုပ်ထားပြီ။ ဒါက ဘယ်နေရာမှာ ပါလဲ architecture ထဲမှာ:

```
Flutter App (Client)
    │
    ▼  Supabase Flutter SDK
    │
    ▼  HTTP/WebSocket requests
    │
    ▼  Supabase Cloud (Kong API Gateway)
        │
        ├─► GoTrue    (auth operations)
        ├─► PostgREST (CRUD queries)
        ├─► Realtime  (WebSocket subscriptions)
        └─► Storage   (file uploads)
```

မင်းရဲ့ Flutter app က **Supabase Cloud** ကို HTTP နဲ့ WebSocket တွေ နဲ့ ပြီးဆက်ပါတယ်။ Kong API Gateway က request ကို သတ်မှတ်ထားတဲ့ service ကို route လုပ်ပေးပါ။

**တိကျတိကျပြောရင်** — မင်း `supabase.from('recipes').select()` လုပ်တော့:

1. Flutter SDK → HTTP GET request → `https://<project-ref>.supabase.co/rest/v1/recipes`
2. Kong → PostgREST
3. PostgREST → `SELECT * FROM recipes` (Postgres မှာ run လုပ်တယ်)
4. ပြန်လာတဲ့ data ကို Kong → Flutter app

အဲဒါပါ။ မင်းရဲ့ server-side controller မရေးတော့ဘဲ — SDK က ကိုယ်စီ အလုပ်လုပ်ပေးတာပါ။

---

## ကျေးဇူးတင်ရမယ် Concepts တွေ

ဒီ chapter ကို နိုင်ရင် အောက်ပါ terms တွေကို စူးစိုက်ထားပါ:

- **BaaS (Backend-as-a-Service)** — backend ကို service အနေနဲ့ ပေးတာ။ မင်းက server မလုပ်ဘဲ frontend ကိုပဲ ရှည်လုပ်ရမယ်။
- **PostgREST** — Postgres table တွေကို auto REST API ဖန်တီးတဲ့ tool။ ဒါက Supabase ရဲ့ အပြိုင်ရင်းကောင်းဆုံး feature ပါ။
- **GoTrue** — Supabase ရဲ့ auth service။ Open-source ပါ၊ Go နဲ့ ရေးထားပါ။
- **JWT (JSON Web Token)** — Auth token format။ GoTrue က JWT ပေးတာပါ၊ ဒီ token ကို RLS မှာ `auth.uid()` ဖြင့် 读取 လုပ်တာပါ။
- **RLS (Row Level Security)** — Postgres ရဲ့ native security feature။ Table တစ်ခုမှာ row တစ်ခုခုအလိုက် access control လုပ်တာပါ။ ဒါက Module 4 မှာ အရမ်း ပြောပါမယ်။

---

## ငဲ့ညီ/မ လေး — သတိထားရမယ့် Gotchas

1. **Supabase က Firebase clone မဟုတ်ဘူး။** Firebase က NoSQL, Supabase က Postgres ဖြစ်လို့ schema design နဲ့ query mindset ကွာတယ်။
2. **PostgREST က table schema ကို ဖော်ထုတ်ပေးတာပါ။** ဒါကြောင့် table/column naming ကို လိုက်နာနေရမယ်။ `camelCase` မသုံးပါနဲ့ — Postgres convention အတိုင်း `snake_case` သုံးပါ။
3. **Supabase က "serverless" မဟုတ်ဘူး။** Postgres server ရှိတယ်၊ connection pooler ရှိတယ်։ ဒါမျိုး "managed database" ပါ။ Free tier မှာ 500MB database limit ရှိတယ်။
4. **SDK က HTTP/WebSocket client wrapper ပါ။** SDK က Supabase APIs ကိုခေါ်ပေးတာဖြစ်လို့ raw HTTP ကို ပုံမှန်မရေးရတော့ဘူး။

---

## လေ့ကျင့်ခန်း — Exercise

Supabase Dashboard မှာ မင်းရဲ့ project ကို သွားပြီး **SQL Editor** ကို ဖွင့်ပါ။ အောက်ပါ query ကို run လုပ်ပြီး ရလဒ်ကို မှတ်ပါ:

```sql
SELECT version();
```

ဒါက မင်းရဲ့ project မှာ Postgres ဘယ် version ရှိလဲ ပြောပေးမယ်။ အောက်တိုင်း page တွေကို လေ့ကျင့်ကြည့်လိုက်ပါ:

- Dashboard → **Project Settings** → ဘယ် info တွေ ရှိလဲ
- Dashboard → **Table Editor** → ဘယ် tables ရှိလဲ (supa_add_column_... လို default tables တွေ ရှိနိုင်ပါ)
- Dashboard → **SQL Editor** → page က ဘယ်လို မြင်လဲ

---

<< နောက်ဆုံး chapter: [02 — Project Setup Recap](./02-project-setup-recap.md) ဆက်ဖတ်ပါ >>
