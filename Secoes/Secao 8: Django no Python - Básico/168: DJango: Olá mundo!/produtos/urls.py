from django.urls import URLPattern, path
from . import views
# produtos
urlpatterns = [
    path('', views.metodo, name='metodo'),
]