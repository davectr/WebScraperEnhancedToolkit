from typing import Type, Optional
from pydantic import BaseModel, Field
from superagi.helper.webpage_extractor import WebpageExtractor, StructuredDataExtractor
from superagi.llms.base_llm import BaseLlm
from superagi.tools.base_tool import BaseTool

class WebScraperSchema(BaseModel):
    website_url: str = Field(
        ...,
        description="Valid website URL without any quotes.",
    )
    content_limit: int = Field(
        600,
        description="Limit for the content length to extract. Default is 600 words.",
    )

class WebScraperEnhancedTool(BaseTool):
    """
    Web Scraper Enhanced Tool

    An enhanced version of the Web Scraper tool, designed for better handling of structured data
    and providing more detailed content extraction with configurable limits.
    """

    llm: Optional[BaseLlm] = None
    name = "WebScraperEnhancedTool"
    description = "Enhanced tool to scrape website URLs and extract text content with structured data handling."
    args_schema: Type[WebScraperSchema] = WebScraperSchema

    class Config:
        arbitrary_types_allowed = True

    def _execute(self, website_url: str, content_limit: int = 600) -> str:
        """
        Execute the Web Scraper Enhanced tool.

        Args:
            website_url : The website URL to scrape.
            content_limit : Limit for the content length to extract.

        Returns:
            The text content of the website within the specified limit.
        """
        try:
            # Use StructuredDataExtractor for structured data like tables
            structured_content = StructuredDataExtractor().extract(website_url)
            if structured_content:
                return structured_content
            
            # If no structured data, extract regular text content
            content = WebpageExtractor().extract_with_bs4(website_url)
            max_length = len(' '.join(content.split(" ")[:content_limit]))
            return content[:max_length]
        except Exception as e:
            # Add more specific exception handling as needed
            return f"An error occurred during web scraping: {str(e)}"

# Consider instantiating WebpageExtractor once if it's a heavy class
webpage_extractor = WebpageExtractor()
