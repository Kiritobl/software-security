"""
Django settings for OurWeb project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os

# BASE_DIR：这个变量指定了项目的根目录路径。在这个例子中，它通过使用Path(__file__).resolve().parent.parent获取了当前文件的绝对路径，并向上两级目录，得到了项目的根目录。
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECRET_KEY：这个变量是用于加密敏感信息的密钥。在生产环境中，应该将其设置为一个随机且安全的字符串，并保持秘密。
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-fp%i4$w4jr+d6&bx4er22qig%8!=*8-@yxgqxsj%7wznwr*)q@'

# DEBUG：这个变量用于设置调试模式。在开发阶段，可以将其设置为True以启用调试模式，但在生产环境中应该将其设置为False。
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS：这个变量指定了允许访问项目的主机名或IP地址。在这个例子中，设置为["*"]表示允许任何主机访问。
ALLOWED_HOSTS = ["*"]

# Application definition

# INSTALLED_APPS：这个变量列出了安装的Django应用程序。在这个例子中，meals是一个自定义的应用程序，它被添加到了这个列表中。
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'meals',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'OurWeb.urls'

# TEMPLATES：这个变量定义了Django模板引擎的配置。在这个例子中，使用了Django默认的模板引擎，并设置了模板文件的搜索路径为BASE_DIR / 'templates'。
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'OurWeb.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES：这个变量指定了数据库的连接设置。在这个例子中，使用了SQLite数据库，并设置了数据库文件的路径为BASE_DIR / 'db.sqlite3'。
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sql_meal',
        'USER': 'root',
        'PASSWORD':'sjtu0408!',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# STATIC_URL：这个变量指定了静态文件的URL前缀。在这个例子中，静态文件的URL将以static/开头。
STATIC_URL = 'static/'

# STATICFILES_DIRS：这个变量指定了其他静态文件目录的路径。在这个例子中，指定了一个静态文件目录os.path.join(BASE_DIR, "/static/")。
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'meals', 'static'),
)

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# MEDIA_URL和MEDIA_ROOT：这两个变量指定了媒体文件的URL前缀和存储路径。在这个例子中，媒体文件将以/media/开头，并存储在BASE_DIR / 'media'目录中。
# 媒体文件地址
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
