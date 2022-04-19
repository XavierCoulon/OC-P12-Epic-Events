from rest_framework.serializers import ModelSerializer

from crm.models import Customer, Contract, Event


class CustomerSerializer(ModelSerializer):
	class Meta:
		model = Customer
		fields = "__all__"


class ContractSerializer(ModelSerializer):
	class Meta:
		model = Contract
		fields = "__all__"


class EventSerializer(ModelSerializer):
	class Meta:
		model = Event
		fields = "__all__"
