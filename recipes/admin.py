from django.contrib import admin

from recipes.models import Category, Comment, Product, Recipe, RecipeProduct

class RecipeProductInline(admin.TabularInline):  # Или admin.StackedInline, если хочешь вертикальную форму
    model = RecipeProduct
    extra = 1  # Количество пустых форм для добавления новых продуктов (по умолчанию 1)
    fields = ('product', 'quantity', 'unit')  # Поля, которые хочешь показывать
    autocomplete_fields = ['product']  

@admin.register(RecipeProduct)
class RecipeProductAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'product', 'quantity', 'unit')  # Что показывать в списке
    search_fields = ('recipe__name', 'product__name')  # Поиск по рецепту и продукту
    list_filter = ('unit',)  # Фильтр по единице
    autocomplete_fields = ['recipe', 'product']  # Автодополнение для выбора

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id' ,'name',)
    list_display_links = ('name',)
    prepopulated_fields = {'slug' : ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id' ,'name',)
    list_display_links = ('name',)
    ordering = ('name',)  # Исправлено: order_by -> ordering (стандартный атрибут Django)
    prepopulated_fields = {'slug' : ('name',)}
    search_fields = ('name',)  # Добавлено: обязательно для autocomplete_fields в RecipeProductInline и RecipeProductAdmin

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeProductInline] 
    list_display = ('id' ,'name', 'author', 'views',)
    list_display_links = ('name',)
    prepopulated_fields = {'slug' : ('name',)}
    ordering = ('name',)  # Исправлено: order_by -> ordering (стандартный атрибут Django)
    readonly_fields = ('views',)
    search_fields = ('name',)  # Добавлено: обязательно для autocomplete_fields=['recipe'] в RecipeProductAdmin

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'recipe')
    ordering = ('id',)  # Исправлено: order_by -> ordering (стандартный атрибут Django)
