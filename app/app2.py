from openai import OpenAI
from dotenv import load_dotenv
import os
import json

# 🔐 Load API key securely
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

APP_NAME = "LegallySahi"


# 🧠 Smart detection
def is_legal_query(text):
    keywords = [
        "law", "legal", "police", "fraud", "complaint",
        "court", "tenant", "rent", "FIR", "cyber",
        "scam", "notice", "agreement", "arrest",
        "rights", "challan", "salary", "company"
    ]
    return any(word.lower() in text.lower() for word in keywords)


# 🎨 Colored output
def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")


# 🤖 AI call
def get_legal_response(user_input):
    prompt = f"""
You are an AI Legal Assistant focused ONLY on Indian legal guidance.

ROLE:
- Explain legal issues simply
- Provide practical steps
- Highlight risks (especially scams)

STRICT RULES:
- ONLY respond to legal queries
- If unclear, say "Uncertain"
- DO NOT hallucinate laws
- Respond ONLY in JSON

FORMAT:
{{
  "issue": "",
  "is_likely_valid": "Yes / No / Uncertain",
  "explanation": "",
  "next_steps": ["", "", "", ""],
  "warning": "",
  "confidence": "High / Medium / Low"
}}

User Query: {user_input}
"""

    response = client.responses.create(
        model="gpt-5-nano",
        input=prompt
    )

    output_text = response.output_text.strip()

    try:
        start = output_text.find("{")
        end = output_text.rfind("}") + 1
        clean_json = output_text[start:end]
        return json.loads(clean_json)

    except Exception:
        print("\n⚠️ Raw output (debug):\n", output_text)
        return {"error": "Invalid JSON format"}


# 💾 Save history
def save_history(user_input, result):
    with open("history.txt", "a", encoding="utf-8") as f:
        f.write(f"Q: {user_input}\nA: {json.dumps(result, indent=2)}\n\n")


# 🚀 Main app
def main():
    print(f"{APP_NAME} - AI Legal Assistant (India)")
    print("⚠️ This is general guidance, not legal advice.\n")

    print("Try examples:")
    print("- Landlord not returning deposit")
    print("- Online scam refund issue")
    print("- Police asking for bribe")
    print("- Fake challan received\n")

    while True:
        user_input = input("Ask your legal question (type 'exit' to quit): ")

        if user_input.lower() == "exit":
            break

        # 🧠 Filter non-legal
        if not is_legal_query(user_input):
            print("\n⚠️ This assistant only handles legal-related queries.")
            print("Try asking about rights, laws, disputes, or legal issues.\n")
            continue

        result = get_legal_response(user_input)

        if "error" in result:
            print("Error:", result["error"])
        else:
            print("\n--- RESULT ---")

            print_colored("Issue: " + result["issue"], "36")
            print("Valid?:", result["is_likely_valid"])
            print("Explanation:", result["explanation"])

            print("\nSteps:")
            for step in result["next_steps"]:
                print("-", step)

            print_colored("\nWarning: " + result["warning"], "31")
            print("Confidence:", result["confidence"])

            print("\n----------------\n")

            save_history(user_input, result)


if __name__ == "__main__":
    main()