# Webscraping on the Cloud

## Required Infrastructure
This folder corresponds to the **SCRAPER** part of the pipeline, which is the first step. The required infrastructure for running this service is a destination bucket on GCP. You will need to pass the *DESTINATION_BUCKET_NAME* and *DESTINATION_PATH* parameters as configuration in ```config.py```, alongside changing the *ENVIRONMENT* manually and also potentially providing a *keyfile.json* to run locally (see the [local](#locally-with-docker) versus [GCR](#deploying-to-google-cloud-run) deployment sections).

### Architecture (NEEDS UPDATE)
![Architecture](https://i.imgur.com/uLg3Jir.png)

## Deployment cases
### Locally with Docker
When deployed to GCR, the environment variable _GOOGLE_APPLICATION_CREDENTIALS_ is set automatically, so in order to deploy locally you must have a valid GCP credentials file with enough permissions inside the Docker container for it to be referenced. You must also confirm that in the _config.py_ you have the environment set to ```dev```. The step by step guide is as follows:

1. Make sure that the environment variable _GOOGLE_APPLICATION_CREDENTIALS_ is going to be set corrently by placing the GCP Service Account credentials file (e.g. ```keyfile.json```) together with the other files in the *scraper* folder (along with the Dockerfile, app.py, etc.). It is going to be copied to the container and be referenced in the code to access GCS, BigQuery, Secret Manager and other GCP services. You must also make sure it has enough permissions for the resources it is going to access;
2. Make sure to set the *ENVIRONMENT* variable in ```config.py``` to ```dev```;
3. ```cd``` to the *scraper* folder and run ```docker build -t <IMAGE_NAME> .```, such as ```docker build -t scraper .```;
4. Execute ```docker run -p 8000:8080 <IMAGE_NAME>```, such as ```docker run -p 8000:8080 scraper```;
5. Access the Flask routes by going to ```http://127.0.0.1:8000/<route_name>```.

### Deploying to Google Cloud Run
To deploy to the Cloud Run service, there's no need to set credentials since the environment variable is set automatically (see [here!](https://cloud.google.com/run/docs/configuring/service-accounts#:~:text=By%20default%2C%20Cloud%20Run%20services,most%20minimal%20set%20of%20permissions.)).
1. ```cd``` into the *scraper* folder.
2. Make sure you're logged into your GCloud project and run ```gcloud builds submit --tag gcr.io/<PROJECT_ID>/<IMAGE_NAME> .```. This will build the container using Cloud Build.
3. Deploy to Cloud Run using ```gcloud beta run deploy <GCR_INSTANCE_NAME> --image gcr.io/<PROJECT_ID>/<IMAGE_NAME> --region southamerica-east1 --platform managed --allow-unauthenticated --quiet```. Be aware of the _allow-unauthenticated_ flag: anyone can access the endpoint as it is deployed at the moment.
