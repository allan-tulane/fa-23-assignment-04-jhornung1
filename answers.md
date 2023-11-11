# CMPS 2200 Assignment 4
## Answers

**Name:** Jacob Hornung


Place all written answers from `assignment-04.md` here for easier grading.

**1a)** Start with the highest denomination available, $2^k$, such that $2^k$ is less than or equal to $N$. While $N$ is not zero, do the following:
  * Find the largest $2^i$ such that $2^i$ is less than or equal to $N$.
  * Subtract $2^i$ from $N$.
  * Repeat this process until $N$ becomes zero.

**1b)** The algorithm's locally optimal choices guarantee a globally optimal solution as each stage is completely optimal. If the algorithm deviates from selecting the largest denomination, the change produced can be improved, leading to a contradiction. Combining the locally optimal choices yields an optimal solution for the original problem, proving the optimal substructure.

**1c)** The work is $\mathcal{O}(\log N)$ and the span is also $\mathcal{O}(\log N)$.

**2a)** If you have coins that are $D_0 = 3$, $D_1 = 5$, and $D_2 = 7$ and want to make change for $N = 15$, our method gives us $D_2, D_1, D_0$, which in coins is $7, 5, 3$. However, the most optimal solution would be $D_1, D_2$ with coins of $5, 7$.

**2b)** If the first coin chosen in the optimal solution for $N$ is of denomination $D_i$, the remainder $N - D_i$ can be solved optimally, and by appending the coin of denomination $D_i$, an optimal solution for $N$ is achieved. This demonstrates that the optimality of the original solution relies on the optimality of its subproblems, validating the optimal substructure property.

**2c)** Create an array minCoins of size $N + 1$. Initialize minCoins[0] to $0$. For each amount $i$ from $1$ to $N$, iterate through each denomination $D_j$ and update minCoins[i] as follows: if $i - D_j \geq 0$, update minCoins[i] with the minimum of the current value and minCoins[i - D_j] + 1. The final result is in minCoins[N]. The work and span are the same, and are both $\mathcal{O}(N^2)$.

