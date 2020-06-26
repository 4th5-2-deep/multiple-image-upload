from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Clothes(models.Model):
    # user = ...
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(blank=True, upload_to='clothes/images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
