from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)

    # Addition Django Config Fields
    prepopulated_fields = {
        "slug": ("title",),
    }
    list_filter = (
        "author",
        "rating",
    )
    list_display = ("title", "author")


# Register your models here.
admin.site.register(Book, BookAdmin)
