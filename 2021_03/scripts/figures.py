import daft

# Figure 1
pgm = daft.PGM()

pgm.add_node("x", r"$X$", 0, 0, observed=True)
pgm.add_node("y", r"$Y$", 2, 0, observed=True)
pgm.add_node("u", r"$U$", 1, 1, observed=False)
pgm.add_node("w", r"$W$", 3, 1, observed=True)

pgm.add_edge("x", "y", plot_params={'ec': 'b'})
pgm.add_edge("u", "x")
pgm.add_edge("u", "y")
pgm.add_edge("u", "w")
pgm.render()

pgm.savefig("single_proxy.png", dpi=300)

# Figure 2
pgm = daft.PGM()

pgm.add_node("x", r"$X$", 1, 0, observed=True)
pgm.add_node("y", r"$Y$", 2, 0, observed=True)
pgm.add_node("u", r"$U$", 1, 1, observed=False)
pgm.add_node("w", r"$W$", 3, 1, observed=True)
pgm.add_node("z", r"$Z$", 0, 0, observed=True)

pgm.add_edge("x", "y", plot_params={'ec': 'b'})
pgm.add_edge("u", "x")
pgm.add_edge("u", "y")
pgm.add_edge("u", "w")
pgm.add_edge("u", "z")
pgm.render()

pgm.savefig("double_proxy.png", dpi=300)

# Figure 3
pgm = daft.PGM()

pgm.add_node("x", r"$X$", 1, 0, observed=True)
pgm.add_node("y", r"$Y$", 2, 0, observed=True)
pgm.add_node("u", r"$U$", 1, 1, observed=False)
pgm.add_node("w", r"$W$", 3, 1, observed=True)
pgm.add_node("z", r"$Z$", 0, 0, observed=True)

pgm.add_edge("x", "y", plot_params={'ec': 'b'})
pgm.add_edge("u", "x")
pgm.add_edge("u", "y")
pgm.add_edge("u", "w")
pgm.add_edge("u", "z")
pgm.add_edge("z", "x")
pgm.render()

pgm.savefig("double_proxy_with_extra_edge.png", dpi=300)

# Figure 4
pgm = daft.PGM()

pgm.add_node("x", r"$X$", 0, 0, observed=True)
pgm.add_node("y", r"$Y$", 2, 0, observed=True)
pgm.add_node("u", r"$U$", 1, 1, observed=False)
pgm.add_node("w", r"$W$", 3, 1, observed=True)

pgm.add_edge("x", "y", plot_params={'ec': 'b'})
pgm.add_edge("u", "x")
pgm.add_edge("u", "y")
pgm.add_edge("u", "w", label=r"$\alpha_{wu}$")
pgm.render()

pgm.savefig("sem.png", dpi=300)

# Figure 5
pgm = daft.PGM()

pgm.add_node("z1", r"$Z_1$", 1, 0, observed=True)
pgm.add_node("x", r"$X$", 2, 0, observed=True)
pgm.add_node("y", r"$Y$", 3, 0, observed=True)
pgm.add_node("z2", r"$Z_2$", 0.5, 1, observed=True)
pgm.add_node("u1", r"$U_1$", 1.5, 1, observed=False)
pgm.add_node("u2", r"$U_2$", 2.5, 1, observed=False)
pgm.add_node("w", r"$W$", 3.5, 1, observed=True)

pgm.add_edge("x", "y", plot_params={'ec': 'b'})
pgm.add_edge("z2", "z1")
pgm.add_edge("z1", "x")
pgm.add_edge("u1", "z1")
pgm.add_edge("u1", "z2")
pgm.add_edge("u1", "x")
pgm.add_edge("u1", "y")
pgm.add_edge("u1", "u2", directed=False)
pgm.add_edge("u2", "y")
pgm.add_edge("u2", "w")
pgm.add_edge("u2", "x")
pgm.add_edge("w", "y")
pgm.add_edge("w", "y")
pgm.render()

pgm.savefig("instrumental_var.png", dpi=300)

