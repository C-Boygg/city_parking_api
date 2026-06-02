from django.db import models


class ParkingSpot(models.Model):
    STATUS_FREE = 'free'
    STATUS_OCCUPIED = 'occupied'
    STATUS_RESERVED = 'reserved'
    STATUS_UNAVAILABLE = 'unavailable'

    STATUS_CHOICES = [
        (STATUS_FREE, 'Свободно'),
        (STATUS_OCCUPIED, 'Занято'),
        (STATUS_RESERVED, 'Зарезервировано'),
        (STATUS_UNAVAILABLE, 'Недоступно'),
    ]

    TYPE_REGULAR = 'regular'
    TYPE_DISABLED = 'disabled'
    TYPE_ELECTRIC = 'electric'

    TYPE_CHOICES = [
        (TYPE_REGULAR, 'Обычное'),
        (TYPE_DISABLED, 'Для инвалидов'),
        (TYPE_ELECTRIC, 'Для электромобилей'),
    ]

    number = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='Номер парковочного места'
    )
    zone = models.CharField(
        max_length=100,
        verbose_name='Парковочная зона'
    )
    address = models.CharField(
        max_length=255,
        verbose_name='Адрес'
    )
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        verbose_name='Широта'
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        verbose_name='Долгота'
    )
    spot_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default=TYPE_REGULAR,
        verbose_name='Тип места'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_FREE,
        verbose_name='Статус'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Время последнего обновления'
    )

    class Meta:
        verbose_name = 'Парковочное место'
        verbose_name_plural = 'Парковочные места'
        ordering = ['zone', 'number']

    def __str__(self):
        return f'{self.zone} - {self.number} ({self.status})'