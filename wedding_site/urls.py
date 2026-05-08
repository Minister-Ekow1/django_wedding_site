from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [

    # ======================================================
    # AUTHENTICATION
    # ======================================================

    path(
        "accounts/login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html"
        ),
        name="login"
    ),

    path(
        "accounts/logout/",
        auth_views.LogoutView.as_view(),
        name="logout"
    ),

    # ======================================================
    # CUSTOM CMS ADMIN
    # ======================================================

    path(
        "cms/",
        include(
            ("custom_admin.urls", "custom_admin"),
            namespace="custom_admin"
        )
    ),

    # ======================================================
    # MAIN WEBSITE
    # ======================================================

    path(
        '',
        include('pages.urls')
    ),

    path(
        'memories/',
        include('memories.urls')
    ),

    path(
        'rsvp/',
        include('rsvp.urls')
    ),

    path(
        'program/',
        include('program.urls')
    ),

    path(
        'guestbook/',
        include('guestbook.urls')
    ),

]

# ==========================================================
# MEDIA FILES
# ==========================================================

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )