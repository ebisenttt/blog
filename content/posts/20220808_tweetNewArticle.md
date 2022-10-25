+++
title =  "TwitterAPI で新しいブログの記事を自動で投稿したい"
date = "2022-08-08T17:11:26+09:00"
tags = ["Twitter"]
+++

ほとんど見られることがないブログとは知りつつも，更新したことすら知られることがないのは虚しいので，Twitter で更新したことを投稿するくらいは許されるだろうと思いました。ただ，毎回ツイートするのは面倒なので自動化したい。でもどうやるの？ということでこの記事に作業の記録を残します。

## TwitterAPI の申請

このサイトで誘導されるがままに申請したら5分くらいで手続きが終わりました。

[Twitter API](https://developer.twitter.com/en/docs/twitter-api)

## TwitterAPI の設定
設定に少し手間取ったので，注意事項を残しておきます。

### v1.1 ではなく v2 を使うこと
v1.1 は Elavated access を有効にしないと使えません。v2 では Essential access を使えます（デフォルトで有効）。手間が多少増えるので，v2 を使っておくのが無難でしょう。
### 公式のドキュメントを読むこと
v1.1 と v2 では使用が大きく異なります。ググって出てきた技術系のブログを参考にして OAuth の設定をすると，バージョンが違ってエラー吐かれまくります。改めてどんなサービスでも公式の docs を読んだ方がいいということを実感しました。
### Authentication の設定(任意)
デフォルトでは`GET`メソッドしか許可されていません。Dash BoardでUser authentication settingsを変更することで`POST`メソッドが許可されます。

## HUGO の仕様

自分の場合は，次のような順序で記事を作成します:

1. `hugo new article/[name].md`で記事のテンプレート`content/article/[name].md`を作成
2. `content/article/name.md`にマークダウンで記事を書く
3. `hugo`で記事をコンパイルし`docs/article/[name]/index.html`を作成
4. リモートリポジトリに`push`

なお，3 と 4 についてはシェルスクリプトで既に自動化しています。

## OGP の設定

OGP とは，Open Graph Protcol の略で，SNS 上でリンクが共有されたときに表示されるカードの設定として使われるプロトコルです。このサイトで使用しているテーマでは，次のような設定でした。

```html
<meta property="og:title" content="{{ .Scratch.Get "title" }}">
<meta property="og:description" content="{{ .Scratch.Get "description" }}">
<meta property="og:image" content="{{ .Scratch.Get "image" | absURL }}">
<meta property="og:url" content="{{ .Permalink | absURL }}">
<meta property="og:site_name" content="{{ .Site.Title }}">
{{- if .IsPage }}
<meta property="og:type" content="article">
{{- else -}}
<meta property="og:type" content="website">
{{- end }}
```
この`{{ }}`で囲まれたコードの部分にだいぶ苦しめられましたが，`themes/bilberry-hugo-theme/layouts/_default/baseof.html`と`config.toml`を編集してとりあえず正常に表示されるようになりました。

## APIを利用するpythonスクリプト
文字列の操作とか組み込みのメソッドが多くて楽ができるpythonを選択しました。
1. `git diff --name-only --cached --diff-filter=A`で新規のファイル名を取得
2. 記事のHTMLファイルの保存先の`docs`内のフォルダのみに絞り込む
3. ファイル名でファイルを指定し，プラグインBeautifulSoup4を使って`<title>`タグ内の文字列（記事のタイトル）を取得
4. `tweepy`で記事名を投稿

コードは次のとおりです
```python
import subprocess
from subprocess import PIPE
import bs4
import re
import tweepy
import os
from dotenv import load_dotenv

def main():
	new_article_arr = get_new_article_path_list()
	if not len(new_article_arr):
		print("Complite: No new article is detected")
		return
	for path in new_article_arr:
		title = get_article_title(path)
		print("New article title is", title)
		api = make_api()
		tweet_text = "新しい記事を投稿しました:\n" + title + "\n"
		result = api.create_tweet(text=text)
		print(result)
	return

def convert_title(string):
	string = re.sub('\n', '', string)
	string = re.sub('\s', '', string)
	string = string.replace("&vert", "|")
	return string

def get_new_article_path_list():
	COMMAND = "git diff --name-only --cached --diff-filter=A"
	process = subprocess.run(COMMAND, shell=True, stdout=PIPE, stderr=PIPE, text=True)
	path_text = process.stdout
	path_arr = path_text.split("\n")[:-1]
	path_arr_of_new_article = list(
		filter(
			lambda path: path.startswith("docs/article"),
			path_arr
		))
	return path_arr_of_new_article

def get_article_title(path):
	soup = bs4.BeautifulSoup(open(path), "html.parser")
	title = convert_title(soup.title.string)
	return title

def make_api():
	API_KEY = os.environ["TWITTER_API_KEY"]
	API_KEY_SECRET = os.environ["TWITTER_API_KEY_SECRET"]
	ACCESS_TOKEN = os.environ["TWITTER_API_ACCESS_TOKEN"]
	ACCESS_TOKEN_SECRET = os.environ["TWITTER_API_ACCESS_TOKEN_SECRET"]

	client = tweepy.Client(
		consumer_key=API_KEY,
		consumer_secret=API_KEY_SECRET,
		access_token=ACCESS_TOKEN,
		access_token_secret=ACCESS_TOKEN_SECRET
	)
	return client

if __name__ == "__main__":
	load_dotenv()
	main()
```