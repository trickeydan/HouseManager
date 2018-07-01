from django.db import migrations


def create_groups(apps, schema_editor):

    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    ContentType = apps.get_model('contenttypes', 'ContentType')
    Person = apps.get_model('people', 'Person')

    Bill = apps.get_model('bills', 'Bill')
    Payment = apps.get_model('bills', 'Payment')
    Service = apps.get_model('bills', 'Service')

    ct_person = ContentType.objects.get_for_model(Person)
    ct_bill = ContentType.objects.get_for_model(Bill)
    ct_payment = ContentType.objects.get_for_model(Payment)
    ct_service = ContentType.objects.get_for_model(Service)

    guest_perms = [
        (ct_person, 'can_edit_profile'),

        (ct_bill, 'can_view_involved_bills'),

        (ct_payment, 'can_view_own_payments'),

        (ct_service, 'can_view_services'),
    ]

    tenant_perms = [
        (ct_person, 'can_view_others'),
        (ct_person, 'can_list_others'),
        (ct_person, 'can_edit_profile'),

        (ct_bill, 'can_view_involved_bills'),
        (ct_bill, 'can_view_all_bills'),

        (ct_payment, 'can_view_own_payments'),
        (ct_payment, 'can_view_all_payments'),

        (ct_service, 'can_view_services'),
    ]




    guest, created = Group.objects.get_or_create(name='Guest')

    for pair in guest_perms:
        perms = Permission.objects.get_or_create(content_type=pair[0], codename=pair[1])

        for p in perms:
            guest.permissions.add(p)

    tenant, created = Group.objects.get_or_create(name='Tenant')

    for pair in tenant_perms:
        perms = Permission.objects.get_or_create(content_type=pair[0], codename=pair[1])

        for p in perms:
            tenant.permissions.add(p)


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
        ('bills', '0001_initial'),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.RunPython(create_groups)
    ]
