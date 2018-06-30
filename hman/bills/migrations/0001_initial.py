# Generated by Django 2.0.6 on 2018-06-30 17:59

import bills.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('people', '0001_initial')
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('comp', 'Complete'), ('pend', 'Pending')], default='pend', max_length=4)),
                ('amount', models.IntegerField()),
                ('due_by', models.DateField()),
            ],
            options={
                'permissions': (('can_view_involved_bills', 'Can view the bills where involved'), ('can_view_all_bills', 'Can view all bills')),
            },
            bases=(bills.models.TellerMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('comp', 'Complete'), ('pend', 'Pending')], default='pend', max_length=4)),
                ('amount', models.IntegerField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='people.Person')),
            ],
            options={
                'permissions': (('can_view_own_payments', 'Can view their own payments'), ('can_view_all_payments', 'Can view all payments')),
            },
            bases=(bills.models.TellerMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
            name='Share',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('comp', 'Complete'), ('pend', 'Pending')], default='pend', max_length=4)),
                ('amount', models.IntegerField()),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bills.Bill')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='people.Person')),
            ],
            options={
                'permissions': (('can_view_own_shares', 'Can view their own shares'), ('can_view_all_shares', 'Can view all shares')),
            },
        ),
        migrations.AddField(
            model_name='bill',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bills.Service'),
        ),
    ]
