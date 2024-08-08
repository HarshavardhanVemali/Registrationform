from django.db import models

class Register(models.Model):
    register_number = models.CharField(max_length=15, null=True, unique=True)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField()
    branch = models.CharField(max_length=10, null=True)
    year = models.CharField(max_length=10, null=True)
    def __str__(self):
        return f"{self.register_number}"
