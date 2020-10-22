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
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.
class IndexView(View):
    template_name='movie/index.html'
    def get(self,request):
        return render (request,self.template_name,{})
class MovieListView(ListView):
    template_name='movie/list.html'
    queryset=Movies.objects.all().order_by('id')
    paginate_by=8
class MovieDetailView(DetailView):
    template_name='movie/detail.html'
    queryset=Movies.objects.all()
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['form']=ReviewForm()
        return context
    """
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,{'form':ReviewForm()})
    """
    def post(self,request,**kwargs):
        primary_key=kwargs['pk']
        form=ReviewForm(request.POST)
        if form.is_valid():
            mform=form.save(commit=False)
            mform.MovieLinked=Movies.objects.get(pk=primary_key)
            mform.save()
            return redirect(f'/{primary_key}/detail')
    """
    def get_success_url(self):
        return reverse('list')
    """
def genrelist_view(request,genre):
    movies_list=Movies.objects.filter(Genre__contains=genre)
    paginator = Paginator(movies_list,8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'movie/genre.html',{'page_obj': page_obj,'genre':genre})
def groupby_list_view(request,groupby_arg):
    movies_list=Movies.objects.all()
    page_obj=[]
    if groupby_arg=='Director':
        director_list=sorted(set([i.Director for i in movies_list]))
       # cmn_dir_list=list(set([i for i in director_list if director_list.count(i)>2]))
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
    """
def movie_list_view(request,groupby_arg,arg):
    movies_list=Movies.objects.all().order_by('id')
    if groupby_arg=='Director':
        movies_list=Movies.objects.filter(Director=arg)
    if groupby_arg=='Year':
        movies_list=Movies.objects.filter(ReleaseYear=arg)
    if groupby_arg=='Language':
        movies_list=Movies.objects.filter(Language=arg)
    if groupby_arg=='Cast':
        movies_list=Movies.objects.filter(Cast_I=arg)| Movies.objects.filter( Cast_II=arg)
    paginator = Paginator(movies_list,8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'movie/genre.html',{'page_obj': page_obj,'genre':groupby_arg})
    """
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
    """
def like_this_movie(request,key):
    obj=Movies.objects.get(pk=key)
    obj.Like+=1
    obj.save()
    if request.user.is_authenticated:
        usrname=request.user.get_username()
        user=User.objects.get(username=usrname)
        try:
            ProfileLikedMovie.objects.get(Liked_list=obj,ProfileLinked=user)
        except:
            profile=ProfileLikedMovie(Liked_list=obj,ProfileLinked=user)
            profile.save()
        return JsonResponse({'success':True,'content':'Like','Like':obj.Like})
    return JsonResponse({'success':True,'content':'Like','Like':obj.Like})
    """
def like_this_movie(request,key):
    if request.session.get('visited_list') is None:
        request.session['visited_list']=[]
    #print(request.session.get('visited_list'))
    if (request.session.get('first_visit')==False)& (key in request.session.get('visited_list')):
        #print(request.session.get('first_visit'))
        return HttpResponse("You have already liked this, go back to home page")
    obj=Movies.objects.get(pk=key)
    obj.Like+=1
    obj.save()
    if request.user.is_authenticated:
        usrname=request.user.get_username()
        user=User.objects.get(username=usrname)
        try:
            ProfileLikedMovie.objects.get(Liked_list=obj,ProfileLinked=user)
        except:
            profile=ProfileLikedMovie(Liked_list=obj,ProfileLinked=user)
            profile.save()
        return JsonResponse({'success':True,'content':'Like','Like':obj.Like})
    request.session['first_visit']=False
    request.session['visited_list'].append(key)
    #print(request.session['visited_list'])
    return JsonResponse({'success':True,'content':'Like','Like':obj.Like})
def dislike_this_movie(request,key):
    if request.session.get('visited_lst') is None:
        request.session['visited_lst']=[]
    if (request.session.get('first_vst')==False)& (key in request.session.get('visited_lst')):
        print(request.session.get('first_visit'))
        return HttpResponse("You have already disliked this, go back to home page")
    obj=Movies.objects.get(pk=key)
    obj.Dislike+=1
    obj.save()
    if request.user.is_authenticated:
        usrname=request.user.get_username()
        user=User.objects.get(username=usrname)
        try:
            ProfileDislikedMovie.objects.get(Dislike_list=obj,ProfileLinked=user)
        except:
            profile=ProfileDislikedMovie(Dislike_list=obj,ProfileLinked=user)
            profile.save()
        return JsonResponse({'success':True,'content':'Dislike','Dislike':obj.Dislike})
    request.session['first_vst']=False
    request.session['visited_lst'].append(key)
    return JsonResponse({'success':True,'content':'Dislike','Dislike':obj.Dislike})
def search(request):
    search_obj=request.POST.get('search_obj')
    movies_list=Movies.objects.filter(Name__icontains=search_obj)
    paginator = Paginator(movies_list,100)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'movie/genre.html',{'page_obj': page_obj,'genre':'search'})
def about(request):
    return render(request,'movie/about.html')
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
def signout(request):
    logout(request)
    return redirect('/signin')
def profile_view(request):
    obj1=ProfileLikedMovie.objects.filter(ProfileLinked=request.user)
    obj2=ProfileDislikedMovie.objects.filter(ProfileLinked=request.user)
    obj3=Profile.objects.filter(ProfileLinked=request.user)
    return render (request,'movie/profile.html',{'object1':obj1,'object2':obj2,'object3':obj3})
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
def remove_from_watchlist(request,key):
    profile=Profile.objects.get(pk=key)
    profile.delete()
    return redirect('/profile')
