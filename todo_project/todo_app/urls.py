from django.contrib import admin
from django.urls import path,include

from . import views
app_name='todo_app'

urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('taskview/',views.TaskListView.as_view(),name='taskview'),
    path('detail/<int:pk>/',views.DetailListView.as_view(),name='detail'),
    path('cbvupdate/<int:pk>/',views.UpdateListView.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.DeleteListView.as_view(),name='cbvdelete'),

]
