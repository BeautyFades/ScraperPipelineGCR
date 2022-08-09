import os
from google.cloud import secretmanager

ENVIRONMENT = 'dev-local' # Either dev-local, dev-cloudrun or prd-cloudrun.
DESTINATION_BUCKET_NAME = 'economia-webscraper'
DESTINATION_PATH = 'bcb-selic'