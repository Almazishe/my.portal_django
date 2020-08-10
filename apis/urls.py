from django.urls import path

from .views import  (StorageList, 
                    StorageDetailAPI,
                    StateListAPI,
                    CatListAPI,
                    SubCatListAPI,
                    RespListAPI
                    )

urlpatterns = [
    path('storage/list/', StorageList.as_view(), name='storage_list'),
    path('storage/detail/<int:pk>/', StorageDetailAPI.as_view(), name='storage-detail'),
    path('state/list/', StateListAPI.as_view(), name='state-list'),
    path('cat/list/', CatListAPI.as_view(), name='cat-list'),
    path('subcat/list/', SubCatListAPI.as_view(), name='subcat-list'),
    path('resp/list/', RespListAPI.as_view(), name='resp-list'),
]
