from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import *
from .views import session_login, session_logout, dashboard

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('firms', FirmViewSet)
router.register('clients', ClientViewSet)
router.register('matters', MatterViewSet)
router.register('documents', DocumentViewSet)
router.register('time-entries', TimeEntryViewSet)
router.register('invoices', InvoiceViewSet)
router.register('invoice-items', InvoiceItemViewSet)
router.register('payments', PaymentViewSet)
router.register('tasks', TaskViewSet)
router.register('notes', NoteViewSet)
router.register('events', EventViewSet)
router.register('messages', MessageViewSet)
router.register('notifications', NotificationViewSet)
router.register('activity-logs', ActivityLogViewSet)

urlpatterns = router.urls
urlpatterns += [
    path('api/login/', session_login, name='session_login'),
    path('api/logout/', session_logout, name='session_logout'),
    path('api/dashboard/', dashboard, name='dashboard'),
]
