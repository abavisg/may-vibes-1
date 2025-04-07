import requests
import logging
import os
from dotenv import load_dotenv
from typing import Dict, List, Tuple, Any
from .base_agent import BaseAgent
import random

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LTDCheckerAgent(BaseAgent):
    """
    Agent responsible for checking UK Companies House LTD name conflicts
    """
    
    def __init__(self):
        """
        Initialize the LTD checker agent
        """
        super().__init__("LTDChecker")
        # Load environment variables
        load_dotenv()
        self.api_key = os.getenv("COMPANIES_HOUSE_API_KEY")
        self.base_url = "https://api.companieshouse.gov.uk"
        self.mock_enabled = os.getenv("MOCK_LTD_CHECKS", "false").lower() == "true"
        
        if not self.api_key:
            logger.error("No Companies House API key found in environment variables")
    
    def _get_mock_ltd_availability(self, name):
        """Generate mock LTD availability data"""
        return {
            "ltd_available": random.choice([True, False]),
            "similar_companies": [
                {"name": f"{name} Ltd", "number": f"{random.randint(10000000, 99999999)}"} 
                for _ in range(random.randint(0, 3))
            ] if random.choice([True, False]) else []
        }

    def execute(self, request):
        try:
            names = request.get("names", [])
            if not names:
                return {"error": "No names provided"}

            results = {}
            for name in names:
                if self.mock_enabled:
                    results[name] = self._get_mock_ltd_availability(name)
                else:
                    if not self.api_key:
                        return {"error": "Companies House API key is required"}
                    
                    # Real API implementation here
                    # ... existing code ...

            return {"ltd_results": results}
        except Exception as e:
            logging.error(f"Exception checking LTD: {str(e)}")
            return {"error": str(e)}
    
    def check_ltd_conflict(self, name: str) -> bool:
        """
        Check if a name conflicts with existing LTD companies.
        
        Args:
            name: The name to check
            
        Returns:
            Boolean indicating if the name is available
            
        Raises:
            ValueError: If the Companies House API key is not configured
        """
        if not self.api_key:
            raise ValueError("Companies House API key is required but not configured. Please add COMPANIES_HOUSE_API_KEY to your .env file.")
        
        try:
            # Make API request to Companies House
            response = requests.get(
                f"{self.base_url}/company-profile/search",
                params={"q": name},
                auth=(self.api_key, "")
            )
            
            if response.status_code == 200:
                data = response.json()
                total_results = data.get("total_results", 0)
                
                # If there are no results, the name is available
                return total_results == 0
            else:
                logger.error(f"Error checking LTD name {name}: {response.status_code}")
                raise Exception(f"Companies House API error: {response.status_code}")
                
        except Exception as e:
            logger.error(f"Exception checking LTD name {name}: {str(e)}")
            raise
    
    def filter_available_names(self, names: List[str]) -> Dict[str, Dict[str, bool]]:
        """
        Filter a list of names and return their LTD availability status.
        
        Args:
            names: List of names to check
            
        Returns:
            Dictionary mapping names to their LTD availability status
            
        Raises:
            ValueError: If the Companies House API key is not configured
        """
        if not self.api_key:
            raise ValueError("Companies House API key is required but not configured. Please add COMPANIES_HOUSE_API_KEY to your .env file.")
            
        results = {}
        for name in names:
            is_available = self.check_ltd_conflict(name)
            results[name] = {"ltd_available": is_available}
        return results

# Create a singleton instance
ltd_checker_agent = LTDCheckerAgent()
