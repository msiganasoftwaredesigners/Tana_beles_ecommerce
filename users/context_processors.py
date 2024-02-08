def social_links(request):
    if request.user.is_authenticated and request.user.is_staff:
        return {
            'facebook_url': request.user.facebook_url,
            'telegram_url': request.user.telegram_url,
            'whatsapp_url': request.user.whatsapp_url,
        }
    return {}