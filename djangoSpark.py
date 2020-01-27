from django.shortcuts import render
from pyspark.sql import SparkSession
from django.http import JsonResponse
from django.http import HttpResponse
# Create your views here.

def df_view(request):
    spark = SparkSession.builder.appName("Python Spark SQL basic example").config("spark.some.config.option", "some-value").getOrCreate()
    df_object=spark.read.load("/SampleXML/abc.csv", format="csv", sep=",", inferSchema="true", header="true")
    #rdd=df.toJSON().collect()
    #return JsonResponse(rdd)
    return HttpResponse(df_object.toJSON().collect(), content_type="application/json")

	https://isgbdstorageg2.blob.core.windows.net/isgdatalake/masters%2Fcf_values.csv
