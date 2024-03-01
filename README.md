# todo_list-drf
to do list, where i use django rest framework to create this



Commands: 
python3 -m venv venv 
source venv/bin/activate 
pip install -r requirements.txt

Скопирайте поля из .env.example 
Создайте папку .env вставте скопированые поля в .env и введите туда свои личные параметры 
Пример: 
SECRET_KEY='dwdpokpoklkkoqw' 
DEBUG=True 
ALLOWED_HOSTS='127.0.0.1 localhost'

PG_DATABASE=todo
PG_USER=postgres
PG_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432


напишите в командную строку:
python manage.py makemigrations 
python manage.py migrate 
python manage.py runserver



