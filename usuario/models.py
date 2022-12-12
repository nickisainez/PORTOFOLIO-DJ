from django.db import models
from taggit.managers import TaggableManager


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to="portfolio/images")
    url = models.URLField(blank=False)
    tags = TaggableManager()

    def __str__(self):
        return self.title
