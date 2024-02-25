from django.contrib import admin  # noqa

from .models import Author, Genre, Type, Tag, Book, Image


admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Type)
admin.site.register(Tag)
admin.site.register(Image)
admin.site.register(Book)
