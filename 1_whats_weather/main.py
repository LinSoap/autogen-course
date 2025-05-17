from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
from autogen_core import CancellationToken
from autogen_agentchat.ui import Console
from config import model_client 
import asyncio


async def get_weather(city: str) -> str:
    """Get the weather for a given city."""
    return f" {city} 的天气是晴天，气温 25°C。" 


agent = AssistantAgent(
    name="weather_agent",
    model_client=model_client,
    tools=[get_weather],
    system_message="你是一个有用的助手，擅长回答天气相关的问题。",
    model_client_stream=True,  
)


async def assistant_run() -> None:
    await Console(
        agent.on_messages_stream(
                [TextMessage(content="北京现在什么天气", source="user")],
                cancellation_token=CancellationToken(),
            ),
            output_stats=True,  # Enable stats printing.
    )


# Use asyncio.run(assistant_run()) when running in a script.
# await assistant_run()
asyncio.run(assistant_run())
