from django.contrib import admin

from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class ReviewCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

class CardAdmin(admin.ModelAdmin):
    model = Card
    list_display = ['title', 'description', 'get_category', ]

    def get_category(self, obj):
        return obj.category.title

    get_category.admin_order_field = 'category__title'
    get_category.short_description = 'Category'


class AccessAdmin(admin.ModelAdmin):
    list_display = ['ip', 'visit_count']


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'get_category', 'score', 'created']

    def get_category(self, obj):
        return obj.category.title

    get_category.admin_order_field = 'category__title'
    get_category.short_description = 'Category'


class BlogAdmin(admin.ModelAdmin):
    model = Card
    list_display = ['title', 'description', 'get_category', 'position',]

    def get_category(self, obj):
        return obj.category.title

    get_category.admin_order_field = 'category__title'
    get_category.short_description = 'Category'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(AccessCount, AccessAdmin)
admin.site.register(ReviewCategory, ReviewCategoryAdmin)
admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogCategory, BlogCategoryAdmin)
