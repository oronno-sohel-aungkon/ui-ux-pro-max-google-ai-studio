# Complete Google AI Studio Installation & Setup Guide

This guide walks you through installing and configuring **UI/UX Pro Max v2.0** in **Google AI Studio** step-by-step.

---

## What is Google AI Studio?

[Google AI Studio](https://aistudio.google.com) is Google's web-based prototyping environment for experimenting with Gemini models (such as **Gemini 2.5 Flash**, **Gemini 2.5 Pro**, and **Gemini 1.5 Pro**).

By loading UI/UX Pro Max as a **System Instruction**, you permanently infuse the Gemini model with:
- The 10-Priority UI/UX Design Decision Hierarchy (WCAG accessibility, touch physics, performance, typography, colors)
- The v2.0 Design System Generator (producing ASCII/Markdown design cards)
- 50 active UI styles taxonomy and 192 product type reasoning profiles
- 16 semantic color roles with exact hex codes
- Industry-specific anti-patterns to avoid
- Pre-delivery quality checklists

---

## Method 1: Web Interface Setup (Recommended • 1 Minute)

### Step 1: Open Google AI Studio
1. Navigate to **[aistudio.google.com](https://aistudio.google.com)**.
2. Sign in with your Google account.
3. Click **Create New Prompt** (or choose **Chat Prompt**).

### Step 2: Choose Your Model
In the right-hand **Run Settings** panel:
- **Model:** Select `Gemini 2.5 Flash` (recommended for fast, responsive UI code generation) or `Gemini 2.5 Pro` (recommended for deep architecture and complex component trees).
- **Temperature:** Set to `0.4` or `0.5`. (Do not leave it at 1.0; a lower temperature ensures design system tokens and color contrast remain strictly compliant).

### Step 3: Paste System Instructions
1. Locate the **System Instructions** text area at the top or left of your prompt workspace.
2. Open [`SYSTEM_INSTRUCTION.md`](../SYSTEM_INSTRUCTION.md) (or [`prompts/gemini-system-instruction.txt`](../prompts/gemini-system-instruction.txt)).
3. Copy the entire instruction text.
4. Paste it directly into the **System Instructions** box in Google AI Studio.

### Step 4: Test Your First Prompt
In the user prompt box, enter any design request:
```text
Build a modern landing page for an AI developer analytics platform in React + Tailwind CSS.
```

### Expected Output:
Gemini will first generate the **Design System Card** (pattern, style, 16 semantic color tokens, typography, and anti-patterns), followed by the complete, production-ready frontend code!

---

## Method 2: Import the Prompt JSON

1. In this repository, navigate to [`prompts/google-ai-studio-prompt.json`](../prompts/google-ai-studio-prompt.json).
2. Download or save the JSON file to your local computer.
3. In Google AI Studio, click **File** -> **Open from File** (or drag the JSON file directly into the AI Studio window).
4. The system instructions, model settings, and sample prompts will load automatically!

---

## Method 3: Gemini Gems (Gemini Advanced)

If you use **Gemini Advanced** (`gemini.google.com`):
1. Go to **Gemini Gems** (`gemini.google.com/gems`).
2. Click **New Gem**.
3. Name your Gem: `UI/UX Pro Max`.
4. In the **Instructions** box, paste the contents of [`SYSTEM_INSTRUCTION.md`](../SYSTEM_INSTRUCTION.md).
5. Click **Create**.
6. You now have a permanent UI/UX Pro Max design assistant across web and mobile!
