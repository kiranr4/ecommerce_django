## RK Custom added (urls.py page)
from django.urls import path

from ecom import views
# from ecom.views import *

urlpatterns = [
    path("", views.index)
]

