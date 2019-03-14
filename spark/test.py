from pyspark.ml.regression import LinearRegression
from pyspark.sql import SparkSession

sc=SparkSession.builder.appName("tradingSessiondomain").getOrCreate() 

data= sc.read.csv("WDM_trades.csv", inferSchema=True, header=True)
data.show()

print("---------DONE-----------")




