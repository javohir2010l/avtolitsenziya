# user/urls.py
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView

from .views import (
    UserProfileView,
    UserPutyovkasView,
    UserInspectionsView,
    UserPaymentsView
)

urlpatterns = [
    # Bu URL /api/user/ so'rovini /api/user/profile/ manziliga yo'naltiradi.
    path('', RedirectView.as_view(url=reverse_lazy('user-profile'), permanent=True), name='user-home'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('putyovkas/', UserPutyovkasView.as_view(), name='user-putyovkas'),
    path('inspections/', UserInspectionsView.as_view(), name='user-inspections'),
    path('payments/', UserPaymentsView.as_view(), name='user-payments'),
]
