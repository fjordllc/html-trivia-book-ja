# なぜ HTML はこうなったのか スタイルガイド

このファイルは、FBC Press 共通ガイドをこの本向けに具体化したものです。共通ルールは `../FBC_Press/STYLE_GUIDE.md` を優先し、このファイルでは本書固有の前提だけを定義します。

## 版の前提

- 確認日: 2026-06-25
- 仕様の主軸: `HTML Living Standard`
- 歴史的な比較対象:
  - HTML 4.01
  - XHTML 1.0 / XHTML 1.1
  - HTML5 という語が広く使われていた時期の議論

## この本で重視すること

- HTML を奇妙な遺物として消費しない。
- 「変な仕様」より「そうならざるをえなかった理由」を主役にする。
- ブラウザの寛容さを、甘さではなく互換性責務として説明する。
- Rails エンジニアやフロントエンド初中級者が、実務の違和感を歴史と仕様で説明できる状態を目指す。

## この本の章で必ずやること

- 章の冒頭で、その章の主張を 1 文で言い切る。
- 具体例は 1 つで済ませず、前の例を踏まえて積み上げる。
- 少なくとも 1 箇所で「読者が実務でどこでつまずくか」に着地させる。
- 誤解されやすい通説を、その章の中で明示的に潰す。
- 章末では、次章へ何を渡すかを 1 文で示す。

## この本で避けること

- 「HTML は適当だから」で説明を終えること。
- ブラウザを擬人化しすぎて、仕様上の規則をぼかすこと。
- `HTML5` という語で、歴史上のラベルと現行仕様を雑に混ぜること。
- 「昔はダメだったが今は正しい」のように、歴史を単線的に裁くこと。
- Web 制作の常識を、そのまま仕様上の規則として書くこと。

## 言語ラベル

- HTML の例は `html`
- CSS の例は `css`
- JavaScript の例は `js`
- 擬似コードや階層図は `text`

## 確認済みの基準URL

- HTML Living Standard: <https://html.spec.whatwg.org/>
- WHATWG FAQ: <https://whatwg.org/faq>
- MDN HTML: <https://developer.mozilla.org/ja/docs/Web/HTML>
- W3C Web Architecture: <https://www.w3.org/TR/webarch/>
- Tim Berners-Lee 1989 Proposal: <https://www.w3.org/History/1989/proposal.html>
