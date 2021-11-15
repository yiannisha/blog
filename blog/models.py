from django.db import models

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name.capitalize()}'

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

    def __str__(self):
        return f'{self.title.capitalize()}'

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return f'written by {self.author} on {self.created_on.date()}'
