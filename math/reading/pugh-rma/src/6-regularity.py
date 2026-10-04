from __future__ import annotations

import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from c6common import prose, note, result, card, write

B = []

B.append(prose("c6-reg-intro", r"""
Carathéodory's definition is efficient but abstract: it does not say what a measurable set looks like. \emph{Regularity} does. A measurable set can be squeezed between a closed set inside and an open set outside with as little measure in between as we please, so up to a zero set it is a countable union of closed sets. This gives a second, more concrete test for measurability in terms of an \emph{inner} measure, and it lets us see why some sets fail the test: at the end of the section we construct a set that is not measurable.
"""))

B.append(note("definition", "c6-def-gdelta-fsigma", "G-delta and F-sigma sets", r"""
A subset of $\R^n$ is a \emph{$G_\delta$-set} if it is the intersection of countably many open sets, and an \emph{$F_\sigma$-set} if it is the union of countably many closed sets. The complement of a $G_\delta$-set is an $F_\sigma$-set and conversely. Both kinds of sets are measurable, since open and closed sets are measurable and the measurable sets form a $\sigma$-algebra.
"""))

B.append(result("theorem", "c6-thm-outer-open", "Outer measure is computed by open sets", r"""
For every $A \subseteq \R^n$,
\[ m^*A = \inf \set{ mU : U \text{ open}, \ U \supseteq A }. \]
Moreover there is a $G_\delta$-set $G \supseteq A$ with $mG = m^*A$.
""", r"""
If $U \supseteq A$ is open, then $m^*A \le m^*U = mU$ by monotonicity, so $m^*A$ is a lower bound for the set on the right. If $m^*A = \infty$, every open $U \supseteq A$ has $mU = \infty$, the infimum is $\infty$, and $G = \R^n$ serves.

Assume $m^*A < \infty$ and let $\eps > 0$. Choose open boxes $B_k$ covering $A$ with $\sum_k \abs{B_k} \le m^*A + \eps$. The set $U = \bigcup_k B_k$ is open, contains $A$, and by countable subadditivity $mU \le \sum_k \abs{B_k} \le m^*A + \eps$. Hence the infimum is at most $m^*A + \eps$ for every $\eps > 0$, and so equals $m^*A$.

For each $j \in \N$ choose in this way an open $U_j \supseteq A$ with $mU_j \le m^*A + 1/j$, and let $G = \bigcap_j U_j$. Then $G$ is a $G_\delta$-set containing $A$, and for every $j$
\[ m^*A \le mG \le mU_j \le m^*A + \tfrac1j . \]
Hence $mG = m^*A$.
""", 2, 20, [
    r"The union of the boxes in a covering is an open set.",
    r"For the $G_\delta$-set, intersect open sets $U_j \supseteq A$ with $mU_j \le m^*A + 1/j$.",
], ["c6-def-gdelta-fsigma", "c6-def-outer-measure", "c6-thm-countable-subadditivity", "c6-thm-open-closed-measurable"]))

B.append(result("theorem", "c6-thm-regularity", "Regularity of Lebesgue measure", r"""
Let $E \subseteq \R^n$ be measurable and $\eps > 0$. Then there are an open set $U$ and a closed set $K$ with
\[ K \subseteq E \subseteq U, \qquad m(U \setminus E) < \eps, \qquad m(E \setminus K) < \eps . \]
""", r"""
\emph{The open set.} Let $C_k = [-k, k]^n$ and $E_k = E \cap C_k$ for $k \in \N$. Each $E_k$ is measurable with $mE_k \le \abs{C_k} < \infty$, and $E = \bigcup_k E_k$. Since outer measure is computed by open sets, there is an open $U_k \supseteq E_k$ with $mU_k < mE_k + \eps/2^{k+1}$. As $mE_k$ is finite, $m(U_k \setminus E_k) = mU_k - mE_k < \eps/2^{k+1}$. Let $U = \bigcup_k U_k$, an open set containing $E$. If $x \in U \setminus E$, then $x \in U_k$ for some $k$ and $x \notin E_k$, so
\[ U \setminus E \subseteq \bigcup_k (U_k \setminus E_k), \qquad m(U \setminus E) \le \sum_{k=1}^\infty \frac{\eps}{2^{k+1}} = \frac{\eps}{2} < \eps. \]

\emph{The closed set.} The complement $E^c$ is measurable, so by the first part there is an open $V \supseteq E^c$ with $m(V \setminus E^c) < \eps$. Let $K = V^c$. Then $K$ is closed, $K \subseteq E$, and $E \setminus K = E \cap V = V \setminus E^c$, so $m(E \setminus K) < \eps$.
""", 3, 35, [
    r"If $mE < \infty$, an open $U \supseteq E$ with $mU < mE + \eps$ works, because then $m(U \setminus E) = mU - mE$. What goes wrong when $mE = \infty$, and how can you cut $E$ into pieces of finite measure?",
    r"Use $E_k = E \cap [-k,k]^n$ with tolerance $\eps/2^{k+1}$ and take the union of the open sets.",
    r"For the closed set, apply the open-set statement to $E^c$ and take complements.",
], ["c6-thm-outer-open", "c6-prop-measure-difference", "c6-thm-boxes-measurable", "c6-thm-countable-subadditivity"]))

B.append(result("theorem", "c6-thm-fsigma-gdelta", "Measurable sets are F-sigma sets up to zero sets", r"""
For a set $E \subseteq \R^n$ the following are equivalent.

(a) $E$ is measurable.

(b) There are an $F_\sigma$-set $F$ and a $G_\delta$-set $G$ with $F \subseteq E \subseteq G$ and $m(G \setminus F) = 0$.

(c) $E = F \cup Z$ where $F$ is an $F_\sigma$-set and $Z$ is a zero set.
""", r"""
(a) $\Rightarrow$ (b). By regularity, for each $j \in \N$ there are a closed $K_j$ and an open $U_j$ with $K_j \subseteq E \subseteq U_j$, $m(E \setminus K_j) < 1/j$ and $m(U_j \setminus E) < 1/j$. Let $F = \bigcup_j K_j$ and $G = \bigcap_j U_j$. Then $F$ is an $F_\sigma$-set, $G$ is a $G_\delta$-set, $F \subseteq E \subseteq G$, and for every $j$
\[ G \setminus F \subseteq U_j \setminus K_j = (U_j \setminus E) \cup (E \setminus K_j), \]
so $m(G \setminus F) < 2/j$. Hence $m(G \setminus F) = 0$.

(b) $\Rightarrow$ (c). Let $Z = E \setminus F$. Then $Z \subseteq G \setminus F$, so $Z$ is a zero set, and $E = F \cup Z$.

(c) $\Rightarrow$ (a). An $F_\sigma$-set is measurable, a zero set is measurable, and the union of two measurable sets is measurable.
""", 2, 20, [
    r"Apply regularity with $\eps = 1/j$ for every $j$ and combine the closed sets and the open sets.",
], ["c6-thm-regularity", "c6-def-gdelta-fsigma", "c6-prop-measurable-basic", "c6-prop-zero-sets"]))

B.append(result("corollary", "c6-cor-lipschitz-measurable", "Lipschitz maps preserve measurability", r"""
Let $T : \R^n \to \R^n$ be Lipschitz. If $E \subseteq \R^n$ is measurable, then $TE$ is measurable. Consequently a bijection $T : \R^n \to \R^n$ such that $T$ and $T^{-1}$ are both Lipschitz is a meseomorphism.
""", r"""
Write $E = \bigcup_j K_j \cup Z$ with each $K_j$ closed and $Z$ a zero set, as the previous theorem allows. With $C_i = [-i, i]^n$, each $K_j \cap C_i$ is closed and bounded, hence compact by the Heine–Borel theorem, and $K_j = \bigcup_i (K_j \cap C_i)$. A Lipschitz map is continuous, and the continuous image of a compact set is compact, hence closed. So each $T(K_j \cap C_i)$ is closed, thus measurable. Since Lipschitz maps do not inflate zero sets, $TZ$ is a zero set, thus measurable. Therefore
\[ TE = \bigcup_{i,j} T(K_j \cap C_i) \;\cup\; TZ \]
is a countable union of measurable sets, hence measurable. If $T$ is a bijection and $T^{-1}$ is also Lipschitz, the same applies to $T^{-1}$, so $T$ is a meseomorphism.
""", 3, 25, [
    r"Decompose $E$ as an $F_\sigma$-set together with a zero set and treat the two parts separately.",
    r"A closed set is a countable union of compact sets, and continuous images of compact sets are compact.",
], ["c6-thm-fsigma-gdelta", "c6-thm-lipschitz-zero", "c6-thm-open-closed-measurable", "c6-prop-measurable-basic", "c6-thm-sigma-algebra"]))

B.append(prose("c6-reg-inner-prose", r"""
Outer measure approximates a set from outside by open sets. Regularity suggests the companion notion, approximation from inside by closed sets. A set should be measurable exactly when the two approximations meet.
"""))

B.append(note("definition", "c6-def-inner-measure", "Inner measure, hull, kernel", r"""
The \emph{inner measure} of a set $A \subseteq \R^n$ is
\[ m_*A = \sup \set{ mK : K \text{ closed}, \ K \subseteq A } \in [0, \infty]. \]
A \emph{hull} of $A$ is a measurable set $H \supseteq A$ with $mH = m^*A$. A \emph{kernel} of $A$ is a measurable set $N \subseteq A$ with $mN = m_*A$.
"""))

B.append(result("proposition", "c6-prop-inner-basic", "Inner measure: first properties", r"""
(a) If $A \subseteq A'$ then $m_*A \le m_*A'$.

(b) $m_*A \le m^*A$ for every $A \subseteq \R^n$.

(c) If $E$ is measurable, then $m_*E = mE$.
""", r"""
(a) Every closed subset of $A$ is a closed subset of $A'$, so the supremum for $A'$ is over a larger family.

(b) If $K \subseteq A$ is closed, then $mK = m^*K \le m^*A$ by monotonicity. Taking the supremum over $K$ gives $m_*A \le m^*A$.

(c) By (b), $m_*E \le mE$. Let $\eps > 0$. By regularity there is a closed $K \subseteq E$ with $m(E \setminus K) < \eps$, and $mE = mK + m(E \setminus K)$. If $mE = \infty$, this forces $mK = \infty$, so $m_*E = \infty = mE$. If $mE < \infty$, then $mK > mE - \eps$, so $m_*E > mE - \eps$ for every $\eps > 0$, and $m_*E \ge mE$.
""", 2, 15, [
    r"Parts (a) and (b) are comparisons of families of sets. For (c) use regularity to find a closed set inside $E$ carrying almost all of its measure.",
], ["c6-def-inner-measure", "c6-thm-regularity", "c6-prop-measure-difference"]))

B.append(result("proposition", "c6-prop-hull-kernel", "Hulls and kernels exist", r"""
Every set $A \subseteq \R^n$ has a hull that is a $G_\delta$-set and a kernel that is an $F_\sigma$-set.
""", r"""
\emph{Hull.} Since outer measure is computed by open sets, there is a $G_\delta$-set $G \supseteq A$ with $mG = m^*A$; it is a hull.

\emph{Kernel.} By the definition of the supremum choose closed sets $K_j \subseteq A$ with $mK_j \to m_*A$ as $j \to \infty$ (with $mK_j > m_*A - 1/j$ if $m_*A < \infty$, and $mK_j > j$ if $m_*A = \infty$). Let $N = \bigcup_j K_j$, an $F_\sigma$-set contained in $A$. For every $j$, $mN \ge mK_j$, so $mN \ge m_*A$. On the other hand $N$ is measurable and $N \subseteq A$, so by the first properties of inner measure $mN = m_*N \le m_*A$. Hence $mN = m_*A$.
""", 2, 20, [
    r"The hull was already found. For the kernel, take a sequence of closed subsets whose measures approach the supremum.",
    r"To see that the union $N$ of those closed sets has measure no more than $m_*A$, use that $N$ is measurable, so $mN = m_*N$.",
], ["c6-def-inner-measure", "c6-thm-outer-open", "c6-prop-inner-basic"]))

B.append(result("theorem", "c6-thm-inner-outer-criterion", "Measurability criterion: inner measure equals outer measure", r"""
Let $A \subseteq \R^n$ with $m^*A < \infty$ (for instance, $A$ bounded). Then $A$ is measurable if and only if $m_*A = m^*A$.
""", r"""
If $A$ is measurable then $m_*A = mA = m^*A$ by the first properties of inner measure.

Conversely suppose $m_*A = m^*A < \infty$. Let $H$ be a hull and $N$ a kernel of $A$, so $N \subseteq A \subseteq H$, both are measurable, and $mN = m_*A = m^*A = mH < \infty$. Then
\[ m(H \setminus N) = mH - mN = 0. \]
The set $A \setminus N$ is contained in $H \setminus N$, so it is a zero set and therefore measurable. Hence $A = N \cup (A \setminus N)$ is measurable.

A bounded set lies in a box, so it has finite outer measure.
""", 3, 25, [
    r"Sandwich $A$ between a kernel and a hull.",
    r"If $mN = mH < \infty$ then $H \setminus N$ is a zero set, and $A$ differs from the measurable set $N$ by a subset of it.",
], ["c6-prop-hull-kernel", "c6-prop-inner-basic", "c6-prop-measure-difference", "c6-prop-measurable-basic", "c6-prop-zero-sets"]))

B.append(result("proposition", "c6-prop-inner-box", "Inner measure inside a box", r"""
Let $B \subseteq \R^n$ be a box and $A \subseteq B$. Then
\[ m_*A = \abs{B} - m^*(B \setminus A). \]
""", r"""
Recall that $B$ is measurable with $mB = \abs{B} < \infty$.

\emph{$\le$.} Let $K \subseteq A$ be closed. Then $B \setminus K$ is measurable, contains $B \setminus A$, and $\abs{B} = mK + m(B \setminus K) \ge mK + m^*(B \setminus A)$. So $mK \le \abs{B} - m^*(B \setminus A)$; taking the supremum over $K$ gives $m_*A \le \abs{B} - m^*(B \setminus A)$.

\emph{$\ge$.} Let $H$ be a hull of $B \setminus A$, and put $M = B \setminus H$. Then $M$ is measurable, and $M \subseteq B \setminus (B \setminus A) = A$. Since $B \subseteq M \cup H$,
\[ \abs{B} \le mM + mH = mM + m^*(B \setminus A), \]
so $mM \ge \abs{B} - m^*(B \setminus A)$. By the first properties of inner measure, $m_*A \ge m_*M = mM$. Hence $m_*A \ge \abs{B} - m^*(B \setminus A)$.
""", 3, 30, [
    r"For $\le$, compare a closed $K \subseteq A$ with its complement in $B$, which contains $B \setminus A$.",
    r"For $\ge$, take a hull $H$ of $B \setminus A$; then $B \setminus H$ is a measurable subset of $A$.",
], ["c6-def-inner-measure", "c6-prop-inner-basic", "c6-prop-hull-kernel", "c6-thm-boxes-measurable", "c6-prop-measure-difference"]))

B.append(result("corollary", "c6-cor-clean-box", "A bounded set is measurable iff it divides a box cleanly", r"""
Let $B \subseteq \R^n$ be a box and $A \subseteq B$. Then $A$ is measurable if and only if
\[ \abs{B} = m^*A + m^*(B \setminus A). \]
""", r"""
Since $A \subseteq B$, $m^*A \le \abs{B} < \infty$ and likewise $m^*(B \setminus A) < \infty$. By the measurability criterion, $A$ is measurable if and only if $m_*A = m^*A$. By the formula for inner measure inside a box, $m_*A = \abs{B} - m^*(B \setminus A)$. So $A$ is measurable if and only if $\abs{B} - m^*(B \setminus A) = m^*A$.
""", 1, 10, [
    r"Combine the criterion $m_*A = m^*A$ with the formula for $m_*A$ inside a box.",
], ["c6-thm-inner-outer-criterion", "c6-prop-inner-box"]))

B.append(note("remark", "c6-rem-one-test-set", "One test set suffices", r"""
Carathéodory's condition asks $A$ to divide \emph{every} test set cleanly. The corollary says that for a set $A$ inside a box $B$, it is enough to check the single test set $X = B$. This was Lebesgue's original definition of measurability.
"""))

B.append(prose("c6-reg-vitali-prose", r"""
Are all sets measurable? No, provided the axiom of choice is allowed. The classical example lives in $\R$ and exploits the one symmetry that measure must respect: translation invariance.
"""))

B.append(result("theorem", "c6-thm-vitali", "A nonmeasurable set (Vitali)", r"""
There is a set $V \subseteq [0,1)$ that is not Lebesgue measurable in $\R$. Specifically, call $x, y \in [0,1)$ equivalent if $x - y \in \Q$, and let $V$ contain exactly one point from each equivalence class (such a set exists by the axiom of choice). Then $V$ is not measurable.
""", r"""
The relation $x \sim y \iff x - y \in \Q$ is an equivalence relation on $[0,1)$: it is reflexive since $0 \in \Q$, symmetric since $-q \in \Q$ when $q \in \Q$, and transitive since sums of rationals are rational. Let $V$ be as described, and let $q_1, q_2, \dots$ be an enumeration of the countable set $\Q \cap (-1, 1)$. Put $V_k = V + q_k$.

\emph{The $V_k$ are pairwise disjoint.} If $v + q_k = v' + q_l$ with $v, v' \in V$, then $v - v' = q_l - q_k \in \Q$, so $v \sim v'$; since $V$ contains only one point of each class, $v = v'$, and then $q_k = q_l$, so $k = l$.

\emph{The $V_k$ cover $[0,1)$.} Let $x \in [0,1)$ and let $v \in V$ be the point of $V$ equivalent to $x$. Then $q = x - v$ is rational and $\abs{q} < 1$ because $x, v \in [0,1)$. So $q = q_k$ for some $k$ and $x = v + q_k \in V_k$.

\emph{The $V_k$ lie in $(-1, 2)$,} since $V \subseteq [0,1)$ and $\abs{q_k} < 1$.

Now suppose $V$ were measurable. Translations are meseometries, so each $V_k$ is measurable with $mV_k = mV$. By countable additivity and monotonicity,
\[ 1 = m[0,1) \le m\Bigl( \bigsqcup_k V_k \Bigr) = \sum_{k=1}^\infty mV \le m(-1, 2) = 3. \]
If $mV = 0$ the sum is $0$, contradicting $1 \le 0$. If $mV > 0$ the sum is $\infty$, contradicting $\infty \le 3$. Hence $V$ is not measurable.
""", 3, 45, [
    r"Translate $V$ by the rationals in $(-1,1)$. How do these countably many translates sit relative to each other and to $[0,1)$?",
    r"Show the translates are pairwise disjoint, cover $[0,1)$, and lie in $(-1,2)$.",
    r"If $V$ were measurable, all translates would have the same measure $mV$, and countably many copies of one number would have to add up to something between $1$ and $3$.",
], ["c6-thm-translation", "c6-thm-sigma-algebra", "c6-prop-measure-difference", "c6-thm-boxes-measurable"]))

B.append(result("exercise", "c6-ex-vitali-inner-outer", "Inner and outer measure of the Vitali set", r"""
Let $V \subseteq [0,1)$ be the set of the previous theorem. Show that $m_*V = 0$ and $m^*V > 0$. (So the criterion $m_*A = m^*A$ visibly fails for $V$.)
""", r"""
Keep the notation $q_k$, $V_k = V + q_k$ of the previous proof; recall the $V_k$ are pairwise disjoint, cover $[0,1)$, and lie in $(-1,2)$.

\emph{$m^*V > 0$.} By translation invariance of outer measure, $m^*V_k = m^*V$. Countable subadditivity gives $1 = m^*[0,1) \le \sum_k m^*V_k = \sum_k m^*V$, which is impossible if $m^*V = 0$.

\emph{$m_*V = 0$.} Let $K \subseteq V$ be closed. The translates $K + q_k \subseteq V_k$ are closed, hence measurable, pairwise disjoint, contained in $(-1, 2)$, and $m(K + q_k) = mK$. By countable additivity
\[ \sum_{k=1}^\infty mK = m\Bigl( \bigsqcup_k (K + q_k) \Bigr) \le 3, \]
which forces $mK = 0$. Hence $m_*V = \sup mK = 0$.
""", 3, 25, [
    r"Rerun the two halves of Vitali's argument separately: the covering half uses only subadditivity, the disjointness half only needs measurable pieces.",
    r"For $m_*V$, apply the disjoint-translates argument to a closed subset $K \subseteq V$.",
], ["c6-thm-vitali", "c6-thm-translation", "c6-thm-countable-subadditivity", "c6-thm-sigma-algebra", "c6-def-inner-measure"]))

B.append(note("remark", "c6-rem-nonmeasurable", "How common are nonmeasurable sets?", r"""
The hypothesis $m^*A < \infty$ in the criterion $m_*A = m^*A$ cannot be dropped: for the Vitali set $V$, the set $A = V \cup [2, \infty)$ has $m_*A = m^*A = \infty$, yet $A$ is not measurable, since otherwise $V = A \cap [0,1)$ would be. It is also true, though not proved here, that every subset of $\R$ of positive outer measure contains a nonmeasurable set. Every such construction relies on the axiom of choice; no explicit formula produces a nonmeasurable set.
"""))

C = [
    card("c6-card-regularity", "c6-thm-regularity", r"State the regularity of Lebesgue measure.", r"For measurable $E$ and $\eps > 0$ there are a closed $K$ and an open $U$ with $K \subseteq E \subseteq U$, $m(U \setminus E) < \eps$, $m(E \setminus K) < \eps$."),
    card("c6-card-regularity-idea", "c6-thm-regularity", r"In proving regularity, how is a set of infinite measure handled, and how is the closed set found?", r"Cut $E$ into the bounded pieces $E \cap [-k,k]^n$ with tolerances $\eps/2^{k+1}$ and unite the open sets. The closed set is the complement of an open set approximating $E^c$."),
    card("c6-card-fsigma", "c6-thm-fsigma-gdelta", r"Describe measurable sets in terms of $F_\sigma$- and $G_\delta$-sets.", r"$E$ is measurable iff $F \subseteq E \subseteq G$ with $F$ an $F_\sigma$, $G$ a $G_\delta$, and $m(G \setminus F) = 0$; equivalently $E$ is an $F_\sigma$-set union a zero set."),
    card("c6-card-inner-measure", "c6-def-inner-measure", r"Define inner measure, hull, and kernel.", r"$m_*A = \sup\set{mK : K \subseteq A \text{ closed}}$. Hull: measurable $H \supseteq A$ with $mH = m^*A$. Kernel: measurable $N \subseteq A$ with $mN = m_*A$."),
    card("c6-card-criterion", "c6-thm-inner-outer-criterion", r"State the inner/outer measure criterion for measurability.", r"If $m^*A < \infty$: $A$ is measurable iff $m_*A = m^*A$. For $A$ in a box $B$: iff $\abs{B} = m^*A + m^*(B \setminus A)$."),
    card("c6-card-vitali", "c6-thm-vitali", r"Describe the Vitali set and why it is not measurable.", r"$V \subseteq [0,1)$ has one point from each class of $x \sim y \iff x - y \in \Q$. Its translates by the rationals in $(-1,1)$ are disjoint, cover $[0,1)$, and lie in $(-1,2)$; equal measures cannot sum to a number in $[1,3]$."),
    card("c6-card-lipschitz-measurable", "c6-cor-lipschitz-measurable", r"Why does a Lipschitz map $T : \R^n \to \R^n$ send measurable sets to measurable sets?", r"$E$ is a countable union of compact sets together with a zero set; $T$ sends compact sets to compact sets and zero sets to zero sets."),
    card("c6-card-outer-open", "c6-thm-outer-open", r"How is $m^*A$ expressed with open sets?", r"$m^*A = \inf\set{mU : U \supseteq A \text{ open}}$, and some $G_\delta$-set $G \supseteq A$ has $mG = m^*A$."),
]

write("6-regularity", B, C)
