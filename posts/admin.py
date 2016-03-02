from django.contrib import admin

from .models import Tag
from .models import Post
from .models import Category


# admin models
class PostAdmin(admin.ModelAdmin):
    """
    Post object admin class
    """
    # generate slug from heading and content
    prepopulated_fields = {"post_url": ("post_heading", "post_content")}
    # save_on_top = True

# Register models.
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
