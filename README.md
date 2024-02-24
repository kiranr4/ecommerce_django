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

    - Create app/views
    def index(request):
    return render(request, "ecom\index.html")

    - Create app/URLs
    from ecom import views
    urlpatterns = [
    path("", views.index)
    ]

    - Create app/models
    class Cateory(models.Model):
    cat_id = models.AutoField(verbose_name="Category ID", primary_key=True)
    cat_title = models.CharField(verbose_name="Category Title", max_length=50, unique=True)
    cat_image = models.ImageField(verbose_name="Category Image", upload_to="img_category/", height_field=None, width_field=None, max_length=None)
    cat_dttm = models.DateTimeField(verbose_name="Date Added", auto_now=True, auto_now_add=True)
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.name


    