from django.contrib import admin
from .models import Post, Tag, comment
admin.site.register(Post)
admin.site.register(comment)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Tag, TagAdmin)

# Register your models here.

