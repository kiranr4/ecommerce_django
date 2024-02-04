# 1. Setup Project

    - Create a virtual env, activate, install django
    */ python -m venv venv /*
    */ venv\Scripts\activate /*
    */ pip install django /*

    - Create new project ecommerce
    */ django-admin startproject ecommerce /*

    - Create new app ecom (or core/main)
    */ python manage.py startapp ecom /*

    - Configure app in settings.py
    INSTALLED_APPS = ['ecom',]

    - import os in settings.py

    - Configure templates in settings.py 
    TEMPLATES = [{'DIRS': [os.path.join(BASE_DIR, 'templates')],}]

    - Confifure static
    STATIC_URL = 'static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'staticfiles')]

    - Configure Media
    MEDIA_URL = 'media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')