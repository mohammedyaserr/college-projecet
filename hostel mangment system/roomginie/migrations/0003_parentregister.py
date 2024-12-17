# Generated by Django 3.2.5 on 2024-11-15 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RoomGenie', '0002_rename_address_studentregister_adrs'),
    ]

    operations = [
        migrations.CreateModel(
            name='parentregister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(blank=True, max_length=50, null=True)),
                ('sname', models.CharField(blank=True, max_length=50, null=True)),
                ('adrs', models.TextField(blank=True, null=True)),
                ('phno', models.IntegerField(blank=True, null=True)),
                ('pid', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('pas', models.CharField(blank=True, max_length=8, null=True)),
            ],
        ),
    ]
