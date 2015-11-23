from django.db import models


class Category(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)


class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category)
    last_updated = models.DateTimeField(auto_now=True)
    image = models.CharField(blank=True, null=True, max_length=100)


class Access(models.Model):
    time = models.DateTimeField(auto_now=True)
    ip = models.CharField(blank=True, max_length=100)

    @staticmethod
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0]
        return request.META.get('REMOTE_ADDR')
