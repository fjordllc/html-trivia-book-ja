# 付録D 番外編 もっと深い HTML 雑学

本編に入れると話の筋から外れてしまうけれど、知ると HTML がもっと面白くなる「深掘り雑学」を集めました。どれも、現在のブラウザで実際に確かめられます。

## なぜ `<!DOCTYPE html>` と書くのか

HTML ファイルの先頭にある `<!DOCTYPE html>`。多くの人は「おまじない」として書いていますが、これにはちゃんと理由があります。しかも、見た目より変な事情を抱えています。

まず、この行は**もう「文書型の宣言」としてはほとんど意味を持っていません**。HTML5 では、`<!DOCTYPE html>` の唯一の仕事は、ブラウザを **Quirks Mode（互換モード）に入れないこと**です。

昔の DOCTYPE は、こんなに長いものでした。

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
```

誰も覚えられないので、みんなコピペしていました。HTML5 はこれを `<!DOCTYPE html>` まで短くしました。中身を理解させることをあきらめ、「Quirks Mode を切るスイッチ」と割り切ったのです。

では、DOCTYPE を書き忘れるとどうなるのか。ブラウザは **Quirks Mode** に入り、1990 年代の挙動をわざと再現します。とくに有名なのが**箱モデルの違い**で、Quirks Mode では `width` に指定した値の中に padding と border が含まれてしまいます。同じ CSS なのに、DOCTYPE の有無だけでレイアウトが静かにずれる——これが昔の Web 制作者を苦しめました。

ちなみにモードは 2 つではなく、`<!DOCTYPE html>` の「標準モード」、何もない「Quirks Mode」、その中間の「Limited-Quirks（ほぼ標準）モード」の 3 つがあります。`<!DOCTYPE html>` という短い呪文は、スキーマの宣言ではなく、互換性のスイッチだったわけです。

## `</script>` は文字列の中でも効いてしまう

`script` 要素の中身は、HTML パーサーにとって「生テキスト」です。パーサーは JavaScript の文法を理解しているわけではなく、最初に現れた `</script>` を見つけた瞬間にスクリプトの終わりだと判断します。

だから、次のコードは壊れます。

```html
<script>
  document.write("</script>");
</script>
```

人間には「`</script>` は文字列の中身」だと分かりますが、パーサーは文字列の途中でもおかまいなしに、最初の `</script>` でスクリプトを閉じてしまいます。回避するには、終了タグに見えないように書きます。

```html
<script>
  document.write("<\/script>");
</script>
```

`<\/script>` の `\/` は JavaScript では `/` と同じ意味なので、動作は変わりません。それでいて、HTML パーサーには `</script>` として見えなくなります。

## `&` を書くだけでは `&` と表示されないことがある

HTML で `&` は、特別な文字です。`&` は**文字参照**の始まりとして扱われるため、`&amp;` と書いてはじめて画面に `&` が出ます。同じように `<` は `&lt;`、`>` は `&gt;`、改行しない空白は `&nbsp;`、著作権マークは `&copy;`(©)で表します。

面白いのは、**一部の古い文字参照はセミコロンを付け忘れても表示される**ことです。たとえば `&copy` とだけ書いても、多くのブラウザは © を出します。ただしこれは互換性のための救済で、仕様上は parse error(問題のある入力)です。`&copy;` と正しく書くのが本筋です。

URL を書くときも要注意です。`?a=1&b=2` をそのまま属性値に書くと、`&b` が文字参照と解釈されかねません。HTML としては `?a=1&amp;b=2` と書くのが正確です。

## `<table>` の直下に書いたテキストは表の外へ飛ぶ

第5章で、表は行グループの入れ子構造だと見ました。では、その構造を無視して、`table` の直下にいきなりテキストを書いたらどうなるでしょうか。

```html
<table>おっと<tr><td>A</td></tr></table>
```

直感的には「`table` の中に "おっと" がある」と思いたくなります。ところが DevTools で DOM を見ると、こうなります。

```html
おっと
<table>
  <tbody>
    <tr><td>A</td></tr>
  </tbody>
</table>
```

**"おっと" は表の中ではなく、表の前へ追い出されます。** これは **foster parenting(里親付け)** と呼ばれる、HTML パーサーの正式な動作です。表の中に置けないものが来たとき、パーサーはそれを捨てず、表の直前へ「里子に出す」のです。

<figure>
<img src="../figures/fig-d-1.svg" alt="table の直下に書いたテキストが、DOM では table の中ではなく table の直前へ移動する様子の図">
<figcaption>図 D-1　表の中に置けないテキストは、表の前へ追い出される。</figcaption>
</figure>

第4章から第7章で見た補完やエラー回復は、ふわっとした「親切」ではなく、こうした名前の付いた規則(パーサーの挿入モードという状態機械)の集まりでした。foster parenting は、その機械じかけがいちばん見えやすい瞬間です。手元のブラウザで、ぜひ DevTools を開いて確かめてみてください。

## 参考資料

* [HTML Living Standard: The DOCTYPE](https://html.spec.whatwg.org/multipage/syntax.html#the-doctype)
* [MDN Web Docs: Quirks Mode and Standards Mode](https://developer.mozilla.org/ja/docs/Web/HTML/Guides/Quirks_Mode_and_Standards_Mode)
* [HTML Living Standard: Restrictions for contents of script elements](https://html.spec.whatwg.org/multipage/scripting.html#restrictions-for-contents-of-script-elements)
* [HTML Living Standard: Named character references](https://html.spec.whatwg.org/multipage/named-characters.html)
* [HTML Living Standard: Foster parenting](https://html.spec.whatwg.org/multipage/parsing.html#foster-parent)
