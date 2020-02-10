from django.core.exceptions import ValidationError


def latitude(value):
    if not (-90 <= value <= 90):
        raise ValidationError('%f is not a valid latitude, latitude should be between -90 and +90' % value)


def longitude(value):
    if not (-180 <= value <= 180):
        raise ValidationError('%f is not a valid longitude, longitude should be between -180 and +180' % value)


def grade(value):
    if not (0 <= value <= 20):
        raise ValidationError('%f is not a valid grade, grade should be between 0 and 20' % value)


def year(value):
    if not (1000 <= value <= 9999):
        raise ValidationError('%f is not a valid year, year should be 4 digits' % value)

