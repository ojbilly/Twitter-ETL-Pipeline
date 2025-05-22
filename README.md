# Twitter ETL Pipeline with Airflow, Tweepy & AWS S3

This project implements a lightweight ETL (Extract, Transform, Load) pipeline to collect tweets from a specific Twitter user using the Twitter API v2, process and transform the data, and store the output in an Amazon S3 bucket.

It uses **Apache Airflow** for orchestration, **Tweepy** for interacting with the Twitter API, and runs securely on an **AWS EC2 instance**.

---

## Key Features

* Daily scheduled ETL via Apache Airflow DAG
* Tweet extraction using Tweepy and the Twitter API
* Data transformation into structured format with Pandas
* Secure credentials handled via environment variables
* Cloud storage of results to AWS S3
* Hosted on EC2 with optional background Airflow service (nohup)

---

## Features

* Extracts tweets using the Twitter API (v2) via Tweepy
* Automatically runs daily using Apache Airflow
* Parses tweet content, creation date, and public metrics
* Converts raw tweets into a refined CSV file
* Uploads the cleaned data to Amazon S3
* Can be deployed and run from an EC2 instance
* Uses Airflow DAGs to manage and schedule the pipeline
* Secure environment variable handling (no hardcoded secrets)
* Retry logic and task management for reliability
* Modular structure for easy maintenance and scalability

---

## Technologies Used

* Python 3.12
* Apache Airflow 3.x
* Tweepy
* Pandas
* Amazon S3
* Amazon EC2
* s3fs
* Flask AppBuilder (Airflow UI)
* Linux (Ubuntu 22.04 LTS)

---

## Project Structure

```bash
twitter_pipeline/
├── twitter_etl.py           # Python script to extract and process tweets
├── twitter_dags.py          # Airflow DAG that schedules and runs the ETL
├── refined_tweets.csv       # Example output (if run locally)
├── airflow_ec2_key.pem      # EC2 key file (should be gitignored)
└── venv/                    # Virtual environment (should be gitignored)
```

---

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/twitter_etl_pipeline.git
   cd twitter_etl_pipeline
   ```

2. **Create virtual environment and activate:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   .\venv\Scripts\activate  # Windows
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Export Twitter credentials as environment variable:**

   ```bash
   export TWITTER_BEARER_TOKEN='your_token_here'  # Linux/Mac
   set TWITTER_BEARER_TOKEN='your_token_here'     # Windows
   ```

5. **Start Airflow locally:**

   ```bash
   airflow db init
   airflow standalone
   ```

---

## Deployment on EC2

* Use a t2.micro or t3.medium instance running Ubuntu 22.04
* Clone your GitHub repo into EC2
* Set up Python virtual environment and install Airflow
* Use `nohup airflow standalone > airflow.log 2>&1 &` to run in background
* Open port 8080 on your EC2 security group to access the Airflow UI
* Ensure your `.pem` file is **never committed to GitHub** and stored securely

---

## Security Considerations

* Never expose your Twitter credentials or AWS keys in code
* Use environment variables or secret managers (like AWS Secrets Manager)
* Add `.env`, `.pem`, and `venv/` to your `.gitignore`
* Regularly rotate keys and tokens
* Restrict EC2 access via security groups (only open required ports)

---

## Author

**Osaze Opene**
Data Engineer | Cloud Enthusiast
GitHub: (https://github.com/ojbilly)

---

## License

This project is licensed by Osaze Omoruyi.
