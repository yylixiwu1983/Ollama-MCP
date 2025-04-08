from praisonaiagents import Agent, MCP

search_agent = Agent(
    instructions="""You help book apartments on Airbnb.""",
    llm="ollama/llama3.2:3b",
    tools=MCP("npx -y @openbnb/mcp-server-airbnb --ignore-robots-txt")
)

search_agent.start("Search for Apartments in Paris for 2 nights. 04/10/25-04/12/25")
# 需要美国BPG，启用tune模式，清除系统代理，绕过大陆



