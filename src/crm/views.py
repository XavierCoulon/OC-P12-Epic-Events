from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from crm.models import Customer, Contract, Event
from crm.serializers import CustomerSerializer, ContractSerializer, EventSerializer


class CustomerViewset(ModelViewSet):
	serializer_class = CustomerSerializer
	queryset = Customer.objects.all()
	filter_backends = [DjangoFilterBackend]
	filter_fields = ["company", "last_name", "email", "sales_contact"]


class ContractViewset(ModelViewSet):
	serializer_class = ContractSerializer
	queryset = Contract.objects.all()
	filter_backends = [DjangoFilterBackend]
	filter_fields = ["customer", "amount", "signed", "customer__company", "customer__last_name"]


class EventViewset(ModelViewSet):
	serializer_class = EventSerializer
	queryset = Event.objects.all()
	filter_backends = [DjangoFilterBackend]
	filter_fields = ["contract", "contract__customer", "contract__customer__company", "date", "support_contact"]
