# まだまだ編集中。実行すると危ないよ。
# AI生成物を元に改変しています
# カレントディレクトリにある自作マクロを FreeCADに設定されているマクロ保存ディレクトリへ コピーする
from typing import Final, cast
import glob
import os
import shutil

import FreeCAD


def main() -> bool:
    # FreeCADの設定からマクロ保存ディレクトリのパス取得
    param_group: Final = cast(
        "FreeCAD.ParameterGrp",  # 実行時に見つからない
        FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Macro"),
    )
    # "MacroPath", os.path.join(FreeCAD.getUserAppDataDir(), "Macro")
    macro_dir: Final = cast(str, param_group.GetString("MacroPath"))

    # カレントディレクトリ取得
    current_dir: Final = (
        os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else ""
    )

    print("--- マクロをFreeCADマクロパスにコピーします ---")
    print(f"コピー元のパス: {current_dir}")
    print(f"コピー先のパス: {macro_dir}")
    if not macro_dir:
        print("***ERROR: FreeCADの【編集→設定→Python→マクロ→マクロのパス】を設定してください")  # fmt: skip
        return False
    if not current_dir:
        print("***ERROR: FreeCADでこのマクロファイルを開き実行（Pythonコンソールからは実行できません）、またはFreeCAD同梱pythonから実行してください。")  # fmt: skip
        return False

    return False  # ***** DEBUG BREAK : 作成中、ここまで動作確認した。 *****

    # マクロディレクトリが存在しない場合は作成
    if not os.path.exists(macro_dir):
        os.makedirs(macro_dir)
        print(f"マクロディレクトリを作成しました: {macro_dir}")

    # 3. カレントディレクトリ内の「.FCMacro」ファイルを検索してコピー
    macro_files = glob.glob(os.path.join(current_dir, "*.FCMacro"))

    if not macro_files:
        print(
            "警告: カレントディレクトリに '.FCMacro' ファイルが見つかりませんでした。"
        )
        print(
            "特定のフォルダからコピーする場合は、'current_dir' を直接書き換えてください。"
        )
    else:
        copied_count = 0
        for file_path in macro_files:
            file_name = os.path.basename(file_path)
            dest_path = os.path.join(macro_dir, file_name)

            try:
                shutil.copy2(file_path, dest_path)
                print(f"成功: {file_name} -> {macro_dir}")
                copied_count += 1
            except Exception as e:
                print(f"エラー: {file_name} のコピーに失敗しました。理由: {e}")

        print(f"--- 処理終了: {copied_count} 個のファイルをコピーしました ---")

    # 終了
    return True


#
main()
