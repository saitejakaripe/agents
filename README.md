# AI Agents Lab

Hands-on AI agent engineering lab covering LangGraph, AutoGen, CrewAI-style orchestration, MCP tool use, memory, persistence, and OpenAI-based workflows. The repository is organized as practical notebooks plus small agent projects so recruiters can see both experimentation and implementation.

## What This Project Shows

- Agent foundations, tool calling patterns, memory workflows, and persistence.
- OpenAI integration experiments for agentic reasoning and structured outputs.
- LangGraph workflows for graph-based state transitions and multi-step agent control.
- AutoGen and multi-agent collaboration patterns.
- MCP-oriented tool integration experiments.
- Crew-style project folders with `agents.yaml`, `tasks.yaml`, and Python orchestration code.

## Repository Structure

```text
agents/
|-- 1_foundations.ipynb
|-- 2_openai.ipynb
|-- 4_langgraph.ipynb
|-- 5_autogen.ipynb
|-- 6_mcp.ipynb
|-- 3_crew/
|   |-- project_1/
|   |-- project_2/
|   `-- project_3/
|-- Sundar_pichai/
|-- memory/
|-- output/
|-- sandbox/
|-- memory-tool.db
|-- memory.db
`-- tickets.db
```

## Notebook Map

| Notebook | Focus |
| --- | --- |
| `1_foundations.ipynb` | Agent basics, reasoning loops, and tool-use foundations |
| `2_openai.ipynb` | OpenAI-backed workflows and structured interaction patterns |
| `4_langgraph.ipynb` | LangGraph state graphs for controlled agent workflows |
| `5_autogen.ipynb` | AutoGen-style multi-agent collaboration experiments |
| `6_mcp.ipynb` | Model Context Protocol experiments and external tool access |

## Tech Stack

- Python and Jupyter Notebook
- OpenAI APIs
- LangGraph, AutoGen, Crew-style agent orchestration
- SQLite-backed memory and persistence experiments
- YAML-based agent/task configuration

## How To Explore

Open the notebooks in order if you want the learning path, or start with the `3_crew/` folders if you want to inspect the project-style agent implementations first.

```bash
cd agents
jupyter lab
```

## Recruiter Notes

This repo demonstrates the progression from agent fundamentals to more realistic multi-agent workflows: tool use, memory, orchestration, structured outputs, and project organization. It is a strong supporting repo for AI Agent Engineer, GenAI Engineer, and LLM application roles.
