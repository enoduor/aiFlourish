from django.db import models

class Tool(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    website_link = models.URLField()
    youtube_link = models.URLField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
