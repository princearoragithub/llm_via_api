from llm_connector import get_llm_response

# Test with Ollama's deepseek-r1:8b model
response = get_llm_response(
    provider="ollama",
    prompt="""You are a content creator on twitter who is participating in a gmtribe campaign. Details of the campaign are given below in <campaign> tags. You will have the input from the user about the content in <user_input> tags. The tone of the required messaging will be in the <tone> tags. 
Please write a tweet incorporating all these details.

<campaign>
How to Participate

Tweet what you built at Starkware x Realms World Agent Hackathon.
Use images, video, selfie recording to optimise your impact. Keep videos between 30 seconds to 1 minute long.
tag @StarkWareLtd and @LootRealms in your tweet.
Campaign Details

Tweet what you built at Starkware x Realms World Agent Hackathon, and get visibility on your project along with some $STRK rewards./n/n All you need to do is tweet what you are building and tag @StarkWareLtd and @LootRealms.
</campaign>

<user_input>
I have built an onchain game of poker where a player can play against other players or AI. I have also built the AI agents, using eliza, that play the game. It is a turn based game and uses core realms functionalities like to provide a web2 experience.
</user_input>

<tone>
Be friendly, considerate as well as competitive so that you can win the campaign.
</tone>""",
    model="deepseek-r1:8b",
    temperature=0.7  # Higher temperature for creative tasks
)

print(f"Generated Tweet:\n{response}") 