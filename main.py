from dotenv import load_dotenv
import os
import pandas as pd
from llama_index.experimental.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str, context
from note_engine import note_engine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from pdf import usa_engine


# Load environment variables
load_dotenv()

# Retrieve the API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Load the data
population_path = os.path.join("data", "WorldPopulation2023.csv")
population_df = pd.read_csv(population_path)

# Initialize the query engine
population_query_engine = PandasQueryEngine(df=population_df, verbose=True, instruction_str=instruction_str)

population_query_engine.update_prompts({"pandas_prompt": new_prompt})

tools = [
    note_engine,
    QueryEngineTool(query_engine=population_query_engine, metadata=ToolMetadata(
        name="population_data",
        description="this gives information at the world population and demographics"
    )),
    QueryEngineTool(query_engine=usa_engine, metadata=ToolMetadata(
        name="merica_data",
        description="this gives information about Merica"
    )),
    
]

# Initialize OpenAI API client with the API key
llm = OpenAI(api_key=api_key, model="gpt-3.5-turbo-1106")

# Initialize ReActAgent with the tools and OpenAI client
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)

# Interactive prompt loop
while True:
    prompt = input("Enter a prompt (q to quit): ")
    if prompt == "q":
        break
    result = agent.query(prompt)
    print(result)

# Optionally, print the first few rows of the dataframe at the end
print('you bet brother:  ', population_df.head())
