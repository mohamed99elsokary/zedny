start  kafka\zookeeper.bat
timeout /t 10 
start  kafka\kafka.bat
timeout /t 10 
start kafka\listen_from_kafka.bat
call  env\Scripts\activate.bat
py manage.py runserver