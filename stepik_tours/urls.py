from django.urls import path

from tours.views import custom_handler404
from tours.views import custom_handler500
from tours.views import departure_view
from tours.views import main_view
from tours.views import tour_view

handler404 = custom_handler404
handler500 = custom_handler500

urlpatterns = [
    path('', main_view),
    path('departure/<str:departure>/', departure_view),
    path('tour/<int:tour_id>/', tour_view),
]
