import os
from dotenv import load_dotenv
from llama_parse import LlamaParse
from llama_index.core import KnowledgeGraphIndex, StorageContext
from llama_index.graph_stores.neo4j import Neo4jGraphStore

load_dotenv()

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
NEO4J_DATABASE = os.getenv("NEO4J_DATABASE")

upload_folder = "./uploads"


def parse_docs():
    parser = LlamaParse(
        api_key=os.getenv("LLAMA_CLOUD_API_KEY"),
        result_type="markdown",
        num_workers=4,
        verbose=True,
        language="en",
    )

    graph_store = Neo4jGraphStore(
        username=NEO4J_USERNAME,
        password=NEO4J_PASSWORD,
        url=NEO4J_URI,
        database=NEO4J_DATABASE,
    )

    file_list = os.listdir(upload_folder)
    if len(file_list) == 1:
        document_path = os.path.join(upload_folder, file_list[0])
        documents = parser.load_data(document_path)

    storage_context = StorageContext.from_defaults(graph_store=graph_store)
    index = KnowledgeGraphIndex.from_documents(
        documents,
        storage_context=storage_context,
        max_triplets_per_chunk=2,
    )

    print("Graph data uploaded successfully.")
    return documents


if __name__ == "__main__":
    file_content = parse_docs()
    with open("parsed_content.txt", 'w') as file:
        for docs in file_content:
            file.write(docs.text + "\n")