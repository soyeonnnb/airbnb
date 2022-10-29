from django.db import models
from common.models import CommonModel


class Photo(CommonModel):

    file = models.ImageField()
    description = models.CharField(max_length=140)
    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos",
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos",
    )

    def __str__(self):
        return "Photo File"


class Video(CommonModel):

    file = models.FileField()
    experience = models.OneToOneField(
        "experiences.Experience", on_delete=models.CASCADE, related_name="videos"
    )
    # experience 1개 당 하나의 Video 를 갖기 때문에 OneToOne 사용 (foreignkey(unique=True)와 개념적 동일)
    # 따라서 foreignkey는 역참조시 queryset을 반환하지만 OneToOne은 하나의 객체 반환

    def __str__(self):
        return "Video File"
