from tabnanny import verbose
from tkinter import CASCADE
from django.contrib.auth import get_user_model
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length= 50, verbose_name="Название", blank=False, null=False)
    slug = models.SlugField(unique=True, verbose_name="Слаг", blank=False, null=False)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    title = models.CharField(max_length= 50, verbose_name="Название", blank=False, null=False)
    picture = models.ImageField(verbose_name="Картинка", upload_to="product_images/", null=True, blank=True)
    slug = models.SlugField(unique=True, verbose_name="Слаг", blank=False, null=False)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.title


class Recipe(models.Model):
    title = models.CharField(max_length= 128, verbose_name="Название", blank=False, null=False)
    category = models.ForeignKey(
        to = Category,
        verbose_name = "Категория",
        related_name = "recipe_by_cats",
        on_delete = models.CASCADE,
        blank = False, 
        null = False,
    )
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания", )
    picture = models.ImageField(verbose_name="Картинка", upload_to="recipe_images/", null=True, blank=True)
    products = models.ManyToManyField(
        to = Product,
        verbose_name = "Список продуктов",
        related_name = "recipes_by_product",
    )
    cook_time = models.IntegerField(verbose_name="Время приготовления (в минутах)")
    recipe_descrition = models.TextField(verbose_name="Текст рецепта", blank=False, null=False)
    author = models.ForeignKey(
        to = get_user_model(),
        on_delete = models.CASCADE,
        verbose_name = "Автор рецепта",
        related_name = "recipes_by_author",
        null = True,
        blank = True
    )
    slug = models.SlugField(unique=True, verbose_name="Слаг", blank=False, null=False)
    short_recipe_descrition = models.TextField(verbose_name="Описание рецепта", blank=False, null=False)

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    author = models.ForeignKey(
        to = get_user_model(),
        on_delete = models.CASCADE,
        verbose_name = "Автор комментария",
        related_name = "comment_by_author",
        null = True,
        blank = True
    )
    comment = models.TextField(verbose_name="Комментарий", blank=False, null=False)
    recipe = models.ForeignKey(
        to = Recipe,
        verbose_name = "Рецепт",
        on_delete = models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f"{self.author.username} - {self.recipe.name}"

