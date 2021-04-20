# -*- coding: utf-8 -*-
from datetime import date

from django.core import signing
from django.conf import settings
from django.contrib.auth.models import BaseUserManager
from django.db.models import Q


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email), **kwargs)
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(email, password=password, **kwargs)
        user.is_admin = True
        user.is_active = True
        user.role = 1
        user.save(using=self._db)
        return user
