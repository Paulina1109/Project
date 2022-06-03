"""Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from books.views import MainPage, ContactView, HomeView, RecommendationView, CatalogView, AddRecommendationView, AddUserView, LogoutView, LoginView, UserListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', MainPage.as_view(), name='main'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('home/', HomeView.as_view(), name='home'),
    path('recommendation/', RecommendationView.as_view(), name='recommendation'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('add-recommendation', AddRecommendationView.as_view(), name='Add-recommendation'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('add-user/', AddUserView.as_view(), name='add-user'),
    path('my-list/', UserListView.as_view(), name='my-list'),
]