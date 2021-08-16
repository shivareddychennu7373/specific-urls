from django.conf import urls
from django.urls import path
from app1 import views
app_name='app1'
urlpatterns=[
    path('madan/',views.hello,name='madan')
]