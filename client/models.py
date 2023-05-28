from django.db import models
from django.contrib.auth.admin import User

# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11)

    def __str__(self) -> str:
        return self.user.username
