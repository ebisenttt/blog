---
title: "Hugoで作ったブログ記事をGithubにdeployする"
date: 2020-08-30T17:01:12+09:00
draft: false

tags: ["hugo", "github"]
---
## はじめに
このブログの記事作成の際は，Hugoで書いた記事をGithubPagesにデプロイしています。書いてからデプロイする作業が多少面倒だったので，これを簡単にする手順をまとめてみます。

## これまでの手順
hugoで記事作成ができたら，下の手順を踏んでいました。

```
hugo
```

で`.md`ファイルから`.html`ファイルを生成し，

```
git add .
```

で記事の'.md'ファイルをインデックスに追加し，

```
git commit -m "メモ"
```

でインデックスのファイルをローカルリポジトリにコミットし，

```
git push origin master
```

でローカルリポジトリをリモートリポジトリの`master`ブランチに`push` する。

こんな感じです。毎回タイプするのが以外と面倒。最初の`hugo`を忘れてしまうことがあります。また，ちょっとした修正をしたいだけのときは特に面倒です。

## 簡単にした手順
`deploy.sh`というファイルを作業ディレクトリ直下に作っておいて，上の4つの手順をこのファイルに予め書いておきます。ファイルの中身は下の通りです。

今回は，`hugo`で生成された`html`ファイルのみを`push`したいので，`cd docs`としています。

```
#!/bin/bash1

echo -e "\033[0;32mDeploying updates to GitHub...\033[0m"

# Build the project.
hugo # if using a theme, replace with `hugo -t <YOURTHEME>`

# Go To Public folder
cd docs
# Add changes to git.
git add .

# Commit changes.
msg="rebuilding site `date`"
if [ $# -eq 1 ]
  then msg="$1"
fi
git commit -m "$msg"

# Push source and build repos.
git push origin master

# Come Back up to the Project Root
cd ..
```
### 権限設定が必要
あとはコマンドラインで

```
./deploy.sh
```

と打てばOK，と思いきや

```
permission denied
```

許可されなかったと。権限の設定が必要です。

ターミナルで次のコマンドを実行します。

```
chmod +x deploy.sh
```

これで権限が与えられました。今度こそ

```
./deploy.sh
```

を実行すれば，記事の生成からリモートリポジトリへの`push`まで行ってくれます。

## 参考サイト
[Git初心者に捧ぐ！Gitの「これなんで？」を解説します|KRAY](https://kray.jp/blog/git-why-explanation/)

Gitについてイラスト付きで解説されています。

[シェルスクリプトを使う前に](https://qiita.com/sanstktkrsyhsk/items/ef88ddfb9fa8e7306e45)

権限設定についてはこちらを参考にしました。

[Host on GitHub](https://gohugo.io/hosting-and-deployment/hosting-on-github/)

`deploy.sh`の内容はこちらを参考にしました。公式ドキュメントです。