from django.contrib import admin
from django.forms import ModelForm, CharField
from pagedown.widgets import AdminPagedownWidget

from .models import Tag
from .models import Post
from .models import Category


class PostAdminForm(ModelForm):
    """

    """
    post_content = CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Post
        fields = '__all__'


# admin models
class PostAdmin(admin.ModelAdmin):
    """
    Post object admin class
    """
    # generate slug from heading and content
    prepopulated_fields = {"post_url": ("post_heading", "post_content")}
    list_display = ('id', 'post_content', 'post_url', 'post_heading', 'post_datetime')
    ordering = ('-post_datetime',)
    search_fields = ('post_heading', 'post_content', 'post_url', 'post_content_author')
    save_on_top = True
    form = PostAdminForm


class CategoryAdmin(admin.ModelAdmin):
    """
    Category object admin class.
    """
    list_display = ('id', 'category_name', 'category_description')
    list_filter = ('category_name', 'category_tags')
    ordering = ('category_name', 'category_tags')
    save_on_top = True


class TagAdmin(admin.ModelAdmin):
    """
    Tag object admin class.
    """
    list_display = ('id', 'tag_name', 'tag_description')
    list_filter = ('tag_name',)
    ordering = ('tag_name',)
    search_fields = ('tag_name', 'tag_description')
    save_on_top = True


# Register models.
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
