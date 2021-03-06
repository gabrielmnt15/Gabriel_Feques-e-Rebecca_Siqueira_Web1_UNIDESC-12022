# Generated by Django 4.0.5 on 2022-06-22 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11)),
                ('rg', models.CharField(max_length=9)),
                ('nome', models.CharField(max_length=100)),
                ('sexo', models.CharField(max_length=10)),
                ('dataNascimento', models.DateField()),
                ('carteiraTrabalho', models.CharField(max_length=100)),
                ('salario', models.IntegerField()),
                ('pis', models.CharField(max_length=100)),
            ],
        ),
    ]
