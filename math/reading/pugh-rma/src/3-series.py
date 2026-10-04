"""Section 3.3, Series: the editable source of 3-series.json."""
from __future__ import annotations

from c3_common import card, definition, example, gate, prose, remark, stated, write

B: list[dict] = []

B.append(prose("c3-series-intro", r"""
A series is a formal sum of infinitely many real numbers. It is given a value by taking the limit of its finite partial sums, so the theory of series is the theory of sequences in other clothing; but the questions are different. One rarely can compute the sum, and asks instead whether the series converges at all. The tests of this section answer that by comparison with series that are understood, above all the geometric series.
"""))

B.append(definition("c3-def-series", "Series, partial sums, convergence", r"""
Let $(a_k)_{k \ge 1}$ be a sequence of real numbers. The \emph{series} $\sum a_k = \sum_{k=1}^\infty a_k$ has \emph{$n$-th partial sum}
\[ A_n = a_1 + a_2 + \dots + a_n . \]
The series \emph{converges} to $A \in \R$ if $A_n \to A$ as $n \to \infty$; we then write $\sum_{k=1}^\infty a_k = A$ and call $A$ the \emph{sum}. A series that does not converge \emph{diverges}. The same definitions apply to series whose index starts at $0$ or at any other integer. For $n \ge 1$ the series $\sum_{k=n+1}^\infty a_k$ is a \emph{tail} of $\sum a_k$.
"""))

B.append(gate("theorem", "c3-thm-series-cauchy", "Cauchy convergence criterion for series", r"""
A series $\sum a_k$ converges if and only if for every $\eps > 0$ there is an $N$ such that
\[ m \ge n \ge N \quad\Longrightarrow\quad \abs{\sum_{k=n}^{m} a_k} < \eps . \]
""", r"""
Since $\R$ is complete, the sequence $(A_n)$ of partial sums converges if and only if it is a Cauchy sequence. For $m \ge n \ge 2$,
\[ \sum_{k=n}^{m} a_k = A_m - A_{n-1} . \]
Suppose $(A_n)$ is Cauchy and let $\eps > 0$. There is an $N_0$ with $\abs{A_p - A_q} < \eps$ for all $p,q \ge N_0$. Put $N = N_0 + 1$. If $m \ge n \ge N$, then $m, n-1 \ge N_0$, so $\abs{\sum_{k=n}^m a_k} = \abs{A_m - A_{n-1}} < \eps$.

Conversely suppose the condition holds; given $\eps > 0$ let $N$ be as in the condition. If $p > q \ge N$, then with $n = q + 1$ and $m = p$ we have $m \ge n \ge N$, so $\abs{A_p - A_q} = \abs{\sum_{k=q+1}^{p} a_k} < \eps$; and $\abs{A_p - A_q} = 0$ if $p = q$. So $(A_n)$ is Cauchy.
""", 2, 15, [
    r"Express $\sum_{k=n}^m a_k$ through partial sums and use the completeness of $\R$.",
], ["c3-def-series"]))

B.append(gate("corollary", "c3-cor-terms-to-zero", "Terms of a convergent series tend to zero; tails", r"""
\begin{enumerate}
\item If $\sum a_k$ converges, then $a_k \to 0$ as $k \to \infty$.
\item For each $n \ge 1$, the series $\sum_{k=1}^\infty a_k$ converges if and only if its tail $\sum_{k=n+1}^\infty a_k$ converges, and then $\sum_{k=1}^\infty a_k = A_n + \sum_{k=n+1}^\infty a_k$.
\item If $\sum a_k$ and $\sum b_k$ converge and $c \in \R$, then $\sum (a_k + c\,b_k)$ converges, to $\sum a_k + c \sum b_k$.
\end{enumerate}
""", r"""
(1) Take $m = n$ in the Cauchy convergence criterion: for every $\eps > 0$ there is an $N$ with $\abs{a_n} < \eps$ for all $n \ge N$.

(2) For $m > n$ the $(m-n)$-th partial sum of the tail is $a_{n+1} + \dots + a_m = A_m - A_n$. With $n$ fixed, $A_m - A_n$ converges as $m \to \infty$ if and only if $A_m$ does, and the limits differ by $A_n$.

(3) The partial sums of $\sum (a_k + c\,b_k)$ are $A_n + c\,B_n$, where $A_n, B_n$ are the partial sums of the two series; by the limit laws for sequences they converge to $\sum a_k + c \sum b_k$.
""", 1, 10, [
    r"For (1), take $m = n$ in the Cauchy criterion. For (2) and (3), write down the partial sums.",
], ["c3-thm-series-cauchy", "c3-def-series"]))

B.append(gate("exercise", "c3-ex-harmonic", "The harmonic series diverges", r"""
The series $\sum_{k=1}^\infty \dfrac{1}{k}$ diverges, although its terms tend to $0$.
""", r"""
For every $n \ge 1$,
\[ \sum_{k=n+1}^{2n} \frac{1}{k} \ \ge\ n \cdot \frac{1}{2n} = \frac12 , \]
since each of the $n$ terms is at least $1/(2n)$. If the series converged, the Cauchy convergence criterion with $\eps = 1/2$ would give an $N$ with $\abs{\sum_{k=n+1}^{2n} 1/k} < 1/2$ for all $n \ge N$ (here $2n \ge n+1 \ge N$), a contradiction. So the series diverges.
""", 2, 15, [
    r"Show the Cauchy criterion fails: find blocks of consecutive terms, arbitrarily far out, whose sum is at least $1/2$.",
], ["c3-thm-series-cauchy"]))

B.append(gate("theorem", "c3-thm-geometric-series", "Geometric series", r"""
Let $\lambda \in \R$. If $\abs{\lambda} < 1$, then $\sum_{k=0}^\infty \lambda^k$ converges and
\[ \sum_{k=0}^\infty \lambda^k = \frac{1}{1 - \lambda} . \]
If $\abs{\lambda} \ge 1$, the series diverges.
""", r"""
Let $S_n = 1 + \lambda + \dots + \lambda^n$. Then $(1 - \lambda)S_n = 1 - \lambda^{n+1}$, because the product telescopes. So for $\lambda \neq 1$,
\[ S_n = \frac{1 - \lambda^{n+1}}{1 - \lambda} . \]
Let $\abs{\lambda} < 1$. We claim $\lambda^n \to 0$. The sequence $c_n = \abs{\lambda}^n$ satisfies $0 \le c_{n+1} = \abs{\lambda}c_n \le c_n$, so it is nonincreasing and bounded below, hence converges to some $c \ge 0$. Letting $n \to \infty$ in $c_{n+1} = \abs{\lambda}c_n$ gives $c = \abs{\lambda}c$, so $(1 - \abs{\lambda})c = 0$ and $c = 0$. Thus $\abs{\lambda^{n}} \to 0$, and $S_n \to 1/(1-\lambda)$.

Let $\abs{\lambda} \ge 1$. Then $\abs{\lambda^k} \ge 1$ for all $k$, so the terms do not tend to $0$, and the series diverges because the terms of a convergent series tend to zero.
""", 2, 15, [
    r"Multiply the partial sum by $1 - \lambda$.",
    r"You need $\lambda^n \to 0$ for $\abs{\lambda} < 1$: the sequence $\abs{\lambda}^n$ is monotone and bounded, and its limit $c$ satisfies $c = \abs{\lambda}c$.",
], ["c3-def-series", "c3-cor-terms-to-zero"]))

B.append(gate("lemma", "c3-lem-nonnegative-series", "Series with nonnegative terms", r"""
Let $a_k \ge 0$ for all $k$. Then $\sum a_k$ converges if and only if its sequence of partial sums is bounded above, and in that case the sum is the supremum of the partial sums.
""", r"""
Since $A_{n+1} - A_n = a_{n+1} \ge 0$, the sequence $(A_n)$ is nondecreasing. A nondecreasing sequence that is bounded above converges to its supremum (by the least upper bound property). Conversely a convergent sequence is bounded.
""", 1, 10, [
    r"The partial sums form a monotone sequence.",
], ["c3-def-series"]))

B.append(gate("theorem", "c3-thm-comparison-test", "Comparison test", r"""
Let $\sum a_k$ and $\sum b_k$ be series and suppose there is a $K$ such that $\abs{a_k} \le b_k$ for all $k \ge K$. If $\sum b_k$ converges, then $\sum a_k$ converges. Equivalently: if $\sum a_k$ diverges, then $\sum b_k$ diverges.
""", r"""
Let $\eps > 0$. By the Cauchy convergence criterion for $\sum b_k$ there is an $N$ with $\abs{\sum_{k=n}^m b_k} < \eps$ whenever $m \ge n \ge N$. Let $N' = \max\set{N,K}$. For $m \ge n \ge N'$, the triangle inequality and $\abs{a_k} \le b_k$ for $k \ge K$ give
\[ \abs{\sum_{k=n}^{m} a_k} \le \sum_{k=n}^{m} \abs{a_k} \le \sum_{k=n}^{m} b_k < \eps . \]
So $\sum a_k$ satisfies the Cauchy convergence criterion and converges. The second formulation is the contrapositive.
""", 2, 15, [
    r"Verify the Cauchy criterion for $\sum a_k$ using the one for $\sum b_k$.",
], ["c3-thm-series-cauchy"]))

B.append(definition("c3-def-absolute-convergence", "Absolute and conditional convergence", r"""
A series $\sum a_k$ \emph{converges absolutely} if $\sum \abs{a_k}$ converges. It \emph{converges conditionally} if it converges but does not converge absolutely.
"""))

B.append(gate("corollary", "c3-cor-absolute-implies-convergent", "Absolute convergence implies convergence", r"""
If $\sum a_k$ converges absolutely, then it converges, and
\[ \abs{\sum_{k=1}^\infty a_k} \le \sum_{k=1}^\infty \abs{a_k} . \]
""", r"""
Apply the comparison test with $b_k = \abs{a_k}$: since $\abs{a_k} \le b_k$ and $\sum b_k$ converges, $\sum a_k$ converges. For each $n$ the triangle inequality gives
\[ \abs{A_n} \le \sum_{k=1}^n \abs{a_k} \le \sum_{k=1}^\infty \abs{a_k}, \]
the last step because a series of nonnegative terms has sum equal to the supremum of its partial sums. Letting $n \to \infty$, $\abs{A_n} \to \abs{\sum_{k=1}^\infty a_k}$, and a limit of numbers that are at most $\sum \abs{a_k}$ is at most $\sum\abs{a_k}$.
""", 1, 10, [
    r"Compare $\sum a_k$ with $\sum \abs{a_k}$.",
], ["c3-thm-comparison-test", "c3-lem-nonnegative-series", "c3-def-absolute-convergence"]))

B.append(prose("c3-integral-test-intro", r"""
A series $\sum f(k)$ is a sum of areas of rectangles of width $1$, so it can be compared with an integral of $f$. The comparison is cleanest when $f$ is monotone; such an $f$ is integrable on each bounded interval.
"""))

B.append(gate("theorem", "c3-thm-integral-test", "Integral test", r"""
Let $f : [1,\infty) \to \R$ be nonnegative and nonincreasing. Then for every $n \ge 2$,
\[ \sum_{k=2}^{n} f(k) \ \le\ \int_1^n f(x)\,dx \ \le\ \sum_{k=1}^{n-1} f(k) . \]
Consequently $\sum_{k=1}^\infty f(k)$ converges if and only if the sequence $\int_1^n f$, $n \in \N$, is bounded.
""", r"""
$f$ is monotone on each interval $[1,n]$ and $[k,k+1]$, hence Riemann integrable there. For $x \in [k,k+1]$ we have $f(k+1) \le f(x) \le f(k)$, so by monotonicity of the integral over this interval of length $1$,
\[ f(k+1) \le \int_k^{k+1} f \le f(k) . \]
Summing over $k = 1, \dots, n-1$ and using additivity of the integral over intervals,
\[ \sum_{k=2}^{n} f(k) \le \int_1^n f \le \sum_{k=1}^{n-1} f(k) . \]

The terms $f(k)$ are nonnegative, so $\sum f(k)$ converges if and only if its partial sums are bounded above. If the integrals $\int_1^n f$ are bounded by $C$, the left inequality bounds every partial sum by $f(1) + C$, so the series converges. If the series converges with sum $S$, the right inequality gives $\int_1^n f \le S$ for all $n \ge 2$; the integrals are also $\ge 0$, so they are bounded.
""", 2, 20, [
    r"On $[k,k+1]$ the function $f$ lies between $f(k+1)$ and $f(k)$. Integrate.",
    r"Sum the inequalities $f(k+1) \le \int_k^{k+1} f \le f(k)$ and use the fact that a series of nonnegative terms converges iff its partial sums are bounded.",
], ["c3-thm-monotone-integrable", "c3-thm-integral-monotone", "c3-thm-integral-additive", "c3-lem-nonnegative-series"]))

B.append(remark("c3-rem-integral-test", r"""
Since $f \ge 0$, the function $b \mapsto \int_1^b f$ is nondecreasing, so the integrals $\int_1^n f$ are bounded exactly when the improper integral $\int_1^\infty f$ converges. Thus: $\sum f(k)$ converges if and only if $\int_1^\infty f$ converges. With the logarithm in hand, $\int_1^n dx/x = \log n$ is unbounded, which is another proof that the harmonic series diverges, and the test also shows that the partial sums of the harmonic series grow like $\log n$.
"""))

B.append(gate("exercise", "c3-ex-p-series", "The $p$-series", r"""
Let $p \in \R$. The series $\sum_{k=1}^\infty \dfrac{1}{k^p}$ converges if $p > 1$ and diverges if $p \le 1$. (Use the standard properties of real powers: the laws of exponents, and for $k \ge 1$, $k^p$ is nondecreasing in $k$ when $p \ge 0$, $k^p \le k$ when $p \le 1$, and $2^{s} < 1$ when $s < 0$.)
""", r"""
\emph{$p \le 1$.} Then $k^p \le k$, so $1/k^p \ge 1/k > 0$ for all $k \ge 1$. Since the harmonic series diverges, $\sum 1/k^p$ diverges by the comparison test.

\emph{$p > 1$.} The terms are positive, so it suffices to bound the partial sums. Group the terms in dyadic blocks: for $j \ge 0$ the block $2^j \le k < 2^{j+1}$ has $2^j$ terms, each at most $1/(2^j)^p$ because $k^p \ge (2^j)^p$. Hence
\[ \sum_{k=2^j}^{2^{j+1}-1} \frac{1}{k^p} \ \le\ 2^j \cdot 2^{-jp} = \lambda^j, \qquad \lambda = 2^{1-p} . \]
Since $1 - p < 0$ we have $0 < \lambda < 1$. Given $n$, choose $J$ with $n < 2^{J+1}$; then
\[ \sum_{k=1}^{n} \frac{1}{k^p} \ \le\ \sum_{j=0}^{J} \ \sum_{k=2^j}^{2^{j+1}-1} \frac{1}{k^p} \ \le\ \sum_{j=0}^{J} \lambda^j \ \le\ \frac{1}{1 - \lambda}, \]
the last step because the partial sums of the geometric series, which has positive terms, are at most its sum. The partial sums are bounded, so the series converges.
""", 3, 25, [
    r"For $p \le 1$ compare with the harmonic series.",
    r"For $p > 1$ group the terms into blocks $2^j \le k < 2^{j+1}$ and bound each block by a term of a geometric series.",
], ["c3-ex-harmonic", "c3-thm-comparison-test", "c3-thm-geometric-series", "c3-lem-nonnegative-series"]))

B.append(prose("c3-root-ratio-intro", r"""
The root and ratio tests compare a series with a geometric series, by measuring the exponential growth rate of its terms. They are stated with limits superior and inferior, which always exist.
"""))

B.append(definition("c3-def-limsup", "Limit superior and limit inferior", r"""
Let $(c_k)$ be a sequence of real numbers. If $(c_k)$ is bounded above, the numbers $s_n = \sup\set{c_k : k \ge n}$ form a nonincreasing sequence, and
\[ \limsup_{k \to \infty} c_k = \lim_{n \to \infty} s_n = \inf_n s_n \]
(which is $-\infty$ if the $s_n$ are unbounded below). If $(c_k)$ is not bounded above, $\limsup c_k = +\infty$. Similarly $\liminf_{k\to\infty} c_k = \lim_{n \to \infty} \inf\set{c_k : k \ge n}$, the limit of a nondecreasing sequence (possibly $+\infty$), with value $-\infty$ if $(c_k)$ is not bounded below. Both always exist in $[-\infty,\infty]$. Directly from the definition, for $r \in \R$:
\begin{enumerate}
\item if $\limsup c_k < r$, then there is an $N$ with $c_k < r$ for all $k \ge N$;
\item if $\limsup c_k > r$, then $c_k > r$ for infinitely many $k$;
\item if $\liminf c_k > r$, then there is an $N$ with $c_k > r$ for all $k \ge N$.
\end{enumerate}
(For (1), some $s_N < r$. For (2), either the sequence is unbounded above or every $s_n > r$; in both cases, for every $n$ some $k \ge n$ has $c_k > r$. For (3), some $\inf\set{c_k : k \ge N} > r$.)
"""))

B.append(gate("theorem", "c3-thm-root-test", "Root test", r"""
Let $\sum a_k$ be a series and $\alpha = \limsup_{k\to\infty} \abs{a_k}^{1/k} \in [0,\infty]$.
\begin{enumerate}
\item If $\alpha < 1$, the series converges absolutely.
\item If $\alpha > 1$, the series diverges.
\end{enumerate}
""", r"""
(1) Choose $r$ with $\alpha < r < 1$. By the definition of the limit superior there is an $N$ such that $\abs{a_k}^{1/k} < r$, that is $\abs{a_k} < r^k$, for all $k \ge N$. The geometric series $\sum r^k$ converges since $0 \le r < 1$. By the comparison test (applied to the series $\sum \abs{a_k}$) the series $\sum \abs{a_k}$ converges.

(2) Since $\alpha > 1$, there are infinitely many $k$ with $\abs{a_k}^{1/k} > 1$, hence with $\abs{a_k} > 1$. So $a_k$ does not tend to $0$, and the series diverges because the terms of a convergent series tend to zero.
""", 2, 20, [
    r"If $\alpha < r < 1$, what does the definition of $\limsup$ say about $\abs{a_k}$ for large $k$?",
    r"Compare with the geometric series $\sum r^k$. For $\alpha > 1$, show the terms do not tend to $0$.",
], ["c3-def-limsup", "c3-thm-comparison-test", "c3-thm-geometric-series", "c3-cor-terms-to-zero", "c3-def-absolute-convergence"]))

B.append(gate("theorem", "c3-thm-ratio-test", "Ratio test", r"""
Let $\sum a_k$ be a series with $a_k \neq 0$ for all $k$, and let
\[ \rho = \limsup_{k\to\infty} \abs{\frac{a_{k+1}}{a_k}}, \qquad \lambda = \liminf_{k\to\infty} \abs{\frac{a_{k+1}}{a_k}} . \]
\begin{enumerate}
\item If $\rho < 1$, the series converges absolutely.
\item If $\lambda > 1$, the series diverges.
\end{enumerate}
""", r"""
(1) Choose $r$ with $\rho < r < 1$. There is an $N$ with $\abs{a_{k+1}/a_k} < r$, i.e. $\abs{a_{k+1}} \le r\abs{a_k}$, for all $k \ge N$. By induction on $k$,
\[ \abs{a_k} \le \abs{a_N}\, r^{k-N} = C r^k \qquad (k \ge N), \quad\text{where } C = \abs{a_N}\, r^{-N} . \]
The series $\sum C r^k$ converges, being a constant multiple of a convergent geometric series. By the comparison test $\sum \abs{a_k}$ converges.

(2) Since $\lambda > 1$, there is an $N$ with $\abs{a_{k+1}/a_k} > 1$ for all $k \ge N$. Then $\abs{a_{k+1}} > \abs{a_k}$ for $k \ge N$, so by induction $\abs{a_k} \ge \abs{a_N} > 0$ for all $k \ge N$. Hence $a_k$ does not tend to $0$ and the series diverges.
""", 2, 20, [
    r"If $\abs{a_{k+1}} \le r\abs{a_k}$ from some point on, how fast do the terms decay?",
    r"Get $\abs{a_k} \le C r^k$ by induction and compare with a geometric series.",
], ["c3-def-limsup", "c3-thm-comparison-test", "c3-thm-geometric-series", "c3-cor-terms-to-zero", "c3-def-absolute-convergence"]))

B.append(remark("c3-rem-root-ratio", r"""
Both tests are inconclusive in the remaining cases. For $a_k = 1/k$ and for $a_k = 1/k^2$ the ratios $a_{k+1}/a_k$ and the roots $a_k^{1/k}$ tend to $1$ (using $k^{1/k} \to 1$), yet the first series diverges and the second converges. One can show that $\liminf \abs{a_{k+1}/a_k} \le \liminf \abs{a_k}^{1/k} \le \limsup \abs{a_k}^{1/k} \le \limsup\abs{a_{k+1}/a_k}$, so the root test succeeds whenever the ratio test does; the ratio test is often easier to apply. For example, for any $x \neq 0$ the series $\sum x^k/k!$ has ratios $\abs{x}/(k+1) \to 0$, so it converges absolutely for every real $x$.
"""))

B.append(prose("c3-alternating-intro", r"""
The tests so far detect absolute convergence. Series that converge only conditionally do so because of cancellation between terms of opposite sign. The simplest case is when the signs alternate.
"""))

B.append(gate("theorem", "c3-thm-alternating-series", "Alternating series test", r"""
Let $a_1 \ge a_2 \ge a_3 \ge \dots \ge 0$ with $a_k \to 0$. Then the alternating series
\[ \sum_{k=1}^\infty (-1)^{k+1} a_k = a_1 - a_2 + a_3 - a_4 + \cdots \]
converges. Moreover its sum $S$ and partial sums $S_n$ satisfy $\abs{S - S_n} \le a_{n+1}$ for every $n \ge 1$.
""", r"""
Since $(a_k)$ is nonincreasing, for every $n \ge 1$
\[ S_{2n+2} - S_{2n} = a_{2n+1} - a_{2n+2} \ge 0, \qquad S_{2n+1} - S_{2n-1} = -a_{2n} + a_{2n+1} \le 0, \qquad S_{2n+1} - S_{2n} = a_{2n+1} \ge 0 . \]
Thus the even partial sums $(S_{2n})$ are nondecreasing, the odd partial sums $(S_{2n-1})$ are nonincreasing, and
\[ S_2 \le S_{2n} \le S_{2n+1} \le S_1 \qquad \text{for all } n . \]
So $(S_{2n})$ is nondecreasing and bounded above by $S_1$; it converges to some $S$. Then $S_{2n+1} = S_{2n} + a_{2n+1} \to S + 0 = S$. Given $\eps > 0$, there are $N_1, N_2$ with $\abs{S_{2n} - S} < \eps$ for $n \ge N_1$ and $\abs{S_{2n+1} - S} < \eps$ for $n \ge N_2$; every $m \ge \max\set{2N_1, 2N_2 + 1}$ is of one of these two forms, so $\abs{S_m - S} < \eps$. Hence $S_m \to S$ and the series converges.

For the estimate: $S$ is the supremum of the nondecreasing sequence $(S_{2n})$ and the infimum of the nonincreasing sequence $(S_{2n-1})$, so
\[ S_{2n} \le S \le S_{2n+1} \qquad\text{and}\qquad S_{2n} \le S \le S_{2n-1} \qquad\text{for all } n \ge 1 . \]
If $m = 2n$ is even, $0 \le S - S_m \le S_{2n+1} - S_{2n} = a_{m+1}$. If $m = 2n - 1$ is odd, $0 \le S_m - S \le S_{2n-1} - S_{2n} = a_{2n} = a_{m+1}$. In both cases $\abs{S - S_m} \le a_{m+1}$.
""", 3, 30, [
    r"Look separately at the partial sums of even index and of odd index. Which way does each subsequence move?",
    r"$S_{2n}$ increases, $S_{2n+1}$ decreases, and $S_{2n} \le S_{2n+1}$ with difference $a_{2n+1} \to 0$. So both converge to the same limit.",
], ["c3-def-series"]))

B.append(example("c3-ex-alternating-harmonic", r"""
The alternating harmonic series $1 - \frac12 + \frac13 - \frac14 + \cdots$ converges by the alternating series test, since $1/k$ decreases to $0$. It does not converge absolutely, because $\sum 1/k$ diverges. So it converges conditionally. (Its sum is $\log 2$, which we do not prove here.)
""", "A conditionally convergent series"))

B.append(prose("c3-rearrangement-intro", r"""
Finite sums can be added in any order. Whether an infinite series can depends on how it converges: absolute convergence is robust under reordering, and conditional convergence is as fragile as could be.
"""))

B.append(definition("c3-def-rearrangement", "Rearrangement", r"""
A \emph{rearrangement} of the series $\sum_{k=1}^\infty a_k$ is a series $\sum_{j=1}^\infty a_{\beta(j)}$, where $\beta : \N \to \N$ is a bijection.
"""))

B.append(gate("theorem", "c3-thm-rearrangement-absolute", "Rearranging an absolutely convergent series", r"""
If $\sum a_k$ converges absolutely with sum $A$, then every rearrangement $\sum a_{\beta(j)}$ converges absolutely, and its sum is $A$.
""", r"""
Let $\eps > 0$. Since $\sum \abs{a_k}$ converges, the Cauchy convergence criterion gives an $N$ such that
\[ \sum_{k=N+1}^{m} \abs{a_k} < \eps \qquad \text{for all } m > N . \]
In particular $\abs{A_m - A_N} \le \sum_{k=N+1}^m \abs{a_k} < \eps$ for $m > N$, and letting $m \to \infty$ gives $\abs{A - A_N} \le \eps$.

Since $\beta$ is surjective, each of $1, \dots, N$ equals $\beta(j)$ for some $j$; let $M$ be the largest of these finitely many $j$. Then $\set{1,\dots,N} \subseteq \set{\beta(1),\dots,\beta(M)}$. Let $m \ge M$ and let $B_m = \sum_{j=1}^m a_{\beta(j)}$. Since $\beta$ is injective, the indices $\beta(1),\dots,\beta(m)$ are distinct; they include $1,\dots,N$, and the remaining ones form a finite set $E$ of integers greater than $N$. Thus
\[ B_m - A_N = \sum_{k \in E} a_k , \qquad \abs{B_m - A_N} \le \sum_{k \in E}\abs{a_k} \le \sum_{k=N+1}^{K}\abs{a_k} < \eps, \]
where $K > N$ is any integer at least as large as every element of $E$ (if $E$ is empty the bound is trivial). Therefore
\[ \abs{B_m - A} \le \abs{B_m - A_N} + \abs{A_N - A} < 2\eps \qquad \text{for all } m \ge M . \]
So $B_m \to A$: the rearrangement converges to $A$.

Finally, $\sum \abs{a_{\beta(j)}}$ is a rearrangement of the absolutely convergent series $\sum\abs{a_k}$, so by what was just proved it converges. Hence the rearrangement converges absolutely.
""", 3, 35, [
    r"Choose $N$ so that the tail $\sum_{k > N}\abs{a_k}$ is small. The first $N$ terms all appear among the first $M$ terms of the rearrangement, for some $M$.",
    r"For $m \ge M$, the $m$-th partial sum of the rearrangement differs from $A_N$ by a finite sum of terms $a_k$ with distinct indices $k > N$.",
], ["c3-thm-series-cauchy", "c3-def-rearrangement", "c3-def-absolute-convergence"]))

B.append(stated("theorem", "c3-thm-riemann-rearrangement", "Riemann's rearrangement theorem", r"""
If $\sum a_k$ converges conditionally, then for every $s \in \R$ there is a rearrangement of $\sum a_k$ that converges to $s$. There are also rearrangements that diverge to $+\infty$, to $-\infty$, and that oscillate.
"""))

B.append(remark("c3-rem-riemann-rearrangement", r"""
This theorem is taken on faith here; it is not used later. The idea: in a conditionally convergent series the positive terms alone sum to $+\infty$ and the negative terms alone to $-\infty$, while the terms tend to $0$. To reach $s$, add positive terms in order until the partial sum first exceeds $s$, then negative terms until it first falls below $s$, and so on. Every term is eventually used, and the overshoots are bounded by terms that tend to $0$. For instance, a suitable rearrangement of the alternating harmonic series sums to any number you like.
"""))

C = [
    card("c3-card-series-convergence", r"Define convergence of $\sum a_k$, and state the Cauchy convergence criterion for series.",
         r"The partial sums $A_n = a_1 + \dots + a_n$ converge. Equivalently: for every $\eps > 0$ there is $N$ with $\abs{\sum_{k=n}^m a_k} < \eps$ whenever $m \ge n \ge N$.", "c3-thm-series-cauchy"),
    card("c3-card-terms-to-zero", r"If $a_k \to 0$, must $\sum a_k$ converge?",
         r"No: the harmonic series $\sum 1/k$ diverges, since $\sum_{k=n+1}^{2n} 1/k \ge 1/2$. The converse is true: convergence forces $a_k \to 0$.", "c3-ex-harmonic"),
    card("c3-card-geometric", r"For which $\lambda$ does $\sum_{k \ge 0} \lambda^k$ converge, and to what?",
         r"Exactly for $\abs{\lambda} < 1$, with sum $1/(1-\lambda)$; partial sums are $(1 - \lambda^{n+1})/(1-\lambda)$.", "c3-thm-geometric-series"),
    card("c3-card-comparison", r"State the comparison test.",
         r"If $\abs{a_k} \le b_k$ for all large $k$ and $\sum b_k$ converges, then $\sum a_k$ converges (absolutely). Proof: Cauchy criterion.", "c3-thm-comparison-test"),
    card("c3-card-absolute-conditional", r"Define absolute and conditional convergence, with an example of the latter.",
         r"Absolute: $\sum\abs{a_k}$ converges (this implies $\sum a_k$ converges). Conditional: $\sum a_k$ converges but $\sum \abs{a_k}$ diverges, e.g. $\sum (-1)^{k+1}/k$.", "c3-ex-alternating-harmonic"),
    card("c3-card-p-series", r"For which $p$ does $\sum 1/k^p$ converge? State the integral test.",
         r"Exactly for $p > 1$. Integral test: for $f \ge 0$ nonincreasing on $[1,\infty)$, $\sum f(k)$ converges iff $\int_1^\infty f$ converges, because $f(k+1) \le \int_k^{k+1} f \le f(k)$.", "c3-ex-p-series"),
    card("c3-card-root-ratio", r"State the root test and the ratio test.",
         r"Root: with $\alpha = \limsup \abs{a_k}^{1/k}$, $\alpha < 1$ gives absolute convergence and $\alpha > 1$ divergence. Ratio: $\limsup \abs{a_{k+1}/a_k} < 1$ gives absolute convergence, $\liminf \abs{a_{k+1}/a_k} > 1$ divergence. Both compare with a geometric series; both are inconclusive at $1$.", "c3-thm-ratio-test"),
    card("c3-card-alternating", r"State the alternating series test and the idea of its proof.",
         r"If $a_k$ decreases to $0$ then $\sum (-1)^{k+1}a_k$ converges, with $\abs{S - S_n} \le a_{n+1}$. Even partial sums increase, odd ones decrease, and they differ by $a_{2n+1} \to 0$.", "c3-thm-alternating-series"),
    card("c3-card-rearrangement", r"What happens to the sum of a series under rearrangement?",
         r"If the series converges absolutely, every rearrangement converges to the same sum. If it converges only conditionally, rearrangements can converge to any real number, or diverge (Riemann)."),
]

write("3-series", B, C)
