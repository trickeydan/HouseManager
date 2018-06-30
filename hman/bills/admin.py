from django.contrib import admin
from bills.models import Service, Bill, Payment, Share

admin.site.register(Service)
admin.site.register(Bill)
admin.site.register(Share)
admin.site.register(Payment)
