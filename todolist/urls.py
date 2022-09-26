from django.urls import path
from todolist.views import logout_user, register, user_login, logout, show_todolist, user_login, upload

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', upload, name='upload'),
]