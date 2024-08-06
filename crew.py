from crewai import Crew, Process
from tasks import research_task, write_task
from agents import Blog_researcher, Blog_writer
crew = Crew(
    agents=[Blog_researcher, Blog_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
)
result = crew.kickoff(inputs={'topic': 'Growth of AI'})
print(result)