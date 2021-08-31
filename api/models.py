from django.db import models

# Create your models here.
class Course(models.Model):
    Name = models.CharField(max_length=20)
    Price = models.IntegerField()
    Discount =  models.IntegerField()
    Duration = models.IntegerField()
    AuthorName = models.CharField(max_length= 20)

    def __str__(self):
        return self.Name