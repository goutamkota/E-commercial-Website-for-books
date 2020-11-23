# Generated by Django 3.1.3 on 2020-11-23 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0007_auto_20201123_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('F', 'Fiction'), ('S', 'Science'), ('N', 'Novel'), ('H', 'History'), ('HF', 'Historical-fiction'), ('NF', 'Non-fiction'), ('M', 'Mystery'), ('P', 'Poetry'), ('B', 'Biography'), ('A', 'Autobiography'), ('CL', 'Children-literature'), ('P', 'Philosophy'), ('SH', 'Self-help')], max_length=2),
        ),
    ]
