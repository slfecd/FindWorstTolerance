# AI生成物を元に改変しています
# テストランナー
# - モデルツリー内の要素を選択して find_worst_tolerances.FCMacro を実行する
# - FreeCADに編集できる状態で読み込み実行しないとエラーになるよ
#   - ファイルをPythonコンソール・パネルにドラックドロップしちゃダメよ
#
# - FreeCAD Ver1.1.1 : Python v3.11.14
# - Windows10 64bit

from typing import Final, TypeAlias
import traceback

import os
import FreeCADGui as Gui
import FreeCAD as App


__version__: Final = "0.1.1"
__date__: Final = "2026/07/08"  # YMD


def clear_report_view() -> None:
    """レポートビューをクリアする"""
    from PySide6 import QtWidgets

    # FreeCADのメインウィンドウを取得
    main_win: Final = Gui.getMainWindow()

    # レポートビューのウィジェット（QTextEdit）を探してクリア
    report_view: Final = main_win.findChild(QtWidgets.QTextEdit, "Report view")
    if report_view:
        report_view.clear()


def run_macro(path: str) -> bool:
    """マクロを実行：成功True エラーFalse を返す"""
    try:
        with open(path, encoding="utf-8") as f:
            code = f.read()

        exec(code, globals().copy())
        return True

    except Exception as e:
        print(f"\n[ERROR] マクロ実行中にエラーが発生しました: {e}")
        traceback.print_exc()  # スタックトレースをレポートビューに出力
        return False


#
Type_SelectionList: TypeAlias = list[tuple[str, str] | tuple[str, str, str]]


def selection_and_run(sel_list: Type_SelectionList) -> bool:
    """要素を選択してマクロ実行：成功True エラーFalse を返す"""

    macro_path: Final = os.path.join(
        os.path.dirname(__file__), "FindWorstTolerance.FCMacro"
    )

    Gui.Selection.clearSelection()
    for sel in sel_list:
        # タプルを展開して渡す
        # FreeCADのスタブ(_Selection.pyi)のオーバーロード定義が不完全なため
        # Pylanceが誤検知する。実行時は正常なためエラーを抑制。
        Gui.Selection.addSelection(*sel)  # type: ignore[reportCallIssue]
    return run_macro(macro_path)


def main(single_run_index: None | int = None) -> bool | None:
    # テスト毎に選択する要素定義
    test_cases: Final[list[Type_SelectionList]] = [
        # Test : Select Origin(原点)
        [("Slider_r0", "Body001", "Origin002.")],
        # Test : Select Sketch
        [("Slider_r0", "Body001", "AdditivePipe001.Sketch003.")],
        # Test : Select Body
        [("Slider_r0", "Body001")],
        # Test : 2 Select
        [
            ("Slider_r0", "Body001", "AdditivePipe001."),
            ("Slider_r0", "Body001", "Fillet001."),
        ],
    ]

    #
    clear_report_view()
    flag: bool | None = None

    if single_run_index is None:
        # Normal test mode
        for index, selections in enumerate(test_cases, start=1):
            App.Console.PrintMessage(f"### [Test {index}]\n")
            flag = selection_and_run(selections)  # マクロ実行
            if not flag:
                break  # エラーならテスト中止
            App.Console.PrintMessage("\n")
    else:
        # Single test run mode
        App.Console.PrintMessage(f"### [Test Single run : index={single_run_index}]\n")
        flag = selection_and_run(test_cases[single_run_index])  # マクロ実行

    return flag


#
if __name__ == "__main__":
    main()
