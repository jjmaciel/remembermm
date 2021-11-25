from django.urls import path
from .views.views_home import home
from .views.views_edit import editData
from .views.views_remove import removeData
from .views.views_search import search

urlpatterns = [
    path('', home, name='home'),
    path('edit-data/<int:id>', editData, name="edit-data"),
    path('remove-data/<int:id>', removeData, name="remove-data"),
    path('search', search, name='search'),
]