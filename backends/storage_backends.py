import boto3
import logging

# noinspection PyPackageRequirements
from storages.backends.s3boto3 import S3Boto3Storage
from botocore.exceptions import ClientError
from django.conf import settings


class PrivateMediaStorage(S3Boto3Storage):
    location = "private"
    default_acl = "private"
    file_overwrite = False
    custom_domain = False
    querystring_auth = True

    def url(self, name, parameters=None, expire=3600):
        """Generate a presigned URL to share an S3 object

        :param name: string. Name of object key
        :param expire: Time in seconds for the presigned URL to remain valid
        :param parameters: dict of params
        :return: Presigned URL as string. If error, returns None.
        """

        # Generate a presigned URL for the S3 object
        session = boto3.session.Session(region_name=settings.AWS_S3_REGION_NAME)
        s3_client = session.client(
            "s3",
            config=boto3.session.Config(signature_version="s3v4"),
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        )
        try:
            url = s3_client.generate_presigned_url(
                "get_object", Params={"Bucket": self.bucket_name, "Key": name}, ExpiresIn=expire,
            )
        except ClientError as e:
            logging.error(e)
            return None

        if self.querystring_auth:
            return url
        return self._strip_signing_parameters(url)
