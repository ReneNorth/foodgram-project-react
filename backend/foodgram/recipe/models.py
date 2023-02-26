from ingredients.models import Ingredient
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

User = get_user_model()


class Recipe(models.Model):
    """
    Рецепт должен описываться такими полями:
    Автор публикации (пользователь).
    Название.
    Картинка.
    Текстовое описание.
    Ингредиенты: продукты для приготовления блюда по рецепту. Множественное поле, выбор из предустановленного списка, с указанием количества и единицы измерения.
    Тег (можно установить несколько тегов на один рецепт, выбор из предустановленных).
    Время приготовления в минутах.
    """
    author = models.ForeignKey(User,
                               verbose_name=('Автор'),
                               on_delete=models.CASCADE)
    name = models.CharField(max_length=80,
                            verbose_name='Название')
    text = models.TextField(max_length=500,
                            verbose_name='Описание')
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')
    cooking_time = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(43200,
                                      'Вы указали время приготовления больше'
                                      'чем один месяц, вы уверены в'
                                      'корректности введённых данных?'),
                    MinValueValidator(1,
                                      'Время приготовления не может'
                                      'быть меньше одной минуты')],
        verbose_name='Время на приготовление в минутах'
        )
    image = models.ImageField(
        upload_to='recipes/', null=True, blank=True)
    
    def __str__(self) -> str:
        return f'id {self.id}: {self.name[:10]}'
    
    # tags = 
    # is_in_shopping_cart


class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient,
                                #    related_name='ingredients',
                                   on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe,
                               related_name='recipes',
                               on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField(
        verbose_name='количество',
        default=1,
        blank=True,
        null=True,
        validators=[MinValueValidator(1,
                                      'вес не может быть меньше одной десятой'
                                      'от одной единицы измерения'), ])
    
    def __str__(self) -> str:
        return f'Ингредиент {self.ingredient} в рецепте {self.recipe}'


class FavoriteRecipe(models.Model):
    who_favorited = models.ForeignKey(User,
                                      related_name='who_favorited',
                                      on_delete=models.CASCADE)
    favorited_recipe = models.ForeignKey(Recipe,
                                         related_name='is_favorited',
                                         on_delete=models.CASCADE)
