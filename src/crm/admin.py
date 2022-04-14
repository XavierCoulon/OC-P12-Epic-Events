from django.contrib import admin

from crm.models import Contract, Event, Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	list_display = (
		"company",
		"first_name",
		"last_name",
		"email",
		"phone",
		"mobile",
		"status",
		"date_created",
		"date_updated",
		"sales_contact",
	)


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
	list_display = (
		"customer",
		"amount",
		"payment_due",
		"signed",
		"date_created",
		"date_updated",
	)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	list_display = (
		"contract",
		"support_contact",
		"amount",
		"date",
		"status",
		"attendees",
		"notes",
		"date_created",
		"date_updated",
	)
