from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.template.loader import render_to_string
from django.http import HttpResponse
#import weasyprint
from django.conf import settings
from myapp.models import *
from .serializers import *

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FirmViewSet(viewsets.ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class MatterViewSet(viewsets.ModelViewSet):
    queryset = Matter.objects.all()
    serializer_class = MatterSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class TimeEntryViewSet(viewsets.ModelViewSet):
    queryset = TimeEntry.objects.all()
    serializer_class = TimeEntrySerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    @action(detail=True, methods=['get'])
    def pdf(self, request, pk=None):
        invoice = self.get_object()
        html = render_to_string('invoices/invoice.html', {'invoice': invoice})
        # If you need static assets, supply base_url pointing to MEDIA or STATIC root
        #pdf_file = weasyprint.HTML(string=html).write_pdf()
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename=invoice_{invoice.pk}.pdf'
        return response

class InvoiceItemViewSet(viewsets.ModelViewSet):
    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class ActivityLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ActivityLog.objects.all().order_by('-timestamp')
    serializer_class = ActivityLogSerializer


@require_POST
def session_login(request):
    """
    Session-based login.
    CSRF is enforced automatically.
    """
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(
        request,
        username=username,
        password=password
    )

    if user is None:
        return JsonResponse(
            {'error': 'Invalid username or password'},
            status=401
        )

    login(request, user)
    return JsonResponse({'success': True})


@login_required
def dashboard(request):
    return JsonResponse({
        'message': 'You are logged in',
        'user': request.user.username
    })


def session_logout(request):
    logout(request)
    return JsonResponse({'success': True})

