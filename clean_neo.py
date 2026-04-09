import os
from dotenv import load_dotenv
from llama_index.graph_stores.neo4j import Neo4jGraphStore

load_dotenv()

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


if __name__ == "__main__":
    graph_store.query(
        """
    MATCH (n) DETACH DELETE n
    """
    )