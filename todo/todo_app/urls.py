from django.conf.urls import url
from todo_app import views

urlpatterns = [
    url(r'^$',views.view,name='index'),
    url(r'^addcat/$',views.add_category,name='add_category'),
    url(r'^addlist/$',views.add_list,name='add_list'),
    url(r'^view/$',views.view,name='view'),
]