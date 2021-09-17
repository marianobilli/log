# trigger pyspark from aws cli

```
aws emr add-steps --cluster-id j-31VQ6K309CYS3 --steps Type=CUSTOM_JAR,Name="maxExecutorsTestMB",ActionOnFailure=CONTINUE,Jar=s3://eu-west-1.elasticmapreduce/libs/script-runner/script-runner.jar,Args=['/usr/lib/spark/bin/spark-submit','--master','yarn','--deploy-mode','cluster','--conf','spark.dynamicAllocation.maxExecutors=40','--conf','spark.pyspark.python=python3','--conf','spark.pyspark.python.opts=','--conf','spark.pyspark.driver.python=python3','--num-executors','20','s3://my-bucket/test.py']
```
