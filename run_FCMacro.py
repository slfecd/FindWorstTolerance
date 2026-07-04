# AI生成物を元に改変しています
# テストランナー
# - モデルツリー内の要素を選択して find_worst_tolerances.FCMacro を実行する
# - FreeCADに編集できる状態で読み込み実行しないとエラーになるよ
#   - ファイルをPythonコンソール・パネルにドラックドロップしちゃダメよ
#
# - FreeCAD Ver1.1.1
# - Windows10 64bit

from typing import Final, TypeAlias
import traceback

import os
import FreeCADGui as Gui
import FreeCAD as App


def clearReportView() -> None:
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

        # グローバル/ローカルのスコープを明示的に渡してexecを実行
        # （マクロ内の変数バッティングを防ぐため {} を推奨）
        exec(code, globals())
        return True

    except Exception as e:
        print(f"\n[ERROR] マクロ実行中にエラーが発生しました: {e}")
        # 詳細なスタックトレース（エラーの発生行など）をレポートビューに出力
        traceback.print_exc()
        return False


#
Type_SelectElementList: TypeAlias = list[tuple[str, str] | tuple[str, str, str]]


def main(single_run_index: None | int = None) -> bool | None:
    # テスト毎に選択する要素定義
    test_cases: Final[list[Type_SelectElementList]] = [
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
    def selectAndRun(sel_list: Type_SelectElementList) -> bool:
        macro_path: Final = os.path.join(
            os.path.dirname(__file__), "find_worst_tolerances.FCMacro"
        )

        Gui.Selection.clearSelection()
        for sel in sel_list:
            # タプルを展開して渡す
            # FreeCADのスタブ(_Selection.pyi)のオーバーロード定義が不完全なため
            # Pylanceが誤検知する。実行時は正常なためエラーを抑制。
            Gui.Selection.addSelection(*sel)  # type: ignore[reportCallIssue]
        return run_macro(macro_path)

    #
    clearReportView()
    flag: bool | None = None

    if single_run_index is None:
        # Normal test mode
        for index, selections in enumerate(test_cases, start=1):
            App.Console.PrintMessage(f"### [Test {index}]\n")
            flag = selectAndRun(selections)
            if not flag:
                break  # エラーならテスト中止
            App.Console.PrintMessage("\n")
    else:
        # Single test run mode
        App.Console.PrintMessage(f"### [Test Single run : index={single_run_index}]\n")
        flag = selectAndRun(test_cases[single_run_index])

    return flag


#
main()
