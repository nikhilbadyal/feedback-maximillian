from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Review(models.Model):
    user_name = models.CharField(max_length=255)
    review = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.user_name} {self.rating}"
