from django.db import models

class OwnerModel():
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField()

    def __str__(self):
        return self.name

class NurseModel():
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField()

    def __str__(self):
        return self.name