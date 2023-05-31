# Generated by Django 3.2.18 on 2023-04-11 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
        ('wagtailredirects', '0008_add_verbose_name_plural'),
        ('wagtailforms', '0005_alter_formsubmission_form_data'),
        ('pages', '0047_contentpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='termsandconditionspage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='termsandconditionspage',
            name='seo_image',
        ),
        migrations.DeleteModel(
            name='PrivacyPolicyPage',
        ),
        migrations.DeleteModel(
            name='TermsAndConditionsPage',
        ),
    ]
