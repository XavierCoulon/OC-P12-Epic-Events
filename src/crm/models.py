from django.core.validators import RegexValidator
from django.db import models

from users.models import Member


class Customer(models.Model):

	TYPE = [("L", "LEAD"), ("C", "CUSTOMER")]

	company = models.CharField(unique=True, max_length=128, blank=False)
	first_name = models.CharField(max_length=128, blank=True)
	last_name = models.CharField(max_length=128, blank=False)
	email = models.EmailField(max_length=128, blank=False)
	phoneRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
	phone = models.CharField(validators=[phoneRegex], max_length=16, blank=True)
	mobile = models.CharField(validators=[phoneRegex], max_length=16, blank=True)
	status = models.CharField(choices=TYPE, default="PROSPECT", max_length=16)
	date_created = models.DateField(auto_now_add=True)
	date_updated = models.DateField(auto_now=True)
	sales_contact = models.ForeignKey(to=Member, on_delete=models.PROTECT, related_name="sales_contact")


class Contract(models.Model):

	customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE, related_name="customer")
	amount = models.FloatField(blank=False)
	payment_due = models.DateField(blank=False)
	signed = models.BooleanField(default=False)
	date_created = models.DateField(auto_now_add=True)
	date_updated = models.DateField(auto_now=True)


class Event(models.Model):

	STATUS = [("N", "Not started"), ("I", "In progress"), ("C", "Closed")]

	contract = models.ForeignKey(to=Contract, on_delete=models.CASCADE, related_name="contract")
	support_contact = models.ForeignKey(to=Member, on_delete=models.PROTECT, related_name="support_contact", null=True)
	amount = models.FloatField(blank=False)
	date = models.DateField(blank=False)
	status = models.CharField(choices=STATUS, default="Not started", max_length=16)
	attendees = models.IntegerField(default=0)
	notes = models.TextField(max_length=255, blank=True)
	date_created = models.DateField(auto_now_add=True)
	date_updated = models.DateField(auto_now=True)

