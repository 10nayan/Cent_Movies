from django.db import models
# Create your models here.
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
    def __str__(self):
        return f"{self.Name} {self.ReleaseYear}"
    def show_name(self):
        if len(self.Name)>16:
            return self.Name[:14]+".."
        else:
            return self.Name
    def search_trailler(self):
        search_string=self.Name.replace(' ','+')
        search_string+="+trailler"
        return search_string
class Review(models.Model):
    Name=models.CharField(max_length=30)
    Review=models.CharField(max_length=50)
    Date=models.DateField(auto_now_add=True)
    MovieLinked=models.ForeignKey(Movies, on_delete=models.CASCADE,related_name='movie_review')
