from abc import ABC, abstractmethod
import logging

# Set up logging
logger = logging.getLogger(__name__)

class BaseAgent(ABC):
    """
    Base agent class that all other agents will inherit from.
    This provides a common interface and shared functionality.
    """
    
    def __init__(self):
        """
        Initialize the base agent
        """
        logger.info(f"Initializing {self.__class__.__name__} agent")
    
    @abstractmethod
    def execute(self, *args, **kwargs):
        """
        Execute the agent's main functionality
        
        Returns:
            The result of the agent's execution
        """
        pass
    
    def log(self, message: str, level: str = "info"):
        """
        Log a message with the agent's name
        
        Args:
            message: The message to log
            level: The log level (info, warning, error, debug)
        """
        log_method = getattr(logger, level.lower(), logger.info)
        log_method(f"[{self.__class__.__name__}] {message}")
    
    def __str__(self):
        return f"{self.__class__.__name__} Agent" 