from django.contrib.auth import get_user_model
from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=30, verbose_name="Название", blank=False, null=False
    )
    slug = models.SlugField(verbose_name="Слаг", unique=True, blank=False, null=False)
    image = models.ImageField(
        verbose_name="Картинка", upload_to="category_image/", blank=True, null=True
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=30, verbose_name="Название", blank=False, null=False
    )
    slug = models.SlugField(verbose_name="Слаг", unique=True, blank=False, null=False)
    image = models.ImageField(
        verbose_name="Картинка", upload_to="product_image/", blank=True, null=True
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(
        max_length=30, verbose_name="Название", blank=False, null=False
    )
    category = models.ForeignKey(to=Category, verbose_name='Категория', related_name='recipes_by_cat', on_delete=models.CASCADE, null=False, blank=False)
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    image = models.ImageField(
        verbose_name="Картинка", upload_to="recipe_image/", blank=True, null=True
    )
    products = models.ManyToManyField(to=Product, through='RecipeProduct', verbose_name='Список продуктов', related_name='recipes_by_product')
    cook_time = models.IntegerField(verbose_name='Время приготовления (в минутах)')
    text = models.TextField(verbose_name='Текст рецепта', null=False, blank=False)
    author = models.ForeignKey(to=get_user_model(), on_delete=models.SET_NULL, verbose_name='Автор', related_name='recipes_by_author', null=True)
    slug = models.SlugField(verbose_name='Слаг', unique=True, blank=False, null=False)
    description = models.TextField(verbose_name='Краткое описание', null=False, blank=False)
    views = models.IntegerField(verbose_name='Просмотры', default=0)

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    author = models.ForeignKey(to=get_user_model(), on_delete=models.SET_NULL, verbose_name='Автор', related_name='comments_by_author', null=True)
    text = models.TextField(verbose_name='Текст комментария', null=False, blank=False)
    recipe = models.ForeignKey(to=Recipe, verbose_name='Рецепт', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f'{self.author.username} - {self.recipe.name}'
    

class RecipeProduct(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_recipes')
    quantity = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Количество', default=0)
    unit = models.CharField(max_length=20, verbose_name='Единица измерения', blank=True, null=True)

    class Meta:
        unique_together = ('recipe', 'product')
        verbose_name = 'Продукт в рецепте'
        verbose_name_plural = 'Продукты в рецепте'

    def __str__(self):
        return f"{self.product.name} - {self.quantity} {self.unit or ''}"
