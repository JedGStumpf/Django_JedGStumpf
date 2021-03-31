from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing, name='aboutme-home'),
    path('links/', views.links, name='aboutme-links'),
    path('myblog/', views.myblog, name='aboutme-myblog'),
    path('achievements/', views.achievements, name='aboutme-achievements'),
]
