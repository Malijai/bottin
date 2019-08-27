from django.urls import path
from . import views


urlpatterns = [
    path('pdf/<int:pk>/',views.some_pdf, name='bsome_pdf'),
    path('listeb.html', views.extractionb, name='listeressources'),
]




