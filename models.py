from django.db import models

class Song(models.Model):

    title = models.TextField()
    length = models.PositiveIntegerField(help_text="in Minutes")
    release_date = models.DateField()
    artists = models.ManyToManyField('Artist')

    def __str__(self): return self.title

class Artist(models.Model):

    CHOICES = (
        ('p' , 'Pop'),
        ('r' , 'Rock'),
        ('o' , 'Other')
    )

    name = models.TextField()
    genre = models.CharField(max_length=1,choices=CHOICES)

    def __str__(self): return self.name