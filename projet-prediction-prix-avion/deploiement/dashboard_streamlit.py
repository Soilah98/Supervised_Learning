#  ── Imports ──

import joblib
import numpy as np
import pandas as pd
import streamlit as st
from pathlib import Path
import requests

# ── Configuration ──
st.set_page_config(
    page_title="Flight Price Finder",
    page_icon="✈️",
    layout="wide",
)

# ── CSS ──

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=Inter:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* ── fond général ── */
.stApp {
    background: #0b0f1a;
    color: #e8eaf0;
}

/* ── hero ── */
.hero {
    text-align: center;
    padding: 3rem 0 2rem;
}
.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: 3rem;
    font-weight: 800;
    letter-spacing: -1px;
    background: linear-gradient(135deg, #ffffff 0%, #7eb8f7 60%, #4f8ef0 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0;
}
.hero-sub {
    color: #6b7280;
    font-size: 1rem;
    font-weight: 300;
    margin-top: .4rem;
    letter-spacing: .5px;
}
.hero-badge {
    display: inline-block;
    background: rgba(79,142,240,.12);
    border: 1px solid rgba(79,142,240,.3);
    color: #7eb8f7;
    font-size: .75rem;
    font-weight: 500;
    padding: 4px 12px;
    border-radius: 999px;
    margin-bottom: 1.2rem;
    letter-spacing: .8px;
    text-transform: uppercase;
}

/* ── carte formulaire ── */
.form-card {
    background: #131827;
    border: 1px solid rgba(255,255,255,.07);
    border-radius: 20px;
    padding: 2rem 2rem 1.5rem;
    margin: 0 auto 2rem;
}
.form-section-label {
    font-size: .7rem;
    font-weight: 600;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    color: #4f8ef0;
    margin-bottom: .6rem;
}

/* ── widgets Streamlit ── */
div[data-testid="stSelectbox"] label,
div[data-testid="stSlider"] label,
div[data-testid="stNumberInput"] label,
div[data-testid="stSegmentedControl"] label {
    font-size: .8rem !important;
    font-weight: 500 !important;
    color: #9ca3af !important;
    letter-spacing: .3px;
}
div[data-testid="stSelectbox"] > div > div,
div[data-testid="stNumberInput"] input {
    background: #0d1220 !important;
    border: 1px solid rgba(255,255,255,.1) !important;
    border-radius: 10px !important;
    color: #e8eaf0 !important;
}
div[data-testid="stSelectbox"] > div > div:focus-within,
div[data-testid="stNumberInput"] input:focus {
    border-color: rgba(79,142,240,.5) !important;
    box-shadow: 0 0 0 3px rgba(79,142,240,.1) !important;
}

/* ── bouton ── */
.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #4f8ef0, #2563eb) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: .9rem 1.5rem !important;
    font-family: 'Syne', sans-serif !important;
    font-size: 1rem !important;
    font-weight: 700 !important;
    letter-spacing: .5px !important;
    transition: all .2s ease !important;
    box-shadow: 0 4px 20px rgba(37,99,235,.3) !important;
}
.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 8px 28px rgba(37,99,235,.45) !important;
}

/* ── résultat ── */
.result-card {
    background: linear-gradient(135deg, #131827 0%, #0f1a2e 100%);
    border: 1px solid rgba(79,142,240,.2);
    border-radius: 20px;
    padding: 2rem;
    position: relative;
    overflow: hidden;
}
.result-card::before {
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 200px; height: 200px;
    background: radial-gradient(circle, rgba(79,142,240,.08) 0%, transparent 70%);
    pointer-events: none;
}
.result-label {
    font-size: .7rem;
    font-weight: 600;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    color: #4f8ef0;
    margin-bottom: .5rem;
}
.price-inr {
    font-family: 'Syne', sans-serif;
    font-size: 3rem;
    font-weight: 800;
    color: #ffffff;
    line-height: 1;
    margin: 0;
}
.price-eur {
    font-size: 1.3rem;
    font-weight: 400;
    color: #7eb8f7;
    margin-top: .25rem;
}
.price-note {
    font-size: .75rem;
    color: #4b5563;
    margin-top: .5rem;
}
.divider {
    border: none;
    border-top: 1px solid rgba(255,255,255,.06);
    margin: 1.5rem 0;
}

/* ── pills ── */
.pill {
    display: inline-block;
    padding: 5px 12px;
    border-radius: 999px;
    background: rgba(255,255,255,.05);
    border: 1px solid rgba(255,255,255,.1);
    font-size: .78rem;
    color: #9ca3af;
    margin: 3px 4px 3px 0;
}
.pill-highlight {
    background: rgba(79,142,240,.12);
    border-color: rgba(79,142,240,.3);
    color: #7eb8f7;
}

/* ── badge confiance ── */
.conf-high   { background:rgba(16,185,129,.12); border:1px solid rgba(16,185,129,.3); color:#34d399; padding:6px 14px; border-radius:999px; font-size:.8rem; font-weight:500; display:inline-block; }
.conf-medium { background:rgba(245,158,11,.12); border:1px solid rgba(245,158,11,.3); color:#fbbf24; padding:6px 14px; border-radius:999px; font-size:.8rem; font-weight:500; display:inline-block; }
.conf-low    { background:rgba(239,68,68,.12);  border:1px solid rgba(239,68,68,.3);  color:#f87171; padding:6px 14px; border-radius:999px; font-size:.8rem; font-weight:500; display:inline-block; }

/* ── detail table ── */
.detail-card {
    background: #0d1220;
    border: 1px solid rgba(255,255,255,.07);
    border-radius: 16px;
    padding: 1.5rem;
    height: 100%;
}
.detail-title {
    font-size: .7rem;
    font-weight: 600;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    color: #4f8ef0;
    margin-bottom: 1rem;
}
.detail-row {
    display: flex;
    justify-content: space-between;
    padding: .45rem 0;
    border-bottom: 1px solid rgba(255,255,255,.04);
    font-size: .85rem;
}
.detail-row:last-child { border-bottom: none; }
.detail-key   { color: #6b7280; }
.detail-value { color: #e8eaf0; font-weight: 500; }

/* ── slider ── */
div[data-testid="stSlider"] > div > div > div {
    background: linear-gradient(to right, #4f8ef0, #2563eb) !important;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------- Chargement modèle -------------------

@st.cache_resource
def load_model():
    model_path = Path(__file__).parent.parent / "artifacts" / "flight_price_model.joblib"
    if not model_path.exists():
        st.error("Modèle introuvable — vérifie le chemin vers `artifacts/flight_price_model.joblib`.")
        st.stop()
    return joblib.load(model_path)

# ------------------Taux de change ----------------

@st.cache_data(ttl=3600)
def get_eur_rate():
    try:
        r = requests.get("https://api.exchangerate-api.com/v4/latest/INR", timeout=5)
        return r.json()["rates"]["EUR"]
    except Exception:
        return 0.011

model = load_model()

# ----------------------- Constantes -------------------------------
AIRLINES   = ['Vistara', 'Air_India', 'Indigo', 'GO_FIRST', 'AirAsia', 'SpiceJet']
CITIES     = ['Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai']
TIME_BANDS = ['Morning', 'Afternoon', 'Evening', 'Night', 'Early_Morning', 'Late_Night']
STOPS_MAP  = {"zero": 0, "one": 1, "two_or_more": 2}
CLASS_MAP  = {"Economy": 0, "Business": 1}

AIRLINE_FLAGS = {
    'Vistara': '🟣', 'Air_India': '🔴', 'Indigo': '🔵',
    'GO_FIRST': '🟠', 'AirAsia': '🔴', 'SpiceJet': '🟡'
}

# ----------------------- Fonctions helpers ---------------------------

def make_row(airline, source_city, dest_city, dep_time, arr_time, duration, days_left, stops, cls):
    # Valeur par défaut si None
    cls = cls or "Economy"
    stops = stops or "zero"
    
    return pd.DataFrame([{
        "airline": airline,
        "source_city": source_city,
        "destination_city": dest_city,
        "departure_time": dep_time,
        "arrival_time": arr_time,
        "duration": float(duration),
        "days_left": int(days_left),
        "stops_num": int(STOPS_MAP[stops]),
        "class_num": int(CLASS_MAP[cls]),
    }])

def fmt_inr(x):
    return f"₹ {float(x):,.0f}"

def get_confidence(model, X_input):
    rf   = model.named_steps["model"]
    prep = model.named_steps["preprocessor"]
    X_t  = prep.transform(X_input)
    preds = np.array([t.predict(X_t) for t in rf.estimators_]).flatten()
    mean, std = preds.mean(), preds.std()
    cv = std / mean if mean > 0 else 1
    if cv < 0.10:
        return "élevée", "conf-high", "●"
    elif cv < 0.20:
        return "moyenne", "conf-medium", "●"
    else:
        return "faible", "conf-low", "●"

# ---------------------------- Hero ----------------------------------

st.markdown("""
<div style="text-align:center; padding: 2.5rem 0 1.5rem;">
    <div style="
        display: inline-block;
        background: rgba(79,142,240,.12);
        border: 1px solid rgba(79,142,240,.3);
        color: #7eb8f7;
        font-size: .75rem;
        font-weight: 600;
        padding: 4px 14px;
        border-radius: 999px;
        margin-bottom: 1rem;
        letter-spacing: .8px;
        text-transform: uppercase;
    ">✈ Powered by Machine Learning</div>
    <br>
    <span style="
        font-size: 2.6rem;
        font-weight: 800;
        color: #ffffff;
        letter-spacing: -1px;
        display: block;
        margin-bottom: .4rem;
    ">Flight Price Finder</span>
    <span style="
        color: #6b7280;
        font-size: 1rem;
        font-weight: 300;
        letter-spacing: .3px;
    ">Estimez le prix de votre vol en Inde en quelques secondes</span>
</div>
""", unsafe_allow_html=True)

# ------------------------------ Formulaire --------------------------------

st.markdown('<div class="form-card">', unsafe_allow_html=True)

st.markdown('<div class="form-section-label">Trajet</div>', unsafe_allow_html=True)
c1, c2, c3 = st.columns([1.2, 1.2, 1], vertical_alignment="bottom")
with c1:
    source_city = st.selectbox("Ville de départ", CITIES, index=0)
with c2:
    dest_options = [c for c in CITIES if c != source_city]
    destination_city = st.selectbox("Ville d'arrivée", dest_options, index=0)
with c3:
    class_label = st.segmented_control(
                        "Classe",
                        options=["Economy", "Business"],
                        default="Economy",
                        selection_mode="single"  
                        )
if class_label is None:
    class_label = "Economy"
    
st.markdown('<div style="height:1px;background:rgba(255,255,255,.05);margin:1.2rem 0"></div>', unsafe_allow_html=True)
st.markdown('<div class="form-section-label">Vol</div>', unsafe_allow_html=True)

c4, c5, c6, c7 = st.columns([1, 1, 1, 1], vertical_alignment="bottom")
with c4:
    airline = st.selectbox("Compagnie", AIRLINES, index=0)
with c5:
    stops_label = st.selectbox("Escales", ["zero", "one", "two_or_more"], index=0,
                               format_func=lambda x: {"zero":"Sans escale","one":"1 escale","two_or_more":"2+ escales"}[x])
with c6:
    days_left = st.slider("Jours avant le vol", 1, 60, 15)
with c7:
    duration = st.number_input("Durée (heures)", min_value=0.5, max_value=60.0, value=2.5, step=0.5)

c8, c9 = st.columns(2, vertical_alignment="bottom")
with c8:
    departure_time = st.selectbox("Créneau départ", TIME_BANDS, index=0)
with c9:
    arrival_time = st.selectbox("Créneau arrivée", TIME_BANDS, index=2)

st.markdown("<div style='height:1.2rem'></div>", unsafe_allow_html=True)
run = st.button("✈  Estimer le prix", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------Résultats -------------------------------------

if run:
    if source_city == destination_city:
        st.warning("Départ et arrivée identiques — choisissez deux villes différentes.")
    else:
        X_input = make_row(airline, source_city, destination_city,
                           departure_time, arrival_time, duration,
                           days_left, stops_label, class_label)

        with st.spinner("Calcul en cours…"):
            try:
                pred = max(0.0, float(model.predict(X_input)[0]))
                rate = get_eur_rate()
                pred_eur = pred * rate
                conf_label, conf_cls, conf_dot = get_confidence(model, X_input)
            except Exception as e:
                st.error(f"Erreur lors de la prédiction : {e}")
                st.stop()

        left, right = st.columns([1.3, 0.9], gap="large")

        with left:
            st.markdown(f"""
            <div class="result-card">
              <div class="result-label">Prix estimé</div>
              <div class="price-inr">{fmt_inr(pred)}</div>
              <div class="price-eur">≈ {pred_eur:,.0f} €</div>
              <div class="price-note">Taux de change en temps réel · Roupies indiennes</div>
              <hr class="divider">
              <div style="margin-bottom:.6rem">
                <span class="{conf_cls}">{conf_dot} Confiance {conf_label}</span>
              </div>
              <div>
                <span class="pill pill-highlight">{source_city} → {destination_city}</span>
                <span class="pill">{AIRLINE_FLAGS.get(airline,'')} {airline}</span>
                <span class="pill">{'Sans escale' if stops_label=='zero' else stops_label}</span>
                <span class="pill">{class_label}</span>
                <span class="pill">⏱ {duration}h</span>
                <span class="pill">J-{days_left}</span>
                <span class="pill">↑ {departure_time}</span>
                <span class="pill">↓ {arrival_time}</span>
              </div>
            </div>
            """, unsafe_allow_html=True)

        with right:
            rows = {
                "Compagnie": f"{AIRLINE_FLAGS.get(airline,'')} {airline}",
                "Trajet": f"{source_city} → {destination_city}",
                "Classe": class_label,
                "Escales": stops_label,
                "Durée": f"{duration} h",
                "Jours avant vol": f"J-{days_left}",
                "Départ": departure_time,
                "Arrivée": arrival_time,
            }
            rows_html = "".join([
                f'<div class="detail-row"><span class="detail-key">{k}</span><span class="detail-value">{v}</span></div>'
                for k, v in rows.items()
            ])
            st.markdown(f"""
            <div class="detail-card">
              <div class="detail-title">Paramètres envoyés au modèle</div>
              {rows_html}
            </div>
            """, unsafe_allow_html=True)