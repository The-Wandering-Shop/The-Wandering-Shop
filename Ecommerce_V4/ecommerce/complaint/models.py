from django.db import models

# Create your models here.

class Complaint(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    order_number = models.CharField(max_length=6)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} -Order # {self.order_number}"