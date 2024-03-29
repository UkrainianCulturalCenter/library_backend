# Generated by Django 5.0.1 on 2024-03-20 10:16

import catalog.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
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
                ("first_name", models.CharField(max_length=63)),
                ("last_name", models.CharField(max_length=63)),
            ],
            options={
                "ordering": ["last_name", "first_name"],
            },
        ),
        migrations.CreateModel(
            name="Genre",
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
                ("name", models.CharField(max_length=31, unique=True)),
            ],
            options={
                "db_table_comment": "Describes a literary genre, such as: a novel, a detective story, a children's tale, fantasy, etc.",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Image",
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
                ("picture", models.ImageField(upload_to=catalog.models.image_filename)),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=31, unique=True)),
            ],
            options={
                "db_table_comment": "Tags that users can create and add.",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Type",
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
                ("name", models.CharField(max_length=31, unique=True)),
            ],
            options={
                "db_table_comment": "Describes the type of object, such as: book, magazine, board game, etc.",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=255)),
                ("year_of_publication", models.IntegerField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("isbn", models.CharField(blank=True, max_length=13, null=True)),
                (
                    "condition",
                    models.CharField(
                        choices=[
                            ("EX", "Excellent."),
                            ("GOOD", "Good."),
                            ("S", "Satisfactory."),
                            ("NR", "Needs repair."),
                            ("REPL", "Needs replacement."),
                            ("D", "Disassembled: missing some elements."),
                        ],
                        default="EX",
                        max_length=4,
                        verbose_name="Condition",
                    ),
                ),
                (
                    "cost_of_compensation",
                    models.DecimalField(
                        decimal_places=2, default=10.0, max_digits=6, null=True
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "genre",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="catalog.genre",
                    ),
                ),
                (
                    "images",
                    models.ManyToManyField(
                        blank=True, related_name="books", to="catalog.image"
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="catalog.type"
                    ),
                ),
            ],
            options={
                "ordering": ["title"],
            },
        ),
        migrations.CreateModel(
            name="Displacement",
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
                ("datetime", models.DateTimeField(auto_now_add=True)),
                ("notes", models.TextField(blank=True, null=True)),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="catalog.book"
                    ),
                ),
                (
                    "to_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="books_i_took",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "via_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="books_that_i_allowed_to_take",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-datetime"],
            },
        ),
    ]
