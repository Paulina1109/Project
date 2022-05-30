from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import Genre, Recommendation
from .forms import RecommendationForm

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
        book = Recommendation.objects.all()
        return render(request, 'recommendation.html', context={"book": book})

class CatalogView(View):
    def get(self, request):
        genre = Genre.objects.all()
        return render(request, 'catalog.html', context={"genre": genre})


class AddRecommendationView(View):
    def get(self, request):
        form = RecommendationForm()
        return render(request, 'add-recommendation.html', {'form': form})
    def post(self, request):
        form = RecommendationForm(request.POST)
        if form.is_valid():
            # book = form.cleaned_data['book']
            # rate = form.cleaned_data['rate']
            # description = form.cleaned_data['description']
            form.save(commit=True)
        return HttpResponse("Thank you for your recommendation!")

