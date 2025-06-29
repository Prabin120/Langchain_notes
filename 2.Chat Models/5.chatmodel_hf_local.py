from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint, HuggingFacePipeline


llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        max_new_tokens=100
    )
)
model = ChatHuggingFace(llm=llm)
res = model.invoke("What is the capital of India?")

print(res.content)