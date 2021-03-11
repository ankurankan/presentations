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

m_2 <- "
u1 =~ z2 + z1 + x + y
u2 =~ w + x + y
z1 ~ u1 + z2
x ~ u1 + u2 + z1
y ~ u1 + u2 + x + w
u1 ~~ u2
"

m_3 <- "
u1 =~ z1 + z2 + x + y
u2 =~ w1 + w2 + x + y
z2 ~ u1 + w2
x ~ u1 + u2 + z1
y ~ u1 + u2 + x
u1 ~~ u2
"

models <- list(m_a, m_b, m_c, m_d, m_2, m_3)

for (i in 1:length(models)){
    print(miivs(models[[i]]))
    # d <- simulateSEM(lavaanToGraph(models[[i]]), b.default=0.4, N=1e5)
    # print(miive(models[[i]], d))
}
