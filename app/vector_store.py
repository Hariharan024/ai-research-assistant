import chromadb


class VectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="./data/chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="documents"
        )


    def add_documents(self, chunks, source):

        documents = []
        metadatas = []
        ids = []

        for i, chunk in enumerate(chunks):

            documents.append(chunk["text"])

            metadatas.append({
                "source": source,
                "page": chunk["page"]
            })

            ids.append(f"{source}_{i}")


        self.collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )


    def search(self, question, top_k=3, source=None):

        if source:

            results = self.collection.query(
                query_texts=[question],
                n_results=top_k,
                where={
                    "source": source
                }
            )

        else:

            results = self.collection.query(
                query_texts=[question],
                n_results=top_k
            )

        return results