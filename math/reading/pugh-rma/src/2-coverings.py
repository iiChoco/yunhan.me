from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c2lib import Section

s = Section("2-coverings")

s.p("c2-cov-intro", r"""
So far compactness has meant: every sequence has a convergent subsequence. There is a second description, in terms of open sets only, which says that a compact set cannot be covered wastefully: from any covering by open sets, finitely many already suffice. The two descriptions are equivalent in a metric space, and proving that is the business of this section. The covering form is the one that generalizes beyond metric spaces, and it is often the quicker tool: it converts local information (something true near each point) into global information (something true everywhere, with uniform constants).
""")

s.d("c2-def-covering", "Covering, covering compact", r"""
Let $A$ be a subset of a metric space $M$. A collection $\mathcal{U}$ of subsets of $M$ \emph{covers} $A$ if every point of $A$ lies in at least one member of $\mathcal{U}$. It is an \emph{open covering} if each of its members is an open subset of $M$. A \emph{subcovering} is a subcollection $\mathcal{V} \subset \mathcal{U}$ that still covers $A$; we say $\mathcal{U}$ \emph{reduces} to $\mathcal{V}$.

$A$ is \emph{covering compact} if every open covering of $A$ reduces to a finite subcovering.
""")

s.e("c2-ex-covering-fails", "An open covering with no finite subcovering", r"""
The intervals $U_n = (1/n, 2)$, $n \in \N$, form an open covering of $(0,1]$ in $\R$. Any finite subcollection $U_{n_1}, \dots, U_{n_k}$ has union $(1/N, 2)$ with $N = \max n_i$, which misses the point $1/N \in (0,1]$. So $(0,1]$ is not covering compact. Note what the definition demands: not that \emph{some} finite open covering exists (the single set $(0,2)$ covers), but that \emph{every} open covering can be thinned to a finite one.
""")

s.t("theorem", "c2-thm-covering-implies-sequential", "Covering compact implies sequentially compact", r"""
If a subset $A$ of a metric space $M$ is covering compact, then it is sequentially compact.
""", r"""
Suppose $A$ is covering compact but some sequence $(a_n)$ in $A$ has no subsequence converging to a point of $A$. Let $a \in A$. By the lemma on extracting a convergent subsequence, since no subsequence converges to $a$ there is a radius $r_a > 0$ such that $a_n \in M_{r_a}(a)$ for only finitely many indices $n$.

The neighborhoods $M_{r_a}(a)$, $a \in A$, are open and cover $A$. By covering compactness finitely many of them cover $A$:
\[ A \subset M_{r_{b_1}}(b_1) \cup \dots \cup M_{r_{b_k}}(b_k) . \]
Every index $n \in \N$ has $a_n \in A$, hence $a_n$ in one of these $k$ neighborhoods. But each of them contains $a_n$ for only finitely many $n$, so $\N$ would be a finite union of finite sets. This is absurd. Hence every sequence in $A$ has a subsequence converging in $A$.
""", 3, 35, [
    r"Argue by contradiction: take a sequence with no subsequence converging in $A$, and build an open covering out of that failure.",
    r"Each $a \in A$ has a neighborhood containing $a_n$ for only finitely many $n$. Cover $A$ by these and extract a finite subcovering.",
], ["c2-def-covering", "c2-def-compact", "c2-lem-cluster-subsequence", "c2-prop-ball-open"])

s.d("c2-def-lebesgue-number", "Lebesgue number", r"""
Let $\mathcal{U}$ be a covering of $A \subset M$. A number $\lambda > 0$ is a \emph{Lebesgue number} for $\mathcal{U}$ if for each $a \in A$ there is a member $U \in \mathcal{U}$ with $M_\lambda(a) \subset U$.

A Lebesgue number is a guaranteed amount of elbow room: every point of $A$ sits at depth at least $\lambda$ inside some single member of the covering. The member depends on the point; $\lambda$ does not. Here $M_\lambda(a)$ is the neighborhood in the ambient space $M$, and the definition is in terms of neighborhoods centered at points of $A$ (the "ball form"). The statement about sets of small diameter (the "diameter form": every nonempty subset of $A$ of diameter less than $\lambda$ lies in one member) follows from it and is recorded after the lemma. Note also that if $\lambda$ is a Lebesgue number then so is every $\lambda'$ with $0 < \lambda' < \lambda$, since $M_{\lambda'}(a) \subset M_\lambda(a)$.
""")

s.t("lemma", "c2-lem-lebesgue-number", "Lebesgue number lemma", r"""
Every open covering of a sequentially compact subset $A$ of a metric space $M$ has a Lebesgue number.
""", r"""
Let $\mathcal{U}$ be an open covering of $A$ and suppose it has no Lebesgue number. Then for each $n \in \N$ the number $1/n$ fails: there is a point $a_n \in A$ such that $M_{1/n}(a_n)$ is not contained in any member of $\mathcal{U}$.

By sequential compactness a subsequence $(a_{n_k})$ converges to some $p \in A$. Since $\mathcal{U}$ covers $A$, $p \in U$ for some $U \in \mathcal{U}$, and since $U$ is open there is an $r > 0$ with $M_r(p) \subset U$. Choose $k$ so large that $d(a_{n_k},p) < r/2$ and $1/n_k \le 1/k < r/2$. If $x \in M_{1/n_k}(a_{n_k})$ then
\[ d(x,p) \le d(x,a_{n_k}) + d(a_{n_k},p) < \frac{1}{n_k} + \frac r2 < r , \]
so $M_{1/n_k}(a_{n_k}) \subset M_r(p) \subset U$. This contradicts the choice of $a_{n_k}$. Hence $\mathcal{U}$ has a Lebesgue number.
""", 3, 35, [
    r"Suppose no $\lambda$ works; in particular $1/n$ fails for each $n$. That gives a sequence of bad points.",
    r"A subsequence of the bad points converges to some $p \in A$, and $p$ lies in some open $U$ of the covering together with a ball $M_r(p)$.",
    r"Far along the subsequence, the small bad ball $M_{1/n_k}(a_{n_k})$ fits inside $M_r(p)$.",
], ["c2-def-lebesgue-number", "c2-def-compact", "c2-def-covering"])

s.t("corollary", "c2-cor-lebesgue-diameter", "Lebesgue number lemma, diameter form", r"""
Let $\mathcal{U}$ be an open covering of a sequentially compact subset $A$ of a metric space $M$, and let $\lambda > 0$ be a Lebesgue number for $\mathcal{U}$ (one exists by the Lebesgue number lemma). Then every set $S \subset M$ that contains at least one point of $A$ and satisfies $d(x,y) < \lambda$ for all $x, y \in S$ is contained in a single member of $\mathcal{U}$. In particular, every nonempty subset of $A$ of diameter less than $\lambda$ lies in a single member of $\mathcal{U}$.
""", r"""
Choose a point $a \in S \cap A$. For every $x \in S$ we have $d(x,a) < \lambda$, so $S \subset M_\lambda(a)$. By the definition of a Lebesgue number there is a $U \in \mathcal{U}$ with $M_\lambda(a) \subset U$, and then $S \subset U$.

For the last statement, let $S \subset A$ be nonempty with $\diam S < \lambda$. Then $S$ contains a point of $A$, and for all $x, y \in S$ we have $d(x,y) \le \diam S < \lambda$, because the diameter is an upper bound of these distances. So the first part applies.
""", 1, 10, [
    r"Pick one point $a$ of $S$ that lies in $A$. How far from $a$ can the other points of $S$ be?",
], ["c2-def-lebesgue-number", "c2-lem-lebesgue-number", "c2-def-diameter"])

s.t("lemma", "c2-lem-compact-totally-bounded", "Sequentially compact sets are totally bounded", r"""
Every sequentially compact subset $A$ of a metric space is totally bounded.
""", r"""
Suppose not. Then for some $\eps > 0$ no finite collection of $\eps$-neighborhoods centered at points of $A$ covers $A$. In particular $A \ne \varnothing$; choose $a_1 \in A$. Recursively, having chosen $a_1, \dots, a_n \in A$, the neighborhoods $M_\eps(a_1), \dots, M_\eps(a_n)$ do not cover $A$, so we can choose
\[ a_{n+1} \in A \setminus \big( M_\eps(a_1) \cup \dots \cup M_\eps(a_n) \big). \]
Then $d(a_i, a_j) \ge \eps$ whenever $i < j$. Consequently no subsequence of $(a_n)$ is Cauchy, since any two of its terms are at least $\eps$ apart, and so no subsequence converges, because convergent sequences are Cauchy. This contradicts the sequential compactness of $A$.
""", 3, 25, [
    r"If finitely many $\eps$-balls never suffice, you can keep choosing a new point outside all previous balls.",
    r"The resulting sequence has all its terms at least $\eps$ apart. Can a subsequence converge?",
], ["c2-def-totally-bounded", "c2-def-compact", "c2-prop-convergent-cauchy"])

s.t("theorem", "c2-thm-sequential-implies-covering", "Sequentially compact implies covering compact", r"""
If a subset $A$ of a metric space $M$ is sequentially compact, then every open covering of $A$ reduces to a finite subcovering.
""", r"""
Let $\mathcal{U}$ be an open covering of $A$. By the Lebesgue number lemma it has a Lebesgue number $\lambda > 0$. Since sequentially compact sets are totally bounded, there are finitely many points $a_1, \dots, a_k \in A$ with
\[ A \subset M_\lambda(a_1) \cup \dots \cup M_\lambda(a_k) . \]
By the definition of a Lebesgue number, for each $i$ there is a $U_i \in \mathcal{U}$ with $M_\lambda(a_i) \subset U_i$. Then $A \subset U_1 \cup \dots \cup U_k$, so $\set{U_1, \dots, U_k}$ is a finite subcovering.
""", 2, 20, [
    r"Combine the two lemmas: a Lebesgue number $\lambda$, and total boundedness at scale $\lambda$.",
], ["c2-lem-lebesgue-number", "c2-lem-compact-totally-bounded", "c2-def-covering"])

s.r("c2-rem-compact-equivalence", r"""
Together the two theorems say: \emph{a subset of a metric space is covering compact if and only if it is sequentially compact.} From now on "compact" means either. Each definition has its uses. Sequences are good for extracting limits; coverings are good for passing from local to global, as the next two exercises illustrate.
""")

s.t("exercise", "c2-ex-uniform-continuity-coverings", "Uniform continuity by coverings", r"""
Using the Lebesgue number lemma (and not arguing by contradiction with sequences), prove again: every continuous map $f : M \to N$ from a compact metric space $M$ is uniformly continuous.
""", r"""
Let $\eps > 0$. For each $p \in M$ the $\eps,\delta$ condition gives a $\delta_p > 0$ such that $d_M(x,p) < \delta_p$ implies $d_N(f(x), f(p)) < \eps/2$. The neighborhoods $M_{\delta_p}(p)$, $p \in M$, form an open covering of $M$. Let $\lambda > 0$ be a Lebesgue number for it.

Suppose $x, y \in M$ and $d_M(x,y) < \lambda$. There is a $p \in M$ with $M_\lambda(x) \subset M_{\delta_p}(p)$. Both $x$ and $y$ lie in $M_\lambda(x)$, hence in $M_{\delta_p}(p)$, so
\[ d_N(f(x), f(y)) \le d_N(f(x), f(p)) + d_N(f(p), f(y)) < \frac\eps2 + \frac\eps2 = \eps . \]
Thus $\delta = \lambda$ works for every pair of points, and $f$ is uniformly continuous.
""", 3, 25, [
    r"Continuity gives a $\delta_p$ at each point $p$ (use $\eps/2$). The balls $M_{\delta_p}(p)$ cover $M$.",
    r"Take $\delta$ to be a Lebesgue number of that covering: two points closer than $\delta$ lie in one common ball.",
], ["c2-lem-lebesgue-number", "c2-thm-eps-delta", "c2-def-uniform-continuity", "c2-prop-ball-open"])

s.t("exercise", "c2-ex-closed-in-compact-coverings", "Closed subsets of compact sets, by coverings", r"""
Using only the covering definition, prove: if $A \subset M$ is covering compact and $S \subset A$ is closed in $M$, then $S$ is covering compact.
""", r"""
Let $\mathcal{U}$ be an open covering of $S$. Since $S$ is closed, $S^c$ is open, and $\mathcal{W} = \mathcal{U} \cup \set{S^c}$ is an open covering of $A$: a point of $A$ lies either in $S$, hence in a member of $\mathcal{U}$, or in $S^c$. By covering compactness of $A$, finitely many members of $\mathcal{W}$ cover $A$, and in particular cover $S$. Discard $S^c$ from this finite collection if it is present; since $S^c$ contains no point of $S$, the remaining sets still cover $S$, and they are members of $\mathcal{U}$. So $\mathcal{U}$ reduces to a finite subcovering of $S$.
""", 2, 15, [
    r"Enlarge an open covering of $S$ to an open covering of $A$ by adding one more open set.",
], ["c2-def-covering", "c2-thm-open-closed-dual"])

s.p("c2-cov-tb-prose", r"""
\textbf{Total boundedness.} The Heine–Borel theorem says that in $\R^m$ compact means closed and bounded. In a general metric space that is false. The correct replacement keeps the spirit of both words: "closed" becomes "complete", and "bounded" becomes "totally bounded".
""")

s.t("lemma", "c2-lem-tb-cauchy-subsequence", "In a totally bounded set every sequence has a Cauchy subsequence", r"""
Let $A$ be a totally bounded subset of a metric space $M$. Then every sequence $(a_n)$ of points of $A$ has a subsequence that is a Cauchy sequence.
""", r"""
\emph{Pigeonhole step.} We claim: if $J \subset \N$ is an infinite set of indices and $r > 0$, then there are a point $c \in A$ and an infinite set $J' \subset J$ such that $a_n \in M_r(c)$ for every $n \in J'$. Indeed, by total boundedness there are finitely many points $c_1, \dots, c_m \in A$ with $A \subset M_r(c_1) \cup \dots \cup M_r(c_m)$. For $i = 1, \dots, m$ let
\[ J_i = \set{n \in J : a_n \in M_r(c_i)} . \]
Every $n \in J$ has $a_n \in A$, so $a_n$ lies in at least one of the $m$ neighborhoods, and therefore $J = J_1 \cup \dots \cup J_m$. If every $J_i$ were finite, then $J$, a union of finitely many finite sets, would be finite. So some $J_i$ is infinite, and we take $c = c_i$, $J' = J_i$.

\emph{Nested index sets.} Put $J_0 = \N$. Applying the claim repeatedly, with $J = J_{k-1}$ and $r = 1/k$ at the $k$-th step, we obtain for every $k \ge 1$ a point $c_k \in A$ and an infinite set $J_k \subset J_{k-1}$ with
\[ a_n \in M_{1/k}(c_k) \quad \text{for all } n \in J_k . \]
Thus $\N = J_0 \supset J_1 \supset J_2 \supset \cdots$, and each $J_k$ is infinite.

\emph{Diagonal choice.} Let $n_1$ be the least element of $J_1$. For $k \ge 2$, once $n_{k-1}$ is chosen, the set $\set{n \in J_k : n > n_{k-1}}$ is nonempty, because $J_k$ is infinite while only finitely many natural numbers are $\le n_{k-1}$; let $n_k$ be its least element. Then $n_1 < n_2 < n_3 < \cdots$, so $(a_{n_k})$ is a subsequence of $(a_n)$, and $n_k \in J_k$ for every $k$.

\emph{It is Cauchy.} Let $\eps > 0$ and choose $K \in \N$ with $2/K < \eps$. If $j \ge K$ then $n_j \in J_j \subset J_K$, so $d(a_{n_j}, c_K) < 1/K$. Hence for $j, k \ge K$,
\[ d(a_{n_j}, a_{n_k}) \le d(a_{n_j}, c_K) + d(c_K, a_{n_k}) < \frac2K < \eps . \]
So $(a_{n_k})$ is a Cauchy sequence.
""", 4, 50, [
    r"Finitely many balls of radius $1$ cover $A$, so one of them contains $a_n$ for infinitely many $n$ (why?). Repeat inside that set of indices with radius $1/2$, then $1/3$, and so on.",
    r"You get infinite index sets $\N \supset J_1 \supset J_2 \supset \cdots$ with all $a_n$, $n \in J_k$, in one ball of radius $1/k$. No single $J_k$ is the answer, and their intersection may be empty.",
    r"Choose $n_1 < n_2 < \cdots$ with $n_k \in J_k$. Then all terms from the $K$-th on have indices in $J_K$, so they lie in one ball of radius $1/K$.",
], ["c2-def-totally-bounded", "c2-def-cauchy", "c2-def-subsequence"])

s.t("theorem", "c2-thm-generalized-heine-borel", "Compact means complete and totally bounded", r"""
A subset $A$ of a metric space $M$ is compact if and only if it is complete and totally bounded.
""", r"""
Suppose $A$ is compact. Sequentially compact sets are totally bounded. For completeness let $(a_n)$ be a Cauchy sequence in $A$. By compactness some subsequence converges to a point $a \in A$, and a Cauchy sequence with a convergent subsequence converges to the same limit; so $a_n \to a \in A$. Thus $A$ is complete.

Conversely suppose $A$ is complete and totally bounded, and let $(a_n)$ be a sequence in $A$. Since $A$ is totally bounded, $(a_n)$ has a Cauchy subsequence $(a_{n_k})$. It is a Cauchy sequence in $A$, and $A$ is complete, so it converges to a point of $A$. Thus every sequence in $A$ has a subsequence converging to a point of $A$: $A$ is sequentially compact.
""", 2, 20, [
    r"The forward direction combines two earlier results: compact sets are totally bounded, and a Cauchy sequence with a convergent subsequence converges.",
    r"For the converse, total boundedness supplies a Cauchy subsequence and completeness makes it converge.",
], ["c2-lem-compact-totally-bounded", "c2-lem-cauchy-subsequence", "c2-lem-tb-cauchy-subsequence", "c2-def-cauchy", "c2-def-compact"])

s.t("corollary", "c2-cor-closed-totally-bounded", "Closed and totally bounded in a complete space", r"""
Let $M$ be a complete metric space. A subset $A \subset M$ is compact if and only if it is closed and totally bounded. For $M = \R^m$ this is the Heine–Borel theorem.
""", r"""
In a complete metric space a subset is complete if and only if it is closed: closed subsets of a complete space are complete, and complete subsets of any metric space are closed. So "complete and totally bounded" is the same as "closed and totally bounded", and the statement follows from the theorem that compact means complete and totally bounded.

$\R^m$ is complete, and a subset of $\R^m$ is totally bounded if and only if it is bounded. So in $\R^m$: compact if and only if closed and bounded.
""", 1, 10, [
    r"In a complete space, which subsets are complete?",
], ["c2-thm-generalized-heine-borel", "c2-thm-closed-complete", "c2-thm-rm-complete", "c2-prop-bounded-rm-totally-bounded"])

s.card("c2-card-covering-compact", "Define covering compact.",
       r"$A \subset M$ is covering compact if every covering of $A$ by open subsets of $M$ reduces to a finite subcovering.",
       "c2-def-covering")
s.card("c2-card-covering-example", "Give an open covering of $(0,1]$ with no finite subcovering.",
       r"$U_n = (1/n, 2)$, $n \in \N$. Finitely many of them cover only $(1/N, 2)$.",
       "c2-ex-covering-fails")
s.card("c2-card-lebesgue", "Define Lebesgue number and state the Lebesgue number lemma.",
       r"$\lambda > 0$ is a Lebesgue number for a covering $\mathcal{U}$ of $A$ if every $a \in A$ has $M_\lambda(a) \subset U$ for some $U \in \mathcal{U}$ (ball form). Every open covering of a compact set has one. Consequence (diameter form): every nonempty subset of $A$ of diameter $< \lambda$ lies in a single member of $\mathcal{U}$.",
       "c2-lem-lebesgue-number")
s.card("c2-card-equivalence-idea", "Outline the proof that sequentially compact implies covering compact.",
       r"Take a Lebesgue number $\lambda$ for the covering; cover $A$ by finitely many $\lambda$-balls (total boundedness); each ball lies in one member of the covering.",
       "c2-thm-sequential-implies-covering")
s.card("c2-card-cov-to-seq-idea", "Outline the proof that covering compact implies sequentially compact.",
       r"If $(a_n)$ had no subsequence converging in $A$, each $a \in A$ would have a ball containing $a_n$ for only finitely many $n$; finitely many such balls cover $A$, so there would be only finitely many indices.",
       "c2-thm-covering-implies-sequential")
s.card("c2-card-generalized-hb", "State the generalized Heine–Borel theorem.",
       r"A subset of a metric space is compact iff it is complete and totally bounded. In a complete space: iff closed and totally bounded.",
       "c2-thm-generalized-heine-borel")
s.card("c2-card-generalized-hb-idea", "Idea: why does complete and totally bounded imply compact?",
       r"Given a sequence, total boundedness at radii $1, 1/2, 1/3, \dots$ and the pigeonhole principle give nested infinite index sets $J_1 \supset J_2 \supset \cdots$; choosing $n_1 < n_2 < \cdots$ with $n_k \in J_k$ gives a Cauchy subsequence, which converges by completeness.",
       "c2-thm-generalized-heine-borel")

s.write()
