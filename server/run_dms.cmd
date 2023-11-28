@echo off
cd C:\dev\Python\DMS\server

call C:\Users\KOSA\anaconda3\envs\DMS\Lib\venv\scripts\nt\activate

set FLASK_APP=pybo
set FLASK_DEBUG=true

flask db migrate
flask db upgrade

flask run


pause