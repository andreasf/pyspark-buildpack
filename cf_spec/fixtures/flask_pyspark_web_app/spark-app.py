import os
import sys

from flask import Flask
from pyspark import SparkConf
from pyspark.sql import SparkSession

app = Flask(__name__)

conf = SparkConf()
conf.set("spark.executor.memory", "256mb")
conf.set("spark.cores.max", "1")

spark_session = SparkSession.builder.config(conf=conf).getOrCreate()
spark_context = spark_session.sparkContext

@app.route("/")
def hello():
    data = spark_context.parallelize(["i", "am", "a", "string", "that", "was", "sent", "to", "spark", "and", "back"])

    return str(data.collect())

@app.route("/version")
def version():
    return sys.version

def get_port():
    port = os.getenv("PORT")
    
    if type(port) == str:
        return port
    
    return 8080

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=get_port())
