from splink import  splink_datasets
from splink.exploratory import completeness_chart
from splink import DuckDBAPI

df = splink_datasets.fake_1000
df = df.drop(columns=["cluster"])
# print(df.head(5))

db_api = DuckDBAPI()
completeness_chart(df, db_api=db_api).show()
