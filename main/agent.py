import os

from dotenv import find_dotenv, load_dotenv
_ = load_dotenv(find_dotenv())

from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType
from langchain.utilities import SQLDatabase
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_toolkits import create_retriever_tool
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.schema import Document

db = SQLDatabase.from_uri(                              # 初始化数据库
    "sqlite:///datasource/localdb.db",
#    include_tables=['albums', 'artists'],       
    sample_rows_in_table_info=5)

# db = SQLDatabase.from_databricks(
#     host="adb-7365545121955305.5.azuredatabricks.net",
#     api_token="dapi8a4dca8f9b2c4c71137b97fbe0092554-3",
#     warehouse_id="01de5ba4dfbb71da",
#     catalog="samples",
#     schema="nyctaxi"
# )

llm = ChatOpenAI(model_name='gpt-4',temperature=0)      # 初始化大模型
toolkit = SQLDatabaseToolkit(db=db, llm=llm)            # 初始化工具箱
embeddings = OpenAIEmbeddings()                         # 初始化embedding

few_shots = {
    'List all artists.': 'SELECT * FROM artists;',
    "Find all albums for the artist 'AC/DC'.": "SELECT * FROM albums WHERE ArtistId = (SELECT ArtistId FROM artists WHERE Name = 'AC/DC');",
    "List all tracks in the 'Rock' genre.": "SELECT * FROM tracks WHERE GenreId = (SELECT GenreId FROM genres WHERE Name = 'Rock');",
    'Find the total duration of all tracks.': 'SELECT SUM(Milliseconds) FROM tracks;',
    'List all customers from Canada.': "SELECT * FROM customers WHERE Country = 'Canada';",
    'How many tracks are there in the album with ID 5?': 'SELECT COUNT(*) FROM tracks WHERE AlbumId = 5;',
    'Find the total number of invoices.': 'SELECT COUNT(*) FROM invoices;',
    'List all tracks that are longer than 5 minutes.': 'SELECT * FROM tracks WHERE Milliseconds > 300000;',
    'Who are the top 5 customers by total purchase?': 'SELECT CustomerId, SUM(Total) AS TotalPurchase FROM invoices GROUP BY CustomerId ORDER BY TotalPurchase DESC LIMIT 5;',
    'Which albums are from the year 2000?': "SELECT * FROM albums WHERE strftime('%Y', ReleaseDate) = '2000';",
    'How many employees are there': 'SELECT COUNT(*) FROM "employee"'
}
few_shot_docs = [Document(page_content=question, metadata={'sql_query': few_shots[question]}) for question in few_shots.keys()]
vector_db = FAISS.from_documents(few_shot_docs, embeddings)
retriever = vector_db.as_retriever()

tool_description = """
    This tool will help you understand similar examples to adapt them to the user question.
    Input to this tool should be the user question.
"""
retriever_tool = create_retriever_tool(
    retriever,
    name='sql_get_similar_examples',
    description=tool_description
)
custom_tool_list = [retriever_tool]

custom_suffix = """
    I should first get the similar examples I know.
    If the examples are enough to construct the query, I can build it.
    Otherwise, I can then look at the tables in the database to see what I can query.
    Then I should query the schema of the most relevant tables
""" 

agent = create_sql_agent(llm=llm,
                         toolkit=toolkit,
                         verbose=True,
                         agent_type=AgentType.OPENAI_FUNCTIONS,
                         extra_tools=custom_tool_list,
                         suffix=custom_suffix
                        )

def get_result_from_query(query):
    return agent.run(query)