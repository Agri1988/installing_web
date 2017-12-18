from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Installation(models.Model):
    number = models.CharField(verbose_name='Numer zlecenia', max_length=22, blank=False, null=False)
    date = models.DateField(verbose_name='Data instalacji')
    time_slot_choices = [('0', '08.00-11.00'), ('1', '11.00-14.00'), ('2', '14.00-17.00'), ('3', '17.00-20.00')]
    time_slot = models.CharField(verbose_name='Slot czasowy', max_length=64, choices=time_slot_choices, blank=False,
                                 null=False)
    address = models.CharField(verbose_name='Adres', max_length=256, blank=False, null=False)
    employee_1 = models.ForeignKey(User, related_name='employee_1', on_delete=models.PROTECT, blank=False, null=False)
    employee_2 = models.ForeignKey(User, related_name='employee_2', on_delete=models.PROTECT, default=None, blank=True,
                                   null=True)
    employee_3 = models.ForeignKey(User, related_name='employee_3', on_delete=models.PROTECT, default=None,
                                   blank=True, null=True)
    success = models.BooleanField(default=False)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.number + str(self.date) + self.address

    def save(self, *args, **kwargs):
        self.number = self.number.upper()
        super(Installation, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Instalacja'
        verbose_name_plural = 'Instalacje'
