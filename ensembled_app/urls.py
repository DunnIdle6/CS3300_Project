from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LoginView.as_view(), name='logout'),

    #each band's individual page
    path('bands/<int:pk>', views.BandDetailView.as_view(), name='band-detail'),
    #page for a list of bands
    path('bands/', views.BandsListView.as_view(), name='bands'),
    #page to create/update/delete a band
    path('bands/create/', views.BandCreate, name='band-create'),
    path('bands/update/<int:pk>', views.BandUpdate, name='band-update'),
    path('bands/delete/<int:pk>', views.BandDelete, name='band-delete'),

    #page for list of musicians
    path('musicians/', views.MusicianListView.as_view(), name='musicians'),
    #page for individual musician
    path('musicians/<int:pk>', views.MusicianDetailView.as_view(), name='musician-detail'),
    #crude pages for musicians
    path('musician/create/', views.MusicianCreate, name='musician-create'),
    path('musician/update/<int:pk>', views.MusicianUpdate, name='musician-update'),
    path('musician/delete/<int:pk>', views.MusicianDelete, name='musician-delete'),

    path('calendar/', views.CalendarView.as_view(), name='calendar'),
]
