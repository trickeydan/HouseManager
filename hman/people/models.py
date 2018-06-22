from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    class Meta:
        verbose_name_plural = "people"

        permissions = (
            ("people.can_view_others", "Can view other people"),
            ("people.can_list_others", "Can list other people"),
        )

    display_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    picture = models.ImageField(upload_to='people')
    gender = models.CharField(max_length=20)
    pronouns = models.CharField(max_length=30)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.display_name

    @property
    def full_name(self):
        return self.user.first_name + ' ' + self.user.last_name

    @property
    def email(self):
        return self.user.email
