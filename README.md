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

準備中  
FreeCAD macro

## 概要

トレランス値ワースト要素(Vertex, Edge, Face)を探して選択状態にします

### 動作確認環境

- FreeCAD v1.1.3
- Windows10 64bit

## 目的

## インストール方法

1. アドオンマネージャーにカスタムリポジトリを追加する
   1. 設定画面を表示する
      - メニューバーの 編集 → 設定 を選択
   2. アドオン・マネージャーの設定項目を表示する
      - 設定画面の左側リストから アドオン・マネージャー を選択
   3. カスタムリポジトリを設定する
      1. カスタムリポジトリ欄の右下の［＋］ボタンを選択
      1. 表示されるダイアログに次の文字列を入力（コピー＆ペースト）、OKボタン を押す
         - リポジトリのURL： https://github.com/slfecd/FindWorstTolerance
         - ブランチ： main
   4. 設定終了

2. アドインマネージャを起動する
      - メニューバーの ツール → Addon Manager を選択
3. 表示されるリストから FindWorstTolerance を選択してインストール

### ツールバーへの登録方法

- 記述するべきか悩み中
- アイコンファイルの選択が大変そう

## 操作手順

1. 選択
2. マクロ実行
3. 結果確認

- ワースト・トレラントの各要素（頂点、エッジ、面）を探す
  - FreeCADのトレランス初期値を超える要素を選択状態にする（選択色に変化）
  - レポートビューに結果表示

## ライセンス

- ソースコード：[GNU Lesser General Public License v2.1 or later (LGPL-2.1-or-later)](LICENSE-LGPL-2.1) or [Apache License 2.0 (Apache-2.0)](LICENSE-Apache-2.0)
- アイコン：[Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en)
- Copyright 2026 ishikawa-slfecd
  - [GitHub - slfecd (ishikawa-slfecd)](https://github.com/slfecd)

## バージョン履歴

## 今後の予定

- README.mdの 整備
- そのうちGUI化するかもしれない
