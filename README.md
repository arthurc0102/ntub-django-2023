**請確保虛擬環境啟動 `poetry shell`**

建立 poetry 專案（產生 pyproject.toml 檔案）：`poetry init`

把套件加入 pyproject.toml 當中：`poetry add <packacge name>`

依照 pyproject.toml 的設定建立虛擬環境並安裝套件：`poetry install`


建立 Django 專案：`django-admin startproject core .`

啟動伺服器：`python manage.py runserver` (用瀏覽器訪問 <http://127.0.0.1:8000>)

建立 Django APP：`python manage.py startapp <app name>`
