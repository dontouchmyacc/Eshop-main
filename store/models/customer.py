from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50,verbose_name='Имя')
    last_name = models.CharField (max_length=50,verbose_name='Фамилия')
    phone = models.CharField(max_length=10,verbose_name='Телефон')
    email=models.EmailField(verbose_name='Е-мэйл')
    password = models.CharField(max_length=100,verbose_name='Пароль')

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

    #to save the data
    def register(self):
        self.save()


    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email= email)
        except:
            return False


    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False