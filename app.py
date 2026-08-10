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

            # التحقق مما إذا كان قد تم التعديل مسبقاً لمنع التكرار
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
                # إدخال الأكواد قبل نهاية وسم </head>
                if "</head>" in content:
                    content = content.replace("</head>", f"{pwa_tags}\n</head>")
                    with open(index_path, "w", encoding="utf-8") as f:
                        f.write(content)
    except Exception:
        pass

# تشغيل الترقية التلقائية للملف التعريفي
patch_streamlit_pwa()

# إعداد الصفحة لتكون عريضة ومحسنة مع أيقونة هندسية
st.set_page_config(
    page_title="نظام محاكاة وإدارة الأحمال الذكية",
    layout="wide",
    page_icon="⚡"
)

# ==========================================
# 2. تنسيق CSS مخصص للواجهة الصناعية المحسنة لهواتف آيفون (Responsive iOS Design)
# ==========================================
st.markdown("""
<style>
    /* إخفاء القوائم والترويسات الافتراضية غير المرغوبة مع الحفاظ على زر القائمة الجانبية */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .viewerBadge_link__1S137 {display: none !important;}

    /* إخفاء أزرار النشر والقائمة الإضافية لتطبيق أنيق */
    button[data-testid="stBaseButton-header"] { display: none !important; }
    button[data-testid="stMainMenuButton"] { display: none !important; }

    /* جعل الهيدر شفافاً ومناسباً لواجهة الهاتف */
    .stAppHeader {
        background-color: transparent !important;
        background: transparent !important;
    }
    header {
        background-color: transparent !important;
        background: transparent !important;
    }

    /* تلوين وتكبير زر التحكم في الشريط الجانبي ليسهل الضغط عليه في الآيفون */
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

    /* خلفية التطبيق والمظهر العام للأيفون مع مراعاة الحواف والمستشعرات */
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

    /* تحسين تصميم الكروت والمؤشرات لتشبه ودجات الأيفون (iOS Widgets) */
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

    /* تجميل الشريط الجانبي في الموبايل */
    section[data-testid="stSidebar"] {
        background-color: #120303 !important;
        border-right: 1px solid #2b0a0a !important;
    }

    /* تجميل أزرار الأوامر لتناسب شاشات اللمس (Touch Targets) */
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

    /* تحسين تصميم الجداول والبيانات لتلائم الهاتف */
    .stDataFrame {
        border-radius: 14px !important;
        overflow: hidden !important;
        border: 1px solid #3b0d0d !important;
    }

    /* تعديل الهوامش والأبعاد للهواتف */
    @media (max-width: 768px) {
        .block-container {
            padding-top: 10px !important;
            padding-bottom: 10px !important;
        }
        h1 {
            font-size: 1.6rem !important;
        }
        h2 {
            font-size: 1.2rem !important;
        }
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

# العنوان الرئيسي للتطبيق بنقوش هندسية
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
        "7️⃣ الدعم الفني وربط اللوحات المصغرة",
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

    # نظام الحماية التلقائي والإنقاذ اللحظي للأحمال
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
# 6. شاشة الودجات العلوية على الأيفون (iOS Metric Cards)
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
            <p>لقد قمنا بتهيئة وتطوير هذا النظام ليدعم ميزة الـ <b>Progressive Web App (PWA)</b> على نظام iOS بالكامل، لكي تفتحه وكأنه تطبيق أصيل (Native App) وبكامل دقة واجهات الأيفون بدون حواف المتصفح.</p>

            <h4 style="color: #fca5a5; margin-bottom: 8px;">اتبع الخطوات البسيطة التالية:</h4>
            <ol style="line-height: 1.8; color: #fbcfe8; padding-right: 20px;">
                <li>قم بفتح رابط هذا التطبيق باستخدام متصفح <b>Safari</b> على هاتف الأيفون الخاص بك.</li>
                <li>اضغط على زر <b>المشاركة (Share Button) 📤</b> الموجود في شريط الأدوات السفلي لمتصفح سفاري.</li>
                <li>مرر للأسفل قليلاً واضغط على خيار <b>"إضافة إلى الشاشة الرئيسية" (Add to Home Screen) 📱</b>.</li>
                <li>ستظهر لك نافذة لتسمية التطبيق، اضغط على <b>"إضافة" (Add)</b> في الزاوية العلوية اليمنى.</li>
                <li>اذهب إلى شاشة الأيفون الرئيسية؛ ستجد أيقونة التطبيق المخصصة بـ <b>شعار الطاقة والصاعقة الذكية ⚡</b> مضافة وتعمل بلمسة واحدة في كامل الشاشة دون أشرطة تصفح!</li>
            </ol>

            <div style="background-color: #2b0a0a; padding: 12px; border-radius: 10px; margin-top: 15px; border-right: 4px solid #ef4444;">
                <p style="margin: 0; font-size: 13px; color: #ffffff;"><b>💡 نصيحة للجنة المناقشة:</b> عند عرض التطبيق على الهاتف مباشرة كـ PWA، سيتفاعل الـ SCADA بشكل فوري ومستقر للغاية مع اللمس وتوزيع الحساسات بشكل هندسي رائع.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
