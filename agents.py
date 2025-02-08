from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os


## call the gemini models
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))

# Creating a senior researcher agent with memory and verbose mode

news_researcher=Agent(
    role="Senior Researcher",
    goal='Discover cutting-edge technologies related to {topic}, that redefine the future ',
    verbose=True,
    memory=True,
    backstory=(
        "Fueled by curiosity, you lead the charge in innovation,"
        "passionately exploring and sharing insights with the power"
        "to shape the future."

    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True

)

## creating a write agent with custom tools responsible in writing news blog

news_writer = Agent(
  role='Writer',
  goal='Tell captivating tech stories about {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "With a talent for simplifying complexity, you craft"
    "compelling narratives that inform, inspire, and make new"
    "discoveries easily accessible."
  ),
  tools=[tool],
  llm=llm,
  allow_delegation=False
)