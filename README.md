# Serverless Data Processing Pipeline on AWS

## Project Description
This project demonstrates the design and implementation of a foundational serverless data pipeline leveraging AWS services to automatically process and store incoming data. It showcases how to build a scalable, cost-effective, and low-maintenance data ingestion solution.

## Architecture Diagram
[Insert your architecture diagram here. You can upload an image (e.g., `architecture.png`) to your repo and link it like: `![Architecture Diagram](images/architecture.png)`]

## Technologies Used
- **AWS Services:** Amazon S3, AWS Lambda, Amazon DynamoDB, AWS Identity and Access Management (IAM), Amazon CloudWatch
- **Programming Language:** Python

## Key Features / How It Works
- **Automated Ingestion:** Data files (e.g., `sample_data.csv`) uploaded to a designated S3 bucket automatically trigger the pipeline.
- **Serverless Processing:** An AWS Lambda function is invoked to read, process, and transform the incoming data.
- **NoSQL Data Storage:** Processed data is securely stored in a NoSQL table in Amazon DynamoDB.
- **Secure Permissions:** Configured AWS IAM roles and policies ensure least-privilege access across all services involved.
- **Monitoring & Logging:** Integrated with Amazon CloudWatch for real-time monitoring of pipeline performance, resource utilization, and logging of Lambda executions.

## Setup and Deployment
This project can be deployed using the provided AWS CloudFormation template (`pipeline-template.yml`).

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/aws-serverless-data-pipeline.git](https://github.com/yourusername/aws-serverless-data-pipeline.git)
    cd aws-serverless-data-pipeline
    ```
2.  **Deploy via CloudFormation:**
    ```bash
    aws cloudformation deploy --template-file pipeline-template.yml --stack-name DataPipelineDemo --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM
    ```
    (Make sure you have the AWS CLI configured with appropriate permissions.)
3.  **Test the pipeline:** Upload `sample_data.csv` to the S3 bucket created by the CloudFormation stack.
    (You can use `aws s3 cp sample_data.csv s3://your-pipeline-s3-bucket-name/` to upload.)

## Key Learnings & Challenges
- Gained hands-on experience designing and implementing end-to-end serverless architectures.
- Deepened understanding of AWS IAM best practices for secure cross-service communication.
- Learned to effectively monitor serverless applications using CloudWatch metrics, logs, and alarms.
- Explored strategies for handling potential Lambda cold starts and optimizing execution efficiency.
- Practiced deploying and managing complex AWS infrastructure using Infrastructure as Code (IaC) with CloudFormation.

## Files in This Repository
- `lambda_function.py`: The Python code for the AWS Lambda function.
- `pipeline-template.yml`: AWS CloudFormation template for deploying the pipeline resources.
- `sample_data.csv`: Example input data for testing the pipeline.