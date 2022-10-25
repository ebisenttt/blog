---
title: 'AmplifyとAPIGatewwayとLambdaとDynamoDB（GraphQL）と'
date: 2022-08-19T09:18:57+09:00
draft: true
---

AWS で Amplify を使った Web アプリを作成中です。DynamoDB とどのように連携するのか初心者目線で作業履歴を残しておきます。

## よくわからずとりあえず手を動かして失敗

特にバックエンドのことはわけもわからず，とにかく手を動かしてみようということでこれまで何度かトライしましたが，結局うまくいかずに DB と API を削除してもう一度最初からということを繰り返しています。そこでこの記事では，一度冷静になって

1. 公式ドキュメントの内容を整理
2. 自分の Web アプリ用にコーディング
3. 動作確認
4. 2,3 を繰り返す
   という流れで作業した記録を残します。

## 公式ドキュメントの整理

### テーブルの作成

```graphql
type Todo @model {
	content: String!
}
```

- `amplify push`したときに自動で DynamoDB のテーブルが作成される
- 自動でフィールド`id`が追加され，primary key になる。この挙動をさせずに自身でカスタムするには`customId: ID! @primarykey`のように`@primarykey`を指定したフィールドを追加すれば良い。
- 自動でフィールド`createdAt`, `updatedAt`も追加される
- 型（`String`など）のあとに`!`をつけると`Non-Null`，つまり`Null`でないフィールドとして設定できる

### Query の作成

データベースのテーブルからデータを取る Query を作成します

```graphql
//引数を渡さない場合
query QueryAllTodos {
	listAllTodos() {
		todos {
			items {
				id
				content
				createdAt
				updatedAt
			}
		}
	}
}

//引数を渡す場合
query QueryTodos($content: String) {
	getTodo(content: $content) {
		todos {
			items {
				id
				content
				createdAt
				updatedAt
			}
		}
	}
}
```

- `todos`によりテーブル`Todo`を指定する
- `items{}`に記載したフィールドのデータを返す
- 条件を満たす item のみ取得するには，引数を指定する。このとき`$`が必要であることに注意する。
- Query はアプリ側から API 経由で実行される(下記のコードを参照)

```js
import { API } from 'aws-amplify';
import { listTodos } from './graphql/queries';

const allTodos = API.graphql(graphqlOperation(listAllTodos));
const hogeTodo = API.graphql(
	graphqlOperation(getTodo, {
		content: 'hoge',
	})
);
```

### Mutation の作成

データベースに書き込みする Mutation を作成します

```graphql
mutation CreateTodo {
	createTodo(input: {content: String!}) {
		id
		content
	}
}
```

- 引数に`id`は渡さず，自動で生成してもらう
- 返り値には`id`を含め，自動で生成された`id`を取得する
- Mutation はアプリ側から API 経由で実行される(下記のコードを参照)

```js
import { API } from 'aws-amplify';
import { createTodo } from './graphql/mutations';

const todo = { content: 'fuga' };
const result = API.graphql(
	graphqlOperation(createTodo, {
		input: todo,
	})
);
```

## 自分の Web アプリ用にコーディング

ここまでで基礎的なことのみまとめてみました。ここからは自分が作っている Web アプリ用にコーディングを開始します。追加で必要になったことはその都度まとめ直します。

### Web アプリの概要

今作っている Web アプリは，卓球の試合結果を入力，表示，共有する SNS です。作成するテーブルとしては，

- Match テーブル（試合結果を記録するテーブル）
- Team テーブル（ユーザーの所属するチームを記録するテーブル。チーム内で試合結果を共有することを想定している。）

です。ユーザーは Cognito で管理します。

### 必要になったこと

#### Authentication

```graphql
type Todo
	@model
	@auth (
		rules: [
			{ allow: owner }
			{ allow: public, query: [get, list]}
	]) {
	#略
}
```

- `@auth (rules: [#ここに設定を書く])`
- `{ allow: owner}`は`owner`に全て許可
- `{ allow: public, query: [#ここにクエリを書く]}`は`public`に制限をつける

#### 検索機能

```graphql
type Todo @searchable
#略
```

- `type`に`@searchable`を追加して検索可能にする(なんかいろいろと自動で追加してくれるらしい)

#### Amplify CLI の新バージョンに対応

ことあるごとにアラートがでるので，アップデートをかけました。ここから地獄です。

`amplify codegen`

`Unknown directive "model"`

graphql transformer が v1 から v2 になっていることを知る

`amplify migrate api`でエラー

`You are using queries or mutations in at least one @auth rule. These cannot be automatically migrated.`

知らない間に`schema.graphql`の書き方にもアップデートがあることを知る

```graphql
#旧
type Todo @model @auth(rules: [{ allow: public, query: [get] }])

#新
type Todo @model @auth(rules: [{ allow: public, operations: [read] }])
```

もう一度`amplify push`
Code generation failed with the following error
Unknown directive "model"

Code generation に問題があるということから `amplify codegen`を実行してみる

`Unknown directive "model"`

初期化したい

`amplify add codegen`

Codegen support only one GraphQL API per project

`.graphqlconfig.yml`を削除

再度`amplify add codegen`

エラーなし

`amplidy codegen`

エラーなし

解決！（ここまで数時間）

あとで思い返すと`graphqlconfig.yml`の
`schemaPath`を`amplify/backend//api/apiName/build/schema.graphql`から`amplify/backend//api/apiName/schema.graphql`に変更していたことが原因でした。
