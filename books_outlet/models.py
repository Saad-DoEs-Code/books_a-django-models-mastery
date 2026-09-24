from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=3)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Countries"


class Address(models.Model):
    street = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.street}, {self.city} ({self.postal_code})"

    class Meta:
        verbose_name_plural = "Address Entries"


class Author(models.Model):

    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return self.full_name()


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    is_bestSelling = models.BooleanField(default=False)
    counntries_published = models.ManyToManyField(Country, null=False)
    slug = models.SlugField(
        default="",
        null=False,
        # blank=True,
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.title}: {self.rating}/5"

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
