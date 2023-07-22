from django.db import models

# Create your models here.
class FormModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {} - {} - {}".format(self.name, self.phone, self.email, self.location)