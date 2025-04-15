from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('interests/', views.interest, name='interest'),
    path('portfolio/annee_<int:annee>/', views.annee, name='portfolio_annee'),
    path('portfolio/annee_<int:annee>/<str:sae>', views.sae, name='sae'),
]