from rest_framework.viewsets import ModelViewSet

from crm.models import Customer
from crm.serializers import CustomerSerializer


class CustomerViewset(ModelViewSet):
	serializer_class = CustomerSerializer

	def get_queryset(self):
		return Customer.objects.all()

