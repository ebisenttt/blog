---
title: "DFSとBFSの実装方法と使い分け"
date: 2023-08-27T10:50:44+09:00
draft: false
---
## 目的
- DFSとBFSの実装方法をまとめる
- queueを使った方法と再帰関数を使った方法の差をまとめる
- DFSとBFSの使い分け型をまとめる

## 結論
- BFSは距離（コスト）が小さい順に探索するため，距離更新=距離確定
- BFS, DFSはあくまで解法の型. いつ距離を更新するか，どのようにデータを保持するかは問題によるので応用が必要．

## BFSとDFS
### BFS
- 幅優先探索
- スタート地点から近い（通る辺が少ない）順に探索する
#### 特徴
- 「スタート地点からの通る辺が少ない順に探索する」ことにより，下記の場合に距離が更新される
  - スタート地点からの距離が計算されていない場合
  - 通る辺は多いけど距離が短い経路が見つかった場合
    - 辺の長さが固定されている場合はこれが起きない．つまり「探索済み」=「最短距離確定済み」となる．よって「探索済みか」=「距離が初期値から更新されているか」で管理できる．
    - 辺の長さが0または1のとき0-1BFSを使って解くことができる．
    - 辺の長さが非負の場合は優先度付きqueueを用いるダイクストラ法を使って解く．

### DFS
- 深さ優先探索
- スタート地点から葉に達するまで探索する．葉に到達したとき，または探索できる頂点がなくなったとき，1つ前の頂点に戻る．
#### 特徴
- 再帰関数で書かれる事が多い（ベースケースに到達するまで同じ構造の関数を呼び続ける実装がしやすいから？）．
- 深さ優先探索でなければいけないという場合は少ない？（結果的に再帰関数を書きたい人はDFS, queueで解きたい人はBFSになっているだけ説．DPで代替されていることも多い．）

## 与えられるグラフのパターン
1. 頂点iから頂点jへの辺があり，長さが与えられている
  
    頂点iからの辺が出ている頂点のリスト（1次元）を各頂点に対して用意する（2次元）．

    木，無向グラフ，有向グラフなど様々．

2. HxWの格子状の地図が与えられ，頂点(i,j),頂点(s,t)間を移動可能な条件が与えられている．
 
    移動可能か，距離はいくつかについては，地図を見て判断する．

    マップ型と呼ぶことにする．

### 例題
1. 幅優先探索，マップ型，距離固定，始点・終点固定 [ABC007-C問題-幅優先探索](https://atcoder.jp/contests/abc007/submissions/44995145)
2. 幅優先探索，木構造，距離固定，始点・終点固定 [ABC270-C問題-Simple path](https://atcoder.jp/contests/abc270/tasks/abc270_c)
3. 幅優先探索，木構造，距離固定，始点・終点任意，塗り分け [ABC146-D問題-Coloring Edges on Tree](https://atcoder.jp/contests/abc146/tasks/abc146_d)
4. 幅優先探索，マップ型，距離固定，始点・終点任意 [ABC151-D問題-Maze Master](https://atcoder.jp/contests/abc151/tasks/abc151_d)
5. 幅優先探索，無向グラフ，距離固定，始点固定，経路復元 [ABC168-D問題-..(Double Dots)](https://atcoder.jp/contests/abc168/tasks/abc168_d)
6. 01-BFS，マップ型，距離0-1，始点・終点固定 [ABC176-D問題-Wizard in Maze](https://atcoder.jp/contests/abc176/tasks/abc176_d)
7. 幅・深さ優先探索，無向グラフ（一直線），始点固定 [ABC209-D問題-Collision](https://atcoder.jp/contests/abc209/tasks/abc209_d)
8. 幅優先探索，無向グラフ，始点・終点固定，経路カウント[ABC211-D問題-Number of Shortest paths](https://atcoder.jp/contests/abc211/tasks/abc211_d)
9. 深さ・幅優先探索，マップ型，始点・終点固定 [ATC001-A問題-深さ優先探索](https://atcoder.jp/contests/atc001/tasks/dfs_a)
10. 深さ優先探索 [ABC029-C問題-Brute-force Attack](https://atcoder.jp/contests/abc029/tasks/abc029_c)
11. 深さ・幅優先探索，重みなし無向グラフ，始点固定 [ABC054-C問題-One-stroke Path](https://atcoder.jp/contests/abc054/tasks/abc054_c)
12. 深さ・幅優先探索，文字列列挙 [ABC114-C問題-755](https://atcoder.jp/contests/abc114/tasks/abc114_c)
13. 深さ・幅優先探索，DP [ABC233-C問題-Product](https://atcoder.jp/contests/abc233/tasks/abc233_c)
14. 01-BFS，マップ型，始点・終点固定，二分探索 [ABC020-C問題-壁抜け](https://atcoder.jp/contests/abc020/tasks/abc020_c)
15. 幅優先探索，無向グラフ，始点・終点固定 [ABC021-C問題-正直者の高橋くん](https://atcoder.jp/contests/abc021/tasks/abc021_c)
16. 幅優先探索，始点・終点任意，メモ化再帰 [ABC037-D問題-経路](https://atcoder.jp/contests/abc037/tasks/abc037_d)
    
    幅優先探索ではあるが，どこを始点とするか，どの順序で探索するかについて考察する難易度がある程度高く，実装方法も他の問題とは異なる
17. 深さ・幅優先探索，始点・終点任意 [ABC049-D問題-連結](https://atcoder.jp/contests/abc049/tasks/arc065_b)

    深さ優先探索でも解けるが，UnionFindのほうが単純？連結部分を求めたあとの実装方法のほうが発想が必要だった．
18. 深さ・幅優先探索，始点固定，木構造 [ABC070-D問題-Transit Tree Path](https://atcoder.jp/contests/abc070/tasks/abc070_d)

    木構造なので距離の更新が起きない．よってダイクストラ法でなく深さ，幅優先探索でもOK．

19. 幅・深さ優先探索，始点固定（でよい），木構造 [ABC126-D問題-Even Relation](https://atcoder.jp/contests/abc126/tasks/abc126_d)
20. 幅・深さ優先探索，始点固定（でよい），木構造 [ABC138-D問題-Ki](https://atcoder.jp/contests/abc138/tasks/abc138_d)
21. 幅・深さ優先探索，始点・終点固定 [ABC184-E問題-Third Avenue](https://atcoder.jp/contests/abc184/tasks/abc184_e)
22. 幅・深さ優先探索，マップ型，始点・終点固定 [第三回PAST過去問-G問題-グリッド金移動](https://atcoder.jp/contests/past202005-open/tasks/past202005_g)


以下の問題は参考サイトでは幅・深さ優先探索に分類されていたが，解説では他の解法だったもの
1. ダイクストラ法，往復経路 [ABC035-D問題-トレジャーハント](https://atcoder.jp/contests/abc035/tasks/abc035_d)
2. DP [ABC185-E問題](https://atcoder.jp/contests/abc185/tasks/abc185_e)

## 参考
[AtCoderの問題を分類しました【計算量・データ構造・アルゴリズム】](https://zenn.dev/koyanagihitoshi/books/atcoder-classification-4)

[AtCoder 問題カテゴリー分類](https://qiita.com/c-yan/items/56a051d826b873b4f78d)