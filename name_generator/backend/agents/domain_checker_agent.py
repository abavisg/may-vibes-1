import os
import logging
import requests
from typing import Dict, List, Tuple, Any
from dotenv import load_dotenv
from .base_agent import BaseAgent
import random

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DomainChecker:
    """Class to check domain availability using the Domainr API."""
    
    def __init__(self):
        """Initialize the DomainChecker with API key from environment variables."""
        load_dotenv()
        self.api_key = os.getenv("DOMAINR_API_KEY")
        self.base_url = "https://api.domainr.com/v1"
        # self.common_tlds = [
        #     "com", "net", "org", "io", "co", "uk", "us", "eu", "app", 
        #     "dev", "me", "info", "biz", "co.uk", "co.jp", "co.nz"
        # ]
        self.common_tlds = [
            "com"
        ]
        
        if not self.api_key:
            logger.error("No Domainr API key found in environment variables")
    
    def check_domain(self, name: str) -> Tuple[bool, List[str]]:
        """
        Check if a domain is available using Domainr via RapidAPI.

        Args:
            name: The domain name to check (without TLD)

        Returns:
            Tuple containing:
            - Boolean indicating if any domain is available
            - List of available domain names with TLDs

        Raises:
            ValueError: If the Domainr API key is not configured
        """
        if not self.api_key:
            raise ValueError("Domainr API key is required but not configured. Please add RAPIDAPI_KEY to your .env file.")

        available_domains = []
        logging.info("CHECKING DOMAIN NAME...")

        # Batch check all common TLDs in one request
        domains = [f"{name}.{tld}" for tld in self.common_tlds]
        query = ",".join(domains)

        logging.info(f"QUERY: {query}")

        try:
            response = requests.get(
                "https://domainr.p.rapidapi.com/v2/status",
                params={"domain": query},
                headers={
                    "Accept": "application/json",
                    "X-RapidAPI-Key": self.api_key,
                    "X-RapidAPI-Host": "domainr.p.rapidapi.com"
                }
            )
            logging.warning(f"Response: {response.text}")
            if response.status_code == 200:
                data = response.json()
                statuses = data.get("status", [])
                # for item in statuses:
                #     if item.get("summary") == "available":
                #         available_domains.append(item.get("domain"))
            else:
                logging.warning(f"Error checking domains: {response.status_code}")
                logging.warning(f"Response: {response.text}")

        except Exception as e:
            logging.error(f"Exception checking domains: {str(e)}")
            raise

        return len(available_domains) > 0, available_domains
    
    def filter_available_names(self, names: List[str]) -> Dict[str, Dict[str, any]]:
        """
        Filter a list of names to only those with available domains.
        
        Args:
            names: List of names to check
            
        Returns:
            Dictionary mapping names to their availability status and available domains
            
        Raises:
            ValueError: If the Domainr API key is not configured
        """
        if not self.api_key:
            raise ValueError("Domainr API key is required but not configured. Please add DOMAINR_API_KEY to your .env file.")
            
        result = {}
        for name in names:
            is_available, available_domains = self.check_domain(name)
            result[name] = {
                "domain_available": is_available,
                "available_domains": available_domains
            }
        return result

class DomainCheckerAgent(BaseAgent):
    """Agent for checking domain availability."""
    
    def __init__(self):
        """Initialize the DomainCheckerAgent."""
        super().__init__("DomainChecker")
        self.domain_checker = DomainChecker()
        logger.info("DomainCheckerAgent initialized")
        self.api_key = os.getenv("DOMAINR_API_KEY")
        self.mock_enabled = os.getenv("MOCK_DOMAIN_CHECKS", "false").lower() == "true"
        self.tlds = [".com", ".net", ".org", ".io", ".co.uk"]
    
    def _get_mock_domain_availability(self, domain_name):
        """Generate mock domain availability data"""
        return {
            "domain_available": random.choice([True, False]),
            "available_domains": [f"{domain_name}{tld}" for tld in self.tlds if random.choice([True, False])]
        }

    def execute(self, request):
        try:
            names = request.get("names", [])
            if not names:
                return {"error": "No names provided"}

            results = {}
            for name in names:
                if self.mock_enabled:
                    results[name] = self._get_mock_domain_availability(name)
                else:
                    if not self.api_key:
                        return {"error": "Domainr API key is required"}
                    
                    # Real API implementation here
                    # ... existing code ...

            return {"domain_results": results}
        except Exception as e:
            logging.error(f"Exception checking domain: {str(e)}")
            return {"error": str(e)} 