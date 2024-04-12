from django.db import models

# Create your models here.


class DataEntry(models.Model):
    actual_word = models.CharField(max_length=100)
    replaced_word = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.actual_word} - {self.replaced_word}"
