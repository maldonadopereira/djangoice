# Generated by Django 4.0.4 on 2022-04-16 22:18

from django.db import migrations, models
import localflavor.br.models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_alter_fornecedor_email_fornecedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedor',
            name='cep_fornecedor',
            field=localflavor.br.models.BRPostalCodeField(max_length=9),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='cnpj_fornecedor',
            field=models.CharField(max_length=18),
        ),
    ]
