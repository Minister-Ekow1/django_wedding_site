from django.db import models

class About(models.Model):
    title = models.CharField(max_length=200, default="Our Love Story")
    story = models.TextField()

    def __str__(self):
        return self.title

class AboutImage(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='about/', blank=True, null=True)

    def __str__(self):
        return f"Image for {self.about.title}"

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
    
class SiteSettings(models.Model):
    site_name = models.CharField(
        max_length=200,
        default="Odoyewu Wedding"
    )

    bride_name = models.CharField(
        max_length=100
    )

    groom_name = models.CharField(
        max_length=100
    )

    wedding_date = models.DateField()

    logo = models.ImageField(
        upload_to="site/logo/",
        blank=True,
        null=True
    )

    hero_video = models.FileField(
        upload_to="site/videos/",
        blank=True,
        null=True
    )

    background_music = models.FileField(
        upload_to="site/music/",
        blank=True,
        null=True
    )

    theme_color = models.CharField(
        max_length=20,
        default="#d63384"
    )

    countdown_title = models.CharField(
        max_length=200,
        default="Countdown to Forever"
    )

    def __str__(self):
        return "Site Settings"