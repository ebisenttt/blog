---
title: "ABC015-C"
date: 2020-08-19T07:27:47+09:00
draft: false
---
AtCoder茶色を目指し，練習のためABCのC問題を全問AC，解説ACすることがとりあえずの目標。
今回はABC015のC問題を解いてみた。
### 問題
[AtCoder ABC015 C](https://atcoder.jp/contests/abc015/tasks/abc015_3)
### 感想
まず排他的論理和（XOR）をまともに勉強していなかったのでそこから。
さらに可変長配列の要素の組み合わせをどう作るかに手こずった。
最終的に`queue`に`vector`を`push`, `pop`することを繰り返す形にした。
`queue`の使い方にまだ慣れていないが自力で書けたことが少し嬉しい。
コメントアウトしているところは一度`WA`が出てしまい，`n`, `k`を最大値にしてみたため。
結局原因はそこではなく，配列の添字を間違えていただけだった。
### 解答
[提出#16031331](https://atcoder.jp/contests/abc015/submissions/16031331)
~~~
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <iomanip>
#include <queue>
using namespace std;
#define REP(i, n) for(int i = 0; i < n; i++)
#define FOR(i, m, n) for(int i = m; i < n; i++)
#define ALL(x) (x).begin(),(x).end() //sortなどの引数を省略したい
#define SIZE(x) ((ll)(x).size()) //sizeをsize_tからllに直しておく
#define MAX(x) *max_element(ALL(x)) //最大値を求める
#define MIN(x) *min_element(ALL(x)) //最小値を求める
typedef long long ll;
typedef long double ld;
int main(){
    ll n,k; cin>>n>>k;
    //ll n=5,k=5;
    vector<vector<ll>> v(n,vector<ll> (k));
    REP(i,n)REP(j,k)cin>>v[i][j];
    //REP(i,n)REP(j,k)v[i][j]=127;
    vector<vector<ll>> w;
    queue<vector<ll>> q;
    q.push({});
    while(!q.empty()){
        vector<ll> x=q.front();
        ll s=SIZE(x);
        if(s<n){
            REP(j,k){
                vector<ll> y=x;
                y.push_back(v[s][j]);
                q.push(y);
            }
            q.pop();
        }else{
            w.push_back(x);
            q.pop();
        }
    }
    string ans="Nothing";
    REP(i,SIZE(w)){
        ll a=0;
        REP(j,n){
            a^=w[i][j];
        }
        if(!a){ans="Found";break;}
    }
    cout<<ans<<endl;
    return 0;
}
~~~
### 公式解説
[解説](https://www.slideshare.net/chokudai/abc015)
### 解説を読んで
再帰関数で書けそうだということは，なんとなく想像できたが，まだ再帰関数に苦手意識がある。
ユークリッドの互除法くらいなら書けるが…。
さらに「深さ優先探索」は名前は知っているが，理解できていない。
案外Wikipediaの「再帰あり」の解説がわかりやすかったのでリンクを載せておく。

[Wikipedia 深さ優先探索](https://ja.wikipedia.org/wiki/深さ優先探索)

今回は訪問済みかどうかメモする必要がない。なぜなら質問の番号順，選択肢順に上からすべて訪問していけばいいから。
解説を参考に解答を書き直してみた（解答2）が，めちゃくちゃシンプルになった。
こういう名前がついたアルゴリズムは覚えていかないといけないなぁ。

### 解答2
[提出#16032134](https://atcoder.jp/contests/abc015/submissions/16032134)
~~~
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <iomanip>
#include <queue>
using namespace std;
#define REP(i, n) for(int i = 0; i < n; i++)
#define FOR(i, m, n) for(int i = m; i < n; i++)
#define ALL(x) (x).begin(),(x).end() //sortなどの引数を省略したい
#define SIZE(x) ((ll)(x).size()) //sizeをsize_tからllに直しておく
#define MAX(x) *max_element(ALL(x)) //最大値を求める
#define MIN(x) *min_element(ALL(x)) //最小値を求める
typedef long long ll;
typedef long double ld;

bool dfs(ll numq, ll value, ll n, ll k, vector<vector<ll>> v){
    if(numq==n)return(value==0);
    REP(i,k){
        if(dfs(numq+1,value^v[numq][i],n,k,v))return true;
    }
    return false;
}

int main(){
    ll n,k; cin>>n>>k;
    vector<vector<ll>> v(n,vector<ll> (k));
    REP(i,n)REP(j,k)cin>>v[i][j];
    ll numq=0, value=0;
    bool is=dfs(numq, value, n, k, v);
    string ans;
    if(is)ans="Found";
    else ans="Nothing";
    cout<<ans<<endl;
    return 0;
}
~~~