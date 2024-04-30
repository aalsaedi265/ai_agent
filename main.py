
from dotenv import load_dotenv
import os
import pandas as pd
from llama_index.experimental.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str
load_dotenv()

# Load the data
population_path = os.path.join("data", "WorldPopulation2023.csv")
population_df = pd.read_csv(population_path)

# Initialize the query engine
population_query_engine = PandasQueryEngine(df=population_df, verbose=True, instruction_str=instruction_str)

# Use the query engine to make a query
result = population_query_engine.query('what is the population of usa')

# Output the result and show the first few rows of the dataframe
print('you bet brother:  ', population_df.head())
