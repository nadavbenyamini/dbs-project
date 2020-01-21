# dbs-project
Final project, database systems course 2020

To launch in *DEV* mode run the following command:
FLASK_APP=app.py FLASK_ENV=development flask run

Full documentation: https://docs.google.com/document/d/1WUfbVdzCbdnAfQqMYTvBFFqI08r0F6ex_-6jTpvz710/edit

Deployment instructions:
1) Login to Nova
3) ssh delta-tomcat-vm
4) cd specific/scratch/benyamini1/django/dbs-project
5) git pull
6) git checkout master
7) pkill screen
8) virtualenv --prompt=venv --python=python3.6 .env
9) source .env/bin/activate.csh
10) python3.6 -m pip install -r --upgrade requirements.txt
11) setenv LD_LIBRARY_PATH /usr/local/lib/openssl-1.1.1a/lib
12) setenv LD_LIBRARY_PATH /usr/local/lib/openssl-1.1.1a/lib:$LD_LIBRARY_PATH
13) screen
14) python3.6 app.py
