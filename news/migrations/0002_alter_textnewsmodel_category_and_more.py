# Generated by Django 4.2.3 on 2023-07-27 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textnewsmodel',
            name='category',
            field=models.CharField(choices=[('uzbekistan', 'UZBEKISTAN'), ('world', 'WORLD'), ('finance', 'FINANCE'), ('society', 'SOCIETY'), ('science-techno', 'SCIENCE-TECHNOLOGY'), ('sport', 'SPORTS'), ('point-of-view', 'POINT OF VIEW'), ('ad', 'ADVERTISEMENT')], db_index=True, max_length=14, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='textnewsmodel',
            name='region',
            field=models.CharField(choices=[('tashkent-city', 'Tashkent city'), ('tashkent-reg', 'Tashkent region'), ('karakalpakstan', 'Karakalpakstan'), ('andijan', 'Andijan'), ('fergana', 'Fergana'), ('namangan', 'Namangan'), ('samarkand', 'Samarkand'), ('bukhara', 'Bukhara'), ('khorazm', 'Khorazm'), ('surkhandarya', 'Surkhandarya'), ('kashkadarya', 'Kashkadarya'), ('jizzakh', 'Jizzakh'), ('sirdarya', 'Sirdarya'), ('navoi', 'Navoi')], db_index=True, max_length=14, verbose_name='Region'),
        ),
    ]
