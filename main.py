
from dotenv import load_dotenv
import os
import pandas as pd
from llama_index.experimental.query_engine import PandasQueryEngine
load_dotenv()

popultion_path = os.path.join("data", "WorldPopulation2023.csv")
population_df = pd.read_csv(popultion_path)

#verbose show how conclusion was made
population_query_engine = PandasQueryEngine(df= population_df, verbose=True )

print('you bet brother:  ', population_df.head())