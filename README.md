# Langflow-Customer-Support-Agent
An **LLM-powered, multi-agent** chatbot using **Langflow, Streamlit, and OpenAI GPT-4o mini**, with **RAG-based retrieval** via **AstraDB**, a vector database. It dynamically routes queries to specialized agents (*FAQAgent*, *OrderLookupAgent*) for accurate, context-aware responses. Includes **vector search** and **file upload for knowledge expansion**.


## 🌟 Features
- **Multi-Agent Architecture**: Uses specialized agents (*FAQAgent*, *OrderLookupAgent*, *ManagerAgent*) for handling different tasks.
- **RAG-powered Retrieval**: Integrates AstraDB to fetch relevant information based on user queries.
- **Dynamic Routing**: The *ManagerAgent* directs queries to the appropriate agent for accurate responses.
- **File Upload for Knowledge Base Expansion**: Users can upload files to enrich the FAQ database.
- **Built with Streamlit**: Provides an interactive and user-friendly frontend.

---

## 📸 App Interface

<img width="750" alt="image" src="https://github.com/user-attachments/assets/bb476c51-773d-4037-a4db-ae8da4ac0371" />
<img width="750" alt="image" src="https://github.com/user-attachments/assets/b3011b32-e2cc-40da-96cb-7c2817e1c9c4" />
<img width="750" alt="image" src="https://github.com/user-attachments/assets/1acb7696-29a8-4a9d-aba9-7c5a79610fc0" />
<img width="750" alt="image" src="https://github.com/user-attachments/assets/61ac0f1a-2a62-4d86-8cb0-a780eff5d1c9" />
<img width="750" alt="image" src="https://github.com/user-attachments/assets/15ad4cff-09f3-430b-85f9-8728857fa45a" />

--

## 🎥 Demo Video

https://github.com/user-attachments/assets/27c3c4b6-4ff5-4627-ae17-878ad72642a8

---

## 🛠 Tech Stack
- **Langflow** – For building multi-agent workflows.
- **Streamlit** – Web UI framework.
- **AstraDB** – Vector storage for RAG-based retrieval.
- **OpenAI GPT-4o mini** – LLM powering the agents.

---

## 📌 How It Works

### 1️⃣ Query Handling
- User inputs a question.
- The *ManagerAgent* determines the best agent to handle the request.
  
### 2️⃣ RAG & FAQ Retrieval
- **AstraDB** stores FAQ entries as vectors.
- Queries are embedded using **NV-Embed-QA** and matched against stored FAQs.
- Results are parsed and injected into the agent's prompt for context-aware responses.

### 3️⃣ Order Lookup
- The *OrderLookupAgent* retrieves product and order details from AstraDB.
- Uses structured queries based on **orderNumber** and **productId**.

### 4️⃣ Multi-Agent Task Delegation
- The *ManagerAgent* intelligently routes queries:
  - **General Queries** → *FAQAgent*
  - **Order/Product Queries** → *OrderLookupAgent*
  - Aggregates responses and returns a structured answer.

### 5️⃣ File Upload for FAQ Expansion
- In the backend, the admin can upload documents to expand the FAQ knowledge base.
- Files are split into chunks and stored as vector embeddings in AstraDB.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- AstraDB Account (for vector storage)
- OpenAI API Key (for GPT-4o mini)
- Streamlit installed

### Installation
```shell
git clone https://github.com/AkshatBhat/Langflow-Customer-Support-Agent.git

cd Langflow-Customer-Support-Agent

pip install -r requirements.txt
```

### Configuration
Set the environment variable for AstraDB Application Token in a .env file (refer to the .env.example file).

### Running the App
```shell
streamlit run app.py
```

---

## 📝 Example Queries
- **General FAQ**: "How can I track my order?"
- **Order Lookup**: "Where is my order with ID #1001?"
- **Product Details**: "What are the features of Product #101?"

---

## 📜 License
MIT License
