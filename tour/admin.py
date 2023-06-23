from django.contrib import admin
from .models import (
    Country,
    Exclusive,
    About_company,
    News,
    Commit,
    Appeal,
    Contact,
    User,
)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'discription', 'youtube_url']
    fields = ['name', 'discription', 'youtube_url']

@admin.register(Exclusive)
class ExclusiveAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'duration']
    fields = ['name', 'price', 'duration']

@admin.register(About_company)
class About_companyAdmin(admin.ModelAdmin):
    list_display = ['discription', 'img']
    fields = ['discription', 'img']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['name', 'discription', 'img', 'appeal']
    fields = ['name', 'discription', 'img', 'appeal']

@admin.register(Commit)
class CommitAdmin(admin.ModelAdmin):
    list_display = ['name', 'discription']
    fields = ['name', 'discription']

@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'emile', 'message', 'title']
    fields = ['name', 'phone_number', 'emile', 'message', 'title']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['area', 'phone_number', 'emile', 'location', 'telegram', 'instagram', 'facebook']
    fields = ['area', 'phone_number', 'emile', 'location', 'telegram', 'instagram', 'facebook']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'password']
    fields = ['username', 'password']

    