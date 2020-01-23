from django.conf.urls import include, url
from django.urls import path
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
#from apps.galeria.views import index

app_name='galeria'

urlpatterns = [
    path('', views.index, name='index'),
    path('galeria/', views.galeria, name='galeria'),
    path('formulario/', views.formulario, name='formulario')
]



"""urlpatterns = [
    url(r'^$', 'index', name='index'),
    url(r'^index/',views.index, name='index'),
    url(r'^galeria/',views.galeria, name='galeria'),
    url(r'^formulario/',views.formulario, name='formulario'),


]"""

urlpatterns += staticfiles_urlpatterns()
