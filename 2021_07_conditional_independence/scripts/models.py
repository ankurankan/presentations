from pgmpy.models import BayesianModel
import matplotlib.pyplot as plt

example_dag = BayesianModel(
    [
        ("Pollution", "Cancer"),
        ("Smoker", "Cancer"),
        ("Cancer", "XRay"),
        ("Cancer", "Breathing"),
    ]
)
p = example_dag.to_daft(
    node_pos={
        "Pollution": (-1, 1),
        "Smoker": (1, 1),
        "Cancer": (0, 0),
        "XRay": (-1, -1),
        "Breathing": (1, -1),
    }
).render()
plt.savefig("../imgs/example_dag.png")
