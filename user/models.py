from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as DjangoUserManager
from django.utils.translation import gettext_lazy as _

# About email verify
# https://python.plainenglish.io/how-to-send-email-with-verification-link-in-django-efb21eefffe8


class UserManager(DjangoUserManager):
    """Define custom user manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email, and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("email_is_verified", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("email_is_verified", True)

        if extra_fields.get("is_staff") is False:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is False:
            raise ValueError("Superuser must have is_superuser=True.")
        if extra_fields.get("email_is_verified") is False:
            raise ValueError("Superuser must have email_is_verified=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    class UserRole(models.TextChoices):
        SUPERUSER = "SUPER", _("Super user")
        OWNER = "OWNER", _("Resource owner")
        VOLUNTEER = "VOLUNTEER", _("Library volunteer")
        CUSTOMER = "CUSTOMER", _("Library customer")

    role = models.CharField(max_length=9, choices=UserRole, default=UserRole.CUSTOMER)
    username = None
    email = models.EmailField(_("email address"), unique=True)
    email_is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()
