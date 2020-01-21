# dbs-project
Final project, database systems course 2020

To launch in *DEV* mode run the following command:
FLASK_APP=app.py FLASK_ENV=development flask run

Full documentation: https://docs.google.com/document/d/1WUfbVdzCbdnAfQqMYTvBFFqI08r0F6ex_-6jTpvz710/edit

Deployment instructions:
1) Login to Nova
2) scp -r ~benyamin1/DBSystems/final-project/dbs-project delta-tomcat-vm:/specific/scratch/benyamini1/django/
3) ssh delta-tomcat-vm
4) cd specific/scratch/benyamini1/django/dbs-project
5) pkill screen (ignore error messages)
6) virtualenv --prompt=venv --python=python3.6 .env
7) source .env/bin/activate.csh
8) python3.6 -m pip install --upgrade pymysql
9) python3.6 -m pip install --upgrade Flask
9) python3.6 -m pip install --upgrade flask_cors
10) setenv LD_LIBRARY_PATH /usr/local/lib/openssl-1.1.1a/lib
11) setenv LD_LIBRARY_PATH /usr/local/lib/openssl-1.1.1a/lib:$LD_LIBRARY_PATH
