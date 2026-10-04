from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c2lib import Section

s = Section("2-metric-space-concepts")

s.p("c2-msc-intro", r"""
Almost everything said about limits and continuity on the real line uses only one feature of $\R$: there is a notion of distance, and it obeys the triangle inequality. A \emph{metric space} is a set with exactly that much structure. Working at this level costs nothing and buys a great deal: one proof then covers $\R$, $\R^m$, their subsets, and later spaces whose points are functions. This section sets up the vocabulary: convergence, continuity, open and closed sets, subspaces, products, and completeness.
""")

s.d("c2-def-metric-space", "Metric space", r"""
A \emph{metric space} is a set $M$ together with a function $d : M \times M \to \R$, the \emph{metric}, such that for all $x, y, z \in M$:
\begin{enumerate}
\item (positive definiteness) $d(x,y) \ge 0$, and $d(x,y) = 0$ if and only if $x = y$;
\item (symmetry) $d(x,y) = d(y,x)$;
\item (triangle inequality) $d(x,z) \le d(x,y) + d(y,z)$.
\end{enumerate}
When two spaces are in play we write $d_M$, $d_N$ for their metrics. For $p \in M$ and $r > 0$ the \emph{$r$-neighborhood} (or open ball) of $p$ is
\[ M_r(p) = \set{x \in M : d(x,p) < r}. \]
""")

s.e("c2-ex-metric-spaces", "First metric spaces", r"""
\begin{itemize}
\item $\R$ with $d(x,y) = \abs{x-y}$, and $\R^m$ with the Euclidean distance $d(x,y) = \abs{x-y}$; the triangle inequality for the Euclidean length was proved in Chapter 1.
\item If $M$ is a metric space and $N \subset M$ is any subset, the restriction of $d$ to $N \times N$ makes $N$ a metric space. We say $N$ \emph{inherits} its metric from $M$ and call it a \emph{subspace}. Note that $N_r(p) = M_r(p) \cap N$ for $p \in N$.
\item Any set $M$ carries the \emph{discrete metric}: $d(x,y) = 1$ if $x \ne y$ and $d(x,x) = 0$.
\end{itemize}
Unless something else is said, $\R$, $\R^m$ and their subsets carry these standard metrics.
""")

s.t("exercise", "c2-ex-discrete-metric", "The discrete metric is a metric", r"""
Let $M$ be a set and define $d(x,y) = 1$ if $x \ne y$ and $d(x,x) = 0$. Show that $d$ is a metric on $M$.
""", r"""
Positive definiteness and symmetry are read off the definition: $d$ takes only the values $0$ and $1$, it is $0$ exactly when the two points agree, and the condition $x \ne y$ is symmetric in $x$ and $y$.

For the triangle inequality take $x, y, z \in M$. If $x = z$ then $d(x,z) = 0 \le d(x,y) + d(y,z)$. If $x \ne z$ then $y$ cannot equal both $x$ and $z$, so at least one of $d(x,y)$, $d(y,z)$ is $1$, and $d(x,z) = 1 \le d(x,y) + d(y,z)$.
""", 1, 10, [
    r"Only the triangle inequality needs an argument. Split into the cases $x = z$ and $x \ne z$.",
    r"If $x \ne z$, can $y$ be equal to both of them?",
], ["c2-def-metric-space"])

s.t("lemma", "c2-lem-reverse-triangle", "Reverse triangle inequality", r"""
In a metric space $M$, for all $x, y, z \in M$,
\[ \abs{d(x,z) - d(y,z)} \le d(x,y). \]
""", r"""
By the triangle inequality $d(x,z) \le d(x,y) + d(y,z)$, so $d(x,z) - d(y,z) \le d(x,y)$. Exchanging the roles of $x$ and $y$ and using symmetry, $d(y,z) - d(x,z) \le d(y,x) = d(x,y)$. The two inequalities together say $\abs{d(x,z) - d(y,z)} \le d(x,y)$.
""", 1, 10, [
    r"An inequality $\abs{t} \le c$ is the pair of inequalities $t \le c$ and $-t \le c$. Get each from the triangle inequality.",
], ["c2-def-metric-space"])

s.d("c2-def-convergence", "Convergent sequence", r"""
A sequence $(p_n)$ of points of a metric space $M$ \emph{converges} to $p \in M$ if for every $\eps > 0$ there is an $N \in \N$ such that
\[ n \ge N \implies d(p_n, p) < \eps. \]
We write $p_n \to p$ and call $p$ the \emph{limit} of the sequence. Equivalently, the sequence of real numbers $d(p_n, p)$ converges to $0$.
""")

s.t("theorem", "c2-thm-limit-unique", "Limits are unique", r"""
If a sequence $(p_n)$ in a metric space $M$ converges to $p$ and also to $q$, then $p = q$.
""", r"""
Let $\eps > 0$. Choose $N_1$ with $d(p_n, p) < \eps$ for $n \ge N_1$ and $N_2$ with $d(p_n, q) < \eps$ for $n \ge N_2$. For $n = \max(N_1, N_2)$ the triangle inequality and symmetry give
\[ d(p,q) \le d(p, p_n) + d(p_n, q) < 2\eps. \]
So $0 \le d(p,q) < 2\eps$ for every $\eps > 0$, which forces $d(p,q) = 0$. By positive definiteness $p = q$.
""", 1, 10, [
    r"Estimate $d(p,q)$ by passing through a single far-out term $p_n$.",
    r"A nonnegative number smaller than every positive number is zero. Which axiom then finishes?",
], ["c2-def-metric-space", "c2-def-convergence"])

s.d("c2-def-subsequence", "Subsequence", r"""
A \emph{subsequence} of $(p_n)$ is a sequence $(p_{n_k})_{k \in \N}$ where $n_1 < n_2 < n_3 < \cdots$ are natural numbers. Since the indices increase strictly, $n_k \ge k$ for every $k$.
""")

s.t("proposition", "c2-prop-subsequence-limit", "Subsequences of a convergent sequence", r"""
If $p_n \to p$ in a metric space $M$, then every subsequence $(p_{n_k})$ also converges to $p$.
""", r"""
Let $\eps > 0$ and choose $N$ with $d(p_n,p) < \eps$ for all $n \ge N$. If $k \ge N$ then $n_k \ge k \ge N$, so $d(p_{n_k}, p) < \eps$. Hence $p_{n_k} \to p$ as $k \to \infty$.
""", 1, 10, [
    r"Use $n_k \ge k$.",
], ["c2-def-convergence", "c2-def-subsequence"])

s.p("c2-msc-continuity-prose", r"""
\textbf{Continuity.} There are three ways to say that a map between metric spaces is continuous: with sequences, with $\eps$ and $\delta$, and with open sets. We take the first as the definition and prove that the others say the same thing. Each is the convenient one in some situation, so all three should be at your fingertips.
""")

s.d("c2-def-continuity", "Continuous map", r"""
Let $M$ and $N$ be metric spaces. A map $f : M \to N$ is \emph{continuous} if it preserves sequential convergence: whenever $p_n \to p$ in $M$, we have $f(p_n) \to f(p)$ in $N$.
""")

s.t("theorem", "c2-thm-composite-continuous", "Composites of continuous maps", r"""
If $f : M \to N$ and $g : N \to P$ are continuous maps of metric spaces, then $g \circ f : M \to P$ is continuous.
""", r"""
Let $p_n \to p$ in $M$. Since $f$ is continuous, $f(p_n) \to f(p)$ in $N$. This is a convergent sequence in $N$, so continuity of $g$ gives $g(f(p_n)) \to g(f(p))$ in $P$. Thus $g \circ f$ preserves sequential convergence.
""", 1, 10, [
    r"Feed a convergent sequence through $f$, then through $g$.",
], ["c2-def-continuity"])

s.t("theorem", "c2-thm-eps-delta", r"The $\eps,\delta$ condition", r"""
A map $f : M \to N$ of metric spaces is continuous if and only if it satisfies the \emph{$\eps,\delta$ condition}: for every $p \in M$ and every $\eps > 0$ there is a $\delta > 0$ such that for all $x \in M$,
\[ d_M(x,p) < \delta \implies d_N(f(x), f(p)) < \eps. \]
""", r"""
Suppose the $\eps,\delta$ condition holds, and let $p_n \to p$ in $M$. Given $\eps > 0$ take the $\delta > 0$ supplied for $p$ and $\eps$. Since $p_n \to p$ there is an $N$ with $d_M(p_n,p) < \delta$ for all $n \ge N$, and then $d_N(f(p_n), f(p)) < \eps$ for all $n \ge N$. So $f(p_n) \to f(p)$, and $f$ is continuous.

Conversely, suppose the $\eps,\delta$ condition fails. Then there are a point $p \in M$ and an $\eps > 0$ for which no $\delta$ works: for every $\delta > 0$ there is an $x \in M$ with $d_M(x,p) < \delta$ and $d_N(f(x), f(p)) \ge \eps$. Applying this with $\delta = 1/n$ gives points $x_n$ with
\[ d_M(x_n, p) < \frac1n \quad\text{and}\quad d_N(f(x_n), f(p)) \ge \eps . \]
The first inequality shows $x_n \to p$ (given $\eta > 0$, any $N > 1/\eta$ works). The second shows that $f(x_n)$ does not converge to $f(p)$. So $f$ is not continuous. By contraposition, a continuous map satisfies the $\eps,\delta$ condition.
""", 3, 25, [
    r"One direction is a direct unwinding of definitions. For the other, argue by contraposition.",
    r"Negate the $\eps,\delta$ condition carefully: there are a $p$ and an $\eps$ such that \emph{every} $\delta$ fails.",
    r"Use $\delta = 1/n$ to manufacture a sequence $x_n \to p$ whose images stay at distance at least $\eps$ from $f(p)$.",
], ["c2-def-continuity", "c2-def-convergence"])

s.d("c2-def-homeomorphism", "Homeomorphism", r"""
A \emph{homeomorphism} is a bijection $f : M \to N$ of metric spaces such that both $f$ and its inverse $f^{-1} : N \to M$ are continuous. If one exists, $M$ and $N$ are \emph{homeomorphic}, written $M \cong N$. A property of metric spaces is \emph{topological} if, whenever $M$ has it, so does every space homeomorphic to $M$.
""")

s.e("c2-ex-circle", "A continuous bijection that is not a homeomorphism", r"""
Wrap the interval $[0, 2\pi)$ around the unit circle $S^1 \subset \R^2$ by $f(x) = (\cos x, \sin x)$. This is a continuous bijection. Its inverse is not continuous: the points $f(2\pi - 1/n)$ converge to $f(0) = (1,0)$ on the circle, while their preimages $2\pi - 1/n$ do not converge to $0$. Continuity of the inverse is a real extra demand. (We will see in the next section that it is automatic when the domain is compact.)
""")

s.p("c2-msc-open-closed-prose", r"""
\textbf{Closed sets and open sets.} A closed set is one you cannot leave by taking limits; an open set is one in which every point has some elbow room. The two notions turn out to be complementary.
""")

s.d("c2-def-limit-of-set", "Limit of a set", r"""
Let $S$ be a subset of a metric space $M$. A point $p \in M$ is a \emph{limit of $S$} if there is a sequence $(p_n)$ of points of $S$ with $p_n \to p$. The set of all limits of $S$ is written $\lim S$. Every point $p$ of $S$ is a limit of $S$ (take the constant sequence), so $S \subset \lim S$.
""")

s.d("c2-def-closed-open", "Closed set, open set", r"""
Let $S$ be a subset of a metric space $M$.
\begin{itemize}
\item $S$ is \emph{closed} if it contains all its limits: $\lim S \subset S$.
\item $S$ is \emph{open} if for each $p \in S$ there is an $r > 0$ with $M_r(p) \subset S$.
\end{itemize}
A set that is both closed and open is \emph{clopen}. We write $S^c = M \setminus S$ for the complement.
""")

s.t("lemma", "c2-lem-limit-ball", "Limits and neighborhoods", r"""
Let $S \subset M$ and $p \in M$. Then $p$ is a limit of $S$ if and only if every neighborhood $M_r(p)$, $r > 0$, contains a point of $S$.
""", r"""
If $p$ is a limit of $S$, take $p_n \in S$ with $p_n \to p$. Given $r > 0$ there is an $N$ with $d(p_N, p) < r$, so $p_N \in M_r(p) \cap S$.

Conversely suppose every neighborhood of $p$ meets $S$. For each $n \in \N$ choose $p_n \in M_{1/n}(p) \cap S$. Given $\eps > 0$ pick $N > 1/\eps$; then for $n \ge N$ we have $d(p_n, p) < 1/n \le 1/N < \eps$. So $(p_n)$ is a sequence in $S$ converging to $p$.
""", 1, 10, [
    r"For the converse, use the neighborhoods of radius $1/n$ to pick the terms of a sequence.",
], ["c2-def-limit-of-set", "c2-def-convergence"])

s.t("theorem", "c2-thm-open-closed-dual", "Open and closed are complementary", r"""
Let $S$ be a subset of a metric space $M$. Then $S$ is closed if and only if $S^c$ is open. Consequently $S$ is open if and only if $S^c$ is closed.
""", r"""
Suppose $S$ is closed and let $p \in S^c$. If no neighborhood of $p$ were contained in $S^c$, then every $M_r(p)$ would contain a point of $S$, and by the lemma on limits and neighborhoods $p$ would be a limit of $S$. As $S$ is closed this gives $p \in S$, contrary to $p \in S^c$. So some $M_r(p) \subset S^c$, and $S^c$ is open.

Suppose $S^c$ is open and let $p$ be a limit of $S$. If $p \in S^c$ there is an $r > 0$ with $M_r(p) \subset S^c$, a neighborhood of $p$ containing no point of $S$; by the same lemma $p$ is then not a limit of $S$, a contradiction. So $p \in S$, and $S$ is closed.

The last sentence follows by applying what was proved to the set $S^c$, whose complement is $S$.
""", 2, 15, [
    r"The lemma on limits and neighborhoods translates between sequences and balls. Use it in both directions.",
    r"If $S$ is closed and $p \notin S$, what would it mean if every ball about $p$ met $S$?",
], ["c2-def-closed-open", "c2-lem-limit-ball"])

s.t("theorem", "c2-thm-topology", "The open sets form a topology", r"""
In a metric space $M$:
\begin{enumerate}
\item $\varnothing$ and $M$ are open;
\item the union of any collection of open sets is open;
\item the intersection of finitely many open sets is open.
\end{enumerate}
""", r"""
(1) The condition for $\varnothing$ to be open is vacuous, since it has no points. For $p \in M$ we have $M_1(p) \subset M$, so $M$ is open.

(2) Let $\set{U_\alpha}$ be a collection of open sets and $p \in \bigcup_\alpha U_\alpha$. Then $p \in U_\beta$ for some $\beta$, and since $U_\beta$ is open there is an $r > 0$ with $M_r(p) \subset U_\beta \subset \bigcup_\alpha U_\alpha$.

(3) Let $U_1, \dots, U_k$ be open and $p \in U_1 \cap \dots \cap U_k$. For each $i$ there is an $r_i > 0$ with $M_{r_i}(p) \subset U_i$. Put $r = \min(r_1, \dots, r_k) > 0$. Then $M_r(p) \subset M_{r_i}(p) \subset U_i$ for every $i$, so $M_r(p) \subset U_1 \cap \dots \cap U_k$.
""", 1, 15, [
    r"For a finite intersection you get finitely many radii. Which single radius works for all of them?",
], ["c2-def-closed-open"])

s.t("corollary", "c2-cor-closed-sets", "Intersections and unions of closed sets", r"""
In a metric space $M$: $\varnothing$ and $M$ are closed; the intersection of any collection of closed sets is closed; the union of finitely many closed sets is closed.
""", r"""
By the theorem that open and closed are complementary, a set is closed exactly when its complement is open. The complements of $\varnothing$ and $M$ are $M$ and $\varnothing$, which are open. If $\set{K_\alpha}$ is a collection of closed sets, De Morgan's law gives
\[ \Big(\bigcap_\alpha K_\alpha\Big)^c = \bigcup_\alpha K_\alpha^c , \]
a union of open sets, hence open; so $\bigcap_\alpha K_\alpha$ is closed. If $K_1, \dots, K_k$ are closed then
\[ (K_1 \cup \dots \cup K_k)^c = K_1^c \cap \dots \cap K_k^c \]
is a finite intersection of open sets, hence open; so $K_1 \cup \dots \cup K_k$ is closed.
""", 1, 10, [
    r"Take complements and use De Morgan's laws.",
], ["c2-thm-open-closed-dual", "c2-thm-topology"])

s.r("c2-rem-infinite-intersections", r"""
Finiteness matters. In $\R$ the open intervals $(-1/n, 1/n)$ intersect in $\set{0}$, which is not open; the closed intervals $[1/n, 1]$ have union $(0,1]$, which is not closed. Also, most sets are neither open nor closed, for instance $[0,1)$ or $\Q$ in $\R$; and some are both, for instance $\varnothing$ and $M$.
""")

s.t("proposition", "c2-prop-ball-open", "Neighborhoods are open", r"""
In a metric space $M$, every neighborhood $M_r(p)$ is an open set.
""", r"""
Let $q \in M_r(p)$ and put $s = r - d(q,p)$, which is positive. If $x \in M_s(q)$ then
\[ d(x,p) \le d(x,q) + d(q,p) < s + d(q,p) = r , \]
so $x \in M_r(p)$. Thus $M_s(q) \subset M_r(p)$, and $M_r(p)$ is open.
""", 1, 10, [
    r"A point $q$ of the ball is at distance less than $r$ from $p$. How much room is left?",
], ["c2-def-closed-open", "c2-def-metric-space"])

s.t("exercise", "c2-ex-closed-ball", "Closed balls are closed", r"""
For $p$ in a metric space $M$ and $r \ge 0$, show that the \emph{closed ball} $D_r(p) = \set{x \in M : d(x,p) \le r}$ is a closed set. In particular every one-point set $\set{p}$ is closed.
""", r"""
We show that the complement is open. Let $q \notin D_r(p)$, so $d(q,p) > r$, and put $s = d(q,p) - r > 0$. If $x \in M_s(q)$ then by the triangle inequality $d(q,p) \le d(q,x) + d(x,p) < s + d(x,p)$, so $d(x,p) > d(q,p) - s = r$ and $x \notin D_r(p)$. Hence $M_s(q) \subset D_r(p)^c$. The complement of $D_r(p)$ is open, so $D_r(p)$ is closed because open and closed are complementary. Finally $D_0(p) = \set{p}$ by positive definiteness.
""", 2, 15, [
    r"Either show the complement is open, or take a convergent sequence in the ball and estimate the distance from its limit to $p$.",
], ["c2-thm-open-closed-dual", "c2-def-closed-open", "c2-def-metric-space"])

s.t("theorem", "c2-thm-lim-closed", "The limit set is closed", r"""
For every subset $S$ of a metric space $M$, the set $\lim S$ of limits of $S$ is a closed set.
""", r"""
Let $p$ be a limit of $\lim S$; we must show $p \in \lim S$. Let $r > 0$. By the lemma on limits and neighborhoods, applied to the set $\lim S$, there is a point $q \in \lim S$ with $d(q,p) < r/2$. By the same lemma applied to $S$ and its limit $q$, there is a point $x \in S$ with $d(x,q) < r/2$. Then
\[ d(x,p) \le d(x,q) + d(q,p) < r , \]
so $M_r(p)$ contains a point of $S$. As $r > 0$ was arbitrary, the lemma shows that $p$ is a limit of $S$.
""", 2, 20, [
    r"A limit of limits should be a limit. Work with neighborhoods rather than sequences.",
    r"Within $r/2$ of $p$ there is a point $q$ of $\lim S$, and within $r/2$ of $q$ there is a point of $S$.",
], ["c2-lem-limit-ball", "c2-def-closed-open"])

s.d("c2-def-closure-interior-boundary", "Closure, interior, boundary", r"""
Let $S$ be a subset of a metric space $M$.
\begin{itemize}
\item The \emph{closure} $\overline{S}$ is the intersection of all closed subsets of $M$ that contain $S$.
\item The \emph{interior} $\interior S$ is the union of all open subsets of $M$ that are contained in $S$.
\item The \emph{boundary} is $\partial S = \overline{S} \setminus \interior S$.
\end{itemize}
""")

s.t("proposition", "c2-prop-closure-lim", "The closure is the limit set", r"""
For every subset $S$ of a metric space $M$, $\overline{S} = \lim S$. Consequently $\overline{S}$ is closed, it is the smallest closed set containing $S$, and $S$ is closed if and only if $S = \overline{S}$.
""", r"""
The set $\lim S$ is closed (the limit set is closed) and contains $S$, so it is one of the sets being intersected in the definition of $\overline{S}$; hence $\overline{S} \subset \lim S$.

For the other inclusion let $K$ be any closed set with $S \subset K$, and let $p \in \lim S$. There is a sequence in $S$, hence in $K$, converging to $p$, so $p$ is a limit of $K$, and $p \in K$ because $K$ is closed. Thus $\lim S \subset K$ for every such $K$, and therefore $\lim S \subset \overline{S}$.

So $\overline{S} = \lim S$. It is closed, it contains $S$, and by its definition it is contained in every closed set containing $S$: it is the smallest such set. If $S$ is closed then $S$ itself is a closed set containing $S$, so $\overline{S} \subset S \subset \overline{S}$; conversely if $S = \overline{S}$ then $S$ is closed because $\overline{S}$ is.
""", 2, 20, [
    r"Prove two inclusions. One uses that $\lim S$ is itself a closed set containing $S$.",
    r"For $\lim S \subset \overline{S}$: a limit of $S$ is a limit of any closed $K \supset S$.",
], ["c2-thm-lim-closed", "c2-def-closure-interior-boundary", "c2-def-closed-open"])

s.t("proposition", "c2-prop-interior", "The interior, pointwise", r"""
For every subset $S$ of a metric space $M$, the interior $\interior S$ is open, it is the largest open set contained in $S$, and
\[ \interior S = \set{p \in M : M_r(p) \subset S \text{ for some } r > 0}. \]
""", r"""
$\interior S$ is a union of open sets, so it is open; each of those sets lies in $S$, so $\interior S \subset S$; and every open subset of $S$ is one of the sets in the union, so it is contained in $\interior S$. That is what "largest open set contained in $S$" means.

If $p \in \interior S$ then $p \in U$ for some open $U \subset S$, and openness of $U$ gives an $r > 0$ with $M_r(p) \subset U \subset S$. Conversely, if $M_r(p) \subset S$ for some $r > 0$, then $M_r(p)$ is an open set (neighborhoods are open) contained in $S$, so $M_r(p) \subset \interior S$, and in particular $p \in \interior S$.
""", 1, 15, [
    r"For the displayed formula, remember that $M_r(p)$ is itself an open set.",
], ["c2-def-closure-interior-boundary", "c2-thm-topology", "c2-prop-ball-open"])

s.t("exercise", "c2-ex-boundary", "The boundary is closed", r"""
Show that for every subset $S$ of a metric space $M$,
\[ M \setminus \interior S = \overline{S^c} \qquad\text{and hence}\qquad \partial S = \overline{S} \cap \overline{S^c}. \]
Conclude that $\partial S$ is closed and that $\partial S = \partial (S^c)$.
""", r"""
A point $p$ fails to lie in $\interior S$ exactly when no neighborhood $M_r(p)$ is contained in $S$ (the interior, pointwise), that is, when every $M_r(p)$ contains a point of $S^c$. By the lemma on limits and neighborhoods this says $p \in \lim (S^c)$, and $\lim(S^c) = \overline{S^c}$ because the closure is the limit set. So $M \setminus \interior S = \overline{S^c}$.

Therefore $\partial S = \overline{S} \setminus \interior S = \overline{S} \cap (M \setminus \interior S) = \overline{S} \cap \overline{S^c}$. This is an intersection of two closed sets, hence closed. The formula is unchanged when $S$ and $S^c$ are exchanged, since $(S^c)^c = S$; so $\partial(S^c) = \overline{S^c} \cap \overline{S} = \partial S$.
""", 2, 20, [
    r"Describe the points \emph{not} in the interior using neighborhoods, then recognise the description of a limit of $S^c$.",
], ["c2-prop-interior", "c2-prop-closure-lim", "c2-lem-limit-ball", "c2-cor-closed-sets"])

s.e("c2-ex-closure-examples", "Closure, interior, boundary on the line", r"""
In $\R$: for $S = [0,1)$ we get $\overline{S} = [0,1]$, $\interior S = (0,1)$, $\partial S = \set{0,1}$. For $S = \Q$ every interval contains rationals and irrationals, so $\overline{\Q} = \R$, $\interior \Q = \varnothing$ and $\partial \Q = \R$. A set whose closure is all of $M$ is called \emph{dense} in $M$.
""")

s.t("theorem", "c2-thm-open-set-condition", "Open and closed set conditions for continuity", r"""
For a map $f : M \to N$ of metric spaces the following are equivalent:
\begin{enumerate}
\item $f$ is continuous;
\item (closed set condition) the preimage $f^{-1}(K)$ of every closed set $K \subset N$ is closed in $M$;
\item (open set condition) the preimage $f^{-1}(U)$ of every open set $U \subset N$ is open in $M$.
\end{enumerate}
""", r"""
(1) $\Rightarrow$ (2). Let $K \subset N$ be closed and let $p$ be a limit of $f^{-1}(K)$: there are $p_n \in f^{-1}(K)$ with $p_n \to p$. By continuity $f(p_n) \to f(p)$, and each $f(p_n)$ lies in $K$, so $f(p)$ is a limit of $K$. As $K$ is closed, $f(p) \in K$, i.e. $p \in f^{-1}(K)$. So $f^{-1}(K)$ is closed.

(2) $\Rightarrow$ (3). Let $U \subset N$ be open. Then $U^c$ is closed, so $f^{-1}(U^c)$ is closed by (2). But $f^{-1}(U^c) = M \setminus f^{-1}(U)$, so $f^{-1}(U)$ is the complement of a closed set and is open.

(3) $\Rightarrow$ (1). We verify the $\eps,\delta$ condition. Let $p \in M$ and $\eps > 0$. The neighborhood $U = N_\eps(f(p))$ is open in $N$, so $f^{-1}(U)$ is open in $M$ by (3), and it contains $p$. Hence there is a $\delta > 0$ with $M_\delta(p) \subset f^{-1}(U)$; that is, $d_M(x,p) < \delta$ implies $d_N(f(x), f(p)) < \eps$. By the theorem on the $\eps,\delta$ condition, $f$ is continuous.
""", 3, 30, [
    r"Prove (1) $\Rightarrow$ (2) $\Rightarrow$ (3) $\Rightarrow$ (1). The middle step is just complements: $f^{-1}(U^c) = f^{-1}(U)^c$.",
    r"For (1) $\Rightarrow$ (2), take a sequence in $f^{-1}(K)$ converging to $p$ and push it forward.",
    r"For (3) $\Rightarrow$ (1), apply (3) to the open set $N_\eps(f(p))$ and compare with the $\eps,\delta$ condition.",
], ["c2-def-continuity", "c2-thm-eps-delta", "c2-thm-open-closed-dual", "c2-prop-ball-open"])

s.r("c2-rem-preimages", r"""
The conditions are about \emph{preimages}. A continuous map need not send open sets to open sets or closed sets to closed sets: $x \mapsto x^2$ sends the open interval $(-1,1)$ onto $[0,1)$. A homeomorphism $f$ does both, because the image of $S$ under $f$ is the preimage of $S$ under the continuous map $f^{-1}$. So a homeomorphism matches the open sets of $M$ with the open sets of $N$, and any property that can be phrased in terms of open sets alone is topological.
""")

s.p("c2-msc-inheritance-prose", r"""
\textbf{Inheritance.} When $N \subset M$ is a subspace, a set $S \subset N$ can be asked to be open or closed \emph{in $N$} or \emph{in $M$}, and the answers can differ: $[0,1)$ is open in $[0,2]$, since it is the neighborhood of $0$ of radius $1$ there, but it is not open in $\R$. The next theorem says exactly how the two are related. Note that a sequence of points of $N$ converges in $N$ to $p \in N$ exactly when it converges in $M$ to $p$, because the distances are the same.
""")

s.t("theorem", "c2-thm-inheritance", "Inheritance principle", r"""
Let $N$ be a subspace of a metric space $M$ and $S \subset N$. Then
\begin{enumerate}
\item $S$ is closed in $N$ if and only if $S = N \cap L$ for some set $L$ that is closed in $M$;
\item $S$ is open in $N$ if and only if $S = N \cap U$ for some set $U$ that is open in $M$.
\end{enumerate}
""", r"""
(1) Suppose $S$ is closed in $N$, and let $L = \overline{S}$ be the closure of $S$ in $M$, a closed subset of $M$ equal to the set of limits in $M$ of $S$. Clearly $S \subset N \cap L$. If $p \in N \cap L$, then some sequence of points of $S$ converges in $M$ to $p$; since $p \in N$, the sequence converges to $p$ in $N$ as well, so $p$ is a limit of $S$ in $N$ and $p \in S$ because $S$ is closed in $N$. Hence $S = N \cap L$.

Conversely suppose $S = N \cap L$ with $L$ closed in $M$, and let $(p_n)$ be a sequence in $S$ converging in $N$ to a point $p \in N$. The sequence also converges to $p$ in $M$, and its terms lie in $L$, so $p \in L$ as $L$ is closed in $M$. Thus $p \in N \cap L = S$, and $S$ is closed in $N$.

(2) Since open and closed are complementary in the metric space $N$, $S$ is open in $N$ if and only if $N \setminus S$ is closed in $N$, which by (1) happens if and only if $N \setminus S = N \cap L$ for some closed $L \subset M$. Taking complements within $N$, the equation $N \setminus S = N \cap L$ is equivalent to $S = N \setminus (N \cap L) = N \cap L^c$. As $L$ ranges over the closed subsets of $M$, $U = L^c$ ranges over the open subsets of $M$. So $S$ is open in $N$ if and only if $S = N \cap U$ for some open $U \subset M$.
""", 3, 30, [
    r"Do the closed case with sequences, then get the open case by taking complements inside $N$.",
    r"If $S$ is closed in $N$, a natural candidate for $L$ is the closure of $S$ in $M$.",
    r"A sequence in $N$ converges in $N$ to $p \in N$ if and only if it converges to $p$ in $M$.",
], ["c2-prop-closure-lim", "c2-thm-open-closed-dual", "c2-def-closed-open"])

s.t("corollary", "c2-cor-inheritance", "Subsets of closed and of open subspaces", r"""
Let $S \subset N \subset M$.
\begin{enumerate}
\item If $N$ is closed in $M$, then $S$ is closed in $N$ if and only if $S$ is closed in $M$.
\item If $N$ is open in $M$, then $S$ is open in $N$ if and only if $S$ is open in $M$.
\end{enumerate}
""", r"""
(1) If $S$ is closed in $M$ then $S = N \cap S$ exhibits $S$ as $N \cap L$ with $L = S$ closed in $M$, so $S$ is closed in $N$ by the inheritance principle (this direction does not use that $N$ is closed). If $S$ is closed in $N$, then $S = N \cap L$ with $L$ closed in $M$; since $N$ is closed in $M$ too, $S$ is an intersection of two closed subsets of $M$ and is closed in $M$.

(2) The same argument with "open" in place of "closed": if $S$ is open in $M$ then $S = N \cap S$; if $S$ is open in $N$ then $S = N \cap U$ with $U$ open in $M$, an intersection of two open subsets of $M$, which is open in $M$.
""", 1, 10, [
    r"Apply the inheritance principle; an intersection of two closed (or two open) sets is closed (open).",
], ["c2-thm-inheritance", "c2-thm-topology", "c2-cor-closed-sets"])

s.p("c2-msc-product-prose", r"""
\textbf{Product metrics.} The plane is the product $\R \times \R$, and its Euclidean distance is built from the distances in the two factors. The same recipe works for any two metric spaces, and there are two other natural recipes. For questions of convergence it makes no difference which is used.
""")

s.d("c2-def-product-metrics", "Product metrics", r"""
Let $X$ and $Y$ be metric spaces and $M = X \times Y$. For $p = (x,y)$ and $p' = (x',y')$ in $M$ define
\begin{align*}
d_E(p,p') &= \sqrt{d_X(x,x')^2 + d_Y(y,y')^2}, \\
d_{\max}(p,p') &= \max\set{d_X(x,x'),\, d_Y(y,y')}, \\
d_{\mathrm{sum}}(p,p') &= d_X(x,x') + d_Y(y,y').
\end{align*}
For $X = Y = \R$ the first is the Euclidean metric on $\R^2$.
""")

s.t("exercise", "c2-ex-product-metrics", "The three product metrics", r"""
Show that $d_E$, $d_{\max}$ and $d_{\mathrm{sum}}$ are metrics on $M = X \times Y$, and that for all $p, p' \in M$
\[ d_{\max}(p,p') \le d_E(p,p') \le d_{\mathrm{sum}}(p,p') \le 2\, d_{\max}(p,p'). \]
""", r"""
Write $p = (x,y)$, $p' = (x',y')$, $p'' = (x'',y'')$ and
\[ a = d_X(x,x'),\quad b = d_Y(y,y'),\quad a' = d_X(x',x''),\quad b' = d_Y(y',y''). \]
These are nonnegative numbers.

\emph{Positive definiteness and symmetry.} Each of $\sqrt{a^2+b^2}$, $\max\set{a,b}$, $a+b$ is nonnegative and vanishes exactly when $a = b = 0$, that is when $x = x'$ and $y = y'$, that is when $p = p'$. Each is unchanged when $p$ and $p'$ are exchanged, because $d_X$ and $d_Y$ are symmetric.

\emph{Triangle inequality.} By the triangle inequalities in $X$ and $Y$, $d_X(x,x'') \le a + a'$ and $d_Y(y,y'') \le b + b'$. Hence
\begin{align*}
d_{\mathrm{sum}}(p,p'') &\le (a+a') + (b+b') = d_{\mathrm{sum}}(p,p') + d_{\mathrm{sum}}(p',p''), \\
d_{\max}(p,p'') &\le \max\set{a+a',\, b+b'} \le \max\set{a,b} + \max\set{a',b'} = d_{\max}(p,p') + d_{\max}(p',p''),
\end{align*}
and, using that $t \mapsto t^2$ is increasing on $[0,\infty)$ and then the triangle inequality for the Euclidean length in $\R^2$ applied to the vectors $(a,b)$ and $(a',b')$,
\[ d_E(p,p'') \le \sqrt{(a+a')^2 + (b+b')^2} = \abs{(a,b) + (a',b')} \le \abs{(a,b)} + \abs{(a',b')} = d_E(p,p') + d_E(p',p''). \]

\emph{Comparison.} For $a, b \ge 0$ we have $\max\set{a,b}^2 \le a^2 + b^2 \le a^2 + 2ab + b^2 = (a+b)^2$; taking square roots gives $\max\set{a,b} \le \sqrt{a^2+b^2} \le a + b$. And $a + b \le 2\max\set{a,b}$. These are the three stated inequalities.
""", 2, 25, [
    r"Name the four distances $a, b, a', b'$ in the factors; everything reduces to inequalities among nonnegative reals.",
    r"For the triangle inequality of $d_E$, use the triangle inequality for vectors in $\R^2$ from Chapter 1.",
], ["c2-def-product-metrics", "c2-def-metric-space"])

s.t("theorem", "c2-thm-product-convergence", "Convergence in a product", r"""
Let $(x_n)$ be a sequence in $X$ and $(y_n)$ a sequence in $Y$, and let $x \in X$, $y \in Y$. The following are equivalent:
\begin{enumerate}
\item $(x_n, y_n) \to (x,y)$ with respect to $d_{\max}$;
\item $(x_n, y_n) \to (x,y)$ with respect to $d_E$;
\item $(x_n, y_n) \to (x,y)$ with respect to $d_{\mathrm{sum}}$;
\item $x_n \to x$ in $X$ and $y_n \to y$ in $Y$.
\end{enumerate}
""", r"""
Write $p_n = (x_n,y_n)$ and $p = (x,y)$. By the comparison of the three product metrics,
\[ d_{\max}(p_n,p) \le d_E(p_n,p) \le d_{\mathrm{sum}}(p_n,p) \le 2\,d_{\max}(p_n,p). \]
If (3) holds, then given $\eps > 0$ eventually $d_{\mathrm{sum}}(p_n,p) < \eps$, hence eventually $d_E(p_n,p) < \eps$: (2) holds. In the same way (2) implies (1). If (1) holds, then given $\eps > 0$ eventually $d_{\max}(p_n,p) < \eps/2$, hence $d_{\mathrm{sum}}(p_n,p) < \eps$: (3) holds. So (1), (2), (3) are equivalent.

(1) $\Rightarrow$ (4): $d_X(x_n,x) \le d_{\max}(p_n,p)$ and $d_Y(y_n,y) \le d_{\max}(p_n,p)$, so both tend to $0$.

(4) $\Rightarrow$ (1): given $\eps > 0$ choose $N_1$ with $d_X(x_n,x) < \eps$ for $n \ge N_1$ and $N_2$ with $d_Y(y_n,y) < \eps$ for $n \ge N_2$. For $n \ge \max(N_1,N_2)$ both distances are less than $\eps$, so $d_{\max}(p_n,p) < \eps$.
""", 2, 20, [
    r"The chain $d_{\max} \le d_E \le d_{\mathrm{sum}} \le 2d_{\max}$ makes the first three equivalent.",
    r"Compare (4) with convergence in $d_{\max}$, which is the easiest of the three to unwind.",
], ["c2-ex-product-metrics", "c2-def-convergence"])

s.t("corollary", "c2-cor-rm-convergence", r"Convergence in $\R^m$ is componentwise", r"""
A sequence of vectors $v_n = (v_{n1}, \dots, v_{nm})$ in $\R^m$ converges to $a = (a_1, \dots, a_m)$ if and only if $v_{ni} \to a_i$ in $\R$ as $n \to \infty$, for each $i = 1, \dots, m$.
""", r"""
For any vector $w = (w_1, \dots, w_m) \in \R^m$ and any index $i$,
\[ \abs{w_i} \le \abs{w} \le \abs{w_1} + \dots + \abs{w_m}. \]
The first inequality holds because $w_i^2 \le w_1^2 + \dots + w_m^2$; the second because $w_1^2 + \dots + w_m^2 \le (\abs{w_1} + \dots + \abs{w_m})^2$, the right side being the left side plus nonnegative cross terms. Taking square roots, which preserves order among nonnegative numbers, gives the displayed inequalities.

Apply this to $w = v_n - a$. If $v_n \to a$ then $\abs{v_{ni} - a_i} \le \abs{v_n - a} \to 0$ for each $i$. Conversely, suppose $v_{ni} \to a_i$ for each $i$, and let $\eps > 0$. Choose $N_i$ with $\abs{v_{ni} - a_i} < \eps/m$ for $n \ge N_i$. For $n \ge \max(N_1, \dots, N_m)$,
\[ \abs{v_n - a} \le \sum_{i=1}^m \abs{v_{ni} - a_i} < \eps . \]
So $v_n \to a$.
""", 2, 15, [
    r"Sandwich: each $\abs{w_i}$ is at most $\abs{w}$, and $\abs{w}$ is at most the sum of the $\abs{w_i}$.",
], ["c2-def-convergence"])

s.t("theorem", "c2-thm-metric-continuous", "The metric is continuous", r"""
Let $M$ be a metric space. If $p_n \to p$ and $q_n \to q$ in $M$, then $d(p_n, q_n) \to d(p,q)$ in $\R$. Equivalently, $d : M \times M \to \R$ is continuous with respect to any of the product metrics on $M \times M$.
""", r"""
By the triangle inequality, $d(p_n,q_n) \le d(p_n,p) + d(p,q) + d(q,q_n)$ and $d(p,q) \le d(p,p_n) + d(p_n,q_n) + d(q_n,q)$. Together with symmetry these give
\[ \abs{d(p_n,q_n) - d(p,q)} \le d(p_n,p) + d(q_n,q). \]
Given $\eps > 0$ choose $N$ so large that $d(p_n,p) < \eps/2$ and $d(q_n,q) < \eps/2$ for all $n \ge N$. Then $\abs{d(p_n,q_n) - d(p,q)} < \eps$ for $n \ge N$, so $d(p_n,q_n) \to d(p,q)$.

For the reformulation: by the theorem on convergence in a product, a sequence $(p_n,q_n)$ converges to $(p,q)$ in $M \times M$, for any of the three product metrics, exactly when $p_n \to p$ and $q_n \to q$. So what was proved is that $d$ preserves sequential convergence.
""", 2, 15, [
    r"Bound $\abs{d(p_n,q_n) - d(p,q)}$ by $d(p_n,p) + d(q_n,q)$ using the triangle inequality twice.",
], ["c2-thm-product-convergence", "c2-def-continuity", "c2-def-metric-space"])

s.p("c2-msc-complete-prose", r"""
\textbf{Completeness.} In Chapter 1 the real line was shown to be complete: a sequence whose terms crowd together must converge. The crowding condition makes sense in any metric space, but whether it forces convergence depends on the space.
""")

s.d("c2-def-cauchy", "Cauchy sequence, complete space", r"""
A sequence $(p_n)$ in a metric space $M$ is \emph{Cauchy} if for every $\eps > 0$ there is an $N$ such that
\[ m, n \ge N \implies d(p_m, p_n) < \eps. \]
$M$ is \emph{complete} if every Cauchy sequence in $M$ converges to a limit in $M$. A subset of $M$ is complete if it is complete as a subspace.
""")

s.t("proposition", "c2-prop-convergent-cauchy", "Convergent sequences are Cauchy", r"""
Every convergent sequence in a metric space is a Cauchy sequence.
""", r"""
Let $p_n \to p$ and $\eps > 0$. Choose $N$ with $d(p_n,p) < \eps/2$ for all $n \ge N$. For $m, n \ge N$,
\[ d(p_m,p_n) \le d(p_m,p) + d(p,p_n) < \eps . \]
""", 1, 10, [
    r"Compare $p_m$ and $p_n$ with the limit, using $\eps/2$.",
], ["c2-def-cauchy", "c2-def-convergence"])

s.e("c2-ex-incomplete", "Incomplete spaces", r"""
The converse can fail. In the subspace $(0,1] \subset \R$ the sequence $1/n$ is Cauchy (it converges in $\R$) but has no limit in $(0,1]$. In $\Q$, the decimal truncations $1, 1.4, 1.41, 1.414, \dots$ of $\sqrt2$ form a Cauchy sequence with no rational limit. Completeness is a property of the metric, not just of the open sets: we will meet a homeomorphism between $\R$, which is complete, and $(-1,1)$, which is not.
""")

s.t("lemma", "c2-lem-cauchy-subsequence", "A Cauchy sequence with a convergent subsequence converges", r"""
Let $(p_n)$ be a Cauchy sequence in a metric space $M$. If some subsequence $(p_{n_k})$ converges to $p \in M$, then $p_n \to p$.
""", r"""
Let $\eps > 0$. Choose $N$ with $d(p_m,p_n) < \eps/2$ for all $m, n \ge N$. Since $p_{n_k} \to p$ there is a $K$ with $d(p_{n_k},p) < \eps/2$ for $k \ge K$; fix one index $k \ge \max(K,N)$, so that also $n_k \ge k \ge N$. Then for every $n \ge N$,
\[ d(p_n,p) \le d(p_n, p_{n_k}) + d(p_{n_k}, p) < \frac{\eps}{2} + \frac{\eps}{2} = \eps . \]
""", 2, 15, [
    r"Far out, all terms are close to each other, and some of them (those of the subsequence) are close to $p$.",
], ["c2-def-cauchy", "c2-def-subsequence", "c2-def-convergence"])

s.t("theorem", "c2-thm-rm-complete", r"$\R^m$ is complete", r"""
Every Cauchy sequence in $\R^m$ converges. (You may use that $\R$ is complete, from Chapter 1.)
""", r"""
Let $(v_n)$ be a Cauchy sequence in $\R^m$, $v_n = (v_{n1}, \dots, v_{nm})$. For each $i$ and all $n, k$,
\[ \abs{v_{ni} - v_{ki}} \le \abs{v_n - v_k}, \]
since the square of the left side is one of the nonnegative terms whose sum is the square of the right side. Hence each component sequence $(v_{ni})_{n \in \N}$ is a Cauchy sequence in $\R$: the $N$ that works for $(v_n)$ and $\eps$ works for it. By the completeness of $\R$ it converges to some $a_i \in \R$. Put $a = (a_1, \dots, a_m)$. Since convergence in $\R^m$ is componentwise, $v_n \to a$.
""", 2, 15, [
    r"Look at one coordinate at a time.",
    r"Each coordinate sequence is Cauchy in $\R$ because $\abs{v_{ni} - v_{ki}} \le \abs{v_n - v_k}$; then reassemble.",
], ["c2-def-cauchy", "c2-cor-rm-convergence"])

s.t("theorem", "c2-thm-closed-complete", "Closed subsets and completeness", r"""
Let $S$ be a subset of a metric space $M$.
\begin{enumerate}
\item If $M$ is complete and $S$ is closed in $M$, then $S$ is complete.
\item If $S$ is complete, then $S$ is closed in $M$.
\end{enumerate}
In particular, a subset of $\R^m$ is complete if and only if it is closed.
""", r"""
(1) Let $(p_n)$ be a Cauchy sequence in the subspace $S$. The distances are those of $M$, so it is a Cauchy sequence in $M$ and converges in $M$ to some $p$. Then $p$ is a limit of $S$, and $p \in S$ because $S$ is closed. So $(p_n)$ converges in $S$.

(2) Let $p \in M$ be a limit of $S$, say $p_n \to p$ with $p_n \in S$. A convergent sequence is Cauchy, so $(p_n)$ is a Cauchy sequence in $S$, and since $S$ is complete it converges in $S$ to some $q \in S$. Then $p_n \to q$ in $M$ as well, and limits are unique, so $p = q \in S$. Hence $S$ is closed.

The last statement follows because $\R^m$ is complete.
""", 2, 20, [
    r"For (1), a Cauchy sequence in $S$ is a Cauchy sequence in $M$. Where does its limit live?",
    r"For (2), a sequence in $S$ converging in $M$ is Cauchy; use completeness of $S$ and uniqueness of limits.",
], ["c2-def-cauchy", "c2-prop-convergent-cauchy", "c2-thm-limit-unique", "c2-thm-rm-complete", "c2-def-closed-open"])

s.card("c2-card-metric", "State the three axioms of a metric $d$ on $M$.",
       r"Positive definiteness: $d(x,y) \ge 0$ with equality iff $x = y$. Symmetry: $d(x,y) = d(y,x)$. Triangle inequality: $d(x,z) \le d(x,y) + d(y,z)$.",
       "c2-def-metric-space")
s.card("c2-card-continuity-three", r"Give three equivalent conditions for $f : M \to N$ to be continuous.",
       r"Sequential: $p_n \to p$ implies $f(p_n) \to f(p)$. $\eps,\delta$: for each $p$ and $\eps$ there is $\delta$ with $d(x,p) < \delta \Rightarrow d(f(x),f(p)) < \eps$. Open set condition: preimages of open sets are open (equivalently, preimages of closed sets are closed).",
       "c2-thm-open-set-condition")
s.card("c2-card-closed-open", "Define closed set and open set in a metric space. How are they related?",
       r"$S$ is closed if it contains every limit of a sequence in $S$; $S$ is open if every $p \in S$ has some $M_r(p) \subset S$. $S$ is closed iff $S^c$ is open.",
       "c2-thm-open-closed-dual")
s.card("c2-card-topology", "Which unions and intersections of open sets are open? Of closed sets closed? Give a counterexample for the rest.",
       r"Open: arbitrary unions, finite intersections. Closed: arbitrary intersections, finite unions. $\bigcap_n (-1/n, 1/n) = \set{0}$ is not open.",
       "c2-cor-closed-sets")
s.card("c2-card-closure", r"Define $\overline{S}$, $\interior S$, $\partial S$. What is $\overline{S}$ in terms of sequences?",
       r"$\overline{S}$: intersection of all closed sets containing $S$; $\interior S$: union of all open sets inside $S$; $\partial S = \overline{S} \setminus \interior S$. $\overline{S} = \lim S$, the set of limits of sequences in $S$.",
       "c2-prop-closure-lim")
s.card("c2-card-homeo", "Define homeomorphism. Give a continuous bijection that is not one.",
       r"A bijection $f$ with $f$ and $f^{-1}$ both continuous. $x \mapsto (\cos x, \sin x)$ from $[0,2\pi)$ onto the circle is a continuous bijection whose inverse is discontinuous at $(1,0)$.",
       "c2-ex-circle")
s.card("c2-card-inheritance", r"State the inheritance principle for $S \subset N \subset M$.",
       r"$S$ is closed in $N$ iff $S = N \cap L$ with $L$ closed in $M$; $S$ is open in $N$ iff $S = N \cap U$ with $U$ open in $M$.",
       "c2-thm-inheritance")
s.card("c2-card-product", r"When does $(x_n,y_n) \to (x,y)$ in $X \times Y$? Why does the choice among $d_E$, $d_{\max}$, $d_{\mathrm{sum}}$ not matter?",
       r"Exactly when $x_n \to x$ and $y_n \to y$. Because $d_{\max} \le d_E \le d_{\mathrm{sum}} \le 2 d_{\max}$.",
       "c2-thm-product-convergence")
s.card("c2-card-complete", "Define Cauchy sequence and complete metric space. Which subsets of a complete space are complete?",
       r"Cauchy: for every $\eps$ there is $N$ with $d(p_m,p_n) < \eps$ for $m,n \ge N$. Complete: every Cauchy sequence converges in the space. In a complete space, the complete subsets are exactly the closed ones.",
       "c2-thm-closed-complete")
s.card("c2-card-lim-closed-idea", r"One-line idea: why is $\lim S$ closed?",
       r"Within $r/2$ of a limit of $\lim S$ there is a point of $\lim S$, and within $r/2$ of that a point of $S$; so every ball about it meets $S$.",
       "c2-thm-lim-closed")

s.write()
