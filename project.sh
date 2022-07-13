echo "Start"

django-admin startproject full_project_turism &&
cd full_project_turism &&
virtualenv venv &&

source venv/bin/activate&&
pip install django &&
pip install pillow &&
pip install djangorestframework && 

python manage.py migrate &&
python manage.py startapp mainapp &&

git init &&
touch .gitignore &&
pip freeze > requiremens.txt


echo "Finish"
