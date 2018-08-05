from django.urls import path

from . import views

app_name = 'write'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/posting/', views.posting, name='posting'),
    path('<int:id>/save/', views.save, name='save'),
]
