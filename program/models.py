from django.db import models

class Event(models.Model):
    time = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.time} - {self.title}"


class ProgramSettings(models.Model):
    title = models.CharField(max_length=200, default="Wedding Program Outline")
    poster = models.ImageField(upload_to='program/', blank=True, null=True)

    def __str__(self):
        return "Program Settings"