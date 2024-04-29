
This is proj to make person ai assistant all code here is users to use how you see fit
I will be using RETRIEVAL augmented generation (RAG) so it can work with new data and and trained data

also the agent can take notes on content it has access too

will see the thinking process of the model before result it provided


#WILL use LLAMAINDEX because making models injest data is very tough this free service will allow us to only focus on the functionality and not making sure data is being injested properly 

pandas reads csv file
pypdf reads pdf file
llama for setting the agent (behind the scenes magic)
python-dotenv for loading secret env files to use


#NOTES 

py -m venv aiAgent
.\aiAgent\Scripts\activate

pip3 install llama-index pypdf python-dotenv pandas