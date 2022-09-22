from django.db import models

class Category(models.Model):
    name= models.CharField(max_length=50,verbose_name='Категория')
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name
