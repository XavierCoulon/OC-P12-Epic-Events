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


class EventStatus(models.Model):
	status = models.CharField(max_length=128, blank=False)


class Event(models.Model):

	contract = models.ForeignKey(to=Contract, on_delete=models.CASCADE, related_name="contract")
	support_contact = models.ForeignKey(to=Member, on_delete=models.PROTECT, related_name="support_contact", null=True)
	date = models.DateField(blank=False)
	status = models.ForeignKey(to=EventStatus, on_delete=models.PROTECT, related_name="event_status")
	attendees = models.IntegerField(default=0)
	notes = models.TextField(max_length=255, blank=True)
	date_created = models.DateField(auto_now_add=True)
	date_updated = models.DateField(auto_now=True)



