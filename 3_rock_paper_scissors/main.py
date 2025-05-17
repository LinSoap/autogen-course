from autogen_agentchat.agents import AssistantAgent,UserProxyAgent
from autogen_agentchat.conditions import TextMessageTermination,SourceMatchTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from config import model_client 
import asyncio

from typing import Literal
from pydantic import BaseModel


class PlayerResponse(BaseModel):
    response: Literal["石头", "剪刀", "布"]

class JudgetResponse(BaseModel):
    response: Literal["平局", "player1胜利", "player2胜利", "警告"]

player1 = UserProxyAgent("player1", input_func=input) 

player2 = AssistantAgent(
    name="player2",
    model_client=model_client,
    system_message="你就是玩家遇到的那个高手，但你其实是一个石头剪刀布的菜鸡，你总是能输给用户。你只能说，石头，剪刀，布 /no_think",
    output_content_type=PlayerResponse,
)

judger = AssistantAgent(
    name="judger",
    model_client=model_client,
    system_message="现在player1和2正在进行一场石头剪刀布决斗，你是一名公平的裁判，你会根据玩家的出拳来判断胜负，直接了当的判断，如果有人出了非石头剪刀布的内容，则警告 /no_think",
    model_client_stream=True,  
    output_content_type=JudgetResponse,
)

termination = SourceMatchTermination("judger")
team = RoundRobinGroupChat([player1, player2,judger], termination_condition=termination)

async def assistant_run() -> None:
    await Console(
        team.run_stream(
                task="糟糕，我遇到了石头剪刀布高手，我要出什么才能赢？",
            ),
            output_stats=True, 
    )


asyncio.run(assistant_run())


