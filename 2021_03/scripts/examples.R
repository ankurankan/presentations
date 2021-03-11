library(MIIVsem)
library(dagitty)

# Example 1a
m_a <- "
u =~ w + x + y
y ~ u + x
"

# Example 1b
m_b <- "
u =~ w + z + x + y
y ~ u + x
"

# Example 1c
m_c <- "
u =~ w + z + x + y
x ~ u + z
y ~ u + x
"

# Example 1d
m_d <- "
u =~ w + z + x + y
x ~ u + z
y ~ u + x + w
"

models <- list(m_a, m_b, m_c, m_d)

for (i in 1:4){
    print(miivs(models[[i]]))
    # d <- simulateSEM(lavaanToGraph(models[[i]]), b.default=0.4, N=1e5)
    # print(miive(models[[i]], d))
}
