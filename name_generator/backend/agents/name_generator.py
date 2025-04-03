from typing import List
import random
import logging
import os
import requests
from dotenv import load_dotenv
from abc import ABC, abstractmethod
import openai
import json
#from smolagents import MultiStepAgent

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NameGeneratorBase(ABC):
    @abstractmethod
    def generate_names(self, industry: str, keywords: List[str], tone: str, audience: str | None) -> List[str]:
        pass

class LocalNameGenerator(NameGeneratorBase):
    def __init__(self):
        # Define word lists for different components
        self.prefixes = [
            "Neo", "Art", "Mod", "Deco", "Zen", "Vue", "Pure", "Flow", "Vibe", "Lux",
            "Aero", "Bliss", "Core", "Echo", "Fuse", "Glow", "Hive", "Iris", "Jade", "Kale",
            "Lume", "Muse", "Nova", "Ora", "Pulse", "Quill", "Rise", "Sage", "Tone", "Unity"
        ]
        
        self.suffixes = [
            "Space", "Design", "Style", "Home", "Living", "Studio", "Works", "House", "Place", "Craft",
            "Lab", "Hub", "Spot", "Zone", "Room", "Den", "Nest", "Corner", "Point", "Base",
            "Center", "Spot", "Place", "Studio", "Works", "House", "Room", "Space", "Zone", "Hub"
        ]
        
        self.connectors = [" ", "-", ".", ""]
        
        self.modern_words = [
            "Modern", "Urban", "Minimal", "Clean", "Fresh", "Smart", "Swift", "Light", "Air", "Sky",
            "Cloud", "Wave", "Flow", "Stream", "Breeze", "Wind", "Sun", "Moon", "Star", "Sky"
        ]
        
        self.playful_words = [
            "Joy", "Fun", "Play", "Spark", "Pop", "Bounce", "Jump", "Skip", "Hop", "Dance",
            "Wiggle", "Twist", "Spin", "Roll", "Flip", "Slide", "Glide", "Float", "Fly", "Soar"
        ]
        
        self.artistic_words = [
            "Art", "Canvas", "Brush", "Palette", "Color", "Hue", "Tone", "Shade", "Paint", "Draw",
            "Sketch", "Design", "Form", "Shape", "Line", "Curve", "Wave", "Flow", "Style", "Craft"
        ]

    def generate_names(self, industry: str, keywords: List[str], tone: str, audience: str | None) -> List[str]:
        try:
            names = set()
            while len(names) < 100:
                # Generate names using different patterns
                patterns = [
                    # Pattern 1: Prefix + Connector + Suffix
                    lambda: f"{random.choice(self.prefixes)}{random.choice(self.connectors)}{random.choice(self.suffixes)}",
                    
                    # Pattern 2: Modern/Playful/Artistic word + Connector + Industry-related word
                    lambda: f"{random.choice(self.modern_words)}{random.choice(self.connectors)}{random.choice(self.suffixes)}",
                    
                    # Pattern 3: Keyword + Connector + Suffix
                    lambda: f"{random.choice(keywords).capitalize()}{random.choice(self.connectors)}{random.choice(self.suffixes)}",
                    
                    # Pattern 4: Prefix + Connector + Keyword
                    lambda: f"{random.choice(self.prefixes)}{random.choice(self.connectors)}{random.choice(keywords).capitalize()}",
                    
                    # Pattern 5: Two-word combination based on tone
                    lambda: self._generate_tone_based_name(tone, keywords)
                ]
                
                name = random.choice(patterns)()
                if name not in names:
                    names.add(name)
            
            return sorted(list(names))
            
        except Exception as e:
            logger.error(f"Error generating names: {str(e)}")
            raise

    def _generate_tone_based_name(self, tone: str, keywords: List[str]) -> str:
        if tone == "modern":
            return f"{random.choice(self.modern_words)}{random.choice(self.connectors)}{random.choice(self.suffixes)}"
        elif tone == "playful":
            return f"{random.choice(self.playful_words)}{random.choice(self.connectors)}{random.choice(self.suffixes)}"
        elif tone == "artistic":
            return f"{random.choice(self.artistic_words)}{random.choice(self.connectors)}{random.choice(self.suffixes)}"
        else:
            return f"{random.choice(self.prefixes)}{random.choice(self.connectors)}{random.choice(self.suffixes)}"

class HuggingFaceNameGenerator(NameGeneratorBase):
    def __init__(self):
        # Initialize MultiStepAgent
        self.agent = MultiStepAgent()

    def generate_names(self, industry: str, keywords: List[str], tone: str, audience: str | None) -> List[str]:
        try:
            # Construct the prompt
            prompt = f"""Generate 100 unique and creative brand names for a {industry} business.
            Keywords: {', '.join(keywords)}
            Tone: {tone}
            Target Audience: {audience or 'Not specified'}
            
            Requirements:
            - Each name should be unique and memorable
            - Names should reflect the specified tone and industry
            - Include a mix of modern, classic, and creative names
            - Names should be 1-3 words long
            - No numbers or special characters except hyphens and spaces
            - Return exactly 100 names, one per line
            - No additional text or numbering
            
            Generate 100 names:"""

            # Use MultiStepAgent to generate names
            response = self.agent.run(prompt)
            
            # Split into lines and clean up
            names = [
                line.strip()
                for line in response.split('\n')
                if line.strip() and not line.strip().startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', '0.'))
            ]
            
            # Ensure we have exactly 100 names
            if len(names) > 100:
                names = names[:100]
            elif len(names) < 100:
                # If we got fewer than 100 names, make another call to get more
                additional_names = self.generate_names(industry, keywords, tone, audience)
                names.extend(additional_names[:100 - len(names)])
            
            return names[:100]
            
        except Exception as e:
            logger.error(f"Error generating names with MultiStepAgent: {str(e)}")
            raise

class OpenAINameGenerator(NameGeneratorBase):
    def __init__(self):
        # Load environment variables
        load_dotenv()
        
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set")
        openai.api_key = api_key

    def generate_names(self, industry: str, keywords: List[str], tone: str, audience: str | None) -> List[str]:
        try:
            # Construct the prompt
            prompt = f"""Generate 100 unique and creative brand names for a {industry} business.
            Keywords: {', '.join(keywords)}
            Tone: {tone}
            Target Audience: {audience or 'Not specified'}
            
            Requirements:
            - Each name should be unique and memorable
            - Names should reflect the specified tone and industry
            - Include a mix of modern, classic, and creative names
            - Names should be 1-3 words long
            - No numbers or special characters except hyphens and spaces
            - Return exactly 100 names, one per line
            - No additional text or numbering
            
            Generate 100 names:"""

            # Make the API call
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a creative brand name generator. Generate exactly 100 unique brand names, one per line, with no additional text or numbering."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.8,
                max_tokens=2000
            )
            
            # Process the response
            generated_text = response.choices[0].message.content
            
            # Split into lines and clean up
            names = [
                line.strip()
                for line in generated_text.split('\n')
                if line.strip() and not line.strip().startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', '0.'))
            ]
            
            # Ensure we have exactly 100 names
            if len(names) > 100:
                names = names[:100]
            elif len(names) < 100:
                # If we got fewer than 100 names, make another API call to get more
                additional_names = self.generate_names(industry, keywords, tone, audience)
                names.extend(additional_names[:100 - len(names)])
            
            return names[:100]
            
        except Exception as e:
            logger.error(f"Error generating names with OpenAI: {str(e)}")
            raise

class OllamaNameGenerator(NameGeneratorBase):
    def __init__(self):
        self.base_url = "http://localhost:11434"
        self.model = "mistral"

    def generate_names(self, industry: str, keywords: List[str], tone: str, audience: str | None) -> List[str]:
        try:
            # Construct the prompt
            prompt = f"""
            You are a naming assistant.

            Generate exactly 100 unique and creative brand names for a business in the "{industry}" industry.

            Use the following context:
            - Keywords: {', '.join(keywords)}
            - Tone: {tone}
            - Target Audience: {audience or 'Not specified'}

            Requirements:
            - Each name must be unique and memorable.
            - Names should reflect the specified tone and industry.
            - Include a mix of modern, classic, and creative styles.
            - Names must be 1–2 words long.
            - No numbers or special characters (except hyphens and spaces).
            - Do not include any explanations, numbering, or formatting.

            Return your response as a valid JSON array of strings. Example:
            ["Name One", "Name Two", "Name Three"]
            ...
            ]
            """

            ## Make the API call with streaming enabled
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False  # Enable streaming
                },
                stream=False  # Enable response streaming
            )
            
            logger.info(f"Response status code: {response.status_code}")
            logger.info(f"Response TEXT: {response.json}")
            
            if response.status_code != 200:
                logger.error(f"Ollama API call failed with status code {response.status_code}")
                logger.error(f"Response: {response.text}")
                raise Exception(f"Ollama API call failed: {response.text}")
            
            raw_response = response.json()['response']

            start = raw_response.find('[')
            end = raw_response.find(']', start)

            if start == -1 or end == -1:
                raise ValueError("Could not locate JSON array in response")

            json_str = raw_response[start:end+1]

            try:
                names = json.loads(json_str)
            except json.JSONDecodeError as e:
                logger.error(f"Failed to parse JSON from cleaned response: {e}")
                raise

            logger.info(f"Generated {len(names)} names. Example: {names[:5]}")
            
            
            return names
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Network error while calling Ollama API: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Error generating names with Ollama: {str(e)}")
            raise

class NameGeneratorFactory:
    @staticmethod
    def create_generator(generator_type: str) -> NameGeneratorBase:
        if generator_type == "local":
            return LocalNameGenerator()
        elif generator_type == "huggingface":
            return HuggingFaceNameGenerator()
        elif generator_type == "openai":
            return OpenAINameGenerator()
        elif generator_type == "ollama":
            logger.info("Creating OllamaNameGenerator")
            return OllamaNameGenerator()
        else:
            raise ValueError(f"Unknown generator type: {generator_type}")

# Create a singleton instance
name_generator_factory = NameGeneratorFactory()