from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_catalog (request):
    data_catalog = CatalogItem.objects.all()
    context = {
        'list_catalog': data_catalog,
        'name': "Dhafin R. Juliawan",
        'student_id': "2106650304"
    }
    return render(request, "katalog.html", context)
