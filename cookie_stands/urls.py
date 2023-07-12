from django.urls import path
from .views import CookieStandList, CookieStandDetail

app_name = 'cookie_stands'

urlpatterns = [
    path("", CookieStandList.as_view(), name="CookieStand_list"),
    path("<int:pk>/", CookieStandDetail.as_view(), name="CookieStand_detail"),
]
