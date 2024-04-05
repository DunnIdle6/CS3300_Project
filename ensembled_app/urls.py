from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LoginView.as_view(), name='logout'),

    #each band's individual page
    path('band/<int:pk>', views.BandDetailView.as_view(), name='band-detail'),

    #page for a list of bands
    path('bands/', views.BandsListView.as_view(), name='bands'),

    #page for list of musicians
    path('musicians/', views.MusicianListView.as_view(), name='musicians'),

    #page for individual musician
    path('musician/<int:pk>', views.MusicianDetailView.as_view(), name='musician-detail'),
]
