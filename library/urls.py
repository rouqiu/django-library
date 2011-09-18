from django.conf.urls.defaults import patterns, include, url
from library.models import *
from django.views.generic import DetailView, ListView

urlpatterns = patterns('library.views',

  url(r'^admin/library/loan/$', 'lateLoans'),

  url(r'^$', 'booksBy'),
  url(r'^bk$', 'booksBy'),

  url(r'^bk/(?P<pk>\d+)/$',
    DetailView.as_view(
      model=Book,
      template_name='library/book.html')),


  url(r'^bk/(?P<args>.+)/$', 'booksBy'),
)
