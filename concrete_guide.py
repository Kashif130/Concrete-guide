import streamlit as st

# ─── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Concrete 101 — The Complete Guide",
    page_icon="🗿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700;900&family=Share+Tech+Mono&family=Syne:wght@700;800&display=swap');

:root {
    --bg-deep:    #05080D;
    --bg-panel:   #090D14;
    --bg-card:    #0C1018;
    --border:     #131B25;
    --border-glow:#1E2D40;
    --neon:       #00FFB2;
    --neon-dim:   #00FFB240;
    --neon-glow:  #00FFB215;
    --gold:       #EDD97A;
    --gold-dim:   #EDD97A40;
    --amber:      #E8A020;
    --red:        #FF3D5A;
    --blue:       #4DA6FF;
    --purple:     #9B59FF;
    --orange:     #FF7A2F;
    --text-primary: #E8F0F8;
    --text-mid:   #556070;
    --text-dim:   #2A3540;
}

html, body, [class*="css"] {
    font-family: 'Share Tech Mono', monospace;
    background: var(--bg-deep);
    color: var(--text-primary);
}

.stApp { background: var(--bg-deep); }
.block-container { padding: 1rem 1.5rem 2rem; max-width: 1400px; }

/* Sidebar */
section[data-testid="stSidebar"] {
    background: var(--bg-panel) !important;
    border-right: 1px solid var(--border) !important;
}
section[data-testid="stSidebar"] * {
    color: var(--text-primary) !important;
    font-family: 'Share Tech Mono', monospace !important;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    background: var(--bg-panel);
    border-bottom: 1px solid var(--border);
    gap: 2px;
    padding: 4px 4px 0;
    flex-wrap: wrap;
}
.stTabs [data-baseweb="tab"] {
    background: transparent;
    color: var(--text-mid);
    border: 1px solid var(--border);
    border-bottom: none;
    border-radius: 4px 4px 0 0;
    font-family: 'Orbitron', monospace;
    font-size: 9px;
    letter-spacing: 2px;
    padding: 8px 14px;
    transition: all 0.2s;
}
.stTabs [aria-selected="true"] {
    background: var(--neon-glow) !important;
    color: var(--neon) !important;
    border-color: var(--neon) !important;
    font-weight: 700 !important;
    box-shadow: 0 0 12px var(--neon-dim) !important;
}

/* Expanders */
.streamlit-expanderHeader {
    background: var(--bg-card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 6px !important;
    color: var(--text-mid) !important;
    font-family: 'Share Tech Mono', monospace !important;
}

/* Metrics */
[data-testid="stMetric"] {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 16px 20px;
}
[data-testid="stMetricLabel"] { font-size: 9px !important; letter-spacing: 3px !important; color: var(--text-dim) !important; }
[data-testid="stMetricValue"] { font-size: 22px !important; font-weight: 700 !important; color: var(--neon) !important; font-family: 'Orbitron', monospace !important; }

hr { border-color: var(--border) !important; margin: 12px 0 !important; }

.guide-card {
    background: var(--bg-card);
    border: 1px solid var(--border-glow);
    border-radius: 10px;
    padding: 20px 24px;
    margin-bottom: 16px;
}
.guide-card-gold {
    background: linear-gradient(135deg, #0C1018, #12100A);
    border: 1px solid var(--gold-dim);
    border-radius: 10px;
    padding: 20px 24px;
    margin-bottom: 16px;
}
.guide-card-neon {
    background: linear-gradient(135deg, #0C1018, #051210);
    border: 1px solid var(--neon-dim);
    border-radius: 10px;
    padding: 20px 24px;
    margin-bottom: 16px;
}
.step-badge {
    display: inline-block;
    background: var(--neon-glow);
    border: 1px solid var(--neon);
    color: var(--neon);
    font-family: 'Orbitron', monospace;
    font-size: 10px;
    padding: 4px 12px;
    border-radius: 4px;
    margin-right: 10px;
    letter-spacing: 2px;
}
.level-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 16px;
    border-bottom: 1px solid var(--border);
    font-size: 13px;
}
.level-row:last-child { border-bottom: none; }
.level-reward {
    display: inline-block;
    background: #EDD97A15;
    border: 1px solid var(--gold-dim);
    color: var(--gold);
    font-size: 11px;
    padding: 3px 10px;
    border-radius: 4px;
}
.tag-neon { display:inline-block; background:#00FFB210; border:1px solid #00FFB233; color:var(--neon); padding:2px 10px; border-radius:4px; font-size:11px; margin:3px; }
.tag-gold { display:inline-block; background:#EDD97A10; border:1px solid #EDD97A33; color:var(--gold); padding:2px 10px; border-radius:4px; font-size:11px; margin:3px; }
.tag-red  { display:inline-block; background:#FF3D5A10; border:1px solid #FF3D5A33; color:var(--red); padding:2px 10px; border-radius:4px; font-size:11px; margin:3px; }
.tag-blue { display:inline-block; background:#4DA6FF10; border:1px solid #4DA6FF33; color:var(--blue); padding:2px 10px; border-radius:4px; font-size:11px; margin:3px; }

.vault-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 16px;
    margin-bottom: 12px;
}
.warning-box {
    background: #FF3D5A08;
    border: 1px solid #FF3D5A40;
    border-radius: 8px;
    padding: 16px 20px;
    margin: 12px 0;
}
.tip-box {
    background: var(--neon-glow);
    border: 1px solid var(--neon-dim);
    border-radius: 8px;
    padding: 14px 18px;
    margin: 10px 0;
    font-size: 13px;
}

/* Language toggle button styling */
.lang-toggle-container {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 16px;
}
</style>
""", unsafe_allow_html=True)

# ─── Language System ───────────────────────────────────────────────────────────
if "lang" not in st.session_state:
    st.session_state.lang = "en"

def t(en_text, ur_text):
    """Return English or Urdu text based on current language setting."""
    if st.session_state.lang == "ur":
        return ur_text
    return en_text

# ─── Header + Language Toggle ─────────────────────────────────────────────────
header_col, toggle_col = st.columns([5, 1])

with header_col:
    st.markdown(f"""
<div style="text-align:center; padding: 30px 0 20px;">
    <div style="font-family:'Orbitron',monospace; font-size:42px; font-weight:900; color:#00FFB2; letter-spacing:6px; text-shadow: 0 0 40px #00FFB260;">
        🗿 CONCRETE 101
    </div>
    <div style="font-family:'Share Tech Mono',monospace; font-size:14px; color:#EDD97A; letter-spacing:4px; margin-top:8px;">
        {t("THE COMPLETE BEGINNER GUIDE — VAULTS · XP · ROLES · MOAI · BADGES",
           "مکمل ابتدائی گائیڈ — والٹس · XP · رولز · موآئی · بیجز")}
    </div>
    <div style="font-size:11px; color:#2A3540; letter-spacing:2px; margin-top:6px;">
        {t("written by community · for community · one team. one vision.",
           "کمیونٹی کی طرف سے · کمیونٹی کے لیے · ایک ٹیم۔ ایک وژن۔")}
    </div>
</div>
""", unsafe_allow_html=True)

with toggle_col:
    st.markdown("<div style='padding-top:36px;'></div>", unsafe_allow_html=True)
    current_lang = st.session_state.lang
    btn_label = "🇵🇰 اردو" if current_lang == "en" else "🇬🇧 English"
    btn_help = "Switch to Urdu" if current_lang == "en" else "Switch to English"
    if st.button(btn_label, help=btn_help, use_container_width=True):
        st.session_state.lang = "ur" if current_lang == "en" else "en"
        st.rerun()

st.markdown("---")

# ─── Sidebar Nav ───────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(f"""
    <div style="font-family:'Orbitron',monospace; font-size:11px; color:#00FFB2; letter-spacing:3px; margin-bottom:16px;">
    🗿 CONCRETE GUIDE
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="font-size:11px; color:#556070; line-height:1.8; margin-bottom:20px;">
    📌 {t("Quick Links:", "فوری لنکس:")}
    </div>
    """, unsafe_allow_html=True)

    links = {
        "🏠 concrete.xyz": "https://concrete.xyz",
        "📘 Docs": "https://docs.concrete.xyz",
        "⭐ Points": "https://points.concrete.xyz",
        "🌿 Ecosystem": "https://concrete.xyz/ecosystem",
        "📊 Vault Tool": "https://concrete-vault.streamlit.app",
    }
    for label, url in links.items():
        st.markdown(f'<a href="{url}" target="_blank" style="display:block; color:#EDD97A; font-size:11px; text-decoration:none; padding:6px 0; border-bottom:1px solid #131B25;">{label}</a>', unsafe_allow_html=True)

    st.markdown("---")

    # Language toggle in sidebar too
    st.markdown(f"""
    <div style="font-family:'Orbitron',monospace; font-size:10px; color:#00FFB2; letter-spacing:2px; margin-bottom:8px;">
    🌐 {t("LANGUAGE", "زبان")}
    </div>
    """, unsafe_allow_html=True)

    lang_col1, lang_col2 = st.columns(2)
    with lang_col1:
        en_style = "background:#00FFB215; border:1px solid #00FFB2; color:#00FFB2;" if st.session_state.lang == "en" else "background:transparent; border:1px solid #131B25; color:#556070;"
        if st.button("🇬🇧 EN", use_container_width=True):
            st.session_state.lang = "en"
            st.rerun()
    with lang_col2:
        ur_style = "background:#00FFB215; border:1px solid #00FFB2; color:#00FFB2;" if st.session_state.lang == "ur" else "background:transparent; border:1px solid #131B25; color:#556070;"
        if st.button("🇵🇰 UR", use_container_width=True):
            st.session_state.lang = "ur"
            st.rerun()

    st.markdown(f"""
    <div style="font-size:10px; color:#2A3540; letter-spacing:2px; line-height:1.8; margin-top:12px;">
    ⚠ {t("NOT FINANCIAL ADVICE", "مالی مشورہ نہیں")}<br>
    {t("COMMUNITY TOOL", "کمیونٹی ٹول")}<br>
    {t("DYOR BEFORE INVESTING", "سرمایہ کاری سے پہلے تحقیق کریں")}
    </div>
    """, unsafe_allow_html=True)

# ─── Main Tabs ─────────────────────────────────────────────────────────────────
tab_labels = [
    t("🚀 START HERE", "🚀 یہاں شروع کریں"),
    t("🏦 VAULTS 101", "🏦 والٹس 101"),
    t("🔑 ACCESS ROLES", "🔑 رولز"),
    t("🏆 XP & POINTS", "🏆 XP اور پوائنٹس"),
    t("🗿 MOAI & BADGES", "🗿 موآئی اور بیجز"),
    t("📝 ARTICLES", "📝 آرٹیکلز"),
    t("🛠️ VAULT TOOL", "🛠️ والٹ ٹول"),
    t("🔑 KEY CONDITIONS", "🔑 کلید شرائط"),
    t("✍️ WRITE GUIDE", "✍️ لکھنے کی گائیڈ"),
    t("😂 MEMES GUIDE", "😂 میمز گائیڈ"),
    t("🐦 TWITTER GUIDE", "🐦 ٹوئٹر گائیڈ"),
    t("❓ FAQ", "❓ سوال جواب"),
]

tabs = st.tabs(tab_labels)
tab_start, tab_vaults, tab_roles, tab_xp, tab_moai, tab_articles, tab_tool, tab_key, tab_write, tab_memes, tab_twitter, tab_faq = tabs

# ════════════════════════════════════════════════════════════════
# TAB 1 — START HERE
# ════════════════════════════════════════════════════════════════
with tab_start:
    st.markdown(f"""
    <div style="font-family:'Orbitron',monospace; font-size:13px; color:#556070; letter-spacing:3px; margin-bottom:20px;">
    👋 {t("WELCOME TO CONCRETE LAND", "کنکریٹ لینڈ میں خوش آمدید")}
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(t("Protocol", "پروٹوکول"), "Concrete.XYZ", "ERC-4626 Vaults")
    with col2:
        st.metric(t("Chain", "چین"), "Ethereum Mainnet", t("Live & Audited", "لائیو اور آڈیٹڈ"))
    with col3:
        st.metric(t("Community", "کمیونٹی"), t("Growing Fast", "تیزی سے بڑھ رہی ہے"), t("Join Discord", "ڈسکورڈ جوائن کریں"))

    st.markdown("---")

    st.markdown(f"""
    <div class="guide-card-neon">
        <div style="font-family:'Orbitron',monospace; font-size:12px; color:#00FFB2; letter-spacing:3px; margin-bottom:14px;">
        🧱 {t("WHAT IS CONCRETE?", "کنکریٹ کیا ہے؟")}
        </div>
        <div style="font-size:13px; color:#E8F0F8; line-height:2;">
        {t(
            'Concrete is a <b style="color:#00FFB2;">DeFi yield protocol</b> that automatically deploys your capital into the best strategies — Aave V3, Morpho, Silo, Radiant.<br><br>You deposit into a vault → Concrete manages that capital → you earn yield.<br><br>Simple. Efficient. Protected. 🗿',
            'کنکریٹ ایک <b style="color:#00FFB2;">DeFi yield protocol</b> ہے جو آپ کا سرمایہ خودکار طور پر بہترین حکمت عملیوں میں لگاتا ہے — Aave V3, Morpho, Silo, Radiant۔<br><br>آپ ایک والٹ میں ڈپازٹ کرتے ہیں → کنکریٹ وہ سرمایہ منظم کرتا ہے → آپ yield کماتے ہیں۔<br><br>سادہ۔ موثر۔ محفوظ۔ 🗿'
        )}
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"### 🗺️ {t('Roadmap for Beginners', 'نئے لوگوں کے لیے روڈ میپ')}")

    steps = [
        (t("STEP 1", "مرحلہ 1"), t("Join Discord", "ڈسکورڈ جوائن کریں"),
         t("Join the Concrete community — this is where XP starts. Chat, engage, learn.", "کنکریٹ کمیونٹی جوائن کریں — یہاں سے XP ملنا شروع ہوتا ہے۔ چیٹ کریں، مشغول ہوں، سیکھیں۔"),
         "#00FFB2"),
        (t("STEP 2", "مرحلہ 2"), t("Visit concrete.xyz", "concrete.xyz وزٹ کریں"),
         t("Go to the official website, explore vaults, read docs. Get familiar with everything.", "آفیشل ویب سائٹ پر جائیں، والٹس دیکھیں، دستاویزات پڑھیں۔"),
         "#EDD97A"),
        (t("STEP 3", "مرحلہ 3"), t("Use the Vault Tool", "والٹ ٹول استعمال کریں"),
         t("Use our community-built Vault Intelligence Terminal — see APY, understand risk, simulate.", "ہمارا کمیونٹی والٹ ٹول استعمال کریں — APY دیکھیں، خطرہ سمجھیں، سمیولیٹ کریں۔"),
         "#4DA6FF"),
        (t("STEP 4", "مرحلہ 4"), t("Earn XP", "XP کمائیں"),
         t("Chat, write articles, earn badges — Level 5 gets you Newbie Role (50 BAGS reward!).", "چیٹ کریں، آرٹیکل لکھیں، بیجز لیں — لیول 5 پر Newbie Role ملتی ہے (50 BAGS انعام!)۔"),
         "#9B59FF"),
        (t("STEP 5", "مرحلہ 5"), t("Deposit (DYOR)", "ڈپازٹ کریں (DYOR)"),
         t("When ready, deposit in a vault. Start small. Understand the risks.", "جب تیار ہوں، والٹ میں ڈپازٹ کریں۔ چھوٹی رقم سے شروع کریں۔ خطرات سمجھیں۔"),
         "#E8A020"),
    ]

    for step, title, desc, color in steps:
        st.markdown(f"""
        <div class="guide-card" style="border-color:{color}30; border-left: 3px solid {color};">
            <div style="display:flex; align-items:center; gap:12px; margin-bottom:8px;">
                <span style="font-family:'Orbitron',monospace; font-size:10px; color:{color}; background:{color}15; border:1px solid {color}33; padding:4px 10px; border-radius:4px; letter-spacing:2px;">{step}</span>
                <span style="font-family:'Orbitron',monospace; font-size:13px; color:{color}; font-weight:700;">{title}</span>
            </div>
            <div style="font-size:12px; color:#556070; line-height:1.8;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="tip-box">
    💡 <b>{t("Pro Tip:", "پرو ٹِپ:")}</b> {t(
        "Staying active on the Concrete Discord is the most important thing — XP comes from there, the community is there, and the latest updates come from there.",
        "کنکریٹ Discord پر فعال رہنا سب سے اہم ہے — XP وہاں سے ملتا ہے، کمیونٹی وہاں ہے، اور تازہ ترین اپڈیٹس بھی وہاں آتی ہیں۔"
    )}
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════
# TAB 2 — VAULTS 101
# ════════════════════════════════════════════════════════════════
with tab_vaults:
    st.markdown(f"""
    <div style="font-family:'Orbitron',monospace; font-size:13px; color:#556070; letter-spacing:3px; margin-bottom:20px;">
    🏦 {t("VAULTS — START UNDERSTANDING", "والٹس — سمجھنا شروع کریں")}
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="guide-card-neon">
        <div style="font-family:'Orbitron',monospace; font-size:12px; color:#00FFB2; margin-bottom:12px; letter-spacing:2px;">
        {t("WHAT IS AN ERC-4626 VAULT?", "ERC-4626 والٹ کیا ہوتا ہے؟")}
        </div>
        <div style="font-size:13px; color:#E8F0F8; line-height:2.0;">
        {t(
            'ERC-4626 is an Ethereum standard for yield-bearing vaults.<br>You deposit <b style="color:#00FFB2;">WETH, USDC, weETH</b> → the vault gives you <b style="color:#EDD97A;">ct[Asset] tokens</b> → these tokens automatically increase in value as yield is earned.<br><br>Never need to manually harvest anything. Compounding is automatic.',
            'ERC-4626 ایک Ethereum معیار ہے yield-bearing والٹس کے لیے۔<br>آپ <b style="color:#00FFB2;">WETH, USDC, weETH</b> ڈپازٹ کرتے ہیں → والٹ آپ کو <b style="color:#EDD97A;">ct[Asset] tokens</b> دیتا ہے → ان ٹوکنز کی قیمت خودکار طور پر بڑھتی رہتی ہے جیسے yield ملتی ہے۔<br><br>کبھی manually کچھ حاصل نہیں کرنا۔ Compound خودکار ہے۔'
        )}
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"### 📦 {t('Available Vaults', 'دستیاب والٹس')}")

    vaults = [
        {
            "name": "🏦 WeETH (Institutional)",
            "asset": "WETH",
            "apy": "~7.84%",
            "strategy": t("Institutional Restaking — Aave V3 + Silo", "انسٹی ٹیوشنل ری اسٹیکنگ — Aave V3 + Silo"),
            "risk": t("LOW", "کم"),
            "risk_color": "#00FFB2",
            "tvl": "$281M+",
            "desc": t(
                "Safest vault. Institutional-grade restaking strategy. Best for long-term holders.",
                "سب سے محفوظ والٹ۔ انسٹی ٹیوشنل ری اسٹیکنگ حکمت عملی۔ طویل مدتی ہولڈرز کے لیے بہترین۔"
            )
        },
        {
            "name": "💎 USDC Yield",
            "asset": "USDC",
            "apy": "~9.10%",
            "strategy": t("Stablecoin Multi-Strategy — Morpho + Aave", "Stablecoin ملٹی اسٹریٹجی — Morpho + Aave"),
            "risk": t("LOW-MED", "کم-درمیانہ"),
            "risk_color": "#EDD97A",
            "tvl": "$134M+",
            "desc": t(
                "Yield on a stable asset. No impermanent loss. Perfect for conservative investors.",
                "مستحکم اثاثے پر yield۔ Impermanent loss نہیں۔ محتاط سرمایہ کاروں کے لیے بہترین۔"
            )
        },
        {
            "name": "🔥 WETH Alpha",
            "asset": "WETH",
            "apy": "~11.2%",
            "strategy": t("Aggressive Restaking — Radiant + Silo", "جارحانہ ری اسٹیکنگ — Radiant + Silo"),
            "risk": t("MEDIUM", "درمیانہ"),
            "risk_color": "#E8A020",
            "tvl": "$89M+",
            "desc": t(
                "Higher APY, higher risk. Active monitoring recommended.",
                "زیادہ APY، زیادہ خطرہ۔ فعال نگرانی کی سفارش۔"
            )
        },
        {
            "name": "⚡ cbBTC Vault",
            "asset": "cbBTC",
            "apy": "~6.50%",
            "strategy": t("BTC Yield — Morpho Blue", "BTC Yield — Morpho Blue"),
            "risk": t("LOW-MED", "کم-درمیانہ"),
            "risk_color": "#EDD97A",
            "tvl": "$45M+",
            "desc": t(
                "Yield for Bitcoin holders. Conservative strategy on wrapped BTC.",
                "بٹ کوئن ہولڈرز کے لیے yield۔ Wrapped BTC پر محتاط حکمت عملی۔"
            )
        },
    ]

    for v in vaults:
        col_a, col_b = st.columns([3, 1])
        with col_a:
            st.markdown(f"""
            <div class="vault-card">
                <div style="display:flex; align-items:center; gap:16px; margin-bottom:10px; flex-wrap:wrap;">
                    <span style="font-family:'Orbitron',monospace; font-size:14px; color:#E8F0F8; font-weight:700;">{v['name']}</span>
                    <span style="font-family:'Orbitron',monospace; font-size:13px; color:#00FFB2;">{v['apy']} APY</span>
                    <span style="font-size:11px; color:{v['risk_color']}; background:{v['risk_color']}15; border:1px solid {v['risk_color']}33; padding:2px 8px; border-radius:4px;">{v['risk']}</span>
                </div>
                <div style="font-size:11px; color:#556070; margin-bottom:6px;">📋 {t('Strategy', 'حکمت عملی')}: {v['strategy']}</div>
                <div style="font-size:11px; color:#556070; margin-bottom:6px;">💰 TVL: {v['tvl']} &nbsp;|&nbsp; 🪙 {t('Asset', 'اثاثہ')}: {v['asset']}</div>
                <div style="font-size:12px; color:#E8F0F8; margin-top:8px;">{v['desc']}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown(f"### 💡 {t('How to Deposit — Step by Step', 'ڈپازٹ کیسے کریں — مرحلہ بہ مرحلہ')}")

    deposit_steps_en = [
        "Open **concrete.xyz** in your browser",
        "**Connect Wallet** (MetaMask or Coinbase Wallet)",
        "Select your **asset** (WETH, USDC, etc.)",
        "**Enter amount** — start with a small amount",
        "Sign the **Approve** transaction (one-time per token)",
        "**Deposit** — ct[Asset] tokens will arrive in your wallet",
        "**ct token value** grows automatically — nothing else to do!",
    ]
    deposit_steps_ur = [
        "**concrete.xyz** براؤزر میں کھولیں",
        "**والٹ کنیکٹ** کریں (MetaMask یا Coinbase Wallet)",
        "اپنا **اثاثہ** منتخب کریں (WETH, USDC، وغیرہ)",
        "**رقم درج کریں** — چھوٹی رقم سے شروع کریں",
        "**Approve** ٹرانزیکشن سائن کریں (ہر ٹوکن کے لیے ایک بار)",
        "**ڈپازٹ** کریں — ct[Asset] ٹوکنز آپ کے والٹ میں آ جائیں گے",
        "**ct ٹوکنز کی قیمت** خودکار بڑھتی ہے — کچھ اور کرنے کی ضرورت نہیں!",
    ]
    deposit_steps = deposit_steps_en if st.session_state.lang == "en" else deposit_steps_ur

    for i, s in enumerate(deposit_steps, 1):
        st.markdown(f"""
        <div style="display:flex; gap:14px; align-items:flex-start; padding:10px 0; border-bottom:1px solid #131B25;">
            <span style="font-family:'Orbitron',monospace; font-size:11px; color:#00FFB2; background:#00FFB210; border:1px solid #00FFB233; padding:3px 8px; border-radius:4px; min-width:28px; text-align:center;">{i}</span>
            <span style="font-size:13px; color:#E8F0F8; line-height:1.6;">{s}</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown(f"""
    <div class="guide-card-gold">
        <div style="font-family:'Orbitron',monospace; font-size:12px; color:#EDD97A; margin-bottom:10px; letter-spacing:2px;">🪙 {t("WHAT IS A CT[ASSET] TOKEN?", "CT[ASSET] ٹوکن کیا ہوتا ہے؟")}</div>
        <div style="font-size:13px; color:#E8F0F8; line-height:2.0;">
        {t(
            'When you deposit, the vault gives you <b style="color:#EDD97A;">ct[Asset]</b> tokens (e.g., ctWETH, ctUSDC).<br><br>• These tokens are ERC-20 — you can transfer, hold, or sell them<br>• Their value <b>automatically appreciates</b> (vault earns yield)<br>• When withdrawing, burn these tokens and get the underlying asset back<br>• <b style="color:#EDD97A;">No claiming. No compounding button. Set and forget!</b>',
            'جب آپ ڈپازٹ کرتے ہیں، والٹ آپ کو <b style="color:#EDD97A;">ct[Asset]</b> ٹوکنز دیتا ہے (مثلاً ctWETH, ctUSDC)۔<br><br>• یہ ٹوکنز ERC-20 ہیں — ٹرانسفر، ہولڈ، یا بیچ سکتے ہیں<br>• ان کی قیمت <b>خودکار بڑھتی</b> ہے (والٹ yield کماتا ہے)<br>• نکالتے وقت ان ٹوکنز کو burn کریں اور بنیادی اثاثہ واپس لیں<br>• <b style="color:#EDD97A;">کوئی claiming نہیں۔ کوئی compounding بٹن نہیں۔ لگاؤ اور بھول جاؤ!</b>'
        )}
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="warning-box">
    ⚠️ <b style="color:#FF3D5A;">{t("RISK REMINDER:", "خطرے کی یاددہانی:")}</b> {t(
        "DeFi carries risk. Smart contract bugs, liquidation, market volatility — all are possible. Only deposit what you can afford to lose. DYOR. This is not financial advice.",
        "DeFi میں خطرہ ہوتا ہے۔ Smart contract bugs، لیکویڈیشن، مارکیٹ کا اتار چڑھاؤ — سب ممکن ہے۔ صرف وہ رقم ڈپازٹ کریں جو آپ کھونے کی استطاعت رکھتے ہیں۔ یہ مالی مشورہ نہیں ہے۔"
    )}
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════
# TAB 3 — ACCESS ROLES
# ════════════════════════════════════════════════════════════════
with tab_roles:
    st.markdown(f"""
    <div style="font-family:'Orbitron',monospace; font-size:13px; color:#556070; letter-spacing:3px; margin-bottom:20px;">
    🔑 {t("ACCESS ROLES — HOW TO UNLOCK", "رولز — کیسے انلاک کریں")}
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="guide-card-neon">
        <div style="font-size:13px; color:#E8F0F8; line-height:2.0;">
        {t(
            'Concrete Discord has <b style="color:#00FFB2;">roles</b> that define your status and access.<br>Earn XP → Level up → Unlock special roles and channels.',
            'کنکریٹ Discord پر <b style="color:#00FFB2;">رولز</b> ہوتے ہیں جو آپ کی حیثیت اور رسائی متعین کرتے ہیں۔<br>XP کمائیں → لیول اپ کریں → خصوصی رولز اور چینلز انلاک کریں۔'
        )}
        </div>
    </div>
    """, unsafe_allow_html=True)

    roles = [
        {
            "name": "👶 Newcomer",
            "unlock": t("Given upon joining Discord", "Discord جوائن کرتے ہی ملتی ہے"),
            "level": t("Level 1", "لیول 1"),
            "perks": [
                t("Basic channels access", "بنیادی چینلز تک رسائی"),
                t("Community chat", "کمیونٹی چیٹ"),
                t("Start earning XP", "XP کمانا شروع کریں"),
            ],
            "color": "#556070"
        },
        {
            "name": "🗿 Newbie",
            "unlock": t("Level 5 — 380 XP", "لیول 5 — 380 XP"),
            "level": t("Level 5", "لیول 5"),
            "perks": [
                t("Newbie Role + 50 BAGS reward!", "Newbie Role + 50 BAGS انعام!"),
                t("More channels access", "زیادہ چینلز تک رسائی"),
                t("Community recognized member", "کمیونٹی میں پہچانا گیا رکن"),
            ],
            "color": "#4DA6FF"
        },
        {
            "name": "🧭 Vault Navigator",
            "unlock": t("Level 10 — 955 XP", "لیول 10 — 955 XP"),
            "level": t("Level 10", "لیول 10"),
            "perks": [
                t("Vault Navigator Role + 150 BAGS!", "Vault Navigator Role + 150 BAGS!"),
                t("Vault discussions access", "والٹ مباحثوں تک رسائی"),
                t("Early protocol updates", "پروٹوکول اپڈیٹس جلدی"),
            ],
            "color": "#00FFB2"
        },
        {
            "name": "☘️ Lucky 17",
            "unlock": t("Level 17 — 2180 XP", "لیول 17 — 2180 XP"),
            "level": t("Level 17", "لیول 17"),
            "perks": [
                t("Lucky 17 Role + 250 BAGS!", "Lucky 17 Role + 250 BAGS!"),
                t("Exclusive community events", "خصوصی کمیونٹی ایونٹس"),
                t("Special Discord channels", "خصوصی Discord چینلز"),
            ],
            "color": "#EDD97A"
        },
        {
            "name": "🏆 Grindooor",
            "unlock": t("Level 25 — 4180 XP", "لیول 25 — 4180 XP"),
            "level": t("Level 25", "لیول 25"),
            "perks": [
                t("Grindooor Role + 1000 BAGS!", "Grindooor Role + 1000 BAGS!"),
                t("Top community member status", "سرفہرست کمیونٹی رکن"),
                t("Maximum perks and recognition", "زیادہ سے زیادہ مراعات اور پہچان"),
            ],
            "color": "#E8A020"
        },
        {
            "name": "📝 Writer / Contributor",
            "unlock": t("Submit a quality article", "معیاری آرٹیکل جمع کرائیں"),
            "level": t("Merit-based", "میرٹ بنیاد پر"),
            "perks": [
                t("Writer badge", "Writer بیج"),
                t("Extra XP per article", "فی آرٹیکل اضافی XP"),
                t("Community visibility", "کمیونٹی میں نمایاں"),
            ],
            "color": "#9B59FF"
        },
    ]

    for r in roles:
        with st.expander(f"{r['name']} — {r['level']}"):
            col_x, col_y = st.columns([2, 1])
            with col_x:
                st.markdown(f"""
                <div style="font-size:13px; color:{r['color']}; font-family:'Orbitron',monospace; margin-bottom:10px;">{t("Unlock:", "انلاک:")} {r['unlock']}</div>
                <div style="font-size:13px; color:#E8F0F8; margin-bottom:8px;"><b>{t("Perks:", "فوائد:")}</b></div>
                """, unsafe_allow_html=True)
                for perk in r['perks']:
                    st.markdown(f"✅ {perk}")
            with col_y:
                st.markdown(f"""
                <div style="text-align:center; padding:20px;">
                    <div style="font-size:40px;">{r['name'].split()[0]}</div>
                    <div style="font-family:'Orbitron',monospace; font-size:10px; color:{r['color']}; margin-top:8px; letter-spacing:2px;">{r['level'].upper()}</div>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown(f"""
    <div class="guide-card-gold">
        <div style="font-family:'Orbitron',monospace; font-size:12px; color:#EDD97A; margin-bottom:10px; letter-spacing:2px;">💰 {t("WHAT ARE BAGS?", "BAGS کیا ہیں؟")}</div>
        <div style="font-size:13px; color:#E8F0F8; line-height:2.0;">
        {t(
            "BAGS is Concrete's community reward currency. Earned by leveling up.<br><br>• <b style='color:#EDD97A;'>50 BAGS</b> — Level 5 (Newbie Role)<br>• <b style='color:#EDD97A;'>150 BAGS</b> — Level 10 (Vault Navigator)<br>• <b style='color:#EDD97A;'>250 BAGS</b> — Level 17 (Lucky 17)<br>• <b style='color:#EDD97A;'>1000 BAGS</b> — Level 25 (Grindooor)<br><br>Exact utility will be announced in the future — keep holding!",
            "BAGS کنکریٹ کی کمیونٹی ریوارڈ کرنسی ہے۔ لیول اپ کرنے پر ملتی ہے۔<br><br>• <b style='color:#EDD97A;'>50 BAGS</b> — لیول 5 (Newbie Role)<br>• <b style='color:#EDD97A;'>150 BAGS</b> — لیول 10 (Vault Navigator)<br>• <b style='color:#EDD97A;'>250 BAGS</b> — لیول 17 (Lucky 17)<br>• <b style='color:#EDD97A;'>1000 BAGS</b> — لیول 25 (Grindooor)<br><br>مستقبل میں utility کا اعلان ہوگا — رکھے رہیں!"
        )}
        </div>
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════
# TAB 4 — XP & POINTS
# ════════════════════════════════════════════════════════════════
with tab_xp:
    st.markdown(f"""
    <div style="font-family:'Orbitron',monospace; font-size:13px; color:#556070; letter-spacing:3px; margin-bottom:20px;">
    🏆 {t("XP SYSTEM & DISCORD POINTS — LEVEL UP", "XP سسٹم اور ڈسکورڈ پوائنٹس — لیول اپ کریں")}
    </div>
    """, unsafe_allow_html=True)

    # Points banner
    st.markdown(f"""
    <div style="background:linear-gradient(135deg,#12100A,#0C1018); border:1px solid #EDD97A40; border-radius:10px; padding:18px 24px; margin-bottom:18px; display:flex; align-items:center; gap:16px; flex-wrap:wrap;">
        <div style="font-family:'Orbitron',monospace; font-size:28px; color:#EDD97A; font-weight:900;">+50 pts</div>
        <div>
            <div style="font-family:'Orbitron',monospace; font-size:13px; color:#00FFB2; letter-spacing:2px; margin-bottom:4px;">{t("CONCRETEXY Z DISCORD POINTS & REWARDS","کنکریٹXYZ ڈسکورڈ پوائنٹس اور ریوارڈز")}</div>
            <div style="font-size:12px; color:#556070;">{t("+ Earn More By Leveling Up!","+ لیول اپ کر کے مزید کمائیں!")}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Elite Tier + Milestone side by side
    ec1, ec2 = st.columns(2)
    with ec1:
        st.markdown(f"""
        <div class="guide-card-gold">
            <div style="font-family:'Orbitron',monospace; font-size:12px; color:#EDD97A; margin-bottom:12px; letter-spacing:2px;">🌿 {t("ELITE TIER — MOAIS","ایلیٹ ٹیئر — موآئیز")}</div>
            <div style="font-size:13px; color:#E8F0F8; line-height:2.2;">
            ✅ {t("Awarded end of season","سیزن کے آخر میں دیا جاتا ہے")}<br>
            ✅ {t("Must use Concrete DeFi tag","Concrete DeFi ٹیگ استعمال کرنا لازم")}<br>
            ✅ {t("Reserved for top contributors","صرف سرفہرست حصہ داروں کے لیے")}<br><br>
            <span style="color:#00FFB2;">#{t("announcements","اعلانات")}</span> {t("for more info","مزید معلومات کے لیے")}
            </div>
        </div>
        """, unsafe_allow_html=True)
    with ec2:
        st.markdown(f"""
        <div class="guide-card-neon">
            <div style="font-family:'Orbitron',monospace; font-size:12px; color:#EDD97A; margin-bottom:12px; letter-spacing:2px;">🏆 {t("MILESTONE REWARDS","سنگ میل ریوارڈز")}</div>
            <div style="font-size:13px; color:#E8F0F8; line-height:2.2;">
            ✅ {t("Level 5","لیول 5")} — <span style="color:#00FFB2;">Newbie: <b>+50 pts</b></span><br>
            ✅ {t("Level 10","لیول 10")} — <span style="color:#4DA6FF;">Vault Navigator: <b>+150 pts</b></span><br>
            ✅ {t("Level 17","لیول 17")} — <span style="color:#9B59FF;">Lucky 17: <b>+250 pts</b></span><br>
            ✅ {t("Level 25","لیول 25")} — <span style="color:#EDD97A;">Grindoor: <b style="font-size:16px;">+1000 pts</b></span><br>
            <span style="font-size:11px; color:#556070;">({t("End of Season Reward","سیزن کے آخر کا انعام")})</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="guide-card-neon">
        <div style="font-size:13px; color:#E8F0F8; line-height:2.0;">
        {t(
            'On Concrete Discord, <b style="color:#00FFB2;">chatting earns XP</b>. The more you engage, the more XP you get, the more you level up. At certain levels you unlock <b style="color:#EDD97A;">special roles + pts milestone rewards</b>.',
            'کنکریٹ Discord پر <b style="color:#00FFB2;">چیٹ کرنے سے XP ملتا ہے</b>۔ جتنا مشغول ہوں، اتنا XP، اتنا لیول اپ۔ کچھ لیولز پر <b style="color:#EDD97A;">خصوصی رولز + pts سنگ میل ریوارڈز</b> ملتے ہیں۔'
        )}
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"### 📊 {t('Complete Level Table', 'مکمل لیول ٹیبل')}")

    levels_data = [
        (1, 100, None, None),
        (2, 155, None, None),
        (3, 220, None, None),
        (4, 295, None, None),
        (5, 380, t("🗿 NEWBIE ROLE", "🗿 نیوبی رول"), "50 BAGS"),
        (6, 475, None, None),
        (7, 580, None, None),
        (8, 695, None, None),
        (9, 820, None, None),
        (10, 955, t("🧭 VAULT NAVIGATOR", "🧭 والٹ نیویگیٹر"), "150 BAGS"),
        (11, 1100, None, None),
        (12, 1250, None, None),
        (13, 1420, None, None),
        (14, 1590, None, None),
        (15, 1780, None, None),
        (16, 1980, None, None),
        (17, 2180, t("☘️ LUCKY 17 ROLE", "☘️ لکی 17 رول"), "+250 pts"),
        (18, 2400, None, None),
        (19, 2620, None, None),
        (20, 2850, None, None),
        (21, 3620, None, None),
        (22, 3900, None, None),
        (23, 3620, None, None),
        (24, 3900, None, None),
        (25, 4180, t("🏆 GRINDOOR ROLE", "🏆 گرنڈور رول"), "+1000 pts"),
    ]

    st.markdown(f"""
    <div style="background:var(--bg-card); border:1px solid var(--border); border-radius:10px; overflow:hidden; margin-bottom:20px;">
        <div style="display:flex; padding:12px 16px; background:#090D14; border-bottom:1px solid #1E2D40; font-family:'Orbitron',monospace; font-size:10px; color:#2A3540; letter-spacing:2px;">
            <span style="width:80px;">{t("LEVEL", "لیول")}</span>
            <span style="width:120px;">{t("XP NEEDED", "ضروری XP")}</span>
            <span style="flex:1;">{t("MILESTONE", "سنگ میل")}</span>
            <span style="width:120px;">{t("REWARD", "انعام")}</span>
        </div>
    """, unsafe_allow_html=True)

    for lvl, xp, role, bags in levels_data:
        is_milestone = role is not None
        row_bg = "#12100A" if is_milestone else "transparent"
        lvl_color = "#EDD97A" if is_milestone else "#556070"
        xp_color = "#00FFB2" if is_milestone else "#E8F0F8"
        role_html = f'<span style="font-size:11px; color:#EDD97A; background:#EDD97A10; border:1px solid #EDD97A33; padding:2px 8px; border-radius:4px;">{role}</span>' if role else '<span style="color:#2A3540; font-size:11px;">—</span>'
        bags_html = f'<span style="font-size:11px; color:#E8A020; font-weight:700;">{bags}</span>' if bags else '<span style="color:#2A3540; font-size:11px;">—</span>'

        st.markdown(f"""
        <div style="display:flex; padding:10px 16px; border-bottom:1px solid #131B25; background:{row_bg}; align-items:center;">
            <span style="width:80px; font-family:'Orbitron',monospace; font-size:12px; color:{lvl_color}; font-weight:{'700' if is_milestone else '400'};">Lv.{lvl}</span>
            <span style="width:120px; font-family:'Orbitron',monospace; font-size:13px; color:{xp_color};">{xp:,} XP</span>
            <span style="flex:1;">{role_html}</span>
            <span style="width:120px;">{bags_html}</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # Weekly Article Submission Rewards
    st.markdown(f"""
    <div class="guide-card-gold">
        <div style="font-family:'Orbitron',monospace; font-size:12px; color:#EDD97A; margin-bottom:10px; letter-spacing:2px;">📰 {t("WEEKLY ARTICLE SUBMISSION REWARDS", "ہفتہ وار آرٹیکل جمع کرانے کے ریوارڈز")}</div>
        <div style="font-size:13px; color:#E8F0F8; line-height:2.0;">
        ✅ {t("Write & submit quality articles for extra weekly rewards!", "معیاری آرٹیکل لکھیں اور جمع کریں — ہفتہ وار اضافی ریوارڈز کے لیے!")}<br><br>
        📝 {t("Platforms accepted:", "قبول شدہ پلیٹ فارمز:")} <span style="color:#00FFB2;">Mirror</span> · <span style="color:#4DA6FF;">Paragraph</span><br><br>
        <span style="color:#00FFB2;">#community-news</span> {t("for details", "تفصیل کے لیے")}
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"### ⚡ {t('Tips to Earn XP Fast', 'تیزی سے XP کمانے کے طریقے')}")

    tips = [
        (t("💬 Daily Chat", "💬 روزانہ چیٹ"),
         t("Stay active on Discord every day. Messages = XP. Quality over quantity.", "ہر روز Discord پر فعال رہیں۔ پیغامات = XP۔ تعداد سے زیادہ معیار۔")),
        (t("📝 Write Articles", "📝 آرٹیکل لکھیں"),
         t("Community articles give more XP + pts rewards on Mirror/Paragraph.", "کمیونٹی آرٹیکلز زیادہ XP + Mirror/Paragraph پر pts ریوارڈز دیتے ہیں۔")),
        (t("🤝 Invite Friends", "🤝 دوستوں کو دعوت دیں"),
         t("Referrals also earn XP. Share your Discord invite link.", "ریفرلز سے بھی XP ملتا ہے۔ اپنا Discord دعوت نامہ شیئر کریں۔")),
        (t("🎯 Participate in Events", "🎯 ایونٹس میں حصہ لیں"),
         t("Join Concrete AMAs, Twitter Spaces, and community events.", "کنکریٹ AMAs، Twitter Spaces، اور کمیونٹی ایونٹس میں شامل ہوں۔")),
        (t("❓ Ask/Answer Questions", "❓ سوال پوچھیں/جواب دیں"),
         t("Helpful replies and questions also count as engagement.", "مددگار جوابات اور سوالات بھی engagement میں شمار ہوتے ہیں۔")),
    ]

    for icon_title, desc in tips:
        st.markdown(f"""
        <div style="display:flex; gap:16px; padding:12px 0; border-bottom:1px solid #131B25; align-items:flex-start;">
            <div style="color:#00FFB2; font-weight:700; min-width:160px; font-family:'Orbitron',monospace; font-size:10px;">{icon_title}</div>
            <div style="font-size:13px; color:#556070; line-height:1.7;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════
# TAB 5 — MOAI & BADGES
# ════════════════════════════════════════════════════════════════
with tab_moai:
    st.markdown(f"""
    <div style="font-family:'Orbitron',monospace; font-size:13px; color:#556070; letter-spacing:3px; margin-bottom:20px;">
    🗿 {t("MOAI NFT & BADGES — IDENTITY SYSTEM", "موآئی NFT اور بیجز — شناختی نظام")}
    </div>
    """, unsafe_allow_html=True)

    col_m1, col_m2 = st.columns(2)

    with col_m1:
        st.markdown(f"""
        <div class="guide-card-gold">
            <div style="font-family:'Orbitron',monospace; font-size:12px; color:#EDD97A; margin-bottom:12px; letter-spacing:2px;">🗿 {t("WHAT IS MOAI?", "موآئی کیا ہے؟")}</div>
            <div style="font-size:13px; color:#E8F0F8; line-height:2.0;">
            {t(
                "Moai is Concrete's mascot/identity — inspired by Easter Island stone figures.<br><br>When you see moai referenced in the community, understand: <b style='color:#EDD97A;'>solid, reliable, unshakeable</b> — just like the Concrete protocol itself.<br><br>🗿 = Symbol of the Concrete family.",
                "موآئی کنکریٹ کا شخصیت/علامت ہے — Easter Island کے پتھر کی مورتوں سے متاثر۔<br><br>جب کمیونٹی میں موآئی کا ذکر ہو، سمجھیں: <b style='color:#EDD97A;'>مضبوط، قابل اعتماد، اٹل</b> — بالکل کنکریٹ پروٹوکول کی طرح۔<br><br>🗿 = کنکریٹ خاندان کی علامت۔"
            )}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_m2:
        st.markdown(f"""
        <div class="guide-card-neon">
            <div style="font-family:'Orbitron',monospace; font-size:12px; color:#00FFB2; margin-bottom:12px; letter-spacing:2px;">🏅 {t("WHAT ARE BADGES?", "بیجز کیا ہوتے ہیں؟")}</div>
            <div style="font-size:13px; color:#E8F0F8; line-height:2.0;">
            {t(
                "Badges are awarded for achievements:<br><br>• <b style='color:#00FFB2;'>Level Badges</b> — at XP milestones<br>• <b style='color:#EDD97A;'>Contributor Badge</b> — for articles/content<br>• <b style='color:#9B59FF;'>Special Badges</b> — events/competitions<br>• <b style='color:#E8A020;'>OG Badge</b> — for early community members",
                "بیجز کامیابیوں کے لیے ملتے ہیں:<br><br>• <b style='color:#00FFB2;'>لیول بیجز</b> — XP سنگ میل پر<br>• <b style='color:#EDD97A;'>Contributor بیج</b> — آرٹیکلز/مواد پر<br>• <b style='color:#9B59FF;'>خصوصی بیجز</b> — ایونٹس/مقابلوں پر<br>• <b style='color:#E8A020;'>OG بیج</b> — ابتدائی کمیونٹی اراکین کو"
            )}
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown(f"### 🏅 {t('Badge Types — Complete Guide', 'بیج اقسام — مکمل گائیڈ')}")

    badges = [
        ("🗿", "Moai OG",
         t("Given to members who joined the community early. Rare and prestigious.", "ابتدائی کمیونٹی اراکین کو ملتا ہے۔ نادر اور باوقار۔"),
         "#EDD97A"),
        ("⭐", "Newbie",
         t("Awarded for completing Level 5. Your first achievement badge.", "لیول 5 مکمل کرنے پر ملتا ہے۔ آپ کا پہلا کامیابی بیج۔"),
         "#4DA6FF"),
        ("🧭", "Vault Navigator",
         t("Level 10 milestone. Proof of vault knowledge.", "لیول 10 سنگ میل۔ والٹ علم کا ثبوت۔"),
         "#00FFB2"),
        ("☘️", "Lucky 17",
         t("Level 17 — a special number in the Concrete community.", "لیول 17 — کنکریٹ کمیونٹی میں ایک خاص نمبر۔"),
         "#9B59FF"),
        ("🏆", "Grindooor",
         t("Level 25 — highest badge. Only for truly dedicated members.", "لیول 25 — سب سے اعلی بیج۔ صرف واقعی سرگرم اراکین کو۔"),
         "#E8A020"),
        ("📝", "Writer",
         t("Awarded for writing community articles or guides.", "کمیونٹی آرٹیکلز یا گائیڈز لکھنے پر ملتا ہے۔"),
         "#FF7A2F"),
        ("🤝", "Contributor",
         t("Significant contribution to protocol development, tools, or content.", "پروٹوکول ڈویلپمنٹ، ٹولز، یا مواد میں نمایاں تعاون۔"),
         "#4DA6FF"),
        ("⚡", "Event Champion",
         t("Awarded for winning community events and competitions.", "کمیونٹی ایونٹس اور مقابلوں میں جیتنے پر ملتا ہے۔"),
         "#FF3D5A"),
    ]

    b_cols = st.columns(2)
    for i, (icon, name, desc, color) in enumerate(badges):
        with b_cols[i % 2]:
            st.markdown(f"""
            <div style="background:var(--bg-card); border:1px solid {color}30; border-left:3px solid {color}; border-radius:8px; padding:14px; margin-bottom:12px;">
                <div style="display:flex; gap:10px; align-items:center; margin-bottom:8px;">
                    <span style="font-size:22px;">{icon}</span>
                    <span style="font-family:'Orbitron',monospace; font-size:12px; color:{color}; font-weight:700;">{name}</span>
                </div>
                <div style="font-size:12px; color:#556070; line-height:1.7;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown(f"""
    <div class="tip-box">
    💡 <b>{t("Moai Wisdom:", "موآئی کی حکمت:")}</b> "{t(
        'Be like Moai — solid, immovable, always facing forward." The community is strong when everyone builds together.',
        'موآئی جیسے بنو — مضبوط، اٹل، ہمیشہ آگے کی طرف۔" کمیونٹی مضبوط ہے جب سب مل کر بناتے ہیں۔'
    )} 🗿
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════
# TAB 6 — ARTICLES
# ════════════════════════════════════════════════════════════════
with tab_articles:
    st.markdown(f"""
    <div style="font-family:'Orbitron',monospace; font-size:13px; color:#556070; letter-spacing:3px; margin-bottom:20px;">
    📝 {t("ARTICLE SUBMISSION — CONTRIBUTE & EARN", "آرٹیکل جمع کرانا — حصہ ڈالیں اور کمائیں")}
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="guide-card-gold">
        <div style="font-family:'Orbitron',monospace; font-size:12px; color:#EDD97A; margin-bottom:12px; letter-spacing:2px;">📝 {t("WHAT IS THE ARTICLE PROGRAM?", "آرٹیکل پروگرام کیا ہے؟")}</div>
        <div style="font-size:13px; color:#E8F0F8; line-height:2.0;">
        {t(
            'Concrete encourages community members to create <b style="color:#EDD97A;">educational content</b>.<br>If your article is accepted → <b style="color:#00FFB2;">you get extra XP + Writer badge + community visibility</b>.<br><br>It\'s a great way to level up fast and build your name in the community.',
            'کنکریٹ کمیونٹی اراکین کی حوصلہ افزائی کرتا ہے کہ وہ <b style="color:#EDD97A;">تعلیمی مواد</b> بنائیں۔<br>اگر آپ کا آرٹیکل قبول ہو → <b style="color:#00FFB2;">اضافی XP + Writer بیج + کمیونٹی نمائش</b> ملتی ہے۔<br><br>یہ تیزی سے لیول اپ کرنے اور کمیونٹی میں نام بنانے کا اچھا طریقہ ہے۔'
        )}
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"### ✅ {t('How to Submit an Article — Step by Step', 'آرٹیکل کیسے جمع کرائیں — مرحلہ بہ مرحلہ')}")

    article_steps = [
        (t("IDEA", "خیال"),
         t("Choose a topic", "موضوع منتخب کریں"),
         t("Write about something related to Concrete — vault guide, explain a DeFi concept, risk management, or share your experience.", "کنکریٹ سے متعلق کچھ لکھیں — والٹ گائیڈ، DeFi تصور سمجھائیں، رسک مینجمنٹ، یا اپنا تجربہ شیئر کریں۔")),
        (t("DRAFT", "مسودہ"),
         t("Write the article", "آرٹیکل لکھیں"),
         t("Use clear and simple language. English or Urdu — both accepted. Add screenshots where helpful.", "واضح اور سادہ زبان استعمال کریں۔ انگریزی یا اردو — دونوں قبول ہیں۔ جہاں مددگار ہو اسکرین شاٹس شامل کریں۔")),
        (t("FORMAT", "فارمیٹ"),
         t("Format properly", "درست فارمیٹ کریں"),
         t("Title, intro, main content, conclusion. Use headings. 300-1000 words ideal.", "عنوان، تعارف، مرکزی مواد، نتیجہ۔ سرخیاں استعمال کریں۔ 300-1000 الفاظ بہترین ہے۔")),
        (t("SUBMIT", "جمع کریں"),
         t("Submit on Discord", "Discord پر جمع کریں"),
         t("Find the #article-submission channel. Paste your article or link there.", "#article-submission چینل تلاش کریں۔ وہاں اپنا آرٹیکل یا لنک جمع کریں۔")),
        (t("REVIEW", "جائزہ"),
         t("Wait for review", "جائزے کا انتظار کریں"),
         t("Concrete team or mods review it. Can take 1-3 days.", "کنکریٹ ٹیم یا mods جائزہ لیتے ہیں۔ 1-3 دن لگ سکتے ہیں۔")),
        (t("REWARD", "انعام"),
         t("Get XP + Badge", "XP + بیج حاصل کریں"),
         t("On acceptance, you get the Writer badge + bonus XP. Congratulations!", "قبولیت پر Writer بیج + بونس XP ملتا ہے۔ مبارک ہو!")),
    ]

    for badge, title, desc in article_steps:
        st.markdown(f"""
        <div style="display:flex; gap:16px; padding:14px 0; border-bottom:1px solid #131B25; align-items:flex-start;">
            <span style="font-family:'Orbitron',monospace; font-size:9px; color:#EDD97A; background:#EDD97A10; border:1px solid #EDD97A33; padding:4px 8px; border-radius:4px; min-width:60px; text-align:center; letter-spacing:1px;">{badge}</span>
            <div>
                <div style="font-family:'Orbitron',monospace; font-size:11px; color:#E8F0F8; margin-bottom:4px;">{title}</div>
                <div style="font-size:12px; color:#556070; line-height:1.7;">{desc}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown(f"### 💡 {t('Article Topics — Inspiration', 'آرٹیکل موضوعات — تحریک')}")

    topics_en = [
        "Concrete vaults — beginner guide",
        "What is ERC-4626?",
        "Risk management in DeFi",
        "What is Health Factor and why it's important",
        "ct[Asset] token mechanics",
        "Aave vs Morpho vs Silo — strategy comparison",
        "My first Concrete deposit — experience share",
        "Concrete XP system explained",
        "Community building in DeFi",
        "Why smart contract audits are necessary",
    ]
    topics_ur = [
        "کنکریٹ والٹس — ابتدائی گائیڈ",
        "ERC-4626 کیا ہوتا ہے؟",
        "DeFi میں رسک مینجمنٹ",
        "Health Factor کیا ہے اور کیوں اہم ہے",
        "ct[Asset] ٹوکنز کی میکانزم",
        "Aave بمقابلہ Morpho بمقابلہ Silo — حکمت عملی موازنہ",
        "میرا پہلا کنکریٹ ڈپازٹ — تجربہ شیئر",
        "کنکریٹ XP سسٹم سمجھایا گیا",
        "DeFi میں کمیونٹی تعمیر",
        "Smart contract آڈٹس کیوں ضروری ہیں",
    ]
    topics = topics_en if st.session_state.lang == "en" else topics_ur

    t_cols = st.columns(2)
    for i, topic in enumerate(topics):
        with t_cols[i % 2]:
            st.markdown(f"""
            <div style="padding:8px 12px; background:var(--bg-card); border:1px solid var(--border); border-radius:6px; margin-bottom:8px; font-size:12px; color:#556070;">
            💡 {topic}
            </div>
            """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="tip-box">
    💡 <b>{t("Writing Tip:", "لکھنے کی ٹِپ:")}</b> {t(
        "Share what you've learned yourself — authentic experience engages the most. Perfect writing isn't needed, honest writing is!",
        "جو خود سیکھا ہے وہ شیئر کریں — اصل تجربہ سب سے زیادہ متوجہ کرتا ہے۔ کامل لکھنے کی ضرورت نہیں، ایمانداری سے لکھیں!"
    )}
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════
# TAB 7 — VAULT TOOL
# ════════════════════════════════════════════════════════════════
with tab_tool:
    st.markdown(f"""
    <div style="font-family:'Orbitron',monospace; font-size:13px; color:#556070; letter-spacing:3px; margin-bottom:20px;">
    🛠️ {t("COMMUNITY VAULT INTELLIGENCE TOOL", "کمیونٹی والٹ انٹیلیجنس ٹول")}
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="guide-card-neon">
        <div style="font-family:'Orbitron',monospace; font-size:14px; color:#00FFB2; margin-bottom:12px; letter-spacing:2px; font-weight:700;">
        🗿 CONCRETE VAULT INTELLIGENCE TERMINAL
        </div>
        <div style="font-size:13px; color:#E8F0F8; line-height:2.0; margin-bottom:16px;">
        {t(
            "A community-built tool providing real-time vault data, yield simulation, risk analysis, and portfolio rebalancing.",
            "کمیونٹی کا بنایا ہوا ٹول جو real-time والٹ ڈیٹا، yield سمیولیشن، رسک تجزیہ اور پورٹ فولیو ری بیلنسنگ فراہم کرتا ہے۔"
        )}
        </div>
        <a href="https://concrete-vault.streamlit.app" target="_blank" style="display:inline-block; background:#00FFB215; border:1px solid #00FFB2; color:#00FFB2; font-family:'Orbitron',monospace; font-size:11px; padding:10px 24px; border-radius:6px; text-decoration:none; letter-spacing:2px;">
        🚀 {t("OPEN VAULT TOOL →", "والٹ ٹول کھولیں →")}
        </a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"### 🔍 {t('Whats Inside the Tool?', 'ٹول میں کیا کیا ہے؟')}")

    features = [
        ("📊", t("Vault Health Radar", "والٹ ہیلتھ ریڈار"),
         t("Real-time health factors, APY comparison, and TVL across all Concrete vaults.", "تمام کنکریٹ والٹس میں real-time health factors، APY موازنہ، اور TVL۔")),
        ("🧬", t("Vault DNA Fingerprint", "والٹ DNA فنگرپرنٹ"),
         t("6-dimensional radar chart — see each vault's unique 'personality'. Yield Consistency, Liquidity, Strategy Diversity.", "6 جہتی ریڈار چارٹ — ہر والٹ کی منفرد 'شخصیت' دیکھیں۔ Yield مستقل مزاجی، لیکویڈیٹی، حکمت عملی تنوع۔")),
        ("💰", t("Yield Simulator", "Yield سمیولیٹر"),
         t("Enter your deposit amount, select a vault, and see how much yield you'd get — from 1 month to 5 years.", "اپنی ڈپازٹ رقم درج کریں، والٹ منتخب کریں، اور دیکھیں کتنا yield ملے گا — 1 ماہ سے 5 سال تک۔")),
        ("⚖️", t("Portfolio Rebalancer", "پورٹ فولیو ری بیلنسر"),
         t("Enter current holdings → suggests optimal allocation based on Max Efficiency, Min Risk, or Max APY strategy.", "موجودہ ہولڈنگز درج کریں → Max Efficiency، Min Risk، یا Max APY حکمت عملی پر مبنی بہترین تقسیم تجویز کرتا ہے۔")),
        ("📈", t("Yield Calendar", "Yield کیلنڈر"),
         t("Day-by-day portfolio growth chart. See daily yield and ct[Asset] token appreciation.", "روزانہ پورٹ فولیو نمو چارٹ۔ روزانہ yield اور ct[Asset] ٹوکن قدر بڑھاؤ دیکھیں۔")),
        ("🔴 vs 🟢", t("DeFi vs Concrete Compare", "DeFi بمقابلہ کنکریٹ موازنہ"),
         t("Standard DeFi yield vs Concrete protected yield comparison — visualize risk-adjusted returns.", "معیاری DeFi yield بمقابلہ کنکریٹ محفوظ yield موازنہ — risk-adjusted returns کو دیکھیں۔")),
        ("❓", t("Technical FAQ", "تکنیکی سوال جواب"),
         t("Technical questions about the protocol — smart contracts, data sources, methodology all explained.", "پروٹوکول کے بارے میں تکنیکی سوالات — smart contracts، ڈیٹا ذرائع، طریقہ کار سب سمجھایا گیا۔")),
    ]

    for icon, title, desc in features:
        st.markdown(f"""
        <div style="display:flex; gap:16px; padding:14px 0; border-bottom:1px solid #131B25; align-items:flex-start;">
            <span style="font-size:22px; min-width:36px;">{icon}</span>
            <div>
                <div style="font-family:'Orbitron',monospace; font-size:11px; color:#00FFB2; margin-bottom:4px;">{title}</div>
                <div style="font-size:12px; color:#556070; line-height:1.7;">{desc}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown(f"""
    <div class="guide-card-gold">
        <div style="font-family:'Orbitron',monospace; font-size:12px; color:#EDD97A; margin-bottom:10px; letter-spacing:2px;">⚡ {t("HOW TO USE THE TOOL?", "ٹول کیسے استعمال کریں؟")}</div>
        <div style="font-size:13px; color:#E8F0F8; line-height:2.0;">
        {t(
            '1. Open <a href="https://concrete-vault.streamlit.app" target="_blank" style="color:#00FFB2;">concrete-vault.streamlit.app</a><br>2. Select your amount and vault in the sidebar<br>3. Explore tabs — Simulator, Rebalancer, Yield Calendar<br>4. See data, compare, then make your decision<br><br><b style="color:#EDD97A;">Made by community member mkashifalikcp. Not officially affiliated with Concrete Protocol.</b>',
            '1. <a href="https://concrete-vault.streamlit.app" target="_blank" style="color:#00FFB2;">concrete-vault.streamlit.app</a> کھولیں<br>2. Sidebar میں اپنی رقم اور والٹ منتخب کریں<br>3. ٹیبز دیکھیں — Simulator، Rebalancer، Yield Calendar<br>4. ڈیٹا دیکھیں، موازنہ کریں، پھر اپنا فیصلہ کریں<br><br><b style="color:#EDD97A;">کمیونٹی رکن mkashifalikcp نے بنایا۔ کنکریٹ پروٹوکول سے آفیشل طور پر وابستہ نہیں۔</b>'
        )}
        </div>
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════
# TAB 8 — FAQ
# ════════════════════════════════════════════════════════════════
with tab_faq:
    st.markdown(f"""
    <div style="font-family:'Orbitron',monospace; font-size:13px; color:#556070; letter-spacing:3px; margin-bottom:20px;">
    ❓ {t("FREQUENTLY ASKED QUESTIONS", "اکثر پوچھے گئے سوالات")}
    </div>
    """, unsafe_allow_html=True)

    faqs = [
        (t("🗿 Is Concrete Protocol safe?", "🗿 کنکریٹ پروٹوکول محفوظ ہے؟"),
         t("Concrete's smart contracts are audited. But no protocol in DeFi is 100% risk-free. Smart contract bugs, oracle failures, and market crashes are all possible. Only invest what you can afford to lose.",
           "کنکریٹ کے smart contracts آڈیٹڈ ہیں۔ لیکن DeFi میں کوئی بھی پروٹوکول 100% خطرہ سے پاک نہیں۔ Smart contract bugs، oracle failures، اور مارکیٹ کریش ممکن ہیں۔ صرف وہ رقم لگائیں جو کھونے کی استطاعت رکھتے ہیں۔")),

        (t("💰 What is the minimum deposit?",  "💰 کم از کم ڈپازٹ کتنا ہے؟"),
         t("Check the official minimum at concrete.xyz — it can vary by vault. Generally it's wise to start with a small amount.",
           "آفیشل کم از کم حد concrete.xyz پر چیک کریں — یہ والٹ کے حساب سے مختلف ہو سکتا ہے۔ عموماً چھوٹی رقم سے شروع کرنا دانش مندی ہے۔")),

        (t("⏳ When is yield received?", "⏳ Yield کب ملتی ہے؟"),
         t("ct[Asset] token values continuously appreciate — second by second! No manual claiming. Whenever you withdraw, accumulated yield is automatically included.",
           "ct[Asset] ٹوکنز کی قیمت مسلسل بڑھتی ہے — سیکنڈ بہ سیکنڈ! کوئی manual claiming نہیں۔ جب بھی نکالیں، جمع شدہ yield خودکار مل جاتی ہے۔")),

        (t("🔄 Can I withdraw anytime?", "🔄 کیا کبھی بھی نکال سکتے ہیں؟"),
         t("Generally yes — ERC-4626 vaults support instant withdrawals. But liquidity can be limited during high utilization periods. Check withdrawal terms per vault.",
           "عام طور پر ہاں — ERC-4626 والٹس فوری نکاسی سپورٹ کرتے ہیں۔ لیکن زیادہ استعمال کے دوران لیکویڈیٹی محدود ہو سکتی ہے۔ ہر والٹ کی نکاسی شرائط چیک کریں۔")),

        (t("📊 Is APY stable?", "📊 کیا APY مستحکم رہتا ہے؟"),
         t("APY is variable — it changes according to underlying protocol conditions. The APY shown today may be different tomorrow. Always check current rates.",
           "APY متغیر ہوتا ہے — بنیادی پروٹوکول حالات کے مطابق بدلتا ہے۔ آج جو APY دکھ رہا ہے، کل مختلف ہو سکتا ہے۔ ہمیشہ موجودہ شرحیں چیک کریں۔")),

        (t("🔑 Is connecting a wallet safe?", "🔑 والٹ کنیکٹ کرنا محفوظ ہے؟"),
         t("Always use the official website concrete.xyz. Verify the URL before clicking any link. Phishing sites are very common in DeFi.",
           "ہمیشہ آفیشل ویب سائٹ concrete.xyz استعمال کریں۔ کسی بھی لنک پر کلک کرنے سے پہلے URL تصدیق کریں۔ DeFi میں phishing سائٹس بہت عام ہیں۔")),

        (t("🏆 How is XP counted?", "🏆 XP کیسے گنا جاتا ہے؟"),
         t("XP comes from activity on Concrete Discord. Chat, engagement, articles — all count. The exact formula isn't public, but staying active is the best strategy.",
           "Concrete Discord پر سرگرمی سے XP ملتا ہے۔ چیٹ، مشغولیت، آرٹیکلز — سب شمار ہوتے ہیں۔ عین فارمولا عام نہیں، لیکن فعال رہنا بہترین حکمت عملی ہے۔")),

        (t("💼 Can ct[Asset] tokens be staked?", "💼 کیا ct[Asset] ٹوکنز stake کر سکتے ہیں؟"),
         t("This depends on protocol updates. For the latest info, check concrete.xyz/ecosystem or Discord.",
           "یہ پروٹوکول اپڈیٹس پر منحصر ہے۔ تازہ ترین معلومات کے لیے concrete.xyz/ecosystem یا Discord چیک کریں۔")),

        (t("📝 What if an article gets rejected?", "📝 اگر آرٹیکل رد ہو جائے تو؟"),
         t("Don't be discouraged! Get feedback from mods, improve, and resubmit. Quality content eventually gets accepted.",
           "مایوس نہ ہوں! mods سے فیڈ بیک لیں، بہتر کریں، اور دوبارہ جمع کریں۔ معیاری مواد بالآخر قبول ہو جاتا ہے۔")),

        (t("🌐 Is this guide financial advice?", "🌐 کیا یہ گائیڈ مالی مشورہ ہے؟"),
         t("Absolutely not! This is a community-written educational guide. Do your own research before making any investment decision. This tool and guide is informational only.",
           "بالکل نہیں! یہ کمیونٹی کا لکھا ہوا تعلیمی گائیڈ ہے۔ کوئی بھی سرمایہ کاری فیصلہ کرنے سے پہلے اپنی تحقیق کریں (DYOR)۔ یہ ٹول اور گائیڈ صرف معلوماتی ہے۔")),
    ]

    for q, a in faqs:
        with st.expander(q):
            st.markdown(f'<div style="font-size:13px; color:#E8F0F8; line-height:2.0; padding:8px 0;">{a}</div>', unsafe_allow_html=True)

    st.markdown("---")

    # Footer
    st.markdown(f"""
    <div style="background:#090D14; border:1px solid #131B25; border-radius:10px; padding:28px; text-align:center; margin-top:20px;">
        <div style="font-family:'Orbitron',monospace; font-size:22px; color:#00FFB2; font-weight:900; margin-bottom:8px; letter-spacing:4px;">
        🗿 CONCRETE 101
        </div>
        <div style="font-family:'Share Tech Mono',monospace; font-size:12px; color:#EDD97A; letter-spacing:3px; margin-bottom:16px;">
        {t("ONE TEAM. ONE VISION. KEEP BUILDING TOGETHER.", "ایک ٹیم۔ ایک وژن۔ مل کر بناتے رہیں۔")}
        </div>
        <div style="display:flex; gap:16px; justify-content:center; flex-wrap:wrap; margin-bottom:16px;">
            <a href="https://concrete.xyz" target="_blank" style="color:#00FFB2; font-size:12px; text-decoration:none;">🏠 concrete.xyz</a>
            <a href="https://docs.concrete.xyz" target="_blank" style="color:#EDD97A; font-size:12px; text-decoration:none;">📘 Docs</a>
            <a href="https://points.concrete.xyz" target="_blank" style="color:#4DA6FF; font-size:12px; text-decoration:none;">⭐ Points</a>
            <a href="https://concrete-vault.streamlit.app" target="_blank" style="color:#9B59FF; font-size:12px; text-decoration:none;">🛠️ Vault Tool</a>
        </div>
        <div style="font-size:9px; color:#2A3540; letter-spacing:2px;">
        ⚠ {t("COMMUNITY GUIDE · NOT FINANCIAL ADVICE · DYOR · NOT AFFILIATED WITH CONCRETE PROTOCOL OFFICIALLY",
               "کمیونٹی گائیڈ · مالی مشورہ نہیں · DYOR · کنکریٹ پروٹوکول سے آفیشل طور پر غیر وابستہ")}
        </div>
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════
# TAB 9 — KEY CONDITIONS (from image 2)
# ════════════════════════════════════════════════════════════════
with tab_key:
    st.markdown(f"""
    <div style="font-family:'Orbitron',monospace; font-size:13px; color:#556070; letter-spacing:3px; margin-bottom:20px;">
    🔑 {t("CONDITIONS FOR GETTING A KEY 🗝️", "کلید حاصل کرنے کی شرائط 🗝️")}
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="guide-card-neon">
        <div style="font-family:'Orbitron',monospace; font-size:12px; color:#00FFB2; margin-bottom:12px; letter-spacing:2px;">
        🗝️ {t("WHAT IS A KEY?", "کلید کیا ہے؟")}
        </div>
        <div style="font-size:13px; color:#E8F0F8; line-height:2.0;">
        {t(
            "A KEY is a special role/access in the Concrete community. It is given to members who consistently contribute value — through support, content creation, and platform engagement.",
            "KEY کنکریٹ کمیونٹی میں ایک خصوصی رول/رسائی ہے۔ یہ ان اراکین کو دی جاتی ہے جو مسلسل قدر شامل کرتے ہیں — سپورٹ، مواد، اور پلیٹ فارم مشغولیت کے ذریعے۔"
        )}
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"### 📋 {t('4 Conditions to Get a Key', 'کلید پانے کی 4 شرائط')}")

    key_conditions = [
        ("1", "🤝", t("Provide enthusiastic and friendly support to everyone",
                       "سب کو پرجوش اور دوستانہ سپورٹ فراہم کریں"),
         t("Help newcomers, answer questions, be welcoming in Discord. Your attitude matters — be the reason someone feels at home in the community.",
           "نئے اراکین کی مدد کریں، سوالات کے جوابات دیں، Discord میں خوش آمدید کہیں۔ آپ کا رویہ اہمیت رکھتا ہے — کسی کو گھر جیسا محسوس کرانے کی وجہ بنیں۔"),
         "#00FFB2"),
        ("2", "😂", t("Create memes every day",
                       "ہر روز میمز بنائیں"),
         t("Make Concrete-related memes daily. Post in the memes channel. Creative, funny, and on-topic content gets noticed. Use AI tools like DALL-E, Canva, CapCut, or manual design.",
           "ہر روز کنکریٹ سے متعلق میمز بنائیں۔ میمز چینل میں پوسٹ کریں۔ تخلیقی، مزاحیہ اور موضوع سے متعلق مواد توجہ حاصل کرتا ہے۔ DALL-E، Canva، CapCut جیسے AI ٹولز استعمال کریں۔"),
         "#EDD97A"),
        ("3", "🤖", t("Use bots to clean the server (not spam bots — moderation bots)",
                       "سرور صاف کرنے کے لیے bots استعمال کریں (اسپام نہیں — ماڈریشن bots)"),
         t("This means actively helping moderate the server — reporting spam, helping with moderation tasks, keeping channels clean and organized. Be a responsible community member.",
           "اس کا مطلب ہے سرور کو فعال طور پر moderate کرنا — spam رپورٹ کرنا، moderation کاموں میں مدد کرنا، چینلز کو صاف اور منظم رکھنا۔ ذمہ دار کمیونٹی رکن بنیں۔"),
         "#4DA6FF"),
        ("4", "📱", t("X (Twitter) = 2–3 posts/day",
                       "X (ٹوئٹر) = روزانہ 2-3 پوسٹس"),
         t("Post 2-3 times daily on X/Twitter about Concrete. Use #ConcreteDeFi tag. Share updates, your vault experience, educational content. Consistent Twitter presence is key!",
           "X/ٹوئٹر پر روزانہ 2-3 بار کنکریٹ کے بارے میں پوسٹ کریں۔ #ConcreteDeFi ٹیگ استعمال کریں۔ اپڈیٹس، اپنا والٹ تجربہ، تعلیمی مواد شیئر کریں۔ مستقل Twitter موجودگی اہم ہے!"),
         "#9B59FF"),
    ]

    for num, icon, cond_title, cond_desc, color in key_conditions:
        st.markdown(f"""
        <div class="guide-card" style="border-left:4px solid {color}; border-color:{color}30; border-left-color:{color};">
            <div style="display:flex; align-items:center; gap:14px; margin-bottom:10px;">
                <span style="font-family:'Orbitron',monospace; font-size:18px; color:{color}; background:{color}15; border:2px solid {color}33; padding:6px 12px; border-radius:8px; font-weight:900;">{num}</span>
                <span style="font-size:28px;">{icon}</span>
                <span style="font-family:'Orbitron',monospace; font-size:12px; color:{color}; font-weight:700;">{cond_title}</span>
            </div>
            <div style="font-size:13px; color:#556070; line-height:1.8; padding-left:4px;">{cond_desc}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="tip-box">
    💡 <b>{t("Pro Tip:", "پرو ٹِپ:")}</b> {t(
        "All 4 conditions work together. Be consistent — daily memes + Twitter posts + helping in Discord. The KEY is earned, not given!",
        "چاروں شرائط مل کر کام کرتی ہیں۔ مستقل رہیں — روزانہ میمز + Twitter پوسٹس + Discord میں مدد۔ KEY کمائی جاتی ہے، دی نہیں جاتی!"
    )}
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════
# TAB 10 — WRITE GUIDE (Article Writing with AI & Manual)
# ════════════════════════════════════════════════════════════════
with tab_write:
    st.markdown(f"""
    <div style="font-family:'Orbitron',monospace; font-size:13px; color:#556070; letter-spacing:3px; margin-bottom:20px;">
    ✍️ {t("HOW TO WRITE CONCRETE ARTICLES — AI & MANUAL", "کنکریٹ آرٹیکل کیسے لکھیں — AI اور خود")}
    </div>
    """, unsafe_allow_html=True)

    wc1, wc2 = st.columns(2)
    with wc1:
        st.markdown(f"""
        <div class="guide-card-neon">
            <div style="font-family:'Orbitron',monospace; font-size:12px; color:#00FFB2; margin-bottom:10px; letter-spacing:2px;">🤖 {t("AI-ASSISTED WRITING", "AI کی مدد سے لکھنا")}</div>
            <div style="font-size:13px; color:#E8F0F8; line-height:2.1;">
            {t(
                "<b>Tools:</b> ChatGPT, Claude, Gemini<br><br><b>How to use:</b><br>1. Give a clear prompt e.g.:<br><span style='color:#00FFB2; font-size:12px;'>\"Write a beginner guide about Concrete Protocol ERC-4626 vaults — what they are, how to deposit, risks. Keep it under 600 words, friendly tone.\"</span><br><br>2. Review & personalize — add your own experience<br>3. Add relevant screenshots<br>4. Proofread before submitting",
                "<b>ٹولز:</b> ChatGPT, Claude, Gemini<br><br><b>کیسے استعمال کریں:</b><br>1. واضح prompt دیں مثلاً:<br><span style='color:#00FFB2; font-size:12px;'>\"Concrete Protocol ERC-4626 والٹس کے بارے میں ابتدائی گائیڈ لکھیں — کیا ہیں، کیسے ڈپازٹ کریں، خطرات۔ 600 الفاظ سے کم، دوستانہ لہجہ۔\"</span><br><br>2. جائزہ لیں اور ذاتی بنائیں — اپنا تجربہ شامل کریں<br>3. متعلقہ اسکرین شاٹس شامل کریں<br>4. جمع کرانے سے پہلے درست کریں"
            )}
            </div>
        </div>
        """, unsafe_allow_html=True)
    with wc2:
        st.markdown(f"""
        <div class="guide-card-gold">
            <div style="font-family:'Orbitron',monospace; font-size:12px; color:#EDD97A; margin-bottom:10px; letter-spacing:2px;">✍️ {t("MANUAL WRITING", "خود لکھنا")}</div>
            <div style="font-size:13px; color:#E8F0F8; line-height:2.1;">
            {t(
                "<b>Best approach:</b> Write from your real experience<br><br>1. Choose a topic you understand<br>2. Start with WHY it matters<br>3. Explain step by step<br>4. Add your personal insights<br>5. End with a clear conclusion<br><br><b style='color:#EDD97A;'>Authentic > Perfect. Your real story is your strongest content.</b>",
                "<b>بہترین طریقہ:</b> اپنے اصل تجربے سے لکھیں<br><br>1. ایسا موضوع چنیں جو آپ سمجھتے ہیں<br>2. WHY (کیوں اہم ہے) سے شروع کریں<br>3. مرحلہ بہ مرحلہ سمجھائیں<br>4. اپنی ذاتی رائے شامل کریں<br>5. واضح نتیجے پر ختم کریں<br><br><b style='color:#EDD97A;'>اصلی > کامل۔ آپ کی اصل کہانی آپ کا سب سے طاقتور مواد ہے۔</b>"
            )}
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"### 📋 {t('Article Structure Template', 'آرٹیکل ڈھانچہ ٹیمپلیٹ')}")

    structure = [
        (t("📌 Title", "📌 عنوان"),
         t("Clear + catchy. e.g. 'My First Concrete Vault Deposit: What I Learned'", "واضح + دلچسپ۔ مثلاً 'میرا پہلا کنکریٹ والٹ ڈپازٹ: کیا سیکھا'")),
        (t("👋 Introduction (50-80 words)", "👋 تعارف (50-80 الفاظ)"),
         t("Hook the reader — why should they read this? What problem does it solve?", "قاری کو ہُک کریں — انہیں یہ کیوں پڑھنا چاہیے؟ کون سا مسئلہ حل ہوتا ہے؟")),
        (t("🧱 Main Content (200-700 words)", "🧱 مرکزی مواد (200-700 الفاظ)"),
         t("Break into sections with H2/H3 headings. Use bullet points for lists. Include examples.", "H2/H3 سرخیوں کے ساتھ حصوں میں تقسیم کریں۔ فہرستوں کے لیے bullet points استعمال کریں۔ مثالیں شامل کریں۔")),
        (t("💡 Key Takeaways", "💡 اہم نکات"),
         t("3-5 bullet points summarizing the most important lessons.", "سب سے اہم اسباق خلاصہ کرتے 3-5 bullet points۔")),
        (t("🔚 Conclusion (50-80 words)", "🔚 نتیجہ (50-80 الفاظ)"),
         t("Wrap up + call to action: 'Join Concrete Discord' or 'Try the Vault Tool'", "خلاصہ + call to action: 'کنکریٹ Discord جوائن کریں' یا 'والٹ ٹول آزمائیں'")),
    ]

    for section, desc in structure:
        st.markdown(f"""
        <div style="display:flex; gap:16px; padding:12px 0; border-bottom:1px solid #131B25; align-items:flex-start;">
            <div style="font-family:'Orbitron',monospace; font-size:10px; color:#00FFB2; min-width:180px;">{section}</div>
            <div style="font-size:13px; color:#556070; line-height:1.7;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"### 🔥 {t('Sample AI Prompts for Concrete Articles', 'کنکریٹ آرٹیکل کے لیے AI Prompts')}")

    prompts = [
        t("\"Write a 500-word beginner guide to Concrete Protocol vaults. Explain ERC-4626, ct[Asset] tokens, and how to deposit. Friendly, simple English.\"",
          "\"کنکریٹ پروٹوکول والٹس کے لیے 500 الفاظ کی ابتدائی گائیڈ لکھیں۔ ERC-4626، ct[Asset] ٹوکنز اور ڈپازٹ کا طریقہ سمجھائیں۔ دوستانہ، سادہ اردو۔\""),
        t("\"Explain the difference between standard DeFi yields and Concrete Protocol's protected yield system. Compare risks. 400 words max.\"",
          "\"معیاری DeFi yields اور کنکریٹ پروٹوکول کے محفوظ yield سسٹم میں فرق سمجھائیں۔ خطرات کا موازنہ کریں۔ زیادہ سے زیادہ 400 الفاظ۔\""),
        t("\"Write about why the Health Factor matters in DeFi lending protocols. Use simple analogies. 350 words, include a tip box.\"",
          "\"DeFi lending میں Health Factor کیوں اہم ہے پر لکھیں۔ سادہ مثالیں استعمال کریں۔ 350 الفاظ، ایک ٹِپ بکس شامل کریں۔\""),
        t("\"Create a short comparison article: Aave vs Morpho vs Silo for yield strategies. Pros, cons, best use case for each. 500 words.\"",
          "\"yield حکمت عملیوں کے لیے Aave بمقابلہ Morpho بمقابلہ Silo کا مختصر موازنہ آرٹیکل بنائیں۔ ہر ایک کے فوائد، نقصانات، بہترین استعمال۔ 500 الفاظ۔\""),
    ]

    for p in prompts:
        st.markdown(f"""
        <div style="background:#00FFB208; border:1px solid #00FFB225; border-radius:8px; padding:12px 16px; margin-bottom:10px; font-size:12px; color:#00FFB2; font-style:italic; line-height:1.8;">
        💬 {p}
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="warning-box">
    ⚠️ <b style="color:#FF3D5A;">{t("Important:", "اہم:")}</b> {t(
        "AI-generated content must be reviewed, personalized, and fact-checked before submission. Pure AI copy-paste without any editing is discouraged. Add your voice!",
        "AI سے بنا مواد جمع کرانے سے پہلے جائزہ لیں، ذاتی بنائیں، اور حقائق جانچیں۔ بغیر کسی تدوین کے صرف AI copy-paste کی حوصلہ شکنی کی جاتی ہے۔ اپنی آواز شامل کریں!"
    )}
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════
# TAB 11 — MEMES GUIDE
# ════════════════════════════════════════════════════════════════
with tab_memes:
    st.markdown(f"""
    <div style="font-family:'Orbitron',monospace; font-size:13px; color:#556070; letter-spacing:3px; margin-bottom:20px;">
    😂 {t("CONCRETE MEMES GUIDE — AI & MANUAL", "کنکریٹ میمز گائیڈ — AI اور خود")}
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="guide-card-neon">
        <div style="font-family:'Orbitron',monospace; font-size:12px; color:#00FFB2; margin-bottom:10px; letter-spacing:2px;">
        🗿 {t("WHY MEMES MATTER", "میمز کیوں اہم ہیں")}
        </div>
        <div style="font-size:13px; color:#E8F0F8; line-height:2.0;">
        {t(
            "Memes are one of the fastest ways to earn engagement, XP, and community recognition. A great meme gets shared, earns reactions, and builds your community identity. Daily meme posting is also a KEY condition!",
            "میمز engagement، XP، اور کمیونٹی پہچان حاصل کرنے کا سب سے تیز طریقہ ہیں۔ ایک اچھا میم شیئر ہوتا ہے، reactions ملتے ہیں، اور آپ کی کمیونٹی شناخت بنتی ہے۔ روزانہ میم پوسٹ کرنا KEY شرط بھی ہے!"
        )}
        </div>
    </div>
    """, unsafe_allow_html=True)

    mc1, mc2 = st.columns(2)

    with mc1:
        st.markdown(f"""
        <div class="guide-card-gold">
            <div style="font-family:'Orbitron',monospace; font-size:11px; color:#EDD97A; margin-bottom:10px; letter-spacing:2px;">🤖 {t("AI MEME CREATION", "AI سے میم بنانا")}</div>
            <div style="font-size:13px; color:#E8F0F8; line-height:2.1;">
            <b style="color:#EDD97A;">{t("Image Generation:", "تصویر بنانا:")}</b><br>
            • <span style="color:#00FFB2;">DALL-E 3</span> {t("(ChatGPT Plus)", "(ChatGPT Plus)")}<br>
            • <span style="color:#00FFB2;">Midjourney</span><br>
            • <span style="color:#00FFB2;">Adobe Firefly</span> ({t("free tier available", "مفت ٹیئر دستیاب")})<br>
            • <span style="color:#00FFB2;">Leonardo.ai</span><br><br>
            <b style="color:#EDD97A;">{t("Meme Text Overlay:", "میم پر متن:")}</b><br>
            • <span style="color:#4DA6FF;">Canva</span> ({t("easiest, free", "آسان ترین، مفت")})<br>
            • <span style="color:#4DA6FF;">imgflip.com</span> ({t("quick meme templates", "فوری میم ٹیمپلیٹس")})<br>
            • <span style="color:#4DA6FF;">CapCut</span> ({t("for video memes", "ویڈیو میمز کے لیے")})<br>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with mc2:
        st.markdown(f"""
        <div class="guide-card-neon">
            <div style="font-family:'Orbitron',monospace; font-size:11px; color:#00FFB2; margin-bottom:10px; letter-spacing:2px;">✋ {t("MANUAL MEME CREATION", "خود میم بنانا")}</div>
            <div style="font-size:13px; color:#E8F0F8; line-height:2.1;">
            <b style="color:#00FFB2;">{t("Free Tools:", "مفت ٹولز:")}</b><br>
            • <span style="color:#EDD97A;">Canva.com</span> — {t("drag & drop, best for beginners", "drag & drop، نئے لوگوں کے لیے بہترین")}<br>
            • <span style="color:#EDD97A;">imgflip.com</span> — {t("pick a template, add text, done!", "ٹیمپلیٹ چنیں، متن شامل کریں، تیار!")}<br>
            • <span style="color:#EDD97A;">PicsArt</span> — {t("mobile app, very powerful", "موبائل ایپ، بہت طاقتور")}<br><br>
            <b style="color:#00FFB2;">{t("Process:", "طریقہ:")}</b><br>
            1. {t("Pick a popular meme format", "مشہور میم فارمیٹ چنیں")}<br>
            2. {t("Replace text with Concrete theme", "متن کو کنکریٹ تھیم سے بدلیں")}<br>
            3. {t("Add 🗿 emoji + #ConcreteDeFi", "🗿 ایموجی + #ConcreteDeFi شامل کریں")}<br>
            4. {t("Post in Discord memes channel", "Discord میمز چینل میں پوسٹ کریں")}<br>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"### 💡 {t('Meme Ideas for Concrete 🗿', 'کنکریٹ 🗿 کے لیے میم آئیڈیاز')}")

    meme_ideas = [
        ("😅", t("When you check your ct[Asset] balance and it grew while you slept",
                  "جب آپ سوتے ہوئے ct[Asset] بیلنس چیک کریں اور وہ بڑھ گئی ہو")),
        ("🤓", t("Me explaining ERC-4626 to my friends vs them looking confused",
                  "میں دوستوں کو ERC-4626 سمجھاتا ہوں بمقابلہ وہ الجھے ہوئے")),
        ("🗿", t("Concrete vault holders watching their yield compound automatically",
                  "کنکریٹ والٹ ہولڈرز اپنا yield خودکار compound ہوتے دیکھ رہے ہیں")),
        ("😤", t("Other DeFi protocols manually harvesting vs Concrete doing it automatically",
                  "دوسرے DeFi پروٹوکولز manually harvesting بمقابلہ کنکریٹ خودکار")),
        ("💪", t("Level 1 Newcomer vs Level 25 Grindoor in Concrete Discord",
                  "کنکریٹ Discord میں لیول 1 Newcomer بمقابلہ لیول 25 Grindoor")),
        ("😂", t("When someone asks 'is DeFi safe?' and you have your Concrete health factor at 2.5",
                  "جب کوئی پوچھے 'DeFi محفوظ ہے؟' اور آپ کا Concrete health factor 2.5 ہو")),
        ("🚀", t("After submitting your first article and getting the Writer badge",
                  "پہلا آرٹیکل جمع کرا کے Writer بیج ملنے کے بعد")),
        ("🗿", t("Moai watching hodlers panic sell while vault yield keeps compounding",
                  "موآئی panic sell کرنے والوں کو دیکھ رہا ہے جبکہ والٹ yield بڑھتی رہتی ہے")),
    ]

    idea_cols = st.columns(2)
    for i, (em, idea) in enumerate(meme_ideas):
        with idea_cols[i % 2]:
            st.markdown(f"""
            <div style="background:var(--bg-card); border:1px solid var(--border); border-radius:8px; padding:12px 14px; margin-bottom:10px; display:flex; gap:10px; align-items:flex-start;">
                <span style="font-size:22px;">{em}</span>
                <span style="font-size:12px; color:#556070; line-height:1.7;">{idea}</span>
            </div>
            """, unsafe_allow_html=True)

    st.markdown(f"### 🤖 {t('AI Prompts for Concrete Meme Images', 'کنکریٹ میم تصاویر کے لیے AI Prompts')}")

    ai_meme_prompts = [
        t("\"Easter Island stone statue (moai) sitting in front of a computer watching DeFi yield charts go up, glowing green, cyberpunk style, neon lighting\"",
          "\"Easter Island پتھر کی مجسمہ (moai) کمپیوٹر کے سامنے بیٹھا DeFi yield charts اوپر جاتے دیکھ رہا ہے، سبز چمک، cyberpunk انداز، neon روشنی\""),
        t("\"Stone moai statue wearing a top hat and suit, holding a bag of coins labeled 'YIELD', smiling confidently, dark background with neon green accents\"",
          "\"پتھر کا موآئی مجسمہ top hat اور سوٹ پہنے، 'YIELD' لکھا سکوں کا تھیلا پکڑے، اعتماد سے مسکراتے ہوئے، dark پس منظر، neon سبز accent\""),
        t("\"Dramatic split image: left side dark chaotic DeFi market crashing, right side peaceful moai statue with green glowing vault shield, cinematic\"",
          "\"ڈرامائی تقسیم تصویر: بائیں طرف DeFi مارکیٹ کریش، دائیں طرف سبز چمکتی والٹ شیلڈ کے ساتھ پرسکون موآئی مجسمہ، سینماٹک\""),
    ]

    for ap in ai_meme_prompts:
        st.markdown(f"""
        <div style="background:#9B59FF08; border:1px solid #9B59FF25; border-radius:8px; padding:12px 16px; margin-bottom:10px; font-size:12px; color:#9B59FF; font-style:italic; line-height:1.8;">
        🎨 {ap}
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="tip-box">
    💡 <b>{t("Meme Strategy:", "میم حکمت عملی:")}</b> {t(
        "Post 1 meme in the morning + 1 in the evening. React to others' memes too. Consistency beats quality — post daily even if simple!",
        "صبح 1 میم + شام 1 میم پوسٹ کریں۔ دوسروں کے میمز پر بھی react کریں۔ مستقل مزاجی معیار سے بہتر ہے — روزانہ پوسٹ کریں چاہے سادہ ہو!"
    )}
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════
# TAB 12 — TWITTER GUIDE
# ════════════════════════════════════════════════════════════════
with tab_twitter:
    st.markdown(f"""
    <div style="font-family:'Orbitron',monospace; font-size:13px; color:#556070; letter-spacing:3px; margin-bottom:20px;">
    🐦 {t("TWITTER/X GUIDE — CONCRETE POSTS", "ٹوئٹر/X گائیڈ — کنکریٹ پوسٹس")}
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="guide-card-neon">
        <div style="font-family:'Orbitron',monospace; font-size:12px; color:#00FFB2; margin-bottom:10px; letter-spacing:2px;">
        📊 {t("WHY TWITTER MATTERS FOR CONCRETE", "کنکریٹ کے لیے Twitter کیوں اہم ہے")}
        </div>
        <div style="font-size:13px; color:#E8F0F8; line-height:2.0;">
        {t(
            "Twitter/X is the main platform for DeFi communities. Posting about Concrete helps:<br>• Build the protocol's visibility<br>• Earn community recognition (KEY condition: 2-3 posts/day)<br>• Attract new members to Discord<br>• Show your expertise and earn more XP",
            "Twitter/X DeFi کمیونٹیز کا مرکزی پلیٹ فارم ہے۔ کنکریٹ کے بارے میں پوسٹ کرنے سے:<br>• پروٹوکول کی مرئیت بڑھتی ہے<br>• کمیونٹی پہچان ملتی ہے (KEY شرط: روزانہ 2-3 پوسٹس)<br>• Discord میں نئے اراکین آتے ہیں<br>• اپنی مہارت ظاہر کریں اور زیادہ XP کمائیں"
        )}
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"### 📝 {t('7 Types of Tweets You Can Make', '7 قسم کے ٹوئٹس جو آپ کر سکتے ہیں')}")

    tweet_types = [
        ("📚", t("Educational Thread", "تعلیمی Thread"),
         t("Explain a concept like ERC-4626, Health Factor, ct[Asset] tokens in 3-5 tweets. Number each tweet 1/5, 2/5 etc.", "ERC-4626، Health Factor، ct[Asset] ٹوکنز جیسا تصور 3-5 ٹوئٹس میں سمجھائیں۔ ہر ٹوئٹ نمبر کریں 1/5، 2/5 وغیرہ۔"),
         "#4DA6FF",
         t("\"🧵 What is ERC-4626? A thread for DeFi beginners:\n\n1/ ERC-4626 is Ethereum's standard for yield vaults...\n\n#ConcreteDeFi #DeFi\"",
           "\"🧵 ERC-4626 کیا ہے؟ DeFi نئے لوگوں کے لیے thread:\n\n1/ ERC-4626 Ethereum کا yield vaults معیار ہے...\n\n#ConcreteDeFi #DeFi\"")),
        ("💰", t("Yield Update", "Yield اپڈیٹ"),
         t("Share current APY rates, vault performance, or protocol stats. Always add a disclaimer.", "موجودہ APY شرحیں، والٹ کارکردگی، یا پروٹوکول اعداد شیئر کریں۔ ہمیشہ disclaimer شامل کریں۔"),
         "#00FFB2",
         t("\"📊 @ConcreteXYZ vault update:\n\n• USDC Yield: ~9.1% APY\n• WeETH: ~7.8% APY\n• WETH Alpha: ~11.2% APY\n\nAll auto-compounding. No claiming needed 🗿\n\n#ConcreteDeFi #NotFinancialAdvice\"",
           "\"📊 @ConcreteXYZ والٹ اپڈیٹ:\n\n• USDC Yield: ~9.1% APY\n• WeETH: ~7.8% APY\n• WETH Alpha: ~11.2% APY\n\nسب auto-compounding۔ کوئی claiming نہیں 🗿\n\n#ConcreteDeFi #NotFinancialAdvice\"")),
        ("🗿", t("Meme Tweet", "میم ٹوئٹ"),
         t("Post your meme image with a short caption. 1-2 lines max. Let the meme do the talking.", "اپنی میم تصویر مختصر caption کے ساتھ پوسٹ کریں۔ زیادہ سے زیادہ 1-2 لائنیں۔ میم خود بولے۔"),
         "#EDD97A",
         t("\"Concrete vault holders watching their yield grow while sleeping 🗿\n\nSet it. Forget it. Compound. 💚\n\n#ConcreteDeFi\"",
           "\"کنکریٹ والٹ ہولڈرز سوتے ہوئے yield بڑھتے دیکھ رہے ہیں 🗿\n\nلگاؤ۔ بھول جاؤ۔ Compound۔ 💚\n\n#ConcreteDeFi\"")),
        ("📖", t("Article Promo", "آرٹیکل پروموشن"),
         t("When you publish an article on Mirror/Paragraph, tweet about it with the link.", "جب Mirror/Paragraph پر آرٹیکل شائع کریں، link کے ساتھ tweet کریں۔"),
         "#9B59FF",
         t("\"📝 Just published my guide on Concrete Protocol vaults!\n\nCovers:\n✅ How ERC-4626 works\n✅ ct[Asset] token mechanics\n✅ Risk management tips\n\nRead it here 👇\n[your link]\n\n#ConcreteDeFi #DeFi\"",
           "\"📝 کنکریٹ پروٹوکول والٹس پر اپنی گائیڈ شائع کر دی!\n\nشامل ہے:\n✅ ERC-4626 کیسے کام کرتا ہے\n✅ ct[Asset] ٹوکن mechanics\n✅ رسک مینجمنٹ tips\n\nیہاں پڑھیں 👇\n[آپ کا link]\n\n#ConcreteDeFi #DeFi\"")),
        ("🙋", t("Community Shoutout", "کمیونٹی Shoutout"),
         t("Tag @ConcreteXYZ, mention Discord activity, shoutout to team or fellow members.", "@ConcreteXYZ ٹیگ کریں، Discord سرگرمی بتائیں، ٹیم یا ساتھی اراکین کو shoutout دیں۔"),
         "#E8A020",
         t("\"Loving the @ConcreteXYZ community vibes today 🗿\n\nActive Discord, helpful members, building together. This is what DeFi should look like.\n\nJoin us 👇 discord.gg/concrete\n\n#ConcreteDeFi #Community\"",
           "\"آج @ConcreteXYZ کمیونٹی کا ماحول بہت اچھا ہے 🗿\n\nفعال Discord، مددگار اراکین، مل کر تعمیر۔ DeFi ایسا ہی ہونا چاہیے۔\n\nہمارے ساتھ شامل ہوں 👇 discord.gg/concrete\n\n#ConcreteDeFi #Community\"")),
        ("❓", t("Question/Poll Tweet", "سوال/Poll ٹوئٹ"),
         t("Ask DeFi-related questions to spark engagement. Polls get high interaction.", "DeFi سے متعلق سوالات پوچھیں engagement بڑھانے کے لیے۔ Polls زیادہ interaction پاتے ہیں۔"),
         "#FF7A2F",
         t("\"🗿 Quick poll for DeFi users:\n\nWhen choosing a yield vault, what matters MOST to you?\n\n🟢 Highest APY\n🔵 Lowest Risk\n🟡 Brand Reputation\n⚪ Auto-compounding\n\n#ConcreteDeFi #DeFi\"",
           "\"🗿 DeFi users کے لیے فوری poll:\n\nyield vault چنتے وقت آپ کو سب سے زیادہ کیا اہمیت دیتا ہے؟\n\n🟢 سب سے زیادہ APY\n🔵 سب سے کم خطرہ\n🟡 برانڈ ساکھ\n⚪ Auto-compounding\n\n#ConcreteDeFi #DeFi\"")),
        ("🔁", t("Retweet + Comment", "Retweet + تبصرہ"),
         t("Find Concrete's official tweets, RT with your own insights added. Easy engagement!", "کنکریٹ کے آفیشل tweets تلاش کریں، اپنی رائے شامل کر کے RT کریں۔ آسان engagement!"),
         "#556070",
         t("\"Exactly this 🗿 I've been using @ConcreteXYZ vaults for [X] weeks and the auto-compounding is a game changer. No more manual harvesting!\"",
           "\"بالکل یہی 🗿 میں [X] ہفتوں سے @ConcreteXYZ والٹس استعمال کر رہا ہوں اور auto-compounding game changer ہے۔ اب manual harvesting نہیں!\"")),
    ]

    for icon, ttype, tdesc, color, example in tweet_types:
        with st.expander(f"{icon} {ttype}"):
            st.markdown(f"""
            <div style="font-size:13px; color:#556070; line-height:1.8; margin-bottom:14px;">{tdesc}</div>
            <div style="font-family:'Share Tech Mono',monospace; background:{color}08; border:1px solid {color}33; border-radius:8px; padding:14px 16px; font-size:12px; color:{color}; white-space:pre-wrap; line-height:1.8;">
{example}
            </div>
            """, unsafe_allow_html=True)

    st.markdown(f"### 📌 {t('Essential Hashtags & Tags', 'ضروری Hashtags اور Tags')}")

    st.markdown(f"""
    <div class="guide-card-gold">
        <div style="font-family:'Orbitron',monospace; font-size:11px; color:#EDD97A; margin-bottom:10px; letter-spacing:2px;">#️⃣ {t("ALWAYS USE THESE", "ہمیشہ یہ استعمال کریں")}</div>
        <div style="display:flex; flex-wrap:wrap; gap:8px; margin-bottom:14px;">
            <span class="tag-neon">#ConcreteDeFi</span>
            <span class="tag-gold">#Concrete</span>
            <span class="tag-blue">#DeFi</span>
            <span class="tag-neon">#ERC4626</span>
            <span class="tag-gold">@ConcreteXYZ</span>
            <span class="tag-blue">#YieldFarming</span>
            <span class="tag-neon">#Ethereum</span>
        </div>
        <div style="font-family:'Orbitron',monospace; font-size:11px; color:#4DA6FF; margin-bottom:8px; letter-spacing:2px;">🎯 {t("OPTIONAL CONTEXT TAGS", "اختیاری context tags")}</div>
        <div style="display:flex; flex-wrap:wrap; gap:8px;">
            <span class="tag-blue">#NotFinancialAdvice</span>
            <span class="tag-gold">#DYOR</span>
            <span class="tag-neon">#Web3</span>
            <span class="tag-blue">#Aave</span>
            <span class="tag-neon">#Morpho</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="guide-card-neon">
        <div style="font-family:'Orbitron',monospace; font-size:11px; color:#00FFB2; margin-bottom:10px; letter-spacing:2px;">⏰ {t("DAILY TWITTER ROUTINE (2-3 posts/day)", "روزانہ Twitter معمول (روزانہ 2-3 پوسٹس)")}</div>
        <div style="font-size:13px; color:#E8F0F8; line-height:2.2;">
        🌅 <b>{t("Morning", "صبح")}</b> — {t("Educational/Info tweet or meme", "تعلیمی/Info ٹوئٹ یا میم")}<br>
        ☀️ <b>{t("Afternoon", "دوپہر")}</b> — {t("Retweet @ConcreteXYZ with comment", "@ConcreteXYZ کو تبصرے کے ساتھ RT")}<br>
        🌙 <b>{t("Evening", "شام")}</b> — {t("Community shoutout or poll or meme", "کمیونٹی shoutout یا poll یا میم")}<br>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="tip-box">
    💡 <b>{t("Twitter Tips:", "Twitter Tips:")}</b> {t(
        "Use Concrete's branding colors in images (neon green #00FFB2, gold #EDD97A). Always tag @ConcreteXYZ. Engage with replies quickly — Twitter rewards fast engagement. 🗿",
        "تصاویر میں کنکریٹ کے رنگ استعمال کریں (neon سبز #00FFB2، سونا #EDD97A)۔ ہمیشہ @ConcreteXYZ ٹیگ کریں۔ جوابات پر جلدی engage کریں — Twitter تیز engagement کو reward کرتا ہے۔ 🗿"
    )}
    </div>
    """, unsafe_allow_html=True)
