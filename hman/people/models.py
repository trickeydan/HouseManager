from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver


class Person(models.Model):
    class Meta:
        verbose_name_plural = "people"

        permissions = (
            ("can_view_others", "Can view other people"),
            ("can_list_others", "Can list other people"),
            ("can_edit_profile", "Can edit / view their profile"),
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

    def get_absolute_url(self):
        return reverse('people:view', args=[self.id])

    @property
    def full_name(self):
        return self.user.first_name + ' ' + self.user.last_name

    @property
    def email(self):
        return self.user.email

    @staticmethod
    def get_from_user(user):
        if user.is_authenticated:
            return Person.objects.all().filter(user=user).first()
        return None