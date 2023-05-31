# Generated by Django 3.2.18 on 2023-03-23 07:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import wagtail.images.models
import wagtail.models.collections
import wagtail.search.index


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'verbose_name': 'Content page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='CustomImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('file', wagtail.images.models.WagtailImageField(height_field='height', upload_to=wagtail.images.models.get_upload_to, verbose_name='file', width_field='width')),
                ('width', models.IntegerField(editable=False, verbose_name='width')),
                ('height', models.IntegerField(editable=False, verbose_name='height')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created at')),
                ('focal_point_x', models.PositiveIntegerField(blank=True, null=True)),
                ('focal_point_y', models.PositiveIntegerField(blank=True, null=True)),
                ('focal_point_width', models.PositiveIntegerField(blank=True, null=True)),
                ('focal_point_height', models.PositiveIntegerField(blank=True, null=True)),
                ('file_size', models.PositiveIntegerField(editable=False, null=True)),
                ('file_hash', models.CharField(blank=True, db_index=True, editable=False, max_length=40)),
                ('collection', models.ForeignKey(default=wagtail.models.collections.get_root_collection_id, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.collection', verbose_name='collection')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text=None, through='taggit.TaggedItem', to='taggit.Tag', verbose_name='tags')),
                ('uploaded_by_user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='uploaded by user')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.images.models.ImageFileMixin, wagtail.search.index.Indexed, models.Model),
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'verbose_name': 'Home page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='StaticPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('html_name', models.CharField(choices=[('404.html', '404.html'), ('500.html', '500.html'), ('blog/blog_category_page.html', 'blog/blog_category_page.html'), ('blog/blog_index_page.html', 'blog/blog_index_page.html'), ('blog/post_page.html', 'blog/post_page.html'), ('includes/footer.html', 'includes/footer.html'), ('includes/main-nav.html', 'includes/main-nav.html'), ('pages/about.html', 'pages/about.html'), ('pages/blog-post.html', 'pages/blog-post.html'), ('pages/content_page.html', 'pages/content_page.html'), ('pages/home_page.html', 'pages/home_page.html'), ('pages/service-finder.html', 'pages/service-finder.html'), ('pages/service.html', 'pages/service.html'), ('pages/static_page.html', 'pages/static_page.html'), ('pages/text-page.html', 'pages/text-page.html')], max_length=250, verbose_name='Choose html')),
            ],
            options={
                'verbose_name': 'Static page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='RedirectPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('external_redirect', models.URLField(blank=True, verbose_name='External link')),
                ('page_redirect', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
            ],
            options={
                'verbose_name': 'Redirect page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='CustomRendition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter_spec', models.CharField(db_index=True, max_length=255)),
                ('file', wagtail.images.models.WagtailImageField(height_field='height', upload_to=wagtail.images.models.get_rendition_upload_to, width_field='width')),
                ('width', models.IntegerField(editable=False)),
                ('height', models.IntegerField(editable=False)),
                ('focal_point_key', models.CharField(blank=True, default='', editable=False, max_length=16)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='renditions', to='pages.customimage')),
            ],
            options={
                'unique_together': {('image', 'filter_spec', 'focal_point_key')},
            },
            bases=(wagtail.images.models.ImageFileMixin, models.Model),
        ),
    ]
