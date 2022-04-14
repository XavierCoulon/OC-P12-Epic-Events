from django.contrib import admin
from django.contrib import messages

from users.models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
	list_display = (
		"email",
		"team",
		"is_active",
		"is_staff",
	)

	def save_model(self, request, obj, form, change):
		# clean from Member not applied...
		if obj.team == "A" and not obj.is_staff:
			messages.add_message(request, messages.WARNING, "This member is not part of the staff.")
		super().save_model(request, obj, form, change)
