# Real-Time Analytics Pipeline

This project demonstrates a real-time analytics pipeline using Apache Kafka, Apache Spark Streaming on Amazon EMR, Amazon S3, Hive, and Amazon QuickSight.

Step-by-Step Guide to Setting Up the Project on GitHub
1. Create a GitHub Repository
Go to GitHub.
Click on the New button to create a new repository.
Name your repository (e.g., real-time-analytics-pipeline).
Add a description (optional).
Choose the repository type (public or private).
Initialize the repository with a README (optional).
Click on Create repository.

2. Clone the Repository Locally
Open your terminal and clone the repository to your local machine:

bash
Copy code
git clone git@github.com:Nikhil15gupta/real-time-analytics-pipeline.git
cd real-time-analytics-pipeline

3. Set Up Project Structure
Create the following directory structure:

## Project Structure
real-time-analytics-pipeline/
├── data_ingestion/
│   ├── kafka_producer.py
├── data_processing/
│   ├── spark_streaming.py
├── data_storage/
│   ├── hive_setup.sql
├── diagrams/
│   ├── pipeline_diagram.py
├── requirements.txt
└── README.md


Create a python venv and use that, this is important

The error ExecutableNotFound: failed to execute WindowsPath('dot'), make sure the Graphviz executables are on your systems' PATH indicates that the Graphviz executables are not available in your system's PATH. The diagrams library relies on Graphviz to generate diagrams, so you need to install Graphviz and add its executables to your system's PATH.

Step-by-Step Guide to Install Graphviz and Add to PATH
1. Download and Install Graphviz
Download Graphviz:

Go to the Graphviz download page.
Download the appropriate installer for your system.
Install Graphviz:

Run the installer and follow the installation instructions.
Take note of the installation directory (e.g., C:\Program Files\Graphviz\bin).
2. Add Graphviz to System PATH
Open System Properties:

Press Win + R, type sysdm.cpl, and press Enter.
Go to the Advanced tab and click on Environment Variables.
Edit PATH Variable:

Under System variables, find and select the Path variable, then click Edit.
Click New and add the path to the Graphviz bin directory (e.g., C:\Program Files\Graphviz\bin).
Apply and Close:

Click OK to close all dialogs and apply the changes.
3. Verify Installation
Open a New Command Prompt:

Open a new command prompt window (to ensure the new PATH is loaded).
Check Graphviz Installation:

Type dot -version and press Enter.
You should see the version information for Graphviz if it is correctly installed and added to the PATH.
4. Run the Diagram Script Again
After successfully installing Graphviz and adding it to the PATH, you can run your diagram script again.

bash
Copy code
python diagrams/pipeline_diagram.py

By following these steps, you should be able to resolve the ExecutableNotFound error and successfully generate the diagram using the diagrams library.

Diagrams:
https://diagrams.mingrammer.com/docs/getting-started/installation

![alt text](image.png)


Step-by-Step Setup of Kafka 3.7.1
Step 1: Download Kafka
Download Kafka 3.7.1:
bash
Copy code
wget https://downloads.apache.org/kafka/3.7.1/kafka_2.13-3.7.1.tgz
Step 2: Extract Kafka
Extract the downloaded tarball:
bash
Copy code
tar -xzf kafka_2.13-3.7.1.tgz
cd kafka_2.13-3.7.1
Step 3: Configure Kafka
Edit the server.properties file to set the advertised.listeners property:
bash
Copy code
sed -i 's|#advertised.listeners=PLAINTEXT://your.host.name:9092|advertised.listeners=PLAINTEXT://<ec2-public-ip>:9092|' config/server.properties
Step 4: Start Zookeeper and Kafka
Start Zookeeper:

bash
Copy code
bin/zookeeper-server-start.sh config/zookeeper.properties &
Start Kafka:

bash
Copy code
bin/kafka-server-start.sh config/server.properties &
Step 5: Create Kafka Topic
Create a Kafka topic for user activity:
bash
Copy code
bin/kafka-topics.sh --create --topic user-activity --bootstrap-server <ec2-public-ip>:9092 --partitions 3 --replication-factor 1
Example Commands
Download Kafka 3.7.1:

bash
Copy code
wget https://downloads.apache.org/kafka/3.7.1/kafka_2.13-3.7.1.tgz
Extract Kafka:

bash
Copy code
tar -xzf kafka_2.13-3.7.1.tgz
cd kafka_2.13-3.7.1
Configure Kafka:

bash
Copy code
sed -i 's|#advertised.listeners=PLAINTEXT://your.host.name:9092|advertised.listeners=PLAINTEXT://<ec2-public-ip>:9092|' config/server.properties
Start Zookeeper:

bash
Copy code
bin/zookeeper-server-start.sh config/zookeeper.properties &
Start Kafka:

bash
Copy code
bin/kafka-server-start.sh config/server.properties &
Create Kafka Topic:

bash
Copy code
bin/kafka-topics.sh --create --topic user-activity --bootstrap-server <ec2-public-ip>:9092 --partitions 3 --replication-factor 1
Summary
By following these steps, you will have Kafka 3.7.1 set up on your EC2 instance. This version includes a significant number of new features and fixes, and it is recommended to use the Scala 2.13 version unless you have specific requirements for Scala 2.12.
