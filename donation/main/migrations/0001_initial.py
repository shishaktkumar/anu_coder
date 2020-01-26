# Generated by Django 2.2.9 on 2020-01-24 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'managed': False,
                'db_table': 'awards',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('contact1', models.IntegerField()),
                ('standard', models.IntegerField()),
                ('dateOfBirth', models.DateField()),
                ('joined_Date', models.DateField()),
                ('last_Date', models.DateField()),
                ('interests', models.CharField(max_length=500)),
            ],
            options={
                'managed': False,
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('contact1', models.IntegerField()),
                ('goods_or_services', models.CharField(max_length=400)),
                ('dateOfBirth', models.DateField()),
                ('joined_Date', models.DateField()),
                ('last_Date', models.DateField()),
            ],
            options={
                'managed': False,
                'db_table': 'supervisor',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('contact1', models.IntegerField()),
                ('expertise', models.CharField(max_length=400)),
                ('dateOfBirth', models.DateField()),
                ('joined_Date', models.DateField()),
                ('last_Date', models.DateField()),
            ],
            options={
                'managed': False,
                'db_table': 'teacher',
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('event_date', models.DateField()),
                ('awards_id', models.CharField(max_length=400)),
            ],
        ),
    ]
