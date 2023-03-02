from django.contrib import admin

# Register your models here.
from .models import Category,Post
# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_diaplay=('is_published','title','posted_at')
    list_filter=('is_published','posted_at')
    # list_editable=('is_published','title','posted_at')

    
    
    
    
admin.site.register(Category)
admin.site.register(Post,PostAdmin)