from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index, name='index'),
    url(r'^signout/$',views.signout,name='signout'),
    url(r'^neighborhood/(\d+)',views.neighborhood,name='neighborhood'),
    url(r'^profile/(\d+)',views.profile,name='profile'),
]