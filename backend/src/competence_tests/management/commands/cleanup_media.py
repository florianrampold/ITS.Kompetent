from django.core.management.base import BaseCommand
import os
from django.conf import settings
from competence_tests.models import ImageItem 

class Command(BaseCommand):
    help = 'Removes files from the media folder that are no longer referenced in the database.'

    def handle(self, *args, **options):
        media_root = settings.MEDIA_ROOT
        files_deleted = 0
        for subdir, dirs, files in os.walk(media_root):
            for file in files:
                file_path = os.path.join(subdir, file)
                relative_path = os.path.relpath(file_path, media_root)
                if not ImageItem.objects.filter(image_field=relative_path).exists():
                    os.remove(file_path)
                    files_deleted += 1
                    self.stdout.write(self.style.SUCCESS(f'Deleted orphaned media file: {relative_path}'))
        self.stdout.write(self.style.SUCCESS(f'Total files deleted: {files_deleted}'))
