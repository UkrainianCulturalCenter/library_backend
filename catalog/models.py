import pathlib
import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ["last_name", "first_name"]


class Genre(models.Model):
    """
    Describes a literary genre, such as: a novel, a detective story, a children's tale,
    fantasy, etc.
    """

    name = models.CharField(max_length=31, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        db_table_comment = (
            "Describes a literary genre, such as: a novel,"
            " a detective story, a children's tale, fantasy, etc."
        )


class Type(models.Model):
    """Describes the type of object, such as: book, magazine, board game, etc."""

    name = models.CharField(max_length=31, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        db_table_comment = (
            "Describes the type of object, such as: book, magazine, board game, etc."
        )


class Tag(models.Model):
    """Tags that users can create and add."""

    name = models.CharField(max_length=31, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        db_table_comment = "Tags that users can create and add."


def image_filename(instance: "Image", filename: str) -> pathlib.Path:
    filename = (
        f"{slugify(pathlib.Path(filename).stem)}-{uuid.uuid4()}"
        + pathlib.Path(filename).suffix
    )
    return pathlib.Path("upload/image/") / pathlib.Path(filename)


class Image(models.Model):
    picture = models.ImageField(upload_to=image_filename)


class Book(models.Model):
    class Conditions(models.TextChoices):
        """The condition of the book (magazine, game, etc.):
        excellent, good, satisfactory, needs repair, cannot be used, etc. ..."""

        EXCELLENT = "EX", _("Excellent.")
        GOOD = "GOOD", _("Good.")
        SATISFACTORY = "S", _("Satisfactory.")
        NEEDS_REPAIR = "NR", _("Needs repair.")
        NEEDS_REPLACEMENT = "REPL", _("Needs replacement.")
        DISASSEMBLED = "D", _("Disassembled: missing some elements.")

    title = models.CharField(max_length=255)
    year_of_publication = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    isbn = models.CharField(max_length=13, null=True, blank=True)
    type = models.ForeignKey("Type", on_delete=models.PROTECT)
    genre = models.ForeignKey("Genre", on_delete=models.PROTECT, null=True)
    condition = models.CharField(
        "Condition", max_length=4, choices=Conditions, default=Conditions.EXCELLENT
    )
    cost_of_compensation = models.DecimalField(
        max_digits=6, decimal_places=2, default=10.0, null=True
    )
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.PROTECT, null=True, blank=True
    )
    images = models.ManyToManyField("Image", blank=True, related_name="books")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]


class Displacement(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    to_user = models.ForeignKey(
        get_user_model(), on_delete=models.PROTECT, related_name="books_i_took"
    )
    via_user = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name="books_that_i_allowed_to_take",
    )  # TODO: CHECK in (SELECT user.id FROM user WHERE user.is_staff is True)
    datetime = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return (
            f"{self.book} moved to user: {self.to_user}, "
            f"datetime: {self.datetime} (moved by staff-user: {self.via_user})"
        )

    class Meta:
        ordering = ["-datetime"]
