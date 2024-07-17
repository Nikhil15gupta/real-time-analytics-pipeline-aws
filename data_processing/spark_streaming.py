from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, window, col
from pyspark.sql.types import StructType, StructField, StringType, TimestampType

# Initialize SparkSession with S3 configurations
spark = SparkSession.builder \
    .appName("UserActivityAnalytics") \
    .config("spark.hadoop.fs.s3a.endpoint", "s3.amazonaws.com") \
    .getOrCreate()

# Set log level to ERROR to reduce logging
spark.sparkContext.setLogLevel("ERROR")

# Kafka topic configuration
kafka_bootstrap_servers = "172.31.17.38:9092"
kafka_topic = "user-activity"

# Define the schema for the incoming data
user_activity_schema = StructType([
    StructField("event_time", TimestampType(), True),
    StructField("event_type", StringType(), True)
])

# Read streaming data from Kafka
user_activity_df = (
    spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", kafka_bootstrap_servers)
    .option("subscribe", kafka_topic)
    .option("startingOffsets", "latest")
    .load()
)

# Parse the JSON data and apply the schema
parsed_df = (
    user_activity_df.selectExpr("CAST(value AS STRING) as json")
    .select(from_json("json", user_activity_schema).alias("data"))
    .select("data.*")
)

# Add watermark to the data
user_activity_df_with_watermark = parsed_df \
    .withWatermark("event_time", "30 seconds")

# Aggregate the data in time windows
windowed_counts = (
    user_activity_df_with_watermark
    .groupBy(window(col("event_time"), "30 seconds", "30 seconds"), "event_type")
    .count()
)

# Write the stream to the console for debugging
query_console = (
    windowed_counts.writeStream
    .outputMode("append")
    .format("console")
    .option("truncate", "false")
    .option("checkpointLocation", "s3://real-time-analytics-processed/user-activity/checkpoints/console")
    .trigger(processingTime='30 seconds')
    .start()
)

# Write the aggregated data to S3 in JSON format
query_s3_json = (
    windowed_counts.writeStream
    .outputMode("append")
    .format("json")
    .option("checkpointLocation", "s3://real-time-analytics-processed/user-activity/checkpoints1/json")
    .option("path", "s3://real-time-analytics-processed/user-activity/output1/json")
    .option("header", "true")
    .trigger(processingTime='30 seconds')
    .start()
)

# Await termination
query_console.awaitTermination()
query_s3_json.awaitTermination()