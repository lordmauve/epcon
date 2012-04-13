# -*- coding: UTF-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('conference.views',
    url(r'^p/(?P<slug>[\w-]+)/?', 'user_profile', name='conference-profile'),
    url(r'^myself$', 'myself_profile', name='conference-myself-profile'),

    url(r'^speakers/(?P<slug>[\w-]+).xml', 'speaker_xml', name='conference-speaker-xml'),
    url(r'^speakers/(?P<slug>[\w-]+)', 'speaker', name='conference-speaker'),

    url(r'^talks/report', 'talk_report', name='conference-talk-report'),
    url(r'^talks/(?P<slug>[\w-]+)/video$', 'talk_video', name='conference-talk-video'),
    url(r'^talks/(?P<slug>[\w-]+)/video.mp4$', 'talk_video', name='conference-talk-video-mp4'),
    url(r'^talks/(?P<slug>[\w-]+).xml$', 'talk_xml', name='conference-talk-xml'),
    url(r'^talks/(?P<slug>[\w-]+)$', 'talk', name='conference-talk'),
    url(r'^talks/(?P<slug>[\w-]+)/preview$', 'talk_preview', name='conference-talk-preview'),

    url(r'^schedule/(?P<conference>.*)/(?P<slug>[\w-]+)/$', 'schedule', name='conference-schedule'),
    url(r'^schedule/(?P<conference>.*)/(?P<slug>[\w-]+).xml/?$', 'schedule_xml', name='conference-schedule-xml'),
    url(r'^schedule/(?P<conference>.*)/(?P<slug>[\w-]+)/(?P<eid>\d+)/$', 'schedule_event', name='conference-schedule-event'),
    url(r'^schedule/(?P<conference>.*)/(?P<slug>[\w-]+)/(?P<eid>\d+)/interest$', 'schedule_event_interest', name='conference-schedule-event-interest'),

    url(r'^places/', 'places', name='conference-places'),
    url(r'^sponsors/(?P<sponsor>.*)/', 'sponsor', name='conference-sponsor'),
    url(r'^paper-submission/$', 'paper_submission', name='conference-paper-submission'),
    url(r'^voting/$', 'voting', name='conference-voting'),

    url(r'^init.js$', 'init_js', name='conference-init.js'),

    url(r'^(?P<conference>[\w-]+).xml/$', 'conference_xml', name='conference-data-xml'),
)
