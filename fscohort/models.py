from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField('Soyad', max_length=50)
    number = models.IntegerField('Numara')
    about = models.TextField('Hakkında', blank=True, null=True)
    image = models.ImageField('Fotograf', blank=True, null=True, upload_to='media/')
    
    def __str__(self):
        return f"{self.first_name}, {self.last_name}"
    class Meta:
        ordering = ["-number"]