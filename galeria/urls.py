from django.conf.urls import include, url
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

"""urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('galeria', views.galeria, name='galeria'),
    path('formulario', views.formulario, name='formulario')
]"""

app_name='galeria'

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^index/',views.index, name='index'),
    url(r'^galeria/',views.galeria, name='galeria'),
    url(r'^formulario/',views.formulario, name='formulario'),


]

urlpatterns += staticfiles_urlpatterns()
