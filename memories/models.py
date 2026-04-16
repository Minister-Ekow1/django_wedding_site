from django.db import models

class Memory(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='memories/images/', blank=True, null=True)
    video = models.FileField(upload_to='memories/videos/', blank=True, null=True)
    story = models.TextField(blank=True)
    caption = models.CharField(max_length=255)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title