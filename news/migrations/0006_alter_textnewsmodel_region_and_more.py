# Generated by Django 4.2.3 on 2023-07-28 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_textnewsmodel_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textnewsmodel',
            name='region',
            field=models.CharField(choices=[('tashkent-city', 'Tashkent city'), ('tashkent-reg', 'Tashkent region'), ('karakalpakstan', 'Karakalpakstan'), ('andijan', 'Andijan'), ('fergana', 'Fergana'), ('namangan', 'Namangan'), ('samarkand', 'Samarkand'), ('bukhara', 'Bukhara'), ('khorazm', 'Khorazm'), ('surkhandarya', 'Surkhandarya'), ('kashkadarya', 'Kashkadarya'), ('jizzakh', 'Jizzakh'), ('sirdarya', 'Sirdarya'), ('navoi', 'Navoi'), ('other', 'Other')], db_index=True, default='other', max_length=14, verbose_name='Region'),
        ),
        migrations.AlterField(
            model_name='textnewsmodel',
            name='region_en',
            field=models.CharField(choices=[('tashkent-city', 'Tashkent city'), ('tashkent-reg', 'Tashkent region'), ('karakalpakstan', 'Karakalpakstan'), ('andijan', 'Andijan'), ('fergana', 'Fergana'), ('namangan', 'Namangan'), ('samarkand', 'Samarkand'), ('bukhara', 'Bukhara'), ('khorazm', 'Khorazm'), ('surkhandarya', 'Surkhandarya'), ('kashkadarya', 'Kashkadarya'), ('jizzakh', 'Jizzakh'), ('sirdarya', 'Sirdarya'), ('navoi', 'Navoi'), ('other', 'Other')], db_index=True, default='other', max_length=14, null=True, verbose_name='Region'),
        ),
        migrations.AlterField(
            model_name='textnewsmodel',
            name='region_ru',
            field=models.CharField(choices=[('tashkent-city', 'Tashkent city'), ('tashkent-reg', 'Tashkent region'), ('karakalpakstan', 'Karakalpakstan'), ('andijan', 'Andijan'), ('fergana', 'Fergana'), ('namangan', 'Namangan'), ('samarkand', 'Samarkand'), ('bukhara', 'Bukhara'), ('khorazm', 'Khorazm'), ('surkhandarya', 'Surkhandarya'), ('kashkadarya', 'Kashkadarya'), ('jizzakh', 'Jizzakh'), ('sirdarya', 'Sirdarya'), ('navoi', 'Navoi'), ('other', 'Other')], db_index=True, default='other', max_length=14, null=True, verbose_name='Region'),
        ),
        migrations.AlterField(
            model_name='textnewsmodel',
            name='region_uz',
            field=models.CharField(choices=[('tashkent-city', 'Tashkent city'), ('tashkent-reg', 'Tashkent region'), ('karakalpakstan', 'Karakalpakstan'), ('andijan', 'Andijan'), ('fergana', 'Fergana'), ('namangan', 'Namangan'), ('samarkand', 'Samarkand'), ('bukhara', 'Bukhara'), ('khorazm', 'Khorazm'), ('surkhandarya', 'Surkhandarya'), ('kashkadarya', 'Kashkadarya'), ('jizzakh', 'Jizzakh'), ('sirdarya', 'Sirdarya'), ('navoi', 'Navoi'), ('other', 'Other')], db_index=True, default='other', max_length=14, null=True, verbose_name='Region'),
        ),
    ]