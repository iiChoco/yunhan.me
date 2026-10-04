from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c2lib import Section

s = Section("2-other-metric-space-concepts")

s.p("c2-oth-intro", r"""
This section collects several further notions that will be used repeatedly. Cluster points refine the idea of a limit of a set by asking for crowding rather than mere approach. Perfect spaces, in which every point is a cluster point, give a second and purely metric proof that the real line is uncountable. We then record that arithmetic in $\R$ is continuous, and look at boundedness and its stronger, better-behaved cousin, total boundedness.
""")

s.d("c2-def-cluster-point", "Cluster point, condensation point", r"""
Let $S$ be a subset of a metric space $M$. A point $p \in M$ is a \emph{cluster point} of $S$ if every neighborhood $M_r(p)$, $r > 0$, contains infinitely many points of $S$. It is a \emph{condensation point} of $S$ if every neighborhood of $p$ contains uncountably many points of $S$. The set of cluster points of $S$ is written $S'$.
""")

s.t("theorem", "c2-thm-cluster-equivalents", "Four descriptions of a cluster point", r"""
Let $S \subset M$ and $p \in M$. The following are equivalent:
\begin{enumerate}
\item there is a sequence of \emph{distinct} points of $S$ converging to $p$;
\item every neighborhood of $p$ contains infinitely many points of $S$;
\item every neighborhood of $p$ contains at least two points of $S$;
\item every neighborhood of $p$ contains at least one point of $S$ other than $p$.
\end{enumerate}
""", r"""
(1) $\Rightarrow$ (2). Let $(p_n)$ be a sequence of distinct points of $S$ with $p_n \to p$, and let $r > 0$. There is an $N$ with $p_n \in M_r(p)$ for all $n \ge N$. The points $p_N, p_{N+1}, \dots$ are distinct, so $M_r(p)$ contains infinitely many points of $S$.

(2) $\Rightarrow$ (3) is immediate, and so is (3) $\Rightarrow$ (4): of two different points of $S$ in $M_r(p)$, at least one is not $p$.

(4) $\Rightarrow$ (1). Choose $p_1 \in S \cap M_1(p)$ with $p_1 \ne p$. Having chosen $p_1, \dots, p_{n-1}$, all different from $p$, let
\[ r_n = \min\set{\tfrac1n,\; d(p_{n-1}, p)} > 0 \]
and choose $p_n \in S \cap M_{r_n}(p)$ with $p_n \ne p$. Then $0 < d(p_n,p) < d(p_{n-1},p)$ for all $n \ge 2$, so the distances $d(p_n,p)$ are strictly decreasing and the points $p_n$ are distinct. Also $d(p_n,p) < 1/n$, so $p_n \to p$.
""", 2, 25, [
    r"Prove (1) $\Rightarrow$ (2) $\Rightarrow$ (3) $\Rightarrow$ (4) $\Rightarrow$ (1). Only the last needs a construction.",
    r"Choose $p_n \ne p$ in $S$ inside a ball about $p$ whose radius is at most $1/n$ and at most $d(p_{n-1},p)$. Why are the $p_n$ distinct?",
], ["c2-def-cluster-point", "c2-def-convergence"])

s.t("proposition", "c2-prop-closure-cluster", "Closure and cluster points", r"""
For every subset $S$ of a metric space, $\overline{S} = S \cup S'$. Consequently $S$ is closed if and only if $S' \subset S$.
""", r"""
$S \subset \overline{S}$, and a cluster point of $S$ has a point of $S$ in each of its neighborhoods, so it is a limit of $S$ by the lemma on limits and neighborhoods; since the closure is the limit set, $S' \subset \overline{S}$. Thus $S \cup S' \subset \overline{S}$.

Conversely let $p \in \overline{S}$ with $p \notin S$. Then $p$ is a limit of $S$, so every neighborhood of $p$ contains a point of $S$, and that point is not $p$ because $p \notin S$. By condition (4) of the four descriptions of a cluster point, $p \in S'$. Hence $\overline{S} \subset S \cup S'$.

Finally, $S$ is closed if and only if $\overline{S} = S$, i.e. $S \cup S' = S$, i.e. $S' \subset S$.
""", 2, 15, [
    r"A point of the closure that is not in $S$ has points of $S$, necessarily different from it, in each neighborhood.",
], ["c2-thm-cluster-equivalents", "c2-prop-closure-lim", "c2-lem-limit-ball"])

s.t("exercise", "c2-ex-lub-in-closure", "The least upper bound lies in the closure", r"""
Let $S \subset \R$ be nonempty and bounded above. Show that $\lub S \in \overline{S}$. Hence a nonempty closed subset of $\R$ that is bounded above contains its least upper bound (and similarly for greatest lower bounds).
""", r"""
Let $u = \lub S$. For each $n \in \N$ the number $u - 1/n$ is not an upper bound of $S$, so there is an $s_n \in S$ with $u - 1/n < s_n \le u$. Then $\abs{s_n - u} < 1/n$, so $s_n \to u$ and $u \in \lim S = \overline{S}$. If $S$ is closed then $\overline{S} = S$, so $u \in S$. The statement for greatest lower bounds follows by the same argument with $u + 1/n$, or by applying this one to $\set{-x : x \in S}$.
""", 1, 10, [
    r"$u - 1/n$ is not an upper bound.",
], ["c2-prop-closure-lim"])

s.d("c2-def-perfect", "Perfect space", r"""
A metric space $M$ is \emph{perfect} if every point of $M$ is a cluster point of $M$, that is, $M' = M$. Equivalently, no point is \emph{isolated}: there is no $p$ with $M_r(p) = \set{p}$ for some $r > 0$.
""")

s.e("c2-ex-perfect", "Perfect and not", r"""
$\R$ and $[a,b]$ (with $a < b$) are perfect, since every interval about a point contains infinitely many points of the space. $\Q$ is perfect too. $\N$ and $\Z$ are not: every point is isolated. The set $\set{0} \cup \set{1/n : n \in \N}$ is compact but not perfect; only $0$ is a cluster point.
""")

s.t("theorem", "c2-thm-perfect-uncountable", "A nonempty perfect complete metric space is uncountable", r"""
Let $M$ be a nonempty, perfect, complete metric space. Then $M$ is uncountable.
""", r"""
Since $M$ is nonempty and each of its points is a cluster point, every neighborhood $M_r(p)$ contains infinitely many points of $M$; in particular $M$ is infinite. Suppose $M$ is countable. Then there is a sequence $x_1, x_2, x_3, \dots$ in which every point of $M$ appears. Write $D_r(y) = \set{x : d(x,y) \le r}$ for the closed ball; closed balls are closed sets.

We construct points $y_n \in M$ and radii $r_n > 0$ such that, with $Y_n = D_{r_n}(y_n)$,
\[ Y_1 \supset Y_2 \supset Y_3 \supset \cdots, \qquad x_n \notin Y_n, \qquad r_n \le \tfrac1n . \]
\emph{Step 1.} Choose $y_1 \ne x_1$ and put $r_1 = \min\set{1,\ d(y_1,x_1)/2}$. Then $d(x_1,y_1) > r_1$, so $x_1 \notin Y_1$.

\emph{Step $n+1$.} Suppose $y_n, r_n$ are chosen. Since $y_n$ is a cluster point of $M$, the neighborhood $M_{r_n}(y_n)$ contains infinitely many points, so we can choose $y_{n+1} \in M_{r_n}(y_n)$ with $y_{n+1} \ne x_{n+1}$. Put
\[ r_{n+1} = \min\set{\tfrac{1}{n+1},\ \ r_n - d(y_{n+1},y_n),\ \ \tfrac12 d(y_{n+1},x_{n+1})} , \]
which is positive. If $x \in Y_{n+1}$ then $d(x,y_n) \le d(x,y_{n+1}) + d(y_{n+1},y_n) \le r_{n+1} + d(y_{n+1},y_n) \le r_n$, so $Y_{n+1} \subset Y_n$. And $d(x_{n+1},y_{n+1}) > r_{n+1}$, so $x_{n+1} \notin Y_{n+1}$.

\emph{The centers converge.} If $m, n \ge N$ then $y_m \in Y_m \subset Y_N$ and $y_n \in Y_N$, so $d(y_m,y_n) \le d(y_m,y_N) + d(y_N,y_n) \le 2r_N \le 2/N$. Hence $(y_n)$ is Cauchy, and by completeness $y_n \to y$ for some $y \in M$.

\emph{The limit is not on the list.} Fix $n$. For all $m \ge n$ we have $y_m \in Y_n$; the sequence $(y_m)_{m \ge n}$ converges to $y$ and $Y_n$ is closed, so $y \in Y_n$. Since $x_n \notin Y_n$, $y \ne x_n$. This holds for every $n$, so $y$ is a point of $M$ that does not appear in the sequence $(x_n)$, a contradiction. Hence $M$ is uncountable.
""", 4, 75, [
    r"Suppose $M = \set{x_1, x_2, \dots}$ and try to build a point that avoids every $x_n$, as a limit.",
    r"Build nested closed balls $Y_1 \supset Y_2 \supset \cdots$ with radii tending to $0$ and $x_n \notin Y_n$. Perfection lets you pick the next center inside the current ball and different from $x_{n+1}$.",
    r"The centers form a Cauchy sequence; completeness gives a limit, which lies in every $Y_n$ because closed balls are closed.",
], ["c2-def-perfect", "c2-def-cluster-point", "c2-ex-closed-ball", "c2-def-cauchy"])

s.t("corollary", "c2-cor-everywhere-uncountable", "Every neighborhood is uncountable", r"""
Let $M$ be a nonempty perfect complete metric space. Then every neighborhood $M_r(p)$ is uncountable; that is, every point of $M$ is a condensation point of $M$. In particular $\R$ and every interval $[a,b]$ with $a < b$ are uncountable.
""", r"""
Let $p \in M$, $r > 0$, and let $B = M_{r/2}(p)$ and $K = \overline{B}$. The closed ball $D_{r/2}(p)$ is a closed set containing $B$, so $K \subset D_{r/2}(p) \subset M_r(p)$. It therefore suffices to show $K$ is uncountable, and for that we check that the subspace $K$ is nonempty, complete and perfect.

$K$ contains $p$. $K$ is a closed subset of the complete space $M$, so it is complete. To see that $K$ is perfect, let $q \in K$ and $\eps > 0$. Since $q$ is a limit of $B$ there is a point $b \in B$ with $d(b,q) < \eps/2$. Since $B$ is open there is an $\eta > 0$ with $M_\eta(b) \subset B$; shrinking it we may take $\eta \le \eps/2$. As $M$ is perfect, $M_\eta(b)$ contains infinitely many points of $M$. All of them lie in $B \subset K$, and all are within $\eta + \eps/2 \le \eps$ of $q$. So the $\eps$-neighborhood of $q$ in $K$ contains infinitely many points of $K$: $q$ is a cluster point of $K$.

By the theorem, $K$ is uncountable, hence so is $M_r(p) \supset K$.

$\R$ is nonempty, complete and perfect, so it is uncountable. $[a,b]$ is a closed subset of $\R$, hence complete, and it is nonempty and perfect, so it is uncountable as well.
""", 3, 35, [
    r"Apply the theorem to a smaller space sitting inside $M_r(p)$. It must be complete, so make it closed.",
    r"Take $K$ to be the closure of $M_{r/2}(p)$. It lies in $M_r(p)$ and is complete. Why is it perfect?",
], ["c2-thm-perfect-uncountable", "c2-thm-closed-complete", "c2-ex-closed-ball", "c2-prop-ball-open", "c2-prop-closure-lim", "c2-lem-limit-ball"])

s.p("c2-oth-arithmetic-prose", r"""
\textbf{Continuity of arithmetic.} Addition, subtraction, multiplication and division are functions of two real variables, and they are continuous. In terms of sequences this is the familiar statement that limits respect arithmetic; recall that convergence in $\R \times \R = \R^2$ is componentwise.
""")

s.t("theorem", "c2-thm-arithmetic-continuous", r"Arithmetic in $\R$ is continuous", r"""
Let $x_n \to x$ and $y_n \to y$ in $\R$. Then
\[ x_n + y_n \to x + y, \qquad x_n - y_n \to x - y, \qquad x_n y_n \to xy, \]
and if $y \ne 0$ and $y_n \ne 0$ for all $n$, then $x_n / y_n \to x/y$. Equivalently, the maps $(x,y) \mapsto x+y$, $x - y$, $xy$ are continuous from $\R^2$ to $\R$, and $(x,y) \mapsto x/y$ is continuous on $\R \times (\R \setminus \set{0})$.
""", r"""
\emph{Sum and difference.} $\abs{(x_n \pm y_n) - (x \pm y)} \le \abs{x_n - x} + \abs{y_n - y}$. Given $\eps > 0$ choose $N$ with $\abs{x_n - x} < \eps/2$ and $\abs{y_n - y} < \eps/2$ for $n \ge N$; then the left side is less than $\eps$.

\emph{Product.} Write
\[ x_n y_n - xy = x_n (y_n - y) + y (x_n - x). \]
Given $\eps > 0$ choose $N$ such that for $n \ge N$
\[ \abs{x_n - x} < \min\set{1,\ \frac{\eps}{2(\abs{y} + 1)}} \quad\text{and}\quad \abs{y_n - y} < \frac{\eps}{2(\abs{x}+1)} . \]
For such $n$, $\abs{x_n} \le \abs{x} + \abs{x_n - x} < \abs{x} + 1$, hence
\[ \abs{x_n y_n - xy} \le \abs{x_n}\abs{y_n - y} + \abs{y}\abs{x_n - x} < (\abs{x}+1)\frac{\eps}{2(\abs{x}+1)} + \abs{y}\frac{\eps}{2(\abs{y}+1)} \le \eps . \]

\emph{Quotient.} First we show $1/y_n \to 1/y$. Choose $N_1$ with $\abs{y_n - y} < \abs{y}/2$ for $n \ge N_1$; then $\abs{y_n} \ge \abs{y} - \abs{y_n - y} > \abs{y}/2$. Given $\eps > 0$ choose $N \ge N_1$ with $\abs{y_n - y} < \eps \abs{y}^2/2$ for $n \ge N$. Then for $n \ge N$
\[ \abs{\frac{1}{y_n} - \frac1y} = \frac{\abs{y - y_n}}{\abs{y_n}\abs{y}} < \frac{2\abs{y_n - y}}{\abs{y}^2} < \eps . \]
By the product rule, $x_n / y_n = x_n \cdot (1/y_n) \to x \cdot (1/y) = x/y$.

\emph{Reformulation.} A sequence $(x_n,y_n)$ converges to $(x,y)$ in $\R^2$ exactly when $x_n \to x$ and $y_n \to y$, so what was shown is that each of the four maps preserves sequential convergence on its domain.
""", 3, 40, [
    r"For the product, write $x_n y_n - xy = x_n(y_n - y) + y(x_n - x)$ and control $\abs{x_n}$.",
    r"For the reciprocal, first make $\abs{y_n} > \abs{y}/2$, then estimate $\abs{1/y_n - 1/y} = \abs{y - y_n}/(\abs{y_n}\abs{y})$.",
], ["c2-def-convergence", "c2-cor-rm-convergence", "c2-def-continuity"])

s.t("corollary", "c2-cor-function-arithmetic", "Sums, products and quotients of continuous functions", r"""
Let $f, g : M \to \R$ be continuous functions on a metric space $M$. Then $f + g$, $f - g$ and $fg$ are continuous, and if $g(x) \ne 0$ for all $x \in M$ then $f/g$ is continuous. In particular every polynomial is a continuous function $\R \to \R$, and $x \mapsto \abs{x}$ is continuous.
""", r"""
Let $p_n \to p$ in $M$. By continuity $f(p_n) \to f(p)$ and $g(p_n) \to g(p)$ in $\R$. By the continuity of arithmetic, $f(p_n) + g(p_n) \to f(p) + g(p)$, $f(p_n) - g(p_n) \to f(p) - g(p)$, $f(p_n) g(p_n) \to f(p) g(p)$, and, when $g$ has no zeros, $f(p_n)/g(p_n) \to f(p)/g(p)$. So each of the four functions preserves sequential convergence.

Constant functions and the identity function $x \mapsto x$ on $\R$ are continuous straight from the definition. A monomial $c x^k$ is a product of finitely many of these, and a polynomial is a finite sum of monomials, so by induction on the number of factors and terms every polynomial is continuous. Finally $\abs{\abs{x_n} - \abs{x}} \le \abs{x_n - x}$, so $x_n \to x$ implies $\abs{x_n} \to \abs{x}$.
""", 1, 15, [
    r"Use the sequential definition of continuity and the previous theorem.",
], ["c2-thm-arithmetic-continuous", "c2-def-continuity"])

s.p("c2-oth-bounded-prose", r"""
\textbf{Boundedness.} Recall that $S \subset M$ is bounded if it lies in some neighborhood $M_r(p)$. Boundedness is useful, but it is a property of the metric and not of the topology, as the next exercise shows.
""")

s.t("proposition", "c2-prop-cauchy-bounded", "Cauchy sequences are bounded", r"""
Every Cauchy sequence in a metric space is bounded. In particular every convergent sequence is bounded.
""", r"""
Let $(p_n)$ be Cauchy. Taking $\eps = 1$ there is an $N$ with $d(p_n,p_m) < 1$ for all $m, n \ge N$; in particular $d(p_n,p_N) < 1$ for $n \ge N$. Let
\[ r = 1 + \max\set{d(p_1,p_N), \dots, d(p_N,p_N)} . \]
Then $d(p_n,p_N) < r$ for every $n$: for $n \le N$ by the choice of $r$, and for $n \ge N$ because $d(p_n,p_N) < 1 \le r$. So all terms lie in $M_r(p_N)$. Convergent sequences are Cauchy, hence bounded.
""", 1, 10, [
    r"Beyond some index all terms are within $1$ of a fixed term; only finitely many terms come before.",
], ["c2-def-cauchy", "c2-def-bounded", "c2-prop-convergent-cauchy"])

s.t("exercise", "c2-ex-r-homeo-interval", r"$\R$ is homeomorphic to $(-1,1)$", r"""
Show that $f(x) = \dfrac{x}{1 + \abs{x}}$ is a homeomorphism from $\R$ onto $(-1,1)$. Conclude that neither boundedness nor completeness is a topological property.
""", r"""
Since $\abs{x} < 1 + \abs{x}$ we have $\abs{f(x)} < 1$, so $f$ maps $\R$ into $(-1,1)$. Define $g : (-1,1) \to \R$ by $g(y) = y/(1 - \abs{y})$; the denominator is positive on $(-1,1)$.

Both $f$ and $g$ are quotients of continuous functions with denominators that never vanish (the functions $x \mapsto x$, $x \mapsto \abs{x}$ and constants are continuous, and so are their sums and differences), so both are continuous; for $g$ this is continuity on the metric space $(-1,1)$.

They are inverse to each other. For $x \in \R$, $\abs{f(x)} = \abs{x}/(1+\abs{x})$, so $1 - \abs{f(x)} = 1/(1+\abs{x})$ and
\[ g(f(x)) = \frac{x}{1+\abs{x}} \cdot (1 + \abs{x}) = x . \]
For $y \in (-1,1)$, $\abs{g(y)} = \abs{y}/(1-\abs{y})$, so $1 + \abs{g(y)} = 1/(1-\abs{y})$ and
\[ f(g(y)) = \frac{y}{1-\abs{y}} \cdot (1 - \abs{y}) = y . \]
Hence $f$ is a bijection $\R \to (-1,1)$ with continuous inverse $g$: a homeomorphism.

$\R$ is unbounded and complete. $(-1,1)$ is bounded, and it is not complete, since it is not closed in $\R$ and complete subsets are closed (concretely, $1 - 1/n$ is a Cauchy sequence in $(-1,1)$ with no limit there). So homeomorphic spaces can differ in boundedness and in completeness.
""", 2, 25, [
    r"Guess the inverse by solving $y = x/(1+\abs{x})$ for $x$, noting that $x$ and $y$ have the same sign.",
    r"The inverse is $g(y) = y/(1-\abs{y})$. Continuity of both follows from the arithmetic of continuous functions.",
], ["c2-cor-function-arithmetic", "c2-def-homeomorphism", "c2-thm-closed-complete"])

s.d("c2-def-totally-bounded", "Totally bounded", r"""
A subset $S$ of a metric space $M$ is \emph{totally bounded} if for every $\eps > 0$ there are finitely many points $s_1, \dots, s_k \in S$ with
\[ S \subset M_\eps(s_1) \cup \dots \cup M_\eps(s_k) . \]
In words: for every $\eps$, finitely many $\eps$-neighborhoods centered in $S$ cover $S$. (The empty set is totally bounded, with $k = 0$.)
""")

s.t("proposition", "c2-prop-totally-bounded-basics", "Total boundedness: first properties", r"""
Let $S$ be a totally bounded subset of a metric space $M$. Then
\begin{enumerate}
\item $S$ is bounded;
\item every subset $T \subset S$ is totally bounded.
\end{enumerate}
""", r"""
(1) If $S$ is empty there is nothing to prove. Otherwise take $\eps = 1$: $S \subset M_1(s_1) \cup \dots \cup M_1(s_k)$ with $k \ge 1$. Let $r = 1 + \max_i d(s_i, s_1)$. Any $x \in S$ lies in some $M_1(s_i)$, so $d(x,s_1) \le d(x,s_i) + d(s_i,s_1) < 1 + d(s_i,s_1) \le r$. Thus $S \subset M_r(s_1)$.

(2) Let $\eps > 0$. Cover $S$ by finitely many neighborhoods $M_{\eps/2}(s_1), \dots, M_{\eps/2}(s_k)$ with $s_i \in S$. For each $i$ such that $M_{\eps/2}(s_i)$ contains a point of $T$, choose one such point $t_i$. If $x \in T$, then $x \in M_{\eps/2}(s_i)$ for some $i$; this neighborhood meets $T$, so $t_i$ is defined, and
\[ d(x,t_i) \le d(x,s_i) + d(s_i,t_i) < \frac\eps2 + \frac\eps2 = \eps . \]
So the finitely many neighborhoods $M_\eps(t_i)$, centered in $T$, cover $T$.
""", 2, 20, [
    r"For (1), use $\eps = 1$ and measure everything from one of the centers.",
    r"For (2), the centers for $S$ need not lie in $T$. Start with radius $\eps/2$ and move each center to a point of $T$ in the same ball.",
], ["c2-def-totally-bounded", "c2-def-bounded"])

s.t("proposition", "c2-prop-bounded-rm-totally-bounded", r"Bounded subsets of $\R^m$ are totally bounded", r"""
A subset of $\R^m$ is totally bounded if and only if it is bounded.
""", r"""
Totally bounded sets are bounded in any metric space. Conversely let $S \subset \R^m$ be bounded, $S \subset M_r(p)$, and let $\eps > 0$. As each coordinate satisfies $\abs{x_i - p_i} \le \abs{x - p}$, $S$ lies in the cube $Q = [p_1 - r, p_1 + r] \times \dots \times [p_m - r, p_m + r]$.

Choose $k \in \N$ with $2r\sqrt{m}/k < \eps$ and let $h = 2r/k$. For each multi-index $j = (j_1, \dots, j_m)$ with $j_i \in \set{1, \dots, k}$ let
\[ Q_j = \prod_{i=1}^m \big[\, p_i - r + (j_i - 1)h,\ \ p_i - r + j_i h \,\big] . \]
There are $k^m$ of these small cubes. They cover $Q$: for $x \in Q$ and each $i$, the $k$ intervals $[p_i - r + (l-1)h,\ p_i - r + lh]$, $l = 1, \dots, k$, cover $[p_i - r, p_i + r]$, so $x_i$ lies in one of them, say the one with $l = j_i$; then $x \in Q_j$. If $x, y \in Q_j$ then $\abs{x_i - y_i} \le h$ for each $i$, so
\[ \abs{x - y} = \Big(\sum_{i=1}^m (x_i - y_i)^2\Big)^{1/2} \le h\sqrt{m} < \eps . \]
For each $j$ such that $Q_j \cap S \ne \varnothing$ choose a point $s_j \in Q_j \cap S$. Every $x \in S$ lies in some $Q_j$, which then meets $S$, and $\abs{x - s_j} < \eps$. So the finitely many neighborhoods $M_\eps(s_j)$, centered in $S$, cover $S$.
""", 3, 30, [
    r"Put $S$ in a big cube and chop the cube into small cubes.",
    r"A cube of side $h$ in $\R^m$ has diameter $h\sqrt m$. Pick one point of $S$ in each small cube that meets $S$.",
], ["c2-def-totally-bounded", "c2-prop-totally-bounded-basics", "c2-def-bounded"])

s.e("c2-ex-bounded-not-totally", "Bounded but not totally bounded", r"""
$\N$ with the discrete metric is bounded, but for $\eps = 1/2$ every $\eps$-neighborhood is a single point, so no finite number of them covers $\N$. Total boundedness is the right notion of "small" in a general metric space; in the next section it is shown that a metric space is compact exactly when it is complete and totally bounded.
""")

s.card("c2-card-cluster", "Define cluster point of $S$ and give three equivalent conditions.",
       r"Every neighborhood of $p$ contains infinitely many points of $S$. Equivalently: a sequence of distinct points of $S$ converges to $p$; every neighborhood contains two points of $S$; every neighborhood contains a point of $S$ other than $p$.",
       "c2-thm-cluster-equivalents")
s.card("c2-card-closure-cluster", r"Express $\overline{S}$ using cluster points.",
       r"$\overline{S} = S \cup S'$; $S$ is closed iff it contains its cluster points.",
       "c2-prop-closure-cluster")
s.card("c2-card-perfect", "Define perfect metric space and state the theorem on perfect complete spaces.",
       r"Perfect: every point is a cluster point of the space (no isolated points). A nonempty perfect complete metric space is uncountable; in fact each of its neighborhoods is uncountable.",
       "c2-thm-perfect-uncountable")
s.card("c2-card-perfect-idea", "Idea of the proof that a nonempty perfect complete space is uncountable.",
       r"If $M = \set{x_1, x_2, \dots}$, build nested closed balls $Y_n$ with radii $\to 0$ and $x_n \notin Y_n$; the centers are Cauchy, their limit lies in every $Y_n$ and so equals no $x_n$.",
       "c2-thm-perfect-uncountable")
s.card("c2-card-arithmetic", r"Key estimate for $x_n y_n \to xy$.",
       r"$x_n y_n - xy = x_n(y_n - y) + y(x_n - x)$, with $\abs{x_n} \le \abs{x} + 1$ eventually.",
       "c2-thm-arithmetic-continuous")
s.card("c2-card-not-topological", "Show that boundedness and completeness are not topological properties.",
       r"$x \mapsto x/(1+\abs{x})$ is a homeomorphism from $\R$ (unbounded, complete) onto $(-1,1)$ (bounded, incomplete).",
       "c2-ex-r-homeo-interval")
s.card("c2-card-totally-bounded", "Define totally bounded. Compare with bounded.",
       r"For every $\eps > 0$ finitely many $\eps$-neighborhoods centered in $S$ cover $S$. Totally bounded implies bounded; the converse holds in $\R^m$ but fails for $\N$ with the discrete metric.",
       "c2-ex-bounded-not-totally")

s.write()
