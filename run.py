from splink import  splink_datasets
from splink.exploratory import completeness_chart, profile_columns
from splink import DuckDBAPI
import altair as alt


alt.renderers.enable('browser')

df = splink_datasets.fake_1000
df = df.drop(columns=["cluster"])
# print(df.head(5))

db_api = DuckDBAPI()

completeness_chart(df, db_api=db_api).show()
profile_columns(df, db_api=DuckDBAPI(), top_n=10, bottom_n=5).show()