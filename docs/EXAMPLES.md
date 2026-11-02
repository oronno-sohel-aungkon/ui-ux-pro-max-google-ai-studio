# UI/UX Pro Max — Prompt Examples & Showcase

Here are curated prompts you can run in **Google AI Studio** with UI/UX Pro Max loaded.

---

## Example 1: B2B Developer Tool Landing Page

### User Prompt:
```text
Build a modern landing page for an AI-powered code security and vulnerability scanner in React + Tailwind CSS.
```

### Expected Output Structure:
1. **Design System Card:**
   - **Pattern:** Hero-Centric + Social Proof + Bento Feature Grid
   - **Style:** Bento Grid Modern + Slate Dark Canvas
   - **Colors:** Primary: `#2563EB` (Blue), Background: `#0B0F19` (Slate 950), Card: `#111827`, Accent: `#10B981` (Emerald)
   - **Typography:** Space Grotesk (Heading) + JetBrains Mono (Body/Code)
   - **Anti-Patterns:** Cartoon emojis as icons, AI pink/purple pastel gradients
2. **Component Code:**
   - Sticky navbar with brand logo, documentation links, and terminal icon.
   - Hero section with live animated command execution snippet (`npx scan-repo`).
   - 4-card Bento Grid highlighting vulnerability graph, CI/CD integrations, compliance badges.
   - Pre-delivery audit verification.

---

## Example 2: Mobile Fintech Dashboard

### User Prompt:
```text
Create a mobile-first personal wealth and cryptocurrency portfolio dashboard with dark theme in HTML + Tailwind.
```

### Expected Output Structure:
1. **Design System Card:**
   - **Pattern:** Data-Dense Drill-Down
   - **Style:** Dark Mode (OLED / Slate) + High-Density Modern
   - **Colors:** Primary: `#F59E0B` (Gold), Background: `#000000` (OLED Black), Card: `#121212`, Text: `#F8FAFC`
   - **Typography:** Inter (Headings) + JetBrains Mono (Financial figures)
   - **Anti-Patterns:** Playful pastel buttons, low-contrast text below 4.5:1
2. **Component Code:**
   - Total balance card with real-time percentage badge (+14.2% in emerald).
   - Horizontal swipeable asset cards (Bitcoin, Ethereum, Solana).
   - Recent transactions list with clean inline SVG arrows.
   - Fixed bottom navigation bar with 4 tap targets (min 44x44px).

---

## Example 3: Luxury Wellness & Spa Booking

### User Prompt:
```text
Design a luxury boutique spa booking interface in React + Tailwind with calming, earthy aesthetics.
```

### Expected Output Structure:
1. **Design System Card:**
   - **Pattern:** Hero-Centric + Service Showcase
   - **Style:** Soft UI Evolution + Editorial Earthy
   - **Colors:** Primary: `#E8B4B8` (Dusty Rose), Secondary: `#A8D5BA` (Sage), Background: `#FFF5F5` (Warm Alabaster), CTA: `#D4AF37` (Muted Gold)
   - **Typography:** Cormorant Garamond (Heading) + Montserrat (Body)
   - **Anti-Patterns:** Corporate tech blue, harsh pure black (#000000), frantic animations
2. **Component Code:**
   - Elegant typography with balanced headings.
   - Soft shadow elevations (`shadow-[0_8px_30px_rgb(0,0,0,0.04)]`).
   - Interactive date & treatment selector with smooth 200ms transition states.

---

## Example 4: UI/UX Quality & Accessibility Audit

### User Prompt:
```text
Review this navigation bar code for UX anti-patterns, accessibility violations, and mobile touch target issues:

<div class="header">
  <span style="font-size:12px; color:#888;">MyApp</span>
  <a href="#" style="margin-left:5px;">🚀 Features</a>
  <a href="#" style="margin-left:5px;">Pricing</a>
  <button style="background:purple; font-size:11px;">Sign In</button>
</div>
```

### Expected Output Structure:
1. **Audit Diagnostics:**
   - Priority 1 (Accessibility): Missing semantic `<header>`, `<nav>`, and `<button>` ARIA attributes. Color `#888` on white fails WCAG 4.5:1 contrast.
   - Priority 2 (Touch Targets): Tap clearance of `5px` is below the 8px minimum. Button font size of `11px` creates touch targets far smaller than 44x44px.
   - Priority 4 (Style): Emojis used as icons (🚀).
2. **Refactored Code:**
   - Complete, accessible, semantically valid navigation component with responsive mobile drawer and visible keyboard focus rings.
