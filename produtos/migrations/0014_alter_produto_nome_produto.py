# Generated by Django 4.0.3 on 2022-04-02 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0013_alter_produto_nome_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='nome_produto',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]