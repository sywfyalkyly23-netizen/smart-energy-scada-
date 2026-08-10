import os
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import streamlit as st
import streamlit.components.v1 as components
import json
import os


st.set_page_config(
    page_title="SCADA Matrix | نظام إدارة الأحمال الذكية",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

دالة لقراءة ملف الـ HTML (index.html)

def load_html_template(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        return """
        

⚠️ ملف index.html غير موجود

يرجى التأكد من وضع ملف index.html في نفس مجلد ملف البايثون.
        """

محاكاة لبيانات النظام (هنا يمكنك ربط قاعدة بياناتك أو مستشعراتك)

system_data = {
    "current_load": "45.8 kW",
    "daily_cost": "124.50 SAR",
    "active_devices": 12,
    "alerts_count": 3
}

def main():
    # عنوان التطبيق في Streamlit (مخفي لأننا نستخدم واجهة HTML مخصصة)
    st.markdown("""
        


    """, unsafe_allow_html=True)

# تحميل الكود من ملف index.html
# ملاحظة: تأكد أن ملف index.html موجود في نفس المسار
html_content = load_html_template("index.html")

# (اختياري) يمكنك استبدال متغيرات داخل الـ HTML ببيانات من بايثون
# مثال: html_content = html_content.replace("{{LOAD}}", system_data["current_load"])

# عرض الواجهة داخل Streamlit
# نستخدم height=900 ليتناسب مع أبعاد شاشات الموبايل أو العرض الكامل
components.html(html_content, height=850, scrolling=True)

# عرض بيانات إضافية في Sidebar (اختياري)
with st.sidebar:
    st.header("⚙️ إعدادات النظام")
    st.write(f"الحمل الحالي: {system_data['current_load']}")
    st.write(f"التكلفة اليومية: {system_data['daily_cost']}")
    
    if st.button("تحديث البيانات"):
        st.rerun()

if name == "main":
    main()
# ==========================================
# 1. إعدادات الصفحة ودمج ملف الـ HTML الخارجي لـ iPhone (PWA Setup)
# ==========================================
st.set_page_config(
    page_title="نظام محاكاة وإدارة الأحمال الذكية",
    layout="wide",
    page_icon="⚡"
)

def load_external_pwa_index():
    try:
        streamlit_dir = os.path.dirname(st.__file__)
        index_path = os.path.join(streamlit_dir, "static", "index.html")
        if os.path.exists("index.html"):
            with open("index.html", "r", encoding="utf-8") as f:
                custom_content = f.read()
            with open(index_path, "w", encoding="utf-8") as f:
                f.write(custom_content)
    except Exception:
        pass

load_external_pwa_index()

# ==========================================
# 2. تنسيق CSS مخصص للواجهة الصناعية المحسنة (Responsive iOS Design)
# ==========================================
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .viewerBadge_link__1S137 {display: none !important;}

    button[data-testid="stBaseButton-header"] { display: none !important; }
    button[data-testid="stMainMenuButton"] { display: none !important; }

    .stAppHeader {
        background-color: transparent !important;
        background: transparent !important;
    }
    header {
        background-color: transparent !important;
        background: transparent !important;
    }

    button[data-testid="stExpandSidebarButton"],
    button[data-testid="stBaseButton-headerNoPadding"] {
        background-color: rgba(31, 7, 7, 0.8) !important;
        border: 1px solid #ef4444 !important;
        border-radius: 50% !important;
        color: #ffffff !important;
        width: 44px !important;
        height: 44px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        box-shadow: 0 4px 10px rgba(239, 68, 68, 0.4) !important;
        z-index: 999999 !important;
        margin: 8px !important;
    }

    html, body, [data-testid="stAppViewContainer"] {
        background-color: #0c0202 !important;
        color: #fca5a5 !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        padding-top: env(safe-area-inset-top, 12px) !important;
        padding-bottom: env(safe-area-inset-bottom, 12px) !important;
        padding-left: env(safe-area-inset-left, 8px) !important;
        padding-right: env(safe-area-inset-right, 8px) !important;
    }

    .main {
        background-color: #0c0202 !important;
    }

    div[data-testid="stMetric"] {
        background: linear-gradient(135deg, #1f0707 0%, #120303 100%) !important;
        padding: 16px !important;
        border-radius: 18px !important;
        border: 1px solid #4a1212 !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5) !important;
        text-align: center !important;
        transition: transform 0.2s, border-color 0.2s;
    }
    div[data-testid="stMetric"]:hover {
        transform: scale(1.02);
        border-color: #ef4444 !important;
    }

    div[data-testid="stMetricLabel"] {
        color: #fbcfe8 !important;
        font-size: 13px !important;
        font-weight: 600 !important;
        letter-spacing: 0.5px;
    }
    div[data-testid="stMetricValue"] {
        color: #ffffff !important;
        font-size: 20px !important;
        font-weight: 800 !important;
    }

    section[data-testid="stSidebar"] {
        background-color: #120303 !important;
        border-right: 1px solid #2b0a0a !important;
    }

    .stButton button {
        background: linear-gradient(90deg, #b91c1c 0%, #ef4444 100%) !important;
        color: #ffffff !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 12px 24px !important;
        font-weight: bold !important;
        width: 100% !important;
        box-shadow: 0 4px 10px rgba(239, 68, 68, 0.3) !important;
        transition: transform 0.1s;
    }
    .stButton button:active {
        transform: scale(0.98);
        background: #991b1b !important;
    }

    .stDataFrame {
        border-radius: 14px !important;
        overflow: hidden !important;
        border: 1px solid #3b0d0d !important;
    }

    @media (max-width: 768px) {
        .block-container {
            padding-top: 10px !important;
            padding-bottom: 10px !important;
        }
        h1 { font-size: 1.6rem !important; }
        h2 { font-size: 1.2rem !important; }
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. إدارة قاعدة البيانات وقيم الجلسات (Session State Database)
# ==========================================
if 'initial_halls' not in st.session_state:
    st.session_state.initial_halls = {
        "جامعة العين - قاعة الأبحاث (101)": {"مكيف 1 (AC-1)": 2.0, "مصباح 1": 0.04, "مصباح 2": 0.04},
        "جامعة العين - قاعة المحاضرات (102)": {"مكيف 1 (AC-1)": 2.0, "مروحة السقف": 0.07, "مصباح 1": 0.04},
        "جامعة العين - معمل الدراسات (103)": {"مكيف 1 (AC-1)": 2.0, "مصباح 1": 0.04}
    }

st.markdown(
    """
    <div style="background: linear-gradient(95deg, #4a0e0e 0%, #170404 100%); padding: 18px; border-radius: 14px; border-right: 6px solid #ef4444; text-align: right; margin-bottom: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.4);">
        <h1 style="margin: 0; color: #ffffff; font-size: 22px; font-weight: 800;">🔴 نظام محاكاة وإدارة الأحمال الذكية (SCADA & IoT)</h1>
        <p style="margin: 5px 0 0 0; color: #fca5a5; font-size: 12px; font-weight: 500;">بوابة المراقبة والتحكم الذكي وحماية الأحمال المصممة للأجهزة الذكية.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ==========================================
# 4. شريط التحكم والمدخلات الجانبي (Sidebar Interface)
# ==========================================
st.sidebar.markdown("<div style='text-align: right;'><h3>📂 لوحة التحكم الرئيسية</h3></div>", unsafe_allow_html=True)
navigation_page = st.sidebar.selectbox(
    "اختر قسم المعرض:",
    [
        "1️⃣ لوحة التشغيل والتحكم الافتراضي",
        "2️⃣ هندسة وتعديل المباني والقاعات",
        "3️⃣ شاشة الحساسات الحية ومؤشرات SCADA",
        "4️⃣ المخططات والتحليلات البيانية",
        "5️⃣ التقارير المالية وجداول الاستهلاك",
        "6️⃣ مركز التنبيهات وحماية الشبكة",
        "7️⃣ التنبؤ الذكي بالذكاء الاصطناعي",
        "8️⃣ مقارنة استهلاك القاعات",
        "9️⃣ الدعم الفني وربط اللوحات المصغرة",
        "📱 دليل التثبيت على الأيفون (PWA)"
    ]
)

st.sidebar.markdown("---")
tariff_rate = st.sidebar.number_input("التعرفة (دينار / kWh)", value=50, step=1)
threshold_kw = st.sidebar.number_input("عتبة الفصل الآلي (kW)", value=5.0, step=0.5)

st.sidebar.markdown("---")
st.sidebar.markdown("<div style='text-align: right;'><h4>🎛️ أدوات التشغيل الفوري</h4></div>", unsafe_allow_html=True)
hall_names = list(st.session_state.initial_halls.keys())
selected_hall = st.sidebar.selectbox("المبنى أو القاعة المستهدفة", hall_names)

available_devices = list(st.session_state.initial_halls[selected_hall].keys()) if selected_hall in st.session_state.initial_halls else []
target_appliance = st.sidebar.selectbox("الجهاز المستهدف بالتحكم", available_devices if available_devices else ["لا توجد أجهزة"])
user_action = st.sidebar.radio("حالة الأمر", ["تشغيل 🟢", "إطفاء 🔴"])

# ==========================================
# 5. معالجة بيانات الحسابات ونظام الحماية اللحظي
# ==========================================
detailed_data = []
hall_summaries = []
notifications = ["📌 **حالة النظام:** نظام المحاكاة يعمل بكفاءة تامة."]
total_system_power = 0.0
active_count = 0
load_categories = {"التكييف ❄️": 0.0, "الإضاءة 💡": 0.0, "أجهزة أخرى ⚙️": 0.0}

for hall, devices in st.session_state.initial_halls.items():
    hall_power = 0.0
    hall_device_states = {}

    for dev, pwr in devices.items():
        state = "يعمل 🟢"
        current_pwr = pwr

        if hall == selected_hall and dev == target_appliance:
            if user_action == "إطفاء 🔴":
                state = "منطفئ 🔴"
                current_pwr = 0.0

        hall_device_states[dev] = {"state": state, "power": current_pwr}
        hall_power += current_pwr

    if hall_power > threshold_kw:
        notifications.append(f"🚨 **[إنذار حماية الأحمال]:** تجاوزت الطاقة في **{hall}** القيمة المسموحة ({round(hall_power, 2)} kW). **تم تفعيل الفصل الآلي للأجهزة الثقيلة!**")
        hall_power = 0.0
        for dev in hall_device_states:
            if "مكيف" in dev:
                hall_device_states[dev]["state"] = "مفصول حماية ⚡"
                hall_device_states[dev]["power"] = 0.0
            hall_power += hall_device_states[dev]["power"]

    for dev, info in hall_device_states.items():
        pwr = info["power"]
        st_val = info["state"]
        if "يعمل" in st_val:
            active_count += 1
            if "مكيف" in dev: load_categories["التكييف ❄️"] += pwr
            elif "مصباح" in dev or "إضاءة" in dev: load_categories["الإضاءة 💡"] += pwr
            else: load_categories["أجهزة أخرى ⚙️"] += pwr

        m_kwh = round(pwr * 8 * 30, 2)
        m_cost = round(m_kwh * tariff_rate, 2)
        detailed_data.append({
            "المبنى / القاعة": hall,
            "الجهاز": dev,
            "الحالة": st_val,
            "القدرة (kW)": pwr,
            "الاستهلاك الشهري (kWh)": m_kwh,
            "التكلفة (دينار)": f"{m_cost:,.0f}"
        })

    total_system_power += hall_power
    hall_summaries.append({
        "المبنى / القاعة": hall,
        "القدرة اللحظية (kW)": round(hall_power, 2),
        "الاستهلاك الشهري (kWh)": round(hall_power * 8 * 30, 2),
        "التكلفة الشهرية (دينار)": round(hall_power * 8 * 30 * tariff_rate, 0)
    })

df_app = pd.DataFrame(detailed_data)
df_hall = pd.DataFrame(hall_summaries)
total_bill = total_system_power * 8 * 30 * tariff_rate

# ==========================================
# 6. شاشة الودجات العلوية (iOS Metric Cards)
# ==========================================
col1, col2, col3, col4 = st.columns(4)
col1.metric("⚡ إجمالي القدرة", f"{round(total_system_power, 2)} kW")
col2.metric("🔌 الأجهزة النشطة", f"{active_count} جهاز")
col3.metric("💰 التكلفة الشهرية", f"{total_bill:,.0f} IQD")
col4.metric("🛡️ حالة النظام", "⚠️ حماية نشطة" if len(notifications) > 1 else "مستقر وآمن 🟢")

st.markdown("---")

# ==========================================
# 7. عرض الأقسام والصفحات بالتفصيل
# ==========================================
if navigation_page.startswith("1️⃣"):
    st.subheader("🎛️ لوحة التشغيل والتحكم الافتراضي")
    st.write("مخصصة لعرض كيفية استجابة النظام للأوامر الفورية والتحكم بالأجهزة لكل قاعة ومبنى لحظياً.")
    st.dataframe(df_app, use_container_width=True)

elif navigation_page.startswith("2️⃣"):
    st.subheader("🏗️ هندسة وتعديل المباني والقاعات")
    st.write("أثناء العرض أمام اللجنة، يمكنك هنا إضافة أو حذف المباني والقاعات لإثبات مرونة النظام.")

    new_hall = st.text_input("اسم المبنى أو القاعة الجديدة:")
    if st.button("إضافة المبنى ➕"):
        if new_hall and new_hall not in st.session_state.initial_halls:
            st.session_state.initial_halls[new_hall] = {"إضاءة رئيسية": 0.05}
            st.success(f"تم إضافة المبنى ({new_hall}) بنجاح!")
            st.rerun()

    del_hall = st.selectbox("اختر القاعة للحذف:", list(st.session_state.initial_halls.keys()))
    if st.button("حذف القاعة 🗑️"):
        if len(st.session_state.initial_halls) > 1:
            del st.session_state.initial_halls[del_hall]
            st.warning(f"تم حذف القاعة ({del_hall}).")
            st.rerun()
        else:
            st.error("يجب أن تبقى قاعة واحدة على الأقل في النظام.")

elif navigation_page.startswith("3️⃣"):
    st.subheader("📡 شاشة الحساسات الحية ومؤشرات SCADA")
    for hall in st.session_state.initial_halls:
        st.info(f"🏛️ **{hall}** — الحالة: متصل بنجاح عبر بروتوكول MQTT/IoT")

elif navigation_page.startswith("4️⃣"):
    st.subheader("📊 المخططات والتحليلات البيانية للأحمال")
    c1, c2 = st.columns(2)
    with c1:
        if not df_hall.empty:
            fig_bar = px.bar(df_hall, x="المبنى / القاعة", y="القدرة اللحظية (kW)", title="مقارنة قدرة المباني الحية", template="plotly_dark")
            fig_bar.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig_bar, use_container_width=True)
    with c2:
        fig_radar = go.Figure(data=go.Scatterpolar(
            r=[load_categories["التكييف ❄️"], load_categories["الإضاءة 💡"], load_categories["أجهزة أخرى ⚙️"]],
            theta=["التكييف ❄️", "الإضاءة 💡", "أخرى ⚙️"],
            fill='toself',
            line_color='#ef4444'
        ))
        fig_radar.update_layout(title="رادار توزيع الأحمال الهندسي", template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_radar, use_container_width=True)

elif navigation_page.startswith("5️⃣"):
    st.subheader("🏛️ التقارير المالية وجداول الاستهلاك")
    tab1, tab2 = st.tabs(["ملخص المباني", "مصفوفة الأجهزة التفصيلية"])
    with tab1:
        st.dataframe(df_hall, use_container_width=True)
    with tab2:
        st.dataframe(df_app, use_container_width=True)

elif navigation_page.startswith("6️⃣"):
    st.subheader("🔔 مركز التنبيهات وحماية الشبكة")
    for note in notifications:
        st.warning(note)

elif navigation_page.startswith("7️⃣"):
    st.subheader("🤖 التنبؤ الذكي بالذكاء الاصطناعي للأحمال المستقبلية")
    st.info("يتوقع نموذج الذكاء الاصطناعي أحمال الطاقة للأيام القادمة بناءً على معدلات الاستهلاك الحالي.")
    hours = np.arange(0, 24)
    pred_load = [total_system_power * (1 + 0.3 * np.sin(h/3)) for h in hours]
    fig_pred = px.line(x=hours, y=pred_load, labels={"x": "الساعة", "y": "القدرة المتوقعة (kW)"}, title="منحنى التنبؤ بالأحمال على مدار 24 ساعة", template="plotly_dark")
    st.plotly_chart(fig_pred, use_container_width=True)

elif navigation_page.startswith("8️⃣"):
    st.subheader("📊 مقارنة استهلاك القاعات والمباني")
    if not df_hall.empty:
        fig_comp = px.bar(df_hall, x="المبنى / القاعة", y="الاستهلاك الشهري (kWh)", color="المبنى / القاعة", title="مقارنة الاستهلاك الشهري بين القاعات (kWh)", template="plotly_dark")
        st.plotly_chart(fig_comp, use_container_width=True)

elif navigation_page.startswith("9️⃣"):
    st.subheader("🤖 الدعم الفني وربط اللوحات المصغرة (IoT)")
    q = st.text_input("💬 اطرح سؤالاً موجهاً للمساعد الذكي (اختبار اللجنة):")
    if q:
        st.success(f"💡 **تحليل المساعد:** استفسارك ('{q}') يتعلق بكفاءة التشغيل الذكي وربط اللوحات المصغرة (ESP32) بالمنصة السحابية.")
    else:
        st.info("أهلاً بك! نظام المحاكاة جاهز بالكامل لعرضه ومناقشته أمام اللجنة.")

elif navigation_page.startswith("📱"):
    st.subheader("📱 دليل تثبيت التطبيق وتثبيته على شاشة الأيفون")
    st.markdown(
        """
        <div style="background-color: #170404; padding: 20px; border-radius: 16px; border: 1px solid #4a1212; direction: rtl; text-align: right;">
            <h3 style="color: #ffffff; margin-top: 0;">كيفية تحميل وتثبيت التطبيق كـ PWA على iPhone:</h3>
            <p>لقد قمنا بتهيئة وتطوير هذا النظام ليدعم ميزة الـ <b>Progressive Web App (PWA)</b> على نظام iOS بالكامل عبر ربطه بملف الـ HTML الخارجي.</p>
            <h4 style="color: #fca5a5; margin-bottom: 8px;">اتبع الخطوات البسيطة التالية:</h4>
            <ol style="line-height: 1.8; color: #fbcfe8; padding-right: 20px;">
                <li>فتح رابط التطبيق بمتصفح <b>Safari</b>.</li>
                <li>ضغط زر <b>المشاركة 📤</b>.</li>
                <li>اختيار <b>"إضافة إلى الشاشة الرئيسية" 📱</b>.</li>
            </ol>
        </div>
        """,
        unsafe_allow_html=True
    )
