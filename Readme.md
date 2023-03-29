# Prerequisites
Install firefox and geckodriver in the *prerequisites* folder
https://blog.henrypoon.com/blog/2020/09/27/running-selenium-webdriver-on-wsl2/
Install python 3.7
Setup environment for python
mkvirtualenv python37 && workon python37

Install Django 1.11 and Selenium 3
pip install "django<1.12" "selenium<4"

# Run
run server
firsttime
python manage.py migrate

python manage.py runserver

run test

python -W ignore functional_tests.py
