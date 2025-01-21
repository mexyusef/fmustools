---
title: Deploy Django app to AWS
date: 2017/08/21
description: Deploy Django app to AWS
tag: django, AWS
author: Yusef
---

# awsebcli installation


```
git clone https://github.com/aws/aws-elastic-beanstalk-cli-setup.git

windows:
python ./aws-elastic-beanstalk-cli-setup/scripts/ebcli_installer.py

linux:
python .\aws-elastic-beanstalk-cli-setup\scripts\ebcli_installer.py

To complete installation, ensure `eb` is in PATH. You can ensure this by executing:
1. CMD Prompt:
	cmd.exe /c "C:\Users\usef\.ebcli-virtual-env\executables\path_exporter.bat"
2. PowerShell:
	& "C:\Users\usef\.ebcli-virtual-env\executables\path_exporter.vbs"
3. linux
	echo 'export PATH="/home/usef/.ebcli-virtual-env/executables:$PATH"' >> ~/.bash_profile && source ~/.bash_profile
```

Here are the steps to create a django project and deploy it to AWS.
```
1)
u -e"/b>py/venvwin"
u -e'/b>py/venvlin'

2)
pip install Django==3.2.12 channels==2.4.0 graphene-django==2.13.0 psycopg2-binary==2.9.3

3)
django-admin startproject mydj
cd mydj
python manage.py runserver 0.0.0.0:7000

4)
pip freeze
pip freeze > requirements.txt

5)
deactivate

6)
u -e"/b>devops/eb1"

7)
eb init -p python-3.7 myeb1

8)
eb init

9)
eb create myenv1

10)
eb status

    usef@DESKTOP-7HH37HJ:~/work/oprek/mydj$ eb status
    Environment details for: myenv1
    Application name: myeb1
    Region: us-west-2
    Deployed Version: app-220328_005509187761
    Environment ID: e-7kjjhm2zpz
    Platform: arn:aws:elasticbeanstalk:us-west-2::platform/Python 3.7 running on 64bit Amazon Linux 2/3.3.11
    Tier: WebServer-Standard-1.0
    CNAME: myenv1.eba-z3x8gxud.us-west-2.elasticbeanstalk.com   <- masukkan ke settings.py
    Updated: 2022-03-27 17:57:52.684000+00:00
    Status: Ready
    Health: Green                                               <- bukan Red

dapatkan nilai CNAME

11)
masukkan CNAME ke settings.py, misal
ALLOWED_HOSTS = ['eb-django-app-dev.elasticbeanstalk.com']

usef@DESKTOP-7HH37HJ:~/work/oprek/mydj$ vi mydj/settings.py

12)
eb deploy

    usef@DESKTOP-7HH37HJ:~/work/oprek/mydj$ eb deploy
    Creating application version archive "app-220328_010036348271".
    Uploading myeb1/app-220328_010036348271.zip to S3. This may take a while.
    Upload Complete.
    2022-03-27 18:00:40    INFO    Environment update is starting.
    2022-03-27 18:00:45    INFO    Deploying new version to instance(s).
    2022-03-27 18:00:49    INFO    Instance deployment successfully generated a 'Procfile'.
    2022-03-27 18:00:58    INFO    Instance deployment completed successfully.
    2022-03-27 18:01:03    INFO    New application version was deployed to running EC2 instances.
    2022-03-27 18:01:03    INFO    Environment update completed successfully.

13)
eb logs

14)
eb open

15)
eb terminate myenv1

16) operasi utk ngisi database, createsuperuser, upload static assets, dst

16.1
source venv/bin/activate

16.2
usef@DESKTOP-7HH37HJ:~/work/oprek/mydj$ python manage.py migrate
(https://youtu.be/51YwXvJ9LOE?t=699)

16.3 
python manage.py createsuperuser

16.4
tambah STATIC_ROOT di settings.py:
STATIC_URL = '/static/'
STATIC_ROOT = 'static'      <- +

16.5
python manage.py collectstatic
    (venv) usef@DESKTOP-7HH37HJ:~/work/oprek/mydj$ python manage.py collectstatic
    128 static files copied to '/home/usef/work/oprek/mydj/static'.

    usef@DESKTOP-7HH37HJ:~/work/oprek/mydj$ ll
    total 164
    drwxr-xr-x 6 usef usef   4096 Mar 28 01:15 ./
    drwxr-xr-x 4 usef usef   4096 Mar 28 00:53 ../
    drwxr-xr-x 2 usef usef   4096 Mar 28 00:54 .ebextensions/
    drwxr-xr-x 2 usef usef   4096 Mar 28 01:16 .elasticbeanstalk/
    -rw-r--r-- 1 usef usef    108 Mar 28 00:54 .gitignore
    -rw-r--r-- 1 usef usef 131072 Mar 28 01:14 db.sqlite3
    -rwxr-xr-x 1 usef usef    660 Mar 28 00:53 manage.py*
    drwxr-xr-x 3 usef usef   4096 Mar 28 01:15 mydj/
    -rw-r--r-- 1 usef usef    604 Mar 28 00:53 requirements.txt
    drwxr-xr-x 3 usef usef   4096 Mar 28 01:15 static/
    https://youtu.be/51YwXvJ9LOE?t=852
    => static/ satu direktori dg requirements.txt dan manage.py dan db.sqlite3

16.6 deploy (keluar dulu dari venv)
    (venv) usef@DESKTOP-7HH37HJ:~/work/oprek/mydj$ deactivate

    usef@DESKTOP-7HH37HJ:~/work/oprek/mydj$ eb deploy
    Creating application version archive "app-220328_011625058569".
    Uploading myeb1/app-220328_011625058569.zip to S3. This may take a while.
    Upload Complete.
    2022-03-27 18:16:32    INFO    Environment update is starting.
    2022-03-27 18:16:36    INFO    Deploying new version to instance(s).
    2022-03-27 18:16:41    INFO    Instance deployment successfully generated a 'Procfile'.
    2022-03-27 18:16:49    INFO    Instance deployment completed successfully.
    2022-03-27 18:16:54    INFO    New application version was deployed to running EC2 instances.
    2022-03-27 18:16:54    INFO    Environment update completed successfully.

```
