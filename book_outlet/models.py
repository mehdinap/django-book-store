from django.db import models
from django.core.validators import (
    MinValueValidator as minval,
    MaxValueValidator as maxval,
)
from django.urls import reverse
from django.utils.text import slugify


class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name} +({self.code})"

    class Meta:
        verbose_name_plural = "Countries"


class Address(models.Model):
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def get_full_address(self):
        return f"{self.street},{self.postal_code},{self.city}"

    def __str__(self):
        return self.get_full_address()

    class Meta:
        verbose_name_plural = "Address Entries"


class Author(models.Model):
    frist_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, null=True
    )  # didn't need set on_deleted because it's one-to-one connection

    def get_full_name(self):
        return f"{self.frist_name} {self.last_name}"

    def __str__(self):
        return self.get_full_name()


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[minval(1), maxval(5)])
    # author = models.CharField(null=True, max_length=100)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="books"
    )
    # some parameter for ForeignKey :
    # on_delete = models.CASCADE => delete if ForeignKey is deleted.
    # on_delete = models.PROTECT => raised an error
    # on_delete = models.SET_NULL => set to null if deleted
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    published_country = models.ManyToManyField(Country, null=False)

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    # def save(self,*args,**kwards):
    #     self.slug=slugify(self.title)
    #     super().save(*args,**kwards)

    def __str__(self):
        return f"{self.title} ({self.rating})"
