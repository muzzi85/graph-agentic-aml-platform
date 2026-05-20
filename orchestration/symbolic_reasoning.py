

def compute_symbolic_risk(

    graph_metrics,
    suspicious_neighbors,
    cycles
):

    symbolic_findings = []

    # ----------------------------------
    # AML SCORE
    # ----------------------------------

    aml_score = graph_metrics[
        "final_aml_score"
    ]

    if aml_score > 0.7:

        symbolic_findings.append(

            "HIGH AML RISK SCORE"
        )

    elif aml_score > 0.3:

        symbolic_findings.append(

            "MEDIUM AML RISK SCORE"
        )

    else:

        symbolic_findings.append(

            "LOW AML RISK SCORE"
        )

    # ----------------------------------
    # CONNECTIVITY RISK
    # ----------------------------------

    if suspicious_neighbors > 50:

        symbolic_findings.append(

            "HIGH suspicious connectivity"
        )

    elif suspicious_neighbors > 10:

        symbolic_findings.append(

            "MODERATE suspicious connectivity"
        )

    else:

        symbolic_findings.append(

            "LOW suspicious connectivity"
        )

    # ----------------------------------
    # CYCLE RISK
    # ----------------------------------

    if cycles > 10:

        symbolic_findings.append(

            "Possible laundering cycles detected"
        )

    elif cycles > 0:

        symbolic_findings.append(

            "Limited laundering cycle exposure"
        )

    else:

        symbolic_findings.append(

            "No laundering cycles detected"
        )

    # ----------------------------------
    # CENTRALITY RISK
    # ----------------------------------

    if (

        graph_metrics[
            "betweenness_centrality"
        ] > 0.5

    ):

        symbolic_findings.append(

            "High intermediary routing behavior"
        )

    return symbolic_findings

