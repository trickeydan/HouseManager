from django.db import models


class Person(models.Model):
    class Meta:
        verbose_name_plural = "people"

    full_name = models.CharField(max_length=150)
    display_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    picture = models.ImageField(upload_to='people')
    gender = models.CharField(max_length=20)
    pronouns = models.CharField(max_length=30)
    bio = models.TextField()

    def __str__(self):
        return self.display_name
