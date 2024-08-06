from crewai import Task
from tools import tool
from agents import Blog_researcher, Blog_writer

# Research task
research_task = Task(
    description=(
        "Conduct in-depth research on {topic}."
        "only include information relevant to the {topic}"
        "understand the conceptual background of the {topic}"
        "Identify key points, market opportunities, potential risks, and the overall narrative. "
        "Your final report should provide a balanced view, highlighting both pros and cons."
    ),
    expected_output='A comprehensive 3 paragraphs long report on the {topic}',
    tools=[tool],
    agent=Blog_researcher,
)

# Writer task 
write_task = Task(
    description=(
        "Compose an insightful article on {topic}."
        "only include information relevant to the {topic}"
        "Focus on the latest developments and conceptual background of the {topic}. "
        "The article should be easy to understand, engaging"
        "it should cover all the important news realted to the {topic}"
    ),
    expected_output=(
        'A 4-paragraph article on {topic} advancements formatted as markdown. \n'
        '<EXAMPLE>\n'
        'Story 1:\n'
        '- Title: **Daily briefing: AI now beats humans at basic reading and maths**\n'
        '- *Summary:* AI systems can now nearly match and sometimes exceed human performance in basic tasks. '
        'The report discusses the need for new benchmarks to assess AI capabilities and highlights the ethical considerations for AI models.\n'
        '</EXAMPLE>'
    ),
    tools=[tool],
    agent=Blog_writer,
    async_execution=False,
    output_file='blog.md'  
)