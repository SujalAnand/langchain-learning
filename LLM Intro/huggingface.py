#install huggingface module
#pip3 install -U huggingface_hub
#pip3 install -U openai
#pip3 install -U langchain
#pip3 install -U langchain-community
#pip3 install -U langchain-huggingface
#from langchain-huggingface.llms import HuggingFaceHub
#from langchain-huggingface.llms import HuggingFaceHub
from langchain.llms import HuggingFaceHub
import os

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
llm = HuggingFaceHub(repo_id="google/flan-t5-large")
our_query = "what is the currency of India"
llm = llm(our_query)
print("Currency is " + llm)