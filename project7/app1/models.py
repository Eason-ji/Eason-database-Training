from django.db import models

# Create your models here.
class BookInfo(models.Model):
    name = models.CharField(max_length=20,null=False)

    class Meta():
        db_table = "BookInfo"

    def __str__(self):
        return self.name



class PersonInfo(models.Model):
    name = models.CharField(max_length=20,null=False)
    data=(
        (0,'男'),
        (0,'女')
    )
    gender = models.SmallIntegerField(choices=data)
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    class Meta():
        db_table = 'PersonInfo'

    def __str__(self):
        return self.name

