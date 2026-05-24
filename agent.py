from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.models.lite_llm import LiteLlm


general_model = LiteLlm(
    model="ollama/llama3.1",
    api_base="http://localhost:11434",
)

coder_model = LiteLlm(
    model="ollama/qwen2.5-coder:7b",
    api_base="http://localhost:11434",
)


research_agent = LlmAgent(
    name="ResearchAgent",
    model=general_model,
    instruction="Create implementation plan. No code.",
    output_key="research",
)

coding_agent = LlmAgent(
    name="CodingAgent",
    model=coder_model,
    instruction="Write Python code only using {research}",
    output_key="code",
)

reviewer_agent = LlmAgent(
    name="ReviewerAgent",
    model=general_model,
    instruction="Improve this code: {code}. Return final code only.",
    output_key="reviewed_code",
)

summarizer_agent = LlmAgent(
    name="SummarizerAgent",
    model=general_model,
    instruction="Summarize the result: {reviewed_code}",
    output_key="summary",
)


# IMPORTANT: ADK WEB ENTRY POINT
root_agent = SequentialAgent(
    name="AutonomousTeam",
    sub_agents=[
        research_agent,
        coding_agent,
        reviewer_agent,
        summarizer_agent,
    ],
)