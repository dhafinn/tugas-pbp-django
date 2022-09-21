from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers
# Create your views here.

def show_movie (request):
    watched_count = MyWatchList.objects.all().filter(watched = True).count()
    unwatched_count = MyWatchList.objects.all().filter(watched = False).count()
    data_movie = MyWatchList.objects.all()
    context = {
        'list_movie': data_movie
    }
    if (watched_count > unwatched_count):
        return render(request, "mywatchlistdone.html", context)
    else:
        return render(request, "mywatchlistundone.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


