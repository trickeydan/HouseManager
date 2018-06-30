from django.db import models
from people.models import Person


class Service(models.Model):
    name = models.CharField(max_length=60)
    start_date = models.DateField()
    end_date = models.DateField()
    owners = models.ManyToManyField(Person)
    description = models.TextField()

    @property
    def bills(self):
        raise NotImplementedError


class Transaction(models.Model):

    COMPLETE = 'comp'
    PENDING = 'pend'

    class Meta:
        abstract = True

    STATUS_CHOICES = (
        (COMPLETE, 'Complete'),
        (PENDING, 'Pending'),
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, default=PENDING, max_length=4)
    amount = models.IntegerField()


class TellerMixin:
    teller_id = models.CharField(max_length=50, blank=True)


class Bill(TellerMixin, Transaction):
    """A payment made out of the account to a company"""
    service = models.ForeignKey(Service, on_delete=models.PROTECT)

    @property
    def payments(self):
        raise NotImplementedError


class Share(Transaction):
    """A person's share of a bill"""
    bill = models.ForeignKey(Bill, on_delete=models.PROTECT)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)


class Payment(TellerMixin, Transaction):
    """A payment made into the account by a person"""
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
