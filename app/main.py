import streamlit as st
from app.utils import read_csv, write_csv
from app.search_api import search
from app.llm_agent import parse_search_results
from app.google_sheets import load_google_sheet
import pandas as pd
st.title("AI-Powered Data Search")

# Upload file or connect Google Sheet
option = st.selectbox("Data Source", ["Upload CSV", "Google Sheet"])
if option == "Upload CSV":
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    if uploaded_file:
        df = read_csv(uploaded_file)
elif option == "Google Sheet":
    sheet_id = st.text_input("Google Sheet ID")
    range_name = st.text_input("Range Name")
    if sheet_id and range_name:
        df = load_google_sheet(sheet_id, range_name)

# Display Data
if "df" in locals():
    st.write(df)
    column = st.selectbox("Select the column with entities", df.columns)

    # Input Custom Prompt
    prompt = st.text_area("Enter your prompt for information retrieval")

    if st.button("Start Search"):
        results = []
        for entity in df[column]:
            query = f"{entity} {prompt}"
            search_results = search(query)
            result = parse_search_results(search_results, prompt)
            results.append({"Entity": entity, "Extracted Info": result})
        
        result_df = pd.DataFrame(results)
        st.write(result_df)

        # Download Results
        st.download_button(
            label="Download Results as CSV",
            data=result_df.to_csv(index=False).encode("utf-8"),
            file_name="search_results.csv",
            mime="text/csv"
        )
