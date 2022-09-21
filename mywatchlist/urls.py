from django.urls import path
from mywatchlist.views import show_movie, show_json, show_xml, show_json_by_id, show_xml_by_id

app_name = "mywatchlist"

urlpatterns = [
    path('', show_movie, name = "show_movie"),
    path('html/', show_movie, name = "show_movie"),
    path('xml/', show_xml, name = "show_xml"),
    path('json/', show_json, name = "show_json"),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
]