# Generated by Django 4.0.3 on 2022-03-27 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0005_alter_produto_fornecedor'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='marca_produto',
            field=models.CharField(max_length=50, null=True),
        ),
    ]