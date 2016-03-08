from django.db import models
from django.utils import timezone
from datetime import date
# Create your models here.


class Category(models.Model):
    user=models.ForeignKey(Searcher)
    category_list=models.ForeignKey(Category_List)
    is_public=models.BooleanField(default=False)
    name=models.CharField(max_length=None)
    def __unicode__(self):
        return self.name

#possibly use this class with one to one correlation with an authorization user class
class Searcher(models.Model):
    GENDER_OPTIONS= (
        ('Other', 'Other'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        )
    username= models.CharField(max_length=40, unique=True)
    password= models.CharField(max_length=32);
    email= models.EmailField()
    name= models.CharField(max_length=None)
    surname=models.CharField(max_length=None)
    age=models.PositiveIntegerField()
    gender=models.CharField(max_length=6, choices=GENDER_OPTIONS)
    # category_list=models.ForeignKey(category_list)
    # search_history=models.ForeignKey(search_history)

    def __unicode__(self):
        return self.username

class Page(models.Model):
    linkURL=models.URLField()
    title=models.CharField(max_length=200)
    category=models.ForeignKey(Category)
    visits=models.PositiveIntegerField(default=0)
    summary=models.CharField(max_length=None)
    flesch_score=models.PositiveIntegerField()
    polarity_score=models.PositiveIntegerField()
    subjectivity_score=models.PositiveIntegerField()
    def __unicode__(self):
        return self.title

class Search(models.Model): #this pertains to the Search History  ("a search" => "searches")
    query=models.CharField(max_length=None)
    timestamp_last_modified=models.DateTimeField(auto_now=True, default=timezone.now())
    timestamp_first_time_search_added_to_table=models.DateTimeField(auto_now_add=True, default=date.today())
    user=models.ForeignKey(Searcher)
    def __unicode__(self):
        return self.query

class Category_List(models.Model):
    name=models.CharField(max_length=200)
    user=models.ForeignKey(Searcher)
    def __unicode__(self):
        return self.name

class Admin(models.Model):
    contract_email=models.EmailField()
    hours=models.CharField(max_length=None)
    address=models.CharField(max_length=None)
    sitename=models.CharField(max_length=100)
    sitelogo=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=100)
    #unicode?


class Favorite_Search(models.Model): #a favorite search has a key to a search
    query=models.OneToOneField(Search)
    user=models.ForeignKey(Searcher)
    #what is the unicdoe? return query.__unicode__()

class Saved_Page(models.Model):
    link=models.OneToOneField(Page)
    is_public= models.BooleanField(default=False)
    user=models.ForeignKey(Searcher)
    saved_timestamp=models.DateTimeField(default=timezone.now(), auto_now_add=True)
    shared_timestamp=models.DateTimeField(default=timezone.now())#not automatic #really set when public is set true
    #unicode? link.title?

