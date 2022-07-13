from django.db import models


class Location(models.Model):
    title = models.CharField(max_length=233)
    image = models.ImageField(upload_to='loc', blank=True, null=True)
    desc = models.TextField()
    maps = models.URLField(blank=True, null=True)
    history = models.TextField()

    def str(self):
        return self.title


class Tur(models.Model):
    title = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    desc = models.TextField()
    price = models.IntegerField()
    duration = models.CharField(max_length=344)
    ocupation = models.IntegerField(verbose_name='множество')

    def str(self):
        return self.title


class Gallery(models.Model):
    title = models.CharField(max_length=344)
    image = models.ImageField(upload_to='tur_gallery', blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def str(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=344)
    image = models.ImageField(upload_to='event_img', blank=True, null=True)
    duration = models.CharField(max_length=344)