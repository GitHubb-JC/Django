from django.contrib import admin
from .models import Articles

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'created_at', 'updated_at']

admin.site.register(Articles, ArticleAdmin)
