# Scraper Pipeline
Monorepository for a brazilian economy indicator webscraper pipeline. This application encompasses data web scraping, data cleaning and disponibilization in three major steps with three different containerized applications:

- **SCRAPER:** A Flask application that listens for HTTP requests to trigger a Selenium-based webscraper that accesses a website, scrapes a table, converts it to .parquet and uploads it to a *landing zone* bucket in Google Cloud Storage. Finally, the application will trigger the next service, a data cleaning pipeline. 

- OPTIONAL **CLEANER/UPDATER:** A second Flask application that listens for HTTP requests from the **SCRAPER** (or manually via manual HTTP requests) to trigger a data cleaning pipeline, downloading the .parquet file from the *landing zone* and manipulating it according to business case rules, reinserts the processed .parquet file into a *gold zone* folder inside the GCS bucket and also requests a PostgreSQL database to update its contents to match the newly scraped and cleansed data. As for improvements for this implementation, there could be multiple cleaning services for different data tiers (the usual bronze/silver/gold architecture), or, if the pipeline is small enough, the transformations and cleaning can be done by the scraper itself, as it is implemented at the moment

- **REST API:** A third Flask application that queries said PostgreSQL database, parses the results and returns a RFC 7159 compliant JSON object containing said data. This could be a public API endpoint where you might share all the cool stuff you scrape, or even quite the contrary, being a secure API that feeds sensitive or otherwise critical information to another internal service.

It is up to the developer to decide how to secure all the Flask HTTP endpoints. The current implementation has no security whatsoever and all endpoints are unauthenticated and exposed, given a user knows the URL for the Cloud Run instances.
