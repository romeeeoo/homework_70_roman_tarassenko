from datetime import datetime, timedelta

from django.db.models import Q

from todo_app.models import Task

# 1
month = timedelta(days=30)
last_month = datetime.today() - month
print(last_month)
last_month_done = Task.objects.filter(status__name="Done", updated_at__gte=last_month)
print(f"Last moth done:{last_month_done}")
# 2
qs_1 = Task.objects.filter(Q(status__name__exact="In Process") | Q(status__name__exact="New"))
qs_2 = Task.objects.filter(Q(types__name__exact="Enhancement") | Q(types__name__exact="Bug"))
tasks_2 = (qs_1 & qs_2).distinct()
print(f"tasks: {tasks_2}")
# 3
qs_3 = Task.objects.filter(summary__icontains="bug", )
qs_4 = Task.objects.filter(types__name__exact="Bug")
qs_5 = (qs_3 | qs_4).distinct()
qs_6 = qs_5.exclude(status__name__exact="Done")
print(f"actual bugs{qs_6}")
