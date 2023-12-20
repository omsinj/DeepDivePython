from tabulate import tabulate

data = [
    ["Hadoop", "- Hadoop Distributed File System (HDFS)\n- MapReduce programming model\n- YARN for resource management", 
     "- Scalability: Can handle large-scale data processing.\n- Fault tolerance: Can recover from node failures.\n- Cost-effective: Uses commodity hardware.", 
     "- Latency: Designed for batch processing, not suitable for low-latency processing.\n- Complexity: Steeper learning curve for MapReduce programming.\n- Overhead: Disk-based storage and processing can result in slower performance for certain use cases."],
    
    ["Spark", "- Resilient Distributed Datasets (RDD)\n- Spark Core, Spark SQL, Spark Streaming, MLlib, GraphX for various processing needs\n- Spark's in-memory processing engine", 
     "- Speed: In-memory processing provides faster data processing compared to Hadoop MapReduce.\n- Ease of use: Supports multiple programming languages (Java, Scala, Python).\n- Versatility: Offers libraries for batch processing, SQL queries, machine learning, and graph processing.", 
     "- Complexity: Learning curve for Spark programming.\n- Resource consumption: Requires more memory compared to Hadoop MapReduce.\n- Limited fault tolerance: Spark's RDD lineage information may not be sufficient for recovering lost data in some cases."],
    
    ["Storm", "- Nimbus for job coordination\n- ZooKeeper for distributed coordination\n- Spouts and bolts for data processing", 
     "- Low latency: Designed for real-time stream processing with low latency.\n- Scalability: Can scale horizontally to handle large amounts of streaming data.\n- Fault tolerance: Resilient to node failures with configurable levels of durability.", 
     "- Complexity: Learning curve for real-time stream processing concepts.\n- Limited support for batch processing compared to Hadoop/Spark.\n- Lack of high-level abstractions, making development more code-intensive."],
    
    ["Flink", "- DataStream API for stream processing\n- DataSet API for batch processing\n- Flink Runtime for execution\n- Flink Gelly for graph processing\n- Flink ML for machine learning", 
     "- Unified processing: Supports both batch and stream processing in a single framework.\n- Event time processing: Supports processing based on event timestamps for accurate results in event-driven applications.\n- Fault tolerance: Provides exactly-once semantics and stateful processing with high fault tolerance.", 
     "- Learning curve: Complexity in mastering both batch and stream processing concepts.\n- Resource utilization: Requires sufficient memory for optimal performance.\n- Community size: Smaller compared to Hadoop and Spark."],
    
    ["Samza", "- Job coordinator for distributed processing\n- Stream processors for data processing\n- Stateful processing with storage backend", 
     "- Fault tolerance: Supports fault-tolerant processing with stateful recovery.\n- Scalability: Scales horizontally to handle large amounts of data.\n- Extensibility: Supports pluggable components for integration with other systems.", 
     "- Limited processing models: Primarily designed for stateful stream processing.\n- Learning curve: Requires understanding of distributed systems concepts.\n- Community size: Smaller compared to Hadoop and Spark."]
]

headers = ["Framework", "Key Components", "Advantages", "Disadvantages"]

table = tabulate(data, headers, tablefmt="grid")
print(table)
