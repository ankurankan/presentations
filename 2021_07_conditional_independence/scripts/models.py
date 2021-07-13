import daft
import matplotlib.pyplot as plt

# example_dag = BayesianModel(
#     [
#         ("Pollution", "Cancer"),
#         ("Smoker", "Cancer"),
#         ("Cancer", "XRay"),
#         ("Cancer", "Breathing"),
#     ]
# )

pgm = daft.PGM(aspect=1)
pgm.add_node("pollution", r"Pollution", 0.5, 1.5)
pgm.add_node("smoker", r"Smoker", 1.5, 1.5)
pgm.add_node("cancer", r"Cancer", 1, 1)
pgm.add_node("xray", r"XRay", 0.5, 0.5)
pgm.add_node("breathing", r"Breathing", 1.5, 0.5)

pgm.add_edge('pollution', 'cancer')
pgm.add_edge('smoker', 'cancer')
pgm.add_edge('cancer', 'xray')
pgm.add_edge('cancer', 'breathing')

pgm.savefig("../imgs/example_dag.png")
