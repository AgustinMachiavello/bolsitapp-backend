from django.urls import path, include
from rest_framework import routers

from .views import *

routerBags = routers.DefaultRouter()
routerBags.register(r'bags', BagViewSet, basename='bags')

routerBranches = routers.DefaultRouter()
routerBranches.register(r'branches', BranchViewSet, basename='branches')

routerExchanges = routers.DefaultRouter()
routerExchanges.register(r'exchanges', ExchangeViewSet, basename='exchanges')

routerPurchases = routers.DefaultRouter()
routerPurchases.register(r'purchases', PurchaseViewSet, basename='purchases')

routerStores = routers.DefaultRouter()
routerStores.register(r'stores', StoreViewSet, basename='stores')

urlpatterns = [
    path('', include(routerBags.urls)),
    path('', include(routerBranches.urls)),
    path('', include(routerExchanges.urls)),
    path('', include(routerPurchases.urls)),
    path('', include(routerStores.urls)),
]
