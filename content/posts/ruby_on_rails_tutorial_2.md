---
title: "2章 | 初学者によるRuby on Rails Tutorial学習記録"
date: 2021-03-06T14:29:08+09:00
draft: false

tags: ['ruby', 'rails']
---
この記事では，プログラミング初学者によるRuby on Rails Tutorial学習中のつまずきを章別に共有します。一覧は次のページに用意しています。
[はじめに | 初学者によるRuby on Rails Tutorial学習記録](https://ebisenttt.github.io/blog/article/ruby_on_rails_tutorial_0/)
# 2章の所感
2章では，データベースやherokuを使います。この辺の連携や認証でかなりつまずいてしまいました…。
# データベースをmysqlへ
Ruby on Rails Tutorialでは，データベースにPostgreSQLを使っていますが，複数の記事でMySQLが推奨されていることや，職場でもMySQLが使用されていることから，MySQLを使用することにしました。
## Gemfile
### 削除するgem
* sqlite3
* pg
### 追加するgem
* mysql2
Gemfileを編集したら
```
bundle install
bundle update
```
します。
## mysqlでデータベースを作成
```
mysql -u root -p //まずはroot権限でログイン
```
パスワードを要求されるので，何も入力せずにEnter。初期設定ではパスワードが設定されていません。
```
create database toy_app;
```
データベースのテーブルやらなんやらは教材の指示に従えばOKです。
## config/database.ymlの設定
この辺から私にはややこしかったです。`config/database.yml`を書き換えます。ここには，データベースに関する設定が書かれています。どこまで信用できるかはわかりませんが，私の設定を書いてみます。
```
default: &default
  adapter: mysql2
  encoding: utf8
  reconnect: false 
  pool: 5
  timeout: 5000

development:
  <<: *default
  database: toy_app     //さっき設定したdatabase名
  user: root
  password:

test:                  //まだtestは使わないのでとりあえずこの状態で
  <<: *default

production:
  <<: *default
  url: <%= ENV['DATABASE_URL'] %>      //これ以降になにが書いてるかは後でわかります
  database: <%= ENV['DB_NAME'] %>
  user: <%= ENV['DB_USER'] %>
  password: <%= ENV['DB_PASSWORD'] %>
```
`default`, `development`, `test`, `production`の4つに別れていて，開発中に使う設定は`development`に，`heroku`にアップロードした後の本番環境で使う設定は`production`に書いてあります。`test`はこの時点ではあまり気にする必要がありません。`default`は全てに共通して設定したい項目です。
## `rails db:migrate`
とりあえず開発環境でのデータベースの設定が終わったので，
```
rails db:migrate
```
をします。ここでエラーが出る場合は，これまで設定した`Gemfile`, `gem mysql2`, `database.yml`を疑ってください。
## heroku
herokuでmysqlを使うための設定をしていきます。Qiitaにわかりやすい記事がたくさんあるので，この部分はお任せしちゃいます。

[Herokuへのデプロイ方法【Heroku+Rails+MySQL】](https://qiita.com/murakami-mm/items/9587e21fc0ed57c803d0)

補足として私がつまずいたことを記録しておきます。
### `heroku config`
`heroku config`では，`DATABASE_URL`を`mysql2`で始めることに注意します。
### SSLとherokuのstack
```
git push heroku main
```
すると，SSL認証に失敗したという旨のエラーが起きました。しかし，`cleardb`の無料プラン`ignite`では，SSL認証は使えません。`heroku-20`ではなく`heroku-18`に変更することで解決しました。（理由はいまいちわからない…。）
```
heroku stack set:heroku-18
```
