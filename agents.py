from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os

## llm model
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))

# agents for creating the blog
Blog_researcher=Agent(
    role="Blog Researcher",
    goal='Identify emerging technologies,news,blogs and trends in {topic}, providing detailed insights and analysis.',
    verbose=True,
    memory=True,
    backstory=(
        "As a seasoned researcher with a passion for discovery,"
        "you delve deep into the {topic},"
        "uncovering valuable information,trends and concepts that can inform and inspire blog readers."

    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True

)
Blog_writer = Agent(
  role='Blog Writer',
  goal='Craft engaging and informative blog posts on {topic}, turning complex information into accessible and captivating stories.',
  verbose=True,
  memory=True,
  backstory=(
    "With a talent for storytelling and a knack for demystifying concepts,"
    "you write blog posts that not only inform but also captivate readers, making the {topic} easy to understand and exciting."
  ),
  tools=[tool],
  llm=llm,
  allow_delegation=False
)