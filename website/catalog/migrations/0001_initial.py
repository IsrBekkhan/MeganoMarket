# Generated by Django 5.1.1 on 2024-10-14 13:25

import django.db.models.deletion
from django.db import migrations, models

import catalog.models
import catalog.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=100, verbose_name="Name")),
                (
                    "icon",
                    models.FileField(
                        upload_to="assets/img/icons/departments", verbose_name="Icon"
                    ),
                ),
                (
                    "archived",
                    models.BooleanField(default=False, verbose_name="Archived status"),
                ),
                (
                    "parent_category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="sub_categories",
                        to="catalog.category",
                        verbose_name="PK category",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "categories",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                    "name",
                    models.CharField(
                        db_index=True, max_length=100, verbose_name="Name"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, db_index=True, null=True, verbose_name="Description"
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=8, verbose_name="Price"
                    ),
                ),
                (
                    "manufacture",
                    models.CharField(
                        db_index=True, max_length=100, verbose_name="Manufacture"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="'Created at"),
                ),
                (
                    "archived",
                    models.BooleanField(default=False, verbose_name="Archived status"),
                ),
                (
                    "limited_edition",
                    models.BooleanField(default=False, verbose_name="Limited edition"),
                ),
                ("view", models.BooleanField(default=False, verbose_name="View")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="catalog.category",
                        verbose_name="PK category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductImage",
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
                    "image",
                    models.ImageField(
                        upload_to=catalog.utils.product_images_directory_path,
                        verbose_name="Image product",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.product",
                        verbose_name="PK product",
                    ),
                ),
            ],
        ),
    ]
