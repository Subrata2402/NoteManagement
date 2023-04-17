from django.urls import path
from questions import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('topic', views.topic, name='topic'),
    path('dbms', views.dbms, name='dbms'),
]