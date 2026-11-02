#!/usr/bin/env python3
"""
UI/UX Pro Max v2.0 — Interactive Terminal CLI with Gemini API
Powered by the official google-genai SDK.

Prerequisites:
    pip install -r requirements.txt
    export GEMINI_API_KEY="your-api-key"   # On Windows: set GEMINI_API_KEY="your-api-key"

Usage:
    python gemini_chat.py
    python gemini_chat.py --model gemini-2.5-pro
    python gemini_chat.py "Build a modern SaaS landing page for an AI editor"
"""

import sys
import os
import argparse
from google import genai
from google.genai import types

def load_system_instruction():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        os.path.join(script_dir, "..", "prompts", "gemini-system-instruction.txt"),
        os.path.join(script_dir, "..", "SYSTEM_INSTRUCTION.md")
    ]
    for path in candidates:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            # Clean markdown formatting if reading SYSTEM_INSTRUCTION.md
            if "```markdown" in content:
                content = content.split("```markdown")[1].split("```")[0]
            return content.strip()
    raise FileNotFoundError("Could not locate system instructions file.")

def main():
    parser = argparse.ArgumentParser(description="UI/UX Pro Max Interactive Chat with Gemini")
    parser.add_argument("query", nargs="?", help="Optional prompt to execute immediately")
    parser.add_argument("--model", default="gemini-2.5-flash", help="Gemini model name (default: gemini-2.5-flash)")
    parser.add_argument("--temperature", type=float, default=0.5, help="Sampling temperature (default: 0.5)")
    args = parser.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("[!] ERROR: GEMINI_API_KEY environment variable is not set.")
        print("    Please set it with: export GEMINI_API_KEY='your-key' (or set on Windows)")
        sys.exit(1)

    system_instruction = load_system_instruction()
    client = genai.Client(api_key=api_key)

    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        temperature=args.temperature,
        top_p=0.95,
        max_output_tokens=8192,
    )

    if args.query:
        print(f"[*] Sending prompt to {args.model}...")
        response = client.models.generate_content(
            model=args.model,
            contents=args.query,
            config=config,
        )
        print("\n" + "=" * 80)
        print(response.text)
        print("=" * 80)
        return

    # Interactive Chat Mode
    print("=" * 80)
    print("  UI/UX Pro Max v2.0 — Google AI Studio Terminal Assistant")
    print(f"  Model: {args.model} | Temperature: {args.temperature}")
    print("  Type 'exit' or 'quit' to end session.")
    print("=" * 80 + "\n")

    chat = client.chats.create(model=args.model, config=config)

    while True:
        try:
            user_input = input("\n[UI/UX Prompt] > ").strip()
            if not user_input:
                continue
            if user_input.lower() in ("exit", "quit", "q"):
                print("Exiting UI/UX Pro Max. Happy designing!")
                break

            print("\n[*] Generating design system & interface code...")
            response = chat.send_message(user_input)
            print("\n" + response.text + "\n")
        except (KeyboardInterrupt, EOFError):
            print("\nSession interrupted. Exiting.")
            break

if __name__ == "__main__":
    main()
