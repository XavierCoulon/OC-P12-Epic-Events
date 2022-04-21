from django.contrib import admin
from django import forms
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin
from rest_framework.permissions import DjangoModelPermissions

from users.models import Member


class MemberCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Member
        fields = ('email', 'password', 'team', 'is_active', 'is_staff', 'groups')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class MemberChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Member
        fields = ('email', 'password', 'team', 'is_active', 'is_staff', 'groups')


@admin.register(Member)
class MemberAdmin(UserAdmin):

    class Meta:
        model = Member

    form = MemberChangeForm
    add_form = MemberCreationForm

    fieldsets = ((None, {"fields": ("email", "password", "team", "groups", "user_permissions")}),)
    add_fieldsets = (
        (
            None,
            {
                "fields": ("email", "password1", "password2"),
            },
        ),
    )

    list_display = ('email', 'team', 'is_active', 'is_staff')

    ordering = ()
    #list_filter = ()
    filter_horizontal = ('groups', 'user_permissions')

    def save_model(self, request, obj, form, change):
        if obj.team == "A" and not obj.is_staff:
            messages.add_message(request, messages.INFO, "Admin team member, so automatically set as part of staff.")
        super().save_model(request, obj, form, change)

