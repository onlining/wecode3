from django.db import models

class Actors(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    date_of_birth=models.DateField()
    movie=models.ManyToManyField("Movies",through="Actors_Movies")
    
    class Meta:
        db_table="actors"

class Movies(models.Model):
    title=models.CharField(max_length=45)
    release_date=models.DateField()
    running_time=models.IntegerField()

    class Meta:
        db_table="movies"

    

# Create your models here.
class Actors_Movies(models.Model):
    actor=models.ForeignKey(Actors, on_delete=models.CASCADE,null=True)
    movie=models.ForeignKey(Movies, on_delete=models.CASCADE,null=True)

    class Meta:
        db_table="actors_movies"