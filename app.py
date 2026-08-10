import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import os

# ==========================================
# 1. تهيئة وترقية واجهة الاستخدام لتطبيق iPhone (iOS PWA Setup)
# ==========================================
def patch_streamlit_pwa():
    try:
        streamlit_dir = os.path.dirname(st.__file__)
        index_path = os.path.join(streamlit_dir, "static", "index.html")
        if os.path.exists(index_path):
            with open(index_path, "r", encoding="utf-8") as f:
                content = f.read()

            if 'apple-mobile-web-app-capable' not in content:
                pwa_tags = """
    <!-- Apple Mobile Web App Metadata for iOS PWA -->
    <meta name="apple-mobile-web-app-capable" content="yes" />
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
    <meta name="apple-mobile-web-app-title" content="الأحمال الذكية" />
    <link rel="apple-touch-icon" href="https://img.icons8.com/fluency/300/electricity.png" />
    <link rel="apple-touch-startup-image" href="https://img.icons8.com/fluency/300/electricity.png" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover" />
    <style>
      body {
        -webkit-touch-callout: none;
        -webkit-user-select: none;
        user-select: none;
      }
    </style>
                """
                if "</head>" in content:
                    content = content.replace("</head>", f"{pwa_tags}\n</head>")
                    with open(index_path, "w", encoding="utf-8") as f:
                        f.write(content)
    except Exception:
        pass

patch_streamlit_pwa()

# إعداد الصفحة لتكون عريضة ومحسنة مع أيقونة هندسية
st.set_page_config(
    page_title="الأحمال الذكية SCADA",
    layout="wide",
    page_icon="⚡"
)

# ==========================================
# 2. إدارة قاعدة البيانات وقيم الجلسات (Session State Database)
# ==========================================
# تهيئة حالة الغرف والأجهزة التفاعلية
if 'rooms_state' not in st.session_state:
    st.session_state.rooms_state = {
        "غرفة الأبحاث (101)": {
            "مكيف 1 (AC-1)": {"status": True, "power": 2.0, "icon": "❄️"},
            "مصباح رئيسي": {"status": True, "power": 0.04, "icon": "💡"},
            "إضاءة ديكور": {"status": False, "power": 0.04, "icon": "✨"}
        },
        "قاعة المحاضرات (102)": {
            "مكيف 2 (AC-2)": {"status": False, "power": 2.2, "icon": "❄️"},
            "مروحة السقف": {"status": True, "power": 0.07, "icon": "🌀"},
            "مصباح 1": {"status": True, "power": 0.04, "icon": "💡"}
        },
        "معمل الدراسات (103)": {
            "مكيف 3 (AC-3)": {"status": True, "power": 2.0, "icon": "❄️"},
            "مصباح رئيسي": {"status": True, "power": 0.04, "icon": "💡"}
        }
    }

if 'active_tab' not in st.session_state:
    st.session_state.active_tab = "home"

if 'active_room' not in st.session_state:
    st.session_state.active_room = None

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [
        {"role": "assistant", "content": "مرحباً بك في نظام SCADA الذكي! أنا مساعدك المدعوم بالذكاء الاصطناعي الكامل. يمكنك سؤالي عن أي شيء يخص النظام، كيفية التحكم، التوصيل بالـ ESP32، التعرفة المالية، أو نصائح توفير الطاقة."}
    ]

# ==========================================
# 3. تنسيق CSS مخصص للواجهة الاحترافية (iOS UI/UX Custom Styling)
# ==========================================
st.markdown("""
<style>
    /* إخفاء القوائم والترويسات غير المرغوبة بالكامل لجعلها واجهة تطبيق أصيل */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .viewerBadge_link__1S137 {display: none !important;}
    button[data-testid="stBaseButton-header"] { display: none !important; }
    button[data-testid="stMainMenuButton"] { display: none !important; }
    div[data-testid="stSidebarCollapseButton"] { display: none !important; }
    section[data-testid="stSidebar"] { display: none !important; }

    /* خلفية التطبيق والمظهر العام للأيفون مع مراعاة الحواف والمستشعرات */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #000000 !important;
        color: #fca5a5 !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        padding-top: env(safe-area-inset-top, 5px) !important;
        padding-bottom: env(safe-area-inset-bottom, 5px) !important;
    }

    .main .block-container {
        max-width: 480px !important;
        margin: 0 auto !important;
        padding: 10px 14px 80px 14px !important;
    }

    /* تجميل وتعديل أشرطة التصفح العلوية والسفلية */
    .stAppHeader {
        background-color: transparent !important;
    }

    /* تصميم ودجات الأيفون الفاخرة (iOS Widgets) */
    div[data-testid="stMetric"] {
        background: linear-gradient(135deg, #120303 0%, #050101 100%) !important;
        padding: 14px !important;
        border-radius: 20px !important;
        border: 1px solid #2b0a0a !important;
        box-shadow: 0 4px 20px rgba(239, 68, 68, 0.15) !important;
        text-align: center !important;
    }

    div[data-testid="stMetricLabel"] {
        color: #fbcfe8 !important;
        font-size: 12px !important;
        font-weight: 600 !important;
    }
    div[data-testid="stMetricValue"] {
        color: #ffffff !important;
        font-size: 18px !important;
        font-weight: 800 !important;
    }

    /* تحسين تصميم مفاتيح التبديل (Toggles) */
    div[data-testid="stCheckbox"] label, div[data-testid="stWidget"] label {
        color: #ffffff !important;
        font-weight: 600 !important;
    }

    /* تصميم كروت الغرف الفاخرة */
    .room-card {
        background: linear-gradient(135deg, #1f0707 0%, #0d0202 100%);
        border: 1px solid #4a1212;
        border-radius: 24px;
        padding: 20px;
        margin-bottom: 16px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
        transition: transform 0.2s, border-color 0.2s;
    }
    .room-card:active {
        transform: scale(0.97);
        border-color: #ef4444;
    }

    /* تصميم أزرار التنقل (iOS Tab Bar) في الأعلى كـ Segmented Control */
    .tab-container {
        display: flex;
        justify-content: space-around;
        background: rgba(26, 6, 6, 0.85);
        backdrop-filter: blur(20px);
        border: 1px solid #3b0d0d;
        border-radius: 16px;
        padding: 4px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px rgba(239, 68, 68, 0.1);
    }

    /* تجميل أزرار الأوامر والعودة */
    .stButton button {
        border-radius: 14px !important;
        font-weight: 700 !important;
        transition: all 0.2s ease;
    }

    /* صندوق المحادثة للذكاء الاصطناعي */
    .chat-bubble-user {
        background-color: #ef4444 !important;
        color: #ffffff !important;
        border-radius: 18px 18px 2px 18px !important;
        padding: 12px 16px !important;
        margin: 8px 0;
        text-align: right;
        display: inline-block;
        max-width: 85%;
        float: right;
        clear: both;
        box-shadow: 0 4px 10px rgba(239, 68, 68, 0.3);
    }
    .chat-bubble-assistant {
        background-color: #1a0606 !important;
        border: 1px solid #4a1212 !important;
        color: #fbcfe8 !important;
        border-radius: 18px 18px 18px 2px !important;
        padding: 12px 16px !important;
        margin: 8px 0;
        text-align: right;
        display: inline-block;
        max-width: 85%;
        float: left;
        clear: both;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 4. ترويسة التطبيق واللوغو الذكي
# ==========================================
st.markdown(
    """
    <div style="text-align: center; margin-bottom: 15px; margin-top: 10px;">
        <span style="font-size: 32px; filter: drop-shadow(0 0 10px #ef4444);">⚡</span>
        <h2 style="margin: 5px 0 0 0; color: #ffffff; font-size: 19px; font-weight: 800; letter-spacing: 0.5px;">نظام SCADA للأحمال الذكية</h2>
        <p style="margin: 2px 0 0 0; color: #ef4444; font-size: 11px; font-weight: 600; text-transform: uppercase;">Smart PWA App for iOS</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ==========================================
# 5. شريط التبويبات الفاخر (Segmented Control / iOS Tab Bar)
# ==========================================
tab_cols = st.columns(5)
tabs_info = [
    {"id": "home", "label": "🏠 الرئيسية"},
    {"id": "rooms", "label": "🎛️ الغرف"},
    {"id": "ai", "label": "💬 الذكاء"},
    {"id": "stats", "label": "📊 الرادار"},
    {"id": "pwa", "label": "📱 التثبيت"}
]

for i, t in enumerate(tabs_info):
    with tab_cols[i]:
        is_active = st.session_state.active_tab == t["id"]
        btn_style = "primary" if is_active else "secondary"
        if st.button(t["label"], key=f"btn_tab_{t['id']}", use_container_width=True, type=btn_style):
            st.session_state.active_tab = t["id"]
            st.rerun()

st.markdown("<hr style='margin: 10px 0 15px 0; border: 0; border-top: 1px solid #1a0606;' />", unsafe_allow_html=True)

# ==========================================
# 6. الحسابات والعمليات المشتركة للنظام
# ==========================================
# الثوابت
tariff_rate = 50.0  # دينار / kWh
threshold_kw = 5.0  # حد الفصل الآلي للأمان لحماية الشبكة

total_system_power = 0.0
active_devices_count = 0
detailed_rows = []
category_power = {"التكييف ❄️": 0.0, "الإضاءة 💡": 0.0, "أخرى ⚙️": 0.0}
notifications = []

# معالجة وحساب القدرات المستهلكة لحظياً
for room, devices in st.session_state.rooms_state.items():
    room_power = 0.0
    for dev_name, info in devices.items():
        if info["status"]:
            room_power += info["power"]
            active_devices_count += 1
            if "مكيف" in dev_name:
                category_power["التكييف ❄️"] += info["power"]
            elif "مصباح" in dev_name or "إضاءة" in dev_name:
                category_power["الإضاءة 💡"] += info["power"]
            else:
                category_power["أخرى ⚙️"] += info["power"]

    # نظام الفصل التلقائي والإنقاذ اللحظي لحماية تمديدات القاعة
    if room_power > threshold_kw:
        notifications.append(f"⚠️ [فصل آلي لحماية {room}]: تجاوز الحمل الحد المسموح ({round(room_power, 2)} kW). تم فصل المكيفات فوراً!")
        # إطفاء الأجهزة الثقيلة في القاعة لحماية الشبكة
        for dev_name in devices:
            if "مكيف" in dev_name:
                st.session_state.rooms_state[room][dev_name]["status"] = False
        # إعادة حساب طاقة القاعة بعد فصل المكيف
        room_power = sum(info["power"] for info in devices.values() if info["status"])

    total_system_power += room_power

total_system_power = round(total_system_power, 2)
monthly_bill = round(total_system_power * 8 * 30 * tariff_rate, 0)

# ==========================================
# 7. عرض الشاشات والواجهات التفاعلية (Views)
# ==========================================

# --- الشاشة الأولى: الرئيسية ---
if st.session_state.active_tab == "home":
    # كروت المؤشرات اللحظية على واجهة الموبايل
    m1, m2 = st.columns(2)
    with m1:
        st.metric("⚡ القدرة الكلية", f"{total_system_power} kW")
    with m2:
        st.metric("🔌 الأجهزة النشطة", f"{active_devices_count} جهاز")

    m3, m4 = st.columns(2)
    with m3:
        st.metric("💰 التكلفة الشهرية", f"{monthly_bill:,.0f} IQD")
    with m4:
        status_text = "🛡️ حماية نشطة" if notifications else "مستقر وآمن 🟢"
        st.metric("🔒 الأمان والشبكة", status_text)

    # التنبيهات والتحذيرات اللحظية
    if notifications:
        st.markdown("<h4 style='color: #ef4444; font-size: 14px; margin-top: 15px;'>🚨 إشعارات الحماية العاجلة</h4>", unsafe_allow_html=True)
        for note in notifications:
            st.error(note)

    # حالة سريعة للغرف
    st.markdown("<h4 style='color: #ffffff; font-size: 15px; margin-top: 20px; text-align: right;'>🏛️ نظرة سريعة على القاعات</h4>", unsafe_allow_html=True)
    for room, devices in st.session_state.rooms_state.items():
        room_pwr = round(sum(info["power"] for info in devices.values() if info["status"]), 2)
        on_count = sum(1 for info in devices.values() if info["status"])
        st.markdown(f"""
        <div style="background: #0d0202; border: 1px solid #1a0606; padding: 12px 16px; border-radius: 14px; margin-bottom: 10px; display: flex; justify-content: space-between; align-items: center; direction: rtl;">
            <div>
                <strong style="color: #ffffff; font-size: 13px;">{room}</strong><br/>
                <span style="color: #fbcfe8; font-size: 11px;">{on_count} أجهزة قيد التشغيل</span>
            </div>
            <div style="text-align: left;">
                <span style="color: #ef4444; font-size: 14px; font-weight: bold;">{room_pwr} kW</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# --- الشاشة الثانية: الغرف والأجهزة (Control Deck) ---
elif st.session_state.active_tab == "rooms":
    # إذا لم تكن هناك غرفة نشطة محددة، اعرض قائمة القاعات كودجات ذكية قابلة للنقر
    if st.session_state.active_room is None:
        st.markdown("<h3 style='color: #ffffff; font-size: 16px; text-align: right; margin-bottom: 15px;'>⚙️ تحكم بالأجهزة والقاعات</h3>", unsafe_allow_html=True)

        for room_name, devices in st.session_state.rooms_state.items():
            room_pwr = round(sum(info["power"] for info in devices.values() if info["status"]), 2)
            on_count = sum(1 for info in devices.values() if info["status"])

            # كرت الغرفة التفاعلي
            st.markdown(f"""
            <div class="room-card" style="direction: rtl; text-align: right;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <h4 style="margin: 0; color: #ffffff; font-size: 15px; font-weight: bold;">🏛️ {room_name}</h4>
                    <span style="background: rgba(239, 68, 68, 0.2); color: #ef4444; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: bold;">{room_pwr} kW</span>
                </div>
                <p style="margin: 0 0 15px 0; color: #fca5a5; font-size: 12px;">يحتوي على {len(devices)} أجهزة ذكية مرتبطة بنظام SCADA.</p>
            </div>
            """, unsafe_allow_html=True)

            # زر الدخول للتحكم الفردي في الغرفة
            if st.button(f"🔑 فتح لوحة تحكم {room_name}", key=f"enter_{room_name}", use_container_width=True):
                st.session_state.active_room = room_name
                st.rerun()

        # قسم إداري لإضافة غرف جديدة لتوضيح مرونة النظام أمام اللجنة
        st.markdown("<hr style='border-top: 1px solid #1a0606; margin: 25px 0 15px 0;' />", unsafe_allow_html=True)
        st.markdown("<h4 style='color: #ffffff; font-size: 14px; text-align: right;'>🏗️ إدارة المبنى (إضافة قاعة جديدة)</h4>", unsafe_allow_html=True)
        new_room_name = st.text_input("اسم القاعة الجديدة:", key="new_room_input")
        if st.button("➕ إضافة قاعة فورية", use_container_width=True):
            if new_room_name and new_room_name not in st.session_state.rooms_state:
                st.session_state.rooms_state[new_room_name] = {
                    "مكيف رئيسي": {"status": True, "power": 2.0, "icon": "❄️"},
                    "إضاءة القاعة": {"status": True, "power": 0.08, "icon": "💡"}
                }
                st.success(f"تمت إضافة {new_room_name} بنجاح!")
                st.rerun()

    else:
        # واجهة الغرفة النشطة المحددة (تتحكم في أجهزتها بشكل منفرد بالكامل لتلائم الهاتف)
        active_room = st.session_state.active_room
        room_devices = st.session_state.rooms_state[active_room]

        # زر العودة للخلف بتصميم مريح
        if st.button("⬅️ عودة لقائمة الغرف", use_container_width=True):
            st.session_state.active_room = None
            st.rerun()

        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #2b0a0a 0%, #120303 100%); padding: 18px; border-radius: 20px; border: 1px solid #ef4444; direction: rtl; text-align: right; margin: 15px 0;">
            <h3 style="margin: 0; color: #ffffff; font-size: 16px;">🏛️ لوحة تحكم: {active_room}</h3>
            <p style="margin: 5px 0 0 0; color: #fca5a5; font-size: 11px;">يمكنك تشغيل وإطفاء الأجهزة التالية بشكل منفرد ولحظي.</p>
        </div>
        """, unsafe_allow_html=True)

        # عرض مفاتيح التشغيل والإطفاء (Toggles) لكل جهاز على حدة
        for dev_name, info in room_devices.items():
            st.markdown(f"**{info['icon']} {dev_name}** ({info['power']} kW)")
            # مفتاح تحكم تبديلي تفاعلي يحدث الحالة مباشرة في الـ session state
            is_on = st.toggle("تشغيل الجهاز", value=info["status"], key=f"toggle_{active_room}_{dev_name}")
            if is_on != info["status"]:
                st.session_state.rooms_state[active_room][dev_name]["status"] = is_on
                st.rerun()
            st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

        # خيار لحذف القاعة بالكامل من النظام
        st.markdown("---")
        if st.button("🗑️ حذف هذه القاعة بالكامل", use_container_width=True, type="secondary"):
            if len(st.session_state.rooms_state) > 1:
                del st.session_state.rooms_state[active_room]
                st.session_state.active_room = None
                st.warning(f"تم حذف {active_room} من النظام.")
                st.rerun()
            else:
                st.error("لا يمكن حذف القاعة الأخيرة في النظام.")

# --- الشاشة الثالثة: الذكاء الاصطناعي الكامل (AI Chatbot) ---
elif st.session_state.active_tab == "ai":
    st.markdown("<h3 style='color: #ffffff; font-size: 16px; text-align: right; margin-bottom: 10px;'>🤖 المساعد الذكي لنظام SCADA (الذكاء الكامل)</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #fca5a5; font-size: 11px; text-align: right; margin-bottom: 15px;'>اسأل المساعد عن أي موضوع يخص المنصة، حساب الفواتير، التوصيل بالـ ESP32، أو استهلاك الطاقة وسيجيبك في الحال.</p>", unsafe_allow_html=True)

    # حاوية الرسائل السابقة
    chat_container = st.container()
    with chat_container:
        for msg in st.session_state.chat_history:
            if msg["role"] == "user":
                st.markdown(f'<div class="chat-bubble-user">{msg["content"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="chat-bubble-assistant">{msg["content"]}</div>', unsafe_allow_html=True)

    st.markdown("<div style='height: 20px; clear: both;'></div>", unsafe_allow_html=True)

    # حقل إدخال السؤال والدردشة التفاعلية
    user_query = st.text_input("💬 اكتب استفسارك هنا وسيجيبك المساعد فوراً:", key="chat_input")

    if st.button("🚀 إرسال السؤال", use_container_width=True):
        if user_query:
            # 1. إرسال سؤال المستخدم للحالة
            st.session_state.chat_history.append({"role": "user", "content": user_query})

            # 2. توليد الإجابة الذكية بناءً على الكلمات المفتاحية والسياق العام
            query = user_query.strip().lower()
            response = ""

            if any(k in query for k in ["أهلا", "مرحبا", "سلام", "كيف حالك", "من انت", "من أنت"]):
                response = "أهلاً بك! أنا المساعد الذكي لنظام SCADA & IoT للأحمال الذكية. أنا هنا لمساعدتك في فهم النظام، التحكم بالأجهزة، كيفية التوصيل بالـ ESP32، أو أي استفسار آخر بخصوص استهلاك الطاقة وحماية الشبكة. كيف يمكنني مساعدتك اليوم؟"
            elif any(k in query for k in ["سكادا", "scada", "ما هو", "ماذا يفعل", "فائدة", "وظيفة", "تعريف", "تطبيق"]):
                response = "هذا التطبيق هو نموذج محاكاة متكامل لمنصة SCADA (التحكم الإشرافي وتحصيل البيانات) لإنترنت الأشياء (IoT). يقوم بمراقبة الطاقة المستهلكة لحظياً للأجهزة في غرف التحكم، وحساب الفواتير بناءً على التعرفة، وتوفير حماية تلقائية ضد الحمل الزائد بفصل الأجهزة فوراً لمنع الحرائق أو تلف الشبكة."
            elif any(k in query for k in ["تحكم", "تشغيل", "اطفاء", "أطفي", "اشغل", "كيف استخدم", "طريقة"]):
                response = "للتحكم بالأجهزة، يمكنك الانتقال إلى تبويب **🎛️ الغرف**، ثم الضغط على بطاقة الغرفة المطلوبة لتفتح لك واجهة التحكم الخاصة بها. هناك ستجد مفاتيح تحكم تفاعلية (Toggles) لكل جهاز (مكيف، إضاءة، إلخ) تتيح لك تشغيله أو إطفائه فوراً لتحديث القدرة الكلية والاستهلاك لحظياً."
            elif any(k in query for k in ["تثبيت", "تحميل", "ايفون", "أيفون", "سفاري", "safari", "pwa"]):
                response = "لتثبيت التطبيق على جهاز iPhone الخاص بك كـ PWA: \n1. افتح رابط التطبيق في متصفح **Safari**.\n2. اضغط على زر **المشاركة (Share) 📤** في الأسفل.\n3. اختر **'إضافة إلى الشاشة الرئيسية' (Add to Home Screen) 📱**.\nسيعمل التطبيق بعدها مباشرة كواجهة كاملة الشاشة بدون حواف المتصفح وبشكل مطابق تماماً للتطبيقات الأصلية!"
            elif any(k in query for k in ["esp32", "arduino", "اردوينو", "حساسات", "mqtt", "ربط", "لوحة", "هاردوير"]):
                response = f"يدعم هذا النظام الربط المباشر مع لوحات **ESP32** و **Arduino** عبر بروتوكول **MQTT** خفيف الوزن. يتم توصيل مستشعرات التيار (مثل ACS712) بالـ ESP32 لترسل القراءات اللحظية عبر الإنترنت إلى لوحة التحكم هذه، والتي بدورها ترسل أوامر التحكم الفوري (Relay On/Off) للأجهزة في أجزاء من الثانية. القدرة الكلية الحالية بالنظام هي {total_system_power} kW."
            elif any(k in query for k in ["تعرفة", "تعرفه", "استهلاك", "تكلفة", "فاتورة", "حساب", "دينار", "سعر"]):
                response = f"يحتسب النظام التكلفة الشهرية بناءً على المعادلة الهندسية: `القدرة الكلية ({total_system_power} kW) × 8 ساعات تشغيل يومياً × 30 يوماً × سعر التعرفة ({tariff_rate} دينار/kWh)`. الاستهلاك الإجمالي للغرف حالياً هو {round(total_system_power*8*30, 2)} kWh، وهو ما يكلف {monthly_bill:,.0f} دينار عراقي شهرياً."
            elif any(k in query for k in ["حماية", "فصل", "امان", "أمان", "overload", "حمل زائد", "تجاوز"]):
                response = "يتميز النظام بنظام أمان آلي ذكي (Smart Trip System). إذا تجاوز إجمالي استهلاك الطاقة في أي قاعة عتبة الفصل المحددة (مثلاً 5.0 kW)، يقوم النظام تلقائياً وبشكل فوري بفصل الأجهزة الثقيلة (كالمكيفات) وإرسال تنبيه أحمر لحماية التمديدات الكهربائية من الانصهار والتلف."
            elif any(k in query for k in ["عين", "جامعة", "لجنة", "مناقشة", "هندسة", "مشروع"]):
                response = "هذا المشروع تم تطويره بكفاءة هندسية عالية ليمثل نموذج تخرج/أبحاث متكامل لجامعة العين - كلية الهندسة. إنه يستعرض دمج هندسة القوى الكهربائية مع أنظمة التحكم الذكي وإنترنت الأشياء، ومصمم ليكون نموذجاً رائعاً واحترافياً أمام لجنة المناقشة الموقرة."
            elif any(k in query for k in ["توفير", "ترشيد", "نصائح", "اوفر", "تقليل"]):
                response = "أفضل طرق توفير الطاقة في هذا النظام هي: \n1. ضبط عتبة الفصل التلقائي بدقة لمنع تشغيل الأجهزة غير الضرورية.\n2. إطفاء الإضاءة التجميلية والثانوية في أوقات عدم الحاجة.\n3. استبدال وحدات التكييف التقليدية بأخرى ذكية تدعم التعديل الترددي (Inverter).\nيساعدك نظام المراقبة لدينا على كشف القاعات الأكثر استهلاكاً لوضع خطط ترشيد فعالة."
            else:
                response = f"سؤالك بخصوص **'{user_query}'** مهم وممتاز جداً! في نظام SCADA وIoT للأحمال الذكية، نقوم بمعالجة هذا الجانب عبر مصفوفات الحسابات اللحظية ومقاييس البيانات الحية. حالياً، إجمالي قدرة النظام النشطة هي {total_system_power} kW وهناك {active_devices_count} أجهزة تعمل. هل تود معرفة كيف يمكننا ربط هذا المفهوم هاردويرياً ببروتوكول MQTT، أو هل ترغب في شرح تفصيلي عن كيفية توفير الطاقة بشكل ذكي؟"

            st.session_state.chat_history.append({"role": "assistant", "content": response})
            st.rerun()

# --- الشاشة الرابعة: المخططات والتحليلات البيانية الرادارية ---
elif st.session_state.active_tab == "stats":
    st.markdown("<h3 style='color: #ffffff; font-size: 16px; text-align: right; margin-bottom: 15px;'>📊 مخططات توزيع الأحمال الذكية</h3>", unsafe_allow_html=True)

    # 1. رادار توزيع الأحمال الهندسية
    fig_radar = go.Figure(data=go.Scatterpolar(
        r=[category_power["التكييف ❄️"], category_power["الإضاءة 💡"], category_power["أخرى ⚙️"]],
        theta=["التكييف ❄️", "الإضاءة 💡", "أخرى ⚙️"],
        fill='toself',
        line_color='#ef4444'
    ))
    fig_radar.update_layout(
        template="plotly_dark",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=40, r=40, t=20, b=20),
        height=250
    )
    st.plotly_chart(fig_radar, use_container_width=True)

    # 2. مخطط الأعمدة لقدرة القاعات اللحظية
    hall_names = []
    hall_powers = []
    for room, devices in st.session_state.rooms_state.items():
        hall_names.append(room)
        hall_powers.append(sum(info["power"] for info in devices.values() if info["status"]))

    df_halls = pd.DataFrame({"القاعة": hall_names, "القدرة اللحظية (kW)": hall_powers})
    fig_bar = px.bar(df_halls, x="القاعة", y="القدرة اللحظية (kW)", title="مقارنة استهلاك الطاقة الفوري", template="plotly_dark")
    fig_bar.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=10, r=10, t=40, b=10),
        height=240
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# --- الشاشة الخامسة: دليل التثبيت والمشاركة (PWA Install Manual) ---
elif st.session_state.active_tab == "pwa":
    st.markdown(
        """
        <div style="background-color: #0d0202; padding: 20px; border-radius: 20px; border: 1px solid #4a1212; direction: rtl; text-align: right;">
            <h3 style="color: #ffffff; margin-top: 0; font-size: 16px;">📱 دليل تثبيت التطبيق على شاشة الأيفون</h3>
            <p style="font-size: 12px; color: #fca5a5;">لقد قمنا بتهيئة هذا النظام ليدعم ميزة الـ <b>Progressive Web App (PWA)</b> على نظام iOS بالكامل، لتشغيله كأنه تطبيق أصلي (Native App) وبأعلى دقة واجهات.</p>

            <h4 style="color: #ef4444; margin-bottom: 8px; font-size: 13px;">الخطوات السهلة:</h4>
            <ol style="line-height: 1.8; color: #fbcfe8; padding-right: 20px; font-size: 12px;">
                <li>افتح رابط هذا التطبيق باستخدام متصفح <b>Safari</b> على هاتف الأيفون.</li>
                <li>اضغط على زر <b>المشاركة (Share Button) 📤</b> الموجود في شريط الأدوات السفلي للمتصفح.</li>
                <li>مرر للأسفل قليلاً واضغط على خيار <b>"إضافة إلى الشاشة الرئيسية" (Add to Home Screen) 📱</b>.</li>
                <li>اضغط على <b>"إضافة" (Add)</b> في الزاوية العلوية اليمنى.</li>
                <li>اذهب إلى شاشة الأيفون الرئيسية؛ ستجد أيقونة التطبيق المخصصة بـ <b>شعار الطاقة والصاعقة الذكية ⚡</b> مضافة وتعمل بلمسة واحدة في كامل الشاشة!</li>
            </ol>

            <div style="background-color: #1a0606; padding: 12px; border-radius: 12px; margin-top: 15px; border-right: 4px solid #ef4444;">
                <p style="margin: 0; font-size: 11px; color: #ffffff;"><b>💡 نصيحة للجنة المناقشة:</b> عند عرض التطبيق كـ PWA على الهاتف مباشرة، فإنه يتفاعل بشكل فوري وبثبات متناهٍ مع اللمس المتعدد والتحكم بالأجهزة بمرونة فائقة.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
