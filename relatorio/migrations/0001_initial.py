# Generated by Django 4.1.4 on 2023-01-14 03:20

from django.db import migrations, models
import django.db.models.deletion
import sobreviventes.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sobreviventes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sobreviventes', models.CharField(max_length=50, verbose_name=sobreviventes.models.Sobreviventes)),
                ('infectados', models.IntegerField(verbose_name=sobreviventes.models.Sobreviventes)),
                ('n_infectados', models.IntegerField(verbose_name=sobreviventes.models.Sobreviventes)),
                ('agua', models.IntegerField(verbose_name=sobreviventes.models.Inventario)),
                ('alimento', models.IntegerField(verbose_name=sobreviventes.models.Inventario)),
                ('medicamento', models.IntegerField(verbose_name=sobreviventes.models.Inventario)),
                ('municao', models.IntegerField(verbose_name=sobreviventes.models.Inventario)),
            ],
        ),
        migrations.CreateModel(
            name='Pontos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pontos', models.IntegerField()),
                ('infectados', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relatorio.sobreviventes')),
            ],
        ),
    ]
