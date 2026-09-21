# DC HOSA Advocacy

Public-facing advocacy site for DC HOSA — Future Health Professionals, served at
**advocacy.dchosa.org**. Audience is congressional offices, institutions, and prospective
partners: what DC HOSA is, what an office can do, and what each option costs them.

---

## The rule that matters

**`data/figures.json` is the only place the headline numbers are stored.** Chapters, members,
SLC attendance, the basis line, and the contact address all live there, once each.
`index.html` is generated from it.

Never hand-edit `index.html`. Edit the data, rebuild, commit both.

```bash
python3 build/build.py     # reads data/, writes index.html
```

No dependencies beyond Python 3. Three fonts from Google Fonts; nothing else external.

### Why this file exists

In September 2026 the leave-behind, the officer briefing, the two-page, and the engagement
package carried three different chapter counts and two different membership figures between
them. That was caught the day before a Hill visit. Figures handed to a congressional office
end up in a staffer's memo, and a wrong one cannot be recalled — so they get stored once,
with their basis stated on the page.

**Current figures (reconciled 21 September 2026):** 15 Local Chapters · 750+ members ·
560 SLC attendees.

Whenever these change, they must change in five places together:

1. `data/figures.json` here
2. `Front.pdf` — the designed leave-behind, edited in Canva
3. `Back.pdf` — same, including the "fifteen schools" line in *Why this is a District investment*
4. `DC_HOSA_Congressional_Engagement_Package.docx` — the copy of record, refreshed each August
5. `DC_HOSA_Hill_Briefing_Two_Page.docx` and the officer briefing — what students say aloud

A number on the printed sheet that differs from what a student says in the room is the
failure this is designed to prevent.

---

## Files

```
index.html              generated — do not edit by hand
CNAME                   advocacy.dchosa.org
data/figures.json       headline numbers, basis line, contact details
data/asks.json          the five asks, ordered by what they cost the office
build/build.py          generator
assets/                 leave-behind PDFs linked from the page
```

## Hosting

GitHub Pages from `main` / root, custom domain via the `CNAME` file. DNS at GoDaddy:
a CNAME record, name `advocacy`, value `hosadistrictofcolumbia-bit.github.io`.

The site is public and indexable. Nothing on it is confidential — it is the same material
handed across the table in a congressional office.

## Scope note

DC HOSA operates under the sponsorship and oversight of the Office of the State
Superintendent of Education and is not an independent legal entity. The page states this.
Nothing here should be written so that it reads as an OSSE position.
