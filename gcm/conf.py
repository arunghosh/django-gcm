from django.conf import settings

GCM_DEVICE_MODEL = getattr(settings, 'GCM_DEVICE_MODEL', 'gcm.models.Device')

GCM_APIKEY = getattr(settings, 'GCM_APIKEY', None)
