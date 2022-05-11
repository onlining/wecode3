from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        db_table = 'menu'
    def __str__(self):  # 이 코드를 넣으면 manage.py shell에서 객체가 아니라 테이블의 name으로 표시됨
        return self.name
class DrinkCategories(models.Model):
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    class Meta:
        db_table = 'drinkcategories'
    def __str__(self):
        return self.name
class Drinks(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('DrinkCategories', on_delete=models.CASCADE)
    is_new = models.BooleanField(default=False)
    description = models.TextField(null=True)
    class Meta:
        db_table = 'drinks'
    def __str__(self):
        return self.name
class DrinkImages(models.Model):
    drink = models.ForeignKey('Drinks', on_delete=models.CASCADE)
    image_url = models.URLField(max_length=3000)
    class Meta:
        db_table = 'drinkimages'
class DrinkNutritions(models.Model):
    drink = models.OneToOneField('Drinks', on_delete=models.CASCADE)
    kcal = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    sugar = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    protein = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    sodium = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    fat = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    caffeine = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    class Meta:
        db_table = 'drinknutritions'
class Allergen(models.Model):
    name = models.CharField(max_length=100)
    drink = models.ManyToManyField('Drinks', through='DrinkAllergies')
    class Meta:
        db_table = 'allergen'
    def __str__(self):
        return self.name
class DrinkAllergies(models.Model):
    drink = models.ForeignKey('Drinks', on_delete=models.CASCADE)
    allergen = models.ForeignKey('Allergen', on_delete=models.CASCADE)
    extraprice=models.IntegerField(default=0)
    class Meta:
        db_table = 'drinkallergies'