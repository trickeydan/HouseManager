from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from hman.models import Model
from bills.models import Payment


class Person(Model):
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

    @property
    def payments(self):
        return Payment.objects.filter(person=self)

    @property
    def balance(self):
        return self.payments.all().aggregate(models.Sum('amount'))['amount__sum']

    @property
    def balance_human(self):
        return "£{0:.2f}".format(self.balance / 100)

    @staticmethod
    def get_from_user(user):
        if user.is_authenticated:
            return Person.objects.all().filter(user=user).first()
        return None
