# SPDX-FileCopyrightText: 2026 ishikawa-slfecd  [slfecd (ishikawa-slfecd)](https://github.com/slfecd)
# SPDX-License-Identifier: LGPL-2.1-or-later OR Apache-2.0

# AI生成物を元に改変しています
# 自作マクロを FreeCADに設定されているマクロ保存ディレクトリへ コピーする
#
# - FreeCAD Ver1.1.1 : Python v3.11.14
# - Windows10 64bit

# ruff:noqa: I001
from typing import Final, cast

import os
import shutil
import fnmatch

import FreeCAD as App


__date__: Final[str] = "2026-08-06"  # YMD


FLAG_DRY_RUN: Final[bool] = False  # True=シミュレーション動作  False=本番動作

MACRO_NAME: Final[str] = "FindWorstTolerance"

COPY_FILE_LIST: Final[list[str]] = [
    "FindWorstTolerance.FCMacro",
    "FindWorstTolerance.svg",
    "package.xml",
]


def file_copy2(
    src_dir: str, dst_dir: str, file_list: list[str], file_mask: str = ""
) -> bool:
    if not os.path.exists(src_dir):
        print(f"コピー元パス異常：{src_dir}")
        return False

    if not os.path.exists(dst_dir):
        if not FLAG_DRY_RUN:
            os.makedirs(dst_dir)
        print(f"コピー先ディレクトリを作成しました: {dst_dir}")

    # File copy
    for file_name in file_list:
        if file_mask and not fnmatch.fnmatch(file_name, file_mask):
            continue

        try:
            src_file_path = os.path.join(src_dir, file_name)
            dst_file_path = os.path.join(dst_dir, file_name)
            if not FLAG_DRY_RUN:
                shutil.copy2(src_file_path, dst_file_path)  # 日付属性もコピー
            print(f"  {file_name}")

        except OSError as e:
            print(f"***Error: {file_name} のコピーに失敗しました。理由: {e}")
            return False
    # for

    return True


def main() -> bool:
    print("--- マクロをFreeCADに仮インストールします（デバッグ用途向け） ---")
    if FLAG_DRY_RUN:
        print("=== DRY RUN MODE ===")

    # カレントディレクトリ取得 /tools/../
    src_dir: Final = (
        os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
        if "__file__" in globals()
        else ""
    )

    if not src_dir:
        print(
            "***ERROR: FreeCADでこのマクロファイルを開き実行（Pythonコンソールからは実行できません）、またはFreeCAD同梱pythonから実行してください。"
        )
        return False

    # FreeCADの設定からマクロ保存ディレクトリのパス取得
    param_group: Final = cast(
        "App.ParameterGrp",  # 実行時に見つからない
        App.ParamGet("User parameter:BaseApp/Preferences/Macro"),
    )
    macro_dir: Final = os.path.normpath(param_group.GetString("MacroPath"))

    if not macro_dir:
        print(
            "***ERROR: FreeCADの【編集→設定→Python→マクロ→マクロのパス】を設定してください"
        )
        return False

    # FreeCAD Modフォルダパス取得
    mod_dir: Final = os.path.join(App.getUserAppDataDir(), "Mod", MACRO_NAME)

    #
    # File copy : Mod dir.
    print(f"コピー先のパス: {mod_dir}")
    if not file_copy2(src_dir, mod_dir, COPY_FILE_LIST):
        return False

    # File copy : Macro dir.
    print(f"コピー先のパス: {macro_dir}")
    if not file_copy2(src_dir, macro_dir, COPY_FILE_LIST, "*.FCMacro"):  # noqa: SIM103
        return False

    # 正常終了
    return True


##
if __name__ == "__main__":
    main()
