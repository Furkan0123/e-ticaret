from django.contrib import admin
from .models import Product , Product2 , Product3 , Category


admin.site.register(Product)

admin.site.register(Product2)


admin.site.register(Product3)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug' : ('name',)}