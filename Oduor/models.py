from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class stuffs(models.Model):
    name_of_tool = models.TextField()
    description = models.TextField(blank=True)
    tutorial_tool = models.TextField(blank=True)
    ad = models.TextField(blank=True, default=None, null=True)
    youtube_link = models.TextField(blank=True)
    #new field
    website_link = models.URLField(blank=True, null=True)
    categories = models.ManyToManyField(category)

    def __str__(self):
        return self.name_of_tool



