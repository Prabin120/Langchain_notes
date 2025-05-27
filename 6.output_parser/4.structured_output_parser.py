from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic'),
    ResponseSchema(name='fact_4', description='Fact 4 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give 4 facts about {topic}\n {format_instructuction}',
    input_variables=['topic'],
    partial_variables={'format_instructuction':parser.get_format_instructions()}
)

# prompt = template.invoke({'topic':"black hole"})

# res = model.invoke(prompt)
# res = parser.parse(res.content)
chain = template | model | parser

res = chain.invoke({'topic': "black hole"})

print(res)