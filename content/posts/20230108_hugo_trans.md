---
title: "Hugoの環境移行でつまづいた"
date: 2023-01-08T13:40:16+09:00
draft: false
---

## 起きた問題
- `hugo server`をたたいてアクセスするも"Page not found"と表示される
- `hugo new posts/hoge.md`をたたいても"Error: no existing content directory configred for this project"と表示され`.md`ファイルが作成されない

## 対処法
1. `git submodule --init --recursive`を実行
2. `config.toml`の以下の項目を設定
    ```toml
    archetypesDir = "archetypes"
    publishDir = "public"
    contentDir = "content"
    ```
3. ディレクトリ`archetypes`を作成
4. ディレクトリ`archetypes`内に下記のファイル`default.md`を作成
   ```markdown
    ---
    title: "{{ replace .Name "-" " " | title }}"
    date: {{ .Date }}
    draft: true
    ---
   ```
5. ディレクトリ`content`を作成（またはディレクトリ名変更）
6. ディレクトリ`public`を作成（またはディレクトリ名変更）

## 補足
最後に更新してからアップデートが入っていたことと，MacBookAir2017からM2MacBookAirに変えて色々と環境が変わったことが原因かと予想していますが，本質的なことは調べてません。逆に以前の環境ではデフォルトのディレクトリ構成ではないのに`config.toml`がちゃんと設定されていなくても動いていたのが謎。

## おまけ
HugoがLive Reloadに対応していたことを知って快適になった。

## 参考サイト
[Hugo ビルドエラー対応 found no layout file - infraya.work](https://infraya.work/posts/hugo_mypage_git_clone_error/)