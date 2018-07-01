from django.contrib import admin
from bills.models import Service, Bill, Payment

admin.site.register(Service)
admin.site.register(Bill)
admin.site.register(Payment)
