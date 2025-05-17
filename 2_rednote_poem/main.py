from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import TextMessageTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from config import model_client 
import asyncio


poem_agent = AssistantAgent(
    name="poem",
    model_client=model_client,
    system_message="你是一个诗人，擅长写诗和对联。",
    model_client_stream=True,  
)

rednote_agent = AssistantAgent(
    name="rednote",
    model_client=model_client,
    system_message="你是一个小红书达人，擅长把诗和对联变成小红书笔记。",
    model_client_stream=True,  
)

text_termination = TextMessageTermination("rednote")
team = RoundRobinGroupChat([poem_agent, rednote_agent], termination_condition=text_termination)


async def assistant_run() -> None:
    await Console(
        team.run_stream(
                task="写一首关于春天的诗",
            ),
            output_stats=True, 
    )


asyncio.run(assistant_run())

