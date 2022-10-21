1. Клонируете репозиторий
2. Открываете папку task1
##ENV
Переходите далее в папку task1 и создаёте файл .env, пишите туда SECRET_KEY = {ключ}
Далее добавляем DEBUG = {True или False}
Выходим из папки task1
3. Открываете cmd в этой папке и устанавливаете venv. #python -m venv venv
4. Активируете venv # venv\Scripts\activate
5. Устанавливаете requirements #pip install -r requirements.txt
6. Переходите в папку task1
7. Далее запускаете сервер #python manage.py runserver
