from django.contrib import admin

from recipes.models import Category, Comment, Product, Recipe

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('title',)
    prepopulated_fields = {'slug' : ('title',)}

@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('title',)
    prepopulated_fields = {'slug' : ('title',)}

@admin.register(Recipe)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'views')
    list_display_links = ('title',)
    order_by = ('title',)
    filter_horizontal = ["products",]
    readonly_fields = ('views',)
    prepopulated_fields = {'slug' : ('title',)}

@admin.register(Comment)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'recipe',)
    order_by = ('id',)