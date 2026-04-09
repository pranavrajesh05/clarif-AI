<div align="center">

# 🔬 ClarifAI

**Transform complex research papers into visual, interactive summaries powered by AI**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://python.org)
[![Node.js](https://img.shields.io/badge/Node.js-18+-339933?logo=node.js&logoColor=white)](https://nodejs.org)
[![Neo4j](https://img.shields.io/badge/Neo4j-Graph_DB-4581C3?logo=neo4j&logoColor=white)](https://neo4j.com)
[![Flask](https://img.shields.io/badge/Flask-Backend-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com)

</div>

---

## 📖 About

**ClarifAI** is an AI-powered tool that takes dense research papers and transforms them into **simplified visual summaries** with an **interactive Q&A chatbot**. Upload a PDF, and the system will:

1. **Parse** the document using LlamaParse
2. **Build a knowledge graph** in Neo4j for structured understanding
3. **Summarize** the content using Groq LLMs (LLaMA 3)
4. **Generate illustrative images** for each section via Krutrim Cloud's Stable Diffusion
5. **Launch an interactive dashboard** with a chatbot that answers questions about the paper

---

## 🏗️ Architecture

```
┌────────────────┐     ┌──────────────┐     ┌─────────────────┐
│  Upload UI     │────▶│  Node.js     │────▶│  Python Pipeline│
│  (frontend/)   │     │  (server.js) │     │  (init.py)      │
└────────────────┘     └──────────────┘     └────────┬────────┘
                                                     │
                        ┌────────────────────────────┤
                        ▼                            ▼
                ┌──────────────┐          ┌─────────────────┐
                │  parser2.py  │          │  clarifai.py    │
                │  PDF → Text  │          │  Summarize +    │
                │  + Neo4j KG  │          │  Image Prompts  │
                └──────────────┘          └────────┬────────┘
                        │                          │
                        ▼                          ▼
                ┌──────────────┐          ┌─────────────────┐
                │  graph.py    │          │  image_gen.py   │
                │  Visualize   │          │  Stable Diffusion│
                │  Knowledge   │          │  Image Gen      │
                │  Graph       │          └─────────────────┘
                └──────────────┘
                        │
                        ▼
                ┌──────────────────────────────────┐
                │         dashboard.py             │
                │  Flask App: Visual Summary +     │
                │  Knowledge Graph + Chat Q&A      │
                └──────────────────────────────────┘
```

---

## ⚙️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend (Upload)** | HTML, CSS, JavaScript |
| **Upload Server** | Node.js, Express, Multer |
| **Document Parsing** | LlamaParse |
| **Knowledge Graph** | Neo4j + LlamaIndex |
| **LLM Summarization** | Groq (LLaMA 3 8B) |
| **Image Generation** | Krutrim Cloud (Stable Diffusion XL) |
| **Q&A Chatbot** | OpenAI GPT-4o-mini + Neo4j Agent |
| **Dashboard** | Flask + Bootstrap |

---

## 📁 Project Structure

```
ClarifAI/
├── frontend/               # Upload page UI
│   ├── index.html
│   ├── script.js
│   ├── style.css
│   └── logo.png
├── templates/
│   └── index.html          # Dashboard template (Flask)
├── static/                 # Generated summaries & images
│   └── output/             # AI-generated images
├── uploads/                # Uploaded research papers
├── server.js               # Node.js file upload server
├── init.py                 # Pipeline orchestrator
├── parser2.py              # PDF parsing + knowledge graph builder
├── clarifai.py             # LLM summarization + image prompt generation
├── image_gen.py            # Stable Diffusion image generation
├── graph.py                # Neo4j graph visualization
├── clean_neo.py            # Neo4j database cleanup utility
├── dashboard.py            # Flask dashboard + chatbot server
├── package.json            # Node.js dependencies
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variable template
└── .gitignore
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10+**
- **Node.js 18+**
- **Neo4j Aura** (or self-hosted) database instance
- API keys for: OpenAI, Groq, LlamaParse, Krutrim Cloud

### 1. Clone the Repository

```bash
git clone https://github.com/pranavrajesh05/clarif-AI.git
cd clarif-AI
```

### 2. Set Up Environment Variables

```bash
cp .env.example .env
```

Edit `.env` and fill in your API keys:

```env
OPENAI_API_KEY=sk-...
GROQ_API_KEY=gsk_...
LLAMA_CLOUD_API_KEY=llx-...
KRUTRIM_API_KEY=...
NEO4J_URI=neo4j+s://...
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=...
NEO4J_DATABASE=neo4j
```

### 3. Install Dependencies

```bash
# Python dependencies
pip install -r requirements.txt

# Node.js dependencies
npm install
```

### 4. Run the Application

```bash
# Start the upload server
node server.js
```

Then open `http://localhost:3000` in your browser, upload a research paper (PDF), and the pipeline will automatically:
- Parse the document and build a knowledge graph
- Generate a visual summary with AI-generated images
- Launch the interactive dashboard at `http://localhost:5000`

---

## 🔄 How It Works

1. **Upload** — Drag & drop a research paper PDF on the upload page
2. **Parse** — LlamaParse extracts text; LlamaIndex builds a knowledge graph in Neo4j
3. **Summarize** — Groq LLM creates an accessible, paragraph-by-paragraph summary
4. **Illustrate** — Each paragraph gets an AI-generated image via Stable Diffusion
5. **Visualize** — The Neo4j knowledge graph is rendered as a network diagram
6. **Interact** — The Flask dashboard displays everything with a chatbot for Q&A

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">
  <b>Built with ❤️ by the ClarifAI Team</b>
</div>
