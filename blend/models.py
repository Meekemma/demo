from django.db import models

# Create your models here.

class Demo(models.Model):
    email = models.EmailField(max_length=254)
    created_on=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.email    


class Contact(models.Model):
    email = models.EmailField(max_length=254)
    message=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f" {self.message} by {self.email}"
    
class Newsletter(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    created_on=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.email    
    
