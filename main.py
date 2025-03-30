import json
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool 

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

llm = ChatOpenAI(model="gpt-4o-2024-08-06")
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant. Your task is to answer user queries and use necessary tools.
            You will be provided with a list of tools and their descriptions. Use them wisely to gather information.
            Always provide a summary of your findings and list the tools you used.
            Wrap the output in this format and provide no other text\n{format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

tools = [search_tool, wiki_tool, save_tool]
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
query = input("Enter your research query: ")
raw_response = agent_executor.invoke({"query": query})

try:
    # Extract and clean the output
    output_text = raw_response.get("output", "")

    # Remove triple backticks if present
    if output_text.startswith("```json"):
        output_text = output_text.strip("```json").strip("```")

    # Parse JSON safely
    structured_response = json.loads(output_text)
    structured_response = ResearchResponse(**structured_response)  # Validate with Pydantic model

    print(structured_response)
except Exception as e:
    print(f"Error parsing response: {e}, Raw Response: {raw_response}")
