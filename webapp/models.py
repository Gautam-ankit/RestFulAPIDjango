from django.db import models

class employees(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    emp_id = models.IntegerField()
    age  = models.IntegerField()

#creating method that will return all my field values

    def __str__(self):
        return self.firstname

    def __str__(self):
        return self.lastname

    def __str__(self):
        return self.emp_id

    def __str__(self):
        return self.age


