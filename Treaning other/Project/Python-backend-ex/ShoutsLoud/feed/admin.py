from django.contrib import admin
from feed.models import Post, Comments, Like
# Register your models here.
@admin.register(Post)
class AppPosts(admin.ModelAdmin):
    pass

@admin.register(Comments)
class AppComments(admin.ModelAdmin):
    pass

@admin.register(Like)
class AppLikes(admin.ModelAdmin):
    pass