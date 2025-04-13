# python-uv-template


## 使用ツール
- uv
https://docs.astral.sh/uv/getting-started/installation/
- ruff

## 実行
### claudeを使用する場合

https://modelcontextprotocol.io/quickstart/server
を参照

### ローカルで実行する場合
uv run test_client.py



## uv
### Pythonのインストール
uv python install <python version>

### インストール済みのPythonバージョンの確認
uv python list

### Pythonの実行可能ファイルの検索
uv python find

### Pythonのバージョン変更
uv python pin <python version>

### uvプロジェクト作成
uv init <project name>

### pyproject変更後
uv sync

### パッケージのインストール
uv add <package>

### パッケージのアンインストール
uv remove <package>
