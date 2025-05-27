from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        max_new_tokens=100
    )
)

model = ChatHuggingFace(llm=llm)

# 1st promt -> Detailed report
template1 = PromptTemplate(
    template="Write a detail report on {topic}",
    input_variables=['topic']
)

# 2nd promt -> summary
template2 = PromptTemplate(
    template="Write a 5 line summary on the following text. /n {text}",
    input_variables=['text']
)

prompt1 = template1.invoke({"topic":"black hole"}) 

res1 = model.invoke(prompt1)

prompt2 = template2.invoke({"text":res1.content}) 

res2 = model.invoke(prompt2)

print(res2.content)
