from django.conf.urls import url
from .views import some_pdf, extractionb


urlpatterns = [
    url(r'^pdf/(?P<pk>[-\w]+)/$', some_pdf, name='bsome_pdf'),
    url(r'listeb.html', extractionb, name='listeressources'),
]

