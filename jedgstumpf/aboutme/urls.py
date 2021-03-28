from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing, name='aboutme-home'),
    path('links/', views.links, name='aboutme-links'),
    path('resume', views.resume, name='aboutme-resume'),
    path('achievements', views.achievements, name='aboutme-achievements'),
]
