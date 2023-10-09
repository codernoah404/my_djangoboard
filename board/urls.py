from django.urls import path

from . import views

app_name = "board"

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.board_list, name='main'),
    path('<int:board_id>', views.board_detail, name='detail'),
    path('comments/', views.comment_list, name='comment_list'),
    path('create/', views.create, name='write'),
    path('<int:board_id>/edit', views.board_edit, name='edit'),

]