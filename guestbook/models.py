from django.db import models

class GuestMessage(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name