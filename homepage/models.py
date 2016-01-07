from django.db import models

"""
Cards
"""
class Category(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return title

class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category)
    last_updated = models.DateTimeField(auto_now=True)
    image = models.CharField(blank=True, null=True, max_length=100)

"""
Reviews
"""
class ReviewCategory(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return title

class Reviews(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True)
    category = models.ForeignKey(ReviewCategory)
    score = models.IntegerField()
    created = models.DateTimeField(auto_now=True)


"""
Blogs
"""
class BlogCategory(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return title

class Blog(models.Model):
    position = models.IntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.ForeignKey(BlogCategory)
    last_updated = models.DateTimeField(auto_now=True)

class Image(models.Model):
    image = models.ImageField()

"""
Access
"""
class Access(models.Model):
    time = models.DateTimeField(auto_now=True)
    ip = models.CharField(blank=True, max_length=100)

    @staticmethod
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0]
        return request.META.get('REMOTE_ADDR')
