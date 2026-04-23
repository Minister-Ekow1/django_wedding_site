from django.db import models

class About(models.Model):
    title = models.CharField(max_length=200, default="Our Love Story")
    subtitle = models.CharField(max_length=200, default="A journey written by fate")
    story = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)

    def __str__(self):
        return self.title


class Venue(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    embed_url = models.TextField(help_text="Paste Google Maps embed link")

    def __str__(self):
        return self.name


class LoveStoryEvent(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title