from django.db import models

class Country(models.Model):
    name = models.TextField()
    discription = models.CharField(max_length=5000)
    youtube_url = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
class Exclusive(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    duration = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    
class About_company(models.Model):
    discription = models.CharField(max_length=5000)
    img = models.ImageField('/company_imgs')

    def __str__(self) -> str:
        return self.discription
    
class News(models.Model):
    name = models.CharField(max_length=20)
    discription = models.CharField(max_length=5000)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    img = models.ImageField('/news_imgs')
    appeal = models.CharField(max_length=5000)

    def __str__(self) -> str:
        return self.name
    
class Commit(models.Model):
    name = models.TextField()
    discription = models.CharField(max_length=5000)

    def __str__(self) -> str:
        return self.name
    
class Appeal(models.Model):
    name = models.TextField()
    phone_number = models.CharField(max_length=30)
    emile = models.EmailField()
    message = models.TextField()
    title = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
class Contact(models.Model):
    area = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=30)
    emile = models.EmailField()
    location = models.CharField(max_length=50)
    telegram = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.area
    
class User(models.Model):
    name = models.CharField(max_length=50)
    emile = models.EmailField()
    phone_number = models.CharField(max_length=30)
    check_admin = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name