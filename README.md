# attract_group_test
Тестовое задание на позицию Python/Django developer


Инструкция по запуску проекта


Устанавливаем вирутальное окружение:

apt-get install python3-venv

python3 -m venv attract_test

Создаём виртуальное окружение:

python -m venv attract_test

Запускаем виртуальное окружение:

Для Windows:

cd attract_group_test/attract_test/Scripts 

activate

Для Ubuntu:

cd attract_group_test

source attract_test/bin/activate


Возвращаемся назад и устанавливаем все необходимые библиотеки:

cd ..

cd ..

pip install -r req.txt


Делаем миграции и запускаем сервер:

cd ordering_lunches

python manage.py makemigrations

python manage.py migrate

#можем создать нового админа командой: python manage.py createsuperuser

python manage.py runserver 0:8000


Открываем браузер и переходим на страницу авторизации для админа:

127.0.0.1:8000/admin/

Username: admin
Password: 1qaz2wsx3edc4rfv
