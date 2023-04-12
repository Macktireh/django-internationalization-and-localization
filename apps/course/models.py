from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Course(TranslatableModel):

    translations = TranslatedFields(
        title = models.CharField(max_length=90),
        description = models.TextField(),
    )

    date = models.DateTimeField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    thumbnail = models.CharField(max_length=500, blank=True, null=True)


    def __str__(self):
        return self.title


class News(models.Model):

    title = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateField(null=True, blank=True)
    thumbnail = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title
