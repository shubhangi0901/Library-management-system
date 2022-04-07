from django.urls import path
from .import views
urlpatterns=[

    path('', views.home, name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.usersignup, name='signup'),
    path('login/', views.userlogin, name='login'),

    path('logout/', views.userlogout, name='logout'),
    path('addbook/', views.addbook, name='addbook'),
    path('viewbook/', views.viewbook, name='viewbook'),
    path('deletebook/<int:id>/', views.deletebook, name='deletebook'),
    path('updatebook/<int:id>/', views.updatebook, name='updatebook'),

]