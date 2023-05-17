from django.contrib import admin
from django.utils.html import format_html
from .models import User, Category, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category_list", "cover_image", "created_at", "updated_at",)

    def category_list(self, obj):
        return ", ".join([cat.title for cat in obj.categories.all()])

    def cover_image(self, obj):
        return format_html('<img width="100" src="{}" />'.format(obj.cover_img_url))


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(User)
