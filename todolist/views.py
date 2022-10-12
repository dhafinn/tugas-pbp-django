import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core import serializers
from django.urls import reverse
from todolist.models import Task
from todolist.forms import TaskUpload
from django.views.decorators.csrf import csrf_exempt


@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.filter(user = request.user)
    context = {
        'todolist' : data_todolist
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def upload(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TaskUpload(request.POST)
        # check whether it's valid:
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            Task.objects.create(title=title, description=description, date=datetime.datetime.now(), user=request.user)
            return redirect('todolist:show_todolist')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TaskUpload()

    return render(request, 'forms.html', {'form': form})

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def update_data(request, id):
    todo = Task.objects.get(id = id)
    todo.is_finished = not(todo.is_finished)
    todo.save()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def delete_data(request, id):
    todo = Task.objects.get(id = id)
    todo.delete()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def show_json(request):
    data = Task.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def add_todolist(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        todolist = Task.objects.create(title=title, description=description,date=datetime.date.today(), is_finished=False, user=request.user)

        result = {
            'fields':{
                'title':todolist.title,
                'description':todolist.description,
                'is_finished':todolist.is_finished,
                'date':todolist.date,
            },
            'pk':todolist.pk
        }

        return JsonResponse(result)

@login_required(login_url='/todolist/login/')
@csrf_exempt
def delete_ajax(request, id):
    if request.method == "DELETE":
        todo = get_object_or_404(Task, id = id)
        todo.delete()
    return HttpResponse(status=202)
