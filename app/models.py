from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Ticket(models.Model):
    STATUS = (
        ("unsolved", "unsolved"),
        ("solved", "solved"),
        ("process","process")
    )

    client = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    status = models.CharField(max_length=255, choices=STATUS)
    date = models.DateField(null=False)

    class Meta:
        verbose_name_plural = "Ticket"