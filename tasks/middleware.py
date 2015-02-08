from tasks.models import Middleware


class RequestsMiddleware:
    """Middleware that stores http requests"""
    def process_request(self, request):
            Middleware.objects.create(
                method=request.method,
                http_referer=request.META.get('HTTP_REFERER', ''),
                path=request.path,
                files=request.FILES.get('photo', '')
            )