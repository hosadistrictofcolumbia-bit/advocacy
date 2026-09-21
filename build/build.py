#!/usr/bin/env python3
import json, os, html as H

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F = json.load(open(os.path.join(ROOT, 'data', 'figures.json')))
ASKS = json.load(open(os.path.join(ROOT, 'data', 'asks.json')))
e = H.escape

PARTNERS = [
    "Children&rsquo;s National Hospital",
    "Occupational Therapy Simulation Lab, Trinity Washington University",
    "Safe Kids Worldwide",
    "So Kids SOAR",
    "GW EMT Training Program",
    "University of the District of Columbia School of Nursing",
    "Catholic University Conway School of Nursing",
    "OSSE Advanced Technical Centers, Wards 5 and 8",
]

asks_html = "\n".join(
    f'''      <li class="ask">
        <div class="cost"><b>{e(a["cost"])}</b><span>{e(a["when"])}</span></div>
        <div class="what"><h3>{e(a["title"])}</h3><p>{e(a["body"])}</p></div>
      </li>''' for a in ASKS)

partners_html = "\n".join(f'        <li>{p}</li>' for p in PARTNERS)

MAILTO = f'mailto:{F["email"]}?subject={F["subject"].replace(" ", "%20")}'

PAGE = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>DC HOSA on the Hill</title>
<meta name="description" content="DC HOSA &mdash; Future Health Professionals: what a congressional office or institution can do for District health science students, and what it costs.">
<meta name="robots" content="index,follow">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<style>
:root{{
  --ground:#E9ECF1; --surface:#FBFCFE; --surface-2:#F1F4F8; --raise:#FFFFFF;
  --ink:#141C28; --ink-2:#414F66; --ink-3:#6C7B94;
  --line:#D3D9E3; --line-2:#E3E8EF;
  --maroon:#862633; --navy:#1B365D; --teal:#0E7C7B; --gold:#8E6A00;
  --on-maroon:#FFFFFF;
  --shadow:0 1px 2px rgba(20,28,40,.06), 0 10px 30px -16px rgba(20,28,40,.22);
}}
@media (prefers-color-scheme: dark){{
 :root:not([data-theme="light"]){{
  --ground:#0D131C; --surface:#151D29; --surface-2:#1B2432; --raise:#1E2836;
  --ink:#E7EBF2; --ink-2:#AAB6C8; --ink-3:#7C8AA1;
  --line:#2A3547; --line-2:#212B3A;
  --maroon:#D9808C; --navy:#86A8DA; --teal:#4FBEB7; --gold:#DCB350;
  --on-maroon:#1B0D10;
  --shadow:0 1px 2px rgba(0,0,0,.4), 0 10px 30px -16px rgba(0,0,0,.6);
 }}
}}
:root[data-theme="dark"]{{
  --ground:#0D131C; --surface:#151D29; --surface-2:#1B2432; --raise:#1E2836;
  --ink:#E7EBF2; --ink-2:#AAB6C8; --ink-3:#7C8AA1;
  --line:#2A3547; --line-2:#212B3A;
  --maroon:#D9808C; --navy:#86A8DA; --teal:#4FBEB7; --gold:#DCB350;
  --on-maroon:#1B0D10;
  --shadow:0 1px 2px rgba(0,0,0,.4), 0 10px 30px -16px rgba(0,0,0,.6);
}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--ground);color:var(--ink);
  font-family:"IBM Plex Sans","Helvetica Neue",Arial,sans-serif;font-size:16px;line-height:1.55;
  -webkit-font-smoothing:antialiased}}
img{{max-width:100%}}
a{{color:var(--teal)}}
:focus-visible{{outline:2px solid var(--teal);outline-offset:2px;border-radius:3px}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important;transition:none!important}}}}

.wrap{{max-width:940px;margin:0 auto;padding:0 24px 90px}}
.eyebrow{{font-family:"IBM Plex Mono",monospace;font-size:11px;font-weight:600;
  letter-spacing:.16em;text-transform:uppercase;color:var(--maroon);margin:0 0 16px}}

header.mast{{padding:52px 0 30px}}
h1{{font-family:"Instrument Serif",Georgia,serif;font-weight:400;
  font-size:clamp(34px,6vw,58px);line-height:1.02;letter-spacing:-.014em;margin:0;
  text-wrap:balance;max-width:17ch}}
.lede{{margin:18px 0 0;max-width:60ch;font-size:17px;color:var(--ink-2)}}

.numbers{{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));
  gap:0;margin:34px 0 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}}
.num{{padding:20px 24px 18px;border-right:1px solid var(--line-2)}}
.num:first-child{{padding-left:0}}
.num:last-child{{border-right:0}}
.num b{{display:block;font-family:"IBM Plex Mono",monospace;font-weight:600;font-size:34px;
  line-height:1;letter-spacing:-.03em;font-variant-numeric:tabular-nums;color:var(--navy)}}
.num span{{display:block;font-size:13px;color:var(--ink-3);margin-top:9px;max-width:24ch}}
.basis{{font-family:"IBM Plex Mono",monospace;font-size:11.5px;color:var(--ink-3);margin:12px 0 0}}

section{{padding-top:46px}}
h2{{font-family:"Instrument Serif",Georgia,serif;font-weight:400;font-size:30px;
  line-height:1.15;letter-spacing:-.01em;margin:0 0 6px}}
.sublede{{margin:0 0 22px;color:var(--ink-3);font-size:14.5px;max-width:62ch}}
p{{max-width:64ch}}

.two{{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:30px}}
.two p{{margin-top:0}}

ol.asks{{list-style:none;margin:0;padding:0;
  border:1px solid var(--line-2);border-radius:12px;overflow:hidden;background:var(--line-2);
  display:flex;flex-direction:column;gap:1px}}
.ask{{display:grid;grid-template-columns:168px 1fr;gap:22px;
  background:var(--surface);padding:20px 22px}}
.cost{{border-left:3px solid var(--maroon);padding-left:13px}}
.cost b{{display:block;font-family:"IBM Plex Mono",monospace;font-size:14px;font-weight:600;
  letter-spacing:-.01em}}
.cost span{{display:block;font-size:12px;color:var(--ink-3);margin-top:3px;
  letter-spacing:.03em;text-transform:uppercase}}
.ask h3{{margin:0 0 5px;font-size:16px;font-weight:600;letter-spacing:-.005em}}
.ask p{{margin:0;font-size:14.5px;color:var(--ink-2)}}
@media (max-width:620px){{
  .ask{{grid-template-columns:1fr;gap:12px}}
}}

.invest{{margin-top:46px;padding:26px 28px;background:var(--surface);
  border:1px solid var(--line-2);border-left:4px solid var(--gold);border-radius:10px;
  box-shadow:var(--shadow)}}
.invest h2{{font-size:25px;margin-bottom:12px}}
.invest p{{margin:0;color:var(--ink-2)}}

ul.partners{{list-style:none;margin:0;padding:0;
  display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:9px 26px}}
ul.partners li{{font-size:14.5px;color:var(--ink-2);
  padding-left:15px;position:relative}}
ul.partners li::before{{content:"";position:absolute;left:0;top:.62em;
  width:6px;height:6px;border-radius:50%;background:var(--teal)}}

.contact{{margin-top:46px;padding:30px 28px;background:var(--raise);
  border:1px solid var(--line);border-radius:12px;box-shadow:var(--shadow)}}
.contact h2{{margin-bottom:10px}}
.btnrow{{display:flex;flex-wrap:wrap;gap:11px;margin-top:20px;align-items:center}}
.btn{{display:inline-flex;align-items:center;gap:8px;padding:11px 18px;border-radius:9px;
  font-size:14.5px;font-weight:600;text-decoration:none;border:1px solid transparent}}
.btn-p{{background:var(--maroon);color:var(--on-maroon);border-color:var(--maroon)}}
.btn-p:hover{{filter:brightness(1.08)}}
.btn-s{{background:var(--surface-2);color:var(--ink-2);border-color:var(--line)}}
.btn-s:hover{{color:var(--ink);border-color:var(--ink-3)}}
.sig{{margin-top:22px;padding-top:18px;border-top:1px solid var(--line-2);font-size:14px}}
.sig b{{display:block;font-weight:600}}
.sig span{{display:block;color:var(--ink-3);font-size:13.5px}}
.sig span+span{{margin-top:2px}}

footer{{margin-top:56px;padding-top:22px;border-top:1px solid var(--line);
  color:var(--ink-3);font-size:12.5px;display:flex;gap:18px;flex-wrap:wrap;
  justify-content:space-between;align-items:baseline}}
footer .m{{font-family:"IBM Plex Mono",monospace;font-size:11.5px}}
</style>
</head>
<body>
<div class="wrap">

<header class="mast">
  <p class="eyebrow">DC HOSA &mdash; Future Health Professionals &middot; Chartered Association, District of Columbia</p>
  <h1>The District&rsquo;s next health workforce is already enrolled.</h1>
  <p class="lede">They are in District classrooms right now, learning to take vitals, run an emergency
  response, and read a chart. What they need from your office is access, not funding.</p>

  <div class="numbers">
    <div class="num"><b>{F["chapters"]}</b><span>{F["chapters_label"]}</span></div>
    <div class="num"><b>{F["members"]}</b><span>{F["members_label"]}</span></div>
    <div class="num"><b>{F["slc"]}</b><span>{F["slc_label"]}</span></div>
  </div>
  <p class="basis">{F["basis"]}</p>
</header>

<section>
  <h2>Who we are</h2>
  <div class="two">
    <p>DC HOSA is the District of Columbia&rsquo;s chartered association of HOSA &mdash; Future Health
    Professionals, a career and technical student organization serving students preparing for nursing,
    medicine, emergency response, public health, behavioral health, and allied health careers.</p>
    <p>Local Chapters sit inside District public, public charter, and independent schools. The association
    is run by an elected student officer team and supported by chapter advisors, some of whom teach
    health science courses full time. It operates under the sponsorship and oversight of the Office of
    the State Superintendent of Education and is not an independent legal entity.</p>
  </div>
</section>

<section>
  <h2>What membership looks like</h2>
  <div class="two">
    <p>Members compete in skill-based events judged by working clinicians and professionals, from
    emergency medical response to medical terminology to public health advocacy. They complete service
    hours that count toward the District&rsquo;s graduation service requirement.</p>
    <p>They also train outside the classroom, through partnerships that put students in simulation labs,
    clinical settings, and community health work before they finish high school.</p>
  </div>
</section>

<section>
  <h2>What your office can do</h2>
  <p class="sublede">Each option is built so that students carry the preparation and your office spends
  the least possible time. They are listed by what they cost you.</p>
  <ol class="asks">
{asks_html}
  </ol>
</section>

<div class="invest">
  <h2>Why this is a District investment</h2>
  <p>The region&rsquo;s hospitals, clinics, and public health agencies hire across state lines, and
  District students compete for those jobs from a standing start. Health science career and technical
  education is how that changes, and it remains one of the few areas of education policy with durable
  bipartisan support. In DC HOSA the structure already exists: fifteen schools, an elected student
  officer team, and a calendar that runs all year. What it needs from Congress is access.</p>
</div>

<section>
  <h2>Where our students already train</h2>
  <p class="sublede">Current partners.</p>
  <ul class="partners">
{partners_html}
  </ul>
</section>

<div class="contact">
  <h2>Start a conversation</h2>
  <p>Any of the options above can begin with one email. Tell us which one interests your office, or ask
  a question first &mdash; a student delegation is glad to answer it.</p>
  <div class="btnrow">
    <a class="btn btn-p" href="{MAILTO}">Email the State Advisor</a>
    <a class="btn btn-s" href="assets/leave-behind-front.pdf" target="_blank" rel="noopener">Leave-behind &mdash; front</a>
    <a class="btn btn-s" href="assets/leave-behind-back.pdf" target="_blank" rel="noopener">Leave-behind &mdash; back</a>
  </div>
  <div class="sig">
    <b>{F["advisor"]}</b>
    <span>{F["advisor_title"]}</span>
    <span>{F["social"]} &middot; dchosa.org</span>
  </div>
</div>

<footer>
  <span>DC HOSA &mdash; Future Health Professionals &middot; School year {F["year"]}</span>
  <span class="m">advocacy.dchosa.org</span>
</footer>

</div>
</body>
</html>
'''

open(os.path.join(ROOT, 'index.html'), 'w').write(PAGE)
print("bytes", len(PAGE), "| asks", len(ASKS), "| partners", len(PARTNERS))
