from django.urls import path
from django.contrib import admin 
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("jobposts/",views.JobPostCreateList.as_view(),name= 'job-create'),
    path("admin/", admin.site.urls)
]
