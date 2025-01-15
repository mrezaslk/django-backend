from django.db import models

# Create your models here.
# mode; => python class
# model rep a table in the db
# attr are the fields in the table


class JobPosting(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    salary = models.IntegerField()


# command for migration
# make migration =>> python manage.py makemigrations
# migration => pyhthon manage.py migrate