# Report Examples

Reference templates and examples for Section 11-compliant AI coaching reports.

---

## Output Format Guidelines

AI systems should structure athlete reports consistently.  
See templates and examples below for annotated reference.

**Pre-Workout Reports must include:**
- Readiness assessment (HRV, RHR, Sleep vs baselines)
- Load context (TSB, ACWR, Load/Recovery, Monotony if elevated)
- Today's planned workout (or rest day + next session preview)
- Go/Modify/Skip recommendation with rationale

**Post-Workout Reports must include:**
- One-line session summary
- Completed session metrics (power, HR, zones, decoupling, VI, TSS vs planned)
- Plan compliance assessment
- Weekly running totals (polarization, CTL, ATL, TSB, ACWR, hours, TSS)
- Overall coach note (2-4 sentences: compliance, key quality observations, load context, recovery note)

See `POST_WORKOUT_TEMPLATE.md` for field reference and rounding conventions.

---

## Files

| File | Description |
|------|-------------|
| [PRE_WORKOUT_TEMPLATE.md](PRE_WORKOUT_TEMPLATE.md) | Template structure for pre-workout briefings (no data) |
| [PRE_WORKOUT_REPORT_EXAMPLES.md](PRE_WORKOUT_REPORT_EXAMPLES.md) | 4 anonymized example pre-workout reports |
| [POST_WORKOUT_TEMPLATE.md](POST_WORKOUT_TEMPLATE.md) | Template structure for post-workout analysis (no data) |
| [POST_WORKOUT_REPORT_EXAMPLES.md](POST_WORKOUT_REPORT_EXAMPLES.md) | 4 anonymized example post-workout reports |

---

## Report Types

### Pre-Workout Briefing
Generated **before** a planned session. Includes:
- Weather and coach note (optional, if location known)
- Current readiness (HRV, RHR, Sleep vs baselines)
- Load context (TSB, ACWR, Load/Recovery, Monotony if > 2.3)
- Planned workout summary (target power/HR, duration, TSS)
- Go/Modify/Skip recommendation with rationale

### Post-Workout Analysis
Generated **after** a completed session. Includes:
- Execution summary (actual vs planned)
- Key metrics (power, HR, decoupling, VI, carbs)
- Zone distribution (Grey Zone and Quality tracking)
- Load impact (updated CTL, ATL, TSB, weekly totals)
- Coaching interpretation

---

## Brevity Rule

These templates follow Section 11's brevity principle:
- **Normal metrics:** Brief — 2-3 sentence interpretation + key data
- **Threshold breach:** Detailed — full analysis with recommendations
- **Rest day:** Minimal — confirm recovery status, preview next session
- **Athlete asks "why":** Deep dive on specific area

---

## Conditional Fields

Some fields appear only when relevant:
- **Weather:** Include if athlete location is available via profile or memory
- **Monotony:** Include only if > 2.3; omit entirely when normal
- **Load/Recovery tolerance note:** Include only when within 0.2 of threshold
- **Coach notes** (brief contextual tips) are encouraged to humanize recommendations

---

## Notes

- All examples use anonymized/placeholder data — replace with actual values from your JSON feed
- Zone percentages round to nearest whole number (see rounding convention in POST_WORKOUT_TEMPLATE.md)
