# from openai import OpenAI
# import json

# client = OpenAI(api_key="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")


# def get_legal_response(user_input):
#     prompt = f"""
# You are an AI Legal Assistant focused ONLY on Indian legal guidance.

# YOUR ROLE:
# - Help users understand legal issues in simple language
# - Provide practical legal guidance
# - Explain rights, risks, and next steps

# STRICT BOUNDARIES:
# - ONLY respond to queries related to law, rights, legal procedures, documents, or disputes
# - If the query is NOT legal (e.g., gaming, downloads, general tech, random questions), DO NOT answer it normally
# - Instead, politely redirect the user to legal usage

# FOR NON-LEGAL QUESTIONS:
# Respond in this JSON format:
# {{
#   "issue": "Non-legal query",
#   "is_likely_valid": "Unrelated",
#   "explanation": "This assistant only provides legal guidance. Your question is not related to legal matters.",
#   "next_steps": [
#     "Ask a legal question related to rights, laws, or disputes",
#     "Example: landlord issues, fraud, police, cybercrime, contracts"
#   ],
#   "warning": "No legal context detected",
#   "confidence": "High"
# }}

# FOR LEGAL QUESTIONS:
# Respond ONLY in this JSON format:
# {{
#   "issue": "Short one-line summary",
#   "is_likely_valid": "Yes / No / Uncertain",
#   "explanation": "Clear simple explanation (3-5 sentences max)",
#   "next_steps": [
#     "Step 1",
#     "Step 2",
#     "Step 3",
#     "Step 4"
#   ],
#   "warning": "Any risk, scam alert, or caution",
#   "confidence": "High / Medium / Low"
# }}

# IMPORTANT RULES:
# - DO NOT answer non-legal queries normally
# - DO NOT provide illegal instructions
# - DO NOT hallucinate laws
# - If unsure, say "Uncertain"
# - Keep answers practical and actionable
# - Always prioritize user safety

# User Query: {user_input}
# """

#     response = client.responses.create(
#         model="gpt-5-nano",
#         input=prompt
#     )

#     output_text = response.output_text.strip()

#     # 🔥 CLEANING STEP (very important)
#     # Sometimes AI adds extra text → we extract only JSON part
#     try:
#         start = output_text.find("{")
#         end = output_text.rfind("}") + 1
#         clean_json = output_text[start:end]

#         return json.loads(clean_json)

#     except Exception as e:
#         print("\n⚠️ Raw output (debug):\n", output_text)
#         return {"error": "Invalid JSON format"}


# def main():
#     print("⚖️ Legal AI Assistant")
#     print("⚠️ This is general guidance, not legal advice.\n")

#     while True:
#         user_input = input("Ask your legal question (type 'exit' to quit): ")

#         if user_input.lower() == "exit":
#             break

#         result = get_legal_response(user_input)

#         if "error" in result:
#             print("Error:", result["error"])
#         else:
#             print("\n--- RESULT ---")
#             print("Issue:", result["issue"])
#             print("Valid?:", result["is_likely_valid"])
#             print("Explanation:", result["explanation"])
#             print("Steps:")
#             for step in result["next_steps"]:
#                 print("-", step)
#             print("Warning:", result["warning"])
#             print("Confidence:", result["confidence"])
#             print("\n----------------\n")


# if __name__ == "__main__":
#     main()