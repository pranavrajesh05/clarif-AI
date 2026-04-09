import os
import logging
from dotenv import load_dotenv
from flask import Flask, render_template, send_from_directory, request, jsonify
import webbrowser
from threading import Timer
from llama_index.graph_stores.neo4j import Neo4jGraphStore
from llama_index.llms.openai import OpenAI
from llama_index.tools.neo4j import Neo4jQueryToolSpec
from llama_index.agent.openai import OpenAIAgent

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
NEO4J_DATABASE = os.getenv("NEO4J_DATABASE")

graph_store = Neo4jGraphStore(
    username=NEO4J_USERNAME,
    password=NEO4J_PASSWORD,
    url=NEO4J_URI,
    database=NEO4J_DATABASE,
)

llm = OpenAI(model="gpt-4o-mini", temperature=0)

gds_db = Neo4jQueryToolSpec(
    url=NEO4J_URI,
    user=NEO4J_USERNAME,
    password=NEO4J_PASSWORD,
    llm=llm,
    database=NEO4J_DATABASE,
)

tools = gds_db.to_tool_list()
agent = OpenAIAgent.from_tools(tools, verbose=True)


def open_browser():
    webbrowser.open_new_tab("http://127.0.0.1:5000/")


@app.route("/static/<path:filename>")
def serve_files(filename):
    return send_from_directory('static', filename)


@app.route("/uploads/<path:filename>")
def graph_files(filename):
    return send_from_directory('uploads', filename)


@app.route('/')
def index():
    return render_template('index.html')


def query_graph(question):
    response = agent.chat(question)
    if "I cannot generate a Cypher statement" in response.response:
        logger.info("Query is unrelated to the research paper. Stopping further processing.")
        return "I couldn't answer that, as it's not related to this research paper."
    return response.response


@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get("question", "")
    answer = query_graph(question)
    return jsonify({"response": answer})


if __name__ == '__main__':
    Timer(0, open_browser).start()
    app.run(port=5000, debug=True)
