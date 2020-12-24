from django.db import models
class BookInfo(models.Model):
    name = models.CharField(max_length=20,null=False)
    pub_date = models.DateField()
    read_count = models.IntegerField()
    comment_count = models.IntegerField()
    writer = models.CharField(max_length=20,null=False)
    is_delete = models.BooleanField(default=0)
    class Meta:
        db_table = 'BookInfo'

    def __str__(self):
        return self.name

class PersonInfo(models.Model):
    name = models.CharField(max_length=20,null=False)
    age = models.IntegerField(null=True)
    GENDER_CHOICE = (
        (0,'BOY'),
        (1,'GIRL'),
        (2,'UNKNOWN')
    )
    gender = models.SmallIntegerField(choices=GENDER_CHOICE)
    description = models.CharField(max_length=200,null=True)
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)
    is_delete = models.BooleanField(default=0)
    class Meta:
        db_table = 'PersonInfo'

    def __str__(self):
        return self.name

# Create your models here.

