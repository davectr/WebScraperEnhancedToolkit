from typing import List
from superagi.tools.base_tool import BaseTool, BaseToolkit, ToolConfiguration

class WebScraperEnhancedToolkit(BaseToolkit):
    """
    Web Scraper Enhanced Toolkit

    This toolkit is an enhanced version of the original Web Scraper Toolkit,
    designed to handle structured data like tables more effectively and provide
    more detailed content extraction.
    """

    name: str = "Web Scraper Enhanced Toolkit"
    description: str = "Enhanced Web Scraper toolkit for structured data extraction."

    def get_tools(self) -> List[BaseTool]:
        return [
            WebScraperEnhancedTool(),
        ]

    def get_env_keys(self) -> List[ToolConfiguration]:
        # Update with necessary environment configurations if any
        return []
