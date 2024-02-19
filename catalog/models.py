from django.db import models
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
