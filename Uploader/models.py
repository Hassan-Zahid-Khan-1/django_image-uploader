from django.db import models

# Create your models here.
class user_post(models.Model):
    image=models.FileField(upload_to='photos/')
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=150)
    upload_date=models.DateTimeField( auto_now_add=True)
    class Meta:
        ordering=('-upload_date',)
        def __str__(self):
           return self.title
