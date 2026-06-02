from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ParkingSpot
from .serializers import ParkingSpotSerializer, ParkingSpotStatusSerializer


@api_view(['GET', 'POST'])
def parking_spot_list_create(request):
    if request.method == 'GET':
        spots = ParkingSpot.objects.all()
        serializer = ParkingSpotSerializer(spots, many=True)

        return Response({
            'success': True,
            'count': spots.count(),
            'data': serializer.data,
        })

    serializer = ParkingSpotSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response({
            'success': True,
            'message': 'Парковочное место успешно создано.',
            'data': serializer.data,
        }, status=status.HTTP_201_CREATED)

    return Response({
        'success': False,
        'message': 'Ошибка валидации данных.',
        'errors': serializer.errors,
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def parking_spot_detail(request, spot_id):
    try:
        spot = ParkingSpot.objects.get(id=spot_id)
    except ParkingSpot.DoesNotExist:
        return Response({
            'success': False,
            'message': 'Парковочное место не найдено.',
        }, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ParkingSpotSerializer(spot)

        return Response({
            'success': True,
            'data': serializer.data,
        })

    if request.method == 'PUT':
        serializer = ParkingSpotSerializer(spot, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({
                'success': True,
                'message': 'Данные парковочного места успешно обновлены.',
                'data': serializer.data,
            })

        return Response({
            'success': False,
            'message': 'Ошибка валидации данных.',
            'errors': serializer.errors,
        }, status=status.HTTP_400_BAD_REQUEST)

    spot.delete()

    return Response({
        'success': True,
        'message': 'Парковочное место успешно удалено.',
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def free_parking_spots(request):
    spots = ParkingSpot.objects.filter(status=ParkingSpot.STATUS_FREE)
    serializer = ParkingSpotSerializer(spots, many=True)

    return Response({
        'success': True,
        'count': spots.count(),
        'data': serializer.data,
    })


@api_view(['PATCH'])
def update_parking_spot_status(request, spot_id):
    try:
        spot = ParkingSpot.objects.get(id=spot_id)
    except ParkingSpot.DoesNotExist:
        return Response({
            'success': False,
            'message': 'Парковочное место не найдено.',
        }, status=status.HTTP_404_NOT_FOUND)

    serializer = ParkingSpotStatusSerializer(
        spot,
        data=request.data,
        partial=True
    )

    if serializer.is_valid():
        serializer.save()

        return Response({
            'success': True,
            'message': 'Статус парковочного места успешно обновлен.',
            'data': ParkingSpotSerializer(spot).data,
        })

    return Response({
        'success': False,
        'message': 'Ошибка обновления статуса.',
        'errors': serializer.errors,
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def parking_statistics(request):
    total_count = ParkingSpot.objects.count()
    free_count = ParkingSpot.objects.filter(
        status=ParkingSpot.STATUS_FREE
    ).count()
    occupied_count = ParkingSpot.objects.filter(
        status=ParkingSpot.STATUS_OCCUPIED
    ).count()
    reserved_count = ParkingSpot.objects.filter(
        status=ParkingSpot.STATUS_RESERVED
    ).count()
    unavailable_count = ParkingSpot.objects.filter(
        status=ParkingSpot.STATUS_UNAVAILABLE
    ).count()

    return Response({
        'success': True,
        'data': {
            'total': total_count,
            'free': free_count,
            'occupied': occupied_count,
            'reserved': reserved_count,
            'unavailable': unavailable_count,
        }
    })