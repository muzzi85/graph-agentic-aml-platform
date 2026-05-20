from deepeval.metrics import HallucinationMetric
from deepeval.test_case import LLMTestCase
from deepeval.models import OllamaModel
from deepeval.metrics import (

    HallucinationMetric,

    FaithfulnessMetric,

    AnswerRelevancyMetric,

    ContextualPrecisionMetric,

    ContextualRecallMetric
)

retrieval_context = [

    """
    Account ID: 6192

    Final AML Score: 0.9 # scale 0-1, 1 is highly suspicious

    Suspicious Neighbor Count: 540 # above 100 is suspicious

    Detected Cycles: 20 # above 10 is suspicious

    Degree Centrality: 0.8 # scale 0-1, 1 is highly suspicious

    Betweenness Centrality: 0.8 # scale 0-1, 1 is highly suspicious
    """
]

generated_output = """

Account appears suspicious due to
high suspicious neighbor exposure
and abnormal graph topology.

Recommended action:
Escalate to AML compliance team.

"""

expected_output = """

Account appears suspicious due to:

- high suspicious neighbor exposure
- abnormal graph topology
- elevated AML risk metrics

Recommended action:
Escalate to AML compliance team.

"""

test_case = LLMTestCase(

    input="Analyze AML risk",

    actual_output=generated_output,

    expected_output=expected_output,

    context=retrieval_context,

    retrieval_context=retrieval_context
)
# metric = HallucinationMetric(
#     threshold=0.5
# )

ollama_model = OllamaModel(
    model="tinyllama"
)

hallucination_metric = HallucinationMetric(

    threshold=0.5,

    model=ollama_model
)

faithfulness_metric = FaithfulnessMetric(

    threshold=0.5,

    model=ollama_model
)

answer_relevancy_metric = AnswerRelevancyMetric(

    threshold=0.5,

    model=ollama_model
)

contextual_precision_metric = ContextualPrecisionMetric(

    threshold=0.5,

    model=ollama_model
)

contextual_recall_metric = ContextualRecallMetric(

    threshold=0.5,

    model=ollama_model
)


metrics = [

    hallucination_metric,

    faithfulness_metric,

    answer_relevancy_metric,

    contextual_precision_metric,

    contextual_recall_metric
]

for metric in metrics:

    metric.measure(test_case)

    print("\n====================")

    print(type(metric).__name__)

    print("Score:")

    print(metric.score)

    print("\nReason:")

    print(metric.reason)

