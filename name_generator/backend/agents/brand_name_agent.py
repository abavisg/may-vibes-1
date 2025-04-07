import logging
from typing import Dict, Any
from .base_agent import BaseAgent
from .name_generator import NameGeneratorAgent

# Configure logging
logger = logging.getLogger(__name__)

class BrandNameAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        logger.info("BrandNameAgent initialized")
    
    def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the brand name generation process.
        
        Args:
            input_data: Dictionary containing the generation parameters
            
        Returns:
            Dictionary with the generated names
        """
        logger.info("STARTING BRAND NAME GENERATION PROCESS ...")

        # Generate names
        try:
            self.name_generator = NameGeneratorAgent(generator_type=input_data.get("generator_type", "local"))
            generated_names = self.name_generator.execute(input_data)
            
            logger.info(f"GENERATED {len(generated_names)} BRAND NAMES!")
            
            # Create a simple response with just the names
            names_dict = {name: {} for name in generated_names}
            
            return {
                "names": names_dict
            }
        except Exception as e:
            logger.error(f"Exception generating names: {str(e)}")
            raise 