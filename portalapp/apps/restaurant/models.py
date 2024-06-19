from django.db import models
from django.urls import reverse


class Restaurant(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            blank=False, null=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('restaurants-detail', kwargs={'pk': self.pk})
