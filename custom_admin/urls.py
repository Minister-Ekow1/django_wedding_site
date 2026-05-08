from django.urls import path
from . import views

app_name = "custom_admin"

urlpatterns = [

    # ======================================================
    # DASHBOARD
    # ======================================================

    path(
        '',
        views.dashboard,
        name='admin_dashboard',
    ),

    # ======================================================
    # ABOUT
    # ======================================================

    path(
        'about/',
        views.about_manage,
        name='about_manage',
    ),

    # ======================================================
    # ABOUT IMAGES
    # ======================================================

    path(
        'about/images/',
        views.about_images,
        name='about_images',
    ),

    path(
        'about/images/add/',
        views.about_image_add,
        name='about_image_add',
    ),

    path(
        'about/images/edit/<int:id>/',
        views.about_image_edit,
        name='about_image_edit',
    ),

    path(
        'about/images/delete/<int:id>/',
        views.about_image_delete,
        name='about_image_delete',
    ),

    # ======================================================
    # VENUE
    # ======================================================

    path(
        'venue/',
        views.venue_manage,
        name='venue_manage',
    ),

    # ======================================================
    # LOVE STORY
    # ======================================================

    path(
        'love-story/',
        views.love_story_manage,
        name='love_story_manage',
    ),

    path(
        'love-story/add/',
        views.love_story_add,
        name='love_story_add',
    ),

    path(
        'love-story/edit/<int:id>/',
        views.love_story_edit,
        name='love_story_edit',
    ),

    path(
        'love-story/delete/<int:id>/',
        views.love_story_delete,
        name='love_story_delete',
    ),

    # ======================================================
    # PROGRAM
    # ======================================================

    path(
        'program/',
        views.program_manage,
        name='program_manage',
    ),

    path(
        'program/add/',
        views.program_add,
        name='program_add',
    ),

    path(
        'program/edit/<int:id>/',
        views.program_edit,
        name='program_edit',
    ),

    path(
        'program/delete/<int:id>/',
        views.program_delete,
        name='program_delete',
    ),

    # ======================================================
    # RSVP
    # ======================================================

    path(
        'rsvp/',
        views.rsvp_manage,
        name='rsvp_manage',
    ),

    path(
        'rsvp/<int:id>/',
        views.rsvp_detail,
        name='rsvp_detail',
    ),

    # ======================================================
    # GUESTBOOK
    # ======================================================

    path(
        'guestbook/',
        views.guestbook_manage,
        name='guestbook_manage',
    ),

    path(
        'guestbook/approve/<int:id>/',
        views.guestbook_approve,
        name='guestbook_approve',
    ),

    path(
        'guestbook/delete/<int:id>/',
        views.guestbook_delete,
        name='guestbook_delete',
    ),

    # ======================================================
    # MEMORIES
    # ======================================================

    path(
        'memories/',
        views.memories_manage,
        name='memories_manage',
    ),

    path(
        'memories/view/<int:id>/',
        views.memory_detail,
        name='memory_detail',
    ),

    path(
        'memories/approve/<int:id>/',
        views.memory_approve,
        name='memory_approve',
    ),

    path(
        'memories/delete/<int:id>/',
        views.memory_delete,
        name='memory_delete',
    ),

    # ======================================================
    # SITE SETTINGS
    # ======================================================

    path(
        'settings/',
        views.site_settings_manage,
        name='site_settings_manage',
    ),

]