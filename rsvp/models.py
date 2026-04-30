from django.db import models

class RSVP(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    attending = models.BooleanField()
    guests = models.IntegerField(default=1)
    dietary_preferences = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class RSVPContact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name