import pandas as pd
from models.embedding_model import get_embedding_model
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS

df = pd.read_excel(r"C:\Users\CHARANSAI\OneDrive\Desktop\Techpanda\agents\laptop_issues_dataset.xlsx")


embed_model = get_embedding_model()

df['description_embeddings'] = embed_model.embed_documents(df['Description of the Problem'].tolist())

documents = [
    Document(
        page_content=row["Description of the Problem"],
        metadata={
            "root_cause": row["Problems That Occur"],
            "resolution_notes": row["Resolution"]
        }
    )
    for _, row in df.iterrows()
]


vectorstore = FAISS.from_documents(documents, embed_model)

# Save the vector store
vectorstore.save_local("root_cause_analysis")

new_vectorstore = FAISS.load_local(
       "root_cause_analysis", embed_model, allow_dangerous_deserialization=True
   )