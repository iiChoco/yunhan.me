from __future__ import annotations

import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from c6common import prose, note, result, card, write

B = []

B.append(prose("c6-int-intro", r"""
The integral of a nonnegative function should be the area under its graph. With Lebesgue measure in hand this can be taken literally: the integral of $f : \R^n \to [0,\infty]$ is the $(n+1)$-dimensional measure of the region under the graph of $f$. Defined this way, the great convergence theorems of Lebesgue become statements about increasing and decreasing sequences of sets, and they follow from measure continuity.

Conventions for this section. Functions take values in $[0, \infty]$ unless said otherwise, with $c \cdot \infty = \infty$ for $c > 0$ and $0 \cdot \infty = 0$. Points of $\R^{n+1} = \R^n \times \R$ are written $(x, y)$ with $x \in \R^n$, $y \in \R$. The letter $m$ denotes Lebesgue measure both in $\R^n$ and in $\R^{n+1}$; the set being measured tells which. An open box in $\R^{n+1}$ is a product $B' \times J$ of an open box $B' \subseteq \R^n$ and an open interval $J$, and its volume is $\abs{B'}\,\abs{J}$.
"""))

B.append(note("definition", "c6-def-integral", "Undergraph, measurable function, Lebesgue integral", r"""
The \emph{undergraph} of $f : \R^n \to [0, \infty]$ is
\[ \mathcal{U}f = \set{ (x, y) \in \R^n \times \R : 0 \le y < f(x) }. \]
The function $f$ is \emph{(Lebesgue) measurable} if $\mathcal{U}f$ is a measurable subset of $\R^{n+1}$. In that case the \emph{Lebesgue integral} of $f$ is
\[ \int f = m(\mathcal{U}f) \in [0, \infty], \]
and $f$ is \emph{integrable} if $\int f < \infty$.
"""))

B.append(result("proposition", "c6-prop-integral-monotone", "The integral is monotone", r"""
If $f, g : \R^n \to [0,\infty]$ are measurable and $f(x) \le g(x)$ for all $x$, then $\int f \le \int g$.
""", r"""
If $0 \le y < f(x)$ then $0 \le y < g(x)$, so $\mathcal{U}f \subseteq \mathcal{U}g$. Both sets are measurable, and measure is monotone, so $\int f = m(\mathcal{U}f) \le m(\mathcal{U}g) = \int g$.
""", 1, 5, [
    r"Compare the undergraphs.",
], ["c6-def-integral", "c6-prop-measure-difference"]))

B.append(result("theorem", "c6-thm-mct", "Monotone convergence theorem", r"""
Let $f_k : \R^n \to [0, \infty]$ be measurable functions with $f_1(x) \le f_2(x) \le \cdots$ for every $x$, and let $f(x) = \lim_{k} f_k(x) = \sup_k f_k(x)$. Then $f$ is measurable and
\[ \int f = \lim_{k \to \infty} \int f_k . \]
""", r"""
Since $f_k \le f_{k+1} \le f$, we have $\mathcal{U}f_k \subseteq \mathcal{U}f_{k+1} \subseteq \mathcal{U}f$. Conversely let $(x, y) \in \mathcal{U}f$, so $0 \le y < f(x) = \sup_k f_k(x)$. As $y$ is less than the supremum, $y < f_k(x)$ for some $k$, that is, $(x, y) \in \mathcal{U}f_k$. Hence
\[ \mathcal{U}f = \bigcup_{k=1}^\infty \mathcal{U}f_k \]
is an increasing union of measurable sets. It is therefore measurable, and by upward measure continuity $m(\mathcal{U}f) = \lim_k m(\mathcal{U}f_k)$, which is the assertion.
""", 2, 15, [
    r"What is the relation between the undergraphs $\mathcal{U}f_k$ and $\mathcal{U}f$?",
    r"Show $\mathcal{U}f = \bigcup_k \mathcal{U}f_k$, an increasing union; the strict inequality $y < f(x)$ in the definition of the undergraph is what makes this work.",
], ["c6-def-integral", "c6-thm-measure-continuity", "c6-thm-sigma-algebra"]))

B.append(prose("c6-int-cylinder-prose", r"""
To compute any integral at all we must know the measure of the simplest undergraphs, the \emph{cylinders} $E \times [0, c)$ over a set $E \subseteq \R^n$. The answer is height times base, as it should be, but it takes some work, because it compares measure in two different dimensions. The next four lemmas do this.
"""))

B.append(result("lemma", "c6-lem-cylinder-upper", "Cylinders: upper bound", r"""
Let $A \subseteq \R^n$ and let $J \subseteq \R$ be a bounded interval. Then, as subsets of $\R^{n+1}$,
\[ m^*(A \times J) \le \abs{J}\, m^*A . \]
(With $0 \cdot \infty = 0$: if $\abs{J} = 0$ then $A \times J$ is a zero set.)
""", r"""
\emph{Case $m^*A < \infty$.} Let $\eps > 0$ and choose open boxes $B_k \subseteq \R^n$ covering $A$ with $\sum_k \abs{B_k} \le m^*A + \eps$. The sets $B_k \times J$ are boxes in $\R^{n+1}$ of volume $\abs{B_k}\abs{J}$, and they cover $A \times J$. Since any boxes may be used in coverings,
\[ m^*(A \times J) \le \sum_k \abs{B_k}\abs{J} \le \abs{J}\,(m^*A + \eps). \]
Let $\eps \to 0$.

\emph{Case $m^*A = \infty$.} If $\abs{J} > 0$ the right side is $\infty$. If $\abs{J} = 0$, then $J$ is empty or a single point $\set{c}$, so $A \times J$ is contained in the coordinate hyperplane $\set{(x,y) : y = c}$ of $\R^{n+1}$ (or is empty), which is a zero set. So $m^*(A \times J) = 0$.
""", 2, 15, [
    r"Multiply each box of a covering of $A$ by $J$.",
], ["c6-cor-any-boxes", "c6-prop-hyperplane-zero"]))

B.append(result("lemma", "c6-lem-cylinder-measurable", "Cylinders over measurable sets", r"""
Let $E \subseteq \R^n$ be measurable and let $J \subseteq \R$ be a bounded interval. Then $E \times \R$ and $E \times J$ are measurable subsets of $\R^{n+1}$, and
\[ m(E \times J) = \abs{J}\, mE . \]
""", r"""
\emph{Step 1: $E \times \R$ is measurable.} Let $X \subseteq \R^{n+1}$ with $m^*X < \infty$ and $\eps > 0$. Choose open boxes $B_k' \times J_k$ of $\R^{n+1}$ covering $X$ with $\sum_k \abs{B_k'}\abs{J_k} \le m^*X + \eps$. Then
\[ X \cap (E \times \R) \subseteq \bigcup_k (B_k' \cap E) \times J_k, \qquad X \setminus (E \times \R) \subseteq \bigcup_k (B_k' \setminus E) \times J_k . \]
By subadditivity and the upper bound for cylinders,
\[ m^*(X \cap (E \times \R)) + m^*(X \setminus (E \times \R)) \le \sum_k \abs{J_k} \bigl[ m^*(B_k' \cap E) + m^*(B_k' \setminus E) \bigr] = \sum_k \abs{J_k}\abs{B_k'} \le m^*X + \eps, \]
where the equality uses the measurability of $E$ with the test set $B_k'$ and $m^*B_k' = \abs{B_k'}$. Letting $\eps \to 0$ gives the inequality required for measurability.

\emph{Step 2: $E \times J$ is measurable.} The set $\R^n \times J = \bigcup_k \bigl( [-k,k]^n \times J \bigr)$ is a countable union of boxes, hence measurable, and $E \times J = (E \times \R) \cap (\R^n \times J)$.

\emph{Step 3: the measure, for bounded $E$.} Suppose $E \subseteq C$ for a box $C \subseteq \R^n$. The box $C \times J$ is the disjoint union of the measurable sets $E \times J$ and $(C \setminus E) \times J$ (the latter is measurable by Step 2 applied to $C \setminus E$). So, using the upper bound for cylinders,
\[ \abs{C}\abs{J} = m(E \times J) + m((C \setminus E) \times J) \le \abs{J}\, mE + \abs{J}\, m(C \setminus E) = \abs{J}\abs{C}. \]
All quantities are finite and each of the two terms on the left is at most the corresponding term on the right, so equality holds termwise: $m(E \times J) = \abs{J}\, mE$.

\emph{Step 4: general $E$.} Let $E_k = E \cap [-k,k]^n$. Then $E_k$ increases to $E$ and $E_k \times J$ increases to $E \times J$. By upward measure continuity in $\R^{n+1}$ and in $\R^n$, and Step 3,
\[ m(E \times J) = \lim_k m(E_k \times J) = \lim_k \abs{J}\, mE_k = \abs{J}\, mE . \]
(If $\abs{J} = 0$ every term is $0$.)
""", 4, 60, [
    r"First show $E \times \R$ is measurable: cover a test set in $\R^{n+1}$ by boxes $B' \times J'$ and split each along $E$ using the measurability of $E$ in $\R^n$.",
    r"For the measure, the upper bound $m(E \times J) \le \abs{J}\,mE$ is already known. For bounded $E$ inside a box $C$, apply the upper bound to both $E$ and $C \setminus E$ and compare with the volume of $C \times J$.",
    r"Pass from bounded to general $E$ by upward measure continuity.",
], ["c6-lem-cylinder-upper", "c6-def-measurable", "c6-rem-half-of-condition", "c6-thm-boxes-measurable", "c6-thm-sigma-algebra", "c6-lem-finite-additivity", "c6-thm-measure-continuity"]))

B.append(result("lemma", "c6-lem-cylinder-lower", "Cylinders: the outer measure of an arbitrary base", r"""
For every set $A \subseteq \R^n$ (measurable or not),
\[ m^*\bigl( A \times [0,1) \bigr) = m^*A . \]
""", r"""
The inequality $\le$ is the upper bound for cylinders. For $\ge$, assume $m^*(A \times [0,1)) < \infty$, let $\eps > 0$ and $0 < \delta < 1$. Choose open boxes $B_k' \times J_k$ in $\R^{n+1}$ covering $A \times [0,1)$ with
\[ \sum_{k=1}^\infty \abs{B_k'}\abs{J_k} \le m^*(A \times [0,1)) + \eps. \]
For $N \in \N$ and $x \in \R^n$ let
\[ g_N(x) = \sum_{k \le N,\; x \in B_k'} \abs{J_k}, \qquad W_N = \set{ x \in \R^n : g_N(x) > 1 - \delta }. \]

\emph{Claim 1: $A \subseteq \bigcup_N W_N$, and $W_N \subseteq W_{N+1}$.} Let $x \in A$. Every point $(x, t)$ with $t \in [0,1)$ lies in some $B_k' \times J_k$, so the open intervals $J_k$ with $x \in B_k'$ cover $[0,1)$. By the definition of outer measure in $\R$ and $m^*[0,1) = 1$, the sum of $\abs{J_k}$ over all $k$ with $x \in B_k'$ is at least $1 > 1 - \delta$. This sum is $\lim_N g_N(x)$, so $g_N(x) > 1 - \delta$ for some $N$. The inclusion $W_N \subseteq W_{N+1}$ holds because $g_N \le g_{N+1}$.

\emph{Claim 2: $W_N$ is measurable and $(1 - \delta)\, mW_N \le \sum_{k \le N} \abs{B_k'}\abs{J_k}$.} For each nonempty $S \subseteq \set{1, \dots, N}$ let
\[ E_S = \set{ x : \text{for } k \le N, \ x \in B_k' \iff k \in S } = \bigcap_{k \in S} B_k' \;\cap \bigcap_{k \le N,\, k \notin S} (B_k')^c . \]
These finitely many sets are measurable, pairwise disjoint, and of finite measure. On $E_S$ the function $g_N$ has the constant value $c_S = \sum_{k \in S} \abs{J_k}$, and $g_N = 0$ outside $\bigcup_S E_S$. Hence $W_N$ is the disjoint union of the $E_S$ with $c_S > 1 - \delta$, so it is measurable. For each $k \le N$, $B_k'$ is the disjoint union of the $E_S$ with $k \in S$, so $\abs{B_k'} = \sum_{S \ni k} mE_S$ by finite additivity. Therefore
\[ \sum_{k \le N} \abs{J_k}\abs{B_k'} = \sum_{k \le N} \sum_{S \ni k} \abs{J_k}\, mE_S = \sum_S c_S\, mE_S \ge (1 - \delta) \sum_{S :\, c_S > 1 - \delta} mE_S = (1 - \delta)\, mW_N . \]

\emph{Conclusion.} By Claim 1, monotonicity, and upward measure continuity, then Claim 2,
\[ m^*A \le m\Bigl( \bigcup_N W_N \Bigr) = \lim_{N} mW_N \le \frac{1}{1 - \delta} \sum_{k=1}^\infty \abs{B_k'}\abs{J_k} \le \frac{ m^*(A \times [0,1)) + \eps }{1 - \delta}. \]
Letting $\eps \to 0$ and $\delta \to 0$ gives $m^*A \le m^*(A \times [0,1))$.
""", 5, 100, [
    r"Take an almost optimal covering of $A \times [0,1)$ by open boxes $B_k' \times J_k$. Over a fixed $x \in A$, the intervals $J_k$ with $x \in B_k'$ cover $[0,1)$, so their lengths add up to at least $1$.",
    r"Consider the function $g(x) = \sum_{k :\, x \in B_k'} \abs{J_k}$ and its partial sums $g_N$. The set where $g_N > 1 - \delta$ is a finite union of pieces cut out by the first $N$ boxes, hence measurable, and these sets increase to a set containing $A$.",
    r"Prove a Chebyshev-type bound $(1 - \delta)\, m\set{g_N > 1 - \delta} \le \sum_{k \le N} \abs{B_k'}\abs{J_k}$ by splitting $\R^n$ into the finitely many sets on which membership in each of $B_1', \dots, B_N'$ is fixed. Finish with upward measure continuity.",
], ["c6-lem-cylinder-upper", "c6-thm-box-measure", "c6-def-outer-measure", "c6-prop-outer-basic", "c6-lem-two-sets", "c6-thm-boxes-measurable", "c6-lem-finite-additivity", "c6-thm-measure-continuity"]))

B.append(result("lemma", "c6-lem-cylinder-slice", "A measurable cylinder has a measurable base", r"""
Let $A \subseteq \R^n$. If $A \times [0,1)$ is a measurable subset of $\R^{n+1}$, then $A$ is a measurable subset of $\R^n$.
""", r"""
Let $C_k = [-k,k]^n$ and $A_k = A \cap C_k$; since $A = \bigcup_k A_k$ it suffices to show each $A_k$ is measurable. Fix $k$. The box $C_k \times [0,1)$ is measurable in $\R^{n+1}$, so
\[ A_k \times [0,1) = (A \times [0,1)) \cap (C_k \times [0,1)) \quad \text{and} \quad (C_k \setminus A_k) \times [0,1) = (C_k \times [0,1)) \setminus (A_k \times [0,1)) \]
are measurable, disjoint, and have union $C_k \times [0,1)$. By additivity, and then the lemma on the outer measure of a cylinder with arbitrary base,
\[ \abs{C_k} = m(A_k \times [0,1)) + m((C_k \setminus A_k) \times [0,1)) = m^*A_k + m^*(C_k \setminus A_k). \]
Thus $A_k$ divides the box $C_k$ cleanly, and so $A_k$ is measurable by the criterion for subsets of a box.
""", 3, 25, [
    r"Reduce to bounded pieces $A \cap [-k,k]^n$ and use the criterion that a subset of a box is measurable iff it divides the box cleanly.",
    r"Additivity in $\R^{n+1}$ for the two measurable cylinders over $A_k$ and $C_k \setminus A_k$, together with $m^*(\,\cdot \times [0,1)) = m^*(\cdot)$, gives $\abs{C_k} = m^*A_k + m^*(C_k \setminus A_k)$.",
], ["c6-lem-cylinder-lower", "c6-cor-clean-box", "c6-thm-boxes-measurable", "c6-lem-finite-additivity", "c6-thm-sigma-algebra"]))

B.append(note("definition", "c6-def-simple", "Characteristic and simple functions", r"""
The \emph{characteristic function} of a set $E \subseteq \R^n$ is $\chi_E(x) = 1$ for $x \in E$ and $\chi_E(x) = 0$ for $x \notin E$. A \emph{simple function} is a function of the form
\[ \varphi = \sum_{i=1}^r c_i \chi_{E_i} \]
where $E_1, \dots, E_r \subseteq \R^n$ are pairwise disjoint measurable sets and $c_1, \dots, c_r \in [0, \infty)$. So $\varphi$ takes the value $c_i$ on $E_i$ and $0$ off $\bigcup_i E_i$.
"""))

B.append(result("proposition", "c6-prop-simple-integral", "Integral of a simple function", r"""
A simple function $\varphi = \sum_{i=1}^r c_i \chi_{E_i}$ (with the $E_i$ pairwise disjoint and measurable, $c_i \in [0,\infty)$) is measurable, and
\[ \int \varphi = \sum_{i=1}^r c_i\, mE_i . \]
In particular $\int \chi_E = mE$ for every measurable $E \subseteq \R^n$, and $\int \chi_{\Q} = 0$ on $\R$.
""", r"""
If $(x, y) \in \mathcal{U}\varphi$ then $\varphi(x) > y \ge 0$, so $x$ lies in exactly one $E_i$, and $0 \le y < c_i$. Conversely if $x \in E_i$ and $0 \le y < c_i$ then $(x,y) \in \mathcal{U}\varphi$. Hence
\[ \mathcal{U}\varphi = \bigsqcup_{i=1}^r E_i \times [0, c_i), \]
a disjoint union because the $E_i$ are disjoint. Each cylinder $E_i \times [0, c_i)$ is measurable with measure $c_i\, mE_i$ by the lemma on cylinders over measurable sets. So $\mathcal{U}\varphi$ is measurable and by finite additivity $\int \varphi = \sum_i c_i\, mE_i$. The case $r = 1$, $c_1 = 1$ gives $\int \chi_E = mE$, and $m\Q = 0$ since $\Q$ is a zero set.
""", 2, 15, [
    r"Describe the undergraph of $\varphi$ as a union of cylinders.",
], ["c6-def-simple", "c6-def-integral", "c6-lem-cylinder-measurable", "c6-lem-finite-additivity"]))

B.append(result("theorem", "c6-thm-scaling-integral", "Scaling the integrand", r"""
Let $f : \R^n \to [0, \infty]$ be measurable and $c \in [0, \infty)$. Then $cf$ is measurable and $\int cf = c \int f$.
""", r"""
If $c = 0$ then $cf = 0$, $\mathcal{U}(cf) = \emptyset$, and $\int cf = 0 = 0 \cdot \int f$. Let $c > 0$ and let $D : \R^{n+1} \to \R^{n+1}$ be the diagonal map $D(x, y) = (x, cy)$. For any $(x, y)$,
\[ (x, y) \in \mathcal{U}f \iff 0 \le y < f(x) \iff 0 \le cy < c f(x) \iff D(x,y) \in \mathcal{U}(cf), \]
which is valid also when $f(x) = \infty$. As $D$ is a bijection, $\mathcal{U}(cf) = D(\mathcal{U}f)$. By the theorem on diagonal maps, $D$ is a meseomorphism that multiplies measure by $\abs{1 \cdots 1 \cdot c} = c$. Hence $\mathcal{U}(cf)$ is measurable and $\int cf = m(D\,\mathcal{U}f) = c\, m(\mathcal{U}f) = c \int f$.
""", 2, 15, [
    r"The undergraph of $cf$ is the image of the undergraph of $f$ under a linear map of $\R^{n+1}$.",
], ["c6-def-integral", "c6-thm-diagonal"]))

B.append(prose("c6-int-completed-prose", r"""
The undergraph uses the strict inequality $y < f(x)$, which suits increasing limits. Decreasing limits and infima are better served by the non-strict inequality. Fortunately the choice does not matter.
"""))

B.append(result("proposition", "c6-prop-completed-undergraph", "The completed undergraph", r"""
The \emph{completed undergraph} of $f : \R^n \to [0, \infty]$ is $\widehat{\mathcal{U}}f = \set{(x, y) \in \R^n \times \R : 0 \le y \le f(x)}$. The function $f$ is measurable if and only if $\widehat{\mathcal{U}}f$ is a measurable subset of $\R^{n+1}$, and then $m(\widehat{\mathcal{U}}f) = \int f$.
""", r"""
Let $H_0 = \R^n \times \set{0}$, a coordinate hyperplane in $\R^{n+1}$ and hence a zero set, all of whose subsets are measurable zero sets. For $c > 0$ let $D_c(x, y) = (x, cy)$, a diagonal map, hence a meseomorphism multiplying measure by $c$. As in the proof of the scaling theorem, $D_c(\mathcal{U}f) = \mathcal{U}(cf)$, and in the same way $D_c(\widehat{\mathcal{U}}f) = \widehat{\mathcal{U}}(cf)$.

\emph{Claim 1:} $\widehat{\mathcal{U}}f = H_0 \cup \bigcap_{k=1}^\infty \mathcal{U}\bigl( (1 + \tfrac1k) f \bigr)$. First, $H_0 \subseteq \widehat{\mathcal{U}}f$ since $f \ge 0$. If $0 \le y < (1 + \tfrac1k) f(x)$ for all $k$, then letting $k \to \infty$ gives $y \le f(x)$ (trivially if $f(x) = \infty$), so the right side is contained in the left. Conversely let $0 \le y \le f(x)$. If $y = 0$ then $(x, y) \in H_0$. If $y > 0$ then $f(x) > 0$ and $y \le f(x) < (1 + \tfrac1k) f(x)$ for all $k$ when $f(x) < \infty$, while $y < \infty = (1 + \tfrac1k) f(x)$ when $f(x) = \infty$.

\emph{Claim 2:} $\mathcal{U}f = Z \cup \Bigl( \set{(x,y) : y > 0} \cap \bigcup_{k=2}^\infty \widehat{\mathcal{U}}\bigl( (1 - \tfrac1k) f \bigr) \Bigr)$, where $Z = \set{(x, 0) : f(x) > 0} \subseteq H_0$. If $(x, y) \in \mathcal{U}f$ and $y = 0$ then $(x,y) \in Z$. If $(x,y) \in \mathcal{U}f$ and $y > 0$, then either $f(x) = \infty$ and $y \le (1 - \tfrac12) f(x)$, or $f(x) < \infty$ and $y / f(x) < 1$, so $y \le (1 - \tfrac1k) f(x)$ for $k$ large. Conversely, $Z \subseteq \mathcal{U}f$; and if $0 < y \le (1 - \tfrac1k) f(x)$ for some $k \ge 2$, then $f(x) > 0$ and $y < f(x)$.

\emph{Measurability.} If $\mathcal{U}f$ is measurable, so is each $\mathcal{U}((1 + \tfrac1k)f) = D_{1 + 1/k}(\mathcal{U}f)$, and Claim 1 shows $\widehat{\mathcal{U}}f$ is measurable. If $\widehat{\mathcal{U}}f$ is measurable, so is each $\widehat{\mathcal{U}}((1 - \tfrac1k)f) = D_{1 - 1/k}(\widehat{\mathcal{U}}f)$; the half-space $\set{y > 0}$ is measurable (as shown in the proof that boxes are measurable) and $Z$ is a zero set; so Claim 2 shows $\mathcal{U}f$ is measurable.

\emph{Measure.} Since $\mathcal{U}f \subseteq \widehat{\mathcal{U}}f$, $\int f \le m(\widehat{\mathcal{U}}f)$; this settles the case $\int f = \infty$. If $\int f < \infty$, Claim 1 gives for every $k$
\[ m(\widehat{\mathcal{U}}f) \le mH_0 + m\bigl( \mathcal{U}((1 + \tfrac1k) f) \bigr) = \bigl(1 + \tfrac1k\bigr) \int f, \]
and letting $k \to \infty$ gives $m(\widehat{\mathcal{U}}f) \le \int f$.
""", 4, 50, [
    r"Stretching vertically by a factor slightly greater than $1$ pushes the undergraph past the graph; shrinking by a factor slightly less than $1$ pulls the completed undergraph strictly below it. Vertical stretches are diagonal maps.",
    r"Express $\widehat{\mathcal{U}}f$ through the sets $\mathcal{U}((1 + \tfrac1k) f)$ and $\mathcal{U}f$ through the sets $\widehat{\mathcal{U}}((1 - \tfrac1k) f)$. Watch the points with $y = 0$: they lie in a hyperplane, a zero set.",
    r"For the measure, $\mathcal{U}f \subseteq \widehat{\mathcal{U}}f \subseteq H_0 \cup \mathcal{U}((1 + \tfrac1k) f)$ and $\int (1 + \tfrac1k) f = (1 + \tfrac1k) \int f$.",
], ["c6-def-integral", "c6-thm-diagonal", "c6-thm-scaling-integral", "c6-prop-hyperplane-zero", "c6-prop-measurable-basic", "c6-thm-boxes-measurable", "c6-thm-sigma-algebra"]))

B.append(result("proposition", "c6-prop-sup-inf", "Suprema, infima, and limits of measurable functions", r"""
Let $f_k : \R^n \to [0, \infty]$ be measurable for $k \in \N$. Then $\sup_k f_k$, $\inf_k f_k$, $\limsup_k f_k$ and $\liminf_k f_k$ (all defined pointwise) are measurable. In particular, if $f_k(x) \to f(x)$ for every $x$, then $f$ is measurable.
""", r"""
\emph{Supremum.} $0 \le y < \sup_k f_k(x)$ holds if and only if $0 \le y < f_k(x)$ for some $k$. So $\mathcal{U}(\sup_k f_k) = \bigcup_k \mathcal{U}f_k$ is measurable.

\emph{Infimum.} $0 \le y \le \inf_k f_k(x)$ holds if and only if $0 \le y \le f_k(x)$ for all $k$. So $\widehat{\mathcal{U}}(\inf_k f_k) = \bigcap_k \widehat{\mathcal{U}}f_k$, which is measurable because each $\widehat{\mathcal{U}}f_k$ is, by the proposition on the completed undergraph; by the same proposition $\inf_k f_k$ is measurable.

\emph{Upper and lower limits.} By definition $\limsup_k f_k = \inf_k \bigl( \sup_{j \ge k} f_j \bigr)$ and $\liminf_k f_k = \sup_k \bigl( \inf_{j \ge k} f_j \bigr)$, and these are measurable by the two cases already proved. If $f_k \to f$ pointwise then $f = \limsup_k f_k$.
""", 2, 20, [
    r"The undergraph of a supremum is a union of undergraphs. For an infimum, the strict inequality gets in the way; use the completed undergraph.",
], ["c6-def-integral", "c6-prop-completed-undergraph", "c6-thm-sigma-algebra"]))

B.append(result("theorem", "c6-thm-fatou", "Fatou's lemma", r"""
If $f_k : \R^n \to [0, \infty]$ are measurable, then
\[ \int \liminf_{k \to \infty} f_k \;\le\; \liminf_{k \to \infty} \int f_k . \]
""", r"""
Let $g_k = \inf_{j \ge k} f_j$. Each $g_k$ is measurable, $g_1 \le g_2 \le \cdots$, and $\lim_k g_k = \sup_k g_k = \liminf_k f_k$. By the monotone convergence theorem,
\[ \int \liminf_k f_k = \lim_{k} \int g_k . \]
For $j \ge k$ we have $g_k \le f_j$, hence $\int g_k \le \int f_j$ by monotonicity of the integral; so $\int g_k \le \inf_{j \ge k} \int f_j$. The right side increases with $k$ to $\liminf_k \int f_k$. Taking limits in $k$ gives $\lim_k \int g_k \le \liminf_k \int f_k$.
""", 3, 25, [
    r"The lower limit is the increasing limit of the functions $g_k = \inf_{j \ge k} f_j$.",
    r"Apply monotone convergence to $g_k$, and compare $\int g_k$ with $\int f_j$ for each $j \ge k$.",
], ["c6-thm-mct", "c6-prop-sup-inf", "c6-prop-integral-monotone"]))

B.append(note("example", "c6-ex-fatou-strict", "Mass can escape", r"""
On $\R$ let $f_k = \chi_{[k, k+1]}$. Then $\int f_k = 1$ for every $k$, while $f_k(x) \to 0$ for every $x$. So $\int \lim f_k = 0 < 1 = \lim \int f_k$: the inequality in Fatou's lemma can be strict, and pointwise convergence alone does not allow the limit and the integral to be interchanged. The same happens for the tall narrow spikes $k\chi_{(0, 1/k)}$. The dominated convergence theorem says that this is prevented when all the $f_k$ stay below one integrable function.
"""))

B.append(result("theorem", "c6-thm-dct", "Dominated convergence theorem", r"""
Let $f_k : \R^n \to [0, \infty]$ be measurable functions such that $f_k(x) \to f(x)$ for every $x$. Suppose there is a measurable $g : \R^n \to [0, \infty]$ with $\int g < \infty$ and $f_k \le g$ for all $k$. Then $f$ is measurable and
\[ \int f = \lim_{k \to \infty} \int f_k . \]
""", r"""
Let $h_k = \inf_{j \ge k} f_j$ and $H_k = \sup_{j \ge k} f_j$. These are measurable, $h_k \le f_k \le H_k \le g$, the $h_k$ increase to $\liminf_k f_k = f$, and the $H_k$ decrease to $\limsup_k f_k = f$. Also $f$ is measurable, and $f \le g$, so all the integrals below are at most $\int g < \infty$.

\emph{Lower envelopes.} By the monotone convergence theorem, $\int h_k \to \int f$.

\emph{Upper envelopes.} The completed undergraphs $\widehat{\mathcal{U}}H_k$ are measurable and decrease with $k$. A point $(x, y)$ lies in all of them if and only if $0 \le y \le H_k(x)$ for all $k$, that is, $0 \le y \le \inf_k H_k(x) = f(x)$. So $\bigcap_k \widehat{\mathcal{U}}H_k = \widehat{\mathcal{U}}f$. Moreover $m(\widehat{\mathcal{U}}H_1) \le m(\widehat{\mathcal{U}}g) = \int g < \infty$. By downward measure continuity and the proposition on the completed undergraph,
\[ \int H_k = m(\widehat{\mathcal{U}}H_k) \longrightarrow m(\widehat{\mathcal{U}}f) = \int f . \]

\emph{Squeeze.} By monotonicity of the integral, $\int h_k \le \int f_k \le \int H_k$, and both outer sequences converge to the finite number $\int f$. Hence $\int f_k \to \int f$.
""", 4, 50, [
    r"Trap $f_k$ between $h_k = \inf_{j \ge k} f_j$ and $H_k = \sup_{j \ge k} f_j$, which converge monotonically to $f$.",
    r"The increasing sequence is handled by monotone convergence. For the decreasing one, look at the completed undergraphs $\widehat{\mathcal{U}}H_k$: they decrease to $\widehat{\mathcal{U}}f$.",
    r"Downward measure continuity needs a set of finite measure to start from; this is exactly what the dominating function $g$ provides.",
], ["c6-thm-mct", "c6-prop-sup-inf", "c6-prop-completed-undergraph", "c6-thm-measure-continuity", "c6-prop-integral-monotone"]))

B.append(prose("c6-int-linearity-prose", r"""
The undergraph of $f + g$ is not the union of the undergraphs of $f$ and $g$, so additivity of the integral is not visible from the definition. We prove it by approximating with simple functions, for which it is bookkeeping. This requires knowing that the sets $\set{f > a} = \set{x : f(x) > a}$ are measurable, which is where the lemmas on cylinders are used.
"""))

B.append(result("theorem", "c6-thm-preimage", "Measurability in terms of superlevel sets", r"""
A function $f : \R^n \to [0, \infty]$ is measurable if and only if for every $a \ge 0$ the set $\set{f > a} = \set{x \in \R^n : f(x) > a}$ is a measurable subset of $\R^n$.
""", r"""
\emph{Superlevel sets measurable $\Rightarrow$ $f$ measurable.} We claim
\[ \mathcal{U}f = \bigcup_{q \in \Q,\ q > 0} \set{f > q} \times [0, q). \]
If $0 \le y < q < f(x)$ then $(x, y) \in \mathcal{U}f$. Conversely if $0 \le y < f(x)$, choose a rational $q$ with $y < q < f(x)$; then $x \in \set{f > q}$ and $y \in [0, q)$. Each set $\set{f > q} \times [0, q)$ is measurable by the lemma on cylinders over measurable sets, and the union is countable.

\emph{$f$ measurable $\Rightarrow$ superlevel sets measurable.} Fix $a \ge 0$ and put $A = \set{f > a}$. For $k \in \N$ the set $\R^n \times [a, a + \tfrac1k)$ is measurable (a cylinder over $\R^n$), so
\[ S_k = \mathcal{U}f \cap \bigl( \R^n \times [a, a + \tfrac1k) \bigr) = \set{ (x, y) : a \le y < a + \tfrac1k, \ y < f(x) } \]
is measurable. The map $\Phi_k(x, y) = (x, k(y - a))$ is a translation followed by a diagonal map, so it is a meseomorphism of $\R^{n+1}$. Writing $t = k(y - a)$, that is, $y = a + t/k$,
\[ P_k := \Phi_k(S_k) = \set{ (x, t) : 0 \le t < 1, \ a + t/k < f(x) } \]
is measurable. We claim $\bigcup_k P_k = A \times [0,1)$. If $(x, t) \in P_k$ then $f(x) > a + t/k \ge a$, so $x \in A$. Conversely if $f(x) > a$ and $0 \le t < 1$, choose $k$ with $t/k < f(x) - a$ (any $k$ if $f(x) = \infty$); then $(x, t) \in P_k$. Thus $A \times [0,1)$ is measurable in $\R^{n+1}$, and by the lemma that a measurable cylinder has a measurable base, $A$ is measurable in $\R^n$.
""", 4, 60, [
    r"One direction: write the undergraph as a countable union of cylinders over the sets $\set{f > q}$, $q$ rational.",
    r"Other direction: the thin horizontal slab of $\mathcal{U}f$ between heights $a$ and $a + 1/k$ is measurable. Stretch it vertically to height $1$.",
    r"The stretched slabs increase to the cylinder $\set{f > a} \times [0,1)$; now use the lemma that a measurable cylinder has a measurable base.",
], ["c6-def-integral", "c6-lem-cylinder-measurable", "c6-lem-cylinder-slice", "c6-thm-translation", "c6-thm-diagonal", "c6-thm-sigma-algebra"]))

B.append(note("remark", "c6-rem-other-level-sets", "Other level sets", r"""
If $f : \R^n \to [0,\infty]$ is measurable, then so are the sets $\set{f \ge a} = \bigcap_k \set{f > a - \tfrac1k}$ (for $a > 0$, taking $k > 1/a$), $\set{f < a}$, $\set{f \le a}$, $\set{a < f \le b}$, and $\set{f = \infty} = \bigcap_k \set{f > k}$, since measurable sets form a $\sigma$-algebra. In the same way, $f$ is measurable if and only if the preimage of every interval is measurable. This is the usual textbook definition of a measurable function.
"""))

B.append(result("lemma", "c6-lem-simple-approx", "Approximation by simple functions", r"""
Let $f : \R^n \to [0, \infty]$ be measurable. Then there are simple functions $\varphi_1 \le \varphi_2 \le \cdots$ with $\varphi_k(x) \to f(x)$ for every $x \in \R^n$.
""", r"""
For $k \in \N$ and $x \in \R^n$ let $N_k(x)$ be the number of $j \in \set{1, 2, \dots, k 2^k}$ with $j 2^{-k} < f(x)$, and let $\varphi_k(x) = 2^{-k} N_k(x)$.

\emph{$\varphi_k$ is simple.} Let $A_j = \set{f > j 2^{-k}}$ for $1 \le j \le k2^k$; these are measurable by the theorem on superlevel sets, and $A_1 \supseteq A_2 \supseteq \cdots$. Hence $N_k(x) = c$ exactly when $x \in A_c \setminus A_{c+1}$ (for $1 \le c < k2^k$) or $x \in A_{k 2^k}$ (for $c = k2^k$). These sets are measurable and pairwise disjoint, so $\varphi_k = \sum_{c=1}^{k2^k - 1} c2^{-k} \chi_{A_c \setminus A_{c+1}} + k \chi_{A_{k2^k}}$ is simple.

\emph{$\varphi_k \le \varphi_{k+1}$.} If $j$ is counted in $N_k(x)$, that is, $1 \le j \le k2^k$ and $j2^{-k} < f(x)$, then $2j - 1$ and $2j$ are both counted in $N_{k+1}(x)$: they lie in $\set{1, \dots, (k+1) 2^{k+1}}$ and $(2j - 1) 2^{-k-1} < 2j \cdot 2^{-k-1} = j 2^{-k} < f(x)$. Distinct $j$ give distinct pairs, so $N_{k+1}(x) \ge 2 N_k(x)$ and $\varphi_{k+1}(x) = 2^{-k-1} N_{k+1}(x) \ge 2^{-k} N_k(x) = \varphi_k(x)$.

\emph{$\varphi_k(x) \to f(x)$.} The $j$ counted in $N_k(x)$ are $1, 2, \dots, N_k(x)$. If $f(x) = \infty$, all $j$ are counted and $\varphi_k(x) = k \to \infty$. Suppose $f(x) < \infty$. If $N_k(x) \ge 1$, then $\varphi_k(x) = N_k(x) 2^{-k} < f(x)$; in any case $\varphi_k(x) \le f(x)$. For $k > f(x)$ we have $N_k(x) < k 2^k$, so $j = N_k(x) + 1$ is in the range and is not counted: $(N_k(x) + 1) 2^{-k} \ge f(x)$. Therefore $0 \le f(x) - \varphi_k(x) \le 2^{-k}$ for all $k > f(x)$, and $\varphi_k(x) \to f(x)$.
""", 3, 40, [
    r"Round $f$ down to a multiple of $2^{-k}$ and cut it off at height $k$.",
    r"The rounded function takes finitely many values, on sets of the form $\set{a < f \le b}$ or $\set{f > k}$, which are measurable by the theorem on superlevel sets.",
    r"Halving the mesh refines the rounding, which gives monotonicity; for $k > f(x)$ the error is at most $2^{-k}$.",
], ["c6-thm-preimage", "c6-def-simple"]))

B.append(result("theorem", "c6-thm-additivity", "The integral is additive", r"""
If $f, g : \R^n \to [0, \infty]$ are measurable, then $f + g$ is measurable and
\[ \int (f + g) = \int f + \int g . \]
""", r"""
\emph{Simple functions.} Let $\varphi = \sum_{i=1}^r a_i \chi_{A_i}$ and $\psi = \sum_{j=1}^s b_j \chi_{B_j}$ be simple. Put $A_0 = \R^n \setminus \bigcup_{i \ge 1} A_i$, $a_0 = 0$, $B_0 = \R^n \setminus \bigcup_{j \ge 1} B_j$, $b_0 = 0$. Then $\R^n$ is the disjoint union of $A_0, \dots, A_r$ and also of $B_0, \dots, B_s$, so the measurable sets $A_i \cap B_j$ ($0 \le i \le r$, $0 \le j \le s$) are pairwise disjoint with union $\R^n$, and $\varphi + \psi = a_i + b_j$ on $A_i \cap B_j$. Thus $\varphi + \psi = \sum_{i,j} (a_i + b_j) \chi_{A_i \cap B_j}$ is simple. By the formula for the integral of a simple function, and finite additivity of $m$ applied to $A_i = \bigsqcup_j (A_i \cap B_j)$ and $B_j = \bigsqcup_i (A_i \cap B_j)$,
\[ \int (\varphi + \psi) = \sum_{i,j} (a_i + b_j)\, m(A_i \cap B_j) = \sum_i a_i\, mA_i + \sum_j b_j\, mB_j = \int \varphi + \int \psi . \]
(These are computations in $[0, \infty]$ with $0 \cdot \infty = 0$; the terms with $i = 0$ or $j = 0$ contribute $0$ to the respective sums.)

\emph{General case.} Choose simple functions $\varphi_k \uparrow f$ and $\psi_k \uparrow g$ pointwise, by the approximation lemma. Then $\varphi_k + \psi_k$ are simple, hence measurable, they increase with $k$, and $\varphi_k + \psi_k \to f + g$ pointwise. By the monotone convergence theorem, used three times, $f + g$ is measurable and
\[ \int (f + g) = \lim_k \int (\varphi_k + \psi_k) = \lim_k \Bigl( \int \varphi_k + \int \psi_k \Bigr) = \int f + \int g . \]
""", 3, 40, [
    r"Prove it first for simple functions, then pass to the limit.",
    r"For two simple functions, refine to the common partition $\set{A_i \cap B_j}$ (after adding the sets where each function vanishes).",
    r"Approximate $f$ and $g$ from below by increasing simple functions and apply monotone convergence to $\varphi_k$, $\psi_k$, and $\varphi_k + \psi_k$.",
], ["c6-prop-simple-integral", "c6-lem-simple-approx", "c6-thm-mct", "c6-lem-finite-additivity"]))

B.append(result("corollary", "c6-cor-series", "Term-by-term integration of nonnegative series", r"""
If $f_k : \R^n \to [0, \infty]$ are measurable for $k \in \N$, then $\sum_{k=1}^\infty f_k$ is measurable and
\[ \int \sum_{k=1}^\infty f_k = \sum_{k=1}^\infty \int f_k . \]
""", r"""
Let $s_N = f_1 + \dots + f_N$. By additivity of the integral and induction, $s_N$ is measurable and $\int s_N = \sum_{k=1}^N \int f_k$. Since the $f_k$ are nonnegative, $s_N$ increases pointwise to $\sum_k f_k$. By the monotone convergence theorem the sum is measurable and
\[ \int \sum_{k=1}^\infty f_k = \lim_{N \to \infty} \int s_N = \sum_{k=1}^\infty \int f_k . \]
""", 2, 10, [
    r"Apply monotone convergence to the partial sums.",
], ["c6-thm-additivity", "c6-thm-mct"]))

B.append(note("definition", "c6-def-almost-everywhere", "Almost everywhere", r"""
A property of points $x \in \R^n$ holds \emph{almost everywhere} (a.e.) if the set of points where it fails is a zero set. For example $f = g$ a.e. means that $\set{x : f(x) \ne g(x)}$ is a zero set.
"""))

B.append(result("proposition", "c6-prop-ae-equal", "Zero sets do not affect integrals", r"""
Let $f, g : \R^n \to [0, \infty]$ with $f$ measurable and $f = g$ almost everywhere. Then $g$ is measurable and $\int g = \int f$.
""", r"""
Let $Z = \set{f \ne g}$, a zero set in $\R^n$. The set $Z \times [0, \infty) = \bigcup_{k} Z \times [0, k)$ is a zero set in $\R^{n+1}$, because $m^*(Z \times [0,k)) \le k\, m^*Z = 0$ by the upper bound for cylinders. If $(x, y)$ lies in one of $\mathcal{U}f$, $\mathcal{U}g$ but not in the other, then $f(x) \ne g(x)$ and $y \ge 0$, so $(x,y) \in Z \times [0, \infty)$. Hence $W_1 = \mathcal{U}f \setminus \mathcal{U}g$ and $W_2 = \mathcal{U}g \setminus \mathcal{U}f$ are zero sets, thus measurable, and
\[ \mathcal{U}g = (\mathcal{U}f \setminus W_1) \cup W_2 \]
is measurable. Finally $m(\mathcal{U}g) = m(\mathcal{U}f \setminus W_1) + mW_2 = m(\mathcal{U}f) - 0 + 0$ when $\int f < \infty$; and if $\int f = \infty$ then $m(\mathcal{U}f \setminus W_1) = \infty$ as well, since $m(\mathcal{U}f) = m(\mathcal{U}f \setminus W_1) + mW_1$. In both cases $\int g = \int f$.
""", 2, 20, [
    r"The two undergraphs differ only above the zero set $Z = \set{f \ne g}$.",
    r"$Z \times [0, \infty)$ is a zero set in $\R^{n+1}$ by the upper bound for cylinders.",
], ["c6-def-almost-everywhere", "c6-lem-cylinder-upper", "c6-prop-zero-sets", "c6-prop-measurable-basic", "c6-lem-finite-additivity"]))

B.append(result("exercise", "c6-ex-chebyshev", "Chebyshev's inequality and vanishing integrals", r"""
Let $f : \R^n \to [0, \infty]$ be measurable.

(a) For every $a > 0$, $\ a \cdot m\set{f > a} \le \int f$.

(b) $\int f = 0$ if and only if $f = 0$ almost everywhere.

(c) If $\int f < \infty$ then $f(x) < \infty$ for almost every $x$.
""", r"""
(a) The set $E = \set{f > a}$ is measurable by the theorem on superlevel sets, and $a \chi_E \le f$. By monotonicity of the integral and the formula for simple functions, $a \cdot mE = \int a \chi_E \le \int f$.

(b) If $f = 0$ a.e., then $\int f = \int 0 = m(\emptyset) = 0$, since zero sets do not affect integrals. Conversely suppose $\int f = 0$. By (a), $m\set{f > 1/k} \le k \int f = 0$ for each $k$, and $\set{f \ne 0} = \set{f > 0} = \bigcup_k \set{f > 1/k}$ is a countable union of zero sets, hence a zero set.

(c) For every $k \in \N$, $\set{f = \infty} \subseteq \set{f > k}$, so by (a) $m^*\set{f = \infty} \le m\set{f > k} \le \tfrac1k \int f$. Letting $k \to \infty$ gives $m^*\set{f = \infty} = 0$.
""", 2, 20, [
    r"For (a), compare $f$ with the simple function $a\chi_{\set{f > a}}$.",
    r"For (b) and (c), write $\set{f > 0}$ as a union of the sets $\set{f > 1/k}$, and bound $\set{f = \infty}$ by $\set{f > k}$.",
], ["c6-thm-preimage", "c6-prop-simple-integral", "c6-prop-integral-monotone", "c6-prop-ae-equal", "c6-prop-zero-sets"]))

B.append(prose("c6-int-signed-prose", r"""
A function with values of both signs is integrated by splitting it into its positive and negative parts.
"""))

B.append(note("definition", "c6-def-signed-integral", "Integrable functions of arbitrary sign", r"""
For $f : \R^n \to \R$ let $f_+ = \max(f, 0)$ and $f_- = \max(-f, 0)$, so that $f_\pm \ge 0$, $f = f_+ - f_-$ and $\abs{f} = f_+ + f_-$. The function $f$ is \emph{measurable} if $f_+$ and $f_-$ are measurable, and \emph{integrable} if in addition $\int f_+ < \infty$ and $\int f_- < \infty$. Its \emph{Lebesgue integral} is then
\[ \int f = \int f_+ - \int f_- . \]
(For $f \ge 0$ this agrees with the earlier definition, since then $f_+ = f$ and $f_- = 0$.) If $E \subseteq \R^n$ is measurable, $\int_E f$ means $\int f \chi_E$ (for $f \ge 0$ the product $f\chi_E$ is measurable when $f$ is, because $\set{f\chi_E > a} = \set{f > a} \cap E$ for $a \ge 0$; for $f$ of arbitrary sign apply this to $f_\pm$, since $(f\chi_E)_\pm = f_\pm \chi_E$); for $n = 1$ and $E = [a, b]$ one writes $\int_a^b f$.
"""))

B.append(result("lemma", "c6-lem-signed-measurable", "Measurable real-valued functions", r"""
(a) A function $f : \R^n \to \R$ is measurable if and only if $\set{f > a}$ is a measurable set for every $a \in \R$.

(b) If $f, g : \R^n \to \R$ are measurable and $c \in \R$, then $f + g$, $cf$ and $\abs{f}$ are measurable.
""", r"""
(a) Suppose $f$ is measurable, so $f_\pm$ are measurable functions with values in $[0, \infty)$. If $a \ge 0$, then $\set{f > a} = \set{f_+ > a}$, which is measurable by the theorem on superlevel sets. If $a < 0$, then $f(x) > a$ if and only if $f_-(x) < -a$: indeed $f_-(x) = \max(-f(x), 0)$ and $-a > 0$, so $f_-(x) < -a$ exactly when $-f(x) < -a$. Hence
\[ \set{f > a} = \set{f_- \ge -a}^c, \qquad \set{f_- \ge -a} = \bigcap_{k > -1/a} \set{f_- > -a - \tfrac1k}, \]
and each set in the intersection is a superlevel set of $f_-$ at a level $\ge 0$, hence measurable.

Conversely suppose all the sets $\set{f > a}$, $a \in \R$, are measurable. For $a \ge 0$, $\set{f_+ > a} = \set{f > a}$ and
\[ \set{f_- > a} = \set{f < -a} = \bigcup_{k=1}^\infty \set{f \le -a - \tfrac1k} = \bigcup_{k=1}^\infty \set{f > -a - \tfrac1k}^c \]
are measurable. By the theorem on superlevel sets, $f_+$ and $f_-$ are measurable.

(b) Use (a). For $a \in \R$,
\[ \set{f + g > a} = \bigcup_{q \in \Q} \bigl( \set{f > q} \cap \set{g > a - q} \bigr): \]
if $f(x) > q$ and $g(x) > a - q$ then $f(x) + g(x) > a$; conversely if $f(x) + g(x) > a$, choose a rational $q$ with $a - g(x) < q < f(x)$. The union is countable, so $f + g$ is measurable. For $cf$: if $c > 0$ then $\set{cf > a} = \set{f > a/c}$; if $c < 0$ then $\set{cf > a} = \set{f < a/c} = \bigcup_k \set{f > a/c - \tfrac1k}^c$; if $c = 0$ the set is $\emptyset$ or $\R^n$. Finally $\abs{f} = f_+ + f_-$ is measurable by additivity of the integral for nonnegative functions (which includes the measurability of the sum).
""", 3, 35, [
    r"Relate the superlevel sets of $f$ to those of $f_+$ (for levels $a \ge 0$) and to sublevel sets of $f_-$ (for $a < 0$).",
    r"For the sum: $f(x) + g(x) > a$ exactly when some rational $q$ satisfies $f(x) > q$ and $g(x) > a - q$.",
], ["c6-def-signed-integral", "c6-thm-preimage", "c6-thm-sigma-algebra", "c6-thm-additivity"]))

B.append(result("theorem", "c6-thm-linearity", "Linearity of the integral", r"""
Let $f, g : \R^n \to \R$ be integrable and $c \in \R$. Then $f + g$ and $cf$ are integrable, and
\[ \int (f + g) = \int f + \int g, \qquad \int cf = c \int f, \qquad \Bigl| \int f \Bigr| \le \int \abs{f} . \]
Also, if $f \le g$ everywhere then $\int f \le \int g$.
""", r"""
By the lemma on measurable real-valued functions, $h = f + g$ and $cf$ are measurable.

\emph{Sum.} Since $h \le f_+ + g_+$ and $0 \le f_+ + g_+$, we get $h_+ \le f_+ + g_+$; similarly $h_- \le f_- + g_-$. By monotonicity and additivity for nonnegative functions, $\int h_+ \le \int f_+ + \int g_+ < \infty$ and $\int h_- < \infty$, so $h$ is integrable. From $h_+ - h_- = f_+ - f_- + g_+ - g_-$ we get the identity between nonnegative measurable functions
\[ h_+ + f_- + g_- = h_- + f_+ + g_+ . \]
Integrating and using additivity for nonnegative functions,
\[ \int h_+ + \int f_- + \int g_- = \int h_- + \int f_+ + \int g_+ . \]
All six numbers are finite, so rearranging gives $\int h_+ - \int h_- = (\int f_+ - \int f_-) + (\int g_+ - \int g_-)$, that is, $\int h = \int f + \int g$.

\emph{Scalar multiple.} If $c \ge 0$ then $(cf)_\pm = c f_\pm$, so by the scaling theorem $\int (cf)_\pm = c \int f_\pm < \infty$ and $\int cf = c \int f_+ - c \int f_- = c \int f$. If $c < 0$ then $(cf)_+ = \abs{c} f_-$ and $(cf)_- = \abs{c} f_+$, so $\int cf = \abs{c} \int f_- - \abs{c} \int f_+ = c \int f$.

\emph{Absolute value.} $\abs{f} = f_+ + f_-$, so $\int \abs{f} = \int f_+ + \int f_-$ and $\abs{\int f} = \abs{\int f_+ - \int f_-} \le \int f_+ + \int f_- = \int \abs{f}$.

\emph{Monotonicity.} If $f \le g$ then $g - f$ is integrable and nonnegative, so $\int g - \int f = \int (g - f) \ge 0$.
""", 3, 35, [
    r"Do not try to compute $(f+g)_\pm$ in terms of $f_\pm$ and $g_\pm$. Instead rearrange $h_+ - h_- = f_+ - f_- + g_+ - g_-$ so that only sums of nonnegative functions appear.",
    r"Integrate $h_+ + f_- + g_- = h_- + f_+ + g_+$ using additivity for nonnegative functions; everything is finite, so you can subtract.",
], ["c6-def-signed-integral", "c6-lem-signed-measurable", "c6-thm-additivity", "c6-thm-scaling-integral", "c6-prop-integral-monotone"]))

B.append(result("corollary", "c6-cor-dct-signed", "Dominated convergence for functions of arbitrary sign", r"""
Let $f_k : \R^n \to \R$ be measurable with $f_k(x) \to f(x) \in \R$ for every $x$. Suppose there is a measurable $g : \R^n \to [0, \infty]$ with $\int g < \infty$ and $\abs{f_k} \le g$ for all $k$. Then $f$ and all $f_k$ are integrable, and
\[ \int f = \lim_{k \to \infty} \int f_k . \]
""", r"""
The function $t \mapsto \max(t, 0)$ is continuous on $\R$, so $(f_k)_+ \to f_+$ and $(f_k)_- \to f_-$ pointwise. These are nonnegative measurable functions with $(f_k)_\pm \le \abs{f_k} \le g$. By the dominated convergence theorem for nonnegative functions, $f_+$ and $f_-$ are measurable and
\[ \int (f_k)_+ \to \int f_+, \qquad \int (f_k)_- \to \int f_- , \]
with all these integrals at most $\int g < \infty$ by monotonicity. So $f$ and the $f_k$ are integrable, and subtracting the two limits gives $\int f_k \to \int f$.
""", 2, 15, [
    r"Apply the nonnegative theorem to the positive parts and to the negative parts separately.",
], ["c6-thm-dct", "c6-def-signed-integral", "c6-prop-integral-monotone"]))

B.append(prose("c6-int-riemann-prose", r"""
Finally we compare with the Riemann integral of Chapter 3. Recall that for a bounded $f : [a,b] \to \R$ and a partition $P : a = x_0 < x_1 < \dots < x_r = b$, with $m_i = \inf f$ and $M_i = \sup f$ over $[x_{i-1}, x_i]$, the lower and upper sums are $L(f, P) = \sum_i m_i (x_i - x_{i-1})$ and $U(f, P) = \sum_i M_i (x_i - x_{i-1})$. If $f$ is Riemann integrable with integral $I$, then $L(f, P) \le I \le U(f, P)$ for every $P$, and for every $\eps > 0$ there is a partition with $U(f, P) - L(f, P) < \eps$.
"""))

B.append(result("theorem", "c6-thm-riemann-lebesgue", "Riemann integrable functions are Lebesgue integrable", r"""
Let $f : [a, b] \to [0, \infty)$ be Riemann integrable, and extend $f$ to $\R$ by $f(x) = 0$ for $x \notin [a,b]$. Then $f$ is Lebesgue measurable, and its Lebesgue integral equals its Riemann integral.
""", r"""
Let $I$ be the Riemann integral of $f$. For a partition $P : a = x_0 < \dots < x_r = b$, with $m_i, M_i$ as above, define subsets of $\R^2$
\[ F_P = \bigcup_{i=1}^r (x_{i-1}, x_i) \times [0, m_i), \qquad G_P = \bigcup_{i=1}^r [x_{i-1}, x_i] \times [0, M_i]. \]

\emph{$F_P \subseteq \mathcal{U}f \subseteq G_P$.} If $x_{i-1} < x < x_i$ and $0 \le y < m_i$, then $y < m_i \le f(x)$, so $(x,y) \in \mathcal{U}f$. If $(x, y) \in \mathcal{U}f$, then $f(x) > y \ge 0$, so $x \in [a, b]$; pick $i$ with $x \in [x_{i-1}, x_i]$; then $0 \le y < f(x) \le M_i$, so $(x, y) \in G_P$.

\emph{Measures.} The rectangles making up $F_P$ are pairwise disjoint, so $mF_P = \sum_i m_i (x_i - x_{i-1}) = L(f, P)$. By subadditivity, $mG_P \le \sum_i M_i (x_i - x_{i-1}) = U(f, P)$. Both sets are measurable, being finite unions of boxes.

Now for each $j \in \N$ choose a partition $P_j$ with $U(f, P_j) - L(f, P_j) < 1/j$, and let
\[ F = \bigcup_j F_{P_j}, \qquad G = \bigcap_j G_{P_j}. \]
These are measurable and $F \subseteq \mathcal{U}f \subseteq G$. For each $j$, $G \setminus F \subseteq G_{P_j} \setminus F_{P_j}$, and since $F_{P_j} \subseteq G_{P_j}$ have finite measure,
\[ m(G \setminus F) \le mG_{P_j} - mF_{P_j} \le U(f, P_j) - L(f, P_j) < \tfrac1j . \]
So $m(G \setminus F) = 0$. Then $\mathcal{U}f \setminus F \subseteq G \setminus F$ is a zero set, and $\mathcal{U}f = F \cup (\mathcal{U}f \setminus F)$ is measurable: $f$ is Lebesgue measurable.

Finally, for each $j$, monotonicity of measure gives
\[ L(f, P_j) = mF_{P_j} \le m(\mathcal{U}f) \le mG_{P_j} \le U(f, P_j), \]
and also $L(f, P_j) \le I \le U(f, P_j)$. Two numbers in an interval of length less than $1/j$ differ by less than $1/j$; as $j$ is arbitrary, $\int f = m(\mathcal{U}f) = I$.
""", 3, 40, [
    r"A lower sum is the area of a union of rectangles inside the undergraph; an upper sum is the area of rectangles covering it.",
    r"Take partitions $P_j$ with $U - L < 1/j$. The union of the inner regions and the intersection of the outer regions are measurable sets that sandwich $\mathcal{U}f$ and differ by a zero set.",
], ["c6-def-integral", "c6-thm-boxes-measurable", "c6-lem-finite-additivity", "c6-thm-countable-subadditivity", "c6-prop-measure-difference", "c6-prop-measurable-basic", "c6-prop-zero-sets"]))

B.append(note("example", "c6-ex-dirichlet", "A Lebesgue integrable function that is not Riemann integrable", r"""
Let $f = \chi_{\Q \cap [0,1]}$. Every subinterval of $[0,1]$ contains rational and irrational numbers, so every lower sum of $f$ is $0$ and every upper sum is $1$: $f$ is not Riemann integrable. But $\Q \cap [0,1]$ is a zero set, so $f$ is a simple function and $\int f = m(\Q \cap [0,1]) = 0$. Since $f = 0$ almost everywhere, this is as it should be: the Lebesgue integral does not see what happens on a zero set.

Furthermore, enumerate $\Q \cap [0,1] = \set{q_1, q_2, \dots}$ and let $f_k = \chi_{\set{q_1, \dots, q_k}}$. Each $f_k$ is Riemann integrable with integral $0$, and $f_k \uparrow f$ pointwise. The monotone convergence theorem applies, but the limit has left the class of Riemann integrable functions. This closure under limits is the main advantage of Lebesgue's integral.
"""))

B.append(note("remark", "c6-rem-riemann-signed", "Signed functions and improper integrals", r"""
If $f : [a,b] \to \R$ is Riemann integrable, of either sign, then so are $f_+$ and $f_-$, and applying the theorem to each shows that $f$ (extended by $0$) is Lebesgue integrable with the same integral. For improper Riemann integrals the comparison is more delicate: a nonnegative function with a convergent improper integral is Lebesgue integrable (by monotone convergence), but a conditionally convergent improper integral such as $\int_0^\infty \frac{\sin x}{x}\,dx$ is not a Lebesgue integral, because $\int \abs{f} = \infty$. These facts are not proved here.
"""))

C = [
    card("c6-card-integral-def", "c6-def-integral", r"Define the undergraph of $f : \R^n \to [0,\infty]$, measurability of $f$, and $\int f$.", r"$\mathcal{U}f = \set{(x,y) : 0 \le y < f(x)} \subseteq \R^{n+1}$. $f$ is measurable if $\mathcal{U}f$ is, and $\int f = m(\mathcal{U}f)$."),
    card("c6-card-mct", "c6-thm-mct", r"State the monotone convergence theorem and the idea of its proof.", r"If $0 \le f_k \uparrow f$ pointwise with $f_k$ measurable, then $f$ is measurable and $\int f_k \uparrow \int f$. Proof: $\mathcal{U}f_k \uparrow \mathcal{U}f$; use upward measure continuity."),
    card("c6-card-fatou", "c6-thm-fatou", r"State Fatou's lemma and give an example of strict inequality.", r"For measurable $f_k \ge 0$: $\int \liminf f_k \le \liminf \int f_k$. Strict for $f_k = \chi_{[k,k+1]}$: integrals are $1$, pointwise limit is $0$."),
    card("c6-card-dct", "c6-thm-dct", r"State the dominated convergence theorem.", r"If $f_k$ are measurable, $f_k \to f$ pointwise, and $\abs{f_k} \le g$ with $\int g < \infty$, then $f$ is integrable and $\int f_k \to \int f$."),
    card("c6-card-dct-idea", "c6-thm-dct", r"Idea of the proof of dominated convergence (nonnegative case) via undergraphs?", r"Squeeze $f_k$ between $h_k = \inf_{j \ge k} f_j \uparrow f$ (monotone convergence) and $H_k = \sup_{j \ge k} f_j \downarrow f$ (downward measure continuity for completed undergraphs, finite because $H_1 \le g$)."),
    card("c6-card-cylinder", "c6-lem-cylinder-measurable", r"What is the measure of a cylinder $E \times J$ over a measurable $E \subseteq \R^n$, and what is $m^*(A \times [0,1))$ for arbitrary $A$?", r"$m(E \times J) = \abs{J}\,mE$, and $m^*(A \times [0,1)) = m^*A$."),
    card("c6-card-preimage", "c6-thm-preimage", r"Characterize measurability of $f : \R^n \to [0,\infty]$ by superlevel sets.", r"$f$ is measurable (undergraph measurable) iff $\set{f > a}$ is measurable for every $a \ge 0$."),
    card("c6-card-additivity-idea", "c6-thm-additivity", r"How is $\int (f+g) = \int f + \int g$ proved for nonnegative measurable $f, g$?", r"Check it for simple functions on a common partition; approximate $f, g$ by increasing simple functions (dyadic rounding) and apply monotone convergence."),
    card("c6-card-ae", "c6-ex-chebyshev", r"State Chebyshev's inequality. When is $\int f = 0$ for measurable $f \ge 0$?", r"$a \cdot m\set{f > a} \le \int f$. $\int f = 0$ iff $f = 0$ almost everywhere."),
    card("c6-card-riemann", "c6-thm-riemann-lebesgue", r"How are the Riemann and Lebesgue integrals related? Give a function separating them.", r"A Riemann integrable function on $[a,b]$ is Lebesgue integrable with the same integral (lower/upper sums are areas of rectangles inside/covering the undergraph). $\chi_{\Q \cap [0,1]}$ is Lebesgue integrable with integral $0$ but not Riemann integrable."),
]

write("6-lebesgue-integrals", B, C)
