from django.urls import path
from .views import IndexView,MovieListView,register,signin,search,MovieDetailView,genrelist_view,groupby_list_view,movie_list_view,like_this_movie,dislike_this_movie,about,signout,profile_view,add_to_watchlist,remove_from_watchlist,signin
urlpatterns=[
    path('', IndexView.as_view(),name='index'),
    path('list', MovieListView.as_view(),name='list'),
    path('search',search,name='search'),
    path('<int:pk>/detail',MovieDetailView.as_view(),name='detail'),
    path('list/<str:genre>',genrelist_view,name='genre'),
    path('groupby/<str:groupby_arg>',groupby_list_view,name='groupby'),
    path('groupby/<str:groupby_arg>/<str:arg>',movie_list_view,name='new_list'),
    path('<int:key>/like',like_this_movie,name='like'),
    path('<int:key>/dislike',dislike_this_movie,name='dislike'),
    path('about',about, name='about'),
    path('register',register,name='register'),
    path('signin',signin,name='signin'),
    path('signout',signout,name='signout'),
    path('profile',profile_view,name='profile'),
    path('<int:key>/detail/watchlist',add_to_watchlist,name='watchlist'),
    path('<int:key>/detail/nowatchlist',remove_from_watchlist,name='nowatchlist')
]