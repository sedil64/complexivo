from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MesaViewSet, PedidoViewSet
from .menu_types_views import service_types_list_create, service_types_detail
from .order_events_views import vehicle_services_list_create, vehicle_services_detail

router = DefaultRouter()
router.register(r"Mesas", MesaViewSet, basename="Mesas")
router.register(r"Pedidos", PedidoViewSet, basename="Pedidos")

urlpatterns = [
    # Mongo
    path("menu-types/", service_types_list_create),
    path("menu-types//", service_types_detail),
    path("order-events/", vehicle_services_list_create),
    path("order-events//", vehicle_services_detail),
]

urlpatterns += router.urls