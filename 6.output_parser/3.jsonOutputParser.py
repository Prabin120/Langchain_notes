from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        max_new_tokens=100
    )
)
model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()
template = PromptTemplate(
    template="Give me the name, age and city of a fictional person \n {instruction}",
    input_variables=[],
    partial_variables={'instruction': parser.get_format_instructions()}
)

# prompt = template.format()
# res = model.invoke(prompt)
# res = parser.parse(res.content)

# With chain
chain = template | model | parser
res = chain.invoke({})

print(res)