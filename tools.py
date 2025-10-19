from crewai_tools import (
    DirectoryReadTool,
    FileReadTool,
    SerperDevTool,
    WebsiteSearchTool
)
import os
from dotenv import load_dotenv

load_dotenv()

# ✅ Ensure SERPER_API_KEY is set correctly
serper_key = os.getenv("SERPER_API_KEY")
if serper_key:
    os.environ["SERPER_API_KEY"] = serper_key
    search_tool = SerperDevTool()
else:
    print("⚠️ SERPER_API_KEY not found — search tool disabled.")
    search_tool = None

file_read_tool = FileReadTool()
directory_read_tool = DirectoryReadTool()
if search_tool is None:
    from crewai_tools import WebsiteSearchTool
    search_tool = WebsiteSearchTool()