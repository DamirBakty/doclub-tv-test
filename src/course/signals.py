from django.db.models.signals import post_save
from django.dispatch import receiver
from course.models import ModuleCompletion, Certificate


@receiver(post_save, sender=ModuleCompletion)
def create_certificate(sender, instance, created, **kwargs):
    if instance.video_started and instance.file_downloaded and instance.test_completed:
        certificate_exists = hasattr(instance, 'certificate')
        if not certificate_exists:
            Certificate.objects.create(
                user=instance.user,
                module_completion=instance
            )
