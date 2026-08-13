# Find worst tolerance

Under construction  
FreeCAD macro  
This text has been machine-translated from Japanese.

[後半に日本語版があります](#japanese-version)

## Summary

Finds elements (Vertex, Edge, Face) with the worst tolerance values and selects them.

### Tested Environment

- FreeCAD v1.1.3
- Windows 10 64-bit

## Objective

## Installation

1. Add repository
2. Addon Manager
3. Toolbar registration method?

## Operating Procedure

1. Select
2. Execute macro
3. Check results

- Find elements with the worst tolerances (vertices, edges, faces)
  - Select elements that exceed FreeCAD's default tolerance values (changes to selection color)
  - Display results in the Report view

## License

- Source code: [GNU Lesser General Public License v2.1 or later (LGPL-2.1-or-later)](LICENSE-LGPL-2.1) or [Apache License 2.0 (Apache-2.0)](LICENSE-Apache-2.0)
- Icon: [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en)
- Copyright 2026 ishikawa-slfecd
  - [GitHub - slfecd (ishikawa-slfecd)](https://github.com/slfecd)

## Version History

## Future Plans

- Improve README.md
- May add a GUI eventually

---
---

## Japanese version

FreeCAD マクロ

## 概要

トレランス値ワースト要素（頂点(Vertex)，線(Edge)，面(Face)）を探して選択状態にします（選択色にハイライトされます）

### 動作確認環境

- FreeCAD v1.1.3 (Python 3.11.14)
- Windows10 64bit
- git version 2.55.0.windows.4

## 目的

準備中

## インストール方法

1. アドオンマネージャーにカスタムリポジトリを追加する
   1. 設定画面を表示する
      - メニューバーの 編集(Edit) → 設定(Preferences) を選択
   2. アドオン・マネージャーの設定項目を表示する
      - 設定画面の左側リストから アドオン・マネージャー(Addon Manager Options) を選択
   3. カスタムリポジトリを設定する
      1. カスタムリポジトリ欄の右下の［＋］ボタンを選択
      2. 表示されるダイアログ画面に次の文字列を入力（コピー＆ペースト）する
         - リポジトリURL： `https://github.com/slfecd/FindWorstTolerance`
         - ブランチ： `main`
      3. ダイアログ画面の右下の［ＯＫ］ボタンを押す
   4. 設定を保存して終了する
      - 設定画面の右下の［ＯＫ］ボタンを押す
2. アドオンマネージャを起動する
      - メニューバーの ツール(Tools) → Addon Manager を選択
3. リストから `FindWorstTolerance` を選択してインストール
4. アドオンマネージャを閉じる

## 操作手順

1. 対象オブジェクトを選択する
   - コンボビューのモデルツリーから対象オブジェクトを選択する
2. Find worst tolerance マクロを実行する
   1. メニューバーの マクロ(Macro) → マクロ(Macros) を選択
   2. 表示されるダイアログ画面のユーザーマクロ・タブから `FindWorstTolerance.FCMacro` を選択する
   3. ダイアログ画面の右上の［実行］ボタンを押す
3. 結果を確認する
   - トレランス値ワースト要素が選択状態になります（選択色にハイライトされる）
     - FreeCADのトレランス初期値($1 \times 10^{-7}$)を超える要素を選択状態にします
   - レポートビューにトレランス値ワースト要素の情報が表示されます
     - レポートビューの表示方法：メニューバーの 表示(View) → パネル(Panels) → レポートビュー(Report View)チェックボックス にチェックを入れる

### ツールバーへの登録方法（手動）

準備中

- 記述するべきか悩み中
- アイコンファイルの選択が大変

## ライセンス

- ソースコード：LGPL-2.1-or-later OR Apache-2.0
  - [(LGPL-2.1)   GNU LESSER GENERAL PUBLIC LICENSE Version 2.1](LICENSE-LGPL-2.1)
  - [(Apache-2.0) Apache License Version 2.0](LICENSE-Apache-2.0)
- アイコン：CC BY-SA 4.0
  - (CC BY-SA 4.0) Creative Commons Attribution-ShareAlike 4.0 International : [https://creativecommons.org/licenses/by-sa/4.0/legalcode.en](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en)
- Copyright 2026 ishikawa-slfecd
  - [GitHub - slfecd (ishikawa-slfecd)](https://github.com/slfecd)

## バージョン履歴

- vX.Y.Z : Y-M-D : 一般公開 初版

## 今後の予定など

- README.md の整備
- そのうちGUI化するかもしれない

## 未整理

- 用語メモ
  - Find worst tolerance
  - メニューバー
  - ダイアログ
  - レポートビュー
  - トレランス
  - コンボビューのモデルツリー
  - Pythonコンソール

- 初回インストール後にアドオンマネージャーを起動するとリペア処理が発動する件の解析
  - マクロ側では対応できないことが確定しました。
  - gitがインストールされて無い環境での挙動は調べていない
  - アドオンマネージャーのコードを解読した感じでは、この挙動は仕様の様です
  1. インストール方法が３種類に別れている。以降の説明はカスタムリポジトリに関します。
     - カスタムリポジトリ／カタログ掲載のマクロ以外のアドオン／カタログ記載のマクロ@Wiki
  2. カスタムリポジトリは全てワークベンチ型として扱われる
  3. 初回インストールはZIPファイル方式
  4. 起動時に mod/アドオン名/.git ディレクトリが存在しないとリペア発動
  5. リペアは git clone が行われる。ブランチ名の指定はない。
  6. 更新の有無の確認は git fetch & status で行われる
