from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.

class User(AbstractUser):
    clothes_img=models.ImageField(null=True)
    pants_img=models.ImageField(null=True)
    #outer_img=models.ImageField(null=True)

    class UserManager(BaseUserManager):
        def create_user(self, email,
                        username,
                        password=None,
                        is_active=True,
                        is_staff=False,
                        is_admin=False,
                        is_client=True,  # anyone registered can be a client
                        is_partner=False

                        ):
            if not username:
                raise ValueError("Unique username is required")
            if not email:
                raise ValueError("User must have an email address")
            if not password:
                raise ValueError("Password is required")
            user_obj = self.model(
                email=self.normalize_username(username)
            )
            user_obj.set_password(password)  # change user password
            user_obj.username = username
            user_obj.email = email
            user_obj.staff = is_staff
            user_obj.client = is_client
            user_obj.partner = is_partner
            user_obj.admin = is_admin
            user_obj.active = is_active
            user_obj.save(using=self._db)
            return user_obj

        def create_staff_user(self, username, password=None):
            user = self.create_user(
                username,
                password=password,
                is_staff=True
            )
            return user

        def create_partner_user(self, username, password=None):
            user = self.create_user(
                username,
                password=password,
                is_partner=True
            )
            return user

        def create_client_user(self, username, password=None):
            user = self.create_user(
                username,
                password=password,
                is_client=True
            )
            return user

        def create_superuser(self, username=None, email=None, password=None):
            user = self.create_user(
                username,

                password=password,
                is_staff=True,
                is_admin=True
            )
            return user


