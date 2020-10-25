import bleach
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.utils.html import mark_safe
from markdown import markdown
from backends.storage_backends import PrivateMediaStorage

ALLOWED_TAGS = [
    'a',
    'abbr',
    'acronym',
    'b',
    'blockquote',
    'br',
    'code',
    'em',
    'i',
    'li',
    'ol',
    'strong',
    'ul',
    'p',
    'table',
    'tbody',
    'thead',
    'tr',
    'td',
    'th',
    'div',
    'span',
    'hr',
    'h1',
    'h2',
    'h3',
    'h4',
    'h5',
    'h6',
    'pre',
    'int:pk',
    'module'
    '>'
    # Update doc/user/markdown.rst if you change this!
]

ALLOWED_ATTRIBUTES = {
    'a': ['href', 'title', 'class'],
    'abbr': ['title'],
    'acronym': ['title'],
    'table': ['width'],
    'td': ['width', 'align'],
    'div': ['class'],
    'p': ['class'],
    'span': ['class', 'title'],
}

ALLOWED_PROTOCOLS = ['http', 'https', 'mailto', 'tel']


class Media(models.Model):
    secure_file = models.CharField(null=True, max_length=512)
    key = models.CharField(max_length=512, null=True)

    class Meta:
        abstract = True

    @staticmethod
    def create_presigned_url(bucket_name, object_name, expiration=3600):
        """Generate a presigned URL to share an S3 object

        :param bucket_name: string
        :param object_name: string
        :param expiration: Time in seconds for the presigned URL to remain valid
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
            response = s3_client.generate_presigned_url(
                "get_object",
                Params={"Bucket": bucket_name, "Key": object_name},
                ExpiresIn=expiration,
            )
        except ClientError as e:
            logging.error(e)
            return None

        # The response contains the presigned URL
        return response


class AWSImage(models.Model):
    file = models.FileField(storage=PrivateMediaStorage())
    key = models.CharField(max_length=128, null=True)
    url = models.URLField(null=True)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return f"Title: {self.title}"

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_message_as_markdown(self):
        return self.content
        # return bleach.clean(
        #     self.content,
        #     tags=ALLOWED_TAGS,
        #     attributes=ALLOWED_ATTRIBUTES,
        #     protocols=ALLOWED_PROTOCOLS,
        # )


class ViewingRecord(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    source = models.GenericIPAddressField()
