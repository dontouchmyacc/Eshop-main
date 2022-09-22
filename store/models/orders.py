from django.db import models
from .product import Products
from .customer import Customer
import datetime


class Order(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE,verbose_name='Товар')
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,verbose_name='Покупатель')
    quantity = models.IntegerField(default=1,verbose_name='Кол-во товаров')
    price = models.IntegerField(verbose_name='Цена')
    address = models.CharField (max_length=50, default='', blank=True,verbose_name='Адрес')
    phone = models.CharField (max_length=50, default='', blank=True,verbose_name='Телефон')
    date = models.DateField (default=datetime.datetime.today,verbose_name='Дата')
    status = models.BooleanField (default=False,verbose_name='Статус')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

