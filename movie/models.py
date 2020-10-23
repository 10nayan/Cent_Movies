from django.db import models
from django.conf import settings
# Movies model is created here
class Movies(models.Model):
    Director=models.CharField(max_length=30)
    Cast_I=models.CharField(max_length=30)
    Cast_II=models.CharField(max_length=30)
    Name=models.TextField()
    ReleaseYear=models.IntegerField()
    ImdbRating=models.CharField(max_length=3)
    Genre=models.TextField(null=True)
    Language=models.CharField(max_length=20,null=True)
    Like=models.IntegerField()
    Dislike=models.IntegerField()
    avail=models.TextField(null=True)
    #this method returns string representation of an object
    def __str__(self):
        return f"{self.Name} {self.ReleaseYear}"
    #this method returns a movie name with "..." after the name if length of name >16 
    def show_name(self):
        if len(self.Name)>16:
            return self.Name[:14]+".."
        else:
            return self.Name
    #this method returns replaces spaces with plus sign for searching in youtube
    def search_trailler(self):
        search_string=self.Name.replace(' ','+')
        search_string+="+trailler"
        return search_string
#this is Review model defined here, which also has a foregin key that linked to a movie object
class Review(models.Model):
    Name=models.CharField(max_length=30)
    Review=models.CharField(max_length=50)
    Date=models.DateField(auto_now_add=True)
    MovieLinked=models.ForeignKey(Movies, on_delete=models.CASCADE,related_name='movie_review')
#this is Profile model defined here, which  has two foregin key that linked to a movie object and User object
class Profile(models.Model):
    Watch_list=models.ForeignKey(Movies, on_delete=models.CASCADE,related_name="watch_later",null=True)
    ProfileLinked=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='user')
#this is ProfileLikedMovie model defined here, which  has two foregin key that linked to a movie object and User object
class ProfileLikedMovie(models.Model):
    Liked_list=models.ForeignKey(Movies, on_delete=models.CASCADE,related_name="like_later",null=True)
    ProfileLinked=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='userliked')
#this is ProfileDislikedMovie model defined here, which  has two foregin key that linked to a movie object and User object
class ProfileDislikedMovie(models.Model):
    Dislike_list=models.ForeignKey(Movies, on_delete=models.CASCADE,related_name="dislike_later",null=True)
    ProfileLinked=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='userdisliked')
