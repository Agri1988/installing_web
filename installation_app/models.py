from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class InstallationStandart(models.Model):
    standart = models.CharField(max_length=16, verbose_name='Standard instalacji', blank=True)
    class Meta:
        ordering = ['standart']
        verbose_name = 'Standard instalacji'
        verbose_name_plural = 'Standardy instalacje'

    def __str__(self):
        return self.standart


class InstallationType(models.Model):
    type = models.CharField(max_length=16, verbose_name='Typ instalacji', blank=True)
    class Meta:
        ordering = ['type']
        verbose_name = 'Typ instalacji'
        verbose_name_plural = 'Typy instalacje'

    def __str__(self):
        return self.type


class Installation(models.Model):
    with_contract = models.BooleanField(verbose_name='Umowa', default=False)
    installation_standart = models.ForeignKey(InstallationStandart, default=None, blank=True, null=True,
                                              on_delete=models.PROTECT, verbose_name='Standard instalacji')
    installation_type = models.ForeignKey(InstallationType,default=None, blank=True, null=True,
                                              on_delete=models.PROTECT, verbose_name='Typ instalacji' )
    number = models.CharField(verbose_name='Numer zlecenia', max_length=22, blank=False, null=False)
    date = models.DateField(verbose_name='Data instalacji')
    time_slot_choices = [('0', '08.00-11.00'), ('1', '11.00-14.00'), ('2', '14.00-17.00'), ('3', '17.00-20.00')]
    time_slot = models.CharField(verbose_name='Slot czasowy', max_length=64, choices=time_slot_choices, blank=False,
                                 null=False)
    address = models.CharField(verbose_name='Adres', max_length=256, blank=False, null=False)
    employee_1 = models.ForeignKey(User, related_name='employee_1', on_delete=models.PROTECT, blank=False, null=False,
                                   verbose_name='pierwszy pracownik')
    employee_2 = models.ForeignKey(User, related_name='employee_2', on_delete=models.PROTECT, default=None, blank=True,
                                   null=True, verbose_name='drugi pracownik')
    employee_3 = models.ForeignKey(User, related_name='employee_3', on_delete=models.PROTECT, default=None,
                                   blank=True, null=True, verbose_name='trzeci pracownik')
    success = models.BooleanField(default=False, verbose_name='Skuteczna')
    accepted = models.BooleanField(default=False, verbose_name='Potwierdzona')

    def __str__(self):
        return self.number + str(self.date) + self.address

    def save(self, *args, **kwargs):
        self.number = self.number.upper()
        super(Installation, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Instalacja'
        verbose_name_plural = 'Instalacje'
        ordering = ['date', 'time_slot', 'address']


