"""
Provides storage classes that separate static and user uploaded media in S3
"""

from storages.backends.s3boto import S3BotoStorage

class StaticRootS3BotoStorage(S3BotoStorage):
    location = 'static'


class MediaRootS3BotoStorage(S3BotoStorage):
    location = 'media'
