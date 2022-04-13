from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class Member(AbstractBaseUser):

	TEAM = [
		("P", "Support"),
		("S", "Sales"),
		("A", "Admin"),
	]

	email = models.EmailField(unique=True, max_length=255, blank=False)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	team = models.CharField(choices=TEAM, max_length=64)

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ["team"]

	def save(self, *args, **kwargs):
		if self.team == "Admin":
			self.is_staff = True
		super().save(*args, **kwargs)


