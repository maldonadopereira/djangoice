# Generated by Django 4.0.4 on 2022-04-16 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_alter_fornecedor_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedor',
            name='email_fornecedor',
            field=models.EmailField(max_length=50),
        ),
    ]
