#!/usr/bin/env python3
"""『なぜ HTML はこうなったのか』の図版生成（自作 SVG）。
ASSET_RULES / FIGURE_GUIDE に従い、全図の定義をここに集約する。
出力: manuscript/assets/fig-*.svg
方針:
  - 1 図 1 主張／図中の用語は本文と一致／色だけに依存しない（形・ラベル・矢印で区別）。
  - 図番号とキャプションは本文（figcaption）側に置き、SVG には焼き込まない。
  - フォントは sans-serif（コード片のみ monospace）。配色は固定パレットの役割で決める。
共通スタイル・パレットは why-programmers-think-textbook-ja/scripts/figures/build_all.py に倣う。
"""
import html, pathlib

ASSETS = pathlib.Path(__file__).resolve().parents[2] / "manuscript/assets"
ASSETS.mkdir(parents=True, exist_ok=True)

# 固定パレット（FIGURE_GUIDE の役割別カラー）
INK="#1f2933"; SUB="#52606d"; ACC="#3a6ea5"; DANGER="#b23a48"
NEUT="#eef1f5"; BLUE="#dce9f2"; WARM="#f4e9dc"; LINE="#b8c2cc"
WARM_ST="#c9a26b"; DANGER_FILL="#f6e7e9"; DANGER_ST="#c9727f"

def esc(s): return html.escape(str(s), quote=True)

def head(w,h,aria):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
            f'font-family="sans-serif" role="img" aria-label="{esc(aria)}">',
            '<defs>'
            f'<marker id="ar" markerWidth="10" markerHeight="10" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="{ACC}"/></marker>'
            f'<marker id="arg" markerWidth="10" markerHeight="10" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="{SUB}"/></marker>'
            '</defs>']

def rect(x,y,w,h,fill="#fff",stroke=LINE,rx=0,sw=1.2,dash=None):
    d=f' stroke-dasharray="{dash}"' if dash else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'

def txt(x,y,s,size=16,fill=INK,anchor="start",weight="normal",mono=False):
    fam=' font-family="ui-monospace,monospace"' if mono else ''
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{weight}" fill="{fill}"{fam}>{esc(s)}</text>'

def ln(x1,y1,x2,y2,stroke=ACC,sw=2,marker=None,dash=None):
    m=f' marker-end="url(#{marker})"' if marker else ''
    d=f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"{m}{d}/>'

def circ(cx,cy,r,fill,stroke="none",sw=1):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

def save(name,p):
    p.append('</svg>')
    (ASSETS/name).write_text("\n".join(p),encoding="utf-8")
    print("wrote",name)

# ---------------------------------------------------------------- fig-2-1
def fig_2_1():
    W,H=920,230
    p=head(W,H,"URL は場所、HTTP は取得方法、HTML は中身の構造という 3 つの役割を並べた図")
    cols=[(40,"URL","どこにあるか","/beam-status.html","場所の名前"),
          (330,"HTTP","どう取りに行くか","GET /...","取得の手順"),
          (620,"HTML","中身はどんな構造か",'<a href="...">',"参照・見出し・本文")]
    for x,big,q,ex,note in cols:
        cx=x+130
        p+=[rect(x,30,260,170,BLUE if big=="HTML" else NEUT,ACC if big=="HTML" else LINE,rx=14),
            txt(cx,82,big,26,ACC,"middle","bold"),
            txt(cx,120,q,16,INK,"middle","bold"),
            txt(cx,152,ex,14,SUB,"middle",mono=True),
            txt(cx,180,note,13,SUB,"middle")]
    save("fig-2-1.svg",p)

# ---------------------------------------------------------------- fig-4-1
def fig_4_1():
    W,H=920,300
    p=head(W,H,"html/head/body を書いていないソースから、ブラウザがそれらを補完した DOM の木を組み立てる流れの図")
    # source
    p+=[txt(40,36,"あなたが書いたソース",15,SUB,weight="bold"),
        rect(40,48,300,120,"#fff",LINE,rx=12),
        txt(60,86,"<title>sample</title>",14,INK,mono=True),
        txt(60,116,"<p>Hello</p>",14,INK,mono=True),
        txt(60,150,"※ html / head / body は書いていない",12,SUB)]
    # arrow
    p+=[ln(360,108,436,108,ACC,2.5,"ar"),txt(398,96,"解釈・補完",13,ACC,"middle","bold")]
    # DOM
    p+=[txt(470,36,"ブラウザが作った DOM",15,SUB,weight="bold"),
        rect(470,48,410,242,"#fff",LINE,rx=12)]
    def node(x,y,s): return txt(x,y,s,14,ACC,"middle","bold",mono=True)
    p+=[node(660,92,"html"),
        ln(660,100,566,124,LINE,1.5),ln(660,100,754,124,LINE,1.5),
        node(566,132,"head"),node(754,132,"body"),
        ln(566,140,566,166,LINE,1.5),ln(754,140,754,166,LINE,1.5),
        node(566,182,"title"),node(754,182,"p"),
        ln(566,190,566,216,LINE,1.5),ln(754,190,754,216,LINE,1.5),
        txt(566,236,'"sample"',13,INK,"middle",mono=True),
        txt(754,236,'"Hello"',13,INK,"middle",mono=True),
        txt(660,268,"html / head / body は補完された",13,ACC,"middle","bold")]
    save("fig-4-1.svg",p)

# ---------------------------------------------------------------- fig-5-1
def fig_5_1():
    W,H=920,300
    p=head(W,H,"tbody を書いていない表のソースから、ブラウザが table と tr のあいだに tbody を補完した DOM を作る流れの図")
    p+=[txt(40,36,"ソース（tbody なし）",15,SUB,weight="bold"),
        rect(40,48,300,120,"#fff",LINE,rx=12),
        txt(60,84,"<table>",14,INK,mono=True),
        txt(78,112,"<tr><td>A</td></tr>",14,INK,mono=True),
        txt(60,140,"</table>",14,INK,mono=True),
        ln(360,108,436,108,ACC,2.5,"ar"),txt(398,96,"補完",13,ACC,"middle","bold")]
    p+=[txt(470,36,"DOM",15,SUB,weight="bold"),
        rect(470,48,410,242,"#fff",LINE,rx=12)]
    def node(x,y,s,fill=ACC): return txt(x,y,s,14,fill,weight="bold",mono=True)
    p+=[node(500,90,"table"),
        ln(516,98,548,120,LINE,1.5),
        rect(548,106,150,26,WARM,WARM_ST,rx=6),node(560,124,"tbody"),
        txt(712,124,"← 補完された",13,ACC,weight="bold"),
        ln(566,132,596,158,LINE,1.5),node(596,176,"tr"),
        ln(608,184,636,208,LINE,1.5),node(636,226,"td"),
        ln(662,222,700,222,LINE,1.5),txt(710,226,'"A"',13,INK,mono=True)]
    save("fig-5-1.svg",p)

# ---------------------------------------------------------------- fig-6-1
def fig_6_1():
    W,H=920,270
    p=head(W,H,"p の中に div を書いたソースから、ブラウザが div の直前で p を閉じ、div を p の外に置いた DOM を作る流れの図")
    p+=[txt(40,36,"ソース（p を閉じていない）",15,SUB,weight="bold"),
        rect(40,48,320,96,"#fff",LINE,rx=12),
        txt(58,88,"<p>前置き",14,INK,mono=True),
        txt(58,116,"<div>本文</div>",14,INK,mono=True),
        ln(380,100,456,100,ACC,2.5,"ar"),txt(418,88,"解釈",13,ACC,"middle","bold")]
    p+=[txt(490,36,"DOM（p と div は兄弟）",15,SUB,weight="bold"),
        rect(490,48,390,180,"#fff",LINE,rx=12)]
    def node(x,y,s): return txt(x,y,s,14,ACC,weight="bold",mono=True)
    p+=[node(520,92,"p"),ln(528,98,556,120,LINE,1.5),txt(556,126,'"前置き"',13,INK,mono=True),
        node(520,166,"div"),ln(534,172,562,190,LINE,1.5),txt(562,196,'"本文"',13,INK,mono=True),
        txt(660,92,"← p はここで閉じた",13,SUB),
        txt(660,166,"← div は p の外へ",13,SUB)]
    save("fig-6-1.svg",p)

# ---------------------------------------------------------------- fig-14-1
def fig_14_1():
    W,H=300+560,300
    W=900
    p=head(W,H,"同じ閉じ忘れの入力に対し、HTML は回復して文書を表示し、XML として扱う XHTML は処理を止めてエラー画面を出す対比の図")
    # shared input
    p+=[txt(40,50,"壊れた入力（閉じ忘れ）",15,INK,weight="bold"),
        rect(40,62,230,60,"#fff",LINE,rx=10),
        txt(56,98,"<p>前置き <div>本文",13,SUB,mono=True),
        ln(280,92,326,92,SUB,2,"arg")]
    # HTML column (望ましく動く側 = ACC/BLUE)
    p+=[rect(350,62,250,200,BLUE,ACC,rx=14),
        txt(475,96,"HTML",18,ACC,"middle","bold"),
        txt(475,132,"回復して読み進める",15,INK,"middle","bold"),
        txt(475,158,"div の手前で p を閉じる",13,SUB,"middle"),
        txt(475,214,"○ 文書は表示される",15,ACC,"middle","bold"),
        txt(475,240,"閲覧を止めない",13,SUB,"middle")]
    # XML column (止まる側 = DANGER)
    p+=[rect(630,62,250,200,DANGER_FILL,DANGER_ST,rx=14),
        txt(755,96,"XHTML（XML）",18,DANGER,"middle","bold"),
        txt(755,132,"不正なら処理を止める",15,INK,"middle","bold"),
        txt(755,158,"回復しない",13,SUB,"middle"),
        txt(755,214,"✕ ページが出ない",15,DANGER,"middle","bold"),
        txt(755,240,"黄色いエラー画面",13,SUB,"middle")]
    save("fig-14-1.svg",p)

# ---------------------------------------------------------------- fig-21-1
def fig_21_1():
    W,H=940,250
    p=head(W,H,"1989 年の提案から公開、img 登場と無償化、ブラウザ戦争、XHTML の挫折、HTML5、2019 年の標準一本化、現在の Living Standard までを並べた年表")
    y=130
    p+=[rect(40,30,860,190,"#fff",LINE,rx=14),ln(90,y,870,y,SUB,2)]
    pts=[(110,"1989","提案書",1),(220,"1991","世界初サイト公開",-1),
         (350,"1993","img 登場 / 無償化",1),(480,"1990s","ブラウザ戦争",-1),
         (600,"2000","XHTML（→挫折）",1),(710,"2014","HTML5",-1),
         (810,"2019","標準を一本化",1),(880,"now","Living Standard",-1)]
    for x,yr,ev,side in pts:
        p.append(circ(x,y,7,ACC))
        yy=y-40 if side>0 else y+34
        p+=[txt(x,yy,yr,15,ACC,"middle","bold"),txt(x,yy+18,ev,12,SUB,"middle")]
    save("fig-21-1.svg",p)

# ---------------------------------------------------------------- fig-24-1
def fig_24_1():
    W,H=920,320
    p=head(W,H,"1 つの HTML 文書を、ブラウザ・検索エンジン・スクリーンリーダー・SNS のカード生成・翻訳や保存ツールがそれぞれ構造から読む様子の図")
    p+=[rect(40,100,220,120,BLUE,ACC,rx=14),
        txt(150,150,"HTML 文書",18,ACC,"middle","bold"),
        txt(150,178,"構造・意味の手がかり",13,SUB,"middle")]
    readers=["ブラウザ（画面に表示）","検索エンジン（主題を推定）",
             "スクリーンリーダー（読み上げ）","SNS（カードを生成）",
             "翻訳・保存・リーダーモード"]
    for i,r in enumerate(readers):
        ry=54+i*52
        p+=[ln(268,160,556,ry+20,ACC,1.6,"ar"),
            rect(570,ry,310,40,NEUT,LINE,rx=10),
            txt(588,ry+26,r,15,INK)]
    save("fig-24-1.svg",p)

# ---------------------------------------------------------------- fig-d-1
def fig_d_1():
    W,H=920,300
    p=head(W,H,"table の直下に書いたテキストが、DOM では table の中ではなく table の直前へ移動する様子の図")
    p+=[txt(40,36,"ソース",15,SUB,weight="bold"),
        rect(40,48,330,96,"#fff",LINE,rx=12),
        txt(58,86,"<table>おっと<tr>",14,INK,mono=True),
        txt(74,114,"<td>A</td></tr></table>",14,INK,mono=True),
        ln(390,96,466,96,ACC,2.5,"ar"),txt(428,84,"解釈",13,ACC,"middle","bold")]
    p+=[txt(500,36,"DOM",15,SUB,weight="bold"),
        rect(500,48,380,240,"#fff",LINE,rx=12),
        rect(520,66,150,28,WARM,WARM_ST,rx=6),
        txt(534,86,'"おっと"',13,DANGER,mono=True),
        txt(690,86,"← 表の外（前）へ",13,ACC,weight="bold")]
    def node(x,y,s): return txt(x,y,s,14,ACC,weight="bold",mono=True)
    p+=[node(520,132,"table"),ln(536,140,562,162,LINE,1.5),
        node(562,180,"tbody"),ln(578,188,602,210,LINE,1.5),
        node(602,228,'tr › td › "A"')]
    save("fig-d-1.svg",p)

for fn in [fig_2_1,fig_4_1,fig_5_1,fig_6_1,fig_14_1,fig_21_1,fig_24_1,fig_d_1]:
    fn()
print("done")
