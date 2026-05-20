from pathlib import Path

import networkx as nx
import pandas as pd


# --------------------------------------------------
# PROJECT ROOT
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

transactions_df = pd.read_csv(
    PROJECT_ROOT / "data" / "transactions.csv"
)

node_features_df = pd.read_csv(
    PROJECT_ROOT / "data" / "node_features.csv"
)


# --------------------------------------------------
# BUILD GRAPH
# --------------------------------------------------

G = nx.from_pandas_edgelist(

    transactions_df,

    source="SENDER_ACCOUNT_ID",

    target="RECEIVER_ACCOUNT_ID",

    edge_attr=True,

    create_using=nx.DiGraph()
)


# --------------------------------------------------
# GET NEIGHBORS
# --------------------------------------------------

def get_neighbors(
    account_id,
    hops=2
):

    neighbors = set([account_id])

    current_layer = set([account_id])

    for _ in range(hops):

        next_layer = set()

        for node in current_layer:

            try:

                node_neighbors = set(
                    G.neighbors(node)
                )

                next_layer.update(
                    node_neighbors
                )

            except:

                pass

        neighbors.update(next_layer)

        current_layer = next_layer

    return list(neighbors)


# --------------------------------------------------
# SUSPICIOUS NEIGHBORS
# --------------------------------------------------

def get_suspicious_neighbors(
    account_id,
    hops=2
):

    neighborhood = get_neighbors(
        account_id,
        hops
    )

    suspicious = node_features_df[

        (node_features_df["ACCOUNT_ID"]
            .isin(neighborhood))

        &

        (node_features_df["final_aml_alert"] == True)
    ]

    return suspicious


# --------------------------------------------------
# GRAPH METRICS
# --------------------------------------------------

def get_graph_metrics(account_id):

    result = node_features_df[

        node_features_df["ACCOUNT_ID"]
        == account_id
    ]

    return result.to_dict(
        orient="records"
    )


# --------------------------------------------------
# CYCLE RETRIEVAL
# --------------------------------------------------
def get_account_cycles(
    account_id,
    hops=2,
    max_cycle_length=6
):

    neighborhood = get_neighbors(
        account_id,
        hops
    )

    local_subgraph = G.subgraph(
        neighborhood
    )

    cycles = list(
        nx.simple_cycles(local_subgraph)
    )

    relevant_cycles = []

    for cycle in cycles:

        if (
            account_id in cycle
            and
            len(cycle) <= max_cycle_length
        ):

            relevant_cycles.append(cycle)

    return relevant_cycles
# --------------------------------------------------
# INVESTIGATION CONTEXT
# --------------------------------------------------

def build_investigation_context(
    account_id
):

    context = {

        "account_id":
            account_id,

        "graph_metrics":
            get_graph_metrics(
                account_id
            ),

        "neighbors":
            get_neighbors(
                account_id
            ),

        "suspicious_neighbors":
            get_suspicious_neighbors(
                account_id
            ).to_dict(
                orient="records"
            ),

        "cycles":
            get_account_cycles(
                account_id
            )
    }

    return context


# --------------------------------------------------
# TEST
# --------------------------------------------------

if __name__ == "__main__":

    context = build_investigation_context(
        6192
    )

    print(context)