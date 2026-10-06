# 第16章 バグはなぜ残るのか

「変な挙動だから直せばよい」と思っても、その挙動を前提にしたページがあると簡単には変えられません。ただし、互換性のために残った挙動を、すべて未修正のバグと呼ぶのも不正確です。`document.all` は、その境界をよく示します。

## 16.1 存在するのに false になるオブジェクト

ブラウザのページ上で、次の式を DevTools のコンソールへ一つずつ入力してみます。Node.js など、document のない環境の例ではありません。

```js
Boolean(document.all)          // false
typeof document.all           // "undefined"
document.all == null          // true
document.all === undefined    // false
```

通常のオブジェクトなら真偽値への変換は true になるはずです。しかし document.all は、要素のコレクションを返すにもかかわらず、このような特別な振る舞いをします。

最後の厳密等価比較が false であることからも、単に undefined が返っているのではないと分かります。値がないのではなく、特定の判定で「ない」ように見せる例外なのです。

## 16.2 古いブラウザ判定と共存するための例外

document.all は Internet Explorer 由来の古い API です。かつては、この API の有無をブラウザ判定にも使うコードがありました。

```js
if (document.all) {
  // 古い IE 向けの処理を選ぶつもりの分岐
}
```

互換性のため API を実装すると、今度はこのような分岐で IE 向け処理へ入る問題が生じます。API を使うコードとの互換性と、判定に使うコードとの互換性が衝突するのです。

現在の HTML Standard は document.all のコレクションに特別な内部スロット `[[IsHTMLDDA]]` を持たせます。ECMAScript の Web ブラウザ向け追加規定は、それに対する真偽値変換、typeof、緩い等価比較を例外扱いします。JavaScript と HTML の両方にまたがって、互換動作が明文化されています。

## 16.3 未修正の不具合とは区別する

この挙動は奇妙ですが、現在では仕様に書かれた互換性の例外です。「現行仕様に違反するバグを放置している」という説明では合いません。既存の利用が、何を仕様どおりとするかにも影響した例として読む必要があります。

一方、すべての不具合がこのように固定されるわけではありません。変更の影響を調べて修正できるものもあれば、使われていない機能を削除できる場合もあります。残っている理由を判断するには、現在の規定と、変更の議論や実装記録を照合します。

## 16.4 新しいコードは必要な機能を調べる

新しく書くコードで document.all を使ったブラウザ判定をまねる必要はありません。要素を探すなら `getElementById` や `querySelector` を使い、機能の利用可否を判定するなら必要な API 自体を調べます。

「このブラウザなら動くだろう」という名前による推測を減らすことは、新しい互換性の負担を増やさないためにも有効です。ただし API の存在確認だけで、すべての操作やアクセシビリティが保証されるわけではありません。[第26章](../part7/chapter26.md)では、標準機能を採用する際の確認へ進みます。

## 参考資料

* [HTML Living Standard: document.all](https://html.spec.whatwg.org/multipage/obsolete.html#dom-document-all)
* [ECMAScript: IsHTMLDDA 内部スロット](https://tc39.es/ecma262/multipage/additional-ecmascript-features-for-web-browsers.html#sec-IsHTMLDDA-internal-slot)
