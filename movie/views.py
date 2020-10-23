from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from .models import Movies,Review,Profile,ProfileLikedMovie,ProfileDislikedMovie
from .forms import ReviewForm,UserForm
from django.views.generic import DetailView,ListView
from django.views import View
from django.urls import reverse
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
#user model is imported here
from django.contrib.auth import get_user_model
User = get_user_model()

#this index function render our home page
class IndexView(View):
    template_name='movie/index.html'
    def get(self,request):
        return render (request,self.template_name,{})

#this index function query through our database model Movies and render all the instances as a list
class MovieListView(ListView):
    template_name='movie/list.html'
    queryset=Movies.objects.all().order_by('id')
    paginate_by=8

#class based moviedetailview  used to query a particular row of 
#Movie model by its pk coloumn and render its details to html templates in a GET request
#but for a  POST request a review form is submitted in the movie instance   
class MovieDetailView(DetailView):
    template_name='movie/detail.html'
    queryset=Movies.objects.all()
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['form']=ReviewForm()
        return context

    def post(self,request,**kwargs):
        primary_key=kwargs['pk']
        form=ReviewForm(request.POST)
        if form.is_valid():
            mform=form.save(commit=False)
            mform.MovieLinked=Movies.objects.get(pk=primary_key)
            mform.save()
            return redirect(f'/{primary_key}/detail')
#this functionn takes an argument genre and renders genre wise movies list to web page
def genrelist_view(request,genre):
    movies_list=Movies.objects.filter(Genre__contains=genre)
    paginator = Paginator(movies_list,8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'movie/genre.html',{'page_obj': page_obj,'genre':genre})

#this view function takes an groupby argument and returns movies list categorized with the 
# input groupby argument and renders it
def groupby_list_view(request,groupby_arg):
    movies_list=Movies.objects.all()
    page_obj=[]
    if groupby_arg=='Director':
        director_list=sorted(set([i.Director for i in movies_list]))
        paginator = Paginator(director_list,12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    if groupby_arg=='Year':
        year_list=sorted(set([i.ReleaseYear for i in movies_list]))
        paginator = Paginator(year_list,12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    if groupby_arg=='Language':
        lang_list=list(set([i.Language for i in movies_list]))
        paginator = Paginator(lang_list,12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    if groupby_arg=='Cast':
        cast_list1=[i.Cast_I for i in movies_list]
        cast_list2=[j.Cast_II for j in movies_list]
        cast_list=sorted(set([*cast_list1,*cast_list2]))
        paginator = Paginator(cast_list,12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    return render(request,'movie/groupby.html',{'page_obj': page_obj,'groupby_arg':groupby_arg})
#this view function takes two argument, a groupby argument and a another argument then returns
# that particuler instances's detail view
def movie_list_view(request,groupby_arg,arg):
    main_movies_list=Movies.objects.all()
    if groupby_arg=='Director':
        movies_list=Movies.objects.filter(Director=arg)
        groupby_obj=sorted(set([i.Director for i in main_movies_list]))
    if groupby_arg=='Year':
        movies_list=Movies.objects.filter(ReleaseYear=arg)
        groupby_obj=sorted(set([i.ReleaseYear for i in main_movies_list]))
    if groupby_arg=='Language':
        movies_list=Movies.objects.filter(Language=arg)
        groupby_obj=list(set([i.Language for i in main_movies_list]))
    if groupby_arg=='Cast':
        movies_list=Movies.objects.filter(Cast_I=arg)| Movies.objects.filter( Cast_II=arg)
        cast_list1=[i.Cast_I for i in main_movies_list]
        cast_list2=[j.Cast_II for j in main_movies_list]
        groupby_obj=cast_list=sorted(set([*cast_list1,*cast_list2]))
    paginator = Paginator(groupby_obj,20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'movie/groupby_name.html',{'page_obj': page_obj,'genre':groupby_arg,'groupby_obj':groupby_obj,'movies_list':movies_list})

#this function takes a key as argument and send a AJAX request after which DOM field is updated
#according to the request, if a user is authorized , liked movie is also added to the users ProfileLikedMovie model
#if session's "first_visit" is True then user can like this movie but after every attempt it resets to False
# sessions "visited_list " is updated with movies object pk, after a user liked a movie object
def like_this_movie(request,key):
    obj=Movies.objects.get(pk=key)
    if request.session.get('visited_list') is None:
        request.session['visited_list']=[]
    if (request.session.get('first_visit')==False)& (key in request.session.get('visited_list')):
        return HttpResponse("You have already liked this, go back to home page")
    if request.user.is_authenticated:
        usrname=request.user.get_username()
        user=User.objects.get(username=usrname)
        try:
            ProfileLikedMovie.objects.get(Liked_list=obj,ProfileLinked=user)
            return JsonResponse({'success':False})
        except:
            obj.Like+=1
            obj.save()
            profile=ProfileLikedMovie(Liked_list=obj,ProfileLinked=user)
            profile.save()
            return JsonResponse({'success':True,'content':'Like','Like':obj.Like})

    obj.Like+=1
    obj.save()
    request.session['first_visit']=False
    request.session['visited_list'].append(key)
    return JsonResponse({'success':True,'content':'Like','Like':obj.Like})

#this function takes a key as argument and send a AJAX request after which DOM field is updated
#according to the request, if a user is authorized , disliked movie is also added to the users ProfileDisLikedMovie model
def dislike_this_movie(request,key):
    obj=Movies.objects.get(pk=key)
    if request.session.get('visited_lst') is None:
        request.session['visited_lst']=[]
    if (request.session.get('first_vst')==False)& (key in request.session.get('visited_lst')):
        print(request.session.get('first_visit'))
        return HttpResponse("You have already disliked this, go back to home page")
    if request.user.is_authenticated:
        usrname=request.user.get_username()
        user=User.objects.get(username=usrname)
        try:
            ProfileDislikedMovie.objects.get(Dislike_list=obj,ProfileLinked=user)
            return JsonResponse({'success':False})
        except:
            obj.Dislike+=1
            obj.save()
            profile=ProfileDislikedMovie(Dislike_list=obj,ProfileLinked=user)
            profile.save()
            return JsonResponse({'success':True,'content':'Dislike','Dislike':obj.Dislike})
    obj.Dislike+=1
    obj.save()
    request.session['first_vst']=False
    request.session['visited_lst'].append(key)
    return JsonResponse({'success':True,'content':'Dislike','Dislike':obj.Dislike})

#this function searches a movie object and renders to webpage
def search(request):
    search_obj=request.POST.get('search_obj')
    movies_list=Movies.objects.filter(Name__icontains=search_obj)
    paginator = Paginator(movies_list,100)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'movie/genre.html',{'page_obj': page_obj,'genre':'search'})

#this function renders about page
def about(request):
    return render(request,'movie/about.html')

#this function registers new user
def register(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully, signin now')
            return redirect('/signin')
    else:
        form=UserForm()
    return render(request,'movie/register.html',{'form':form})

#this function is for signin new user to application and redirects to home page
def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, f"You are now logged in as {username}")
            return redirect('/signin')
        else:
            messages.warning(request,"Invalid username or password")
            return redirect('/signin')
    return render (request,'movie/signin.html')

#this function signout already logged in user
def signout(request):
    logout(request)
    return redirect('/signin')

#this function returns a profile view associated with every user
def profile_view(request):
    obj1=ProfileLikedMovie.objects.filter(ProfileLinked=request.user)
    obj2=ProfileDislikedMovie.objects.filter(ProfileLinked=request.user)
    obj3=Profile.objects.filter(ProfileLinked=request.user)
    return render (request,'movie/profile.html',{'object1':obj1,'object2':obj2,'object3':obj3})

#this function takes pk of movies object as a input and tries to linked the movie 
#with current logged in user and saves that in Watchlater model
@login_required(login_url='signin')
def add_to_watchlist(request,key):
    usrname=request.user.get_username()
    obj=Movies.objects.get(pk=key)
    user=User.objects.get(username=usrname)
    try:
        Profile.objects.get(Watch_list=obj,ProfileLinked=user)
    except:
        profile=Profile(Watch_list=obj,ProfileLinked=user)
        profile.save()
    finally:
        return redirect('/profile')

#this function removes a movie instances from watch later
def remove_from_watchlist(request,key):
    profile=Profile.objects.get(pk=key)
    profile.delete()
    return redirect('/profile')
