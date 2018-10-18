# Blog

this Simple blog was written by me using Python2(Django) and Bootstrap theme for the frontend.
- you can check live version here: http://amranwar00.pythonanywhere.com/

### to run the project

- after clone it, write in the project dir terminal:

```
virtualenv venv # make sure you've virtualenv in your machine, #pip install virtualenv
python2 manage.py migrate
pip2 install -r requirements.txt
python2 manage.py collectstatic
python2 manage.py migrate # creare database(sqlite)
python2 manage.py runserver # to run the server
```
- check after running the server:

```
(venv) amranwar00 blog-master $ python2 manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
October 18, 2018 - 23:10:39
Django version 1.11.15, using settings 'myblog.settings'
Starting development server at http://127.0.0.1:8000/
```

- open the localhost http://127.0.0.1:8000/
should see something like:

![home](http://www7.0zz0.com/2018/10/19/02/584800181.jpeg)

-  to connect the adminastration to add posts go : http://127.0.0.1:8000/admin/

first in terminal create your admin user 

```
python2 manage.py createsupersuer
```
then you will see the admin page like:

![pasted image](http://www7.0zz0.com/2018/10/19/02/547203549.jpeg)