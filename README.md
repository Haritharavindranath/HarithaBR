# AI Blog Generator using CrewAI

## Introduction:
This project is a Blog Generator that uses CrewAI to generate blogs based on a user-given topic. The application takes a topic as input through a Streamlit interface and returns a well-researched and well-written blog post on the given subject. The entire process involves researching and writing tasks powered by AI agents and tools to generate high-quality content.

## Project Overview
### Agents Used
Blog_researcher: This agent is responsible for gathering information from various sources, ensuring that the content is relevant, up-to-date, and accurate.
Blog_writer: This agent processes the researched content and writes a structured blog with a natural flow.
### Tasks Defined
research_task: Task assigned to the Blog_researcher agent for information gathering.
write_task: Task assigned to the Blog_writer agent for converting the information into a blog post.
### Tools Used
Serper Dev Tool: This is a search engine tool integrated into the project for fetching reliable and accurate search results. It allows the Blog_researcher agent to collect useful data from the web in an efficient manner.
### LLM Model
Gemini1.5 Flash: The Large Language Model (LLM) used for both research and writing tasks is Gemini1.5 Flash, which is optimized for faster, high-quality text generation.
### Process
Sequential: The tasks are carried out in a sequential process, meaning the research task is completed first, followed by the writing task. This ensures that all necessary information is gathered before the blog post is created.

## Example Output:

![crew](https://github.com/user-attachments/assets/0b46d973-6b58-435a-9df4-a5b703f818b4)
