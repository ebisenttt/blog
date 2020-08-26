---
title: "HugoとGithubPagesでブログ公開"
date: 2020-08-19T13:16:13+09:00
draft: true

categories: ["Programming"]
tags: ["hugo", "github pages"]
author: ""
---
# はじめに
これは完全に自分のための備忘録です。

### 記事の作成
次のコマンドを実行すると`content/post`の中に`article.md`が作成される。このときデフォルトの記事タイトルは`article`になる。
```
$ hugo new post/article.md
```
`article.md`を開くと次のような内容になっている。ただし，選択したテーマによって若干異なるがだいたいこんな感じ。
```
---
title: "article"      //ファイル名末尾の`.md`を除いた文字列になる
date: （ファイル作成日） //ファイル作成日時。記事公開時に更新される。
draft: true　　　　　　 //trueのとき下書きとして扱われ，公開されない。あとで変更する。

categories: [] //カテゴリ。好きにつけてOK。
tags: []　　　　//タグ。同上。
author: ""     //著者名。同上。
---
//ここに内容を書く。
```
Hugoはマークダウン記法を採用している（記事のファイルの拡張子が`.md`になっている）。マークダウン記法の文法について，著者はまだ詳しくない。わかりやすいサイトのリンクを貼っておく。

[Qiita マークダウン記法 一覧表・チートシート](https://qiita.com/kamorits/items/6f342da395ad57468ae3)

### 記事の編集と確認
Hugoはローカルサーバーの機能も兼ねている。これを使って編集中の記事がブラウザで実際にどう表示されるのか確認する。次のコマンドを実行してローカルサーバーを起動する。
```
$ hugo server -D
```
次にブラウザのアドレスバーに「localhost:1313」と入力すると，今作っているサイトがブラウザで表示される。ここでレイアウト等を確認しながら，記事の内容を編集する。もし「Notfound404」と表示されるようであれば，作業しているディレクトリ名まで入力（たとえば「localhost:1313/blog」など）する。

記事が完成したら，公開のために記事上部の`draft: true`を`draft: false`にして保存し終了。

### 公開用のファイルを作成
次のコマンドを実行
```
$ hugo
```
`/docs`に公開用のファイルが作成される。

### Githubへのアップロード
Githubでアカウントを作成し，リポジトリを作っておく。今回は「blog」というリポジトリを想定する。
まず

変更があったファイルを確認する。次のコマンドを実行する。赤字で書かれているファイルが，変更があったのにローカルリポジトリに追加されていないファイル。
```
$ git satatus
```

上で表示されたファイルを全てローカルリポジトリに追加する
```
$ git add .
```
ローカルリポジトリをコミットする。このとき変更内容を記録しておいた方があとで見返したときにわかりやすい。例えば`article.md`を新しく作成して「article」というタイトルの記事を公開するときは`"add article.md"などとすればよい。
``` 
$ git commit -m "article.md"
```
いよいよGithubのリモートリポジトリにアップロードする。
```
$ git push origin master
```
以上でGithubへのアップロードは終了。

### 確認
最後に無事に記事が表示されるか確認する。記事を編集しているときにはブラウザで「localhost:1313」をみていた。今はすでに記事がネット上に公開されているので，記事のURLを入力する。URLはGithubのリポジトリのページの「Setting」に載っている。表示されたら終了。お疲れ様でした。