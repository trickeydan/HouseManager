# Generated by Django 2.0.6 on 2018-07-01 16:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=60)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.TextField()),
                ('owners', models.ManyToManyField(to='people.Person')),
            ],
            options={
                'permissions': (('can_view_services', 'Can view the services for the house'),),
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('amount', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('transaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bills.Transaction')),
                ('due_by', models.DateField()),
                ('status', models.CharField(choices=[('comp', 'Complete'), ('pend', 'Pending')], default='pend', max_length=4)),
                ('description', models.TextField()),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bills.Service')),
            ],
            options={
                'permissions': (('can_view_involved_bills', 'Can view the bills where involved'), ('can_view_all_bills', 'Can view all bills')),
            },
            bases=('bills.transaction',),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('transaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bills.Transaction')),
                ('date', models.DateField(blank=True, null=True)),
                ('associated_bill', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bills.Bill')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='people.Person')),
            ],
            options={
                'permissions': (('can_view_own_payments', 'Can view their own payments'), ('can_view_all_payments', 'Can view all payments')),
            },
            bases=('bills.transaction',),
        ),
    ]
