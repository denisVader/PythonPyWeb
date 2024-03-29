from django.contrib import admin
from .models import Author, Tag, AuthorProfile, Entry

admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(AuthorProfile)
admin.site.register(Entry)
