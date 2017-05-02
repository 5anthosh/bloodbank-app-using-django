from django.db import models


class Request(models.Model):
    choice1 = (('O Positive', 'O Positive'),
               ('O Negative', 'O Negative'),
               ('A Positive', 'A Positive'),
               ('A Negative', 'A Negative'),
               ('B Positive', 'B Positive'),
               ('B Negative', 'B Negative'),
               ('AB Negative', 'AB Negative'),
               ('AB Positive', 'AB Positive'),
               )
    name = models.CharField(max_length=30)
    name_of_hospital = models.CharField(max_length=100)
    blood_type = models.CharField(max_length=30,choices=choice1)
    units = models.IntegerField()
    reason = models.TextField(max_length=100)
    contact_number = models.CharField(max_length=20)
