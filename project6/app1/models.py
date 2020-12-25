from django.db import models


class BookInfo(models.Model):
    name = models.CharField(max_length=20, null=False)
    pub_date = models.DateField(null=True)
    read_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=True)

    class Meta():
        db_table = 'BookInfo_db'

    def __str__(self):
        return self.name


class PersonInfo(models.Model):
    name = models.CharField(max_length=20, null=False)
    GENDER_DATA = (
        (0, 'BOY'),
        (1, 'GIRL')
    )
    gender = models.SmallIntegerField(choices=GENDER_DATA)
    description = models.CharField(max_length=200, null=True)
    is_delete = models.BooleanField(default=True)

    class Meta():
        db_table = 'PersonInfo_db'

    def __str__(self):
        return self.name
