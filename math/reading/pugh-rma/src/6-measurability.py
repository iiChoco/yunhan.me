from __future__ import annotations

import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from c6common import prose, note, result, card, write

B = []

B.append(prose("c6-meas-intro", r"""
Outer measure is subadditive, and for badly intertwined sets the inequality can be strict. Carathéodory's remedy is to single out the sets that never cause this trouble: a set is \emph{measurable} if it cuts every set, however wild, into two pieces whose outer measures add up. The payoff is large. The measurable sets are closed under every countable set operation, outer measure is countably additive on them, and they include all open and closed sets.
"""))

B.append(note("definition", "c6-def-measurable", "Measurable set (Carathéodory)", r"""
A set $E \subseteq \R^n$ is \emph{(Lebesgue) measurable} if for every \emph{test set} $X \subseteq \R^n$,
\[ m^*X = m^*(X \cap E) + m^*(X \cap E^c), \]
where $E^c = \R^n \setminus E$. One says that $E$ \emph{divides $X$ cleanly}. For a measurable set $E$ the \emph{Lebesgue measure} of $E$ is $mE = m^*E$.
"""))

B.append(note("remark", "c6-rem-half-of-condition", "Only one inequality needs checking", r"""
Since $X = (X \cap E) \cup (X \cap E^c)$, subadditivity always gives $m^*X \le m^*(X \cap E) + m^*(X \cap E^c)$. So $E$ is measurable as soon as
\[ m^*(X \cap E) + m^*(X \cap E^c) \le m^*X \]
for every $X$ with $m^*X < \infty$ (for $m^*X = \infty$ the inequality is automatic).
"""))

B.append(result("proposition", "c6-prop-measurable-basic", "Zero sets and complements", r"""
(a) Every zero set is measurable. In particular $\emptyset$ is measurable.

(b) If $E$ is measurable, so is $E^c$. In particular $\R^n$ is measurable.
""", r"""
(a) Let $m^*Z = 0$ and let $X$ be any test set. By monotonicity $m^*(X \cap Z) \le m^*Z = 0$ and $m^*(X \cap Z^c) \le m^*X$, so $m^*(X \cap Z) + m^*(X \cap Z^c) \le m^*X$. The reverse inequality is subadditivity. So $Z$ is measurable; $\emptyset$ is a zero set.

(b) Since $(E^c)^c = E$, the condition $m^*X = m^*(X \cap E^c) + m^*(X \cap (E^c)^c)$ is the same equation as the one for $E$. Thus $E^c$ is measurable, and $\R^n = \emptyset^c$.
""", 1, 10, [
    r"For a zero set, one of the two pieces of $X$ has outer measure $0$ and the other is a subset of $X$.",
], ["c6-def-measurable", "c6-rem-half-of-condition", "c6-def-zero-set", "c6-prop-outer-basic"]))

B.append(result("lemma", "c6-lem-two-sets", "Unions, intersections, differences of two measurable sets", r"""
If $E_1$ and $E_2$ are measurable subsets of $\R^n$, then so are $E_1 \cup E_2$, $E_1 \cap E_2$, and $E_1 \setminus E_2$. Hence finite unions and finite intersections of measurable sets are measurable.
""", r"""
Let $X$ be a test set. Since $E_1$ is measurable,
\[ m^*X = m^*(X \cap E_1) + m^*(X \cap E_1^c). \]
Since $E_2$ is measurable, applying its condition to the test set $X \cap E_1^c$ gives
\[ m^*(X \cap E_1^c) = m^*(X \cap E_1^c \cap E_2) + m^*(X \cap E_1^c \cap E_2^c). \]
Now $X \cap (E_1 \cup E_2) = (X \cap E_1) \cup (X \cap E_1^c \cap E_2)$, so by subadditivity
\[ m^*(X \cap (E_1 \cup E_2)) \le m^*(X \cap E_1) + m^*(X \cap E_1^c \cap E_2), \]
and $X \cap (E_1 \cup E_2)^c = X \cap E_1^c \cap E_2^c$. Adding,
\[ m^*(X \cap (E_1 \cup E_2)) + m^*(X \cap (E_1 \cup E_2)^c) \le m^*(X \cap E_1) + m^*(X \cap E_1^c \cap E_2) + m^*(X \cap E_1^c \cap E_2^c) = m^*X. \]
The reverse inequality always holds, so $E_1 \cup E_2$ is measurable.

Complements of measurable sets are measurable, so $E_1 \cap E_2 = (E_1^c \cup E_2^c)^c$ is measurable, and then $E_1 \setminus E_2 = E_1 \cap E_2^c$ is measurable. The statement for finitely many sets follows by induction.
""", 3, 30, [
    r"Cut the test set $X$ first by $E_1$, then cut the piece $X \cap E_1^c$ by $E_2$. That gives three pieces whose outer measures add up to $m^*X$.",
    r"Two of the three pieces together cover $X \cap (E_1 \cup E_2)$; the third is $X \cap (E_1 \cup E_2)^c$. Use subadditivity on the first two.",
], ["c6-def-measurable", "c6-rem-half-of-condition", "c6-prop-measurable-basic"]))

B.append(result("lemma", "c6-lem-finite-additivity", "Finite additivity inside any test set", r"""
Let $E_1, \dots, E_k$ be pairwise disjoint measurable sets and let $X \subseteq \R^n$ be arbitrary. Then
\[ m^*\Bigl( X \cap \bigcup_{i=1}^k E_i \Bigr) = \sum_{i=1}^k m^*(X \cap E_i). \]
In particular $m(E_1 \sqcup \dots \sqcup E_k) = mE_1 + \dots + mE_k$.
""", r"""
Induct on $k$; the case $k = 1$ is trivial. For $k \ge 2$, apply the measurability of $E_k$ to the test set $Y = X \cap \bigcup_{i=1}^k E_i$. Because the sets are disjoint, $Y \cap E_k = X \cap E_k$ and $Y \cap E_k^c = X \cap \bigcup_{i=1}^{k-1} E_i$. Hence
\[ m^*Y = m^*(X \cap E_k) + m^*\Bigl( X \cap \bigcup_{i=1}^{k-1} E_i \Bigr) = m^*(X \cap E_k) + \sum_{i=1}^{k-1} m^*(X \cap E_i), \]
the last step by the induction hypothesis. The final statement is the case $X = \R^n$; the union is measurable by the lemma on two measurable sets.
""", 2, 15, [
    r"Induct on $k$, and choose the test set cleverly.",
    r"Test the measurability of $E_k$ against $Y = X \cap (E_1 \cup \dots \cup E_k)$.",
], ["c6-def-measurable", "c6-lem-two-sets"]))

B.append(note("definition", "c6-def-sigma-algebra", "Sigma-algebra", r"""
A collection $\mathcal{M}$ of subsets of a set $S$ is a \emph{$\sigma$-algebra} if $\emptyset \in \mathcal{M}$, if $E \in \mathcal{M}$ implies $S \setminus E \in \mathcal{M}$, and if $E_1, E_2, \dots \in \mathcal{M}$ implies $\bigcup_{j=1}^\infty E_j \in \mathcal{M}$. By De Morgan's laws a $\sigma$-algebra is then also closed under countable intersections, and under differences.
"""))

B.append(result("theorem", "c6-thm-sigma-algebra", "Measurable sets form a sigma-algebra; measure is countably additive", r"""
(a) If $E_1, E_2, \dots$ are measurable subsets of $\R^n$, then $\bigcup_{j} E_j$ and $\bigcap_j E_j$ are measurable. Hence the measurable subsets of $\R^n$ form a $\sigma$-algebra.

(b) If $E_1, E_2, \dots$ are pairwise disjoint measurable sets, then
\[ m\Bigl( \bigsqcup_{j=1}^\infty E_j \Bigr) = \sum_{j=1}^\infty mE_j. \]
""", r"""
\emph{Disjoint unions.} Let $E_1, E_2, \dots$ be pairwise disjoint measurable sets, $E = \bigsqcup_j E_j$, and $F_k = E_1 \cup \dots \cup E_k$, which is measurable by the lemma on two measurable sets. Let $X$ be a test set. Using the measurability of $F_k$, then finite additivity inside $X$, and $F_k^c \supseteq E^c$ with monotonicity,
\[ m^*X = m^*(X \cap F_k) + m^*(X \cap F_k^c) \ge \sum_{j=1}^k m^*(X \cap E_j) + m^*(X \cap E^c). \]
This holds for every $k$, so letting $k \to \infty$,
\[ m^*X \ge \sum_{j=1}^\infty m^*(X \cap E_j) + m^*(X \cap E^c) \ge m^*(X \cap E) + m^*(X \cap E^c), \tag{$*$} \]
where the second inequality is countable subadditivity applied to $X \cap E = \bigcup_j (X \cap E_j)$. Since the reverse inequality always holds, $E$ is measurable.

(b) Take $X = E$ in $(*)$: then $X \cap E^c = \emptyset$ and $m^*E \ge \sum_j m^*E_j \ge m^*E$, so $mE = \sum_j mE_j$.

(a) Let $E_1, E_2, \dots$ be measurable, not necessarily disjoint. Put $E_1' = E_1$ and $E_j' = E_j \setminus (E_1 \cup \dots \cup E_{j-1})$ for $j \ge 2$. These sets are measurable by the lemma on two measurable sets, they are pairwise disjoint, and $\bigcup_j E_j' = \bigcup_j E_j$ (a point of the union lies in $E_j'$ for the least $j$ with $x \in E_j$). By the first part of the proof, $\bigcup_j E_j$ is measurable. Finally $\bigcap_j E_j = \bigl( \bigcup_j E_j^c \bigr)^c$ is measurable because complements of measurable sets are measurable. Together with the measurability of $\emptyset$ this says the measurable sets form a $\sigma$-algebra.
""", 4, 60, [
    r"Treat a disjoint sequence first. The finite unions $F_k = E_1 \cup \dots \cup E_k$ are measurable and you know how $m^*(X \cap F_k)$ splits.",
    r"From $m^*X = m^*(X \cap F_k) + m^*(X \cap F_k^c)$, replace $F_k^c$ by the smaller set $E^c$ and let $k \to \infty$; then use countable subadditivity to reassemble $X \cap E$.",
    r"For a general sequence, make it disjoint: $E_j' = E_j \setminus (E_1 \cup \dots \cup E_{j-1})$.",
], ["c6-def-measurable", "c6-rem-half-of-condition", "c6-prop-measurable-basic", "c6-lem-two-sets", "c6-lem-finite-additivity", "c6-def-sigma-algebra"]))

B.append(result("proposition", "c6-prop-measure-difference", "Monotonicity and differences", r"""
Let $A \subseteq E$ be measurable subsets of $\R^n$. Then $mE = mA + m(E \setminus A)$. Consequently $mA \le mE$, and if $mA < \infty$ then $m(E \setminus A) = mE - mA$.
""", r"""
The set $E \setminus A$ is measurable by the lemma on two measurable sets, and $E = A \sqcup (E \setminus A)$. Finite additivity gives $mE = mA + m(E \setminus A)$. Since $m(E \setminus A) \ge 0$, $mA \le mE$; if $mA$ is finite it may be subtracted from both sides.
""", 1, 5, [
    r"Write $E$ as a disjoint union.",
], ["c6-lem-two-sets", "c6-lem-finite-additivity"]))

B.append(result("theorem", "c6-thm-measure-continuity", "Measure continuity", r"""
Let $E_1, E_2, \dots$ be measurable subsets of $\R^n$.

(a) (Upward) If $E_1 \subseteq E_2 \subseteq \cdots$, then $m\bigl( \bigcup_j E_j \bigr) = \lim_{j \to \infty} mE_j$.

(b) (Downward) If $E_1 \supseteq E_2 \supseteq \cdots$ and $mE_1 < \infty$, then $m\bigl( \bigcap_j E_j \bigr) = \lim_{j \to \infty} mE_j$.

(Limits are taken in $[0,\infty]$; in both cases the sequence $(mE_j)$ is monotone.)
""", r"""
(a) Put $D_1 = E_1$ and $D_j = E_j \setminus E_{j-1}$ for $j \ge 2$. These are measurable and pairwise disjoint, $D_1 \sqcup \dots \sqcup D_k = E_k$, and $\bigsqcup_j D_j = \bigcup_j E_j$. By countable additivity and then finite additivity,
\[ m\Bigl( \bigcup_j E_j \Bigr) = \sum_{j=1}^\infty mD_j = \lim_{k \to \infty} \sum_{j=1}^k mD_j = \lim_{k \to \infty} mE_k. \]

(b) Let $E = \bigcap_j E_j$. The sets $E_1 \setminus E_j$ are measurable and increase with $j$, and their union is $E_1 \setminus E$. By (a), $m(E_1 \setminus E) = \lim_j m(E_1 \setminus E_j)$. Since $mE_1 < \infty$, all of $mE_j$ and $mE$ are finite, and the proposition on differences gives $m(E_1 \setminus E_j) = mE_1 - mE_j$ and $m(E_1 \setminus E) = mE_1 - mE$. Hence $mE_1 - mE = \lim_j (mE_1 - mE_j)$, that is, $mE = \lim_j mE_j$.
""", 3, 30, [
    r"For (a), turn the increasing union into a disjoint union of the successive differences.",
    r"For (b), apply (a) to the increasing sets $E_1 \setminus E_j$; finiteness of $mE_1$ lets you subtract.",
], ["c6-thm-sigma-algebra", "c6-lem-finite-additivity", "c6-prop-measure-difference"]))

B.append(prose("c6-meas-open-prose", r"""
So far the only sets known to be measurable are zero sets and their complements. To get a useful supply we show that a half-space is measurable; boxes, open sets, and closed sets then follow from the $\sigma$-algebra property.
"""))

B.append(result("lemma", "c6-lem-half-space", "Half-spaces are measurable", r"""
For $1 \le i \le n$ and $c \in \R$, the half-space $H = \set{x \in \R^n : x_i < c}$ is measurable.
""", r"""
Let $X$ be a test set with $m^*X < \infty$ and let $\eps > 0$. Choose open boxes $B_1, B_2, \dots$ covering $X$ with $\sum_k \abs{B_k} \le m^*X + \eps$.

Fix $k$ and write $B_k = \prod_j (a_j, b_j)$. Then $B_k \cap H$ and $B_k \cap H^c$ are obtained from $B_k$ by replacing the $i$-th interval $(a_i, b_i)$ with $I' = (a_i, b_i) \cap (-\infty, c)$ and $I'' = (a_i, b_i) \cap [c, \infty)$ respectively. Both are bounded intervals, so $B_k \cap H$ and $B_k \cap H^c$ are boxes. Moreover $\abs{I'} + \abs{I''} = b_i - a_i$: if $c \le a_i$ the lengths are $0$ and $b_i - a_i$; if $c \ge b_i$ they are $b_i - a_i$ and $0$; and if $a_i < c < b_i$ they are $c - a_i$ and $b_i - c$. Multiplying by the lengths of the other $n-1$ intervals,
\[ \abs{B_k \cap H} + \abs{B_k \cap H^c} = \abs{B_k}. \]

The boxes $B_k \cap H$ cover $X \cap H$ and the boxes $B_k \cap H^c$ cover $X \cap H^c$. Since any boxes may be used in coverings,
\[ m^*(X \cap H) + m^*(X \cap H^c) \le \sum_k \abs{B_k \cap H} + \sum_k \abs{B_k \cap H^c} = \sum_k \abs{B_k} \le m^*X + \eps. \]
As $\eps$ is arbitrary, $m^*(X \cap H) + m^*(X \cap H^c) \le m^*X$, which is the inequality that needs checking.
""", 3, 30, [
    r"Take an almost optimal covering of the test set by open boxes and cut each box with the hyperplane $x_i = c$.",
    r"Each box splits into two boxes whose volumes add up to the volume of the original, and the two families cover $X \cap H$ and $X \cap H^c$.",
], ["c6-def-measurable", "c6-rem-half-of-condition", "c6-cor-any-boxes"]))

B.append(result("theorem", "c6-thm-boxes-measurable", "Boxes are measurable", r"""
Every box $B \subseteq \R^n$ is measurable, and $mB = \abs{B}$.
""", r"""
Fix $i$ and $c$. The set $\set{x_i < c}$ is measurable by the lemma on half-spaces. Hence so are
\[ \set{x_i \le c} = \bigcap_{k=1}^\infty \set{x_i < c + \tfrac1k}, \qquad \set{x_i > c} = \set{x_i \le c}^c, \qquad \set{x_i \ge c} = \set{x_i < c}^c, \]
because measurable sets form a $\sigma$-algebra.

Let $B = I_1 \times \dots \times I_n$. If some $I_i$ is empty, $B = \emptyset$ is measurable. Otherwise each $I_i$ is a bounded interval with endpoints $a_i \le b_i$, so it is the intersection of one of $(a_i, \infty)$, $[a_i, \infty)$ with one of $(-\infty, b_i)$, $(-\infty, b_i]$. Thus $S_i = \set{x \in \R^n : x_i \in I_i}$ is the intersection of two of the measurable sets above, and $B = S_1 \cap \dots \cap S_n$ is measurable. Finally $mB = m^*B = \abs{B}$ by the theorem that the outer measure of a box is its volume.
""", 2, 20, [
    r"Build a box out of half-spaces using countable set operations.",
    r"$\set{x_i \le c} = \bigcap_k \set{x_i < c + 1/k}$; the other half-spaces are complements; a box is a finite intersection of slabs $\set{x_i \in I_i}$.",
], ["c6-lem-half-space", "c6-thm-sigma-algebra", "c6-prop-measurable-basic", "c6-thm-box-measure"]))

B.append(result("lemma", "c6-lem-open-union-boxes", "Open sets are countable unions of open boxes", r"""
Every open set $U \subseteq \R^n$ is the union of countably many open boxes.
""", r"""
Call an open box \emph{rational} if it has the form $\prod_i (q_i, q_i')$ with all $q_i, q_i' \in \Q$. The rational boxes are indexed by a subset of $\Q^{2n}$, which is countable, so there are countably many of them. Let $\mathcal{B}$ be the set of rational boxes contained in $U$; it is countable, and $\bigcup \mathcal{B} \subseteq U$.

Conversely let $x \in U$. Since $U$ is open there is an $r > 0$ such that every $y$ with $\abs{y - x} < r$ lies in $U$. By the density of $\Q$ in $\R$, choose rationals $q_i, q_i'$ with
\[ x_i - \frac{r}{\sqrt n} < q_i < x_i < q_i' < x_i + \frac{r}{\sqrt n} \qquad (1 \le i \le n). \]
The rational box $R = \prod_i (q_i, q_i')$ contains $x$. If $y \in R$ then $\abs{y_i - x_i} < r/\sqrt n$ for each $i$, so $\abs{y - x} = \bigl( \sum_i (y_i - x_i)^2 \bigr)^{1/2} < r$ and $y \in U$. Thus $R \in \mathcal{B}$ and $x \in \bigcup \mathcal{B}$. Therefore $U = \bigcup \mathcal{B}$.
""", 2, 20, [
    r"There are only countably many boxes with rational endpoints.",
    r"Around each $x \in U$ fit a rational box inside a ball of $U$; a box with sides shorter than $r/\sqrt n$ around $x$ lies in the ball of radius $r$.",
], []))

B.append(result("theorem", "c6-thm-open-closed-measurable", "Open sets and closed sets are measurable", r"""
Every open subset and every closed subset of $\R^n$ is measurable.
""", r"""
An open set is a countable union of open boxes, each box is measurable, and a countable union of measurable sets is measurable. A closed set is the complement of an open set, and complements of measurable sets are measurable.
""", 1, 10, [
    r"Combine the previous lemma with the $\sigma$-algebra property.",
], ["c6-lem-open-union-boxes", "c6-thm-boxes-measurable", "c6-thm-sigma-algebra", "c6-prop-measurable-basic"]))

B.append(note("remark", "c6-rem-borel", "Borel sets", r"""
The smallest $\sigma$-algebra of subsets of $\R^n$ that contains the open sets is called the \emph{Borel $\sigma$-algebra}; its members are the \emph{Borel sets}. They include open sets, closed sets, countable intersections of open sets, countable unions of closed sets, and so on. Since the measurable sets form a $\sigma$-algebra containing the open sets, every Borel set is measurable.
"""))

B.append(note("example", "c6-ex-downward-needs-finite", "Downward continuity needs finite measure", r"""
In $\R$ let $E_j = [j, \infty)$. Each $E_j$ is closed, hence measurable, and $mE_j = \infty$ because $E_j$ contains the interval $[j, j+k]$ of length $k$ for every $k$. The sets decrease and $\bigcap_j E_j = \emptyset$, so $m\bigl(\bigcap_j E_j\bigr) = 0 \ne \infty = \lim_j mE_j$. The hypothesis $mE_1 < \infty$ in downward measure continuity cannot be dropped.
"""))

B.append(result("exercise", "c6-ex-inclusion-exclusion", "Union plus intersection", r"""
Show that for measurable sets $A, E \subseteq \R^n$,
\[ m(A \cup E) + m(A \cap E) = mA + mE. \]
""", r"""
All the sets involved are measurable. The disjoint decompositions $A \cup E = A \sqcup (E \setminus A)$ and $E = (A \cap E) \sqcup (E \setminus A)$ give, by finite additivity,
\[ m(A \cup E) = mA + m(E \setminus A), \qquad mE = m(A \cap E) + m(E \setminus A). \]
If $m(E \setminus A) = \infty$, then $m(A \cup E) = \infty$ and $mE = \infty$, so both sides of the claimed identity are $\infty$. If $m(E \setminus A) < \infty$, add $m(A \cap E)$ to the first equation and substitute the second:
\[ m(A \cup E) + m(A \cap E) = mA + m(E \setminus A) + m(A \cap E) = mA + mE. \]
""", 2, 15, [
    r"Decompose $A \cup E$ and $E$ into disjoint pieces involving $E \setminus A$.",
    r"Be careful not to subtract an infinite quantity; treat $m(E \setminus A) = \infty$ separately.",
], ["c6-lem-two-sets", "c6-lem-finite-additivity"]))

C = [
    card("c6-card-measurable", "c6-def-measurable", r"State Carathéodory's condition for $E \subseteq \R^n$ to be measurable.", r"For every test set $X \subseteq \R^n$: $m^*X = m^*(X \cap E) + m^*(X \cap E^c)$. Only $\ge$ needs proof, and only when $m^*X < \infty$."),
    card("c6-card-sigma-algebra", "c6-def-sigma-algebra", r"Define a $\sigma$-algebra.", r"A collection of subsets containing $\emptyset$, closed under complements and under countable unions (hence countable intersections)."),
    card("c6-card-two-sets-idea", "c6-lem-two-sets", r"Idea of the proof that $E_1 \cup E_2$ is measurable when $E_1, E_2$ are?", r"Cut $X$ by $E_1$, then cut $X \cap E_1^c$ by $E_2$: three pieces whose outer measures sum to $m^*X$. Two of them cover $X \cap (E_1 \cup E_2)$."),
    card("c6-card-countable-additivity", "c6-thm-sigma-algebra", r"State countable additivity of Lebesgue measure, and the key inequality in its proof.", r"For disjoint measurable $E_j$: $m(\bigsqcup_j E_j) = \sum_j mE_j$. Key: $m^*X \ge \sum_{j \le k} m^*(X \cap E_j) + m^*(X \cap E^c)$ for all $k$, from measurability of the finite unions."),
    card("c6-card-continuity", "c6-thm-measure-continuity", r"State upward and downward measure continuity.", r"If $E_j \uparrow$ then $m(\bigcup E_j) = \lim mE_j$. If $E_j \downarrow$ and $mE_1 < \infty$ then $m(\bigcap E_j) = \lim mE_j$."),
    card("c6-card-downward-counterexample", "c6-ex-downward-needs-finite", r"Give an example showing that downward measure continuity needs $mE_1 < \infty$.", r"$E_j = [j, \infty)$: each has infinite measure, but the intersection is empty."),
    card("c6-card-half-space-idea", "c6-lem-half-space", r"Why is a half-space $\set{x_i < c}$ measurable?", r"Cover the test set almost optimally by open boxes; the hyperplane cuts each box into two boxes whose volumes add, covering $X \cap H$ and $X \cap H^c$."),
    card("c6-card-which-measurable", "c6-thm-open-closed-measurable", r"Name the main classes of sets known to be measurable.", r"Zero sets, boxes, open sets, closed sets, and everything obtained from them by countable unions, countable intersections, and complements (all Borel sets)."),
]

write("6-measurability", B, C)
