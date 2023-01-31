---
title: "VSCODEのterminalの配色テーマをコピペできるサイト「Base16 Terminal Colors」が便利だった話"
date: 2023-01-09T15:03:01+09:00
draft: true
---

## はじめに
ショートカット`ctrl + l`で表示されるterminalのデフォルトカラーテーマがビビットすぎて気に入っていなかったので変えたかった。変える方法と便利なツールをメモしておく。

## Base16 Terminal Colors
[Base16 Terminal Colors](https://glitchbone.github.io/vscode-base16-term/#/3024)が便利。
1. 気に入ったテーマを選んで，「Copy to clipboard」をクリック
2. VSCODEで`setting.json`を開いて`workbench.colorCustomizations`に貼り付ける（以下の例は「Chalk」というテーマです）。
```json
"workbench.colorCustomizations": {
    "terminal.background":"#151515",
    "terminal.foreground":"#D0D0D0",
    "terminalCursor.background":"#D0D0D0",
    "terminalCursor.foreground":"#D0D0D0",
    "terminal.ansiBlack":"#151515",
    "terminal.ansiBlue":"#6FC2EF",
    "terminal.ansiBrightBlack":"#505050",
    "terminal.ansiBrightBlue":"#6FC2EF",
    "terminal.ansiBrightCyan":"#12CFC0",
    "terminal.ansiBrightGreen":"#ACC267",
    "terminal.ansiBrightMagenta":"#E1A3EE",
    "terminal.ansiBrightRed":"#FB9FB1",
    "terminal.ansiBrightWhite":"#F5F5F5",
    "terminal.ansiBrightYellow":"#DDB26F",
    "terminal.ansiCyan":"#12CFC0",
    "terminal.ansiGreen":"#ACC267",
    "terminal.ansiMagenta":"#E1A3EE",
    "terminal.ansiRed":"#FB9FB1",
    "terminal.ansiWhite":"#D0D0D0",
    "terminal.ansiYellow":"#DDB26F"
  }
```
3. 綺麗になった

## おわりに
こういうちょっとした便利ツール作って公開したい。

## 参考サイト

[VisualStudioCodeのターミナルの配色を変える-MemoriaE](https://memoriae.mattune.jp/2020/03/05/vscode-terminal-color/)
