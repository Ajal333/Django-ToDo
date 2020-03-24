from django.conf.urls import url
from todo_app import views

urlpatterns = [
    url(r'^$',views.view,name='index'),
    url(r'^addcat/$',views.add_category,name='add_category'),
    url(r'^addlist/$',views.add_list,name='add_list'),
    url(r'^view/$',views.view,name='view'),
    url(r'^delete/list/(?P<list1>\w+)/$',views.del_list,name='del_list'),
    url(r'^delete/category/(?P<cat>\w+)/$',views.del_cat,name='del_cat'),
]