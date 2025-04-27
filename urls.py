# from django.contrib import admin
# from django.urls import path
# from django.urls import include
# from django.urls import settings
# from django.conf.urls.static import static
# from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
#     path('accounts/', include('accounts.urls', namespace='accounts')),
#     path('reservas/', include('reservas.urls', namespace='reservas')),
#     path('pages/', include('pages.urls', namespace='pages')),
#     path('', include('pages.urls', namespace='pages')),
#     path('ckeditor/', include('ckeditor_uploader.urls')),
#     path('', TemplateView.as_view(template_name='home.html'), name='home'),
#     path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)