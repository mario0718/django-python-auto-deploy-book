from rightadmin.models import Action


def fake_action_data():
    Action.objects.all().delete()
    print('delete all action data')
    Action.objects.create(name="CREATE", aid=1)
    Action.objects.create(name="XCHANGE", aid=2)
    Action.objects.create(name="DEPLOY", aid=3)
    print('create action action data')
