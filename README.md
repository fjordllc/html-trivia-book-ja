# html-trivia-book-ja

FBC Press 向け書籍『なぜ HTML はこうなったのか』の原稿リポジトリです。

本書は、プログラミングスクール [FjordBootCamp](https://bootcamp.fjord.jp/) の教材として作成しています。

## 構成

- `OUTLINE.md`: 節レベルの詳細目次
- `manuscript/`: 原稿本体
- `manuscript/SUMMARY.md`: 目次
- `manuscript/partX/`: 各部の導入・章
- `manuscript/appendix/`: 付録

## 編集方針

- `../FBC_Press` のルールを最優先にします
- 背景、仕様、実装、判断基準を一続きで説明します
- HTML を笑いものにせず、「なぜそうなったのか」を追います
- 半角英数字・英単語と日本語の間には半角スペースを入れます
- このルールは本文だけでなく、章見出し、部見出し、`manuscript/SUMMARY.md` の目次表記にも適用します
- ただし `第8章` `第1部` `付録A` のような日本語の番号ラベル内ではスペースを入れません

## FjordBootCamp

FjordBootCamp は、現役エンジニアが運営するオンラインのプログラミングスクールです。本書もその教材の一つとして、単なる暗記ではなく「なぜそうなっているのか」を理解する学習姿勢に合わせて作っています。

公式サイト:

- <https://bootcamp.fjord.jp/>

## ビルド

mdBook を前提にした構成です。必要に応じて `book.toml` を調整してください。
