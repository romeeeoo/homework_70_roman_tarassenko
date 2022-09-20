from django.db import models


# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('in_process', 'In Process'),
        ('done', 'Done')
    ]
    description = models.CharField(max_length=200, null=False, blank=False)
    status = models.CharField(null=False, blank=False, choices=STATUS_CHOICES, default='new', max_length=50)
    deadline = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}. {}".format(self.pk, self.description, self.status)
