# HarborCrest Inspector — VAST Challenge 2026, Mini-Challenge 1

This repository contains our submission for VAST Challenge 2026, Mini-Challenge 1. It is a forensic
visual-analytics system that examines the two weeks of AI-agent communications leading up to the Project
HarborCrest embargo breach, and answers whether the release was a deliberate leak or a collapse of the
control system.

There are two entry points. `index.htm` is the answer form: it holds our written responses to the three
challenge questions together with the accompanying figures, and it opens in any browser. `dashboard.html`
is the interactive visual system, two coordinated panels ("The leak chain" and "Behavior & control") built
with D3.js. It is self-contained (the library is embedded), so it runs offline and opens with a double
click, without a server or an internet connection.

## Repository structure

```
index.htm         Answer form: responses to the three questions plus figures
dashboard.html    Interactive visual system (self-contained, opens offline)
data/             Source dataset (MC1_final_00.json) and its data dictionary
scripts/          Build pipeline that generates the dashboard from the data
reportes/         Supporting analysis notes and the presentation guide (Spanish)
```

## Reproducing the dashboard

The dashboard is generated from the source data by a single script. From the repository root:

```
cd scripts
pip install scikit-learn vaderSentiment
python 04_build_dashboard.py
```

The script reads `data/MC1_final_00.json`, computes the behavioral metrics and the build-time NLP
(TF-IDF keywords and a tone/urgency signal), and injects them, together with the embedded D3 library,
into `plantilla_dashboard.html` to produce the self-contained `dashboard.html`. No web server is required.

All data is fully synthetic and provided by the VAST Challenge.
