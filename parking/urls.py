from django.urls import path

from . import views


urlpatterns = [
    path(
        'parking-spots/',
        views.parking_spot_list_create,
        name='parking_spot_list_create'
    ),
    path(
        'parking-spots/free/',
        views.free_parking_spots,
        name='free_parking_spots'
    ),
    path(
        'parking-spots/statistics/',
        views.parking_statistics,
        name='parking_statistics'
    ),
    path(
        'parking-spots/<int:spot_id>/',
        views.parking_spot_detail,
        name='parking_spot_detail'
    ),
    path(
        'parking-spots/<int:spot_id>/status/',
        views.update_parking_spot_status,
        name='update_parking_spot_status'
    ),
]