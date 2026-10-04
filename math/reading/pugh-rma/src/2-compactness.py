from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c2lib import Section

s = Section("2-compactness")

s.p("c2-cpt-intro", r"""
Compactness is the most important idea in this chapter. A compact set behaves, for many purposes, like a finite set: sequences in it cannot escape, continuous functions on it attain their extremes, and continuity on it is automatically uniform. We define it here through sequences. In $\R^m$ the compact sets will turn out to be exactly the closed and bounded ones, but in a general metric space that description is false, and the sequential definition is the one to hold on to.
""")

s.d("c2-def-compact", "Compact set", r"""
A subset $A$ of a metric space $M$ is \emph{(sequentially) compact} if every sequence $(a_n)$ of points of $A$ has a subsequence $(a_{n_k})$ that converges to a limit in $A$. The space $M$ is compact if it is a compact subset of itself.
""")

s.r("c2-rem-compact-intrinsic", r"""
The definition only involves points of $A$ and distances between them, so $A$ is a compact subset of $M$ exactly when $A$, as a metric space in its own right, is compact. Unlike "closed" or "open", compactness does not depend on the surrounding space. Finite sets are compact: a sequence in a finite set takes some value infinitely often, and those terms form a constant subsequence.
""")

s.d("c2-def-bounded", "Bounded set", r"""
A subset $S$ of a metric space $M$ is \emph{bounded} if $S \subset M_r(p)$ for some $p \in M$ and some $r > 0$. A sequence is bounded if its set of terms is bounded.
""")

s.t("lemma", "c2-lem-cluster-subsequence", "Extracting a convergent subsequence", r"""
Let $(p_n)$ be a sequence in a metric space $M$ and let $p \in M$. Then $(p_n)$ has a subsequence converging to $p$ if and only if for every $r > 0$ there are infinitely many indices $n$ with $p_n \in M_r(p)$.
""", r"""
Suppose $p_{n_k} \to p$. Given $r > 0$ there is a $K$ with $d(p_{n_k},p) < r$ for all $k \ge K$. The indices $n_K < n_{K+1} < \cdots$ are infinitely many, and $p_n \in M_r(p)$ for each of them.

Conversely, suppose each neighborhood of $p$ contains $p_n$ for infinitely many $n$. Choose $n_1$ with $d(p_{n_1},p) < 1$. Having chosen $n_1 < \dots < n_{k-1}$, note that there are infinitely many $n$ with $d(p_n,p) < 1/k$, so one of them is larger than $n_{k-1}$; call it $n_k$. This defines a subsequence with $d(p_{n_k},p) < 1/k$ for all $k$. Given $\eps > 0$, for $k > 1/\eps$ we get $d(p_{n_k},p) < \eps$, so $p_{n_k} \to p$.
""", 2, 15, [
    r"Build the subsequence one index at a time, using radius $1/k$ at step $k$.",
    r"Why can the $k$-th index always be chosen larger than the previous one?",
], ["c2-def-subsequence", "c2-def-convergence"])

s.t("theorem", "c2-thm-compact-closed-bounded", "Compact sets are closed and bounded", r"""
Every compact subset $A$ of a metric space $M$ is closed in $M$ and bounded.
""", r"""
\emph{Closed.} Let $p$ be a limit of $A$, so $a_n \to p$ for some sequence $(a_n)$ in $A$. By compactness a subsequence $(a_{n_k})$ converges to some $q \in A$. But subsequences of a convergent sequence converge to the same limit, so $a_{n_k} \to p$ as well. Limits are unique, so $p = q \in A$.

\emph{Bounded.} If $A$ is empty it is contained in any ball. Otherwise fix a point $p \in M$ and suppose $A$ is not bounded. Then for each $n \in \N$ the ball $M_n(p)$ does not contain $A$, so there is a point $a_n \in A$ with $d(a_n,p) \ge n$. By compactness some subsequence $(a_{n_k})$ converges to a point $q \in A$. Choose $K$ with $d(a_{n_k},q) < 1$ for all $k \ge K$. For such $k$,
\[ k \le n_k \le d(a_{n_k},p) \le d(a_{n_k},q) + d(q,p) < 1 + d(q,p) . \]
This is false as soon as $k \ge 1 + d(q,p)$. The contradiction shows $A$ is bounded.
""", 2, 25, [
    r"For closedness: a sequence in $A$ converging to $p$ has a subsequence converging in $A$. What is that subsequence's limit?",
    r"For boundedness: if $A$ were unbounded, choose $a_n \in A$ with $d(a_n,p) \ge n$ and look at a convergent subsequence.",
], ["c2-def-compact", "c2-def-bounded", "c2-def-subsequence", "c2-prop-subsequence-limit", "c2-thm-limit-unique"])

s.e("c2-ex-closed-bounded-not-compact", "Closed and bounded is not enough", r"""
Give $\N$ the discrete metric. The whole space is closed, and it is bounded since it lies in the ball of radius $2$ about $1$. But the sequence $1, 2, 3, \dots$ has no convergent subsequence: distinct terms are at distance $1$, so no subsequence is even Cauchy. Similarly the subspace $(0,1]$ of $\R$ is closed and bounded as a subset of itself and is not compact, since $1/n$ has no subsequence converging in $(0,1]$. The converse of the theorem does hold in $\R^m$; proving that is the main work of this section.
""")

s.t("theorem", "c2-thm-interval-compact", r"$[a,b]$ is compact", r"""
For real numbers $a \le b$, the closed bounded interval $[a,b] \subset \R$ is compact.
""", r"""
Let $(x_n)$ be a sequence in $[a,b]$ and put
\[ C = \set{x \in [a,b] : x_n < x \text{ for only finitely many } n}. \]
Then $a \in C$ (no $x_n$ is less than $a$) and $b$ is an upper bound of $C$, so by the least upper bound property $c = \lub C$ exists and $a \le c \le b$.

\emph{Claim: for every $r > 0$ there are infinitely many $n$ with $x_n \in (c-r, c+r)$.} Suppose not, and take $r > 0$ for which only finitely many $n$ have $x_n \in (c-r,c+r)$. Since $c - r$ is not an upper bound of $C$ there is an $x \in C$ with $x > c - r$. Every $n$ with $x_n \le c-r$ has $x_n < x$, so there are only finitely many such $n$. Combined with the supposition, only finitely many $n$ satisfy $x_n < c + r$. If $c + r > b$ this is absurd, because then every $n \in \N$ satisfies $x_n \le b < c+r$. If $c + r \le b$ then $c + r$ is a point of $[a,b]$ with $x_n < c+r$ for only finitely many $n$, so $c + r \in C$, contradicting that $c$ is an upper bound of $C$. This proves the claim.

By the lemma on extracting a convergent subsequence, the claim gives a subsequence $(x_{n_k})$ converging to $c$, and $c \in [a,b]$.
""", 4, 60, [
    r"You need a candidate limit. Use the least upper bound property on a cleverly chosen set.",
    r"Consider $C = \set{x \in [a,b] : x_n < x \text{ for only finitely many } n}$ and $c = \lub C$.",
    r"Show every interval $(c-r,c+r)$ contains $x_n$ for infinitely many $n$: otherwise $c + r$ (or a contradiction with $x_n \le b$) would beat $c$.",
], ["c2-def-compact", "c2-lem-cluster-subsequence"])

s.t("theorem", "c2-thm-product-compact", "The product of two compact sets is compact", r"""
Let $A \subset M$ and $B \subset N$ be compact subsets of metric spaces. Then $A \times B$ is a compact subset of $M \times N$ (with any of the product metrics $d_E$, $d_{\max}$, $d_{\mathrm{sum}}$).
""", r"""
Let $(a_n, b_n)$ be a sequence in $A \times B$. Since $A$ is compact there is a subsequence $(a_{n_k})$ converging to some $a \in A$. The corresponding sequence $(b_{n_k})_{k \in \N}$ lies in $B$, so by compactness of $B$ it has a subsequence $(b_{n_{k_j}})_{j \in \N}$ converging to some $b \in B$. The sequence $(a_{n_{k_j}})_{j}$ is a subsequence of $(a_{n_k})_k$ and so still converges to $a$. By the theorem on convergence in a product, $(a_{n_{k_j}}, b_{n_{k_j}}) \to (a,b)$ with respect to each of the product metrics, and $(a,b) \in A \times B$. Since $(n_{k_j})_j$ is strictly increasing, this is a subsequence of the original sequence.
""", 3, 25, [
    r"Extract a subsequence to make the first coordinates converge. What can you do next?",
    r"Take a sub-subsequence for the second coordinates; the first coordinates keep converging.",
], ["c2-def-compact", "c2-def-subsequence", "c2-thm-product-convergence", "c2-prop-subsequence-limit"])

s.t("corollary", "c2-cor-box-compact", "Boxes are compact", r"""
A \emph{box} $[a_1,b_1] \times \dots \times [a_m,b_m] \subset \R^m$ is compact.
""", r"""
Call the box $B$ and let $(v_n)$ be a sequence in $B$, $v_n = (v_{n1}, \dots, v_{nm})$. We show by induction on $j = 0, 1, \dots, m$ that $(v_n)$ has a subsequence whose $i$-th coordinates converge to a point of $[a_i,b_i]$ for every $i \le j$. For $j = 0$ the sequence itself works. Suppose $(w_k)$ is such a subsequence for $j - 1$. Its $j$-th coordinates form a sequence in $[a_j,b_j]$, which is compact, so there is a subsequence $(w_{k_l})_l$ whose $j$-th coordinates converge to a point of $[a_j,b_j]$. For $i < j$ the $i$-th coordinates of $(w_{k_l})$ are a subsequence of a convergent sequence and converge to the same limit in $[a_i,b_i]$. A subsequence of a subsequence of $(v_n)$ is a subsequence of $(v_n)$, which completes the induction.

For $j = m$ we obtain a subsequence of $(v_n)$ all of whose coordinate sequences converge, the $i$-th to some $c_i \in [a_i,b_i]$. Since convergence in $\R^m$ is componentwise, this subsequence converges to $c = (c_1, \dots, c_m) \in B$.
""", 2, 20, [
    r"Repeat the sub-subsequence trick $m$ times, one coordinate at a time, and use that convergence in $\R^m$ is componentwise.",
], ["c2-thm-interval-compact", "c2-cor-rm-convergence", "c2-prop-subsequence-limit", "c2-def-compact"])

s.t("theorem", "c2-thm-bolzano-weierstrass", "Bolzano–Weierstrass", r"""
Every bounded sequence in $\R^m$ has a convergent subsequence.
""", r"""
Let $(v_n)$ be bounded: there are $p \in \R^m$ and $r > 0$ with $\abs{v_n - p} < r$ for all $n$. Each coordinate satisfies $\abs{v_{ni} - p_i} \le \abs{v_n - p} < r$, so every $v_n$ lies in the box $[p_1 - r, p_1 + r] \times \dots \times [p_m - r, p_m + r]$. Boxes are compact, so $(v_n)$ has a subsequence converging (to a point of the box).
""", 2, 15, [
    r"Put the bounded sequence inside a compact set you already know.",
], ["c2-cor-box-compact", "c2-def-bounded"])

s.t("theorem", "c2-thm-closed-in-compact", "Closed subsets of compact sets are compact", r"""
If $A$ is a compact subset of a metric space $M$ and $S \subset A$ is closed in $M$, then $S$ is compact.
""", r"""
Let $(s_n)$ be a sequence in $S$. It is a sequence in $A$, so some subsequence $(s_{n_k})$ converges to a point $p \in A$. Then $p$ is a limit of $S$, and $S$ is closed, so $p \in S$. Thus the subsequence converges to a limit in $S$.
""", 1, 10, [
    r"Compactness of $A$ gives a convergent subsequence; closedness of $S$ says where its limit is.",
], ["c2-def-compact", "c2-def-closed-open"])

s.t("theorem", "c2-thm-heine-borel", "Heine–Borel", r"""
A subset of $\R^m$ is compact if and only if it is closed and bounded.
""", r"""
Compact sets are closed and bounded in any metric space. Conversely let $A \subset \R^m$ be closed and bounded, say $A \subset M_r(p)$. As in the proof of Bolzano–Weierstrass, each coordinate of a point $v$ with $\abs{v - p} < r$ satisfies $\abs{v_i - p_i} < r$, so $A$ lies in the box $B = [p_1 - r, p_1 + r] \times \dots \times [p_m - r, p_m + r]$. The box is compact and $A$ is a closed subset of $\R^m$ contained in it, so $A$ is compact, because closed subsets of compact sets are compact.
""", 2, 15, [
    r"One direction is already a theorem. For the other, trap the set inside a box.",
], ["c2-thm-compact-closed-bounded", "c2-def-bounded", "c2-cor-box-compact", "c2-thm-closed-in-compact"])

s.e("c2-ex-compact-examples", "Compact sets in Euclidean space", r"""
By Heine–Borel the closed unit ball $\set{x \in \R^m : \abs{x} \le 1}$ and the unit sphere $S^{m-1} = \set{x \in \R^m : \abs{x} = 1}$ are compact (the sphere is closed because $x \mapsto \abs{x}$ is continuous and $\set{1}$ is closed in $\R$). A convergent sequence together with its limit, such as $\set{0} \cup \set{1/n : n \in \N}$, is compact. The sets $(0,1]$, $\N$, and $\Q \cap [0,1]$ are not compact in $\R$: the first and the last are not closed, the second is not bounded.
""")

s.t("theorem", "c2-thm-nested-compact", "Nested compact sets", r"""
Let $A_1 \supset A_2 \supset A_3 \supset \cdots$ be a decreasing sequence of nonempty compact subsets of a metric space $M$. Then $A = \bigcap_{n} A_n$ is nonempty and compact.
""", r"""
Each $A_n$ is closed in $M$ because compact sets are closed, so $A$ is closed as an intersection of closed sets; it is a closed subset of the compact set $A_1$, hence compact.

To see that $A$ is nonempty, choose $a_n \in A_n$ for each $n$. This is a sequence in $A_1$, so a subsequence $(a_{n_k})$ converges to some $p \in A_1$. Fix $m \in \N$. For $k \ge m$ we have $n_k \ge k \ge m$, hence $a_{n_k} \in A_{n_k} \subset A_m$. So the sequence $(a_{n_k})_{k \ge m}$ lies in $A_m$ and converges to $p$; since $A_m$ is closed, $p \in A_m$. As $m$ was arbitrary, $p \in A$.
""", 3, 25, [
    r"Pick one point from each $A_n$ and use compactness of $A_1$.",
    r"For fixed $m$, the tail of your subsequence lies in $A_m$, and $A_m$ is closed.",
], ["c2-def-compact", "c2-def-subsequence", "c2-def-closed-open", "c2-thm-compact-closed-bounded", "c2-thm-closed-in-compact", "c2-cor-closed-sets"])

s.d("c2-def-diameter", "Diameter", r"""
The \emph{diameter} of a nonempty bounded subset $S$ of a metric space is
\[ \diam S = \sup \set{d(x,y) : x, y \in S}. \]
(If $S \subset M_r(p)$ then $d(x,y) \le d(x,p) + d(p,y) < 2r$ for $x, y \in S$, so the supremum exists.)
""")

s.t("corollary", "c2-cor-nested-diameter", "Nested compact sets shrinking to a point", r"""
Let $A_1 \supset A_2 \supset \cdots$ be nonempty compact subsets of a metric space with $\diam A_n \to 0$ as $n \to \infty$. Then $\bigcap_n A_n$ consists of exactly one point.
""", r"""
Compact sets are bounded, so each $\diam A_n$ is defined. By the theorem on nested compact sets the intersection $A$ is nonempty. If $p, q \in A$, then $p, q \in A_n$ for every $n$, so $0 \le d(p,q) \le \diam A_n$ for every $n$. Since $\diam A_n \to 0$, this forces $d(p,q) = 0$, so $p = q$.
""", 1, 10, [
    r"Existence is the previous theorem. For uniqueness, two points of the intersection lie in every $A_n$.",
], ["c2-thm-nested-compact", "c2-thm-compact-closed-bounded", "c2-def-diameter"])

s.r("c2-rem-nested-fails", r"""
Compactness cannot be weakened to closedness or to boundedness here. The closed sets $[n, \infty) \subset \R$ are nested with empty intersection, and so are the bounded sets $(0, 1/n)$.
""")

s.p("c2-cpt-continuity-prose", r"""
\textbf{Continuity and compactness.} Continuous maps need not preserve closedness or boundedness separately ($x \mapsto 1/(1+x^2)$ sends the closed set $\R$ onto $(0,1]$, which is not closed in $\R$, and $x \mapsto 1/x$ sends the bounded set $(0,1]$ onto the unbounded set $[1,\infty)$), but they do preserve compactness. Most of the good behaviour of continuous functions on $[a,b]$ comes from this one fact.
""")

s.t("theorem", "c2-thm-continuous-image-compact", "The continuous image of a compact set is compact", r"""
Let $f : M \to N$ be a continuous map of metric spaces and $A \subset M$ a compact set. Then $f(A)$ is a compact subset of $N$.
""", r"""
Let $(b_n)$ be a sequence in $f(A)$, and for each $n$ choose $a_n \in A$ with $f(a_n) = b_n$. By compactness of $A$ a subsequence $(a_{n_k})$ converges to some $a \in A$. By continuity $b_{n_k} = f(a_{n_k}) \to f(a)$, and $f(a) \in f(A)$. So $(b_n)$ has a subsequence converging to a limit in $f(A)$.
""", 2, 15, [
    r"Lift a sequence in $f(A)$ to a sequence in $A$.",
], ["c2-def-compact", "c2-def-continuity"])

s.t("corollary", "c2-cor-extreme-values", "Extreme values", r"""
Let $A$ be a nonempty compact metric space and $f : A \to \R$ a continuous function. Then $f$ is bounded and attains a maximum and a minimum: there are $p, q \in A$ with $f(p) \le f(x) \le f(q)$ for all $x \in A$.
""", r"""
The image $f(A)$ is a compact subset of $\R$, hence closed and bounded, and it is nonempty. Being bounded and nonempty it has a least upper bound $u$. For each $n \in \N$ the number $u - 1/n$ is not an upper bound of $f(A)$, so there is a $y_n \in f(A)$ with $u - 1/n < y_n \le u$. Then $y_n \to u$, so $u$ is a limit of $f(A)$, and $u \in f(A)$ because $f(A)$ is closed. Thus $u = f(q)$ for some $q \in A$, and $f(x) \le u = f(q)$ for all $x \in A$.

Applying this to the continuous function $-f$ (if $x_n \to x$ then $-f(x_n) \to -f(x)$) gives a point $p$ with $-f(x) \le -f(p)$, that is $f(p) \le f(x)$, for all $x \in A$.
""", 2, 20, [
    r"What kind of subset of $\R$ is $f(A)$?",
    r"A nonempty closed bounded subset of $\R$ contains its least upper bound: the supremum is a limit of the set.",
], ["c2-thm-continuous-image-compact", "c2-thm-compact-closed-bounded", "c2-def-closed-open", "c2-def-continuity"])

s.t("theorem", "c2-thm-compact-homeomorphism", "A continuous bijection from a compact space is a homeomorphism", r"""
Let $M$ be a compact metric space and $f : M \to N$ a continuous bijection onto a metric space $N$. Then $f^{-1} : N \to M$ is continuous, so $f$ is a homeomorphism.
""", r"""
We check the closed set condition for $g = f^{-1} : N \to M$. Let $K \subset M$ be closed. Since $f$ is a bijection, $g^{-1}(K) = \set{y \in N : f^{-1}(y) \in K} = f(K)$. Now $K$ is a closed subset of the compact space $M$, hence compact; its continuous image $f(K)$ is compact; and compact sets are closed. So $g^{-1}(K)$ is closed in $N$ for every closed $K \subset M$, and $g$ is continuous.
""", 3, 25, [
    r"Use the closed set condition for $f^{-1}$. What is the preimage of $K$ under $f^{-1}$?",
    r"Closed in compact is compact; continuous images of compact sets are compact; compact sets are closed.",
], ["c2-thm-open-set-condition", "c2-thm-closed-in-compact", "c2-thm-continuous-image-compact", "c2-thm-compact-closed-bounded"])

s.r("c2-rem-circle-again", r"""
This explains the example of $[0,2\pi)$ wrapped around the circle: the inverse failed to be continuous, and indeed $[0,2\pi)$ is not compact. It also shows that the circle is not homeomorphic to $[0,2\pi)$ by any map, since one is compact and the other is not, and compactness is a topological property (continuous images of compact sets are compact).
""")

s.d("c2-def-uniform-continuity", "Uniform continuity", r"""
A map $f : M \to N$ of metric spaces is \emph{uniformly continuous} if for every $\eps > 0$ there is a $\delta > 0$ such that for all $p, q \in M$,
\[ d_M(p,q) < \delta \implies d_N(f(p), f(q)) < \eps . \]
The difference from the $\eps,\delta$ condition is that $\delta$ depends on $\eps$ only, not on the point. For example $x \mapsto x^2$ is continuous on $\R$ and not uniformly continuous: $(n + 1/n)^2 - n^2 > 2$ although the two points are $1/n$ apart.
""")

s.t("theorem", "c2-thm-uniform-continuity", "Continuity on a compact space is uniform", r"""
Every continuous map $f : M \to N$ from a compact metric space $M$ to a metric space $N$ is uniformly continuous.
""", r"""
Suppose $f$ is not uniformly continuous. Then there is an $\eps > 0$ for which no $\delta$ works; taking $\delta = 1/n$ gives points $p_n, q_n \in M$ with
\[ d_M(p_n,q_n) < \frac1n \quad\text{and}\quad d_N(f(p_n), f(q_n)) \ge \eps . \]
By compactness a subsequence $(p_{n_k})$ converges to some $p \in M$. Then
\[ d_M(q_{n_k}, p) \le d_M(q_{n_k}, p_{n_k}) + d_M(p_{n_k}, p) < \frac{1}{n_k} + d_M(p_{n_k},p) \le \frac1k + d_M(p_{n_k},p), \]
which tends to $0$ as $k \to \infty$, so $q_{n_k} \to p$ too. By continuity $f(p_{n_k}) \to f(p)$ and $f(q_{n_k}) \to f(p)$. Choose $k$ so large that both $d_N(f(p_{n_k}), f(p)) < \eps/2$ and $d_N(f(q_{n_k}), f(p)) < \eps/2$. Then
\[ d_N(f(p_{n_k}), f(q_{n_k})) \le d_N(f(p_{n_k}), f(p)) + d_N(f(p), f(q_{n_k})) < \eps , \]
contradicting $d_N(f(p_{n_k}), f(q_{n_k})) \ge \eps$. Hence $f$ is uniformly continuous.
""", 3, 35, [
    r"Argue by contradiction and negate uniform continuity carefully.",
    r"You get pairs $p_n, q_n$ with $d(p_n,q_n) < 1/n$ whose images stay $\eps$ apart. Use compactness on $(p_n)$.",
    r"If $p_{n_k} \to p$ then $q_{n_k} \to p$ as well; now apply continuity at $p$ to both.",
], ["c2-def-uniform-continuity", "c2-def-compact", "c2-def-subsequence", "c2-def-continuity"])

s.card("c2-card-compact", "Define (sequentially) compact subset of a metric space.",
       r"$A \subset M$ is compact if every sequence in $A$ has a subsequence converging to a limit in $A$.",
       "c2-def-compact")
s.card("c2-card-compact-closed-bounded", "Compact implies closed and bounded. Give a closed bounded set that is not compact.",
       r"$\N$ with the discrete metric: closed, bounded, and $1, 2, 3, \dots$ has no convergent subsequence. (Or the unit interval $(0,1]$ as a space in itself.)",
       "c2-ex-closed-bounded-not-compact")
s.card("c2-card-heine-borel", "State the Heine–Borel theorem and the Bolzano–Weierstrass theorem.",
       r"Heine–Borel: a subset of $\R^m$ is compact iff it is closed and bounded. Bolzano–Weierstrass: every bounded sequence in $\R^m$ has a convergent subsequence.",
       "c2-thm-heine-borel")
s.card("c2-card-interval-idea", r"One-line idea of the proof that $[a,b]$ is compact.",
       r"For a sequence $(x_n)$, let $c$ be the least upper bound of the $x \in [a,b]$ with $x_n < x$ only finitely often; every interval about $c$ contains $x_n$ infinitely often, so a subsequence converges to $c$.",
       "c2-thm-interval-compact")
s.card("c2-card-nested", "State the theorem on nested compact sets. What extra hypothesis gives a single point?",
       r"A decreasing sequence of nonempty compact sets has nonempty compact intersection; if the diameters tend to $0$ the intersection is one point. Fails for closed sets $[n,\infty)$ and for bounded sets $(0,1/n)$.",
       "c2-cor-nested-diameter")
s.card("c2-card-image", "What do continuous maps do to compact sets? Name two consequences.",
       r"The continuous image of a compact set is compact. Consequences: a continuous real function on a nonempty compact set attains a maximum and a minimum; a continuous bijection from a compact space is a homeomorphism.",
       "c2-thm-compact-homeomorphism")
s.card("c2-card-uniform", "Define uniform continuity and state the theorem about compact domains. Give a continuous function that is not uniformly continuous.",
       r"For every $\eps$ there is one $\delta$ with $d(p,q) < \delta \Rightarrow d(f(p),f(q)) < \eps$ for all $p, q$. Every continuous map on a compact space is uniformly continuous. $x^2$ on $\R$ (or $1/x$ on $(0,1]$) is not.",
       "c2-thm-uniform-continuity")
s.card("c2-card-product-compact", "Idea of the proof that a product of two compact sets is compact.",
       r"Take a subsequence making the first coordinates converge, then a sub-subsequence making the second coordinates converge; convergence in a product is coordinatewise.",
       "c2-thm-product-compact")

s.write()
