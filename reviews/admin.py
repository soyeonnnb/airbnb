from django.contrib import admin
from .models import Review


class WordFilter(admin.SimpleListFilter):

    title = "Filter by Word"
    parameter_name = "word"  # url에 표시

    def lookups(self, request, model_admin):
        # request에는 admin.action과 동일하게 현재 이 메소드를 호출하고 있는 user에 대한 정보가 들어감
        # model_admin도 admin.action과 동일하게 이 필터를 사용하는 클래스가 들어감
        return [
            ("good", "Good"),  # 첫번째 인자는 url에 나타나고, 두번째 인자는 사용자에게 보여짐
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request, reviews):  # 3번째는 queryset
        word = self.value()
        # self.value()를 이용하면 굳이 request.GET으로 parameter를 선택하지 않아도 사용자가 선택한 인자를 가져올 수 있음
        if word:
            return reviews.filter(payload__contains=word)
        else:  # 안하면 word가 없는 상태에서 filtering을 하게 됨으로 오류("Cannot use None as a query value")발생
            return reviews


class GoodBadFilter(admin.SimpleListFilter):

    title = "Good or Bad Reviews"
    parameter_name = "goodOrBad"

    def lookups(self, request, model_admin):
        return [("good", "Good Reviews"), ("bad", "Bad Reviews")]

    def queryset(self, request, reviews):
        select = self.value()
        if select == "good":
            return reviews.filter(rating__gte=3)
        elif select == "bad":
            return reviews.filter(rating__lt=3)
        else:
            return reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = ("__str__", "payload")
    list_filter = (
        WordFilter,
        GoodBadFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )
