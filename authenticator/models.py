from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class AuthUserManager(BaseUserManager):

    def _create_user(self, email, password=None, isactive=True, isstaff=False, superuser=False):
        if not email:
            raise ValueError(_('Users must have a email.'))
        if not password:
            raise ValueError(_('Users must have a password'))
        usermanageruser = self.model(
            email=self.normalize_email(email)
        )
        usermanageruser.is_active = isactive
        usermanageruser.is_staff = isstaff
        usermanageruser.is_superuser = superuser
        usermanageruser.set_password(password)
        usermanageruser.save(using=self._db)
        return usermanageruser

    def create_staffuser(self, email, password):
        user = self._create_user(
            email,
            password=password,
            isstaff=True
        )
        return user

    def create_superuser(self, email, password):
        user = self._create_user(
            email,
            password=password,
            isstaff=True,
            superuser=True
        )
        return user


class AuthUser (AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Email'), max_length=100, unique=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('Active'), default=True)
    is_staff = models.BooleanField(_('Staff'), default=False)

    objects = AuthUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email
