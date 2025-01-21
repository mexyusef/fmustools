# langkah bikin django app + deploy to aws

## masuk direktori kerja

## buat dan masuk venv

jangan di windows:
```
u -e"/b>py/venvwin"
<nama venv>\Scripts\activate
```

tapi:
```
u -e'/b>py/venvlin'
```

## instalasi django
```
pip install Django==3.2.12 channels==2.4.0 graphene-django==2.13.0 psycopg2-binary==2.9.3
```

## buat proyek django
```
django-admin startproject <nama proyek>
cd <nama proyek>
python manage.py runserver 0.0.0.0:7000
```

```
django-admin startproject mydj
cd mydj
python manage.py runserver 0.0.0.0:7000
```

catat nama folder berisi wsgi.py dan catat nama "application" di dalam wsgi.py

## buat requirements.txt
```
pip freeze
pip freeze > requirements.txt
```

## keluar venv
deactivate

## buat .ebextension dari dalam <nama proyek>
```
u -e"/b>devops/eb1"
```

masukkan input "nama folder berisi wsgi.py" dari langkah sebelumnya, sehingga hasilkan spt:
`<nama proyek>.wsgi:application`

## deployment
### eb init -p python-3.7 myeb1
```
eb init -p python-3.7 myeb1
```
(nanti kita coba python-3.8 jk ini berhasil)
### eb init
```
eb init
```
### eb create myenv1
```
eb create myenv1
```

jika proyek dibuat di windows, requirements.txt selalu hasilkan:
```
Failed to build twisted-iocpsupport

2022/03/27 17:41:38.035665 [ERROR] An error occurred during execution of command [app-deploy] - [InstallDependency]. Stop running the command. Error: fail to install dependencies with requirements.txt file with error Command /bin/sh -c /var/app/venv/staging-LQM1lest/bin/pip install -r requirements.txt failed with error exit status 1. Stderr:  error: subprocess-exited-with-error
```

### eb status
```
eb status
```

dapatkan nilai CNAME

### modify settings.py/config.py berdasarkan nilai CNAME
```
ALLOWED_HOSTS = ['eb-django-app-dev.elasticbeanstalk.com']
```

### eb deploy
```
eb deploy
```

### eb logs
```
eb logs
```

### eb open
```
eb open
```

### eb terminate myenv1
```
eb terminate myenv1
```
