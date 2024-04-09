"""
@authors Alexander Fisher & Jonathan Salem
@version Barbell Version 1.2

@about Defines URL routing for the 'gym_project' Django project, mapping URL paths to views. 
       This configuration determines how URLs are processed by the application.

        *Django Administration Site:
            - '/admin/' path is reserved for the admin site, providing an interface for site administrators.

        *Application URL Inclusion:
            - The root URL ('') includes URLs from the 'gym_app' application, delegating URL management to the app level.
            - The '/accounts/' path includes URLs from 'django-allauth', handling user authentication and registration.

        *Error Handling:
            - 'handler404' and 'handler500' specify custom views to handle 404 Not Found and 500 Internal Server Error 
              responses, enhancing the user experience during errors.

        *Static and Media Files (Development Only):
            - In debug mode, Django serves media files uploaded by users through the built-in development server.
              This is helpful for testing purposes but is not intended for use in production environments.

        *Security Note:
            - It's important to note that serving static and media files directly from Django is inefficient and potentially insecure for production use.
              In a production setting, these files should be served by a dedicated web server (e.g., Nginx) for improved performance and security.

        *Including Other URL Configurations:
            - The 'include()' function allows for modular URL configuration, 
              enabling the inclusion of URL patterns from other applications or third-party packages.
              This approach promotes separation of concerns and reusability across the project.

"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

handler404 = 'gym_app.views.custom_page_not_found_view'
handler500 = 'gym_app.views.custom_internal_server_error_view'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gym_app.urls')),
    #path('auth/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# This will enable Django to serve media files in debug mode, 
# for profile pictures in the development environment. 
# Note that this setup is suitable for development, not for production. 
# For production, need to serve the static files through the web server 
# (in our case we're gonna use Nginx)