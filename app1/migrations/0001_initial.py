# Generated by Django 4.1.4 on 2022-12-25 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('adresse', models.CharField(max_length=50)),
                ('téléphone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('adresse', models.CharField(max_length=50)),
                ('téléphone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Type_Produit',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('designation', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('designation', models.CharField(max_length=50)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Type', to='app1.type_produit')),
            ],
        ),
    ]