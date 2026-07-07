# AI生成物を元に改変しています
# カレントディレクトリにある自作マクロを FreeCADに設定されているマクロ保存ディレクトリへ コピーする

from typing import Final, cast

_Version__: Final[str] = "0.0.1"
__Date__: Final[str] = "2026/07/08"  # YMD

import os
import shutil

import FreeCAD

FLAG_DRY_RUN: Final[bool] = False  # True=シミュレーション動作  False=本番用
COPY_FILE_LIST: Final[list[str]] = ["find_worst_tolerances.FCMacro"]


def main() -> bool:
    print("--- マクロをFreeCADマクロパスにコピーします ---")

    # カレントディレクトリ取得
    src_dir: Final = (
        os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else ""
    )  # Source

    print(f"コピー元のパス: {src_dir}")
    if not src_dir:
        print("***ERROR: FreeCADでこのマクロファイルを開き実行（Pythonコンソールからは実行できません）、またはFreeCAD同梱pythonから実行してください。")  # fmt: skip
        return False

    # FreeCADの設定からマクロ保存ディレクトリのパス取得
    param_group: Final = cast(
        "FreeCAD.ParameterGrp",  # 実行時に見つからない
        FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Macro"),
    )
    dst_dir: Final = cast(str, param_group.GetString("MacroPath"))  # Destination

    print(f"コピー先のパス: {dst_dir}\n")
    if not dst_dir:
        print("***ERROR: FreeCADの【編集→設定→Python→マクロ→マクロのパス】を設定してください")  # fmt: skip
        return False

    # マクロ保存先ディレクトリが無い場合は作成する
    if not os.path.exists(dst_dir):
        if not FLAG_DRY_RUN:
            os.makedirs(dst_dir)
        print(f"FreeCADマクロ保存ディレクトリを作成しました: {dst_dir}")

    # File copy
    for file_name in COPY_FILE_LIST:
        try:
            dest_path = os.path.join(dst_dir, file_name)  # os.path.basename(file_path)
            if not FLAG_DRY_RUN:
                shutil.copy2(file_name, dest_path)  # 日付属性もコピー
            print(f"{file_name} --> {dst_dir}")
        except Exception as e:
            print(f"***Error: {file_name} のコピーに失敗しました。理由: {e}")
            return False
    # for

    return True


#
main()
