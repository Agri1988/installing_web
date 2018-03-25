from django.contrib.auth.models import User
from django.db import models
from installation_app.models import Installation
# Create your models here.



class Car(models.Model):
    model = models.CharField(max_length=128, blank=False, null=False, verbose_name='Model samochodu')
    number = models.CharField(max_length=32, blank=False, null=False, verbose_name='Numer rejestracyjny')

    class Meta:
        verbose_name = 'Samocód'
        verbose_name_plural = 'Samochody'

    def __str__(self):
        return '%s %s' %(self.model, self.number)

class CarRefueling(models.Model):
    car = models.ForeignKey('Car', on_delete=models.PROTECT, verbose_name='Samochód')
    date = models.DateField(verbose_name='Data')
    refueling_quantity = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False,
                                             verbose_name='Ilość paliwa')
    refueling_cost = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False,
                                         verbose_name='Koszt tankowania')
    mileage = models.IntegerField(verbose_name='Przebieg')

    class Meta:
        verbose_name = 'Tankowanie'
        verbose_name_plural = 'Tankowania'
        ordering = ['car','date']

    def __str__(self):
        return '%s %s %s %s' %(self.car, self.date, self.refueling_quantity, self.refueling_cost)


class MileageAccount(models.Model):
    car = models.ForeignKey('Car', on_delete=models.PROTECT, verbose_name='Samochód')
    date = models.DateField(verbose_name='Data')
    user = models.ForeignKey(User, verbose_name='Pracownik', on_delete=models.PROTECT)
    installation = models.OneToOneField(Installation, default=None, blank=True, null=True, verbose_name='Instalacja',
                                        on_delete=models.PROTECT)
    comments = models.TextField(verbose_name='Cel podróży', default=None, null=True, blank=True)
    start_mileage = models.IntegerField(verbose_name='Początek przebiegu')
    end_mileage = models.IntegerField(verbose_name='Koniec przebiegu')

    class Meta:
        verbose_name = 'Przebieg'
        verbose_name_plural = 'Przebiegi'
        ordering = ['car', 'date', 'user']

    def __str__(self):
        return '%s %s' %(self.date, self.car)
