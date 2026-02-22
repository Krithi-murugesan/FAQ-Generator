import os
import json
from src.crew import FaqGeneratorCrew


def save_markdown(faq_data):
    os.makedirs("outputs", exist_ok=True)

    with open("outputs/faq_output.md", "w", encoding="utf-8") as f:
        f.write("# Frequently Asked Questions\n\n")
        for faq in faq_data["faqs"]:
            f.write(f"## {faq['question']}\n\n")
            f.write(f"{faq['answer']}\n\n")


def run():
    # Ask user for input file
    input_file = input("Enter the path to your text file: ").strip()

    # Check if file exists
    if not os.path.exists(input_file):
        print("❌ File not found.")
        return

    # Read file content
    with open(input_file, "r", encoding="utf-8") as file:
        source_text = file.read()

    if not source_text.strip():
        print("❌ Input file is empty.")
        return

    print("📂 File loaded successfully.")
    print("🚀 Running FAQ Generator Crew...")

    inputs = {
        "source_text": source_text
    }

    result = FaqGeneratorCrew().crew().kickoff(inputs=inputs)

    # Convert structured result
    faq_data = json.loads(result.raw)

    # Create outputs folder
    os.makedirs("outputs", exist_ok=True)

    # Save JSON
    with open("outputs/faq_output.json", "w", encoding="utf-8") as f:
        json.dump(faq_data, f, indent=4)

    # Save Markdown
    save_markdown(faq_data)

    print("✅ FAQ Generation Complete!")
    print("📁 Check outputs/faq_output.json and outputs/faq_output.md")


if __name__ == "__main__":
    run()
