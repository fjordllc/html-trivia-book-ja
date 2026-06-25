# theme

このディレクトリは、mdBook の見た目や共通 UI の調整に使います。

## ファイル構成

- `mdbook-book-core.css`: `mdbook-book-jp` から導入した共通レイアウト層です。直接編集しません。
- `mdbook-book-jp.css`: `mdbook-book-jp` から導入した日本語書籍向けタイポグラフィ層です。直接編集しません。
- `html-trivia-book.css`: この本だけに必要な見た目調整を書くための書籍固有 CSS です。
- `textbook-footer.js`: 各ページ末尾に、FjordBootCamp 教材であることを示す短いフッターを挿入します。

## 役割分担

- 共通 CSS:
  - `mdbook-book-core.css`
  - `mdbook-book-jp.css`
- 書籍固有 CSS:
  - `html-trivia-book.css`
- 共通導線 JS:
  - `textbook-footer.js`

本文そのものに入れるべき情報は Markdown 原稿側で管理し、各ページで共通化したい短い導線だけを JavaScript で注入します。
