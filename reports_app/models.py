from django.db import models
from installation_app.models import Installation

# Create your models here.
class MonthReport(models.Model):
    month = models.DateFields()