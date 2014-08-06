django-cms
==========

基于 Django 1.7

最后一次接触 Django 是 1.2 版本，做一个小的 CMS，看看新版本有什么新的功能，嘿嘿嘿


安装依赖
-------

```
$ sudo pip install https://www.djangoproject.com/download/1.7c2/tarball/
$ sudo pip install django-markdown
```


初始化项目
--------

```
$ django-admin.py startproject django_cms
```

tips: 如果忘记 django-admin 的参数，可以直接输入

```
$ django-admin.py | less
```
看一下生成的代码结构

```
$ tree
.
├── django_cms
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── README.md
```

启动 Debug 服务

```
$ python manage.py migrate
$ python manage.py runserver
```

创建一个名为 articles　的 App

```
$ python manage.py startapp articles
```

App 的代码结构

```
$ tree articles/
articles/
├── admin.py
├── __init__.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py
```

写完 models 模块之后，运行

```
$ python manage.py makemigrations articles
$ python manage.py migrate
```

写完 amdin 模块之后，运行
```
$ python manage.py createsuperuser
```
然后访问 http://localhost:8000/admin



