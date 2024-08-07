import os

AIRFLOW_HOME = os.environ["AIRFLOW_HOME"]

spark_confs = {
    "hive.metastore.uris": "thrift://hive:9083",
    "spark.hadoop.datanucleus.autoCreateTables": True,
    "spark.hadoop.datanucleus.schema.autoCreateTables": True,
    "spark.hadoop.datanucleus.fixedDatastore": False,
    "spark.driver.userClassPathFirst": True,
    "spark.sql.extensions": "io.delta.sql.DeltaSparkSessionExtension",
    "spark.sql.catalog.spark_catalog": "org.apache.spark.sql.delta.catalog.DeltaCatalog",
    "spark.sql.hive.metastore.warehouse.dir": "s3a://warehouse",
    "spark.hadoop.fs.s3a.access.key": "admin",
    "spark.hadoop.fs.s3a.secret.key": "admin1234",
    "spark.hadoop.fs.s3a.endpoint": "http://minio:9000",
    "spark.hadoop.fs.s3a.path.style.access": True,
    "spark.hadoop.fs.s3a.connection.ssl.enabled": False,
    "spark.hadoop.fs.s3a.impl": "org.apache.hadoop.fs.s3a.S3AFileSystem"
}
