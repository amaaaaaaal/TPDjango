# Generated by Django 5.0.2 on 2024-02-26 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0004_fournisseur_produit_fournisseur'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProduitNC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duree_garantie', models.CharField(max_length=100)),
            ],
        ),
    ]
