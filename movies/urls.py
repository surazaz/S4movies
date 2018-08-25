from django.conf.urls import url
from django.urls import path

from . import views
app_name='movies'

urlpatterns=[
    path('detail/<str:movietitle_or_id>/',views.detail),
    path('recom/',views.get_recom),
    path('all/',views.index)

    ]