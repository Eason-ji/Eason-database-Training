from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    gender = models.BooleanField()
    book = models.ForeignKey(Book,on_delete=models.CASCADE)

    def __str__(self):
        return self.name