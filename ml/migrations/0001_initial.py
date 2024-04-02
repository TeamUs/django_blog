# Generated by Django 4.2.1 on 2024-04-02 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passenger_id', models.IntegerField(unique=True)),
                ('sex', models.CharField(max_length=255)),
                ('age', models.FloatField(null=True)),
                ('parch', models.IntegerField(null=True)),
                ('fare', models.FloatField(null=True)),
                ('survived', models.IntegerField(null=True)),
                ('is_test', models.IntegerField(null=True)),
            ],
        ),
    ]
