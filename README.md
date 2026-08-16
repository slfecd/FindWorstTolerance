# Find worst tolerance

FreeCAD macro  
This text has been machine-translated from Japanese.

[後半に日本語版があります](#japanese-version)

## Summary

Finds elements (Vertex, Edge, Face) with the worst tolerance values and selects them (highlighted in the selection color)

### Tested Environment

- FreeCAD v1.1.3 (Python 3.11.14)
- Windows10 64bit
- git version 2.55.0.windows.4

## Objective

Under construction

## Installation

1. Add a custom repository to the Addon Manager
   1. Open the preferences screen
      - Select **Edit** -> **Preferences** from the menu bar
   2. Display the Addon Manager settings items
      - Select **Addon Manager Options** from the list on the left side of the preferences screen
   3. Configure the custom repository
      1. Select the `+` button at the bottom right of the Custom repositories field
      2. Enter (copy and paste) the following strings into the displayed dialog screen:
         - Repository URL: `https://github.com/slfecd/FindWorstTolerance`
         - Branch: `main`
      3. Press the **OK** button at the bottom right of the dialog screen
   4. Save settings and exit
      - Press the **OK** button at the bottom right of the preferences screen
2. Launch the Addon Manager
      - Select **Tools** -> **Addon Manager** from the menu bar
3. Select `FindWorstTolerance` from the list and install it
4. Close the Addon Manager

## Operating Procedure

1. Select the target object
   - Select the target object from the model tree in the combo view
2. Run the `Find worst tolerance` macro
   1. Select **Macro** -> **Macros** from the menu bar
   2. Select `FindWorstTolerance.FCMacro` from the User macros tab in the displayed dialog screen
   3. Press the **Execute** button at the top right of the dialog screen
3. Check the results
   - Elements with the worst tolerance values will be selected (highlighted in the selection color)
      - Selects elements that exceed FreeCAD's default tolerance value ($1 \times 10^{-7}$)
   - Information on the elements with the worst tolerance values will be displayed in the Report view
      - How to display the Report view: Check **View** -> **Panels** -> **Report view** checkbox in the menu bar

### Toolbar Registration Method (Manual)

1. Preparation
   - The tricky part of toolbar registration is registering the **full path of the directory** where the icon file is located
   - It is easier if you copy the full path string to the clipboard in advance
   - We have prepared a script that automatically copies it to the clipboard.  
     If you copy and paste this script into FreeCAD's Python console screen and run it, the full path string will be copied to the clipboard.  
   - How to display the Python console screen: Check **View** -> **Panels** -> **Python Console** checkbox in the menu bar

     ``` Python
     import os, FreeCAD; from PySide.QtGui import QApplication; p = os.path.join(FreeCAD.getUserAppDataDir(), "Mod", "FindWorstTolerance"); QApplication.clipboard().setText(p); print(f"Copied the full path name of the icon directory to the clipboard: {p}")
     ```

2. Open the Execute Macro screen
   1. Select **Macro** -> **Macros** from the menu bar
   2. Select `FindWorstTolerance.FCMacro` from the User macros tab in the dialog screen
   3. Press the **Toolbar** button on the dialog screen
   4. If a confirmation screen appears, it is a good idea to select the **OK** button

3. The Walkthrough Dialog 1/2 screen is displayed
   1. Confirm that the macro item is `FindWorstTolerance.FCMacro`
   2. Select the **[...]** button for the icon item
   3. The Choose Icon screen is displayed
      1. Select the **Icon folders** button at the bottom left of the screen
      2. The Icon Folders screen is displayed
         1. Select the `+` button
         2. The Add icon folder screen is displayed
            1. Paste the full path string from the clipboard into the folder field
            2. Select the **Choose folder** button
         3. Select the **OK** button
      3. Select the `FindWorstTolerance.svg` icon, which is probably displayed near the end or beginning <!-- markdownlint-disable-line MD033 --><img src="./FindWorstTolerance.svg" width="32" alt="FindWorstTolerance.svg">
   4. Select the **Add** button
   5. Select the **Close** button

4. The Walkthrough Dialog 2/2 screen is displayed
   1. Select the **->** button
   2. Select the **Close** button

5. Select the **Close** button on the Execute Macro screen
6. Finished (Good job!)

## License

- Source code: LGPL-2.1-or-later OR Apache-2.0
  - [(LGPL-2.1)   GNU LESSER GENERAL PUBLIC LICENSE Version 2.1](LICENSE-LGPL-2.1)
  - [(Apache-2.0) Apache License Version 2.0](LICENSE-Apache-2.0)
- Icon: CC BY-SA 4.0
  - (CC BY-SA 4.0) Creative Commons Attribution-ShareAlike 4.0 International : [https://creativecommons.org/licenses/by-sa/4.0/legalcode.en](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en)
- Copyright 2026 ishikawa-slfecd
  - [GitHub - slfecd (ishikawa-slfecd)](https://github.com/slfecd)

## Version History

- vX.Y.Z : Y-M-D : Public initial release

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
   2. アドオンマネージャーの設定項目を表示する
      - 設定画面の左側リストから アドオンマネージャー(Addon Manager Options) を選択
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
2. `Find worst tolerance` マクロを実行する
   1. メニューバーの マクロ(Macro) → マクロ(Macros) を選択
   2. 表示されるダイアログ画面のユーザーマクロ・タブから `FindWorstTolerance.FCMacro` を選択する
   3. ダイアログ画面の右上の［実行］ボタンを押す
3. 結果を確認する
   - トレランス値ワースト要素が選択状態になります（選択色にハイライトされる）
     - FreeCADのトレランス初期値($1 \times 10^{-7}$)を超える要素を選択します
   - レポートビューにトレランス値ワースト要素の情報が表示されます
     - レポートビューの表示方法：メニューバーの 表示(View) → パネル(Panels) → レポートビュー(Report View)チェックボックス にチェックを入れる

### ツールバーへの登録方法（手動）

1. 準備
   - ツールバー登録の難所はアイコンファイルのある**ディレクトリのフルパスを登録**する作業です
   - あらかじめクリップボードにフルパス文字列をコピーしておくと作業が楽になります
   - 自動的にクリップボードへコピーするスクリプトを準備しました。  
      FreeCADのPythonコンソール画面へ、このスクリプトをコピー＆ペーストして実行すると、フルパス文字列がクリップボードへコピーされた状態になります。  
   - Pythonコンソール画面の表示方法：メニューバーの 表示(View) → パネル(Panels) → Pythonコンソール(Python Console)チェックボックス にチェックを入れる

      ``` Python
      import os, FreeCAD; from PySide.QtGui import QApplication; p = os.path.join(FreeCAD.getUserAppDataDir(), "Mod", "FindWorstTolerance"); QApplication.clipboard().setText(p); print(f"クリップボードにアイコンのディレクトリのフルパス名をコピーしました : {p}")
      ```

2. マクロを実行 画面を表示する
   1. メニューバーの マクロ(Macro) → マクロ(Macros) を選択
   2. ダイアログ画面のユーザーマクロ・タブから `FindWorstTolerance.FCMacro` を選択する
   3. ダイアログ画面の［ツールバー］ボタンを押す
   4. 確認画面が出た場合は［ＯＫ］ボタンを選択すると良いでしょう

3. ウォークスルー・ダイアログ1/2 画面が表示される
   1. 項目マクロが `FindWorstTolerance.FCMacro` であることを確認する
   2. 項目アイコンの［…］ボタンを選択
   3. アンコンを選択してください(Choose Icon) 画面が表示される
      1. 画面左下の［アイコンフォルダー(Icon Folders)］ボタンを選択
      2. アイコンフォルダー(Icon Folders) 画面が表示される
         1. ［＋］ボタンを選択
         2. アイコンフォルダーを追加 画面が表示される
            1. フォルダー欄へクリップボードからフルパス文字列をペースト
            2. ［フォルダーの選択］ボタンを選択
         3. ［ＯＫ］ボタンを選択
      3. おそらく末尾や先頭付近に表示されている <!-- markdownlint-disable-line MD033 --><img src="./FindWorstTolerance.svg" width="32" alt="FindWorstTolerance.svg"> `FindWorstTolerance.svg` アイコンを選択する
   4. ［追加］ボタンを選択
   5. ［閉じる］ボタンを選択

4. ウォークスルー・ダイアログ2/2 画面が表示される
   1. ［→］ボタンを選択
   2. ［閉じる］ボタンを選択

5. マクロを実行 画面の［閉じる］ボタンを選択
6. 終了（お疲れさまでした）

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
