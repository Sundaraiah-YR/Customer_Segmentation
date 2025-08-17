import streamlit as st
import pickle
import numpy as np

# ---------------------------
# Load the KMeans model
# ---------------------------
with open('Kmodel.pkl', 'rb') as file:
    kmeans_model = pickle.load(file)

# ---------------------------
# Cluster mapping (based on your table)
# ---------------------------
cluster_details = {
    0: {
        "name": "Budget Big Spenders",
        "color": "Yellow",
        "income_range": "15–40 k$",
        "spending_range": "60–100",
        "description": "Low income, high spending",
        "strategy": "Offer affordable but trendy products; use discounts & loyalty cards"
    },
    1: {
        "name": "Premium Customers",
        "color": "Red",
        "income_range": "60–100 k$",
        "spending_range": "60–100",
        "description": "High income, high spending",
        "strategy": "Focus on luxury products, premium services, exclusive offers"
    },
    2: {
        "name": "Price-Conscious Customers",
        "color": "Blue",
        "income_range": "15–40 k$",
        "spending_range": "0–40",
        "description": "Low income, low spending",
        "strategy": "Minimal marketing spend, cost-effective promotions"
    },
    3: {
        "name": "Average Customers",
        "color": "Green",
        "income_range": "40–70 k$",
        "spending_range": "40–60",
        "description": "Balanced income and spending",
        "strategy": "Maintain loyalty, seasonal campaigns, product bundles"
    },
    4: {
        "name": "Potential Customers",
        "color": "Pink/Violet",
        "income_range": "70–140 k$",
        "spending_range": "0–40",
        "description": "High income, low spending",
        "strategy": "Personalized marketing, highlight value propositions"
    }
}

# ---------------------------
# Streamlit UI
# ---------------------------
st.title("🛍 Mall Customer Segmentation")
st.write("Predict customer cluster based on Annual Income and Spending Score.")

# User inputs
annual_income = st.number_input("Annual Income (k$)", min_value=0, max_value=200, value=50)
spending_score = st.number_input("Spending Score (1-100)", min_value=1, max_value=100, value=50)

# Predict button
if st.button("Predict Cluster"):
    # Prepare input
    input_data = np.array([[annual_income, spending_score]])
    
    # Predict
    cluster_num = kmeans_model.predict(input_data)[0]
    cluster_info = cluster_details[cluster_num]
    
    # Display result
    st.success(f"🎯 Predicted Cluster: **{cluster_num + 1} - {cluster_info['name']}**")
    st.markdown(f"**Color in Plot:** {cluster_info['color']}")
    st.markdown(f"**Annual Income Range:** {cluster_info['income_range']}")
    st.markdown(f"**Spending Score Range:** {cluster_info['spending_range']}")
    st.markdown(f"**Customer Type:** {cluster_info['description']}")
    st.markdown(f"**Business Strategy:** {cluster_info['strategy']}")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit & KMeans Clustering")