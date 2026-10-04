from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c2lib import Section

s = Section("2-cantor-sets")

s.p("c2-can-intro", r"""
The Cantor set is the standard example of a set that defeats naive intuition. It is what remains of $[0,1]$ after the open middle third is removed, then the open middle thirds of the two remaining pieces, and so on forever. What is left is as thin as dust (it contains no interval and has total length zero) and yet it has as many points as the whole line, none of them isolated. All the tools of this chapter are needed to see this: compactness, perfection, completeness, and connectedness.
""")

s.d("c2-def-cantor-set", "The standard Cantor set", r"""
For a closed interval $I = [a,b]$ with $a < b$, its \emph{left third} is $[a,\, a + \tfrac{b-a}{3}]$ and its \emph{right third} is $[b - \tfrac{b-a}{3},\, b]$; they are what is left of $I$ when the open \emph{middle third} $(a + \tfrac{b-a}{3},\, b - \tfrac{b-a}{3})$ is removed.

Define finite collections $\mathcal{I}_0, \mathcal{I}_1, \mathcal{I}_2, \dots$ of closed intervals recursively: $\mathcal{I}_0$ consists of the single interval $[0,1]$, and $\mathcal{I}_{n+1}$ consists of the left third and the right third of each interval in $\mathcal{I}_n$. Let $C^n$ be the union of the intervals in $\mathcal{I}_n$; the members of $\mathcal{I}_n$ are called \emph{the intervals of $C^n$}. So
\[ C^1 = [0,\tfrac13] \cup [\tfrac23, 1], \qquad C^2 = [0,\tfrac19] \cup [\tfrac29,\tfrac13] \cup [\tfrac23,\tfrac79] \cup [\tfrac89,1], \qquad \dots \]
The \emph{standard (middle-thirds) Cantor set} is
\[ C = \bigcap_{n=0}^\infty C^n . \]
""")

s.t("lemma", "c2-lem-cantor-structure", r"The structure of $C^n$", r"""
For every $n \ge 0$:
\begin{enumerate}
\item the intervals of $C^n$ are $2^n$ pairwise disjoint closed intervals, each of length $3^{-n}$ (and $C^n$ is their union);
\item $C^{n+1} \subset C^n$;
\item every endpoint of each of these $2^n$ intervals belongs to $C$.
\end{enumerate}
""", r"""
(1) By induction on $n$. $C^0 = [0,1]$ has one interval, of length $1$. Suppose the intervals of $C^n$ are $2^n$ pairwise disjoint closed intervals of length $3^{-n}$. Each such interval $I = [a,b]$ (with $a < b$, as its length is positive) contributes its two thirds to $\mathcal{I}_{n+1}$; each third is a closed interval of length $(b-a)/3 = 3^{-(n+1)}$, the two are disjoint because $a + \tfrac{b-a}{3} < b - \tfrac{b-a}{3}$, and both are contained in $I$. Thirds of different intervals of $C^n$ are disjoint because those intervals are. So the intervals of $C^{n+1}$ are $2 \cdot 2^n = 2^{n+1}$ pairwise disjoint closed intervals of length $3^{-(n+1)}$, and $C^{n+1}$ is their union.

(2) Each interval of $C^{n+1}$ is a third of an interval $I$ of $C^n$ and so is contained in $I \subset C^n$. Hence $C^{n+1} \subset C^n$.

(3) Let $e$ be an endpoint of one of the intervals $I = [a,b]$ of $C^n$. The left endpoint $a$ of $I$ is the left endpoint of the left third of $I$, and the right endpoint $b$ is the right endpoint of the right third. So $e$ is an endpoint of one of the intervals of $C^{n+1}$. By induction on $k$, $e$ is an endpoint of one of the intervals of $C^k$, and in particular $e \in C^k$, for every $k \ge n$. For $k < n$, part (2) applied repeatedly gives $e \in C^n \subset C^{n-1} \subset \dots \subset C^k$. Hence $e \in \bigcap_k C^k = C$.
""", 2, 25, [
    r"Induct on $n$ for (1). For (3), ask what happens to an endpoint of an interval when its middle third is removed.",
    r"An endpoint of an interval of $C^n$ is again an endpoint of an interval of $C^{n+1}$, so it is never removed.",
], ["c2-def-cantor-set"])

s.t("theorem", "c2-thm-cantor-compact", "The Cantor set is compact and nonempty", r"""
The Cantor set $C$ is a nonempty compact subset of $\R$.
""", r"""
$0 \in C$ by part (3) of the structure lemma, since $0$ is an endpoint of $C^0$. Each $C^n$ is a finite union of closed intervals and so is closed in $\R$; hence $C$, an intersection of closed sets, is closed. $C \subset [0,1]$ is bounded. By the Heine–Borel theorem $C$ is compact.
""", 1, 10, [
    r"Closed and bounded in $\R$.",
], ["c2-lem-cantor-structure", "c2-thm-heine-borel", "c2-cor-closed-sets"])

s.t("theorem", "c2-thm-cantor-perfect", "The Cantor set is perfect", r"""
Every point of $C$ is a cluster point of $C$. That is, $C$, as a metric space, is perfect.
""", r"""
Let $x \in C$ and $\eps > 0$. Choose $n$ with $3^{-n} < \eps$ (possible since $3^n \ge n$). Since $x \in C^n$, $x$ lies in one of the intervals $I = [a,b]$ of $C^n$, and $b - a = 3^{-n}$. Both endpoints $a$ and $b$ belong to $C$ by the structure lemma, both satisfy $\abs{a - x} \le 3^{-n} < \eps$ and $\abs{b - x} \le 3^{-n} < \eps$, and since $a \ne b$ at least one of them is different from $x$. So every neighborhood of $x$ contains a point of $C$ other than $x$. By the four descriptions of a cluster point, $x$ is a cluster point of $C$.
""", 2, 20, [
    r"Near $x$ you need points of $C$ other than $x$. Which points of $C$ do you know explicitly?",
    r"$x$ lies in an interval of $C^n$ of length $3^{-n}$, and the endpoints of that interval are in $C$.",
], ["c2-lem-cantor-structure", "c2-thm-cluster-equivalents", "c2-def-perfect"])

s.t("corollary", "c2-cor-cantor-uncountable", "The Cantor set is uncountable", r"""
The Cantor set $C$ is uncountable.
""", r"""
$C$ is nonempty and perfect. It is a closed subset of the complete space $\R$, so it is complete. A nonempty perfect complete metric space is uncountable.
""", 1, 10, [
    r"Which theorem produces uncountability from metric properties?",
], ["c2-thm-cantor-compact", "c2-thm-cantor-perfect", "c2-thm-perfect-uncountable", "c2-thm-closed-complete"])

s.r("c2-rem-cantor-endpoints", r"""
The endpoints of the intervals of the sets $C^n$ are countably many, since there are $2^{n+1}$ of them at stage $n$. So most points of $C$ are not endpoints; they are harder to see, and the next section gives a way to name them all.
""")

s.t("theorem", "c2-thm-cantor-gaps", "Between two points of $C$ there is a gap", r"""
If $x, y \in C$ and $x < y$, then there is a point $z \notin C$ with $x < z < y$.
""", r"""
Choose $n$ with $3^{-n} < y - x$. Let $I$ be the interval of $C^n$ containing $x$. Since $I$ has length $3^{-n} < y - x$, $y \notin I$.

Suppose, for a contradiction, that $[x,y] \subset C^n$. Let $J_1, \dots, J_{2^n}$ be the intervals of $C^n$, with $J_1 = I$. Then
\[ [x,y] = \bigcup_{i} \big( [x,y] \cap J_i \big) , \]
a union of pairwise disjoint sets, each closed in the subspace $[x,y]$ by the inheritance principle. The set $A = [x,y] \cap I$ is therefore closed in $[x,y]$, and its complement in $[x,y]$ is the finite union of the closed sets $[x,y] \cap J_i$, $i \ge 2$, hence closed; so $A$ is also open in $[x,y]$. Moreover $x \in A$ and $y \notin A$. Thus $A$ is a proper clopen subset of $[x,y]$, contradicting the fact that intervals are connected.

So there is a $z \in [x,y]$ with $z \notin C^n$, hence $z \notin C$. Since $x, y \in C$, $z$ is neither $x$ nor $y$, and $x < z < y$.
""", 3, 35, [
    r"Go to a stage $n$ where the intervals of $C^n$ are shorter than $y - x$, so that $x$ and $y$ are in different intervals.",
    r"If all of $[x,y]$ were in $C^n$, the interval of $C^n$ containing $x$ would cut out a proper clopen piece of $[x,y]$.",
], ["c2-lem-cantor-structure", "c2-thm-intervals-connected", "c2-thm-inheritance", "c2-cor-closed-sets", "c2-thm-open-closed-dual"])

s.d("c2-def-totally-disconnected", "Totally disconnected, nowhere dense", r"""
A metric space $M$ is \emph{totally disconnected} if every point has arbitrarily small clopen neighborhoods: for each $p \in M$ and each $\eps > 0$ there is a clopen set $U \subset M$ with $p \in U \subset M_\eps(p)$.

A subset $S$ of a metric space $M$ is \emph{nowhere dense} in $M$ if its closure has empty interior: $\interior \overline{S} = \varnothing$.
""")

s.t("theorem", "c2-thm-cantor-totally-disconnected", "The Cantor set is totally disconnected", r"""
The Cantor set $C$, as a metric space, is totally disconnected.
""", r"""
Let $x \in C$ and $\eps > 0$. Choose $n$ with $3^{-n} < \eps$, let $I$ be the interval of $C^n$ containing $x$, and put $U = C \cap I$. Then $x \in U$, and every point of $U$ is within $3^{-n} < \eps$ of $x$, so $U \subset C_\eps(x)$, the $\eps$-neighborhood of $x$ in $C$.

$U$ is closed in $C$ by the inheritance principle, since $I$ is closed in $\R$. Let $L$ be the union of the other $2^n - 1$ intervals of $C^n$; it is a finite union of closed intervals, hence closed in $\R$, and disjoint from $I$. Since $C \subset C^n = I \cup L$, we have $C \setminus U = C \cap L$, which is closed in $C$ by the inheritance principle. So $U$ is also open in $C$. Thus $U$ is a clopen subset of $C$ with $x \in U \subset C_\eps(x)$.
""", 2, 25, [
    r"The pieces of $C$ cut out by the intervals of $C^n$ are small. Show such a piece is clopen in $C$.",
    r"$C \cap I$ is closed in $C$; its complement in $C$ is $C$ intersected with the other intervals of $C^n$, also closed.",
], ["c2-def-totally-disconnected", "c2-lem-cantor-structure", "c2-thm-inheritance", "c2-cor-closed-sets", "c2-thm-open-closed-dual"])

s.t("corollary", "c2-cor-cantor-nowhere-dense", "The Cantor set is nowhere dense", r"""
$C$ contains no interval $(a,b)$ with $a < b$. Consequently $C$ has empty interior in $\R$, it is nowhere dense in $\R$, and every connected subset of $C$ has at most one point.
""", r"""
Suppose $(a,b) \subset C$ with $a < b$. Pick $x < y$ in $(a,b)$. Both are in $C$, so by the theorem on gaps there is a $z \notin C$ with $x < z < y$; but $z \in (a,b) \subset C$, a contradiction.

If $p$ were an interior point of $C$ in $\R$, some neighborhood $(p - r, p + r)$ would be contained in $C$, which was just excluded. So $\interior C = \varnothing$. Since $C$ is closed, $\overline{C} = C$, so $\interior \overline{C} = \varnothing$: $C$ is nowhere dense.

Let $S \subset C$ be connected. A connected subset of $\R$ is an interval. If $S$ had two points $x < y$, then every $z$ with $x < z < y$ would lie in $S \subset C$, contradicting the theorem on gaps. So $S$ has at most one point.
""", 2, 15, [
    r"Apply the theorem on gaps to two points of the supposed interval.",
], ["c2-thm-cantor-gaps", "c2-def-totally-disconnected", "c2-prop-interior", "c2-cor-connected-subsets-of-r", "c2-thm-cantor-compact", "c2-prop-closure-lim"])

s.d("c2-def-zero-set", "Zero set", r"""
A set $Z \subset \R$ is a \emph{zero set} (it has \emph{length zero}) if for every $\eps > 0$ there is a countable collection of open intervals $(a_i, b_i)$ that covers $Z$ and has total length $\sum_i (b_i - a_i) \le \eps$.
""")

s.t("theorem", "c2-thm-cantor-zero-set", "The Cantor set has length zero", r"""
The Cantor set $C$ is a zero set.
""", r"""
Let $\eps > 0$. By Bernoulli's inequality $(3/2)^n \ge 1 + n/2$, so we can choose $n$ with $(3/2)^n > 2/\eps$, that is, $(2/3)^n < \eps/2$. The set $C^n \supset C$ is the union of $2^n$ closed intervals $[a_i, b_i]$ of length $3^{-n}$. Put $\eta = \eps / 2^{n+2}$ and enlarge each to the open interval $(a_i - \eta,\ b_i + \eta)$. These $2^n$ open intervals cover $C^n$, hence $C$, and their total length is
\[ 2^n \big( 3^{-n} + 2\eta \big) = \Big(\frac23\Big)^n + 2^{n+1} \eta = \Big(\frac23\Big)^n + \frac\eps2 < \eps . \]
A finite collection is countable, so $C$ is a zero set.
""", 2, 20, [
    r"$C$ is contained in $C^n$. What is the total length of $C^n$?",
    r"The total length $(2/3)^n$ tends to $0$. Fatten the closed intervals slightly to make them open, spending at most $\eps/2$ in all.",
], ["c2-def-zero-set", "c2-lem-cantor-structure"])

s.r("c2-rem-cantor-summary", r"""
To summarize: $C$ is compact, nonempty, perfect, totally disconnected, nowhere dense, uncountable, and of length zero. The lengths of the removed middle thirds add up to $\tfrac13 + \tfrac29 + \tfrac4{27} + \dots = 1$, the whole length of $[0,1]$, and still uncountably many points remain. Smallness in the sense of length and smallness in the sense of cardinality are different things. (They can also be separated the other way: removing shorter middle pieces at each stage produces "fat" Cantor sets, which have all the topological properties above and positive length.)
""")

s.card("c2-card-cantor-def", "Define the standard Cantor set.",
       r"$C = \bigcap_n C^n$, where $C^0 = [0,1]$ and $C^{n+1}$ is obtained from $C^n$ by removing the open middle third of each of its $2^n$ intervals (of length $3^{-n}$).",
       "c2-def-cantor-set")
s.card("c2-card-cantor-properties", "List the main properties of the Cantor set.",
       r"Compact, nonempty, perfect, totally disconnected, nowhere dense, uncountable, length zero.",
       "c2-thm-cantor-zero-set")
s.card("c2-card-cantor-perfect-idea", "Why is the Cantor set perfect?",
       r"A point $x \in C$ lies in an interval of $C^n$ of length $3^{-n}$ whose two endpoints are in $C$; at least one differs from $x$ and both are within $3^{-n}$ of it.",
       "c2-thm-cantor-perfect")
s.card("c2-card-cantor-uncountable-idea", "Why is the Cantor set uncountable?",
       r"It is nonempty, perfect, and complete (closed in $\R$); such a space is uncountable.",
       "c2-cor-cantor-uncountable")
s.card("c2-card-totally-disconnected", "Define totally disconnected and nowhere dense.",
       r"Totally disconnected: each point has clopen neighborhoods of arbitrarily small radius. Nowhere dense: the closure has empty interior.",
       "c2-def-totally-disconnected")
s.card("c2-card-zero-set", r"Define zero set, and say why $C$ is one.",
       r"For every $\eps$ it can be covered by countably many open intervals of total length $\le \eps$. $C \subset C^n$, which has total length $(2/3)^n \to 0$.",
       "c2-thm-cantor-zero-set")

s.write()
