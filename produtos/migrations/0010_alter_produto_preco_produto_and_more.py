# Generated by Django 4.0.3 on 2022-03-30 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0009_alter_produto_fornecedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco_produto',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='produto',
            name='quantidade_produto',
            field=models.PositiveIntegerField(default=0),
        ),
    ]