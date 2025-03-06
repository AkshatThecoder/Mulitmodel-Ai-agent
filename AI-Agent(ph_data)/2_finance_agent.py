from phi.agent import Agent
from phi.model.groq import Groq    
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

env_path = '/Users/akshatpeter/Documents/AI-Agent(ph_data)/.env'
load_dotenv(env_path)
def get_company_symbol(company: str)-> str:
    """Use this function to get the symbol for a company.

    args:
    company (str): The name of the company.

    Returns:
    str: The symbol of the company.
    """
    symbols = {
        "Phidata": "MSFT",
        "Infosys": "INFY",
        "Tesla": "TSLA",
        "Apple": "AAPL",
        "Microsoft": "MSFT",
        "Amazon": "AMZN",
        "Google": "GOOGL",
    }
    return symbols.get(company, "Unknown")
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True),
    get_company_symbol],
    show_tool_calls=True,
    markdown=True,
    instructions=["Use tabels to display the data.","If you don't know the company symbol, use the get_company_symbol tool, even if it is not a public company."],
    debug_mode=True,
)
agent.print_response("Summarize and compare the analyst recommendations and fundamentals of TSLA and Phidata")

