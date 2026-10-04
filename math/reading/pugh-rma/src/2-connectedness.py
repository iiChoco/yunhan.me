from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c2lib import Section

s = Section("2-connectedness")

s.p("c2-con-intro", r"""
A space is connected if it is all in one piece. The precise version says that it cannot be split into two nonempty parts each of which is open. Connectedness is what lies behind the intermediate value theorem: a continuous function cannot tear a connected space apart, so it cannot jump over a value. In this section we prove that, identify the connected subsets of the line, and compare connectedness with the more hands-on notion of being joined by paths.
""")

s.d("c2-def-connected", "Connected and disconnected", r"""
A subset $A$ of a metric space $M$ is \emph{proper} if $A \ne \varnothing$ and $A \ne M$. A metric space $M$ is \emph{disconnected} if it has a proper clopen subset, and \emph{connected} otherwise. A subset $S \subset M$ is connected or disconnected according as the subspace $S$ is.

If $A$ is a proper clopen subset of $M$ then so is $A^c$, and $M = A \sqcup A^c$ is a \emph{separation} of $M$: a splitting into two disjoint nonempty open sets. Conversely, if $M = A \sqcup B$ with $A, B$ disjoint, nonempty and open, then $A = B^c$ is also closed, so $A$ is a proper clopen set.
""")

s.e("c2-ex-disconnected", "Some disconnected spaces", r"""
The subspace $[0,1] \cup [2,3]$ of $\R$ is disconnected: $[0,1]$ is its intersection with the open set $(-1, 3/2)$ and with the closed set $[0,1]$, so it is clopen in the subspace. The rationals are disconnected: $\Q \cap (-\infty, \sqrt2) = \Q \cap (-\infty, \sqrt2]$ is clopen in $\Q$. A discrete space with at least two points is disconnected, since every subset of it is clopen.
""")

s.t("theorem", "c2-thm-connected-image", "The continuous image of a connected space is connected", r"""
Let $f : M \to N$ be a continuous map of metric spaces. If $f$ is onto and $M$ is connected, then $N$ is connected. More generally, if $S \subset M$ is connected then $f(S)$ is a connected subset of $N$.
""", r"""
Suppose $f$ is onto and $A \subset N$ is clopen with $A \ne \varnothing$, $A \ne N$. By the open and closed set conditions for continuity, $f^{-1}(A)$ is both open and closed in $M$. Since $f$ is onto and $A$ is nonempty, $f^{-1}(A)$ is nonempty; since $A^c$ is nonempty, $f^{-1}(A^c) = M \setminus f^{-1}(A)$ is nonempty, so $f^{-1}(A) \ne M$. Thus $f^{-1}(A)$ is a proper clopen subset of $M$, and $M$ is disconnected. Contrapositively, if $M$ is connected then so is $N$.

For the general statement let $S \subset M$ be connected and consider $g : S \to f(S)$, $g(x) = f(x)$, where $S$ and $f(S)$ carry the inherited metrics. If $x_n \to x$ in $S$, then $x_n \to x$ in $M$, so $f(x_n) \to f(x)$ in $N$, and since these points lie in $f(S)$ this is convergence in the subspace $f(S)$. So $g$ is continuous, and it is onto. By the first part, $f(S)$ is connected.
""", 2, 20, [
    r"Pull a proper clopen subset of $N$ back to $M$.",
    r"Check that the preimage is clopen (open and closed set conditions) and proper (this is where onto is used).",
], ["c2-def-connected", "c2-thm-open-set-condition", "c2-def-continuity"])

s.t("corollary", "c2-cor-generalized-ivt", "Generalized intermediate value theorem", r"""
Let $M$ be a connected metric space and $f : M \to \R$ a continuous function. If $p, q \in M$ and $f(p) < c < f(q)$, then $f(x) = c$ for some $x \in M$.
""", r"""
Suppose $f$ never takes the value $c$. Then
\[ A = f^{-1}\big((-\infty, c)\big) = f^{-1}\big((-\infty, c]\big). \]
The interval $(-\infty,c)$ is open in $\R$: if $t < c$ then $(t - r, t + r) \subset (-\infty,c)$ for $r = c - t$. Likewise $(c,\infty)$ is open, so its complement $(-\infty,c]$ is closed. By the open and closed set conditions for continuity, the first description shows $A$ is open and the second shows $A$ is closed. Moreover $p \in A$ and $q \notin A$, so $A$ is a proper clopen subset of $M$, contradicting connectedness. Hence $f$ takes the value $c$.
""", 2, 20, [
    r"Suppose $c$ is not a value. Find a proper clopen subset of $M$.",
    r"The set where $f < c$ is the same as the set where $f \le c$.",
], ["c2-def-connected", "c2-thm-open-set-condition", "c2-thm-open-closed-dual"])

s.p("c2-con-line-prose", r"""
For this to be useful we need a supply of connected spaces. The fundamental one is the real line, and more generally any interval. This is where the least upper bound property enters. Call a set $I \subset \R$ an \emph{interval} if it contains every point between any two of its points: $x, z \in I$ and $x < y < z$ imply $y \in I$. This covers $(a,b)$, $[a,b]$, $[a,b)$, $(a,\infty)$, $\R$ itself, and so on.
""")

s.t("theorem", "c2-thm-intervals-connected", "Intervals are connected", r"""
Every interval $I \subset \R$ is connected. In particular $\R$, $(a,b)$ and $[a,b]$ are connected.
""", r"""
Suppose $I$ is disconnected: $I = A \sqcup B$ with $A$, $B$ disjoint, nonempty and clopen in $I$. Choose $p \in A$ and $q \in B$; exchanging the names of $A$ and $B$ if necessary, assume $p < q$. Since $I$ is an interval, $[p,q] \subset I$. Let
\[ X = \set{x \in [p,q] : [p,x] \subset A}. \]
Then $p \in X$ and $q$ is an upper bound of $X$, so $s = \lub X$ exists and $p \le s \le q$; in particular $s \in I$.

\emph{$s \in A$.} For each $n \in \N$, $s - 1/n$ is not an upper bound of $X$, so there is $x_n \in X$ with $s - 1/n < x_n \le s$. Each $x_n$ lies in $[p,x_n] \subset A$, and $x_n \to s$. So $s$ is a limit, in $I$, of the set $A$, and $s \in A$ because $A$ is closed in $I$.

\emph{$[p,s] \subset A$.} If $p \le y < s$, then $y$ is not an upper bound of $X$, so there is an $x \in X$ with $y < x$, and $y \in [p,x] \subset A$. Together with $s \in A$ this gives $[p,s] \subset A$.

\emph{Contradiction.} Since $s \in A$ and $q \in B$, $s \ne q$, so $s < q$. Since $A$ is open in $I$ there is an $r > 0$ such that every $x \in I$ with $\abs{x - s} < r$ lies in $A$. Put $t = \min(s + r/2,\, q)$. Then $s < t \le q$, and every $x \in [s,t]$ lies in $[p,q] \subset I$ and satisfies $\abs{x - s} < r$, so $[s,t] \subset A$. Hence $[p,t] = [p,s] \cup [s,t] \subset A$, that is, $t \in X$. But $t > s = \lub X$, a contradiction. Therefore $I$ is connected.
""", 4, 60, [
    r"Suppose $I = A \sqcup B$ is a separation, with $p \in A$, $q \in B$, $p < q$. Walk from $p$ towards $q$ and ask where you first leave $A$.",
    r"Let $s$ be the least upper bound of the $x \in [p,q]$ with $[p,x] \subset A$. Use that $A$ is closed in $I$ to place $s$.",
    r"Then use that $A$ is open in $I$ to step a little past $s$ while staying in $A$, contradicting the choice of $s$.",
], ["c2-def-connected", "c2-def-closed-open"])

s.t("corollary", "c2-cor-connected-subsets-of-r", "The connected subsets of the line", r"""
A subset $S \subset \R$ is connected if and only if it is an interval. Consequently (the intermediate value theorem) a continuous function $f : [a,b] \to \R$ takes every value between $f(a)$ and $f(b)$.
""", r"""
Intervals are connected by the previous theorem. Conversely suppose $S$ is not an interval: there are $x, z \in S$ and $y \notin S$ with $x < y < z$. Put $A = S \cap (-\infty, y)$. Since $y \notin S$ we also have $A = S \cap (-\infty, y]$. The ray $(-\infty,y)$ is open in $\R$ (if $t < y$ then $(t-r,t+r) \subset (-\infty,y)$ for $r = y - t$), and likewise $(y,\infty)$ is open, so its complement $(-\infty,y]$ is closed in $\R$. By the inheritance principle the first description shows $A$ is open in $S$ and the second shows $A$ is closed in $S$. Also $x \in A$ and $z \in S \setminus A$. So $A$ is a proper clopen subset of $S$, and $S$ is disconnected.

For the intermediate value theorem, let $c$ be a value between $f(a)$ and $f(b)$. If $c = f(a)$ or $c = f(b)$ it is taken at an endpoint. Otherwise $c$ lies strictly between $f(a)$ and $f(b)$; since $[a,b]$ is an interval it is connected, so the generalized intermediate value theorem applies (with $p = a$, $q = b$ if $f(a) < c < f(b)$, and with $p = b$, $q = a$ if $f(b) < c < f(a)$) and gives an $x \in [a,b]$ with $f(x) = c$.
""", 2, 20, [
    r"If $S$ misses a point $y$ between two of its points, cut $S$ at $y$.",
    r"$S \cap (-\infty,y) = S \cap (-\infty,y]$ is clopen in $S$ by the inheritance principle.",
], ["c2-thm-intervals-connected", "c2-thm-inheritance", "c2-cor-generalized-ivt", "c2-thm-open-closed-dual"])

s.r("c2-rem-topological-invariant", r"""
Connectedness is a topological property, since a homeomorphism and its inverse are continuous and onto. This gives a way to tell spaces apart. For instance $[0,1)$ is not homeomorphic to $(0,1)$: removing the point $0$ from $[0,1)$ leaves a connected set, whereas removing any point from $(0,1)$ leaves a disconnected one, and a homeomorphism $h : [0,1) \to (0,1)$ would restrict to a homeomorphism from $(0,1)$ onto $(0,1) \setminus \set{h(0)}$.
""")

s.t("theorem", "c2-thm-closure-connected", "The closure of a connected set is connected", r"""
Let $S$ be a connected subset of a metric space $M$ and let $S \subset T \subset \overline{S}$. Then $T$ is connected. In particular $\overline{S}$ is connected.
""", r"""
Suppose $A$ is a proper clopen subset of the subspace $T$. Its complement $B = T \setminus A$ is then also a proper clopen subset of $T$.

By the inheritance principle $A = T \cap U$ and $A = T \cap L$ for some open $U \subset M$ and closed $L \subset M$. Then $A \cap S = S \cap U = S \cap L$, so $A \cap S$ is clopen in $S$, again by the inheritance principle. Since $S$ is connected, $A \cap S = \varnothing$ or $A \cap S = S$. In the second case $B \cap S = \varnothing$. So, replacing $A$ by $B$ if necessary, we may assume that $A$ is a proper clopen subset of $T$ with $A \cap S = \varnothing$.

Since $A \ne \varnothing$ pick $a \in A$. As $A$ is open in $T$, the inheritance principle gives an open set $U \subset M$ with $A = T \cap U$. There is an $r > 0$ with $M_r(a) \subset U$. Now $a \in T \subset \overline{S} = \lim S$, so $a$ is a limit of $S$, and by the lemma on limits and neighborhoods $M_r(a)$ contains a point $x \in S$. Then $x \in S \subset T$ and $x \in U$, so $x \in T \cap U = A$. This contradicts $A \cap S = \varnothing$. Hence $T$ has no proper clopen subset.
""", 3, 40, [
    r"Suppose $A$ is a proper clopen subset of $T$. What can $A \cap S$ be?",
    r"By the inheritance principle $A \cap S$ is clopen in $S$, so it is empty or all of $S$; pass to the complement if needed so that $A$ misses $S$.",
    r"$A$ is nonempty and open in $T$, and each of its points is a limit of $S$. Find a point of $S$ in $A$.",
], ["c2-def-connected", "c2-thm-inheritance", "c2-prop-closure-lim", "c2-lem-limit-ball"])

s.t("theorem", "c2-thm-union-connected", "A union of connected sets with a common point is connected", r"""
Let $\set{S_\alpha}$ be a nonempty collection of connected subsets of a metric space $M$, and suppose there is a point $p$ belonging to every $S_\alpha$. Then $S = \bigcup_\alpha S_\alpha$ is connected.
""", r"""
Let $A$ be a nonempty clopen subset of the subspace $S$; we show $A = S$, so that $S$ has no proper clopen subset. Suppose first that $p \in A$. For each $\alpha$, the set $A \cap S_\alpha$ is clopen in $S_\alpha$: by the inheritance principle $A = S \cap U = S \cap L$ with $U$ open and $L$ closed in $M$, so $A \cap S_\alpha = S_\alpha \cap U = S_\alpha \cap L$ is open and closed in $S_\alpha$. It contains $p$, so it is nonempty, and since $S_\alpha$ is connected, $A \cap S_\alpha = S_\alpha$. Thus $S_\alpha \subset A$ for every $\alpha$, and $A = S$.

If instead $p \notin A$, then $S \setminus A$ is a clopen subset of $S$ containing $p$, so by what was just shown $S \setminus A = S$, i.e. $A = \varnothing$, contrary to assumption. Hence every nonempty clopen subset of $S$ is $S$ itself.
""", 3, 30, [
    r"Take a clopen subset $A$ of the union containing $p$ and intersect it with each $S_\alpha$.",
    r"$A \cap S_\alpha$ is clopen in $S_\alpha$ (inheritance) and contains $p$.",
], ["c2-def-connected", "c2-thm-inheritance"])

s.d("c2-def-path-connected", "Path, path-connected", r"""
A \emph{path} in a metric space $M$ from $p$ to $q$ is a continuous map $f : [a,b] \to M$ with $f(a) = p$ and $f(b) = q$. $M$ is \emph{path-connected} if every two of its points are joined by a path in $M$. A subset is path-connected if it is so as a subspace.
""")

s.t("theorem", "c2-thm-path-connected", "Path-connected spaces are connected", r"""
Every path-connected metric space is connected.
""", r"""
Let $M$ be path-connected. If $M$ is empty it has no proper subset and is connected. Otherwise fix $p \in M$. For each $q \in M$ choose a path $f_q : [a_q,b_q] \to M$ from $p$ to $q$ and let $S_q = f_q([a_q,b_q])$ be its image. The interval $[a_q,b_q]$ is connected, and the continuous image of a connected set is connected, so $S_q$ is a connected subset of $M$. Every $S_q$ contains $p$, and $q \in S_q$, so $M = \bigcup_{q \in M} S_q$ is a union of connected sets with a common point. Hence $M$ is connected.
""", 2, 20, [
    r"The image of a path is connected. Why?",
    r"Fix a base point $p$ and write $M$ as a union of images of paths starting at $p$.",
], ["c2-def-path-connected", "c2-thm-intervals-connected", "c2-thm-connected-image", "c2-thm-union-connected"])

s.t("corollary", "c2-cor-convex-connected", "Convex sets are connected", r"""
A set $S \subset \R^m$ is \emph{convex} if $(1-t)p + tq \in S$ whenever $p, q \in S$ and $0 \le t \le 1$. Every convex subset of $\R^m$ is path-connected, hence connected. In particular $\R^m$ and every ball $\set{x : \abs{x - c} < r}$ in $\R^m$ are connected.
""", r"""
Let $S$ be convex and $p, q \in S$. Define $f : [0,1] \to S$ by $f(t) = (1-t)p + tq = p + t(q-p)$; it takes values in $S$ by convexity, $f(0) = p$ and $f(1) = q$. For $t, u \in [0,1]$,
\[ \abs{f(t) - f(u)} = \abs{(t-u)(q-p)} = \abs{t-u}\,\abs{q-p}, \]
so if $t_n \to t$ then $\abs{f(t_n) - f(t)} = \abs{t_n - t}\abs{q-p} \to 0$, and $f$ is continuous. Thus $f$ is a path in $S$ from $p$ to $q$, $S$ is path-connected, and path-connected spaces are connected.

$\R^m$ is plainly convex. For the ball $B = \set{x : \abs{x-c} < r}$, let $p, q \in B$ and $0 \le t \le 1$. Then
\[ \abs{(1-t)p + tq - c} = \abs{(1-t)(p-c) + t(q-c)} \le (1-t)\abs{p-c} + t\abs{q-c} < (1-t) r + t r = r , \]
where the strict inequality holds because $\abs{p-c} < r$, $\abs{q-c} < r$, and $1-t$, $t$ are nonnegative and not both zero. So $B$ is convex.
""", 2, 20, [
    r"The straight-line path $t \mapsto (1-t)p + tq$ is continuous: compute $\abs{f(t) - f(u)}$.",
], ["c2-thm-path-connected", "c2-def-path-connected", "c2-def-continuity"])

s.e("c2-ex-topologists-sine-curve", "The topologist's sine curve: connected, not path-connected", r"""
The converse of the last theorem is false. Let
\[ G = \set{(x, \sin(1/x)) : 0 < x \le 1}, \qquad Y = \set{(0,y) : -1 \le y \le 1}, \qquad M = G \cup Y \subset \R^2 . \]
(We use freely that $\sin$ is continuous and takes the values $\pm 1$ at $\pi/2 + k\pi$.)

\emph{$M$ is connected.} $G$ is the image of the interval $(0,1]$ under the continuous map $x \mapsto (x, \sin(1/x))$, so it is connected. Every point $(0,y)$ of $Y$ is a limit of $G$: choose $\theta$ with $\sin\theta = y$; for $n$ large the numbers $x_n = 1/(\theta + 2\pi n)$ lie in $(0,1]$, they tend to $0$, and $(x_n, \sin(1/x_n)) = (x_n, y) \to (0,y)$. So $G \subset M \subset \overline{G}$, and $M$ is connected by the theorem on the closure of a connected set.

\emph{$M$ is not path-connected.} Suppose $f = (f_1, f_2) : [a,b] \to M$ is a path from $(0,0)$ to a point of $G$. The coordinate functions $f_1, f_2$ are continuous. Let $t_0 = \lub \set{t \in [a,b] : f_1(t) = 0}$. By continuity $f_1(t_0) = 0$, and $t_0 < b$ since $f_1(b) > 0$; also $f_1(t) > 0$ for $t > t_0$. By continuity of $f_2$ at $t_0$ there is a $\delta > 0$ with $t_0 + \delta \le b$ and $\abs{f_2(t) - f_2(t_0)} < 1/2$ for $t \in [t_0, t_0 + \delta]$. But $f_1$ is continuous on $[t_0, t_0+\delta]$ with $f_1(t_0) = 0 < f_1(t_0+\delta) = \eta$, so by the intermediate value theorem it takes every value in $(0,\eta)$ there. Among those values are numbers of the form $x = 1/(\pi/2 + 2\pi n)$ and $x' = 1/(3\pi/2 + 2\pi n)$ for large $n$, at which $\sin(1/x) = 1$ and $\sin(1/x') = -1$. So $f_2$ takes both values $1$ and $-1$ on $[t_0,t_0+\delta]$, which is impossible for a function staying within $1/2$ of $f_2(t_0)$. Hence no such path exists.
""")

s.card("c2-card-connected", "Define connected metric space.",
       r"$M$ is connected if it has no proper clopen subset, i.e. it cannot be written as a disjoint union of two nonempty open sets.",
       "c2-def-connected")
s.card("c2-card-connected-image", "What do continuous maps do to connected sets? State the generalized intermediate value theorem.",
       r"The continuous image of a connected set is connected. If $M$ is connected, $f : M \to \R$ is continuous and $f(p) < c < f(q)$, then $f(x) = c$ for some $x$.",
       "c2-cor-generalized-ivt")
s.card("c2-card-intervals", r"Which subsets of $\R$ are connected? One-line idea of the proof that an interval is connected.",
       r"Exactly the intervals. Given a separation $A \sqcup B$ with $p \in A$, $q \in B$, $p < q$, let $s = \lub\set{x : [p,x] \subset A}$; closedness of $A$ puts $s$ in $A$, openness lets you step past $s$: contradiction.",
       "c2-cor-connected-subsets-of-r")
s.card("c2-card-closure-union", "Two ways to build connected sets from connected sets.",
       r"If $S$ is connected and $S \subset T \subset \overline{S}$ then $T$ is connected. A union of connected sets that share a common point is connected.",
       "c2-thm-union-connected")
s.card("c2-card-path", "Define path-connected. How does it relate to connected? Give the standard counterexample.",
       r"Any two points are joined by a continuous $f : [a,b] \to M$. Path-connected implies connected; the topologist's sine curve $\set{(x,\sin(1/x)) : 0 < x \le 1} \cup (\set{0} \times [-1,1])$ is connected and not path-connected.",
       "c2-ex-topologists-sine-curve")
s.card("c2-card-not-homeo", r"Why is $[0,1)$ not homeomorphic to $(0,1)$?",
       r"Connectedness is topological. Removing $0$ from $[0,1)$ leaves a connected set; removing any point from $(0,1)$ disconnects it.",
       "c2-rem-topological-invariant")

s.write()
