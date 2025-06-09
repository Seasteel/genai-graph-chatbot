from langchain.chat_models import ChatOpenAI
from langchain.graphs import Neo4jGraph
from dotenv import load_dotenv
import os

load_dotenv()

graph = Neo4jGraph(
    url="bolt://localhost:7687",
    username="neo4j",
    password="test123"
)

llm = ChatOpenAI(model="gpt-4", temperature=0, openai_api_key=os.getenv("OPENAI_API_KEY"))

def ask_graph(question):
    context = graph.query("MATCH (n) RETURN n LIMIT 5")
    prompt = f"{question}\n\nContext: {context}"
    response = llm.predict(prompt)
    return response
