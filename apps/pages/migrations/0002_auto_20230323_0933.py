# Generated by Django 3.2.18 on 2023-03-23 09:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailcore', '0083_workflowcontenttype'),
        ('wagtailforms', '0005_alter_formsubmission_form_data'),
        ('wagtailredirects', '0008_add_verbose_name_plural'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContentPage',
            new_name='AboutPage',
        ),
        migrations.AlterModelOptions(
            name='aboutpage',
            options={'verbose_name': 'About page'},
        ),
        migrations.AlterField(
            model_name='staticpage',
            name='html_name',
            field=models.CharField(choices=[('404.html', '404.html'), ('500.html', '500.html'), ('blog/blog_category_page.html', 'blog/blog_category_page.html'), ('blog/blog_index_page.html', 'blog/blog_index_page.html'), ('blog/blog_page.html', 'blog/blog_page.html'), ('blog/post_page.html', 'blog/post_page.html'), ('includes/footer.html', 'includes/footer.html'), ('includes/main-nav.html', 'includes/main-nav.html'), ('pages/about_page.html', 'pages/about_page.html'), ('pages/home_page.html', 'pages/home_page.html'), ('pages/service-finder.html', 'pages/service-finder.html'), ('pages/service.html', 'pages/service.html'), ('pages/static_page.html', 'pages/static_page.html'), ('pages/text-page.html', 'pages/text-page.html'), ('seo.html', 'seo.html')], max_length=250, verbose_name='Choose html'),
        ),
    ]
