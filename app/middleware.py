from .models import Visitor
import datetime

class VisitorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Kullanıcının IP adresini alma
        ip_address = request.META.get('REMOTE_ADDR')
        user_agent = request.META.get('HTTP_USER_AGENT', '<unknown>')
        if not request.session.session_key:
            request.session.save()
        session_key = request.session.session_key
        path = request.path

        # Ziyaretçiyi kaydet
        Visitor.objects.update_or_create(
            session_key=session_key,
            defaults={
                'ip_address': ip_address,
                'user_agent': user_agent,
                'path': path,
                'timestamp': datetime.datetime.now()
            }
        )
        
        response = self.get_response(request)
        return response