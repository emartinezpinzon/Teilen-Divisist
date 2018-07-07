from django.conf.urls import url

from Apps.usuario import views
from django.urls import path

urlpatterns = [
    path('estudiante/', views.EstudianteLogin.as_view()),
    path('docente/', views.DocenteLogin.as_view())
]
