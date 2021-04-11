from django.db import models

from django.contrib.auth.models import AbstractUser

class LocationEnum(models.TextChoices):
    CJ = 'CJ', 'Cluj'
    B = 'B', 'Bucuresti'
class RoleEnum(models.TextChoices):
    U = 'U', 'User'
    A = 'A', 'Admin'


class User(AbstractUser):
    name=models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    role=models.CharField(max_length=100,
        choices=RoleEnum.choices,
        default=RoleEnum.U,
    )
    location = models.CharField(max_length=100,
        choices=LocationEnum.choices,
        default=LocationEnum.CJ,
    )
    email = models.CharField(max_length=100)
    def __str__(self):
        return self.username


class Task(models.Model):

    id = models.IntegerField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    starttime = models.DateTimeField()
    location = models.CharField(max_length=100,
        choices=LocationEnum.choices,
        default=LocationEnum.CJ,
    )
    description = models.CharField(max_length=100)
    reward = models.FloatField()
    def __str__(self):
        return self.name

class AcceptedTasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    #def __str__(self):
     #   return self.user+' '+self.task
