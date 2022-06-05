from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from .models import Genre, TopTen
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.conf import settings

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
        form = BookForm()
        return render(request, 'catalog.html', context={"genre": genre, "form": form})
    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            # book = form.cleaned_data['book']
            # rate = form.cleaned_data['rate']
            # description = form.cleaned_data['description']
            form.save(commit=True)
        return HttpResponse("Thank you for your recommendation!")

class AddRecommendationView(View):
    def get(self, request):
        user = request.user
        if not user.is_authenticated:
            return redirect('/login')
        else:
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


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login_form.html', {'form': form})
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['login'],
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                next_parameter = request.GET.get('next')
                if next_parameter:
                    return redirect(next_parameter)
                return HttpResponseRedirect('/add-recommendation')
            else:
                return HttpResponseRedirect('/add-user')
        return render(request, 'login_form.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/main')

class AddUserView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "add_user_form.html", {"form": form})
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks')
        return render(request, "add_user_form.html", {"form": form})

class UserListView(View):
    def get(self, request):
        user = request.user
        if not user.is_authenticated:
            return redirect('/login')
        else:
            form = UserListForm()
            userlist = UserList.objects.all()
            return render(request, "my-list.html", {"userlist": userlist, "form": form})
    def post(self,request):
        form = UserListForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return HttpResponse("Your choose has been saved!")

class TopTenView(View):
    def get(self, request):
        items = TopTen.objects.all()
        return render(request, "top-ten.html", {"items" : items})

