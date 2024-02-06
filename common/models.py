from django.db import models


class BaseModel:
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Profile(models.Model):
    full_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='profile/')
    bio = models.TextField()

    def __str__(self):
        return self.full_name


class Skill(models.Model):
    title = models.CharField(max_length=255)
    percentage = models.IntegerField()
    order = models.IntegerField()

    def __str__(self):
        return self.title


class About(models.Model):
    experience = models.TextField()
    total_products = models.IntegerField()
    salary = models.IntegerField(default=100)

    def __str__(self):
        return str(self.id)


class Post(models.Model):
    author = models.CharField(max_length=255)
    title = models.TextField()
    description = models.TextField(null=True, blank=True)
    count_views = models.PositiveBigIntegerField(default=1)
    image = models.ImageField(upload_to='post/')

    def __str__(self):
        return self.author


class Service(models.Model):
    title = models.TextField(null=True, blank=True)
    icon = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)


class Category(models.Model):
    name = models.CharField(max_length=255)


class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    used_tools = models.ManyToManyField(Skill)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    completed_at = models.DateTimeField(auto_now=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='portfolio/')
