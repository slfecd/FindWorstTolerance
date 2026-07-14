# AI生成物を元に改変しています
# 自作マクロを FreeCADに設定されているマクロ保存ディレクトリへ コピーする
#
# - FreeCAD Ver1.1.1 : Python v3.11.14
# - Windows10 64bit

from typing import Final, cast

import os
import shutil
import FreeCAD


__date__: Final[str] = "2026/07/12"  # YMD


FLAG_DRY_RUN: Final[bool] = False  # True=シミュレーション動作  False=本番用

COPY_FILE_LIST: Final[list[str]] = [
    "FindWorstTolerance.FCMacro",
    "package.xml",
]


def main() -> bool:
    print("--- マクロをFreeCADマクロパスにコピーします ---")
    if FLAG_DRY_RUN:
        print("=== DRY RUN MODE ===")

    # カレントディレクトリ取得
    src_dir: Final = (
        os.path.normpath(
            os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "../"
            )  # ディレクトリ移動対応
        )
        if "__file__" in globals()
        else ""
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
    dst_dir: Final = os.path.normpath(param_group.GetString("MacroPath"))

    print(f"コピー先のパス: {dst_dir}")
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
            print(f"  {file_name}")
        except Exception as e:
            print(f"***Error: {file_name} のコピーに失敗しました。理由: {e}")
            return False
    # for

    return True


#
if __name__ == "__main__":
    main()
