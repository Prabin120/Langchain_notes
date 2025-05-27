from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4", temperature=0.3, max_completion_tokens=50)

# temperature is a parameter that controls  the randomness of the language model's output. It affects how creative and deterministic the response are:
# Lower values (0.0 - 0.3) -> model detemistic and predictable (can expect same output for same prompt)
# 0.3 - 0.7 -> Balanced
# Higher values (0.7 - 1.5) -> More random, creative and diverse. 

res = model.invoke("What is the capital of india")

print(res.content)

