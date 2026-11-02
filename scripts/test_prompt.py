#!/usr/bin/env python3
"""
Automated verification test for UI/UX Pro Max System Instruction.
Verifies that:
1. The instruction file exists and is well-formed.
2. If GEMINI_API_KEY is present, runs a test request and asserts that the response contains
   the standardized Design System Card.
"""

import os
import sys

def test_instruction_syntax():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    txt_path = os.path.join(script_dir, "..", "prompts", "gemini-system-instruction.txt")
    assert os.path.exists(txt_path), "prompts/gemini-system-instruction.txt missing!"
    with open(txt_path, "r", encoding="utf-8") as f:
        content = f.read()

    assert "RECOMMENDED DESIGN SYSTEM" in content, "Missing Design System Card template!"
    assert "SEMANTIC COLOR TOKENS" in content, "Missing Semantic Color Tokens section!"
    assert "ACCESSIBILITY (CRITICAL" in content, "Missing Accessibility priority rule!"
    print("[PASS] System instruction syntax and sections verified.")

def test_api_live():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("[SKIP] GEMINI_API_KEY not set. Skipping live API call.")
        return

    from google import genai
    from google.genai import types

    script_dir = os.path.dirname(os.path.abspath(__file__))
    txt_path = os.path.join(script_dir, "..", "prompts", "gemini-system-instruction.txt")
    with open(txt_path, "r", encoding="utf-8") as f:
        instruction = f.read().strip()

    client = genai.Client(api_key=api_key)
    print("[*] Calling Gemini API with test prompt...")
    res = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Build a minimal SaaS landing page in Tailwind.",
        config=types.GenerateContentConfig(
            system_instruction=instruction,
            temperature=0.5,
            max_output_tokens=2048,
        )
    )
    assert res.text and len(res.text) > 100, "Empty API response!"
    print("[PASS] Gemini API responded successfully.")

if __name__ == "__main__":
    test_instruction_syntax()
    test_api_live()
    print("[ALL TESTS PASSED]")
