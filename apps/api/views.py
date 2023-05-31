from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.routers import DefaultRouter
from rest_framework.response import Response
from apps.services.models import ServicePage,ServiceLocation,ServiceType
from apps.api.serializers import ServicePageSerializer,ServiceLocationSerializer,ServiceTypeSerializer
router = DefaultRouter()

# A Viewset responsible for listing all the service pages(clinics).
class ServicesViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = ServicePageSerializer
    queryset = ServicePage.objects.all()
    def list(self, request, *args, **kwargs):
        location_id = self.request.GET.get('location', None)
        if location_id:
            try:
                location_id = int(location_id)
            except ValueError:
                location_id = None
        service_type_id = self.request.GET.get('type', None)
        if service_type_id:
            try:
                service_type_id = int(service_type_id)
            except ValueError:
                service_type_id = None
        if location_id and service_type_id:
            queryset = ServicePage.objects.filter(location__id=location_id).filter(service_type__id=service_type_id)
        elif location_id:
            queryset = ServicePage.objects.filter(location__id=location_id)
        elif service_type_id:
            queryset = ServicePage.objects.filter(service_type__id=service_type_id)
        else:
            queryset = ServicePage.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

# A Viewset responsible for listing all the service pages(clinics) locations.
class ServiceLocationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ServiceLocationSerializer
    queryset = ServiceLocation.objects.all()

# A Viewset responsible for listing all the service pages(clinics) service types.
class ServiceTypeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ServiceTypeSerializer
    queryset = ServiceType.objects.all()

router.register(r'services', ServicesViewSet)
router.register(r'services-locations', ServiceLocationViewSet)
router.register(r'services-types', ServiceTypeViewSet)