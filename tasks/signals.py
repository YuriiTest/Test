from tasks.models import SignalLogEntry


def signal_logger(sender, **kwargs):
    if sender._meta.object_name == 'SignalLogEntry' or sender._meta.object_name == 'Migration':
        return
    action = 'DELETE'
    if 'created' in kwargs:
        action = 'CREATE OR UPDATE'
    SignalLogEntry.objects.create(
        model=sender._meta.object_name,
        action=action
    )