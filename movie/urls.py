from django.urls import path
from .views import IndexView,MovieListView,search,MovieDetailView,genrelist_view,groupby_list_view,movie_list_view,like_this_movie,dislike_this_movie,about
urlpatterns=[
    path('', IndexView.as_view(),name='index'),
    path('list', MovieListView.as_view(),name='list'),
    path('search',search,name='search'),
    path('<int:pk>/detail',MovieDetailView.as_view(),name='detail'),
    path('list/<str:genre>',genrelist_view,name='genre'),
    path('<str:groupby_arg>',groupby_list_view,name='groupby'),
    path('<str:groupby_arg>/<str:arg>',movie_list_view,name='new_list'),
    path('list/<int:key>/like',like_this_movie,name='like'),
    path('list/<int:key>/dislike',dislike_this_movie,name='dislike'),
    path('/about',about, name='about')
]