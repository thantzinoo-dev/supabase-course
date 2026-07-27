# 08 — Realtime Comments

## ဒီ chapter မှာ ဘာတွေ လုပ်မှာလဲ

- Realtime ရဲ့ Postgres Changes, Broadcast, Presence ကို ခွဲသိမယ်
- Recipe comment stream ကို Flutter မှာလုပ်မယ်
- subscription cleanup ကို မမေ့အောင်လုပ်မယ်

## Realtime modes

| Mode | ဘယ်အတွက် |
|---|---|
| Postgres Changes | database row insert/update/delete ကို listen |
| Broadcast | ephemeral custom messages: typing, cursor, game event |
| Presence | online/active user state |

Comment feed အတွက် Postgres Changes က ရိုးရှင်းဆုံးပါ။ Typing indicator လို DB မသိမ်းရမယ့် event အတွက် Broadcast သုံးပါ။

## Realtime publication enable

Dashboard -> Database -> Publications/Replication မှာ `comments` table ကို `supabase_realtime` publication ထဲထည့်ပါ။ SQL ဖြင့်လည်း:

```sql
alter publication supabase_realtime add table public.comments;
```

Table ကို RLS enable လုပ်ထားရင် Realtime client ကလည်း corresponding `select` policy အောက်မှာပဲ row ကိုလက်ခံရတယ်။ Realtime အတွက် RLS bypass မလုပ်ပါနဲ့။

## Flutter: easiest stream

`stream(primaryKey: ['id'])` က initial rows နဲ့ future database changes ကို `Stream<List<Map<String, dynamic>>>` အဖြစ်ပေးတယ်။ StatefulWidget state မှာ stream ကို တစ်ခါပဲ create လုပ်ပါ။ Build ထဲမှာ create လုပ်ရင် rebuild တိုင်း re-subscribe ဖြစ်မယ်။

```dart
class CommentsList extends StatefulWidget {
  const CommentsList({super.key, required this.recipeId});
  final String recipeId;

  @override
  State<CommentsList> createState() => _CommentsListState();
}

class _CommentsListState extends State<CommentsList> {
  late final Stream<List<Map<String, dynamic>>> _comments;

  @override
  void initState() {
    super.initState();
    _comments = supabase
        .from('comments')
        .stream(primaryKey: ['id'])
        .eq('recipe_id', widget.recipeId)
        .order('created_at');
  }

  @override
  Widget build(BuildContext context) {
    return StreamBuilder<List<Map<String, dynamic>>>(
      stream: _comments,
      builder: (context, snapshot) {
        if (snapshot.hasError) return Text('Could not load comments: ${snapshot.error}');
        if (!snapshot.hasData) return const Center(child: CircularProgressIndicator());
        final comments = snapshot.data!;
        return ListView.builder(
          itemCount: comments.length,
          itemBuilder: (_, index) => ListTile(title: Text(comments[index]['body'] as String)),
        );
      },
    );
  }
}
```

## Flutter: low-level channel

Event payload ကိုကိုယ်တိုင် handle ချင်ရင် channel API သုံးပါ:

```dart
late final RealtimeChannel channel;

@override
void initState() {
  super.initState();
  channel = supabase.channel('recipe-comments-${widget.recipeId}')
    ..onPostgresChanges(
      event: PostgresChangeEvent.insert,
      schema: 'public',
      table: 'comments',
      filter: PostgresChangeFilter(
        type: PostgresChangeFilterType.eq,
        column: 'recipe_id',
        value: widget.recipeId,
      ),
      callback: (payload) => debugPrint('New comment: ${payload.newRecord}'),
    )
    ..subscribe();
}

@override
void dispose() {
  supabase.removeChannel(channel);
  super.dispose();
}
```

## Next.js client component

```tsx
'use client'

useEffect(() => {
  const channel = supabase
    .channel(`recipe-comments-${recipeId}`)
    .on('postgres_changes', {
      event: 'INSERT', schema: 'public', table: 'comments', filter: `recipe_id=eq.${recipeId}`,
    }, (payload) => setComments((old) => [...old, payload.new as Comment]))
    .subscribe()

  return () => { supabase.removeChannel(channel) }
}, [recipeId, supabase])
```

Initial comments ကို normal query နဲ့ယူ, incoming event တွေကို state ထဲ merge လုပ်ပါ။ Event အသစ်တိုင်း page refetch လုပ်တာ MVP မှာရပေမဲ့ traffic များရင် inefficient ဖြစ်တယ်။

## ညီလေး — သတိထားရမယ့်

- Realtime ကို every table/every row အတွက် မဖွင့်ပါနဲ့။ User value ရှိတဲ့ use case မှာပဲသုံးပါ။
- Subscription ကို widget/component unmount မှာ cleanup မလုပ်ရင် duplicate event, memory/network waste ဖြစ်တယ်။
- Postgres Changes က row-by-row authorization checking လုပ်ရလို့ high volume system မှာ Broadcast/other architecture ကို evaluate လုပ်ပါ။

## လေ့ကျင့်ခန်း

Browser window နှစ်ခု သို့ device နှစ်ခုနဲ့ recipe တစ်ခုဖွင့်ပါ။ Device A မှာ comment insert လုပ်ပြီး Device B မှာ refresh မလုပ်ဘဲပေါ်တာစစ်ပါ။

<< Previous: [07 Storage](./07-storage-for-media.md) | Next: [09 Edge Functions](./09-edge-functions.md) >>
