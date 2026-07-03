# HarborCrest Inspector
### VAST Challenge 2026 · Mini-Challenge 1 — final visual solution

> **Was the embargo breach a deliberate leak, or did the control system collapse under pressure?**
> **Verdict: both.** A deliberate, coordinated leak by the *Legal* and *Social-Manager* agents — possible only
> because the control ("the Judge") was absent during the decisive window and, by design, never watched personal
> or anonymous accounts.

A forensic visual-analytics system over **912 messages from 7 AI communication agents** at TenantThread, covering
the two weeks before the Project HarborCrest merger leaked (5:25 PM, June 5, 2046 — 35 minutes before the embargo).

---

## ▶ View the project

| File | What it is |
|---|---|
| **`index.htm`** | Start here — the **analytical answers** to the VAST questions (Q1/Q2/Q3), insights and methods. |
| **`dashboard.html`** | The **interactive visual system** (two coordinated panels). Opens by double-click; D3.js is embedded, so it **runs offline**. |

**Local:** download the repo and open `index.htm` (or `dashboard.html`) in any modern browser.
**Online (optional):** enable GitHub Pages (*Settings → Pages → deploy from `main` / root*) and the project is served at
`https://<user>.github.io/<repo>/`.

---

## 🧭 What the system shows

**Panel 1 · The leak chain (Q1)** — a swimlane flow: time on X (semantic zoom onto the crisis hours), agents on Y,
the critical path highlighted, decisions as labeled nodes, cause→reaction and secret-propagation arrows, and a
control-status band that turns empty exactly across the leak window.

**Panel 2 · Behavior & control (Q2 + Q3)** — an anomaly heatmap (agent × round) plus a footprint dumbbell
(typical → crisis) over four risk behaviors, incident markers with the institutional-response color, three
repeated-pattern signatures, a severity-vs-response gap, and governance bands (market sentiment, Judge surveillance).

A single color language runs through both panels: **red = threat/severity · teal = control/response · gray = context**.

---

## 🔑 Answers in one paragraph

- **Q1 — sequence & decisions:** SaltWind's reporting + the CEO's escalating private pressure set the stage; with the
  Judge gone after 3:08 PM, Legal staged a press release, self-authorized a release via §4.3(c) on *unverifiable verbal
  consent* ("GO", 5:19 PM), and published the merger from a **personal account** at 5:25 PM, amplified by Social-Manager.
- **Q2 — typical vs. deviant:** agents normally talk in **monitored** channels; on June 5 Legal & Social-Manager migrate
  to **personal/anonymous** channels with merger talk and execution language. The control system deviates by *collapsing*;
  the CEO escalates from vague encouragement to an operational countdown.
- **Q3 — leading indicators:** eleven precursor incidents and a full rehearsal (the May 29 faux pas) preceded the leak;
  no structural action followed because the institutional response was always cosmetic (delete/warn), never structural.

Full, evidence-backed answers are in **`index.htm`** and **`reportes/02_Respuestas_MC1.md`**.

---

## ⚙ Reproduce the dashboard

```bash
cd scripts
python 04_build_dashboard.py      # reads ../data/MC1_final_00.json and regenerates ../dashboard.html
```

**Requirements:** Python 3 with `scikit-learn` and `vaderSentiment` (used for the build-time NLP).

```bash
pip install scikit-learn vaderSentiment
```

The builder injects the data and the embedded D3 library into `scripts/plantilla_dashboard.html` to produce a
single self-contained `dashboard.html`.

---

## 📁 Repository structure

```
.
├── index.htm                     # analytical answers (submission entry point)
├── dashboard.html                 # final interactive visual system (self-contained)
├── README.md
├── data/
│   ├── MC1_final_00.json           # source dataset
│   └── mc1 data description.md     # data dictionary
├── scripts/
│   ├── 04_build_dashboard.py       # builds dashboard.html from the data
│   ├── plantilla_dashboard.html    # D3 template (the visualization code)
│   └── d3.v7.min.js                # embedded charting library (offline)
└── reportes/
    ├── 02_Respuestas_MC1.md        # detailed analytical answers (ES)
    └── 05_Guion_Exposicion_Detallado.md  # full design justification + demo script (ES)
```

---

## 🧪 Method & honesty

The system is a transparent **hybrid**: the narrative scaffolding we verified (critical path, decisions, incidents,
signatures) is **analyst-curated**, while behavior is **computed** — an anomaly metric (deviation from each agent's
pre-crisis baseline) and build-time **NLP** over all 912 messages (TF-IDF keywords for the per-node word cloud,
lead-sentence summaries, an urgency signal). We state which is which rather than claim the system discovers the whole
narrative on its own.

---

*Course project · VAST Challenge 2026 · Mini-Challenge 1 — forensic visual analytics for the CivicLoom legal team.*
