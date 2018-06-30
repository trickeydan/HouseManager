from django.db import models
from django.urls import reverse
from people.models import Person


class Service(models.Model):

    class Meta:
        permissions = (
            ('can_view_services', 'Can view the services for the house'),
        )

    name = models.CharField(max_length=60)
    start_date = models.DateField()
    end_date = models.DateField()
    owners = models.ManyToManyField(Person)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bills:services_view', args=[self.id])

    @property
    def bills(self):
        return Bill.objects.filter(service=self)


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

    @property
    def amount_human(self):
        return " £" + str(self.amount /100)

    @property
    def status_human(self):
        for pair in Transaction.STATUS_CHOICES:
            if pair[0] == self.status:
                return pair[1]
        return self.status


class TellerMixin:
    teller_id = models.CharField(max_length=50, blank=True) # This is not working :/


class Bill(Transaction):
    """A payment made out of the account to a company"""

    class Meta:
        permissions = (
            ('can_view_involved_bills', 'Can view the bills where involved'),
            ('can_view_all_bills', 'Can view all bills'),
        )

    service = models.ForeignKey(Service, on_delete=models.PROTECT)
    due_by = models.DateField()

    @property
    def payments(self):
        raise NotImplementedError

    def __str__(self):
        return self.service.name + self.amount_human


class Share(Transaction):
    """A person's share of a bill"""

    class Meta:
        permissions = (
            ('can_view_own_shares', 'Can view their own shares'),
            ('can_view_all_shares', 'Can view all shares'),
        )

    bill = models.ForeignKey(Bill, on_delete=models.PROTECT)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)


class Payment(Transaction):
    """A payment made into the account by a person"""

    class Meta:
        permissions = (
            ('can_view_own_payments', 'Can view their own payments'),
            ('can_view_all_payments', 'Can view all payments'),
        )

    person = models.ForeignKey(Person, on_delete=models.PROTECT)
