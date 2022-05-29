from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import Genre, Recommendation

class MainPage(View):
    def get(self, request):
        return render(request, 'main.html')

class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')
    def post(self, request):
        name = request.POST.get("firstname")
        return redirect("/main")

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class RecommendationView(View):
    def get(self, request):
        return render(request, 'recommendation.html')

class CatalogView(View):
    def get(self, request):
        genre = Genre.objects.all()
        return render(request, 'catalog.html', context={"genre": genre})


class AddRecommendationView(View):
    def get(self, request):
        return render(request, 'add-recommendation.html')
    def post(self, request):
        rate = request.POST.get("rate")
        description = request.POST.get("description")
        book = request.POST.get("book")
        Recommendation.objects.create(rate= rate, description= description, book= book)
        return redirect("/recommendation")
