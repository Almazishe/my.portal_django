from django.urls import path
from rest_framework import routers

from .views import  (
                    StorageViewSet,
                    CategoryViewSet,
                    SubCategoryViewSet,
                    StateViewSet,
                    RespViewSet,
                    UserViewSet
                    )

router = routers.DefaultRouter()
router.register('storages',StorageViewSet)
router.register('categories',CategoryViewSet)
router.register('subcategories',SubCategoryViewSet)
router.register('states',StateViewSet)
router.register('resps',RespViewSet)
router.register('users', UserViewSet)


urlpatterns = router.urls 
