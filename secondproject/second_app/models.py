from django.db import models
from django.core.validators import validate_email,MaxValueValidator
# Create your models here.
class Userdata(models.Model):
    fname = models.CharField(max_length=128)
    lname = models.CharField(max_length=128)
    email = models.EmailField(unique=True,validators=[validate_email])