from django.db import models
from django.urls import reverse
from people.models import Person
from hman.models import Model


class Service(Model):

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


class Transaction(Model):

    description = models.TextField()
    amount = models.IntegerField()

    @property
    def amount_human(self):
        return " £{0:.2f}".format(self.amount / 100)


class Bill(Transaction):
    """A payment made out of the account to a company"""

    COMPLETE = 'comp'
    PENDING = 'pend'

    STATUS_CHOICES = (
        (COMPLETE, 'Complete'),
        (PENDING, 'Pending'),
    )

    class Meta:
        permissions = (
            ('can_view_involved_bills', 'Can view the bills where involved'),
            ('can_view_all_bills', 'Can view all bills'),
        )

    service = models.ForeignKey(Service, on_delete=models.PROTECT)
    due_by = models.DateField()
    status = models.CharField(choices=STATUS_CHOICES, default=PENDING, max_length=4)

    def __str__(self):
        return self.service.name + self.amount_human

    def get_absolute_url(self):
        return reverse('bills:bills_view', args=[self.id])

    @property
    def payments(self):
        return Payment.objects.filter(associated_bill=self)

    @property
    def status_human(self):
        for pair in Bill.STATUS_CHOICES:
            if pair[0] == self.status:
                return pair[1]
        return self.status


class Payment(Transaction):
    """A change in a person's balance"""

    class Meta:
        permissions = (
            ('can_view_own_payments', 'Can view their own payments'),
            ('can_view_all_payments', 'Can view all payments'),
        )

    associated_bill = models.ForeignKey(Bill, on_delete=models.PROTECT, null=True, blank=True)  # Associated bill if applicable
    person = models.ForeignKey(Person, on_delete=models.PROTECT)  # Person the payment was made to / from
    date = models.DateField(null=True, blank=True)  # Date the payment was made

    def __str__(self):
        return str(self.date) + " " + self.person.full_name + self.amount_human
