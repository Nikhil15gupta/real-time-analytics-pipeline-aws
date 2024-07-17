import os
from diagrams import Diagram, Cluster
from diagrams.aws.analytics import EMR, Quicksight
from diagrams.aws.storage import S3
from diagrams.onprem.queue import Kafka

# Add Graphviz bin directory to the PATH
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'

with Diagram("Real-Time Analytics Pipeline", show=False):
    webapp = Kafka("User Activity Data")
    
    with Cluster("Amazon EMR"):
        emr = EMR("EMR Cluster")
    
    with Cluster("Data Storage"):
        s3_raw = S3("Raw Data")
        s3_processed = S3("Processed Data")
    
    with Cluster("Data Visualization"):
        quicksight = Quicksight("Dashboard")
    
    webapp >> emr >> s3_raw
    emr >> s3_processed >> quicksight