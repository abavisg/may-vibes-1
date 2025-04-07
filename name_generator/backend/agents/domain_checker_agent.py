import os
import logging
import requests
from typing import Dict, Any
from dotenv import load_dotenv
from .base_agent import BaseAgent
import random

# Configure logging
logger = logging.getLogger(__name__)

class DomainCheckerAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        load_dotenv()
        self.api_key = os.getenv("DOMAINR_API_KEY")
        self.mock_enabled = os.getenv("MOCK_DOMAIN_CHECKS", "false").lower() == "true"
        self.tlds = [".com", ".co.uk"]
        logger.info("DomainCheckerAgent initialized")
        
    def _get_mock_domain_availability(self, domain_name):
        """Generate mock domain availability data"""
        return {
            "domain_available": random.choice([True, False]),
            "available_domains": [f"{domain_name}{tld}" for tld in self.tlds if random.choice([True, False])]
        }

    def execute(self, request):
        try:
            name = request.get("name")
            if not name:
                return {"error": "No name provided"}

            if self.mock_enabled:
                return self._get_mock_domain_availability(name)
            else:
                if not self.api_key:
                    return {"error": "Domainr API key is required"}
                
                # Real API implementation
                try:
                    # Check domain availability using Domainr API
                    available_domains = []
                    domains = [f"{name}{tld}" for tld in self.tlds]
                    query = ",".join(domains)
                    
                    logging.info(f"Checking domains: {query}")

                    response = requests.get(
                        "https://domainr.p.rapidapi.com/v2/status",
                        params={"domain": query},
                        headers={
                            "Accept": "application/json",
                            "X-RapidAPI-Key": self.api_key,
                            "X-RapidAPI-Host": "domainr.p.rapidapi.com"
                        }
                    )

                    if response.status_code == 200:
                        data = response.json()
                        statuses = data.get("status", [])
                        logging.info(f"Statuses: {statuses}")
                        for item in statuses:
                            if item.get("summary") == "available" or item.get("status") == "undelegated inactive":
                                available_domains.append(item.get("domain"))
                    else:
                        logger.warning(f"Error checking domains: {response.status_code}")
                        logger.warning(f"Response: {response.text}")
                    
                    return {
                        "domain_available": len(available_domains) > 0,
                        "available_domains": available_domains
                    }
                except Exception as e:
                    logger.error(f"Exception checking domain: {str(e)}")
                    return {
                        "domain_available": False,
                        "available_domains": [],
                        "error": str(e)
                    }
        except Exception as e:
            logger.error(f"Exception checking domain: {str(e)}")
            return {"error": str(e)} 