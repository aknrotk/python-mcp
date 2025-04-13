import asyncio

from mcp import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client


async def test_hello_world_from_mini_server():
    server_parameters = StdioServerParameters(
        command="python",
        args=["mini_server.py"],
    )

    async with stdio_client(server_parameters) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            result = await session.call_tool("hello_world", {"name": "MCP"})
            print("Tool result:", result.content)


async def test_get_forecast_from_weather():
    server_parameters = StdioServerParameters(
        command="python",
        args=["weather.py"],
        # args=["mini_server.py"],
    )

    async with stdio_client(server_parameters) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            result = await session.call_tool("get_weather_alerts", {"state": "CA"})
            print("Tool result:", result.content)


if __name__ == "__main__":
    asyncio.run(test_get_forecast_from_weather())
