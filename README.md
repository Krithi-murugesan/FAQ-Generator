# FAQ-Generator
An AI-driven FAQ generator using CrewAI agents to transform raw text into validated JSON/Markdown outputs.

A multi-agent system designed to transform unstructured text into structured, validated FAQ data. This project focuses on agent orchestration and guaranteed output schemas.

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

# 📊 Output Example
The project ensures the output is always a valid JSON object:

JSON
{
  "faqs": [
    {
      "question": "What is the return window for products?",
      "answer": "Customers can return products within 30 days of purchase."
    },
    {
      "question": "Are digital downloads refundable?",
      "answer": "No, digital products are exempt from refunds once they have been downloaded."
    }
  ]
}

# 🧠 Skills Learned
Multi-Agent Coordination: Managing hand-offs between specialized AI roles.

Output Schemas: Using Pydantic to force LLMs into machine-readable formats.

Prompt Engineering: Creating distinct "backstories" to steer agent behavior.
