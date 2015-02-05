from django.db import models


class Information(models.Model):
    """Presents information about me"""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    bio = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    photo = models.CharField(max_length=100, blank=True, default='/static/tasks/img/no-image.png')


class Middleware(models.Model):
    """Stores HTTP Requests"""
    date_time = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=10)
    http_referer = models.CharField(max_length=100)
    path = models.CharField(max_length=100)
    files = models.CharField(max_length=100)


class ImageUpload(models.Model):
    """Stores urls of uploaded images"""
    photo = models.ImageField(upload_to='tasks/photo/%Y/%m/%d')


class SignalLogEntry(models.Model):
    """Stores model operations"""
    date = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=50)
    model = models.CharField(max_length=50)