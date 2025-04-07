import logging
from typing import Dict, List, Any, Type
from .base_agent import BaseAgent
# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AgentManager:
    """
    Manages and coordinates multiple agents
    """
    
    def __init__(self):
        """
        Initialize the agent manager
        """
        self.agents: Dict[str, BaseAgent] = {}
        logger.info("Initializing Agent Manager")
    
    def register_agent(self, agent: BaseAgent) -> None:
        """
        Register an agent with the manager
        
        Args:
            agent: The agent to register
        """
        agent_name = agent.__class__.__name__
        self.agents[agent_name] = agent
        logger.info(f"Registered agent: {agent_name}")
    
    def get_agent(self, agent_name: str) -> BaseAgent:
        """
        Get an agent by name
        
        Args:
            agent_name: The name of the agent to get
            
        Returns:
            The agent with the given name
            
        Raises:
            KeyError: If the agent is not found
        """
        if agent_name not in self.agents:
            raise KeyError(f"Agent '{agent_name}' not found")
        return self.agents[agent_name]
    
    def execute_agent(self, agent_name: str, *args, **kwargs) -> Any:
        """
        Execute an agent by name
        
        Args:
            agent_name: The name of the agent to execute
            *args: Positional arguments to pass to the agent
            **kwargs: Keyword arguments to pass to the agent
            
        Returns:
            The result of the agent's execution
            
        Raises:
            KeyError: If the agent is not found
        """
        agent = self.get_agent(agent_name)
        logger.info(f"Executing agent: {agent_name}")
        return agent.execute(*args, **kwargs)
    
    def execute_agent_chain(self, agent_names: List[str], initial_data: Any = None) -> Any:
        """
        Execute a chain of agents in sequence
        
        Args:
            agent_names: List of agent names to execute in order
            initial_data: Initial data to pass to the first agent
            
        Returns:
            The result of the last agent's execution
            
        Raises:
            KeyError: If any agent is not found
        """
        data = initial_data
        for agent_name in agent_names:
            agent = self.get_agent(agent_name)
            logger.info(f"Executing agent in chain: {agent_name}")
            data = agent.execute(data)
        return data
    
    def list_agents(self) -> List[str]:
        """
        List all registered agents
        
        Returns:
            List of agent names
        """
        return list(self.agents.keys())

# Create a singleton instance
agent_manager = AgentManager() 