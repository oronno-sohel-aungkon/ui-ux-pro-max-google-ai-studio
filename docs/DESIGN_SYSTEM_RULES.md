# UI/UX Pro Max — Design System Rules & Catalogs Reference

This reference documents the architectural standards and catalog taxonomies baked into **UI/UX Pro Max v2.0**.

---

## 1. The 10 Priority Decision Categories

| Priority | Category | Impact | Domain | Key Checks (Must Have) | Anti-Patterns (Avoid) |
|:---|:---|:---|:---|:---|:---|
| **1** | **Accessibility** | CRITICAL | `ux` | Contrast >= 4.5:1, Alt text, Keyboard nav, Aria-labels | Removing focus rings, Icon-only buttons without labels |
| **2** | **Touch & Interaction** | CRITICAL | `ux` | Min size 44x44px, 8px+ spacing, 80-150ms press feedback | Reliance on hover only, Instant state changes (0ms) |
| **3** | **Performance** | HIGH | `ux` | WebP/AVIF, Lazy loading, Reserve space (CLS < 0.1) | Layout thrashing, Cumulative Layout Shift |
| **4** | **Style Selection** | HIGH | `style` | Match product type, Consistency, SVG icons (no emoji) | Mixing flat & skeuomorphic randomly, Emoji as icons |
| **5** | **Layout & Responsive** | HIGH | `ux` | Mobile-first breakpoints (375px+), Viewport meta | Horizontal scroll, Fixed px container widths |
| **6** | **Typography & Color** | MEDIUM | `typography` | Base 16px, Line-height 1.5, 16 Semantic color tokens | Text < 12px body, Gray-on-gray, Raw hex in components |
| **7** | **Animation** | MEDIUM | `motion` | Context-aware timing (150-350ms), Spatial continuity | One duration for all, Animating width/height |
| **8** | **Forms & Feedback** | MEDIUM | `ux` | Visible labels, Inline error near field, Progressive disclosure | Placeholder-only label, Errors only at top |
| **9** | **Navigation** | HIGH | `ux` | Predictable back, Bottom nav <= 5 tabs, Deep linking | Overloaded nav, Broken back behavior |
| **10** | **Charts & Data** | LOW | `chart` | Accessible legends, Tooltips, Color independence | Relying on color alone to convey metrics |

---

## 2. The 16 Semantic Color Tokens

Every component must reference semantic color tokens rather than raw hex codes:

| Token Name | CSS Variable | Semantic Purpose |
|:---|:---|:---|
| **Primary** | `--color-primary` | Main brand call-to-action color |
| **On Primary** | `--color-on-primary` | Text and icons placed on top of Primary |
| **Secondary** | `--color-secondary` | Supporting actions, subtle tags, chips |
| **On Secondary** | `--color-on-secondary` | Text on top of Secondary surfaces |
| **Accent / CTA** | `--color-accent` | High-conversion highlights, sales triggers |
| **On Accent / CTA** | `--color-on-accent` | Text on top of Accent / CTA elements |
| **Background** | `--color-background` | Base canvas / page background |
| **Foreground** | `--color-foreground` | Main body copy, high-contrast headings |
| **Card / Surface** | `--color-card` | Container background for cards, modals, sheets |
| **Card Foreground** | `--color-card-foreground` | Text on top of cards and elevated panels |
| **Muted** | `--color-muted` | Background for disabled states, subtle fills |
| **Muted Foreground** | `--color-muted-foreground` | Captions, timestamps, secondary helper text |
| **Border** | `--color-border` | Subtle dividers and container borders |
| **Destructive** | `--color-destructive` | Error badges, delete buttons, destructive alerts |
| **On Destructive** | `--color-on-destructive` | Text on top of Destructive elements |
| **Ring** | `--color-ring` | High-contrast keyboard focus indicators (`:focus-visible`) |

---

## 3. Top Active Visual Styles (Sample)

- **Bento Grid:** Information-dense, modular grid cards of varying sizes with subtle borders and micro-elevation. Ideal for SaaS features and developer dashboards.
- **Minimalism & Swiss Style:** High contrast, strict grid alignment, bold sans-serif typography, generous whitespace. Ideal for enterprise SaaS, documentation, and tools.
- **Glassmorphism:** Frosted-glass blur (`backdrop-blur-md`), semi-transparent surfaces (`rgba(255,255,255,0.08)`), crisp 1px borders. Ideal for modern consumer apps.
- **Soft UI Evolution:** Modern refinement of neumorphism — subtle organic shadows, warm tints, and tactile depth without muddy contrast. Ideal for wellness and lifestyle.
- **Dark Mode (OLED / Slate):** Pitch black (#000000) or deep slate (#0B0F19) canvas with vibrant accents and strict WCAG text contrast. Ideal for crypto, trading, and gaming.
- **Neo-Brutalism:** High-contrast borders (2-3px black), bold drop shadows with zero blur (`shadow-[4px_4px_0px_0px_#000]`), raw typography. Ideal for creative agencies and Gen-Z platforms.

---

## 4. Curated Google Fonts Pairings

1. **Modern SaaS / Tech:** `Plus Jakarta Sans` (Heading) + `Inter` (Body)
2. **Luxury & Editorial:** `Cormorant Garamond` (Heading) + `Montserrat` (Body)
3. **Contemporary Elegant:** `Playfair Display` (Heading) + `Source Sans 3` (Body)
4. **Developer & Data-Dense:** `Space Grotesk` (Heading) + `JetBrains Mono` (Body/Code)
5. **Creative & Avant-Garde:** `Syne` (Heading) + `Space Grotesk` (Body)
6. **Friendly & Mobile:** `Outfit` (Heading) + `DM Sans` (Body)
