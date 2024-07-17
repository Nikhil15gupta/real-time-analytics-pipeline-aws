CREATE EXTERNAL TABLE user_activity (
    user_id STRING,
    event_type STRING,
    timestamp TIMESTAMP,
    page STRING
)
STORED AS PARQUET
LOCATION 's3://bucket-name/user-activity/raw';

CREATE EXTERNAL TABLE user_activity_metrics (
    window STRUCT<start: TIMESTAMP, end: TIMESTAMP>,
    event_type STRING,
    count INT
)
STORED AS PARQUET
LOCATION 's3://bucket-name/user-activity/metrics';
