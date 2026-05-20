import chromadb

client = chromadb.Client()

memory_collection = client.create_collection(
    name="aml_memory"
)
historical_cases = [

    {

        "summary": """

        Previous investigations involving
        elevated suspicious connectivity
        and abnormal intermediary routing
        behavior required AML escalation.

        Layering transaction patterns and
        coordinated graph exposure were
        considered high-risk indicators.

        """
    },

    {

        "summary": """

        Previous investigations with
        moderate suspicious connectivity
        and partially elevated graph
        exposure required enhanced
        monitoring and analyst review.

        """
    },

    {

        "summary": """

        Previous investigations with
        stable transaction flow and
        low connectivity exposure were
        classified as low-risk behavior.

        No escalation was required.

        """
    }
]

for i, case in enumerate(historical_cases):

    memory_collection.add(

        documents=[case["summary"]],

        # metadatas=[{}],
        ids=[str(i)]
    )

def retrieve_similar_cases(

    query,
    n_results=2
):

    results = memory_collection.query(

        query_texts=[query],

        n_results=n_results
    )

    documents = results["documents"][0]

    # metadata = results["metadatas"][0]

    distances = results["distances"][0]

    formatted_memory = "\n\n"

    formatted_memory += (
        "SIMILAR AML INVESTIGATIONS\n"
    )

    formatted_memory += (
        "============================\n\n"
    )

    for i in range(len(documents)):

        formatted_memory += (

            # f"CASE: "
            # f"{metadata[i]['case_id']}\n\n"

            f"Similarity Distance: "
            f"{distances[i]:.4f}\n\n"

            f"{documents[i]}\n\n"

            f"--------------------------------\n\n"
        )

    return formatted_memory

# memory_results = retrieve_similar_cases(

#     """

#     High suspicious neighbors.

#     High betweenness centrality.

#     Abnormal graph topology.

#     """
# )

# print(memory_results)