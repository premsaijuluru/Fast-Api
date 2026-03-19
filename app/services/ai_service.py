# import requests
# import os

# GEMINI_KEY = os.getenv("GEMINI_KEY")

# def analyze(sector, data):
#     url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_KEY}"

#     prompt = f"""
#     Create a professional market analysis report in markdown.

#     Sector: {sector}
#     Data: {data}

#     Include:
#     - Overview
#     - Trends
#     - Opportunities
#     - Risks
#     - Conclusion
#     """

#     body = {
#         "contents": [{"parts": [{"text": prompt}]}]
#     }

#     try:
#         res = requests.post(url, json=body)
#         return res.json()['candidates'][0]['content']['parts'][0]['text']
#     except:
#         return "AI analysis failed"


import requests
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_KEY = os.getenv("GEMINI_KEY")
def analyze(sector, data):
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_KEY}"

        prompt = f"""
        Analyze the {sector} sector in India.

        Data:
        {data}

        Give a structured markdown report:
        - Overview
        - Trends
        - Opportunities
        - Risks
        """

        body = {
            "contents": [
                {
                    "parts": [{"text": prompt}]
                }
            ]
        }

        response = requests.post(url, json=body)
        result = response.json()

        print("Gemini Response:", result)

        # ✅ safer extraction
        if "candidates" in result:
            return result["candidates"][0]["content"]["parts"][0]["text"]
        else:
            return "AI response format changed"

    except Exception as e:
        print("Gemini Error:", str(e))
        return "AI analysis failed"
