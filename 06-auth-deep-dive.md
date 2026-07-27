# 06 — Auth Deep Dive

## ဒီ chapter မှာ ဘာတွေ လုပ်မှာလဲ

- Email/password signup and login
- Auth user နဲ့ `profiles` row ကို trigger နဲ့ချိတ်မယ်
- Flutter auth state နဲ့ Next.js server auth ကိုနားလည်မယ်

## Auth user vs profile

`auth.users` မှာ email, encrypted password, provider data လို sensitive Auth data ရှိတယ်။ App UI data (`display_name`, avatar) ကို `public.profiles` မှာထားတယ်။ `profiles.id = auth.users.id` ဖြစ်တယ်။

Signup ဖြစ်တိုင်း profile row auto-create ဖို့ trigger:

```sql
create function public.handle_new_user()
returns trigger
language plpgsql
security definer set search_path = ''
as $$
begin
  insert into public.profiles (id, display_name)
  values (
    new.id,
    coalesce(new.raw_user_meta_data ->> 'display_name', 'Mont-Tae user')
  );
  return new;
end;
$$;

create trigger on_auth_user_created
  after insert on auth.users
  for each row execute procedure public.handle_new_user();
```

Trigger fail ရင် signup fail နိုင်တယ်။ Function ကို intentionally simple/fast ထားပါ။

## Flutter signup, login, logout

```dart
Future<void> signUp(String email, String password, String displayName) async {
  await supabase.auth.signUp(
    email: email.trim(),
    password: password,
    data: {'display_name': displayName.trim()},
  );
}

Future<void> signIn(String email, String password) async {
  await supabase.auth.signInWithPassword(
    email: email.trim(),
    password: password,
  );
}

Future<void> signOut() => supabase.auth.signOut();
```

Dashboard Auth settings မှာ **Confirm email** enabled ဖြစ်ရင် signup response က user ရပေမဲ့ session မရနိုင်ဘူး။ User email ကို confirm လုပ်ပြီးမှ sign in လုပ်ရမယ်။ ဒါကို UI မှာ "Check your email" လို့ရှင်းပြပါ။

## Flutter auth state

```dart
class AuthGate extends StatelessWidget {
  const AuthGate({super.key});

  @override
  Widget build(BuildContext context) {
    return StreamBuilder<AuthState>(
      stream: supabase.auth.onAuthStateChange,
      builder: (context, snapshot) {
        final session = snapshot.data?.session ?? supabase.auth.currentSession;
        return session == null ? const SignInPage() : const RecipeFeedPage();
      },
    );
  }
}
```

`onAuthStateChange` က signed in/out, token refreshed စတဲ့ events ကိုထုတ်ပေးတယ်။ Navigator ကို event callback ထဲက မကြမ်းတမ်းစွာ push မလုပ်ဘဲ auth state ကို route layer က render/redirect လုပ်တာက ပို maintainable ဖြစ်တယ်။ GoRouter သုံးရင် redirect ကို current session ပေါ်မူတည်စေပါ။

## Magic link and OAuth

```dart
await supabase.auth.signInWithOtp(
  email: email,
  emailRedirectTo: 'com.example.monttae://login-callback/',
);
```

Mobile OAuth / magic-link အတွက် deep link setup လိုတယ်။ Android intent filter, iOS URL scheme, Supabase Auth redirect URL allow-list သုံးနေရာလုံးမှာ matching callback URL ထည့်ရတယ်။ Provider enable မလုပ်ဘဲ Google button ရေးထားရင် အလုပ်မလုပ်ဘူး။

## Next.js: user ကို server မှာစစ်ခြင်း

```ts
import { redirect } from 'next/navigation'
import { createClient } from '@/lib/supabase/server'

export default async function NewRecipePage() {
  const supabase = await createClient()
  const { data: { user } } = await supabase.auth.getUser()
  if (!user) redirect('/sign-in')

  return <h1>Create recipe</h1>
}
```

App Router SSR အတွက် `@supabase/ssr` browser client နဲ့ server client နှစ်ခုလိုတယ်။ Server client က request cookies ကိုသုံးလို့ request တိုင်း create လုပ်ရတယ်။ Expired token refresh ရေးဖို့ Supabase official SSR pattern အတိုင်း `proxy.ts`/session updater ထည့်ပါ။ Authorization check အတွက် server မှာ `getUser()` သို့မဟုတ် current docs မှာ recommend ထားတဲ့ `getClaims()` ကိုသုံး; raw `getSession()` user object ကို authorization အတွက် မယုံပါနဲ့။

## Password reset

```dart
await supabase.auth.resetPasswordForEmail(
  email,
  redirectTo: 'com.example.monttae://reset-password/',
);
```

Reset callback ရပြီးမှ `supabase.auth.updateUser(UserAttributes(password: newPassword))` နဲ့ password အသစ်သတ်မှတ်တယ်။ ဒါကို login screen မှာ "forgot password" flow အဖြစ်သီးသန့်ထားပါ။

## ငဲ့ညီ/မ လေး — သတိထားရမယ့်

- Auth ကို UI redirect နဲ့တင် protect မလုပ်ပါနဲ့။ RLS က data access အမှန်တကယ်ပိတ်ပေးရမယ်။
- Auth user ID ကို email နဲ့မနှိုင်းပါနဲ့။ Foreign key/policies အတွက် UUID `user.id` သုံးပါ။
- OAuth mobile callback က setup အနည်းငယ်ခက်တယ်; email/password ကိုအရင် complete လုပ်ပြီးမှ provider ထည့်ပါ။

## လေ့ကျင့်ခန်း

Sign up page တစ်ခုလုပ်ပါ။ Signup ပြီးရင် Dashboard -> Authentication -> Users မှာ user အသစ်နဲ့ `profiles` table မှာ matching UUID row နှစ်ခုလုံးပေါ်တာစစ်ပါ။

<< Previous: [05 CRUD](./05-crud-with-flutter-and-nextjs.md) | Next: [07 Storage](./07-storage-for-media.md) >>
