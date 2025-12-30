from dotenv import load_dotenv
load_dotenv()

import os

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langchain.agents import create_agent

from langchain_core.messages import AIMessage


def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    if provider=='Groq':
        llm=ChatGroq(model=llm_id)
    elif provider=='OpenAI':
        llm=ChatOpenAI(model=llm_id)
    else:
        raise ValueError("Invalid provider")
    tools = [TavilySearch(max_results=2)] if allow_search else []
    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=system_prompt
    )

    state={'messages':query}
    response = agent.invoke(state)
    messages=response.get('messages')
    ai_messages=[message.content for message in messages if isinstance(message, AIMessage)]
    return ai_messages[-1]