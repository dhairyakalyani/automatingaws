import boto3
import click

session = boto3.Session(profile_name='pythonautomation')
s3 = session.resource('s3')

@click.group()
def cli():
    "Webotron deploys websites to AWS"
    pass

@cli.command('list-buckets')
def list_buckets():
    "List all S3 buckets"
    for bucket in s3.buckets.all():
        print (bucket.name)

@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    "List all onjects in S3 bucket"
    for obj in s3.Bucket(bucket).objects.all():
        print(obj)


if __name__=="__main__":
    cli()
