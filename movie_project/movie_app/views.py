from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy 
from .forms import Movieform, LoginForm, RegisterForm,EditUserProfileForm, ReviewForm
from django.views import generic
from . models import  Category, Movie, Review
from django.contrib.auth.models import User
from django.contrib import messages , auth
from django.contrib.auth.models  import User
from django.views.generic import  ListView
from django.db.models import Q



# Create your views here.
# Home page


def index(request,):
    
    movie=Movie.objects.all()
    p_category = Category.objects.all()


    
    context={
        'movie_list':movie,
        'p_category':p_category
     }
    
    return render(request,"index.html",context)


def detail(request,Movie_id):
     movie=Movie.objects.get(pk=Movie_id)
     
    
     reviews = Review.objects.filter(movie=movie).order_by("comment")
     average = reviews.aggregate()
    
     return render(request,"detail.html",{'movie':movie,'reviews': reviews})

def add_movie(request):
     p_category = Category.objects.all()
     if request.method=="POST":
          title=request.POST.get('title')
          description=request.POST.get('description')
          category = Category.objects.get(id = request.POST['category'])

          poster=request.FILES['img']
          actors=request.POST.get('actors')
          trailer_link=request.POST.get('trailer_link')
          release_date =request.POST.get('release_date')
          added_by = request.user
          movie=Movie(title=title,description=description,category=category,poster=poster,trailer_link=trailer_link,release_date=release_date,actors=actors,added_by=added_by)
          
          
          
          movie.save()
          return redirect('home')
          
          
     return render(request,"add.html",{'p_category':p_category})

def update(request,id):
     movie=Movie.objects.get(id=id)
     request_user=request.user
     
        
     form=Movieform(request.POST or None, request.FILES,instance=movie)
     if form.is_valid():
          form.save()
          return redirect('home')
     return render(request, 'update.html',{'form':form,'movie':movie,"request_user": request_user})

def delete(request,id):
     if request.method=='POST':
          movie=Movie.objects.get(id=id)
          
       
          movie.delete()
          return redirect('home')
     return render(request,'delete.html')

# signup page
def user_signup(request):
     if request.method =="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.info(request,"username is already exists")
            return redirect('signup')
        elif User.objects.filter(email=email).exists(): 
            messages.info(request,"email is already exists")
            return redirect('signup')
        else:
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            user.save();
            return redirect('login')
     else:
         return render(request, 'register.html')   
    # if request.method == 'POST':
    #     form = SignupForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         login(request, user)
    #         messages.success(request, "Registration successful." )
    #         return redirect("main:homepage")
    #     messages.error(request, "Unsuccessful registration. Invalid information.")
    # form = SignupForm()
    # return render (request=request, template_name="register.html", context={"register_form":form})
        

# login page
def user_login(request):
    if request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,"Invalid login")
            return redirect('login')
    return render(request,'login.html')
    
#    

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')

class UpdateUserView(generic.UpdateView):
    form_class = EditUserProfileForm
    template_name = "edit_user_profile.html"
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
    
def add_review(request, id):
      if request.user.is_authenticated:
        
        movie = Movie.objects.get(id=id)
        if request.method == "POST":
            
            form = ReviewForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.comment = request.POST["comment"]
                data.rating = request.POST["rating"]
                data.user = request.user
                data.movie = movie
                data.save()
                return redirect("detail", id)

        else:
            form = ReviewForm()

        return render(request, 'detail.html', {"form": form})
    
      return redirect("login") 

def edit_review(request, movie_id, review_id):
    if request.user.is_authenticated:
        movie = Movie.objects.get(id=movie_id)
        review = Review.objects.get(movie=movie, id=review_id)

        if request.user == review.user:
            if request.method == "POST":
                form = ReviewForm(request.POST, instance=review)
                if form.is_valid():
                    data = form.save(commit=False)
                    if (data.rating > 10) or (data.rating < 0):
                        error = "Out of range. Select value from 0 to 10."
                        return render(request, 'editreview.html', {"error": error, "form": form})
                    else:
                        data.save()
                        return redirect("detail", movie_id)
            else:
                form = ReviewForm(instance=review)
            return render(request, 'editreview.html', {"form": form})
        else:
            return redirect("detail", movie_id)

def delete_review(request, movie_id, review_id):
    if request.user.is_authenticated:
        movie = Movie.objects.get(id=movie_id)
        review = Review.objects.get(movie=movie, id=review_id)

        if request.user == review.user:
            review.delete()
        return redirect("detail", movie_id)
    else:        
        return redirect("login") 
    


class SearchResultsView(ListView):
    model = Movie
    template_name = 'search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Movie.objects.filter(
            Q(title__icontains=query) 
        )
        return object_list
    
def category_detail(request, pk):
     category = get_object_or_404(Category, pk=pk)
     movies = category.get_movies()
     return render(request, 'category_detail.html', {'category': category, 'movies': movies})