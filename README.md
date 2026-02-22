# FAQ-Generator
An AI-driven FAQ generator using CrewAI agents to transform raw text into validated JSON/Markdown outputs.

A multi-agent system designed to transform unstructured text into structured, validated FAQ data. This project focuses on agent orchestration and guaranteed output schemas.

This project is a **FAQ Generator** built using **CrewAI** and **OpenAI**.  
It reads a text document, analyzes it to extract key topics, and generates a **structured FAQ** in both **JSON** and **Markdown** formats.

This is designed to demonstrate:

- Multi-agent workflows (Analyzer → FAQ Writer)
- Sequential task orchestration
- Structured outputs
- Schema validation
- File-based input/output handling

# 🎯 Goal
To practice generating structured outputs from LLMs that can be immediately consumed by frontend applications or databases.

# 🏗️ Architecture
The system utilizes two specialized agents:

The Analyzer: Scans raw text to identify key themes and high-impact pain points.

The FAQ Writer: Transforms analysis into clear Q&A pairs, strictly following a Pydantic JSON schema.

# 🛠️ Tech Stack
Framework: CrewAI

Language: Python 3.10+

Validation: Pydantic (v2)

Model: OpenAI GPT-4o (or compatible LLMs)

# 🧠 Skills Learned
Multi-Agent Coordination: Managing hand-offs between specialized AI roles.

Output Schemas: Using Pydantic to force LLMs into machine-readable formats.

Prompt Engineering: Creating distinct "backstories" to steer agent behavior.


## Features

- ✅ Reads any text file as input
- ✅ Multi-agent AI processing using CrewAI
- ✅ Generates 5–7 FAQs automatically
- ✅ Outputs:
  - `outputs/faq_output.json` → Structured JSON
  - `outputs/faq_output.md` → Human-readable Markdown
- ✅ Pydantic validation ensures the output structure
- ✅ Single-file Python program for easy execution


