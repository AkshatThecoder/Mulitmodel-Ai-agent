from phi.agent import Agent
from phi.model.groq import Groq    
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

env_path = '/Users/akshatpeter/Documents/AI-Agent(ph_data)/.env'
load_dotenv(env_path)

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile")
)
agent.print_response("Write 2 sentences about the indian stock market")

