# Generated by Django 3.0.4 on 2020-03-08 00:32

from django.utils.text import slugify
from django.db import migrations, models


def populate_faculty_slugs(apps, schema_editor):
    """populate faculty slug"""
    db_alias = schema_editor.connection.alias
    Faculty = apps.get_model('faculty', 'Faculty')
    for row in Faculty.objects.using(db_alias).filter(slug__isnull=True):
        # Cannot use signal inside of a migration
        slug = "{} {}".format(row.first_name, row.last_name)
        slug = slugify(slug)
        if Faculty.objects.filter(slug=slug).exists():
            slug = "{}-{}".format(slug, row.pk)
        row.slug = slug
        row.save()


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0002_profile_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='slug',
            field=models.SlugField(
                blank=True, editable=False, max_length=80, unique=True, null=True,
                help_text='Slug field to uniquely identify faculty in URLs (based off of name)',
            ),
        ),
        migrations.RunPython(populate_faculty_slugs, reverse_code=migrations.RunPython.noop),
        migrations.AlterField(
            model_name='faculty',
            name='slug',
            field=models.SlugField(
                blank=True, editable=False, max_length=80, unique=True, null=False,
                help_text='Slug field to uniquely identify faculty in URLs (based off of name)',
            ),
        ),
    ]
