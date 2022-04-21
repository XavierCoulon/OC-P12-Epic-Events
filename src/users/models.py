from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
	def create_user(self, email, password=None, team=None, **kwargs):
		if not email:
			raise ValueError("You must enter an email.")

		user = self.model(email=self.normalize_email(email), team=team)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, email, password=None, team=None):
		user = self.create_user(email=email, password=password, team="Admin")
		user.is_staff = True
		user.save()
		return user


class Member(AbstractBaseUser, PermissionsMixin):

	TEAM = [
		("P", "Support"),
		("S", "Sales"),
		("A", "Admin"),
	]

	email = models.EmailField(unique=True, max_length=255, blank=False)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	team = models.CharField(choices=TEAM, max_length=64, blank=False)

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ["team"]

	objects = CustomUserManager()

	def has_perm(self, perm, obj=None):
		print(f"from has_perm / model: {perm}")
		return True

	def has_module_perms(self, perm, obj=None):
		return True

	def save(self, *args, **kwargs):
		if self.team == "A":
			self.is_staff = True
		super().save()

