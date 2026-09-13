import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='whitegrid')

st.set_page_config(page_title="E-Commerce Public Dataset Dashboard", layout="wide")


@st.cache_data
def load_data():
    df = pd.read_csv("main_data.csv")
    df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])
    df["order_delivered_customer_date"] = pd.to_datetime(df["order_delivered_customer_date"])
    df["order_estimated_delivery_date"] = pd.to_datetime(df["order_estimated_delivery_date"])
    return df


main_df = load_data()

# ---------- Sidebar filter ----------
st.sidebar.header("Filter")
min_date = main_df["order_purchase_timestamp"].min().date()
max_date = main_df["order_purchase_timestamp"].max().date()

date_range = st.sidebar.date_input(
    "Rentang Tanggal Pembelian",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date,
)

if len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date, end_date = min_date, max_date

state_options = ["Semua"] + sorted(main_df["customer_state"].dropna().unique().tolist())
selected_state = st.sidebar.selectbox("Customer State", state_options)

filtered_df = main_df[
    (main_df["order_purchase_timestamp"].dt.date >= start_date)
    & (main_df["order_purchase_timestamp"].dt.date <= end_date)
]
if selected_state != "Semua":
    filtered_df = filtered_df[filtered_df["customer_state"] == selected_state]

# ---------- Header ----------
st.title("📊 E-Commerce Public Dataset Dashboard")
st.markdown(
    "Dashboard interaktif untuk menjawab pertanyaan bisnis seputar **keterlambatan "
    "pengiriman vs review score** dan **tren pembayaran bulanan**, berdasarkan Olist "
    "Brazilian E-Commerce Dataset."
)

# ---------- Metrics ----------
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Order", f"{filtered_df['order_id'].nunique():,}")
with col2:
    total_payment = filtered_df["payment_value"].sum()
    st.metric("Total Nilai Pembayaran", f"BRL {total_payment:,.0f}")
with col3:
    late_rate = filtered_df["is_late"].mean() * 100 if len(filtered_df) else 0
    st.metric("Late Delivery Rate", f"{late_rate:.1f}%")
with col4:
    avg_review = filtered_df["review_score"].mean()
    st.metric("Rata-rata Review Score", f"{avg_review:.2f}" if pd.notna(avg_review) else "N/A")

st.markdown("---")

# ---------- Pertanyaan 1 ----------
st.subheader("Pertanyaan 1: Keterlambatan Pengiriman & Kategori Produk vs Review Score")

c1, c2 = st.columns(2)

with c1:
    late_summary = filtered_df.groupby("is_late")["review_score"].mean().reindex([False, True])
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.bar(["Tepat Waktu", "Terlambat"], late_summary.values, color=["#72BCD4", "#D3D3D3"])
    ax.set_ylabel("Rata-rata Review Score")
    ax.set_ylim(0, 5)
    for i, v in enumerate(late_summary.values):
        if pd.notna(v):
            ax.text(i, v + 0.1, f"{v:.2f}", ha="center", fontweight="bold")
    ax.set_title("Review Score: Tepat Waktu vs Terlambat")
    st.pyplot(fig)

with c2:
    cat_review = filtered_df.groupby("product_category_name_english")["review_score"].agg(["mean", "count"])
    cat_review = cat_review[cat_review["count"] >= 20].sort_values("mean").head(5)
    fig, ax = plt.subplots(figsize=(5, 4))
    colors = ["#72BCD4"] + ["#D3D3D3"] * 4
    ax.barh(cat_review.index[::-1], cat_review["mean"][::-1], color=colors[::-1])
    ax.set_xlim(0, 5)
    ax.set_xlabel("Rata-rata Review Score")
    ax.set_title("5 Kategori dengan Review Score Terendah")
    st.pyplot(fig)

st.caption("Order yang terlambat secara konsisten memiliki review score jauh lebih rendah dibandingkan order tepat waktu.")

st.markdown("---")

# ---------- Pertanyaan 2 ----------
st.subheader("Pertanyaan 2: Tren Total Nilai Pembayaran Bulanan")

monthly_df = filtered_df.copy()
monthly_df["month"] = monthly_df["order_purchase_timestamp"].dt.to_period("M").astype(str)
monthly_payment = monthly_df.groupby("month")["payment_value"].sum().reset_index()

fig, ax = plt.subplots(figsize=(12, 4))
ax.plot(monthly_payment["month"], monthly_payment["payment_value"], marker="o", color="#D3D3D3")

if len(monthly_payment) > 0:
    peak_idx = monthly_payment["payment_value"].idxmax()
    peak_month = monthly_payment.loc[peak_idx, "month"]
    peak_value = monthly_payment.loc[peak_idx, "payment_value"]
    ax.plot(peak_month, peak_value, marker="o", color="#72BCD4", markersize=10)
    ax.annotate(
        f"{peak_month}\nBRL {peak_value:,.0f}",
        xy=(peak_month, peak_value),
        xytext=(0, 15),
        textcoords="offset points",
        ha="center",
        fontweight="bold",
    )
    ax.set_ylim(0, monthly_payment["payment_value"].max() * 1.25)

ax.set_xlabel("Bulan")
ax.set_ylabel("Total Nilai Pembayaran")
ax.set_title("Tren Total Nilai Pembayaran per Bulan")
plt.xticks(rotation=45)
st.pyplot(fig)

st.markdown("---")

# ---------- Geospatial ----------
st.subheader("Analisis Lanjutan: Rata-rata Waktu Pengiriman per State")

state_delivery = filtered_df.groupby("customer_state").agg(
    avg_delivery_days=("delivery_days", "mean"),
    n_orders=("order_id", "count"),
).reset_index()
state_delivery = state_delivery[state_delivery["n_orders"] >= 10].sort_values("avg_delivery_days", ascending=False).head(10)

fig, ax = plt.subplots(figsize=(10, 5))
colors = ["#72BCD4"] + ["#D3D3D3"] * (len(state_delivery) - 1)
ax.barh(state_delivery["customer_state"][::-1], state_delivery["avg_delivery_days"][::-1], color=colors[::-1])
ax.set_xlabel("Rata-rata Hari Pengiriman")
ax.set_title("10 State dengan Rata-rata Waktu Pengiriman Terlama")
st.pyplot(fig)

st.caption("Copyright (c) Novia Dwi Cahyanti 2026")
