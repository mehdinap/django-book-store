from django.db import models
from django.core.validators import (
    MinValueValidator as minval,
    MaxValueValidator as maxval,
)
from django.urls import reverse
from django.utils.text import slugify

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[minval(1), maxval(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True,null=False,db_index=True)

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    def save(self,*args,**kwards):
        self.slug=slugify(self.title)
        super().save(*args,**kwards)


    def __str__(self):
        return f"{self.title} ({self.rating})"
