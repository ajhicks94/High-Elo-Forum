from django.contrib import admin
from .models import Category, Forum, Thread, Post, Profile

class PostInlineAdmin(admin.TabularInline):
    model = Post
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
   list_display = ('name', 'position') 

class ForumAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description', 'category', 'thread_count', 'post_count')

class ThreadAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'forum', 'created', 'modified', 'post_count', 'sticky')
    inlines = [PostInlineAdmin]

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'thread', 'author', 'created', 'modified')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'group', 'post_count', 'rep_count', 'server', 'rank')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Forum, ForumAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Post, PostAdmin)
