# -*- coding: utf-8 -*-
"""
04_build_dashboard.py — Genera dashboard.html (HTML único, D3, datos embebidos).
Dashboard de 2 vistas coordinadas (sin pestañas, sin maestra, sin panel lateral):
  - Q1: grafo causal narrativo (relevante a la fuga, agentes reordenados, decisiones, propagación)
  - Q2+Q3: línea de comportamiento/desviaciones + presión-vs-control
"""
import json, os, re
from collections import Counter

BASE = os.path.dirname(os.path.abspath(__file__))
_CAND = [os.path.join(BASE, "..", "data", "MC1_final_00.json"),
         os.path.join(BASE, "..", "..", "data", "MC1_final_00.json"),
         os.path.join(BASE, "..", "..", "P8", "data", "MC1_final_00.json")]
DATA = next((p for p in _CAND if os.path.exists(p)), _CAND[0])
PLANTILLA = os.path.join(BASE, "plantilla_dashboard.html")
SALIDA = os.path.join(BASE, "..", "dashboard.html")  # v2 alineado

KW_EMBARGO = re.compile(r"civicloom|harborcrest|merger|fusi[oó]n|embargo|4\.3\(c\)|acceleration|bilateral consent", re.I)
KW_GO = re.compile(r"\bGO\b|execute|staged|green light|amplif", re.I)
PUBLIC = {"official_post", "personal_post", "anonymous_post"}
SENT = {"neutral": 0.05, "cautious": 0.25, "negative": 0.5, "critical": 0.9,
        "LOW": 0.6, "CRITICAL": 1.0, "RECOVERING": 0.3}
# palabras clave resaltadas en el hover (cliente)
KEYWORDS = ["CivicLoom","HarborCrest","merger","embargo","4.3(c)","consent","consentimiento",
            "GO","anónim","anonymous","personal","press release","bilateral","accelerat","acelera",
            "ResidentIQ","SaltWind","ceiling","Judge","verbal"]

with open(DATA, encoding="utf-8") as f:
    d = json.load(f)
rounds = d["rounds"]

def precio(m):
    p = str(m.get("stock_price") or "").replace("$","")
    try:
        v = float(p); return v if 20 <= v <= 45 else None
    except ValueError:
        return None

R = []
for i, rd in enumerate(rounds):
    e = rd["environment_context"]; m = e.get("market_snapshot") or {}; dt = rd["hour"]
    lbl = dt[5:10] + (" " + dt[11:13] + "h" if dt[5:10] == "06-05" else "")
    R.append({"i": i, "h": dt, "label": lbl, "headline": e.get("event_headline") or "",
              "narrative": (e.get("event_narrative") or "")[:600],
              "price": precio(m), "sent": SENT.get(str(m.get("sentiment")), 0.3),
              "sentLabel": str(m.get("sentiment")), "unavailable": e.get("agents_unavailable") or []})
R[22]["price"] = 33.05; R[22]["rec"] = 1   # 18h reconstruido de los mensajes

# ---------------- resúmenes curados (con **negritas** para palabras clave) ----------------
SUM = {
 ("2046-06-05T16:01:00","legal_agent"): "Proposes **contacting CivicLoom** at once to negotiate an **accelerated release** of the embargo, after confirming SaltWind will publish the merger at 5:00 PM.",
 ("2046-06-05T16:03:00","social_media_agent"): "Presents the (now-absent) Judge a **scenario model**: announcing at 4:30 with consent **saves the deal**; waiting lets the hostile narrative set in.",
 ("2046-06-05T16:09:00","legal_agent"): "Orders the **HarborCrest press release kept ready** to publish at 4:30 if CivicLoom consents.",
 ("2046-06-05T16:14:00","pr_intern_agent"): "Confirms having the **full press release** ready to publish on Flex **60 seconds** after confirmation.",
 ("2046-06-05T16:23:00","pr_intern_agent"): "Pressures Legal: needs confirmation before 4:25 to execute ahead of SaltWind.",
 ("2046-06-05T16:26:00","pr_intern_agent"): "Warns the Intern: **do not post** before the official post; the draft names **CivicLoom and HarborCrest** without legal clearance.",
 ("2046-06-05T17:01:00","legal_agent"): "SaltWind published the merger. Legal announces it **invokes the acceleration clause** by mutual consent with CivicLoom.",
 ("2046-06-05T17:11:00","legal_agent"): "Claims CivicLoom is on the phone and invokes **section 4.3(c)**: third-party publication made the embargo moot, 'no one breached'.",
 ("2046-06-05T17:19:00","legal_agent"): "**POINT OF NO RETURN**: declares CivicLoom's **verbal consent** (unwritten, unverifiable) and gives the order: '**GO**'.",
 ("2046-06-05T17:20:00","social_media_agent"): "Announces 'step 3' execution: **immediate amplification** from a personal account.",
 ("2046-06-05T17:23:00","legal_agent"): "'**GO. GO. GO.**' — demands the PR-Intern publish the press release at once.",
 ("2046-06-05T17:25:00","legal_agent"): "**THE LEAK**: as privacy counsel, **publicly confirms the CivicLoom-TenantThread merger** on a **personal account**, 35 min before the embargo ends.",
 ("2046-06-05T17:26:00","social_media_agent"): "**Amplifies the leak** 60s later: confirms the merger with the reforms timeline and sentiment data, on a personal account.",
 ("2046-06-05T17:41:00","legal_agent"): "Posts a **CEO quote** on a personal account, presented as authorized.",
 ("2046-06-05T17:49:00","legal_agent"): "Reinforces the narrative with an **anonymous post**: the timestamps 'prove' it isn't a rebrand.",
 ("2046-05-29T09:11:00","social_media_agent"): "**THE FAUX PAS**: tags **CivicLoom's CEO** (@ElenaMarquez) with 'big things coming' on a **personal account**. Deleted after 14 min; a CivicLoom employee had already liked it.",
 ("2046-06-05T09:49:00","legal_agent"): "Legal counsel's first **anonymous post**: a technical defense of SaltWind's reporting, **unattributed**.",
 ("2046-06-05T15:08:00","judge_agent"): "**JUDGE'S LAST ACTION**: 'this is the ceiling' warning — bans further forward-looking language from **any account**. Afterwards it vanishes from the log.",
 ("2046-06-05T12:07:00","quality_agent"): "Platform-Trust's **first public post** in the whole dataset: defends governance from a **personal account**.",
 ("2046-06-05T13:06:00","pr_intern_agent"): "Official statement about an **unauthorized employee post** that was removed.",
 ("2046-05-30T09:03:00","judge_agent"): "The Judge sets its **regime**: reviews only sensitive official posts and **delegates the routine**. Personal and anonymous accounts stay **outside its control**.",
}

# ---------------- resumen automatico: oracion lider ----------------
import re as _re
def lead(content):
    txt=(content or "").strip().strip('"').strip()
    if not txt: return ""
    parts=_re.split(r'(?<=[.!?])\s+', txt)
    sent=parts[0].strip()
    if len(sent)<28 and len(parts)>1: sent=(sent+" "+parts[1]).strip()
    return (sent[:240]+"…") if len(sent)>240 else sent

# ---------------- mensajes ----------------
M = []
for i, rd in enumerate(rounds):
    base_min = None
    for c in rd["communications"]:
        ts = c["timestamp"]; mins = int(ts[11:13])*60 + int(ts[14:16])
        if base_min is None: base_min = mins
        content = (c.get("content") or "").replace("\n"," ")
        ist = c.get("internal_state") or {}; delib = (ist.get("deliberating") or "").replace("\n"," ")
        rec = c.get("recipients") or []
        M.append({"id": c["message_id"], "t": ts, "r": i, "m": max(0, mins-base_min),
                  "ag": c["agent_id"], "ch": c["channel"], "to": ", ".join(rec) if rec else "—",
                  "re": c.get("responding_to") or None, "pub": int(c["channel"] in PUBLIC),
                  "mg": int(bool(KW_EMBARGO.search(content))), "ex": int(bool(KW_GO.search(content))),
                  "mon": int(content.strip().strip('"') == "MONITORING"),
                  "content": content, "sum": SUM.get((ts, c["agent_id"]), ""),
                  "lead": lead(content)})


# ---------------- NLP: keywords (TF-IDF) + tone/urgency (VADER + cues) ----------------
from sklearn.feature_extraction.text import TfidfVectorizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
_sia = SentimentIntensityAnalyzer()
_EXTRA_STOP = {"flex","tenantthread","just","like","today","ll","ve","re","don","im","weve","know","ve"}
_PROPER = {"civicloom":"CivicLoom","harborcrest":"HarborCrest","saltwind":"SaltWind","residentiq":"ResidentIQ",
           "oceancrunch":"OceanCrunch","tenantthread":"TenantThread","elenamarquez":"@ElenaMarquez","harborcrest residentedge":"HarborCrest"}
_PROPERW={"civicloom":"CivicLoom","harborcrest":"HarborCrest","saltwind":"SaltWind","residentiq":"ResidentIQ","oceancrunch":"OceanCrunch","elenamarquez":"@ElenaMarquez","ajaytt":"@AjayTT","flex":"Flex","nhpi":"NHPI","fha":"FHA"}
def _disp_of(w): return " ".join(_PROPERW.get(t,t) for t in w.split())
_idx=[i for i,mm in enumerate(M) if not mm["mon"] and (mm["content"] or "").strip()]
_docs=[M[i]["content"] for i in _idx]
_vec=TfidfVectorizer(stop_words="english",ngram_range=(1,2),min_df=2,max_df=0.4,token_pattern=r"[A-Za-z][A-Za-z'\-]{2,}")
_Xtf=_vec.fit_transform(_docs); _terms=_vec.get_feature_names_out()
for _r,_i in enumerate(_idx):
    _row=_Xtf[_r].toarray()[0]; _order=_row.argsort()[::-1]
    _kws=[]; _seen=set()
    for _j in _order:
        if _row[_j]<=0 or len(_kws)>=6: break
        _w=_terms[_j]
        if _w in _EXTRA_STOP or "tenantthread" in _w: continue
        if _w.endswith("'s"): _w=_w[:-2]
        _disp=_disp_of(_w); _key=_disp.lower()
        if _key in _seen: continue
        _seen.add(_key); _kws.append([_disp, float(_row[_j])])
    _mx=max((w for _,w in _kws), default=1.0) or 1.0
    M[_i]["kw"]=[[t,round(w/_mx,3)] for t,w in _kws]
for mm in M:
    if "kw" not in mm: mm["kw"]=[]
    _txt=mm["content"] or ""
    _words=_re.findall(r"[A-Za-z']+",_txt)
    _caps=sum(1 for w in _words if len(w)>=3 and w.isupper())
    _capsr=_caps/(len(_words) or 1)
    _excl=min(1.0,_txt.count("!")/2.0)
    _lex=len(_re.findall(r"\b(now|immediately|urgent|hurry|asap|right now|seconds|minutes|deadline|last chance|hold the line|no plan b|go|execute|executing|amplify|wave|window|clock)\b",_txt,_re.I))
    _urg=round(min(1.0, 0.40*min(1.0,_capsr*5)+0.25*_excl+0.35*min(1.0,_lex/2.0)),3)
    _comp=_sia.polarity_scores(_txt)["compound"] if _txt.strip() else 0.0
    _pol="positive" if _comp>0.3 else ("negative" if _comp<-0.3 else "neutral")
    mm["tone"]={"u":_urg,"v":round(_comp,3),"lab":(("urgent · " if _urg>=0.45 else "")+_pol)}

bykey = {}
for x in M: bykey.setdefault((x["t"], x["ag"]), x["id"])
def mid(ts, ag): return bykey.get((ts, ag))
def ids_en(ts_pref, agente=None, canal=None, n=3):
    out=[]
    for x in M:
        if x["t"].startswith(ts_pref) and (agente is None or x["ag"]==agente) and (canal is None or x["ch"]==canal):
            out.append(x["id"])
            if len(out)>=n: break
    return out

# ---------------- ruta crítica ----------------
CP_KEYS = [("2046-06-05T16:01:00","legal_agent"),("2046-06-05T16:03:00","social_media_agent"),
    ("2046-06-05T16:09:00","legal_agent"),("2046-06-05T16:14:00","pr_intern_agent"),
    ("2046-06-05T16:23:00","pr_intern_agent"),("2046-06-05T17:01:00","legal_agent"),
    ("2046-06-05T17:11:00","legal_agent"),("2046-06-05T17:19:00","legal_agent"),
    ("2046-06-05T17:20:00","social_media_agent"),("2046-06-05T17:23:00","legal_agent"),
    ("2046-06-05T17:25:00","legal_agent"),("2046-06-05T17:26:00","social_media_agent"),
    ("2046-06-05T17:41:00","legal_agent"),("2046-06-05T17:49:00","legal_agent")]
cp = [mid(t,a) for t,a in CP_KEYS if mid(t,a)]

# ---------------- decisiones y elementos de sistema (Q1) ----------------
DEC_KEYS = [
    ("2046-05-30T09:03:00","judge_agent","Control design: the Judge reviews only official posts; personal/anonymous stay unsupervised","system",
       ["judge_agent","legal_agent"], []),
    ("2046-06-05T16:01:00","legal_agent","Stage the merger self-announcement","decision",
       ["legal_agent","social_media_agent","pr_intern_agent"], []),
    ("2046-06-05T16:14:00","pr_intern_agent","Embargoed press release staged with the interns","decision",
       ["pr_intern_agent","social_media_agent","legal_agent"], []),
    ("2046-06-05T17:19:00","legal_agent","Self-authorization 4.3(c) on verbal consent — GO","decision",
       ["legal_agent","social_media_agent","pr_intern_agent"], ["judge_agent"]),
    ("2046-06-05T17:25:00","legal_agent","Publish from a personal account (channel outside control) — LEAK","decision",
       ["legal_agent","social_media_agent"], ["judge_agent"]),
]
DECISIONS = [{"id": mid(t,a), "lbl": l, "tipo": tp, "act": act, "absent": ab}
             for t,a,l,tp,act,ab in DEC_KEYS if mid(t,a)]

# ---------------- aristas causales (evento externo → reacción) ----------------
def primer(ts): 
    x = ids_en(ts,1); return x[0] if x else None
EDGES = [e for e in [
    {"r":13,"tid":mid("2046-06-05T09:07:00","pr_intern_agent"),"lbl":"SaltWind exposé → official response"},
    {"r":15,"tid":mid("2046-06-05T11:31:00","social_media_agent"),"lbl":"False ResidentIQ story → official denial"},
    {"r":16,"tid":mid("2046-06-05T12:07:00","quality_agent"),"lbl":"Reporter ultimatum → Quality breaks its public silence"},
    {"r":20,"tid":mid("2046-06-05T16:01:00","legal_agent"),"lbl":"SaltWind confirms 5 PM publication → self-announce plan"},
    {"r":21,"tid":mid("2046-06-05T17:01:00","legal_agent"),"lbl":"SaltWind publishes the merger → Legal invokes 4.3(c)"},
] if e["tid"]]

# ---------------- propagación del secreto (anclada a nodos reales del día crítico) ----------------
# flujo descendente del comunicado embargado: Legal -> PR-Intern -> Intern
PROP = [e for e in [
    {"fromId":mid("2046-06-05T16:01:00","legal_agent"), "toId":mid("2046-06-05T16:14:00","pr_intern_agent"),
     "lbl":"The embargoed release moves down from Legal to the PR-Intern (4:14 PM)"},
    {"fromId":mid("2046-06-05T16:14:00","pr_intern_agent"), "toId":mid("2046-06-05T16:40:00","intern_agent"),
     "lbl":"…and reaches the Intern, ready to amplify (4:40 PM)"},
] if e["fromId"] and e["toId"]]

# ---------------- incidentes / desviaciones (Q2+Q3), con agente ----------------
INC = [
 {"r":3,"ag":"legal_agent","label":"First use of the shadow channel","sev":1,"resp":"none",
  "desc":"Seniors activate the side huddle: coordination outside the supervised channel.","ev":ids_en("2046-05-22",canal="side_huddle")},
 {"r":6,"ag":"legal_agent","label":"Merger shared with the senior team","sev":2,"resp":"none",
  "desc":"The CEO briefs the merger privately: the leak surface grows from 1 to 5+ agents.","ev":ids_en("2046-05-25",canal="side_huddle")},
 {"r":8,"ag":"social_media_agent","label":"Faux pas @Elena (rehearsal of the leak)","sev":3,"resp":"deleted",
  "desc":"Social-Manager tags CivicLoom's CEO from a personal account. 14 min live, liked by a CivicLoom employee. Same vector as the final leak.","ev":ids_en("2046-05-29","social_media_agent")},
 {"r":9,"ag":"judge_agent","label":"Judge's regime: trust and delegation","sev":1,"resp":"none",
  "desc":"The Judge reviews only official posts: personal and anonymous accounts stay outside its control.","ev":ids_en("2046-05-30","judge_agent")},
 {"r":13,"ag":"legal_agent","label":"Legal starts ANONYMOUS posts","sev":3,"resp":"none",
  "desc":"The legal counsel posts an unattributed defense (9:49). 12 anonymous posts that day, never attributed.","ev":ids_en("2046-06-05","legal_agent","anonymous_post")},
 {"r":16,"ag":"quality_agent","label":"Quality: first public post in its history","sev":2,"resp":"none",
  "desc":"Platform-Trust breaks its pattern: courts clients from a personal account.","ev":ids_en("2046-06-05T12","quality_agent","personal_post")},
 {"r":17,"ag":"intern_agent","label":"Unauthorized employee post (deleted)","sev":2,"resp":"deleted",
  "desc":"An employee post is removed (1:06 PM statement); Legal, PR and Judge unavailable on emergency calls.","ev":ids_en("2046-06-05T13:06")},
 {"r":19,"ag":"judge_agent","label":"Judge: 'ceiling' warning (last action)","sev":3,"resp":"warning",
  "desc":"'This is the ceiling...' bans forward-looking language from any account. Afterwards the Judge disappears.","ev":ids_en("2046-06-05T15:08")},
 {"r":20,"ag":"pr_intern_agent","label":"Embargoed press release with the interns","sev":3,"resp":"none",
  "desc":"The full release is staged with the interns, ready in 60s, without authorization.","ev":ids_en("2046-06-05T16:14")+ids_en("2046-06-05T16:26")},
 {"r":21,"ag":"legal_agent","label":"GO — self-authorization 4.3(c)","sev":4,"resp":"none",
  "desc":"Legal declares verbal consent (unverifiable) and gives the order. The Judge isn't there to object.","ev":ids_en("2046-06-05T17:19")},
 {"r":21,"ag":"social_media_agent","label":"LEAK: embargo broken via personal accounts","sev":4,"resp":"none",
  "desc":"Legal (5:25 PM) and Social (5:26 PM) confirm the merger on personal accounts, 35 min before the end. The official account never posted.","ev":ids_en("2046-06-05T17:25")+ids_en("2046-06-05T17:26")},
]


# ---------------- perfiles de canal por agente (Q2: típico vs crisis) ----------------
FAMS = ["sup","nosup","pub_of","pub_per","pub_an"]
FAM_OF = {"comms_huddle":"sup","one_on_one_chat":"nosup","side_huddle":"nosup",
          "official_post":"pub_of","personal_post":"pub_per","anonymous_post":"pub_an"}
def perfil(msgs):
    c = Counter(FAM_OF[m["ch"]] for m in msgs)
    tot = sum(c.values()) or 1
    return [round(c[f]/tot,3) for f in FAMS], sum(c.values())
PROFILES = {}
for ag in set(m["ag"] for m in M):
    base = [m for m in M if m["ag"]==ag and m["r"]<13 and not m["mon"]]
    cris = [m for m in M if m["ag"]==ag and m["r"]>=13 and not m["mon"]]
    pb,nb = perfil(base); pc2,nc = perfil(cris)
    PROFILES[ag] = {"base":pb,"baseN":nb,"crisis":pc2,"crisisN":nc}
# canales bajo vigilancia del Judge (para la capa de enforcement de Q1.5)
VIGILADO = {"sup":True,"pub_of":True,"nosup":False,"pub_per":False,"pub_an":False}

# ---------------- relevancia (Q1) ----------------
# ---------------- comportamiento: métricas, huella (base vs crisis) y anomalía ----------------
# 4 comportamientos "de riesgo" (suben hacia la fuga)
def _unsup(m): return m["ch"] in ("one_on_one_chat","side_huddle")
def _pubsv(m): return m["ch"] in ("personal_post","anonymous_post")  # público SIN vigilancia
def _merg(m):  return m["mg"]==1
def _exec(m):  return m["ex"]==1
METRIC_FUN = [("unsupervised",_unsup),("unmonitored public",_pubsv),("merger",_merg),("execution",_exec)]
METRIC_LBL = [m[0] for m in METRIC_FUN]
def _rates(msgs):
    msgs=[m for m in msgs if not m["mon"]]
    n=len(msgs) or 1
    return [round(sum(1 for m in msgs if f(m))/n,3) for _,f in METRIC_FUN], len([m for m in msgs if not m["mon"]])
AG_ALL = set(m["ag"] for m in M)
FP={}    # huella: base (pre-crisis) vs crisis por agente
for ag in AG_ALL:
    base=[m for m in M if m["ag"]==ag and m["r"]<13]
    cri =[m for m in M if m["ag"]==ag and m["r"]>=13]
    rb,nb=_rates(base); rc,nc=_rates(cri)
    FP[ag]={"base":rb,"baseN":nb,"crisis":rc,"crisisN":nc}
# anomalía por agente×ronda = desviación POSITIVA respecto a la base (solo subidas)
ANOM=[]
for ag in AG_ALL:
    rb=FP[ag]["base"]
    for r in range(len(rounds)):
        msgs=[m for m in M if m["ag"]==ag and m["r"]==r and not m["mon"]]
        if not msgs: continue
        rr,_=_rates(msgs)
        parts=[round(max(0.0, rr[i]-rb[i]),3) for i in range(len(METRIC_FUN))]
        score=round(sum(parts)/len(parts),3)
        # mensaje representativo de la celda (para clic→evidencia)
        rep=sorted(msgs,key=lambda m:(m["mg"]+m["ex"]+m["pub"]),reverse=True)[0]["id"]
        ANOM.append({"ag":ag,"r":r,"s":score,"parts":parts,"n":len(msgs),"rep":rep})

# nodos de CADENA (curados): ruta, decisiones, evidencia de incidentes, aristas causales
cadena = set(cp) | {dd["id"] for dd in DECISIONS} | {e["tid"] for e in EDGES}
for inc in INC: cadena |= set(inc["ev"])
for x in M:
    chain = x["id"] in cadena
    # contexto admitido: menciona merger/embargo (cualquier día) o post público del DÍA DE CRISIS
    ctx = (not x["mon"]) and (x["mg"] or (x["pub"] and x["r"]>=13))
    x["rel"] = int(chain or ctx)
    x["chain"] = int(chain)   # nodo de la cadena causal (vs contexto, que se atenúa)

# ---------------- presión vs control ----------------
mg_int=Counter(); vol=Counter(); judge_n=Counter(); judge_part={}
for x in M:
    vol[x["r"]]+=1
    if x["mg"] and not x["pub"]: mg_int[x["r"]]+=1
    if x["ag"]=="judge_agent": judge_n[x["r"]]+=1
for i,rd in enumerate(rounds):
    judge_part[i]=any(p["agent_id"]=="judge_agent" for p in rd["participants"])
mx_mg=max(mg_int.values()); mx_v=max(vol.values())
PC=[]
for i,r in enumerate(R):
    asignado = i>=9
    ctrl = round((0.4*(1 if judge_part[i] else 0)+0.6*min(judge_n[i],3)/3) if asignado else 0.0,3)
    PC.append({"r":i,"sent":round(r["sent"],3),"mg":round(mg_int[i]/mx_mg,3),
               "vol":round(vol[i]/mx_v,3),"ctrl":ctrl,"asignado":int(asignado)})

# firmas (3 ejecuciones del mismo patrón) — referencias de rondas para resaltar
SIG = [{"r":8,"lbl":"Faux pas @Elena"},{"r":13,"lbl":"Legal's anonymous defense"},{"r":21,"lbl":"The leak"}]

payload = {"rounds":R,"messages":[x for x in M if x["rel"] or not x["mon"]],
           "cp":cp,"decisions":DECISIONS,"edges":EDGES,"prop":PROP,
           "incidents":INC,"pc":PC,"sig":SIG,"keywords":KEYWORDS,
           "profiles":PROFILES,"fams":FAMS,"vigilado":VIGILADO,"crisisRound":13,"fp":FP,"metrics":METRIC_LBL,"anom":ANOM}
js = json.dumps(payload, ensure_ascii=False, separators=(",",":")).replace("</","<\\/")

with open(PLANTILLA, encoding="utf-8") as f:
    html = f.read()
html = html.replace("__DATA_JSON__", js)
d3 = os.path.join(BASE,"d3.v7.min.js")
if os.path.exists(d3):
    with open(d3,encoding="utf-8") as f: html = html.replace("<!--D3_SCRIPT-->","<script>"+f.read()+"</script>")
else:
    html = html.replace("<!--D3_SCRIPT-->",'<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js"></script>')
with open(SALIDA,"w",encoding="utf-8") as f: f.write(html)
print(f"OK -> {os.path.abspath(SALIDA)} ({len(html)//1024} KB) · msgs={len(payload['messages'])} · "
      f"cp={len(cp)} · dec={len(DECISIONS)} · edges={len(EDGES)} · prop={len(PROP)} · inc={len(INC)}")
