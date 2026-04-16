from django.db import models

class ProgramEvent(models.Model):
    time = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.time} - {self.title}"