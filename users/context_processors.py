from django.conf import settings
from django.contrib.auth.models import User
from .models import Avatar

def avatar_in_context(request):
    if request.user.is_authenticated:
        try:
            avatar = Avatar.objects.get(user=request.user)
            avatar_url = f"{settings.MEDIA_URL}{avatar.imagen}"
        except Avatar.DoesNotExist:
            avatar_url = None
    else:
        avatar_url = None

    return {'avatar_url': avatar_url}
