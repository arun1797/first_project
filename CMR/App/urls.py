from unicodedata import name
from . import views
from django.urls import path

urlpatterns=[
    path("",views.CMR_home,name="CMR_home"),
    path("CMR_dashboard",views.CMR_dashboard,name="CMR_dashboard"),
    path("CMR_archive",views.CMR_archive,name="CMR_archive"),

]