# Cloud Resume Challenge — Backend

Visitor counter service for the resume site, built as part of the [Cloud Resume Challenge](https://cloudresumechallenge.dev/).

Frontend: [crc-front](https://github.com/mahdiboukhadra/crc-front)

## What it does

`visitsUpdater` is a Python AWS Lambda function that increments and returns a visitor count on each page load. The count is stored in DynamoDB, with the Lambda function handling the read/increment/write logic. The function is invoked via API Gateway, called directly from the frontend.

## Architecture

- **Compute:** AWS Lambda (Python)
- **Storage:** DynamoDB — stores and persists the visit count
- **API:** Exposed via API Gateway, called from the frontend on page load
- **IAM:** Scoped IAM role/permissions for Lambda to read/write to DynamoDB

## Notes

Originally deployed alongside the frontend on AWS; domain has since expired but the service code here reflects the working implementation.
