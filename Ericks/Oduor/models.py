from django.db import models

# Create your models here.

class stuffs(models.Model):
    name_of_tool = models.TextField()
    description = models.TextField(blank=True)
    tutorial_tool = models.TextField(blank=True)
    ad = models.TextField(blank=True)
    youtube_link = models.TextField(blank=True)
    #new field
    website_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name_of_tool



