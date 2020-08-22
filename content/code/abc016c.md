---
title: "ABC016-C"
date: 2020-08-19T12:09:33+09:00
draft: true

categories: ["Programming"]
tags: ["atcoder"]
author: "ebisenttt"
---
### 問題
[AtCoder ABC016 C](https://atcoder.jp/contests/abc016/tasks/abc016_3)
### 感想
とりあえずグラフを作ればいいことは分かったが，どう実装していいのか悩んだ。
考えた結果，以前「ワーシャルフロイド法」を使ったことを思い出した。
各頂点について，距離が2である別の頂点がいくつかあるか確かめれば良い。
公式解説も同じ趣旨だったので達成感。今回は解答は1つだけ。
解き終わるまで1時間くらいかかったけど…。
### 解答
[提出 #16034003](https://atcoder.jp/contests/abc016/submissions/16034003)
~~~
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <iomanip>
using namespace std;
#define REP(i, n) for(int i = 0; i < n; i++)
#define FOR(i, m, n) for(int i = m; i < n; i++)
#define ALL(x) (x).begin(),(x).end() //sortなどの引数を省略したい
#define SIZE(x) ((ll)(x).size()) //sizeをsize_tからllに直しておく
#define MAX(x) *max_element(ALL(x)) //最大値を求める
#define MIN(x) *min_element(ALL(x)) //最小値を求める
typedef long long ll;
typedef long double ld;
const int INF = 1e9;
int main(){
    int n,m;cin>>n>>m;
    vector<vector<int>> f(n), dis((n), vector<int> (n,INF));
    REP(i,m){
        int a, b;
        cin>>a>>b;
        a--, b--;
        f[a].push_back(b);
        f[b].push_back(a);
    }
    REP(i,n)dis[i][i]=0;
    REP(i,n)REP(j,SIZE(f[i]))dis[i][f[i][j]]=1;
    REP(k,n)REP(i,n)REP(j,n){
        if(dis[i][j]>dis[i][k]+dis[k][j])dis[i][j]=dis[i][k]+dis[k][j];
    }
    REP(i,n){
        int cnt=0;
        REP(j,n)if(dis[i][j]==2)cnt++;
        cout<<cnt<<endl;
    }
    return 0;
}
~~~
### 公式解説
[解説](https://www.slideshare.net/chokudai/abc016)