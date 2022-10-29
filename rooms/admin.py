from django.contrib import admin
from .models import Room, Amenity


@admin.action(description="모든 price를 0으로 설정함")
def reset_prices(model_admin, request, rooms):
    # model_admin에는 실행된 해당 model이 들어감
    # request에는 누가 이 함수를 실행했는지 들어감
    # queryset(여기에선 rooms)에는 action을 실행하려 선택한 객체들이 들어감
    # admin.action을 이용해서 실무에서 해당 queryset을 엑셀로 옮긴다든지 할 수 있음.
    for room in rooms.all():
        room.price = 0
        room.save()


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    actions = (reset_prices,)

    list_display = (
        "name",
        "price",
        "kind",
        "total_amenities",
        "rating",
        "owner",
        "created_at",
    )

    list_filter = (
        "country",
        "city",
        "pet_friendly",
        "kind",
        "amenities",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "name",
        "^price",  # startswith
        "=owner__username",  # __를 사용하면 foreign key로 그에 해당하는 attrs로 검색 가능
    )


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )
    readonly_fields = ("created_at", "updated_at")
