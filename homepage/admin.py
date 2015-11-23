from django.contrib import admin

from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class CardAdmin(admin.ModelAdmin):
    model = Card
    list_display = ['title', 'description', 'get_category', ]

    def get_category(self, obj):
        return obj.category.title

    get_category.admin_order_field = 'category__title'
    get_category.short_description = 'Category'


class AccessAdmin(admin.ModelAdmin):
    list_display = ['time', 'ip', ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Access, AccessAdmin)
