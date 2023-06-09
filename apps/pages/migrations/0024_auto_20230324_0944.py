# Generated by Django 3.2.18 on 2023-03-24 09:44

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0023_delete_staticpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='privacypolicypage',
            name='left_column_text',
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='privacypolicypage',
            name='seo_image',
            field=models.ForeignKey(blank=True, help_text='The image displayed when a page gets posted on social media.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='pages.customimage', verbose_name='Seo Image'),
        ),
        migrations.AddField(
            model_name='termsandconditionspage',
            name='left_column_text',
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='termsandconditionspage',
            name='right_column_text',
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='termsandconditionspage',
            name='seo_image',
            field=models.ForeignKey(blank=True, help_text='The image displayed when a page gets posted on social media.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='pages.customimage', verbose_name='Seo Image'),
        ),
    ]
