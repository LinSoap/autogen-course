from autogen_agentchat.agents import AssistantAgent,UserProxyAgent
from autogen_agentchat.conditions import MaxMessageTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from config import model_client 
import asyncio
import json
import os



user = UserProxyAgent("user", input_func=input) 

assistant = AssistantAgent(
    name="assistant",
    model_client=model_client,
    system_message="你叫Lucy，你是一个温柔善良的女孩,你只会记得你说过的事情 /no_think",
)


termination = MaxMessageTermination(max_messages=8)

team = RoundRobinGroupChat([user, assistant], termination_condition=termination)

async def assistant_run() -> None:
    if os.path.exists("4_50_first_dates/team_state.json"):
        with open("4_50_first_dates/team_state.json", "r") as f:
            team_state = json.load(f)
        await team.load_state(team_state)

    await Console(
        team.run_stream(),
            output_stats=True, 
    )

    team_state = await team.save_state()

    with open("4_50_first_dates/team_state.json", "w") as f:
        json.dump(team_state, f)

asyncio.run(assistant_run())



