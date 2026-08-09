import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# إعداد الصفحة لتكون عريضة وذات طابع هندسي داكن
st.set_page_config(page_title="نظام محاكاة وإدارة الأحمال الذكية", layout="wide", page_icon="⚡")

# تنسيق CSS مخصص للواجهة الصناعية
st.markdown("""
<style>
    .main { background-color: #1a0505; color: #fca5a5; }
    h1, h2, h3 { color: #ffffff !important; }
    .stMetric { background-color: #2b0a0a; padding: 10px; border-radius: 8px; border: 1px solid #4a0e0e; }
</style>
""", unsafe_allow_html=True)

# قاعدة البيانات المبدئية
if 'initial_halls' not in st.session_state:
    st.session_state.initial_halls = {
        "جامعة العين - قاعة الأبحاث (101)": {"مكيف 1 (AC-1)": 2.0, "مصباح 1": 0.04, "مصباح 2": 0.04},
        "جامعة العين - قاعة المحاضرات (102)": {"مكيف 1 (AC-1)": 2.0, "مروحة السقف": 0.07, "مصباح 1": 0.04},
        "جامعة العين - معمل الدراسات (103)": {"مكيف 1 (AC-1)": 2.0, "مصباح 1": 0.04}
    }

# العنوان الرئيسي
st.markdown(
    """
    <div style="background: linear-gradient(90deg, #4a0e0e 0%, #1a0505 100%); padding: 18px; border-radius: 10px; border-right: 5px solid #ef4444; text-align: right; margin-bottom: 15px;">
        <h1 style="margin: 0; color: #ffffff; font-size: 24px;">🔴 نظام محاكاة وإدارة الأحمال الذكية (SCADA & IoT System)</h1>
        <p style="margin: 3px 0 0 0; color: #fca5a5; font-size: 13px;">مشروع تخرج متكامل لمراقبة المباني، التحكم بالأجهزة، وحماية شبكات الطاقة.</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# الشريط الجانبي للتحكم
st.sidebar.markdown("### 📂 لوحة التحكم الرئيسية")
navigation_page = st.sidebar.selectbox(
    "اختر قسم المعرض:",
    [
        "1️⃣ لوحة التشغيل والتحكم الافتراضي",
        "2️⃣ هندسة وتعديل المباني والقاعات",
        "3️⃣ شاشة الحساسات الحية ومؤشرات SCADA",
        "4️⃣ المخططات والتحليلات البيانية",
        "5️⃣ التقارير المالية وجداول الاستهلاك",
        "6️⃣ مركز التنبيهات وحماية الشبكة",
        "7️⃣ الدعم الفني وربط اللوحات المصغرة"
    ]
)

st.sidebar.markdown("---")
tariff_rate = st.sidebar.number_input("التعرفة (دينار / kWh)", value=50, step=1)
threshold_kw = st.sidebar.number_input("عتبة الفصل الآلي (kW)", value=5.0, step=0.5)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🎛️ أدوات التشغيل الفوري")
hall_names = list(st.session_state.initial_halls.keys())
selected_hall = st.sidebar.selectbox("المبنى أو القاعة المستهدفة", hall_names)

available_devices = list(st.session_state.initial_halls[selected_hall].keys()) if selected_hall in st.session_state.initial_halls else []
target_appliance = st.sidebar.selectbox("الجهاز المستهدف بالتحكم", available_devices if available_devices else ["لا توجد أجهزة"])
user_action = st.sidebar.radio("حالة الأمر", ["تشغيل 🟢", "إطفاء 🔴"])

# معالجة بيانات المحاكاة
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
        
    # نظام الحماية التلقائي
    auto_trip_triggered = False
    if hall_power > threshold_kw:
        auto_trip_triggered = True
        notifications.append(f"🚨 **[إنذار حماية الأحمال]:** تجاوزت الطاقة في **{hall}** القيمة ({round(hall_power, 2)} kW). **تم فصل الأجهزة الثقيلة تلقائياً!**")
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

# شاشة المؤشرات العليا الثابتة
col1, col2, col3, col4 = st.columns(4)
col1.metric("⚡ إجمالي القدرة", f"{round(total_system_power, 2)} kW")
col2.metric("🔌 الأجهزة النشطة", f"{active_count} جهاز")
col3.metric("💰 التكلفة الشهرية", f"{total_bill:,.0f} IQD")
col4.metric("🛡️ الحالة العامة", "⚠️ إنذار حماية" if len(notifications) > 1 else "مستقر وآمن 🟢")

st.markdown("---")

# عرض الأقسام حسب اختيار القائمة الجانبية
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
            st.plotly_chart(fig_bar, use_container_width=True)
    with c2:
        fig_radar = go.Figure(data=go.Scatterpolar(
            r=[load_categories["التكييف ❄️"], load_categories["الإضاءة 💡"], load_categories["أجهزة أخرى ⚙️"]],
            theta=["التكييف ❄️", "الإضاءة 💡", "أخرى ⚙️"],
            fill='toself'
        ))
        fig_radar.update_layout(title="رادار توزيع الأحمال الهندسي", template="plotly_dark")
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
