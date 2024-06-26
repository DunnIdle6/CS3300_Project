# Generated by Django 4.2 on 2024-04-05 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('genre', models.CharField(choices=[('ALT', 'Alternative'), ('BLU', 'Blues'), ('CLA', 'Classical'), ('CON', 'Concert Band'), ('CNT', 'Country'), ('ELE', 'Electronic'), ('FLK', 'Folk'), ('HPH', 'Hip Hop'), ('JAZ', 'Jazz'), ('LTN', 'Latin'), ('MET', 'Metal'), ('ORC', 'Orchestral'), ('POP', 'Pop'), ('RAB', 'R&B'), ('RCK', 'Rock'), ('WLD', 'World')], max_length=100)),
                ('isOpen', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('instruments', models.CharField(max_length=100)),
                ('isLooking', models.BooleanField(default=True)),
            ],
        ),
    ]
