# Generated by Django 5.0.6 on 2024-05-17 14:03

import ckeditor_uploader.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("block", "0002_blogpost"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Birthday",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "person_name",
                    models.CharField(max_length=200, verbose_name="Person Name"),
                ),
                ("birth_date", models.DateField(verbose_name="Birth Date")),
                ("gift_ideas", models.TextField(blank=True, verbose_name="Gift Ideas")),
                (
                    "is_celebrated",
                    models.BooleanField(default=False, verbose_name="Is Celebrated"),
                ),
                ("deleted", models.BooleanField(default=False, verbose_name="Deleted")),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250, verbose_name="Title")),
                ("body", ckeditor_uploader.fields.RichTextUploadingField()),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                ("last_updated_date", models.DateTimeField(auto_now=True)),
                ("deleted", models.BooleanField(default=False)),
                (
                    "recipients",
                    models.ManyToManyField(
                        blank=True,
                        related_name="received_posts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sent_posts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="title",
            field=models.CharField(max_length=250, verbose_name="Title"),
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "post",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="block.post",
                    ),
                ),
                ("name", models.CharField(max_length=200, verbose_name="Name")),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="Description"),
                ),
                ("date", models.DateField(blank=True, null=True, verbose_name="Date")),
                ("time", models.TimeField(blank=True, null=True, verbose_name="Time")),
                ("deleted", models.BooleanField(default=False, verbose_name="Deleted")),
            ],
        ),
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "post",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="block.post",
                    ),
                ),
                ("title", models.CharField(max_length=200, verbose_name="Title")),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="Description"),
                ),
                (
                    "release_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Release Date"
                    ),
                ),
                (
                    "duration",
                    models.IntegerField(blank=True, null=True, verbose_name="Duration"),
                ),
                ("deleted", models.BooleanField(default=False, verbose_name="Deleted")),
            ],
        ),
        migrations.CreateModel(
            name="Shopping",
            fields=[
                (
                    "post",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="block.post",
                    ),
                ),
                (
                    "product_name",
                    models.CharField(max_length=200, verbose_name="Product Name"),
                ),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="Description"),
                ),
                (
                    "price",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=10,
                        null=True,
                        verbose_name="Price",
                    ),
                ),
                (
                    "store",
                    models.CharField(blank=True, max_length=200, verbose_name="Store"),
                ),
                ("deleted", models.BooleanField(default=False, verbose_name="Deleted")),
            ],
        ),
        migrations.DeleteModel(
            name="Blog",
        ),
        migrations.DeleteModel(
            name="Task",
        ),
    ]
