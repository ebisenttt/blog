---
title: "SoftBankAirのWi-fi通信速度を定期計測してみた（1/2）"
date: 2021-07-06T21:54:57+09:00
draft: true

tags: ["wifi", "softbank air", "Shell Script"]
---
# はじめに
光回線工事ができない賃貸物件のため，SoftbankAirを利用しています。「通信速度が遅い」という声が多く，あまり評判のよくないSoftbankAirについて，中長期的に通信速度を記録してみました。
# Softbank Airについて
Softbank Airとは何か，という説明は割愛します。SoftbankAirは，時間帯で速度制限がかかります。今回は，特に時間帯ごとの通信速度に着目しました。
# 測定の環境
* 物件: 鉄筋コンクリート2階建の1階
* 設置場所: 窓付近の床
* 使用ルータ: Airターミナル4（記事作成時の最新モデル）
* 公式サイトによる住所別下り最大速度: 962Mbps
* 使用PC: MacBook Ratina 2017
# 測定の方法
launchdで10分ごとにspeed-cliを実行し，標準出力の一部をテキストファイルに記録しました。
詳細なコードは以下の記事をご覧ください。

# 測定の結果

# 参考サイト