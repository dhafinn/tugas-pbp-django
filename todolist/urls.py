from django.urls import path
from todolist.views import delete_data, logout_user, register, user_login, logout, show_todolist, user_login, upload, update_data, delete_data, show_json, add_todolist, delete_ajax

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', upload, name='upload'),
    path('update/<int:id>', update_data, name='update'),
    path('delete/<int:id>', delete_ajax, name='delete_ajax'),
    path('json', show_json, name='show_json'),
    path('add', add_todolist, name='add_todolist'),
]