from rest_framework import serializers

from .models import ParkingSpot


class ParkingSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSpot
        fields = [
            'id',
            'number',
            'zone',
            'address',
            'latitude',
            'longitude',
            'spot_type',
            'status',
            'updated_at',
        ]
        read_only_fields = ['id', 'updated_at']

    def validate_number(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                'Номер парковочного места не может быть пустым.'
            )

        if len(value.strip()) < 2:
            raise serializers.ValidationError(
                'Номер парковочного места должен содержать минимум 2 символа.'
            )

        return value.strip().upper()

    def validate_zone(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                'Название парковочной зоны не может быть пустым.'
            )

        return value.strip()

    def validate_address(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                'Адрес парковочного места не может быть пустым.'
            )

        return value.strip()

    def validate_latitude(self, value):
        if value < -90 or value > 90:
            raise serializers.ValidationError(
                'Широта должна находиться в диапазоне от -90 до 90.'
            )

        return value

    def validate_longitude(self, value):
        if value < -180 or value > 180:
            raise serializers.ValidationError(
                'Долгота должна находиться в диапазоне от -180 до 180.'
            )

        return value

    def validate(self, data):
        spot_type = data.get('spot_type')
        status = data.get('status')

        if spot_type == ParkingSpot.TYPE_DISABLED and status == ParkingSpot.STATUS_UNAVAILABLE:
            raise serializers.ValidationError(
                'Место для инвалидов нельзя сразу создавать со статусом "недоступно".'
            )

        return data


class ParkingSpotStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSpot
        fields = ['status']

    def validate_status(self, value):
        allowed_statuses = [
            ParkingSpot.STATUS_FREE,
            ParkingSpot.STATUS_OCCUPIED,
            ParkingSpot.STATUS_RESERVED,
            ParkingSpot.STATUS_UNAVAILABLE,
        ]

        if value not in allowed_statuses:
            raise serializers.ValidationError(
                'Недопустимый статус парковочного места.'
            )

        return value