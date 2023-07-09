from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    image = models.ImageField(upload_to='movies/files/covers')

    def __str__(self):
        return f'{self.title} from {self.year}' 