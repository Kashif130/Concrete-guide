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
</style>
""", unsafe_allow_html=True)

# ─── Header ───────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; padding: 30px 0 20px;">
    <div style="font-family:'Orbitron',monospace; font-size:42px; font-weight:900; color:#00FFB2; letter-spacing:6px; text-shadow: 0 0 40px #00FFB260;">
        🗿 CONCRETE 101
    </div>
    <div style="font-family:'Share Tech Mono',monospace; font-size:14px; color:#EDD97A; letter-spacing:4px; margin-top:8px;">
        THE COMPLETE BEGINNER GUIDE — VAULTS · XP · ROLES · MOAI · BADGES
    </div>
    <div style="font-size:11px; color:#2A3540; letter-spacing:2px; margin-top:6px;">
        written by community · for community · one team. one vision.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ─── Sidebar Nav ───────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="font-family:'Orbitron',monospace; font-size:11px; color:#00FFB2; letter-spacing:3px; margin-bottom:16px;">
    🗿 CONCRETE GUIDE
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="font-size:11px; color:#556070; line-height:1.8; margin-bottom:20px;">
    📌 Quick Links:
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
    st.markdown("""
    <div style="font-size:10px; color:#2A3540; letter-spacing:2px; line-height:1.8;">
    ⚠ NOT FINANCIAL ADVICE<br>
    COMMUNITY TOOL<br>
    DYOR BEFORE INVESTING
    </div>
    """, unsafe_allow_html=True)

# ─── Main Tabs ─────────────────────────────────────────────────────────────────
tabs = st.tabs([
    "🚀 START HERE",
    "🏦 VAULTS 101",
    "🔑 ACCESS ROLES",
    "🏆 XP & LEVELS",
    "🗿 MOAI & BADGES",
    "📝 ARTICLES",
    "🛠️ VAULT TOOL",
    "❓ FAQ",
])

# ════════════════════════════════════════════════════════════════
# TAB 1 — START HERE
# ════════════════════════════════════════════════════════════════
with tabs[0]:
    st.markdown("""
    <div style="font-family:'Orbitron',monospace; font-size:13px; color:#556070; letter-spacing:3px; margin-bottom:20px;">
    👋 WELCOME TO CONCRETE LAND
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Protocol", "Concrete.XYZ", "ERC-4626 Vaults")
    with col2:
        st.metric("Chain", "Ethereum Mainnet", "Live & Audited")
    with col3:
        st.metric("Community", "Growing Fast", "Join Discord")

    st.markdown("---")

    st.markdown("""
    <div class="guide-card-neon">
        <div style="font-family:'Orbitron',monospace; font-size:12px; color:#00FFB2; letter-spacing:3px; margin-bottom:14px;">
        🧱 CONCRETE KYA HAI?
        </div>
        <div style="font-size:13px; color:#E8F0F8; line-height:2;">
        Concrete ek <b style="color:#00FFB2;">DeFi yield protocol</b> hai jo tumhara capital automatically best strategies mein deploy karta hai — Aave V3, Morpho, Silo, Radiant.
        <br><br>
        Tum ek vault mein deposit karte ho → Concrete woh capital manage karta hai → tum yield kamate ho.
        <br><br>
        Simple. Efficient. Protected. 🗿
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🗺️ Roadmap for Beginners")

    steps = [
        ("STEP 1", "Discord Join Karo", "Concrete ki community join karo — yahan se XP milna shuru hota hai. Chat karo, engage karo, seekho.", "#00FFB2"),
        ("STEP 2", "concrete.xyz Visit Karo", "Official website pe jao, vaults explore karo, docs padho. Apne aap ko familiar karo.", "#EDD97A"),
        ("STEP 3", "Vault Tool Use Karo", "Hamara community-built Vault Intelligence Terminal use karo — APY dekho, risk samjho, simulate karo.", "#4DA6FF"),
        ("STEP 4", "XP Earn Karo", "Chat karo, articles likho, badges lo — Level 5 pe Newbie Role milti hai (50 BAGS reward!).", "#9B59FF"),
        ("STEP 5", "Deposit Karo (DYOR)", "Jab ready ho, vault mein deposit karo. Small amount se shuru karo. Risk samjho.", "#E8A020"),
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

    st.markdown("""
    <div class="tip-box">
    💡 <b>Pro Tip:</b> Concrete Discord pe active rehna sabse important hai — XP wahan milta hai, community wahan hai, aur latest updates wahan aate hain.
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════
# TAB 2 — VAULTS 101
# ════════════════════════════════════════════════════════════════
with tabs[1]:
    st.markdown("""
    <div style="font-family:'Orbitron',monospace; font-size:13px; color:#556070; letter-spacing:3px; margin-bottom:20px;">
    🏦 VAULTS — SAMAJHNA SHURU KARO
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="guide-card-neon">
        <div style="font-family:'Orbitron',monospace; font-size:12px; color:#00FFB2; margin-bottom:12px; letter-spacing:2px;">
        ERC-4626 VAULT KYA HOTA HAI?
        </div>
        <div style="font-size:13px; color:#E8F0F8; line-height:2.0;">
        ERC-4626 ek Ethereum standard hai yield-bearing vaults ke liye.<br>
        Tum <b style="color:#00FFB2;">WETH, USDC, weETH</b> deposit karte ho → vault tumhe <b style="color:#EDD97A;">ct[Asset] tokens</b> deta hai → in tokens ki value automatically badh'ti rehti hai jaise yield milta hai.<br><br>
        Kabhi manually kuch harvest nahi karna. Compound automatic hai.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📦 Available Vaults")

    vaults = [
        {
            "name": "🏦 WeETH (Institutional)",
            "asset": "WETH",
            "apy": "~7.84%",
            "strategy": "Institutional Restaking — Aave V3 + Silo",
            "risk": "LOW",
            "risk_color": "#00FFB2",
            "tvl": "$281M+",
            "desc": "Sabse safe vault. Institutional-grade restaking strategy. Long-term holders ke liye best."
        },
        {
            "name": "💎 USDC Yield",
            "asset": "USDC",
            "apy": "~9.10%",
            "strategy": "Stablecoin Multi-Strategy — Morpho + Aave",
            "risk": "LOW-MED",
            "risk_color": "#EDD97A",
            "tvl": "$134M+",
            "desc": "Stable asset pe yield. Impermanent loss nahi. Conservative investors ke liye perfect."
        },
        {
            "name": "🔥 WETH Alpha",
            "asset": "WETH",
            "apy": "~11.2%",
            "strategy": "Aggressive Restaking — Radiant + Silo",
            "risk": "MEDIUM",
            "risk_color": "#E8A020",
            "tvl": "$89M+",
            "desc": "Higher APY, higher risk. Active monitoring recommended."
        },
        {
            "name": "⚡ cbBTC Vault",
            "asset": "cbBTC",
            "apy": "~6.50%",
            "strategy": "BTC Yield — Morpho Blue",
            "risk": "LOW-MED",
            "risk_color": "#EDD97A",
            "tvl": "$45M+",
            "desc": "Bitcoin holders ke liye yield. Wrapped BTC pe conservative strategy."
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
                <div style="font-size:11px; color:#556070; margin-bottom:6px;">📋 Strategy: {v['strategy']}</div>
                <div style="font-size:11px; color:#556070; margin-bottom:6px;">💰 TVL: {v['tvl']} &nbsp;|&nbsp; 🪙 Asset: {v['asset']}</div>
                <div style="font-size:12px; color:#E8F0F8; margin-top:8px;">{v['desc']}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 💡 Deposit Kaise Karte Hain — Step by Step")

    deposit_steps = [
        "**concrete.xyz** open karo browser mein",
        "**Connect Wallet** karo (MetaMask ya Coinbase Wallet)",
        "Apna **asset** select karo (WETH, USDC, etc.)",
        "**Amount enter** karo — chhota amount se start karo",
        "**Approve** transaction sign karo (one-time per token)",
        "**Deposit** karo — ct[Asset] tokens tumhare wallet mein aa jaenge",
        "**ct tokens ki value** automatically grow kari hai — kuch karna nahi!",
    ]

    for i, s in enumerate(deposit_steps, 1):
        st.markdown(f"""
        <div style="display:flex; gap:14px; align-items:flex-start; padding:10px 0; border-bottom:1px solid #131B25;">
            <span style="font-family:'Orbitron',monospace; font-size:11px; color:#00FFB2; background:#00FFB210; border:1px solid #00FFB233; padding:3px 8px; border-radius:4px; min-width:28px; text-align:center;">{i}</span>
            <span style="font-size:13px; color:#E8F0F8; line-height:1.6;">{s}</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div class="guide-card-gold">
        <div style="font-family:'Orbitron',monospace; font-size:12px; color:#EDD97A; margin-bottom:10px; letter-spacing:2px;">🪙 CT[ASSET] TOKEN KYA HOTA HAI?</div>
        <div style="font-size:13px; color:#E8F0F8; line-height:2.0;">
        Jab tum deposit karte ho, vault tumhe <b style="color:#EDD97A;">ct[Asset]</b> tokens deta hai (e.g., ctWETH, ctUSDC).<br>
        <br>
        • Yeh tokens ERC-20 hain — transfer, hold, sell kar sakte ho<br>
        • In ki value <b>automatically appreciate</b> hoti hai (vault yield earn karta hai)<br>
        • Withdraw karte waqt in tokens ko burn karo aur underlying asset wapis lo<br>
        • <b style="color:#EDD97A;">Koi claiming nahi. Koi compounding button nahi. Set and forget!</b>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="warning-box">
    ⚠️ <b style="color:#FF3D5A;">RISK REMINDER:</b> DeFi mein risk hota hai. Smart contract bugs, liquidation, market volatility — sab possible hai.
    Sirf woh amount deposit karo jo lose afford kar sako. DYOR. Yeh financial advice nahi hai.
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════
# TAB 3 — ACCESS ROLES
# ════════════════════════════════════════════════════════════════
with tabs[2]:
    st.markdown("""
    <div style="font-family:'Orbitron',monospace; font-size:13px; color:#556070; letter-spacing:3px; margin-bottom:20px;">
    🔑 ACCESS ROLES — UNLOCK KAISA KAREN
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="guide-card-neon">
        <div style="font-size:13px; color:#E8F0F8; line-height:2.0;">
        Concrete Discord pe <b style="color:#00FFB2;">roles</b> hote hain jo tumhara status aur access define karte hain.<br>
        XP earn karo → Level up karo → Special roles aur channels unlock karo.
        </div>
    </div>
    """, unsafe_allow_html=True)

    roles = [
        {
            "name": "👶 Newcomer",
            "unlock": "Discord join karte hi milti hai",
            "level": "Level 1",
            "perks": ["Basic channels access", "Community chat", "XP earn karna shuru"],
            "color": "#556070"
        },
        {
            "name": "🗿 Newbie",
            "unlock": "Level 5 — 380 XP",
            "level": "Level 5",
            "perks": ["Newbie Role + 50 BAGS reward!", "More channels access", "Community recognized member"],
            "color": "#4DA6FF"
        },
        {
            "name": "🧭 Vault Navigator",
            "unlock": "Level 10 — 955 XP",
            "level": "Level 10",
            "perks": ["Vault Navigator Role + 150 BAGS!", "Vault discussions access", "Protocol updates early"],
            "color": "#00FFB2"
        },
        {
            "name": "☘️ Lucky 17",
            "unlock": "Level 17 — 2180 XP",
            "level": "Level 17",
            "perks": ["Lucky 17 Role + 250 BAGS!", "Exclusive community events", "Special Discord channels"],
            "color": "#EDD97A"
        },
        {
            "name": "🏆 Grindooor",
            "unlock": "Level 25 — 4180 XP",
            "level": "Level 25",
            "perks": ["Grindooor Role + 1000 BAGS!", "Top community member status", "Maximum perks aur recognition"],
            "color": "#E8A020"
        },
        {
            "name": "📝 Writer / Contributor",
            "unlock": "Quality article submit karo",
            "level": "Merit-based",
            "perks": ["Writer badge", "Extra XP per article", "Community visibility"],
            "color": "#9B59FF"
        },
    ]

    for r in roles:
        with st.expander(f"{r['name']} — {r['level']}"):
            col_x, col_y = st.columns([2, 1])
            with col_x:
                st.markdown(f"""
                <div style="font-size:13px; color:{r['color']}; font-family:'Orbitron',monospace; margin-bottom:10px;">Unlock: {r['unlock']}</div>
                <div style="font-size:13px; color:#E8F0F8; margin-bottom:8px;"><b>Perks:</b></div>
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
    st.markdown("""
    <div class="guide-card-gold">
        <div style="font-family:'Orbitron',monospace; font-size:12px; color:#EDD97A; margin-bottom:10px; letter-spacing:2px;">💰 BAGS KYA HAIN?</div>
        <div style="font-size:13px; color:#E8F0F8; line-height:2.0;">
        BAGS Concrete ki community reward currency hai. Level up karne pe milti hai.<br>
        <br>
        • <b style="color:#EDD97A;">50 BAGS</b> — Level 5 (Newbie Role)<br>
        • <b style="color:#EDD97A;">150 BAGS</b> — Level 10 (Vault Navigator)<br>
        • <b style="color:#EDD97A;">250 BAGS</b> — Level 17 (Lucky 17)<br>
        • <b style="color:#EDD97A;">1000 BAGS</b> — Level 25 (Grindooor)<br>
        <br>
        Exact utility future mein announce hogi — hold karte raho!
        </div>
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════
# TAB 4 — XP & LEVELS
# ════════════════════════════════════════════════════════════════
with tabs[3]:
    st.markdown("""
    <div style="font-family:'Orbitron',monospace; font-size:13px; color:#556070; letter-spacing:3px; margin-bottom:20px;">
    🏆 XP SYSTEM — LEVEL UP KARO
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="guide-card-neon">
        <div style="font-size:13px; color:#E8F0F8; line-height:2.0;">
        Concrete Discord pe <b style="color:#00FFB2;">chat karke XP milta hai</b>. Jitna engage karo, utna XP milega, utna level up hoga.
        Har level pe naya milestone — kuch levels pe <b style="color:#EDD97A;">special roles aur BAGS rewards</b> milte hain.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📊 Complete Level Table")

    levels_data = [
        (1, 100, None, None),
        (2, 155, None, None),
        (3, 220, None, None),
        (4, 295, None, None),
        (5, 380, "🗿 NEWBIE ROLE", "50 BAGS"),
        (6, 475, None, None),
        (7, 580, None, None),
        (8, 695, None, None),
        (9, 820, None, None),
        (10, 955, "🧭 VAULT NAVIGATOR", "150 BAGS"),
        (11, 1100, None, None),
        (12, 1250, None, None),
        (13, 1420, None, None),
        (14, 1590, None, None),
        (15, 1780, None, None),
        (16, 1980, None, None),
        (17, 2180, "☘️ LUCKY 17 ROLE", "250 BAGS"),
        (18, 2400, None, None),
        (19, 2620, None, None),
        (20, 3000, None, None),
        (22, 3350, None, None),
        (23, 3620, None, None),
        (24, 3900, None, None),
        (25, 4180, "🏆 GRINDOOOR ROLE", "1000 BAGS"),
    ]

    st.markdown("""
    <div style="background:var(--bg-card); border:1px solid var(--border); border-radius:10px; overflow:hidden; margin-bottom:20px;">
        <div style="display:flex; padding:12px 16px; background:#090D14; border-bottom:1px solid #1E2D40; font-family:'Orbitron',monospace; font-size:10px; color:#2A3540; letter-spacing:2px;">
            <span style="width:80px;">LEVEL</span>
            <span style="width:120px;">XP NEEDED</span>
            <span style="flex:1;">MILESTONE</span>
            <span style="width:120px;">REWARD</span>
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

    st.markdown("### ⚡ XP Fast Earn Karne ke Tips")

    tips = [
        ("💬 Daily Chat", "Har roz Discord pe active raho. Messages = XP. Quality over quantity."),
        ("📝 Articles Likho", "Community articles zyada XP dete hain. Topic: vaults, DeFi, Concrete features."),
        ("🤝 Dooston Ko Invite Karo", "Referral se bhi XP milta hai. Apna Discord invite link share karo."),
        ("🎯 Events Participate Karo", "Concrete ke AMAs, Twitter Spaces, aur community events mein hissa lo."),
        ("❓ Questions Poochho/Jawab Do", "Helpful replies aur questions bhi engagement count hote hain."),
    ]

    for icon_title, desc in tips:
        st.markdown(f"""
        <div style="display:flex; gap:16px; padding:12px 0; border-bottom:1px solid #131B25; align-items:flex-start;">
            <div style="font-size:13px; color:#00FFB2; font-weight:700; min-width:160px; font-family:'Orbitron',monospace; font-size:10px;">{icon_title}</div>
            <div style="font-size:13px; color:#556070; line-height:1.7;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════
# TAB 5 — MOAI & BADGES
# ════════════════════════════════════════════════════════════════
with tabs[4]:
    st.markdown("""
    <div style="font-family:'Orbitron',monospace; font-size:13px; color:#556070; letter-spacing:3px; margin-bottom:20px;">
    🗿 MOAI NFT & BADGES — IDENTITY SYSTEM
    </div>
    """, unsafe_allow_html=True)

    col_m1, col_m2 = st.columns(2)

    with col_m1:
        st.markdown("""
        <div class="guide-card-gold">
            <div style="font-family:'Orbitron',monospace; font-size:12px; color:#EDD97A; margin-bottom:12px; letter-spacing:2px;">🗿 MOAI KYA HAI?</div>
            <div style="font-size:13px; color:#E8F0F8; line-height:2.0;">
            Moai Concrete ka mascot/identity hai — Easter Island stone figure inspired.<br><br>
            Community mein moai reference ho to samjho: <b style="color:#EDD97A;">solid, reliable, unshakeable</b> — jaise Concrete protocol khud.<br><br>
            🗿 = Concrete family ka symbol.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_m2:
        st.markdown("""
        <div class="guide-card-neon">
            <div style="font-family:'Orbitron',monospace; font-size:12px; color:#00FFB2; margin-bottom:12px; letter-spacing:2px;">🏅 BADGES KYA HOTE HAIN?</div>
            <div style="font-size:13px; color:#E8F0F8; line-height:2.0;">
            Badges achievements ke liye milte hain:<br><br>
            • <b style="color:#00FFB2;">Level Badges</b> — XP milestones pe<br>
            • <b style="color:#EDD97A;">Contributor Badge</b> — articles/content pe<br>
            • <b style="color:#9B59FF;">Special Badges</b> — events/competitions pe<br>
            • <b style="color:#E8A020;">OG Badge</b> — early community members ko
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🏅 Badge Types — Complete Guide")

    badges = [
        ("🗿", "Moai OG", "Early community mein join karne wale members ko milta hai. Rare aur prestigious.", "#EDD97A"),
        ("⭐", "Newbie", "Level 5 complete karne pe milta hai. Tumhara pehla achievement badge.", "#4DA6FF"),
        ("🧭", "Vault Navigator", "Level 10 milestone. Vault knowledge ka proof.", "#00FFB2"),
        ("☘️", "Lucky 17", "Level 17 — ek special number Concrete community mein.", "#9B59FF"),
        ("🏆", "Grindooor", "Level 25 — highest badge. Sirf true dedicated members ko milta hai.", "#E8A020"),
        ("📝", "Writer", "Community articles ya guides likhne pe milta hai.", "#FF7A2F"),
        ("🤝", "Contributor", "Protocol development, tools, ya content mein significant contribution.", "#4DA6FF"),
        ("⚡", "Event Champion", "Community events aur competitions mein win karne pe.", "#FF3D5A"),
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
    st.markdown("""
    <div class="tip-box">
    💡 <b>Moai Wisdom:</b> "Be like Moai — solid, immovable, always facing forward." Community strong hai jab sab ek saath build karte hain. 🗿
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════
# TAB 6 — ARTICLES
# ════════════════════════════════════════════════════════════════
with tabs[5]:
    st.markdown("""
    <div style="font-family:'Orbitron',monospace; font-size:13px; color:#556070; letter-spacing:3px; margin-bottom:20px;">
    📝 ARTICLE SUBMISSION — CONTRIBUTE & EARN
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="guide-card-gold">
        <div style="font-family:'Orbitron',monospace; font-size:12px; color:#EDD97A; margin-bottom:12px; letter-spacing:2px;">📝 ARTICLE PROGRAM KYA HAI?</div>
        <div style="font-size:13px; color:#E8F0F8; line-height:2.0;">
        Concrete community members ko encourage karta hai ke woh <b style="color:#EDD97A;">educational content</b> create karen.<br>
        Agar tumhara article accept hota hai → <b style="color:#00FFB2;">extra XP milta hai + Writer badge + community visibility</b>.<br><br>
        Yeh ek acha tarika hai level fast karne ka aur apna naam community mein banane ka.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### ✅ Article Kaise Submit Karen — Step by Step")

    article_steps = [
        ("IDEA", "Topic choose karo", "Concrete ke baare mein kuch likho — vault guide, DeFi concept explain karo, risk management, ya apna experience share karo."),
        ("DRAFT", "Article likho", "Clear aur simple language use karo. Hindi ya English — dono accepted. Screenshots add karo jahan helpful ho."),
        ("FORMAT", "Proper format karo", "Title, intro, main content, conclusion. Headings use karo. 300-1000 words ideal hai."),
        ("SUBMIT", "Discord pe submit karo", "#article-submission channel dhundho. Wahan apna article paste ya link karo."),
        ("REVIEW", "Wait for review", "Concrete team ya mods review karte hain. 1-3 din lag sakte hain."),
        ("REWARD", "XP + Badge lo", "Accept hone pe Writer badge milti hai + bonus XP. Congratulations!"),
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
    st.markdown("### 💡 Article Topics — Inspiration")

    topics = [
        "Concrete vaults — beginner guide",
        "ERC-4626 kya hota hai?",
        "DeFi mein risk management",
        "Health Factor kya hota hai aur kyu important hai",
        "ct[Asset] tokens ka mechanics",
        "Aave vs Morpho vs Silo — strategy comparison",
        "Mera pehla Concrete deposit — experience share",
        "Concrete XP system samjhaya",
        "Community building in DeFi",
        "Smart contract audits kyu zaroori hain",
    ]

    t_cols = st.columns(2)
    for i, topic in enumerate(topics):
        with t_cols[i % 2]:
            st.markdown(f"""
            <div style="padding:8px 12px; background:var(--bg-card); border:1px solid var(--border); border-radius:6px; margin-bottom:8px; font-size:12px; color:#556070;">
            💡 {topic}
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div class="tip-box">
    💡 <b>Writing Tip:</b> Khud jo seekha hai woh share karo — authentic experience sabse zyada engage karta hai. Perfect writing ki zaroorat nahi, honest writing chahiye!
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════
# TAB 7 — VAULT TOOL
# ════════════════════════════════════════════════════════════════
with tabs[6]:
    st.markdown("""
    <div style="font-family:'Orbitron',monospace; font-size:13px; color:#556070; letter-spacing:3px; margin-bottom:20px;">
    🛠️ COMMUNITY VAULT INTELLIGENCE TOOL
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="guide-card-neon">
        <div style="font-family:'Orbitron',monospace; font-size:14px; color:#00FFB2; margin-bottom:12px; letter-spacing:2px; font-weight:700;">
        🗿 CONCRETE VAULT INTELLIGENCE TERMINAL
        </div>
        <div style="font-size:13px; color:#E8F0F8; line-height:2.0; margin-bottom:16px;">
        Community-built tool hai jo real-time vault data, yield simulation, risk analysis aur portfolio rebalancing provide karta hai.
        </div>
        <a href="https://concrete-vault.streamlit.app" target="_blank" style="display:inline-block; background:#00FFB215; border:1px solid #00FFB2; color:#00FFB2; font-family:'Orbitron',monospace; font-size:11px; padding:10px 24px; border-radius:6px; text-decoration:none; letter-spacing:2px;">
        🚀 OPEN VAULT TOOL →
        </a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🔍 Tool Mein Kya Kya Hai?")

    features = [
        ("📊", "Vault Health Radar", "Real-time health factors, APY comparison, aur TVL across all Concrete vaults."),
        ("🧬", "Vault DNA Fingerprint", "6-dimensional radar chart — har vault ki unique 'personality' dekho. Yield Consistency, Liquidity, Strategy Diversity."),
        ("💰", "Yield Simulator", "Apna deposit amount daalo, select karo vault, aur dekho kitna yield milega — 1 month se 5 saal tak."),
        ("⚖️", "Portfolio Rebalancer", "Current holdings enter karo → optimal allocation suggest karta hai based on Max Efficiency, Min Risk, ya Max APY strategy."),
        ("📈", "Yield Calendar", "Day-by-day portfolio growth chart. Daily yield aur ct[Asset] token appreciation dekho."),
        ("🔴 vs 🟢", "DeFi vs Concrete Compare", "Standard DeFi yield vs Concrete protected yield ka comparison — risk-adjusted returns visualize karo."),
        ("❓", "Technical FAQ", "Protocol ke baare mein technical questions — smart contracts, data sources, methodology sab explain hai."),
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
    st.markdown("""
    <div class="guide-card-gold">
        <div style="font-family:'Orbitron',monospace; font-size:12px; color:#EDD97A; margin-bottom:10px; letter-spacing:2px;">⚡ TOOL KAISE USE KAREN?</div>
        <div style="font-size:13px; color:#E8F0F8; line-height:2.0;">
        1. <a href="https://concrete-vault.streamlit.app" target="_blank" style="color:#00FFB2;">concrete-vault.streamlit.app</a> open karo<br>
        2. Sidebar mein apna amount aur vault select karo<br>
        3. Tabs explore karo — Simulator, Rebalancer, Yield Calendar<br>
        4. Data dekho, compare karo, phir apna decision lo<br>
        <br>
        <b style="color:#EDD97A;">Made by community member mkashifalikcp. Not affiliated with Concrete Protocol officially.</b>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════
# TAB 8 — FAQ
# ════════════════════════════════════════════════════════════════
with tabs[7]:
    st.markdown("""
    <div style="font-family:'Orbitron',monospace; font-size:13px; color:#556070; letter-spacing:3px; margin-bottom:20px;">
    ❓ FREQUENTLY ASKED QUESTIONS
    </div>
    """, unsafe_allow_html=True)

    faqs = [
        ("🗿 Concrete Protocol safe hai?",
         "Concrete ke smart contracts audited hain. Lekin DeFi mein koi bhi protocol 100% risk-free nahi hota. Smart contract bugs, oracle failures, aur market crashes possible hain. Sirf woh amount invest karo jo lose afford kar sako."),

        ("💰 Minimum deposit kitna hai?",
         "Official minimum limit check karo concrete.xyz pe — yeh vault ke hisaab se different ho sakta hai. Generally chhota amount se shuru karna wise hai."),

        ("⏳ Yield kab milta hai?",
         "ct[Asset] tokens ki value continuously appreciate hoti hai — second-by-second! Koi manual claiming nahi. Jab bhi withdraw karo, accumulated yield automatically milti hai."),

        ("🔄 Kab bhi withdraw kar sakte hain?",
         "Generally haan — ERC-4626 vaults instant withdrawal support karte hain. Lekin high utilization periods mein liquidity limited ho sakti hai. Check karo withdrawal terms per vault."),

        ("📊 APY stable rehta hai?",
         "APY variable hota hai — underlying protocol conditions ke hisaab se change hota hai. Jo APY aaj dikha raha hai, kal different ho sakta hai. Always current rates check karo."),

        ("🔑 Wallet connect karna safe hai?",
         "Official website pe hamesha concrete.xyz use karo. Kisi bhi link pe click karne se pehle URL verify karo. Phishing sites bahut common hain DeFi mein."),

        ("🏆 XP kaise count hota hai?",
         "Concrete Discord pe activity se XP milta hai. Chat, engagement, articles — sab count hote hain. Exact formula public nahi hai, lekin active rehna best strategy hai."),

        ("💼 ct[Asset] tokens ko stake kar sakte hain?",
         "Yeh protocol ke updates pe depend karta hai. Latest info ke liye concrete.xyz/ecosystem ya Discord check karo."),

        ("📝 Koi article reject ho jaye to?",
         "Discouraged mat ho! Feedback lo mods se, improve karo, aur dobara submit karo. Quality content eventually accept hota hai."),

        ("🌐 Is guide ka matlab financial advice hai?",
         "Bilkul nahi! Yeh ek community-written educational guide hai. Koi bhi investment decision lene se pehle apna research karo (DYOR). Yeh tool aur guide sirf informational hai."),
    ]

    for q, a in faqs:
        with st.expander(q):
            st.markdown(f'<div style="font-size:13px; color:#E8F0F8; line-height:2.0; padding:8px 0;">{a}</div>', unsafe_allow_html=True)

    st.markdown("---")

    # Footer
    st.markdown("""
    <div style="background:#090D14; border:1px solid #131B25; border-radius:10px; padding:28px; text-align:center; margin-top:20px;">
        <div style="font-family:'Orbitron',monospace; font-size:22px; color:#00FFB2; font-weight:900; margin-bottom:8px; letter-spacing:4px;">
        🗿 CONCRETE 101
        </div>
        <div style="font-family:'Share Tech Mono',monospace; font-size:12px; color:#EDD97A; letter-spacing:3px; margin-bottom:16px;">
        ONE TEAM. ONE VISION. KEEP BUILDING TOGETHER.
        </div>
        <div style="display:flex; gap:16px; justify-content:center; flex-wrap:wrap; margin-bottom:16px;">
            <a href="https://concrete.xyz" target="_blank" style="color:#00FFB2; font-size:12px; text-decoration:none;">🏠 concrete.xyz</a>
            <a href="https://docs.concrete.xyz" target="_blank" style="color:#EDD97A; font-size:12px; text-decoration:none;">📘 Docs</a>
            <a href="https://points.concrete.xyz" target="_blank" style="color:#4DA6FF; font-size:12px; text-decoration:none;">⭐ Points</a>
            <a href="https://concrete-vault.streamlit.app" target="_blank" style="color:#9B59FF; font-size:12px; text-decoration:none;">🛠️ Vault Tool</a>
        </div>
        <div style="font-size:9px; color:#2A3540; letter-spacing:2px;">
        ⚠ COMMUNITY GUIDE · NOT FINANCIAL ADVICE · DYOR · NOT AFFILIATED WITH CONCRETE PROTOCOL OFFICIALLY
        </div>
    </div>
    """, unsafe_allow_html=True)
