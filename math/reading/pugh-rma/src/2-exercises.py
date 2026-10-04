"""End-of-chapter exercises for chapter 2 (A Taste of Topology) of the Pugh reading module.

Every block is optional extra credit; the chapter clears on its theorems alone.
"""
from __future__ import annotations

import json

OUT = "/Users/choco/Projects/yunhan.me/math/reading/pugh-rma/sections/2-exercises.json"

blocks: list[dict] = []


def prose(id: str, tex: str) -> None:
    blocks.append({"id": id, "kind": "prose", "tex": tex.strip()})


def ex(id: str, title: str, tex: str, proof: str, difficulty: int, minutes: int,
       hints: list[str], uses: list[str]) -> None:
    blocks.append({"id": id, "kind": "exercise", "number": "", "title": title, "tex": tex.strip(),
                   "proof": proof.strip(), "difficulty": difficulty, "minutes": minutes,
                   "hints": [h.strip() for h in hints], "uses": uses, "optional": True})


prose("c2-exercises-intro", r"""
These exercises are extra credit: none of them is a gate, and the chapter clears on its theorems alone. Take them in any order; each may lean on anything proved in the chapter, one of them leans on an earlier exercise in this list, and another looks back at one.
""")

# ---------------------------------------------------------------- metric basics

ex("c2-ex-bounded-metric", "Every metric space carries a bounded metric", r"""
Let $(M,d)$ be a nonempty metric space and define
\[ \rho(x,y) = \frac{d(x,y)}{1 + d(x,y)} . \]
Show that $\rho$ is a metric on $M$, that $M$ is bounded with respect to $\rho$, and that $d$ and $\rho$ have the same convergent sequences with the same limits. Conclude that $d$ and $\rho$ have the same closed sets and the same open sets.
""", r"""
Let $\phi(t) = t/(1+t)$ for $t \ge 0$. Since $\phi(t) = 1 - 1/(1+t)$, $\phi$ is strictly increasing on $[0,\infty)$, $\phi(0) = 0$, and $0 \le \phi(t) < 1$. Also $\phi$ is subadditive: for $a, b \ge 0$,
\[ \phi(a+b) = \frac{a}{1+a+b} + \frac{b}{1+a+b} \le \frac{a}{1+a} + \frac{b}{1+b} = \phi(a) + \phi(b) . \]

\emph{$\rho$ is a metric.} $\rho(x,y) = \phi(d(x,y)) \ge 0$, and it is $0$ exactly when $d(x,y) = 0$, that is when $x = y$. Symmetry of $\rho$ follows from symmetry of $d$. For the triangle inequality, monotonicity and then subadditivity of $\phi$ give
\[ \rho(x,z) = \phi(d(x,z)) \le \phi\big(d(x,y) + d(y,z)\big) \le \phi(d(x,y)) + \phi(d(y,z)) = \rho(x,y) + \rho(y,z) . \]

\emph{Bounded.} Fix any $p \in M$. Every $x \in M$ has $\rho(x,p) < 1$, so $M$ is the $\rho$-neighborhood of radius $1$ about $p$.

\emph{Same convergent sequences.} Since $1 + d \ge 1$ we have $\rho \le d$, so if $d(p_n,p) \to 0$ then $\rho(p_n,p) \to 0$. Conversely $1 - \rho(x,y) = 1/(1 + d(x,y))$, hence $d = \rho/(1-\rho)$, and $t \mapsto t/(1-t) = 1/(1-t) - 1$ is increasing on $[0,1)$. Suppose $\rho(p_n,p) \to 0$ and let $\eps > 0$. Put $\eta = \eps/(1+\eps) \in (0,1)$. For $n$ large, $\rho(p_n,p) < \eta$, and then $d(p_n,p) = \rho(p_n,p)/(1 - \rho(p_n,p)) < \eta/(1-\eta) = \eps$. So $d(p_n,p) \to 0$.

\emph{Same closed and open sets.} A set is closed when it contains the limits of all convergent sequences of its points; the convergent sequences and their limits are the same for $d$ and $\rho$, so the closed sets are the same. Open sets are exactly the complements of closed sets, so they are the same as well.
""", 2, 25, [
    r"Write $\rho = \phi \circ d$ with $\phi(t) = t/(1+t)$. Show $\phi$ is increasing and $\phi(a+b) \le \phi(a) + \phi(b)$.",
    r"$\rho \le d$ gives one direction of the comparison of convergent sequences. Solve $\rho = d/(1+d)$ for $d$ to get the other.",
    r"Closed sets are defined through convergent sequences, and open sets through closed sets.",
], ["c2-def-metric-space", "c2-def-convergence", "c2-def-bounded", "c2-def-closed-open", "c2-thm-open-closed-dual"])

ex("c2-ex-ball-closure", "The closure of an open ball", r"""
Let $p$ be a point of a metric space $M$ and $r > 0$. Show that $\overline{M_r(p)} \subset D_r(p) = \set{x \in M : d(x,p) \le r}$, and that equality holds when $M = \R^m$. Prove or disprove: equality holds in every metric space.
""", r"""
\emph{The inclusion.} The closed ball $D_r(p)$ is a closed set (closed balls are closed) and it contains $M_r(p)$. The closure $\overline{M_r(p)}$ is the intersection of all closed sets containing $M_r(p)$, so $\overline{M_r(p)} \subset D_r(p)$.

\emph{Equality in $\R^m$.} Let $x \in \R^m$ with $\abs{x - p} \le r$ and put $x_n = p + (1 - \tfrac1n)(x - p)$. Then $\abs{x_n - p} = (1 - \tfrac1n)\abs{x-p} \le (1 - \tfrac1n) r < r$, so $x_n \in M_r(p)$, and $\abs{x_n - x} = \abs{x - p}/n \le r/n \to 0$. Thus $x$ is a limit of $M_r(p)$, and since the closure is the limit set, $x \in \overline{M_r(p)}$. So $D_r(p) \subset \overline{M_r(p)}$, and with the inclusion above the two sets are equal.

\emph{Equality can fail.} Let $M$ be a set with at least two points, carrying the discrete metric, and take $r = 1$. If $d(x,p) < 1$ then $d(x,p) = 0$, so $M_1(p) = \set{p}$. The one-point set $\set{p}$ is closed (it is the closed ball $D_0(p)$), so $\overline{M_1(p)} = \set{p}$. But every distance is at most $1$, so $D_1(p) = M \ne \set{p}$.
""", 2, 20, [
    r"The closed ball is a closed set containing the open ball; that gives the inclusion at once.",
    r"In $\R^m$, slide a point of the sphere toward the center along the segment joining them.",
    r"For a counterexample, look at the discrete metric with $r = 1$.",
], ["c2-ex-closed-ball", "c2-def-closure-interior-boundary", "c2-prop-closure-lim", "c2-ex-discrete-metric", "c2-ex-metric-spaces"])

ex("c2-ex-distance-to-set", "The distance to a set", r"""
For a nonempty subset $S$ of a metric space $M$ and a point $x \in M$ define
\[ d(x,S) = \inf \set{d(x,s) : s \in S} . \]
\begin{enumerate}
\item Show that $\abs{d(x,S) - d(y,S)} \le d(x,y)$ for all $x, y \in M$. Hence $x \mapsto d(x,S)$ is a uniformly continuous function $M \to \R$.
\item Show that $d(x,S) = 0$ if and only if $x \in \overline{S}$.
\end{enumerate}
Conclude that every closed subset $K$ of $M$ is the set of zeros $\set{x \in M : f(x) = 0}$ of some continuous function $f : M \to \R$.
""", r"""
The set $\set{d(x,s) : s \in S}$ is nonempty and bounded below by $0$, so its greatest lower bound $d(x,S)$ exists and is $\ge 0$.

(1) Let $x, y \in M$. For every $s \in S$, $d(x,S) \le d(x,s) \le d(x,y) + d(y,s)$, so $d(x,S) - d(x,y) \le d(y,s)$. Thus $d(x,S) - d(x,y)$ is a lower bound of $\set{d(y,s) : s \in S}$, and therefore $d(x,S) - d(x,y) \le d(y,S)$, that is, $d(x,S) - d(y,S) \le d(x,y)$. Exchanging $x$ and $y$ gives $d(y,S) - d(x,S) \le d(x,y)$, and the two together are the claim. Given $\eps > 0$, $\delta = \eps$ now works for all pairs of points, so the function is uniformly continuous. In particular it satisfies the $\eps,\delta$ condition and is continuous.

(2) If $x \in \overline{S}$, then since the closure is the limit set there are $s_n \in S$ with $s_n \to x$, and $0 \le d(x,S) \le d(x,s_n) \to 0$, so $d(x,S) = 0$. Conversely suppose $d(x,S) = 0$ and let $r > 0$. Then $r$ is not a lower bound of $\set{d(x,s) : s \in S}$, so some $s \in S$ has $d(x,s) < r$: every neighborhood of $x$ contains a point of $S$. By the lemma on limits and neighborhoods $x$ is a limit of $S$, so $x \in \overline{S}$.

For the conclusion, if $K = \varnothing$ take the constant function $f = 1$. Otherwise put $f(x) = d(x,K)$, which is continuous by (1); by (2) its zeros are the points of $\overline{K} = K$, since $K$ is closed.
""", 2, 20, [
    r"For (1), compare $d(x,s)$ with $d(x,y) + d(y,s)$ and take the infimum over $s$.",
    r"For (2), $d(x,S) = 0$ says that every neighborhood of $x$ contains a point of $S$.",
], ["c2-def-metric-space", "c2-def-uniform-continuity", "c2-thm-eps-delta", "c2-prop-closure-lim", "c2-lem-limit-ball"])

ex("c2-ex-separating-closed-sets", "Disjoint closed sets are separated by a continuous function", r"""
Let $A$ and $B$ be disjoint nonempty closed subsets of a metric space $M$. Show that there is a continuous function $f : M \to \R$ with $0 \le f \le 1$, $f(x) = 0$ exactly for $x \in A$, and $f(x) = 1$ exactly for $x \in B$. Deduce that there are disjoint open sets $U \supset A$ and $V \supset B$.
""", r"""
Using the distance to a set from the previous exercise, put
\[ f(x) = \frac{d(x,A)}{d(x,A) + d(x,B)} . \]
The denominator never vanishes: $d(x,A) + d(x,B) = 0$ would force $d(x,A) = 0$ and $d(x,B) = 0$, that is $x \in \overline{A} \cap \overline{B} = A \cap B$, because closed sets equal their closures; but $A \cap B = \varnothing$. The functions $x \mapsto d(x,A)$ and $x \mapsto d(x,B)$ are continuous, so their sum is continuous, and the quotient of continuous functions with a nonvanishing denominator is continuous. Since $0 \le d(x,A) \le d(x,A) + d(x,B)$ we have $0 \le f \le 1$. Now $f(x) = 0$ if and only if $d(x,A) = 0$, if and only if $x \in \overline{A} = A$; and $f(x) = 1$ if and only if $d(x,A) = d(x,A) + d(x,B)$, if and only if $d(x,B) = 0$, if and only if $x \in B$.

The rays $(-\infty, \tfrac12)$ and $(\tfrac12, \infty)$ are open in $\R$: if $t < \tfrac12$ then $(t - r, t + r) \subset (-\infty, \tfrac12)$ for $r = \tfrac12 - t$, and similarly on the other side. By the open set condition for continuity,
\[ U = f^{-1}\big((-\infty, \tfrac12)\big), \qquad V = f^{-1}\big((\tfrac12, \infty)\big) \]
are open in $M$. They are disjoint, since no $f(x)$ lies in both rays. Finally $f = 0 < \tfrac12$ on $A$, so $A \subset U$, and $f = 1 > \tfrac12$ on $B$, so $B \subset V$.
""", 3, 30, [
    r"Normalize the distance to $A$ by the distance to $A$ plus the distance to $B$.",
    r"Why does the denominator never vanish? A closed set is its own closure.",
    r"For the open sets, pull back the rays $(-\infty, 1/2)$ and $(1/2, \infty)$.",
], ["c2-ex-distance-to-set", "c2-cor-function-arithmetic", "c2-thm-open-set-condition", "c2-prop-closure-lim"])

# ---------------------------------------------------------------- cluster points

ex("c2-ex-cluster-set-closed", "The set of cluster points is closed", r"""
Let $S$ be a subset of a metric space $M$. Show that $S'$, the set of cluster points of $S$, is a closed subset of $M$, and that $(\overline{S})' = S'$.
""", r"""
\emph{$S'$ is closed.} Let $p$ be a limit of $S'$; we show $p \in S'$. Let $r > 0$. By the lemma on limits and neighborhoods, $M_{r/2}(p)$ contains a point $q \in S'$. If $x \in M_{r/2}(q)$ then $d(x,p) \le d(x,q) + d(q,p) < r$, so $M_{r/2}(q) \subset M_r(p)$. Since $q$ is a cluster point of $S$, $M_{r/2}(q)$ contains infinitely many points of $S$, hence so does $M_r(p)$. As $r$ was arbitrary, $p \in S'$. So $S'$ contains all its limits and is closed.

\emph{$(\overline{S})' = S'$.} Since $S \subset \overline{S}$, a neighborhood containing infinitely many points of $S$ contains infinitely many points of $\overline{S}$; so $S' \subset (\overline{S})'$. Conversely let $p \in (\overline{S})'$ and $r > 0$. By the four descriptions of a cluster point, $M_{r/2}(p)$ contains a point $q \in \overline{S}$ with $q \ne p$. Put $s = \min\set{r/2,\ d(q,p)} > 0$. Since $\overline{S}$ is the limit set of $S$, the neighborhood $M_s(q)$ contains a point $x \in S$. Then $d(x,p) \le d(x,q) + d(q,p) < r/2 + r/2 = r$, and $x \ne p$ because $d(x,q) < d(q,p)$. So every neighborhood of $p$ contains a point of $S$ other than $p$, and by the four descriptions again $p \in S'$.
""", 2, 20, [
    r"A ball of radius $r/2$ about a point of $S'$ lying within $r/2$ of $p$ sits inside the ball of radius $r$ about $p$.",
    r"For $(\overline{S})' \subset S'$, use description (4) of a cluster point: find a point of $S$ other than $p$ in each neighborhood of $p$ by going through a point of $\overline{S}$ other than $p$.",
], ["c2-def-cluster-point", "c2-lem-limit-ball", "c2-def-closed-open", "c2-thm-cluster-equivalents", "c2-prop-closure-lim", "c2-prop-closure-cluster"])

ex("c2-ex-condensation-point", "An uncountable set on the line has condensation points", r"""
Let $S \subset \R$ be uncountable. Show that the set $T$ of points of $S$ that are not condensation points of $S$ is countable. Hence all but countably many points of $S$ are condensation points of $S$; in particular $S$ has a condensation point.
""", r"""
Let $x \in T$. Since $x$ is not a condensation point of $S$, some neighborhood $(x - r_x, x + r_x)$ contains only countably many points of $S$. Every interval contains a rational number, so we can choose rationals $q_x, q'_x$ with
\[ x - r_x < q_x < x < q'_x < x + r_x . \]
Then $x \in (q_x, q'_x)$, and $S \cap (q_x, q'_x) \subset S \cap (x - r_x, x + r_x)$ is countable.

Let $P = \set{(q_x, q'_x) : x \in T}$. It is a subset of $\Q \times \Q$, which is countable, so $P$ is countable. Each $x \in T$ lies in $S \cap (q_x, q'_x)$, hence
\[ T \subset \bigcup_{(q,q') \in P} S \cap (q,q') , \]
a countable union of countable sets, which is countable. So $T$ is countable.

If every point of $S$ were in $T$, then $S = T$ would be countable, contrary to hypothesis. So some point of $S$ is a condensation point of $S$; indeed $S \setminus T$ is uncountable, since otherwise $S = T \cup (S \setminus T)$ would be countable.
""", 3, 30, [
    r"Each point of $S$ that is not a condensation point sits in an open interval with rational endpoints that holds only countably many points of $S$.",
    r"There are only countably many intervals with rational endpoints.",
], ["c2-def-cluster-point", "c2-ex-closure-examples"])

# ---------------------------------------------------------------- compactness

ex("c2-ex-convergent-sequence-compact", "A convergent sequence with its limit is compact", r"""
Let $p_n \to p$ in a metric space $M$. Show that $S = \set{p} \cup \set{p_n : n \in \N}$ is a compact subset of $M$. (Try it with the covering definition.)
""", r"""
Let $\mathcal{U}$ be an open covering of $S$. Since $p \in S$ there is a member $U_0 \in \mathcal{U}$ with $p \in U_0$, and since $U_0$ is open there is an $r > 0$ with $M_r(p) \subset U_0$. As $p_n \to p$ there is an $N$ with $d(p_n,p) < r$, hence $p_n \in U_0$, for all $n \ge N$. For each of the finitely many indices $n < N$ choose $U_n \in \mathcal{U}$ with $p_n \in U_n$. Then the finitely many sets $U_0, U_1, \dots, U_{N-1}$ cover $S$: $U_0$ contains $p$ and every $p_n$ with $n \ge N$, and $U_n$ contains $p_n$ for $n < N$. So every open covering of $S$ reduces to a finite subcovering: $S$ is covering compact, and therefore sequentially compact.
""", 1, 10, [
    r"One member of the covering contains the limit, and with it all but finitely many terms.",
], ["c2-def-covering", "c2-def-closed-open", "c2-def-convergence", "c2-thm-covering-implies-sequential"])

ex("c2-ex-unions-intersections-compact", "Unions and intersections of compact sets", r"""
Let $M$ be a metric space.
\begin{enumerate}
\item Show that the union of finitely many compact subsets of $M$ is compact.
\item Show that the intersection of any nonempty collection of compact subsets of $M$ is compact.
\item Prove or disprove: the union of any collection of compact subsets of $M$ is compact.
\end{enumerate}
""", r"""
(1) By induction on the number of sets it suffices to treat two compact sets $A$ and $B$. Let $(x_n)$ be a sequence in $A \cup B$. The index sets $\set{n : x_n \in A}$ and $\set{n : x_n \in B}$ have union $\N$, so one of them is infinite; say the first (the other case is the same with $B$). Listing it in increasing order as $n_1 < n_2 < \cdots$ gives a subsequence $(x_{n_k})$ lying in $A$. By compactness of $A$ it has a subsequence converging to a point of $A \subset A \cup B$, and a subsequence of a subsequence of $(x_n)$ is a subsequence of $(x_n)$. So $A \cup B$ is compact.

(2) Let $\set{A_\alpha}$ be a nonempty collection of compact sets and $A = \bigcap_\alpha A_\alpha$. Compact sets are closed, so $A$ is an intersection of closed sets and is closed in $M$. Fix one index $\beta$. Then $A$ is a closed subset of $M$ contained in the compact set $A_\beta$, so $A$ is compact because closed subsets of compact sets are compact.

(3) False. Each one-point set $\set{n} \subset \R$ is compact (finite sets are compact), but their union $\N$ is not bounded in $\R$, and compact sets are bounded. So $\N$ is not compact.
""", 2, 15, [
    r"For (1), one of the two sets contains infinitely many terms of the sequence.",
    r"For (2), compact sets are closed, and a closed subset of a compact set is compact.",
    r"For (3), every one-point set is compact.",
], ["c2-def-compact", "c2-def-subsequence", "c2-thm-compact-closed-bounded", "c2-cor-closed-sets", "c2-thm-closed-in-compact", "c2-rem-compact-intrinsic"])

ex("c2-ex-infinite-subset-cluster", "Compactness through cluster points", r"""
Show that a metric space $M$ is compact if and only if every infinite subset of $M$ has a cluster point in $M$.
""", r"""
\emph{Compact implies the cluster point property.} Let $S \subset M$ be infinite. Choose distinct points $s_1, s_2, s_3, \dots$ of $S$ recursively: having chosen $s_1, \dots, s_n$, the set $S \setminus \set{s_1, \dots, s_n}$ is nonempty because $S$ is infinite, and $s_{n+1}$ is any of its points. By compactness some subsequence $(s_{n_k})$ converges to a point $p \in M$. Its terms are distinct points of $S$, so by the four descriptions of a cluster point (a sequence of distinct points of $S$ converging to $p$) $p$ is a cluster point of $S$.

\emph{The cluster point property implies compact.} Let $(a_n)$ be a sequence in $M$ and let $T = \set{a_n : n \in \N}$ be its set of terms.

If $T$ is finite, then $\N = \bigcup_{t \in T} \set{n : a_n = t}$ is a finite union, so for some $t \in T$ the index set $\set{n : a_n = t}$ is infinite; listing it in increasing order gives a constant subsequence, which converges to $t \in M$.

If $T$ is infinite, it has a cluster point $p \in M$ by hypothesis. Let $r > 0$. The neighborhood $M_r(p)$ contains infinitely many points of $T$; each of them is $a_n$ for at least one $n$, and distinct points have distinct indices, so $a_n \in M_r(p)$ for infinitely many $n$. By the lemma on extracting a convergent subsequence, $(a_n)$ has a subsequence converging to $p$.

In both cases $(a_n)$ has a subsequence converging in $M$, so $M$ is compact.
""", 3, 30, [
    r"An infinite set contains a sequence of distinct points. Where does a convergent subsequence of it take you?",
    r"For the converse, split according to whether the sequence takes finitely or infinitely many distinct values.",
    r"Infinitely many points of the set of terms in a ball means infinitely many indices in that ball; then use the lemma on extracting a convergent subsequence.",
], ["c2-def-compact", "c2-def-cluster-point", "c2-thm-cluster-equivalents", "c2-lem-cluster-subsequence", "c2-def-subsequence"])

ex("c2-ex-compact-closed-distance", "A compact set keeps its distance from a disjoint closed set", r"""
Let $A$ and $B$ be disjoint nonempty subsets of a metric space $M$, with $A$ compact and $B$ closed. Show that there is a $\delta > 0$ with $d(a,b) \ge \delta$ for all $a \in A$ and $b \in B$. Prove or disprove: the same holds when $A$ and $B$ are both closed and disjoint.
""", r"""
Suppose no such $\delta$ exists. Then for each $n \in \N$ the number $1/n$ fails, so there are $a_n \in A$ and $b_n \in B$ with $d(a_n,b_n) < 1/n$. By compactness a subsequence $(a_{n_k})$ converges to some $a \in A$. Then
\[ d(b_{n_k}, a) \le d(b_{n_k}, a_{n_k}) + d(a_{n_k}, a) < \frac{1}{n_k} + d(a_{n_k}, a) \to 0 , \]
so $b_{n_k} \to a$. Thus $a$ is a limit of $B$, and since $B$ is closed, $a \in B$. This contradicts $A \cap B = \varnothing$. Hence some $\delta > 0$ works.

For two closed sets the statement is false. In $\R^2$ let
\[ A = \set{(x,y) : y = 0}, \qquad B = \set{(x,y) : xy = 1} . \]
The map $(x,y) \mapsto y$ is continuous, since convergence in $\R^2$ is componentwise, and $(x,y) \mapsto xy$ is continuous because arithmetic is continuous. One-point sets $\set{0}$ and $\set{1}$ are closed in $\R$ (they are closed balls of radius $0$), so by the closed set condition for continuity $A$ and $B$ are closed in $\R^2$. They are disjoint, since $y = 0$ gives $xy = 0 \ne 1$, and nonempty. But $(n, 0) \in A$ and $(n, 1/n) \in B$ are at distance $1/n$, so no $\delta > 0$ works.
""", 3, 30, [
    r"If no $\delta$ works you can pick $a_n$ and $b_n$ within $1/n$ of each other. Use compactness of $A$.",
    r"For the counterexample, a hyperbola and its asymptote.",
], ["c2-def-compact", "c2-def-closed-open", "c2-thm-open-set-condition", "c2-thm-arithmetic-continuous", "c2-cor-rm-convergence", "c2-ex-closed-ball"])

ex("c2-ex-isometry-onto", "An isometry of a compact space is onto", r"""
Let $M$ be a compact metric space and $f : M \to M$ an \emph{isometry}: $d(f(x), f(y)) = d(x,y)$ for all $x, y \in M$. Show that $f$ is onto, and hence a homeomorphism of $M$ onto itself. Show by example that compactness cannot be dropped.
""", r"""
Given $\eps > 0$, $\delta = \eps$ works in the $\eps,\delta$ condition, so $f$ is continuous. It is also one-to-one: $f(x) = f(y)$ gives $d(x,y) = d(f(x),f(y)) = 0$, so $x = y$.

Suppose some $p \in M$ is not in $f(M)$. The set $f(M)$ is the continuous image of a compact set, hence compact, hence closed in $M$. As $p \notin f(M)$, $p$ is not a limit of $f(M)$, and by the lemma on limits and neighborhoods there is an $r > 0$ with $M_r(p) \cap f(M) = \varnothing$: every point of $f(M)$ is at distance at least $r$ from $p$.

Define $p_0 = p$ and $p_{n+1} = f(p_n)$, so that $p_n \in f(M)$ for all $n \ge 1$. We claim that $d(p_m, p_n) \ge r$ whenever $m < n$, by induction on $m$. For $m = 0$: $p_n \in f(M)$, so $d(p_0, p_n) \ge r$. If the claim holds for $m$ and all $n > m$, then for $n > m$,
\[ d(p_{m+1}, p_{n+1}) = d(f(p_m), f(p_n)) = d(p_m, p_n) \ge r , \]
and every index larger than $m+1$ has the form $n+1$ with $n > m$; so the claim holds for $m+1$.

Thus any two distinct terms of $(p_n)$ are at distance at least $r$. No subsequence of $(p_n)$ is Cauchy, so no subsequence converges, because convergent sequences are Cauchy. This contradicts the compactness of $M$. Hence $f$ is onto.

So $f$ is a continuous bijection of the compact space $M$ onto $M$, and a continuous bijection from a compact space is a homeomorphism.

\emph{Compactness is needed.} On $\N \subset \R$ the map $f(n) = n + 1$ satisfies $\abs{f(m) - f(n)} = \abs{m - n}$, so it is an isometry, but $1$ is not in its image.
""", 4, 50, [
    r"If $p$ is missed, the compact set $f(M)$ stays at some positive distance $r$ from $p$.",
    r"Follow the orbit $p, f(p), f(f(p)), \dots$ and apply the isometry $m$ times to compare its $m$-th and $n$-th terms.",
    r"A sequence whose terms are pairwise at least $r$ apart has no convergent subsequence.",
], ["c2-def-compact", "c2-thm-eps-delta", "c2-thm-continuous-image-compact", "c2-thm-compact-closed-bounded", "c2-lem-limit-ball", "c2-prop-convergent-cauchy", "c2-thm-compact-homeomorphism", "c2-def-homeomorphism"])

ex("c2-ex-compact-separable", "A compact space has a countable dense subset", r"""
Let $M$ be a compact metric space. Show that $M$ has a countable subset $D$ with $\overline{D} = M$. Deduce that $M$ has at most countably many isolated points.
""", r"""
Compact sets are totally bounded, so for each $n \in \N$ there is a finite set $F_n \subset M$ with
\[ M = \bigcup_{s \in F_n} M_{1/n}(s) . \]
Let $D = \bigcup_n F_n$, a countable union of finite sets, hence countable.

$D$ is dense: let $x \in M$ and $r > 0$. Choose $n$ with $1/n < r$. Then $x \in M_{1/n}(s)$ for some $s \in F_n \subset D$, so $d(x,s) < r$ and $M_r(x)$ contains a point of $D$. Every neighborhood of $x$ meets $D$, so by the lemma on limits and neighborhoods $x$ is a limit of $D$, and since the closure is the limit set, $x \in \overline{D}$. Thus $\overline{D} = M$.

Isolated points: if $p \in M$ is isolated, there is an $r > 0$ with $M_r(p) = \set{p}$. This neighborhood contains a point of $D$, as just shown, so $p \in D$. Hence the set of isolated points is a subset of the countable set $D$, and is countable.
""", 2, 20, [
    r"Total boundedness hands you finitely many centers for each $\eps = 1/n$. Collect them all.",
    r"An isolated point's small neighborhood must still contain a point of the dense set.",
], ["c2-lem-compact-totally-bounded", "c2-def-totally-bounded", "c2-lem-limit-ball", "c2-prop-closure-lim", "c2-ex-closure-examples", "c2-def-perfect"])

ex("c2-ex-uniform-continuity-cauchy", "Which maps preserve Cauchy sequences?", r"""
Let $f : M \to N$ be a map of metric spaces.
\begin{enumerate}
\item Show that if $f$ is uniformly continuous and $(p_n)$ is a Cauchy sequence in $M$, then $(f(p_n))$ is a Cauchy sequence in $N$.
\item Prove or disprove: the same holds if $f$ is merely continuous.
\item Suppose $f$ is a bijection and both $f$ and $f^{-1}$ are uniformly continuous. Show that $M$ is complete if and only if $N$ is. (Compare: $\R$ and $(-1,1)$ are homeomorphic, and only one of them is complete.)
\end{enumerate}
""", r"""
(1) Let $\eps > 0$. Uniform continuity gives a $\delta > 0$ such that $d_M(x,y) < \delta$ implies $d_N(f(x),f(y)) < \eps$, for all $x, y \in M$. Since $(p_n)$ is Cauchy there is an $N$ with $d_M(p_m,p_n) < \delta$ for all $m, n \ge N$, and then $d_N(f(p_m), f(p_n)) < \eps$ for all $m, n \ge N$. So $(f(p_n))$ is Cauchy.

(2) False. Let $M = (0,1] \subset \R$ and $f(x) = 1/x$. The function $x \mapsto x$ is continuous and nonvanishing on $M$, so $f$ is continuous as a quotient of continuous functions. The sequence $p_n = 1/n$ converges to $0$ in $\R$, hence is Cauchy in $\R$, hence is Cauchy in the subspace $(0,1]$, where the distances are the same. But $f(p_n) = n$, and $\abs{f(p_m) - f(p_n)} \ge 1$ for $m \ne n$, so $(f(p_n))$ is not Cauchy.

(3) Suppose $M$ is complete and let $(q_n)$ be a Cauchy sequence in $N$. By (1) applied to $f^{-1}$, the sequence $p_n = f^{-1}(q_n)$ is Cauchy in $M$, so it converges to some $p \in M$. A uniformly continuous map satisfies the $\eps,\delta$ condition, so $f$ is continuous, and therefore $q_n = f(p_n) \to f(p)$. Thus every Cauchy sequence in $N$ converges, and $N$ is complete. The converse follows by exchanging the roles of $f$ and $f^{-1}$.
""", 2, 25, [
    r"In (1), the $\delta$ of uniform continuity does not depend on the point, so a single $N$ serves for the whole tail.",
    r"For (2), try $1/x$ on $(0,1]$.",
    r"For (3), carry a Cauchy sequence across by $f^{-1}$, let it converge, and bring the limit back by $f$.",
], ["c2-def-uniform-continuity", "c2-def-cauchy", "c2-def-continuity", "c2-thm-eps-delta", "c2-cor-function-arithmetic", "c2-prop-convergent-cauchy", "c2-ex-incomplete", "c2-ex-r-homeo-interval"])

# ---------------------------------------------------------------- connectedness

ex("c2-ex-countable-disconnected", "A countable metric space is totally disconnected", r"""
Show that every countable metric space $M$ is totally disconnected. In particular, a countable metric space with at least two points is disconnected.
""", r"""
Let $p \in M$ and $\eps > 0$. The set of distances $\set{d(x,p) : x \in M}$ is the image of the countable set $M$ under a function, so it is countable. The interval $(0,\eps)$ is uncountable, since it contains $[\eps/3, 2\eps/3]$ and every nondegenerate closed interval is uncountable. Hence there is an $r \in (0,\eps)$ that is not of the form $d(x,p)$ for any $x \in M$.

Let $U = M_r(p)$. It is open, since neighborhoods are open. Because no point is at distance exactly $r$ from $p$,
\[ U = \set{x : d(x,p) < r} = \set{x : d(x,p) \le r} = D_r(p) , \]
and closed balls are closed. So $U$ is clopen, $p \in U$, and $U \subset M_\eps(p)$ because $r < \eps$. This is what it means for $M$ to be totally disconnected.

If $M$ has two distinct points $p$ and $q$, apply this with $\eps = d(p,q)$: the clopen set $U$ contains $p$ and not $q$ (as $d(q,p) = \eps > r$), so $U$ is a proper clopen subset and $M$ is disconnected.
""", 3, 30, [
    r"Only countably many distances $d(x,p)$ occur. Pick a radius that is not one of them.",
    r"A ball whose radius is not a distance from the center is also a closed ball.",
], ["c2-def-totally-disconnected", "c2-def-connected", "c2-prop-ball-open", "c2-ex-closed-ball", "c2-cor-everywhere-uncountable", "c2-def-metric-space"])

ex("c2-ex-interior-not-connected", "Is the interior of a connected set connected?", r"""
The closure of a connected set is connected. Prove or disprove: the interior of a connected subset of a metric space is connected.
""", r"""
False. In $\R^2$ let $S = \set{(x,y) : xy \ge 0}$.

\emph{$S$ is connected.} Let $Q_1 = \set{(x,y) : x \ge 0,\ y \ge 0}$ and $Q_3 = \set{(x,y) : x \le 0,\ y \le 0}$. If $xy \ge 0$ then $x$ and $y$ are both $\ge 0$ or both $\le 0$, so $S = Q_1 \cup Q_3$. Each quadrant is convex: for $u, v \in Q_1$ and $0 \le t \le 1$ the coordinates of $(1-t)u + tv$ are sums of nonnegative numbers, and similarly for $Q_3$ with nonpositive numbers. Convex sets are connected, and both quadrants contain the origin, so their union $S$ is connected.

\emph{The interior of $S$ is $W = \set{(x,y) : xy > 0}$.} The map $m(x,y) = xy$ is continuous because arithmetic is continuous, and the ray $(0,\infty)$ is open in $\R$, so $W = m^{-1}((0,\infty))$ is open. As $W \subset S$, $W \subset \interior S$. Conversely let $q = (a,b) \in S \setminus W$, so $ab = 0$. We produce points $q_n \notin S$ with $q_n \to q$. If $a = 0$, let $\sigma = 1$ when $b \ge 0$ and $\sigma = -1$ when $b < 0$, and put $q_n = (-\sigma/n,\ b + \sigma/n)$; the product of its coordinates is $-\sigma b/n - 1/n^2 = -\abs{b}/n - 1/n^2 < 0$. If $a \ne 0$ (so $b = 0$), let $\sigma$ be the sign of $a$ and put $q_n = (a, -\sigma/n)$; the product is $-\abs{a}/n < 0$. In both cases $q_n \notin S$, and $q_n \to q$ because convergence in $\R^2$ is componentwise. So every neighborhood of $q$ contains a point outside $S$, no neighborhood of $q$ lies in $S$, and $q \notin \interior S$. Hence $\interior S = W$.

\emph{$W$ is disconnected.} Let $W_+ = \set{(x,y) \in W : x > 0}$ and $W_- = \set{(x,y) \in W : x < 0}$. A point of $W$ has $x \ne 0$, so $W = W_+ \sqcup W_-$, and both parts are nonempty: $(1,1) \in W_+$, $(-1,-1) \in W_-$. The projection $\pi(x,y) = x$ is continuous (convergence in $\R^2$ is componentwise), so $\pi^{-1}((0,\infty))$ and $\pi^{-1}((-\infty,0))$ are open in $\R^2$, and $W_\pm$ are their intersections with $W$, open in $W$ by the inheritance principle. Thus $W$ splits into two disjoint nonempty open sets, and is disconnected.
""", 3, 35, [
    r"Two closed quadrants touching at the origin.",
    r"The interior is $\set{xy > 0}$: show that no point with $xy = 0$ is interior by approaching it from outside.",
    r"$\set{xy > 0}$ splits by the sign of $x$.",
], ["c2-def-connected", "c2-cor-convex-connected", "c2-thm-union-connected", "c2-prop-interior", "c2-thm-open-set-condition", "c2-thm-arithmetic-continuous", "c2-cor-rm-convergence", "c2-thm-inheritance", "c2-thm-closure-connected"])

ex("c2-ex-plane-minus-point", r"$\R$ and $\R^2$ are not homeomorphic", r"""
Show that $\R^2 \setminus \set{p}$ is path-connected for every $p \in \R^2$. Deduce that $\R$ is not homeomorphic to $\R^2$.
""", r"""
For $u, v \in \R^2$ the straight path $g(t) = (1-t)u + tv$, $0 \le t \le 1$, is continuous: $\abs{g(t) - g(s)} = \abs{t - s}\,\abs{v - u}$, so $t_n \to t$ implies $g(t_n) \to g(t)$. Write $[u,v]$ for its image, the segment from $u$ to $v$.

Let $x, y \in \R^2 \setminus \set{p}$. If $p \notin [x,y]$, the straight path from $x$ to $y$ takes its values in $\R^2 \setminus \set{p}$; since convergence in the subspace is convergence in $\R^2$, it is a path in $\R^2 \setminus \set{p}$ from $x$ to $y$.

Otherwise $p = (1 - t_0)x + t_0 y$ for some $t_0 \in [0,1]$, and $0 < t_0 < 1$ since $p \ne x, y$; in particular $x \ne y$ and $p - x = t_0 (y - x)$. Let $w = (-(y_2 - x_2),\ y_1 - x_1)$, so that $\inner{w}{y - x} = 0$ and $\abs{w} = \abs{y - x} > 0$, and put $z = x + w$. We check that $p$ lies on neither $[x,z]$ nor $[z,y]$. If $p = (1-s)x + sz = x + sw$ with $s \in [0,1]$, then $sw = t_0(y-x)$; taking the inner product with $y - x$ gives $0 = t_0 \abs{y-x}^2$, so $t_0 = 0$, a contradiction. If $p = (1-s)z + sy = x + s(y-x) + (1-s)w$ with $s \in [0,1]$, then $(t_0 - s)(y - x) = (1-s) w$; taking the inner product with $w$ gives $0 = (1-s)\abs{w}^2$, so $s = 1$ and $p = y$, a contradiction.

Define $g : [0,2] \to \R^2$ by $g(t) = (1-t)x + tz$ for $0 \le t \le 1$ and $g(t) = (2-t)z + (t-1)y$ for $1 \le t \le 2$; the two formulas agree at $t = 1$. Its values lie in $[x,z] \cup [z,y]$, which avoids $p$, and $g(0) = x$, $g(2) = y$. Let $K = \max\set{\abs{z - x}, \abs{y - z}}$. If $s, t$ lie in the same piece, $\abs{g(t) - g(s)} \le K \abs{t - s}$ by the computation above; if $s \le 1 \le t$, then $\abs{g(t) - g(s)} \le \abs{g(t) - g(1)} + \abs{g(1) - g(s)} \le K(t-1) + K(1-s) = K\abs{t-s}$. So $\abs{g(t) - g(s)} \le K\abs{t-s}$ for all $s, t$, and $g$ is continuous. Hence $g$ is a path in $\R^2 \setminus \set{p}$ from $x$ to $y$, and $\R^2 \setminus \set{p}$ is path-connected.

\emph{$\R \not\cong \R^2$.} Suppose $h : \R \to \R^2$ is a homeomorphism, and let $p = h(0)$. Then $h$ restricts to a bijection $h_0 : \R \setminus \set{0} \to \R^2 \setminus \set{p}$. A restriction of a continuous map to a subspace is continuous, because convergence in a subspace is convergence in the whole space; so $h_0$ and its inverse, the restriction of $h^{-1}$, are continuous, and $h_0$ is a homeomorphism. Now $\R^2 \setminus \set{p}$ is path-connected, hence connected, so its continuous image $\R \setminus \set{0}$ under $h_0^{-1}$ is connected. But $\R \setminus \set{0}$ is not an interval ($-1$ and $1$ belong to it and $0$ does not), so it is disconnected. This contradiction shows no such $h$ exists.
""", 3, 40, [
    r"If the segment from $x$ to $y$ passes through $p$, go around through a point $z$ off the line through $x$ and $y$.",
    r"To glue two straight paths, define one map on $[0,2]$ and check it is Lipschitz.",
    r"A homeomorphism $\R \to \R^2$ would restrict to one from $\R \setminus \set{0}$ onto the plane minus a point.",
], ["c2-def-path-connected", "c2-thm-path-connected", "c2-def-homeomorphism", "c2-thm-connected-image", "c2-cor-connected-subsets-of-r", "c2-def-continuity", "c2-rem-topological-invariant", "c2-cor-convex-connected"])

ex("c2-ex-open-sets-of-r", "The open subsets of the line", r"""
Show that every nonempty open set $U \subset \R$ is the union of a countable collection of pairwise disjoint open intervals $(a,b)$, where $-\infty \le a < b \le \infty$.
""", r"""
For $x \in U$ let $I_x$ be the union of all connected subsets of $\R$ that contain $x$ and are contained in $U$. The collection is nonempty, since $\set{x}$ is connected (it has no proper subset at all). As a union of connected sets with the common point $x$, $I_x$ is connected, so it is an interval; and $x \in I_x \subset U$.

\emph{Each $I_x$ is open.} Let $y \in I_x$. Since $y \in U$ and $U$ is open, $(y - r, y + r) \subset U$ for some $r > 0$. The interval $(y-r,y+r)$ is connected, and it shares the point $y$ with $I_x$, so $I_x \cup (y-r,y+r)$ is connected, contains $x$, and lies in $U$. By the definition of $I_x$ it is contained in $I_x$. So $(y-r,y+r) \subset I_x$.

\emph{Two of them are equal or disjoint.} Let $x, x' \in U$ and suppose $I_x \cap I_{x'}$ contains a point $y$. Then $I_x \cup I_{x'}$ is connected (common point $y$), contains $x$, and lies in $U$, so it is contained in $I_x$; hence $I_{x'} \subset I_x$. By symmetry $I_x \subset I_{x'}$, so $I_x = I_{x'}$.

\emph{Countably many.} Let $\mathcal{I}$ be the set of distinct sets among the $I_x$, $x \in U$; they are pairwise disjoint, and their union is $U$ because $x \in I_x$. Each $I \in \mathcal{I}$ is a nonempty open set, so it contains some interval $(y-r,y+r)$, which contains a rational number; choose one and call it $q(I)$. Since the members of $\mathcal{I}$ are pairwise disjoint, $q : \mathcal{I} \to \Q$ is one-to-one, and as $\Q$ is countable so is $\mathcal{I}$.

\emph{Each is an open interval.} Let $I \in \mathcal{I}$; it is a nonempty, open, connected subset of $\R$. Let $a = \glb I$ if $I$ is bounded below and $a = -\infty$ otherwise, and $b = \lub I$ if $I$ is bounded above and $b = \infty$ otherwise. If $a < y < b$, then $y$ is neither a lower nor an upper bound of $I$, so there are $u, v \in I$ with $u < y < v$, and $y \in I$ because $I$ is an interval; thus $(a,b) \subset I$. Conversely every point of $I$ lies in $[a,b]$, and $a \notin I$: if $a \in I$ (so $a$ is finite), openness would give $(a - r, a + r) \subset I$, contradicting that $a$ is a lower bound of $I$. Likewise $b \notin I$. So $I = (a,b)$, and $a < b$ because $I$ is nonempty (if $a = b$ then $I \subset [a,b] \setminus \set{a} = \varnothing$).
""", 3, 45, [
    r"For $x \in U$, take the union of all connected subsets of $U$ containing $x$; it is connected, hence an interval.",
    r"Show each such interval is open, and that two of them are either equal or disjoint.",
    r"Each of the disjoint open intervals contains its own rational number.",
], ["c2-def-closed-open", "c2-thm-union-connected", "c2-cor-connected-subsets-of-r", "c2-thm-intervals-connected", "c2-ex-closure-examples", "c2-def-connected"])

# ---------------------------------------------------------------- zero sets and the Cantor set

ex("c2-ex-interval-not-zero-set", "An interval is not a zero set", r"""
Let $a < b$. Show that if finitely many open intervals cover $[a,b]$, then the sum of their lengths exceeds $b - a$. Deduce that $[a,b]$ is not a zero set, and that a zero set contains no interval $(c,d)$ with $c < d$.
""", r"""
\emph{Finitely many intervals.} We prove by induction on $k \ge 0$: if $k$ open intervals $(a_1,b_1), \dots, (a_k,b_k)$ cover a closed interval $[a,b]$ with $a \le b$, then $\sum_{i=1}^k (b_i - a_i) > b - a$. For $k = 0$ the statement holds vacuously, since no collection of zero sets covers the nonempty set $[a,b]$. Let $k \ge 1$ and assume the statement for $k - 1$. The point $b$ lies in one of the intervals; renumber so that $b \in (a_k, b_k)$. If $a_k < a$, then $b_k - a_k > b - a$ already, and the other lengths are nonnegative. If $a_k \ge a$, then $a \le a_k < b$, so $[a, a_k]$ is a nonempty closed interval. Every point $t$ of it lies in $[a,b]$, hence in some $(a_i,b_i)$, and $i \ne k$ because $t \le a_k$; so the $k-1$ intervals other than $(a_k,b_k)$ cover $[a,a_k]$, and by the induction hypothesis $\sum_{i < k} (b_i - a_i) > a_k - a$. Since $b_k > b$, also $b_k - a_k > b - a_k$. Adding, $\sum_{i \le k} (b_i - a_i) > b - a$.

\emph{$[a,b]$ is not a zero set.} Suppose it were, and take $\eps = (b-a)/2$: there is a countable collection of open intervals $(a_i,b_i)$ covering $[a,b]$ with $\sum_i (b_i - a_i) \le (b-a)/2$. Each $(a_i,b_i)$ is an open subset of $\R$, since a point $t$ of it has $(t - r, t + r) \subset (a_i,b_i)$ for $r = \min\set{t - a_i,\ b_i - t}$. The interval $[a,b]$ is compact, hence covering compact, so finitely many of the $(a_i,b_i)$ already cover $[a,b]$. Their total length is at most $\sum_i (b_i - a_i)$, because the lengths are nonnegative and a finite partial sum of a series with nonnegative terms is at most its sum. So finitely many open intervals of total length at most $(b-a)/2 < b - a$ cover $[a,b]$, contradicting the first part.

\emph{A zero set contains no interval.} A subset of a zero set $Z$ is a zero set, since any collection of intervals covering $Z$ covers the subset. If $(c,d) \subset Z$ with $c < d$, then the closed interval $[c + (d-c)/3,\ d - (d-c)/3] \subset (c,d)$ would be a zero set, which was just excluded.
""", 4, 60, [
    r"For finitely many intervals, induct on their number: the interval containing $b$ either reaches past $a$, or leaves a shorter closed interval $[a, a_k]$ for the others to cover.",
    r"Compactness of $[a,b]$ turns a countable covering into a finite one.",
    r"A subset of a zero set is a zero set.",
], ["c2-def-zero-set", "c2-thm-interval-compact", "c2-thm-sequential-implies-covering", "c2-def-covering", "c2-def-closed-open"])

ex("c2-ex-cantor-sum", r"$C + C = [0,2]$", r"""
Show that $C + C = \set{x + y : x, y \in C}$ is all of $[0,2]$. (Compare with the previous exercise: the sum of two zero sets can be an interval.)
""", r"""
Since $C \subset [0,1]$, every sum $x + y$ with $x, y \in C$ lies in $[0,2]$. For the converse let $t \in [0,2]$ and put $x = t/2 \in [0,1]$; we find $a, b \in C$ with $a + b = 2x = t$.

\emph{A base-$3$ expansion of $x$.} We choose digits $d_1, d_2, \dots \in \set{0,1,2}$ recursively so that the partial sums $s_n = \sum_{i=1}^n d_i 3^{-i}$ satisfy $s_n \le x \le s_n + 3^{-n}$ for all $n \ge 0$. For $n = 0$, $s_0 = 0 \le x \le 1$. Given $s_n$ with $x \in [s_n, s_n + 3^{-n}]$, put $h = 3^{-(n+1)}$; the three closed intervals $[s_n + jh,\ s_n + (j+1)h]$, $j = 0, 1, 2$, have union $[s_n, s_n + 3h] = [s_n, s_n + 3^{-n}]$, so $x$ lies in one of them. Let $d_{n+1}$ be such a $j$. Then $s_{n+1} = s_n + d_{n+1} h$ and $s_{n+1} \le x \le s_{n+1} + h$, as required. Consequently $\abs{x - s_n} \le 3^{-n} \le 1/n$ for $n \ge 1$, so $s_n \to x$.

\emph{Two addresses.} Define letters $\alpha_i, \beta_i \in \set{0,2}$ by
\[ (\alpha_i, \beta_i) = (0,0) \text{ if } d_i = 0, \qquad (0,2) \text{ if } d_i = 1, \qquad (2,2) \text{ if } d_i = 2 , \]
so that $\alpha_i + \beta_i = 2 d_i$ for every $i$. Then $\alpha = \alpha_1\alpha_2\dots$ and $\beta = \beta_1\beta_2\dots$ are addresses, and by the theorem on addresses the series $\sum_i \alpha_i 3^{-i}$ and $\sum_i \beta_i 3^{-i}$ converge to points $a = p(\alpha)$ and $b = p(\beta)$ of $C$.

\emph{They add up.} The partial sums satisfy
\[ \sum_{i=1}^n \alpha_i 3^{-i} + \sum_{i=1}^n \beta_i 3^{-i} = \sum_{i=1}^n 2 d_i 3^{-i} = 2 s_n . \]
As $n \to \infty$ the left side converges to $a + b$, since the limit of a sum of two convergent sequences is the sum of their limits, and the right side converges to $2x = t$. Limits are unique, so $a + b = t$. Hence $t \in C + C$.
""", 4, 60, [
    r"It is enough to write every $x \in [0,1]$ as $(a+b)/2$ with $a, b \in C$.",
    r"Give $x$ a base-$3$ expansion with digits $0,1,2$ by nested intervals of length $3^{-n}$; then split each digit $1$ as $(0+2)/2$.",
    r"Addresses name points of $C$. Add the two series term by term.",
], ["c2-thm-addresses", "c2-def-address", "c2-def-cantor-set", "c2-thm-arithmetic-continuous", "c2-thm-limit-unique", "c2-thm-cantor-zero-set", "c2-ex-interval-not-zero-set"])

ex("c2-ex-endpoint-addresses", "Endpoints are the points with eventually constant addresses", r"""
Call an address $\omega$ \emph{eventually constant} if there is an $n$ with $\omega_i = \omega_{n+1}$ for all $i > n$. Show that a point $x \in C$ is an endpoint of one of the intervals of some $C^n$ if and only if its address is eventually constant. Conclude that the set $E$ of endpoints is countable and that $C \setminus E$ is uncountable.
""", r"""
Recall from the proof of the theorem on addresses that $\sum_{i=n+1}^m 2 \cdot 3^{-i} = 3^{-n} - 3^{-m}$ for $n < m$; letting $m \to \infty$, the tail $\sum_{i > n} 2 \cdot 3^{-i}$ converges to $3^{-n}$.

Let $\alpha$ be a word of length $n$. The address $\alpha 000\dots$ has $p(\alpha 000 \dots) = \sum_{i \le n} \alpha_i 3^{-i} = a_\alpha$, the left endpoint of $C_\alpha$. The address $\alpha 222 \dots$ has
\[ p(\alpha 222 \dots) = a_\alpha + \sum_{i > n} 2 \cdot 3^{-i} = a_\alpha + 3^{-n} , \]
the right endpoint of $C_\alpha$.

\emph{Endpoints have eventually constant addresses.} The intervals of $C^n$ are exactly the $C_\alpha$ with $\abs{\alpha} = n$, so an endpoint $x$ of one of them is $a_\alpha$ or $a_\alpha + 3^{-n}$ for some word $\alpha$ of length $n$, that is, $x = p(\omega)$ for $\omega = \alpha 000\dots$ or $\omega = \alpha 222\dots$. Since every point of $C$ has exactly one address, this $\omega$ is the address of $x$, and it is eventually constant.

\emph{Conversely.} If the address of $x$ is eventually constant, it has the form $\alpha 000\dots$ or $\alpha 222\dots$ for a word $\alpha$ of some length $n$, so $x = a_\alpha$ or $x = a_\alpha + 3^{-n}$, an endpoint of the interval $C_\alpha$ of $C^n$.

\emph{Counting.} For each $n$ there are $2^n$ words of length $n$, so the set of all words is a countable union of finite sets and is countable; an eventually constant address is determined by a word and one of two letters, so there are countably many eventually constant addresses. The map $p$ is one-to-one (each point has exactly one address), so $E$, the image of the eventually constant addresses, is countable. Finally $C$ is uncountable, and if $C \setminus E$ were countable then $C = E \cup (C \setminus E)$ would be countable; so $C \setminus E$ is uncountable.
""", 2, 25, [
    r"The tail $\sum_{i > n} 2 \cdot 3^{-i}$ equals $3^{-n}$: an address ending in all $2$s reaches the right endpoint.",
    r"Both endpoints of $C_\alpha$ have addresses beginning with $\alpha$. Which ones?",
], ["c2-def-address", "c2-lem-address-intervals", "c2-thm-addresses", "c2-cor-cantor-uncountable", "c2-rem-cantor-endpoints"])


with open(OUT, "w") as f:
    json.dump({"version": 1, "id": "2-exercises", "blocks": blocks, "cards": []}, f, indent=1, ensure_ascii=False)

exercises = [b for b in blocks if b["kind"] == "exercise"]
print(f"2-exercises: {len(blocks)} blocks, {len(exercises)} exercises, "
      f"difficulties {sorted(b['difficulty'] for b in exercises)}")
