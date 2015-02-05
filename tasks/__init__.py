from django.db.models.signals import post_save, post_delete
from JBS.signals import signal_logger

post_save.connect(signal_logger)
post_delete.connect(signal_logger)