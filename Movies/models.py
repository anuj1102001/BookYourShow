from django.db import models
from django.utils.text import slugify

# Create your models here.

genres = [
    ['action','Action'],
    ['comedy','Comedy'],
    ['drama','Drama'],
    ['fantasy','Fantasy'],
    ['horror','Horror'],
    ['romance','Romance'],
    ['thriller','Thriller'],
]

languages = [
    ['english', 'English'],
    ['hindi', 'Hindi'],
    ['kannada','Kannada'],
    ['tamil','Tamil'],
    ['telugu','Telugu'],
    ['malayalam','Malayalam']
]


class Movies(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255,choices=genres)
    language = models.CharField(max_length=255, choices=languages)
    synopsis = models.TextField()
    cast = models.TextField()
    duration_minutes = models.IntegerField()
    release_date = models.DateField()
    trailer_url = models.CharField(max_length=2000, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    image_url=models.URLField(max_length=800, null=True, blank=True)
    slug=models.CharField(max_length=2000, null=True, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug: 
            self.slug = slugify(self.title)
        super(Movies, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    def get_genre_display(self):
        return dict(genres).get(self.genre, self.genre)

    def get_language_display(self):
        return dict(languages).get(self.language,self.language)
    
