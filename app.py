import requests
import os
from dotenv import load_dotenv
import streamlit as st
from streamlit_navigation_bar import st_navbar
import pandas as pd

import warnings

warnings.filterwarnings("ignore")

load_dotenv()

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "91f5152c-54cd-4794-8549-ed4c6343d982"
FLOW_ID = "8a91b921-f7ed-45ec-b176-304f7a5f673c"
APPLICATION_TOKEN = os.getenv("APP_TOKEN")
ENDPOINT = "customer"
PATH = os.path.dirname(__file__)


def run_flow(message: str) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
    headers = None
    headers = {
        "Authorization": "Bearer " + APPLICATION_TOKEN,
        "Content-Type": "application/json",
    }
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()


def main():

    st.set_page_config(
        page_title="Langflow Customer Support Agent", page_icon=":robot_face:"
    )

    st.title("Langflow Customer Support Agent")
    st.divider()
    st.markdown("####")

    pages = ["💬 Agent Chat", "📦 Products Data", "📜 Orders Data"]

    page = st_navbar(pages)

    # Display content based on selection
    if page == pages[0]:
        st.subheader("💬 Agent Chat")
        message = st.text_area(
            "Query",
            help="Ask your query in the chat box provided.",
            placeholder="How can I track my order?",
        )

        if st.button("Ask Agent"):
            if not message.strip():
                st.error("Please enter a query.")
                return

            try:
                with st.spinner("Agent is thinking..."):
                    response = run_flow(message)

                response = response["outputs"][0]["outputs"][0]["results"]["message"][
                    "text"
                ]
                st.markdown(f"{response}")

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

    elif page == pages[1]:
        st.subheader("📦 Products Data")
        st.markdown("#####")
        products = pd.read_csv(os.path.join(PATH, "sample_data/sample_products.csv"))
        st.dataframe(products)

    elif page == pages[2]:
        st.subheader("📜 Orders Data")
        st.markdown("#####")
        orders = pd.read_csv(os.path.join(PATH, "sample_data/sample_orders.csv"))
        st.dataframe(orders)

    st.markdown("######")
    st.divider()

    st.markdown(
        """
            <style>
                .footer {
                    text-align: center;
                }
            </style>
            <div class="footer">
                Built with ❤️ by Akshat
            </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
