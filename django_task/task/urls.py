from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to

urlpatterns = patterns('task.views',
        (r'^$', redirect_to, {'url': '/pending/'}),
        (r'^pending/$', 'pending_tasks'),
        (r'^completed/$', 'completed_tasks'),
        (r'^add/task/$', 'add_task'),
        (r'^add/tags/$', 'add_tag'),
        (r'^add/project/$', 'add_project'),
        (r'^done/(?P<task_id>\d+)/$', 'done_task'),
        (r'^edit/task/(?P<task_id>\d+)/$', 'edit_task'),
        (r'^detail/task/(?P<task_id>\d+)/$', 'detail_task'),
        (r'^detail/project/(?P<proj_id>\d+)/$', 'detail_project'),
        (r'^taskdb/(?P<filename>.*)$', 'taskdb')
        )
