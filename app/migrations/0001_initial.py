# Generated by Django 3.2.8 on 2021-10-11 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=255)),
                ('quantidade', models.IntegerField(max_length=4)),
                ('preco', models.FloatField(max_length=10)),
            ],
        ),
    ]