from django.db import models
from django.utils import timezone
#from authentication.models import Account
from django import forms
# from PIL import Image
from django.core.exceptions import ValidationError
from requests import auth


class Ingredient(models.Model):
    name = models.CharField(max_length=300)
    weight = models.IntegerField(null=False, default=0)
    price = models.IntegerField(null=False, default=0)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    #def __init__(self, *args, **kwargs):
       # super(models.Model, self).__init__(*args, **kwargs)
        # adding css classes to widgets without define the fields:
       # for field in self.fields:
        #    self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta:
        ordering = ('name',)


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    calories = models.BigIntegerField(null=True, blank=True)
    price = models.BigIntegerField(null=True, error_messages={'required': 'Determine the priceyi'})
    created_date = models.DateTimeField(default=timezone.now)
    image = models.FileField(null=True, upload_to='images/dishes')
    published_date = models.DateTimeField(blank=True, null=True)
    ingredients = models.ManyToManyField(Ingredient)
   # pic = models.ImageField(blank=True, )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.choice_text

   # def __init__(self, *args, **kwargs):
    #    super(models.Model, self).__init__(*args, **kwargs)
        # adding css classes to widgets without define the fields:
     #   for field in self.fields:
      #      self.fields[field].widget.attrs['class'] = 'form-control'
            # class PostIngredient(models.Model):
            # post = models.ForeighKey(Post)
            # ingredient = models.ForeignKey(Ingredient)

class Menu(models.Model):
        date = models.DateTimeField(blank=True, null=True)
        items = models.ManyToManyField('Post')
        title = models.TextField()
        # pic = models.ImageField(blank=True, )

        def publish(self):
            self.published_date = timezone.now()
            self.save()

        def __str__(self):
            return self.items.name

        def __unicode__(self):
            return self.choice_text

            # def __init__(self, *args, **kwargs):
            #    super(models.Model, self).__init__(*args, **kwargs)
            # adding css classes to widgets without define the fields:
            #   for field in self.fields:
            #      self.fields[field].widget.attrs['class'] = 'form-control'
            # class PostIngredient(models.Model):
            # post = models.ForeighKey(Post)
            # ingredient = models.ForeignKey(Ingredient)


def clean_price(self):
    if self.clean_data.get('price') < 0:
        raise ValidationError("Значение цены должно быть положительным!", code="invalid")

