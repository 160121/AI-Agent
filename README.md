# AI Agent for Information Retrieval

This project is an AI-powered agent that reads through a dataset (CSV or Google Sheets), performs web searches for specified entities, and extracts structured information using a language model. It features an intuitive dashboard for data upload, query definition, and results visualization.

## Features
- Upload CSV files or connect to Google Sheets.
- Define dynamic queries with placeholders for custom information retrieval.
- Leverage web search APIs (SerpAPI/ScraperAPI) for automated data collection.
- Process and parse search results using LLMs (e.g., OpenAI's GPT API).
- Display extracted data in a structured table format.
- Download results as a CSV or update Google Sheets.

## Technologies Used
- **Frontend/Dashboard**: Streamlit
- **Backend**: Python, Flask
- **Data Handling**: Pandas, Google Sheets API
- **Search API**: SerpAPI/ScraperAPI
- **LLM API**: OpenAI GPT API
- **Agent Framework**: LangChain

## Prerequisites
- Python 3.9 or higher
- API keys for:
  - Google Sheets API
  - SerpAPI or ScraperAPI
  - OpenAI GPT API
- A Google Cloud project for Sheets integration (if required)

## Setup Instructions
1. **Clone the Repository**
   ```bash
   git clone https://github.com/160121/AI-Agent.git
   cd AI-Agent
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
3. **Set Up Environment Variables**:Create a .env file in the root directory and add the following keys:
   ```bash
   GOOGLE_SHEETS_API_KEY=your-google-sheets-api-key
   SERP_API_KEY=your-serpapi-key
   OPENAI_API_KEY=your-openai-api-key

4. **Run the Application**
   ```bash
   python -m streamlit run app/main.py
5. **Access the Dashboard**: Open your browser and navigate to
   ```bash
   http://localhost:8501

## How to Use
- Upload a CSV file or connect to a Google Sheet.
- Select the primary column containing the entities (e.g., company names).
- Enter a dynamic query in the prompt box (e.g., "Find the email address for {company}").
- View the extracted results in the dashboard.
- Download the results as a CSV or update the linked Google Sheet.
