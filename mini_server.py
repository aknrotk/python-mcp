from mcp.server.fastmcp import FastMCP

mcp = FastMCP("hello")


@mcp.tool()
async def hello_world(name: str) -> str:
    """
    指定された名前に対して挨拶を返します。

    Args:
        name (str): 挨拶する相手の名前

    Returns:claude_desktop_config.json
        str: "hello,名前" の形式の挨拶メッセージ
    """
    return f"hello,{name}"


if __name__ == "__main__":
    mcp.run(transport="stdio")
