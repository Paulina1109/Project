from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from .models import Genre, TopTen
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.conf import settings


# Main page of the application
class MainPage(View):
    def get(self, request):
        return render(request, 'main.html')


# Home view with all the functionalities to enter
class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

# Contact form to sent the request
class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')
    def post(self, request):
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        country = request.POST["country"]
        subject = request.POST["subject"]
        return render(request, 'contact.html', {"firstname": firstname})


# Recommendation view to check the books that are recommended by the user who were logged in
class RecommendationView(View):
    def get(self, request):
        book = Recommendation.objects.all()
        return render(request, 'recommendation.html', context={"book": book})


# Recommendation view available to all users to check the database of books
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


# Add_Recommendation View for users who are logged in, to recommend books from database
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

# Login view for users wanted to access Add Recommendation or My View page
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

# Once enter /logout the user is logged out from app
class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/main')

# If user is not in database, the web is redirected to create user
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


#My list view for users logged in
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
        return HttpResponse("Your choice has been saved!")

#View for Top10 books recommended by web creator
class TopTenView(View):
    def get(self, request):
        items = TopTen.objects.all()
        return render(request, "top-ten.html", {"items" : items})

