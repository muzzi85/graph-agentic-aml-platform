import json
import pandas as pd


with open(
    "configs/aml_config.json",
    "r"
) as f:

    config = json.load(f)

node_features_df = pd.read_csv(
    "data/node_features.csv"
)

node_features_df["aml_score"] = (

    node_features_df["degree_centrality"]
    * config["degree_weight"]

    +

    node_features_df["betweenness_centrality"]
    * config["betweenness_weight"]

    +

    node_features_df["pagerank"]
    * config["pagerank_weight"]

    +

    node_features_df["clustering_coefficient"]
    * config["clustering_weight"]
)

alerts = []

for _, row in node_features_df.iterrows():

    if row["aml_score"] > config["threshold"]:

        reasons = []

        if row["degree_centrality"] > 0.002:
            reasons.append(
                "High transaction connectivity"
            )

        if row["betweenness_centrality"] > 0.001:
            reasons.append(
                "Elevated intermediary routing behavior"
            )

        if row["pagerank"] > 0.001:
            reasons.append(
                "High graph influence score"
            )

        alert = {

            "account_id":
                int(row["ACCOUNT_ID"]),

            "aml_score":
                float(row["aml_score"]),

            "risk_level":
                "HIGH",

            "reasons":
                reasons
        }

        alerts.append(alert)

# SAVE ALERTS
with open(
    "data/generated_alerts.json",
    "w"
) as f:

    json.dump(
        alerts,
        f,
        indent=4
    )