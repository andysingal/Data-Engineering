Pros and Cons of a Data Warehouse

Data warehouses act as a centralized repository for organizations to store all their data coming in from a multitude of sources, allowing data consumers such as analysts and BI engineers to access data easily and quickly from one single source to start their analysis. In addition, the technological components powering data warehouses enable accessing vast volumes of data while supporting workloads such as business intelligence to run on top of it.

Data warehouses act as a centralized repository for organizations to store data from multiple sources, enabling easy access for analysis by data consumers.
Data warehouses are limited to relational workloads and cannot handle machine learning-based tasks natively, requiring data to be moved to other platforms for advanced analytics.
Data warehouses support only structured data, limiting the ability to analyze semi-structured and unstructured data, which can provide valuable insights.
Data warehouses have tightly coupled technical components, leading to a closed form of data architecture and potential data lock-in issues.
Storing data in a data warehouse and using its compute engines can result in significant costs, especially with increasing workloads over time.
Organizations are seeking alternative data platforms like Data Lakes, allowing data to be stored in open file formats, reducing costs, and enabling parallel processing for BI and machine learning.

![11](https://github.com/andysingal/Data-Engineering/blob/main/Iceberg/images/Screenshot%202023-07-20%20at%2012.41.53%20PM.png)

Note that in data lakes, there isn’t really any service that fulfills the needs of the storage engine function. Generally the compute engine decides how to write the data, then the data is usually never revisited and optimized, unless rewriting entire tables or partitions which is usually done on an ad-hoc basis


Pros of a Data Lake:

Lower Cost: Storing data and executing queries on a data lake is more cost-effective compared to a data warehouse, allowing wider analytical reach.
Store Data in Open Formats: Data can be stored in any file format, providing more control over data and compatibility with various tools.
Handle Unstructured Data: Data lakes support unstructured data, making them suitable for analytics on such data types.
Cons of a Data Lake:

Performance: Decoupled components in a data lake may lead to performance issues, requiring significant engineering efforts to optimize.
Lack of ACID Guarantees: Data lakes may not offer ACID guarantees, affecting data consistency and integrity.
Lots of Configuration: Setting up and configuring a data lake with optimal performance and coupling requires significant input from data engineers, potentially adding to costs.


Enter Data Lakehouse
While using a data warehouse gave us performance and ease of use, analytics on data lakes gave us lower costs and reduced data drift from a complex web of data copies. The desire to thread the needle leads to great strides and innovation leading to what we now know as the data lakehouse.

What makes a data lakehouse truly unique are data lake table formats that eliminate all the previous issues with the Hive table format. You store the data in the same places you would with a data lake, you use the query engines you would use with a data lake, your data is stored in the same formats it would be on a data lake, what truly transforms your world from a “read only” data to a “center of my data world” data lakehouse is the table format (refer to Figure 1-4). Table formats enabled better consistency, performance and ACID guarantees when working with data directly on your data lake storage leading to several value propositions.

- Fewer Copies, Less Drift
With ACID guarantees and better performance you can now move workloads typically saved for the data warehouse like updates and other data manipulation. If you don’t have to move your data to the lakehouse you can have a more streamlined architecture with fewer copies. Fewer copies mean less storage costs, less compute costs from moving data to a data warehouse, and better governance of your data to maintain compliance with regulations and internal controls.

- Faster Queries, Fast Insights
The end goal is always to get business value from quality insights from our data, everything is else just steps to that end. If you can get faster queries that means you can get insights faster. Data Lakehouses enable faster performing queries by using optimizations at the query engine, table format and file format.

- Mistakes Don’t Have to Hurt
Data Lakehouse table formats enable the possibility to undo mistakes by using snapshot isolation, allowing you to revert the table back to prior snapshots. You can work with your data but not have to be up at night wondering if a mistake will lead to hours of auditing, repairing then backfilling.











<h1>The Hive Table Format</h1>
The Hive table format took the approach of defining a table as any and all files within a specified directory, the partitions of those tables would be the subdirectories.

These directory paths defining the table are tracked by a service called the Hive metastore which query engines can access to know where to find the data applicable to their query.


Figure 1-6. The architecture of a table stored using the Hive table format
The Hive table format had several benefits:

It enabled more efficient query patterns than full table scans, so techniques like partitioning and bucketing made it possible to avoid scanning every file for faster queries

It was file format agnostic so it allowed the data community overtime to develop better file formats like Apache Parquet and use them in their Hive tables and did not require transformation prior to making the data available in a Hive table (e.g., Avro, CSV/TSV).

Through atomic swaps of the listed directory in the hive metastore, you can make all or nothing (atomic) changes to an individual partition in the table.

Over time this became the de facto standard working with most data tools and providing a uniform answer to “what data is in this table?”.

While these benefits were significant there were also many limitations that become apparent as time passed:

File level changes are inefficient since there was no mechanism to atomically swap a file in the same way the Hive Metastore could be used to swap a partition directory. You are essentially left making swaps at the partition level to update a single file atomically.

While you could atomically swap a partition there wasn’t a mechanism for atomically updating multiple partitions as one transaction. This opens up the possibility for end users seeing inconsistent data between transactions updating multiple partitions.

There really aren’t good mechanisms to enable concurrent simultaneous updates, especially with tools beyond Hive itself.

An engine listing files and directories was time consuming and slowed down queries. Having to read and list files and directories that may not need scanning in the resulting query comes at a cost.

Partition columns were often derived from other columns, such as deriving a month column from a timestamp. Partitioning only helped if you filtered by the partition column, and someone who has a filter on the timestamp column may not intuitively know to also filter on the derived month column leading to a full table scan since partitioning was not taken advantage of.

Table statistics would be gathered through asynchronous jobs resulting in often state table statistics if any statistics were available at all, making it difficult for query engines to further optimize queries.

Since object storage often throttles requests against the same prefix (think of an object storage prefix as analogous to a file directory), queries on tables with large numbers of files in a single partition (so all the files would be in one prefix) can have performance issues.

The larger the scale of the datasets and use cases, the more these problems would be amplified resulting in significant pain in need of a new solution, so newer table formats were created.



<h2>What Problems Do Modern Table Formats Solve?</h2>
Modern table formats all aim to bring a core set of major benefits over the Hive table format:

Modern table formats allowed for ACID transactions which are safe transactions that either complete in full or are canceled. In legacy formats like the Hive table format, many transactions could not have these guarantees.

Enable safe transactions when there are multiple writers. If two or more writers write to a table, there is a mechanism to make sure the writer that completes their write second is aware and considers what the other writer(s) have done to keep the data consistent.

Better collection of table statistics and metadata that can allow a query engine scanning the data to plan more efficiently.

While most modern table formats provide the above, the Apache Iceberg format provides these and solves many of the other problems with the Hive table format.



<h1>How Did Apache Iceberg Come to Be?</h1>
Netflix in the creation of what became the Apache Iceberg format came to a conclusion that many of the problems with the Hive Format stemmed from one simple but fundamental flaw. That flaw is that each table is tracked as directories and subdirectories limiting the granularity that is necessary to provide consistency guarantees, better concurrency and more.

With this in mind netflix set out to create a new table format with several goals in mind:

Consistency
If updates to a table occur over multiple transactions, it is possible for end users to experience inconsistency in the data they are viewing. An update to a table across multiple partitions should be done fast and atomically so data is consistent to end users. They either see the data before the update or after the update and nothing in between.

Performance
With Hive’s file/directory listing bottleneck, query planning would take excessively long to complete before actually executing the query. The table should provide metadata and avoid excessive file listing so not only can query planning can be quicker but the resulting plans can also be executed faster since they scan only the files necessary to satisfy the query.

Easy to Use
To get the benefits of techniques like partitioning, end users should not have to be aware of the physical structure of the table. The table should be able to give users the benefits of partitioning based on naturally intuitive queries and not depend on filtering extra partition columns derived from a column they are already filtering by (like filtering by a month column when you’ve already filtered the timestamp it is derived from).

Evolvability
Updating schemas of Hive tables could result in unsafe transactions and updating how a table is partitioned would result in a need to rewrite the entire table. A table should be able to evolve its schema and partitioning scheme safely and without rewriting the table.

Scalability
All the above should be able to be accomplished at the petabyte scale of Netflix’s data.



**** So they began creating the Iceberg format which focuses on defining tables as a canonical list of files instead of tracking a table as a list of directories and subdirectories.

The Apache Iceberg project is a specification, a standard of how metadata defining a data lakehouse table should be written across several files. To support the adoption of this standard Apache Iceberg has many support libraries to help individuals work with the format or for compute engines to implement support. Along with these libraries, the project has created implementations for open source compute engines like Apache Spark and Apache Flink.

![12](https://github.com/andysingal/Data-Engineering/blob/main/Images/Screenshot%202023-07-20%20at%201.32.30%20PM.png)

![13]
