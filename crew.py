import streamlit as st
import asyncio
from crewai import Crew, Process
from tasks import research_task, write_task
from agents import Blog_researcher, Blog_writer
crew = Crew(
    agents=[Blog_researcher, Blog_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
)
async def run_crew_ai(topic):
    return crew.kickoff(inputs={'topic': topic})
st.title("AI Blog Generator")
topic = st.text_input("Enter a topic:")
if st.button('Generate Blog'):
    if topic:
        with st.spinner('Processing...'):
            result = asyncio.run(run_crew_ai(topic)) 
        st.subheader("Generated Blog Content:")
        st.write(result)
    else:
        st.error("Please enter a topic.")
