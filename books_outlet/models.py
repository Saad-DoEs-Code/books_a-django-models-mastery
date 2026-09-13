from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Author(models.Model):

    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    is_bestSelling = models.BooleanField(default=False)
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
