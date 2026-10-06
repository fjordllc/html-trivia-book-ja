# 第11章 属性値はなぜ省略できるのか

`disabled` だけでもボタンは無効になります。それなら `disabled="false"` と書けば有効になるでしょうか。HTML の属性では、構文と意味を分けて考える必要があります。

## 11.1 属性名だけなら値は空文字列

HTML には、値を明記せず属性名だけを書く構文があります。これは値が空文字列であることを表します。ブール属性専用の構文ではなく、たとえば `title` だけなら空の title 属性になります。ただし、その空文字列が適合する値か、どんな意味になるかは各属性の規則で決まります。

ブール属性は、存在すれば真、なければ偽です。

```html
<input type="checkbox" checked>
<input type="checkbox" checked="">
<input type="checkbox" checked="checked">
```

この三つは、いずれも初期状態でチェックの付いたチェックボックスです。checked は適用対象も決まっているため、type を省略したテキスト入力に付ける例では説明できません。

## 11.2 false という文字列は偽にならない

次のボタンは無効になります。

```html
<button disabled="false">送信</button>
```

disabled が存在するからです。ただし、この `false` はブール属性の適合する値でもありません。空文字列または属性名に一致する値を使います。無効化を解除するには disabled 属性を取り除きます。JavaScript なら `button.disabled = false` とすることで、その属性が除去されます。

一方、`contenteditable="false"` は編集不可を表します。contenteditable は列挙属性であり、ブール属性ではありません。「false と書いても効かない」という知識を、すべての属性へ広げてはいけません。

## 11.3 引用符の省略は値の省略とは違う

次の二つでは title の値は同じです。日本語であること自体は、引用符を必要とする理由ではありません。

```html
<a href="/about" title=会社概要ページ>会社概要</a>
<a href="/about" title="会社概要ページ">会社概要</a>
```

しかし ASCII スペースを入れると結果が変わります。

```html
<a href="/about" title=会社 概要>会社概要</a>
<a href="/about" title="会社 概要">会社概要</a>
```

最初の title は「会社」までで終わり、「概要」は別の属性名として読み取られます。意図した値を渡せるのは二つ目です。

引用符なしの属性値は空にできず、ASCII 空白、二重引用符、一重引用符、等号、小なり記号、大なり記号、バッククォートを含められません。全角スペースと ASCII スペースも構文上は同じ扱いではありません。境界を毎回判断するより、値を引用符で囲むほうが保守しやすくなります。

## 11.4 HTML とテンプレートの規則を混ぜない

XML としての XHTML では属性値を引用符で囲みます。React の JSX では `disabled={false}` の波括弧内は JavaScript の値です。HTML 文字列の `disabled="false"` とは違います。

省略可能という仕様上の条件と、チームで省略するかどうかは別の判断です。整形器で引用符を統一しても、HTML の規則に反しません。読める表記を選びつつ、トラブル時には属性が存在するか、その値が何か、属性の種類は何かを順に確認します。

次章では、このように異なる種類の規則を HTML 仕様書でどう探すかを見ます。

## 参考資料

* [HTML Living Standard: Attributes](https://html.spec.whatwg.org/multipage/syntax.html#attributes-2)
* [HTML Living Standard: Boolean attributes](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#boolean-attributes)
* [HTML Living Standard: The contenteditable content attribute](https://html.spec.whatwg.org/multipage/interaction.html#the-contenteditable-attribute)
* [React: Writing Markup with JSX](https://react.dev/learn/writing-markup-with-jsx)
