# Generated by Django 3.2.18 on 2023-04-11 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0049_auto_20230411_0435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='header_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='pages.customimage', verbose_name='Header image'),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='seo_image',
            field=models.ForeignKey(blank=True, help_text='The image displayed when a page gets posted on social media.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='pages.customimage', verbose_name='Seo image'),
        ),
        migrations.AlterField(
            model_name='contentpage',
            name='seo_image',
            field=models.ForeignKey(blank=True, help_text='The image displayed when a page gets posted on social media.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='pages.customimage', verbose_name='Seo image'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='seo_image',
            field=models.ForeignKey(blank=True, help_text='The image displayed when a page gets posted on social media.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='pages.customimage', verbose_name='Seo image'),
        ),
    ]
