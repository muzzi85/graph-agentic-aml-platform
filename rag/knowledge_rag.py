from pathlib import Path

knowledge_path = Path(
    "knowledge_base"
)

documents = []

for file in knowledge_path.glob("*.md"):

    with open(file, "r") as f:

        text = f.read()

        documents.append({

            "filename": file.name,

            "content": text
        })

import chromadb

client = chromadb.Client()

collection = client.create_collection(
    name="aml_knowledge"
)

for i, doc in enumerate(documents):

    collection.add(

        documents=[doc["content"]],

        metadatas=[{

            "source": doc["filename"]
        }],

        ids=[str(i)]
    )



def retrieve_knowledge(
    query,
    n_results=2
):

    results = collection.query(

        query_texts=[query],

        n_results=n_results
    )

    documents = results["documents"][0]

    metadata = results["metadatas"][0]

    distances = results["distances"][0]

    MAX_DISTANCE = 1.5

    formatted_knowledge = "\n\n"

    formatted_knowledge += (
        "RETRIEVED AML KNOWLEDGE\n"
    )

    formatted_knowledge += (
        "========================\n\n"
    )

    found_results = False

    for i in range(len(documents)):

        if distances[i] > MAX_DISTANCE:

            continue

        found_results = True

        formatted_knowledge += (

            f"DOCUMENT {i+1}\n\n"

            f"Source: "
            f"{metadata[i]['source']}\n"

            f"Similarity Distance: "
            f"{distances[i]:.4f}\n\n"

            f"CONTENT:\n\n"

            f"{documents[i]}\n\n"

            f"--------------------------------\n\n"
        )

    if not found_results:

        return (
            "No sufficiently relevant "
            "AML knowledge found."
        )

    return formatted_knowledge

# knowledge = retrieve_knowledge(

#     "- AML Score: 0.92 - Suspicious Neighbors: 540 - Detected Cycles: 20 - Degree Centrality: 0.81 - Betweenness Centrality: 0.79" #Explain AML graph topology risk
# )

# print(knowledge)

