from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.CategoryViewSet.as_view(
            {
                # HTTP method와 class method를 연걸
                "get": "list",  # 전체 queryset 리스트 가져옴
                "post": "create",
            }
        ),
    ),
    path(
        "<int:pk>",
        views.CategoryViewSet.as_view(
            {
                "get": "retrieve",  # 여러개 중 하나만 가져옴
                "put": "partial_update",
                "delete": "destroy",
            }
        ),
    ),  # /GET
]
