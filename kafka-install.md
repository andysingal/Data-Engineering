Apache Kafka Installation Guide - Getting Started with Kafka | Article
Apache Kafka is a popular distributed streaming platform that is widely used for building real-time data pipelines and streaming applications. In this article, we will provide a comprehensive guide on how to install Apache Kafka on your local machine, allowing you to get started with Kafka and explore its powerful features.

Step 1: Prerequisites:
Before we begin the installation process, there are a few prerequisites that need to be fulfilled:

Java Development Kit (JDK): Apache Kafka requires Java to run. Ensure that you have JDK version 8 or higher installed on your system.

Step 2: Downloading Apache Kafka:
To download Apache Kafka, follow these steps:

Visit the Apache Kafka website (https://kafka.apache.org/downloads) and navigate to the downloads page.

Choose the desired Kafka version that suits your requirements (e.g., the latest stable release).

Select the binary download option for the Scala version you prefer.

Once you have chosen the download, click on the mirror link to begin the download.

Step 3: Extracting Kafka:
After downloading Kafka, follow these steps to extract it:
```
Locate the downloaded Kafka file on your local machine (e.g., kafka_2.13-3.4.0.tgz).
```
Open a terminal or command prompt and navigate to the directory where the Kafka file is located.

Use the appropriate command to extract the Kafka file. For example, if you're using Linux or macOS, use the following command:
```
tar -xzf kafka_2.13-3.4.0.tgz
```
Step 4: Starting ZooKeeper:
Kafka relies on ZooKeeper for managing its cluster and maintaining coordination among its nodes. To start ZooKeeper, follow these steps:

Open a terminal or command prompt.

Navigate to the Kafka directory:
```
cd kafka_2.13-3.4.0

```
Start ZooKeeper by executing the following command:
```

bin/zookeeper-server-start.sh config/zookeeper.properties
```
Step 5: Starting Kafka:
With ZooKeeper running, we can now start Kafka. Follow these steps:

Open a new terminal or command prompt.

Navigate to the Kafka directory:
```
cd kafka_2.13-3.4.0
Start Kafka by executing the following command:

bin/kafka-server-start.sh config/server.properties
```
Step 6: Verifying the Installation:
To verify that Kafka has been successfully installed and is running, follow these steps:

Open a new terminal or command prompt.

Navigate to the Kafka directory:
```
cd kafka_2.13-3.4.0
Create a test topic by executing the following command:

bin/kafka-topics.sh --create --topic test-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```
Verify that the topic has been created by executing the following command:
```
bin/kafka-topics.sh --list --bootstrap-server localhost:9092
```
If the test topic is listed, it indicates that Kafka has been installed and is running correctly on your local machine.
