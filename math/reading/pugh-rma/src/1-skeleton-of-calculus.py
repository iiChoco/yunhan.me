from __future__ import annotations
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from c1_common import Section

s = Section("1-skeleton-of-calculus")

s.prose("skel-intro", r"""
Calculus rests on three facts about a continuous function on a closed bounded interval: it is bounded, it attains a largest and a smallest value, and it takes every value in between. None of them is a fact about formulas; each is a consequence of the completeness of $\R$. This section proves all three directly from the least upper bound property, by one and the same method: push a good property from the left endpoint as far to the right as it will go, and show that it goes all the way.
""")

s.definition("def-continuity", "Continuity", r"""
Let $D \subset \R$ and $f \colon D \to \R$. The function $f$ is \emph{continuous at} a point $c \in D$ if for every $\eps > 0$ there is a $\delta > 0$ such that
\[ x \in D \text{ and } \abs{x - c} < \delta \quad\Longrightarrow\quad \abs{f(x) - f(c)} < \eps. \]
It is \emph{continuous} (on $D$) if it is continuous at every point of $D$. If $f$ is continuous on $D$ and $D' \subset D$, then the restriction of $f$ to $D'$ is continuous on $D'$, since the same $\delta$ serves.
""")

s.result("ex-basic-continuous", "exercise", "First continuous functions", r"""
Prove from the definition that the following functions $\R \to \R$ are continuous: a constant function $x \mapsto k$; the identity $x \mapsto x$; the absolute value $x \mapsto \abs{x}$.
""", r"""
Let $c \in \R$ and $\eps > 0$.

\emph{Constant.} For every $x$, $\abs{k - k} = 0 < \eps$; any $\delta > 0$ works.

\emph{Identity.} Take $\delta = \eps$: if $\abs{x - c} < \delta$ then $\abs{x - c} < \eps$.

\emph{Absolute value.} Take $\delta = \eps$: if $\abs{x - c} < \delta$ then, by the inequality $\big|\abs{x} - \abs{c}\big| \le \abs{x - c}$, we get $\big|\abs{x} - \abs{c}\big| < \eps$.
""", 1, 10, [
    r"In each case say explicitly which $\delta$ answers a given $\eps$.",
    r"For the absolute value use $\big|\abs{x} - \abs{c}\big| \le \abs{x - c}$.",
], ["def-continuity", "prop-triangle-inequality"])

s.result("prop-continuity-algebra", "proposition", "Sums and products of continuous functions", r"""
Let $D \subset \R$, let $f, g \colon D \to \R$ be continuous at $c \in D$, and let $k \in \R$. Then $f + g$, $kf$, and $fg$ are continuous at $c$.
""", r"""
Let $\eps > 0$.

\emph{Sum.} Choose $\delta_1, \delta_2 > 0$ such that for $x \in D$: $\abs{x - c} < \delta_1$ implies $\abs{f(x) - f(c)} < \eps/2$, and $\abs{x - c} < \delta_2$ implies $\abs{g(x) - g(c)} < \eps/2$. Let $\delta = \min(\delta_1, \delta_2)$. For $x \in D$ with $\abs{x - c} < \delta$,
\[ \abs{(f + g)(x) - (f + g)(c)} \le \abs{f(x) - f(c)} + \abs{g(x) - g(c)} < \eps. \]

\emph{Product.} For $x \in D$,
\[ f(x)g(x) - f(c)g(c) = f(x)\big(g(x) - g(c)\big) + g(c)\big(f(x) - f(c)\big). \]
Choose $\delta_1 > 0$ such that $\abs{x - c} < \delta_1$ implies $\abs{f(x) - f(c)} < 1$, hence $\abs{f(x)} < \abs{f(c)} + 1$. Choose $\delta_2 > 0$ such that $\abs{x - c} < \delta_2$ implies $\abs{g(x) - g(c)} < \dfrac{\eps}{2(\abs{f(c)} + 1)}$, and $\delta_3 > 0$ such that $\abs{x - c} < \delta_3$ implies $\abs{f(x) - f(c)} < \dfrac{\eps}{2(\abs{g(c)} + 1)}$ (all for $x \in D$). Let $\delta = \min(\delta_1, \delta_2, \delta_3)$. For $x \in D$ with $\abs{x - c} < \delta$,
\[ \abs{f(x)g(x) - f(c)g(c)} \le \abs{f(x)}\abs{g(x) - g(c)} + \abs{g(c)}\abs{f(x) - f(c)} < \frac{\eps}{2} + \frac{\abs{g(c)}}{\abs{g(c)} + 1} \cdot \frac{\eps}{2} \le \eps. \]

\emph{Constant multiple.} The constant function $x \mapsto k$ is continuous, so $kf$ is continuous at $c$ as a product of two functions continuous at $c$.
""", 3, 30, [
    r"For the sum, split $\eps$ in two and take the smaller $\delta$.",
    r"For the product, write $f(x)g(x) - f(c)g(c) = f(x)(g(x) - g(c)) + g(c)(f(x) - f(c))$. The factor $f(x)$ varies with $x$, so first make it bounded near $c$.",
], ["def-continuity", "prop-triangle-inequality", "ex-basic-continuous"])

s.result("cor-polynomials", "corollary", "Polynomials are continuous", r"""
Every polynomial function $p(x) = a_0 + a_1 x + \dots + a_n x^n$ (with $a_0, \dots, a_n \in \R$) is continuous on $\R$.
""", r"""
First, $x \mapsto x^k$ is continuous for every $k \in \N$, by induction: for $k = 1$ it is the identity, and $x^{k+1} = x^k \cdot x$ is a product of continuous functions. Hence each $x \mapsto a_k x^k$ is continuous, as a constant multiple of a continuous function, and $x \mapsto a_0$ is continuous as a constant.

Now induct on $n$. For $n = 0$, $p$ is constant. If the statement holds for $n - 1$, then $p(x) = \big(a_0 + \dots + a_{n-1}x^{n-1}\big) + a_n x^n$ is a sum of two continuous functions, hence continuous.
""", 1, 10, [
    r"Build $p$ from constants and the identity using sums and products, by induction.",
], ["prop-continuity-algebra", "ex-basic-continuous"])

s.result("lem-local-sign", "lemma", "A strict inequality at a point persists nearby", r"""
Let $D \subset \R$, let $f \colon D \to \R$ be continuous at $c \in D$, and let $\gamma \in \R$.
\begin{enumerate}
\item If $f(c) > \gamma$, there is a $\delta > 0$ such that $f(x) > \gamma$ for all $x \in D$ with $\abs{x - c} < \delta$.
\item If $f(c) < \gamma$, there is a $\delta > 0$ such that $f(x) < \gamma$ for all $x \in D$ with $\abs{x - c} < \delta$.
\end{enumerate}
""", r"""
(1) Let $\eps = f(c) - \gamma > 0$ and take $\delta > 0$ from the definition of continuity at $c$. If $x \in D$ and $\abs{x - c} < \delta$, then $\abs{f(x) - f(c)} < \eps$, so $f(x) > f(c) - \eps = \gamma$.

(2) Let $\eps = \gamma - f(c) > 0$ and take the corresponding $\delta$. If $x \in D$ and $\abs{x - c} < \delta$, then $f(x) < f(c) + \eps = \gamma$.
""", 1, 10, [
    r"Apply the definition of continuity with $\eps$ equal to the gap between $f(c)$ and $\gamma$.",
], ["def-continuity", "prop-triangle-inequality"])

s.result("thm-bounded", "theorem", "A continuous function on a closed interval is bounded", r"""
Let $a \le b$ and let $f \colon [a, b] \to \R$ be continuous. Then there is a $K \in \R$ with $\abs{f(x)} \le K$ for all $x \in [a, b]$.
""", r"""
Say that $f$ is \emph{bounded on} a set $E \subset [a, b]$ if there is a $K$ with $\abs{f(t)} \le K$ for all $t \in E$. Let
\[ X = \set{x \in [a, b] : f \text{ is bounded on } [a, x]}. \]
Then $a \in X$ (take $K = \abs{f(a)}$), and $b$ is an upper bound for $X$. By the least upper bound property $c = \lub X$ exists, and $a \le c \le b$.

By continuity at $c$ with $\eps = 1$, there is a $\delta > 0$ such that $\abs{f(t) - f(c)} < 1$, and hence $\abs{f(t)} < \abs{f(c)} + 1$, for all $t \in [a, b]$ with $\abs{t - c} < \delta$.

Since $c - \delta < c$, the number $c - \delta$ is not an upper bound for $X$: there is an $x_0 \in X$ with $c - \delta < x_0 \le c$. Let $K_0$ be a bound for $\abs{f}$ on $[a, x_0]$.

Let $t_1 = \min(b, c + \delta/2)$; then $c \le t_1 \le b$. We claim $t_1 \in X$. Let $t \in [a, t_1]$. If $t \le x_0$ then $\abs{f(t)} \le K_0$. If $t > x_0$ then $c - \delta < x_0 < t \le t_1 < c + \delta$, so $\abs{t - c} < \delta$ and $\abs{f(t)} < \abs{f(c)} + 1$. Thus $\abs{f}$ is bounded on $[a, t_1]$ by $\max(K_0, \abs{f(c)} + 1)$, and $t_1 \in X$.

Since $c$ is an upper bound for $X$, $t_1 \le c$, that is, $\min(b, c + \delta/2) \le c$. As $c + \delta/2 > c$, this forces $b \le c$; hence $c = b$ and $t_1 = b$. So $b \in X$, which says that $f$ is bounded on $[a, b]$.
""", 4, 60, [
    r"Consider how far to the right boundedness extends: let $X$ be the set of $x \in [a, b]$ such that $f$ is bounded on $[a, x]$, and let $c = \lub X$.",
    r"Continuity at $c$ makes $f$ bounded on a small interval around $c$. Some point of $X$ lies inside that small interval, to the left of $c$ or at $c$.",
    r"Glue the two bounds to show that $f$ is bounded on $[a, t]$ for $t = \min(b, c + \delta/2)$. Since no point of $X$ exceeds $c$, conclude $c = b$ and $b \in X$.",
], ["thm-lub", "def-continuity", "prop-triangle-inequality"])

s.result("thm-extreme-value", "theorem", "Extreme value theorem", r"""
Let $a \le b$ and let $f \colon [a, b] \to \R$ be continuous. Then there are points $x_1, x_2 \in [a, b]$ with
\[ f(x_2) \le f(x) \le f(x_1) \quad\text{for all } x \in [a, b]. \]
That is, $f$ attains a maximum value and a minimum value.
""", r"""
\emph{Maximum.} The set $f([a, b])$ is nonempty and, because a continuous function on a closed interval is bounded, bounded above. Let $M = \lub f([a, b])$. Suppose, for contradiction, that $f(x) < M$ for every $x \in [a, b]$. Let
\[ X = \set{x \in [a, b] : \text{there is } M' < M \text{ with } f(t) \le M' \text{ for all } t \in [a, x]}. \]
Then $a \in X$ (take $M' = f(a)$) and $b$ is an upper bound for $X$, so $c = \lub X$ exists and $a \le c \le b$.

Put $M_1 = (f(c) + M)/2$, so that $f(c) < M_1 < M$. By the lemma on strict inequalities, there is a $\delta > 0$ such that $f(t) < M_1$ for all $t \in [a, b]$ with $\abs{t - c} < \delta$. Since $c - \delta$ is not an upper bound for $X$, there is an $x_0 \in X$ with $c - \delta < x_0 \le c$; let $M_0 < M$ satisfy $f(t) \le M_0$ for $t \in [a, x_0]$.

Let $t_1 = \min(b, c + \delta/2)$, so $c \le t_1 \le b$. For $t \in [a, t_1]$: if $t \le x_0$ then $f(t) \le M_0$; if $t > x_0$ then $c - \delta < t < c + \delta$, so $f(t) < M_1$. Hence $f(t) \le \max(M_0, M_1) < M$ on $[a, t_1]$, and $t_1 \in X$. Since $c$ is an upper bound for $X$, $t_1 \le c$; as $c + \delta/2 > c$ this forces $b \le c$, so $c = b$ and $t_1 = b \in X$.

Thus there is an $M' < M$ with $f(t) \le M'$ for all $t \in [a, b]$. Then $M'$ is an upper bound for $f([a, b])$ smaller than its least upper bound $M$, a contradiction. Therefore $f(x_1) \ge M$ for some $x_1 \in [a, b]$; since $M$ is an upper bound for the values of $f$, $f(x_1) = M$ and $f(x) \le f(x_1)$ for all $x$.

\emph{Minimum.} The function $-f$ is continuous on $[a, b]$ (a constant multiple of $f$), so by the first part there is an $x_2$ with $-f(x) \le -f(x_2)$, that is, $f(x) \ge f(x_2)$, for all $x \in [a, b]$.
""", 4, 75, [
    r"Let $M = \lub f([a, b])$, which exists by the boundedness theorem. You must show $M$ is a value of $f$. Suppose it is not.",
    r"Run the same sweep as in the boundedness theorem: let $X$ be the set of $x$ such that $f$ stays below some $M' < M$ on all of $[a, x]$, and let $c = \lub X$.",
    r"Since $f(c) < M$, $f$ stays below $(f(c) + M)/2 < M$ near $c$. Conclude that $b \in X$, so $f \le M' < M$ on $[a, b]$, contradicting the definition of $M$.",
], ["thm-lub", "thm-bounded", "lem-local-sign", "prop-continuity-algebra", "def-continuity"])

s.example("ex-hypotheses-needed", r"""
Each hypothesis matters. On the interval $(0, 1]$, which is not closed, $x \mapsto 1/x$ is continuous and unbounded. On $(0, 1)$ the identity is bounded and continuous and has neither a maximum nor a minimum: its values have least upper bound $1$ and greatest lower bound $0$, and neither is attained. On $[0, 1]$ the discontinuous function with $f(x) = x$ for $x < 1$ and $f(1) = 0$ has no maximum.
""", "Why closed, why continuous")

s.result("thm-ivt", "theorem", "Intermediate value theorem", r"""
Let $a < b$, let $f \colon [a, b] \to \R$ be continuous, and let $\gamma$ be a real number strictly between $f(a)$ and $f(b)$ (that is, $f(a) < \gamma < f(b)$ or $f(b) < \gamma < f(a)$). Then there is a $c \in (a, b)$ with $f(c) = \gamma$.
""", r"""
\emph{Case $f(a) < \gamma < f(b)$.} Let
\[ S = \set{x \in [a, b] : f(x) < \gamma}. \]
Then $a \in S$ and $b$ is an upper bound for $S$, so $c = \lub S$ exists and $a \le c \le b$. We rule out $f(c) < \gamma$ and $f(c) > \gamma$.

Suppose $f(c) < \gamma$. Then $c \ne b$ because $f(b) > \gamma$, so $c < b$. By the lemma on strict inequalities there is a $\delta > 0$ such that $f(t) < \gamma$ for all $t \in [a, b]$ with $\abs{t - c} < \delta$. Let $t_1 = \min(b, c + \delta/2)$. Then $t_1 \in [a, b]$, $c < t_1$, and $\abs{t_1 - c} < \delta$, so $f(t_1) < \gamma$ and $t_1 \in S$. This contradicts the fact that $c$ is an upper bound for $S$.

Suppose $f(c) > \gamma$. By the same lemma there is a $\delta > 0$ such that $f(t) > \gamma$ for all $t \in [a, b]$ with $\abs{t - c} < \delta$. Since $c - \delta$ is not an upper bound for $S$, there is an $x \in S$ with $c - \delta < x \le c$. Then $\abs{x - c} < \delta$, so $f(x) > \gamma$, contradicting $x \in S$.

Hence $f(c) = \gamma$. Since $f(a) \ne \gamma$ and $f(b) \ne \gamma$, $c$ is neither $a$ nor $b$, so $c \in (a, b)$.

\emph{Case $f(b) < \gamma < f(a)$.} The function $-f$ is continuous on $[a, b]$ and $(-f)(a) < -\gamma < (-f)(b)$. By the first case there is a $c \in (a, b)$ with $-f(c) = -\gamma$, that is, $f(c) = \gamma$.
""", 3, 45, [
    r"Assume $f(a) < \gamma < f(b)$. Look for the last place where $f$ is below $\gamma$: a least upper bound of a suitable set.",
    r"Let $S = \set{x \in [a, b] : f(x) < \gamma}$ and $c = \lub S$. Show that $f(c) < \gamma$ and $f(c) > \gamma$ are both impossible.",
    r"If $f(c) < \gamma$, then $f < \gamma$ slightly to the right of $c$, so $c$ is not an upper bound of $S$. If $f(c) > \gamma$, then $f > \gamma$ slightly to the left of $c$, where $S$ has points.",
], ["thm-lub", "lem-local-sign", "prop-continuity-algebra", "def-continuity"])

s.result("cor-range-interval", "corollary", "The range of a continuous function on a closed interval", r"""
Let $a \le b$ and let $f \colon [a, b] \to \R$ be continuous, with minimum value $m$ and maximum value $M$. Then $f([a, b]) = [m, M]$.
""", r"""
By the extreme value theorem there are $x_1, x_2 \in [a, b]$ with $f(x_2) = m$, $f(x_1) = M$, and $m \le f(x) \le M$ for all $x$; so $f([a, b]) \subset [m, M]$ and $m, M \in f([a, b])$.

Let $m < \gamma < M$. Then $x_1 \ne x_2$. Let $I$ be the closed interval with endpoints $x_1$ and $x_2$; it is contained in $[a, b]$, and the restriction of $f$ to $I$ is continuous. The values of $f$ at the endpoints of $I$ are $m$ and $M$, and $\gamma$ lies strictly between them, so by the intermediate value theorem there is a $c \in I$ with $f(c) = \gamma$. Hence $[m, M] \subset f([a, b])$.
""", 2, 15, [
    r"One inclusion is the extreme value theorem. For the other, apply the intermediate value theorem on the interval between a point where the minimum is attained and a point where the maximum is attained.",
], ["thm-extreme-value", "thm-ivt"])

s.result("ex-fixed-point", "exercise", "A fixed point", r"""
Let $a < b$ and let $f \colon [a, b] \to [a, b]$ be continuous. Prove that $f(x) = x$ for some $x \in [a, b]$.
""", r"""
Let $g(x) = f(x) - x$ for $x \in [a, b]$. Then $g$ is continuous, being the sum of $f$ and a constant multiple of the identity. Since $f$ takes values in $[a, b]$,
\[ g(a) = f(a) - a \ge 0, \qquad g(b) = f(b) - b \le 0. \]
If $g(a) = 0$ then $f(a) = a$; if $g(b) = 0$ then $f(b) = b$. Otherwise $g(b) < 0 < g(a)$, and by the intermediate value theorem there is a $c \in (a, b)$ with $g(c) = 0$, that is, $f(c) = c$.
""", 2, 20, [
    r"A fixed point of $f$ is a zero of $g(x) = f(x) - x$.",
    r"Compare the signs of $g$ at the two endpoints, treating separately the case where $g$ vanishes at an endpoint.",
], ["thm-ivt", "prop-continuity-algebra", "ex-basic-continuous"])

s.result("ex-nth-roots", "exercise", "Existence of n-th roots", r"""
Let $c > 0$ be real and $n \in \N$. Prove that there is exactly one real number $y > 0$ with $y^n = c$.
""", r"""
\emph{Uniqueness.} If $0 < y_1 < y_2$ then $y_1^n < y_2^n$, by induction on $n$: it holds for $n = 1$, and if $y_1^n < y_2^n$ then $y_1^{n+1} = y_1^n y_1 < y_2^n y_1 < y_2^n y_2 = y_2^{n+1}$. So two different positive numbers have different $n$th powers.

\emph{Existence.} The function $f(x) = x^n$ is a polynomial, so it is continuous on $[0, c + 1]$. We have $f(0) = 0 < c$. Also $(c + 1)^n \ge c + 1$ by induction on $n$ (if $(c + 1)^n \ge c + 1$, then $(c + 1)^{n+1} \ge (c + 1)^2 \ge c + 1$, because $c + 1 \ge 1$), so $f(c + 1) \ge c + 1 > c$. By the intermediate value theorem there is a $y \in (0, c + 1)$ with $y^n = c$.
""", 2, 20, [
    r"Apply the intermediate value theorem to $x \mapsto x^n$ on an interval $[0, B]$ with $B^n > c$.",
    r"$B = c + 1$ works, since $(c + 1)^n \ge c + 1$. Uniqueness comes from $x^n$ being strictly increasing on positive numbers.",
], ["thm-ivt", "cor-polynomials"])

s.remark("skel-outro", r"""
All three theorems fail over $\Q$: on the rational points of $[0, 2]$ the function $x^2 - 2$ is continuous, negative at $0$ and positive at $2$, and never zero. So their proofs \emph{must} use completeness, and each of the proofs above uses it in the same place, to produce the point $c$. In the next chapter the same theorems reappear as statements about compact and connected sets.
""")

s.card("continuity", r"Define: $f \colon D \to \R$ is continuous at $c \in D$.",
       r"For every $\eps > 0$ there is a $\delta > 0$ such that $x \in D$ and $\abs{x - c} < \delta$ imply $\abs{f(x) - f(c)} < \eps$.", "def-continuity")
s.card("product-continuous", r"What identity drives the proof that a product of continuous functions is continuous?",
       r"$f(x)g(x) - f(c)g(c) = f(x)(g(x) - g(c)) + g(c)(f(x) - f(c))$, after first bounding $\abs{f(x)}$ by $\abs{f(c)} + 1$ near $c$.", "prop-continuity-algebra")
s.card("bounded", r"State the boundedness theorem and the set used in its proof.",
       r"A continuous $f \colon [a, b] \to \R$ is bounded. Let $X = \set{x \in [a, b] : f \text{ is bounded on } [a, x]}$ and $c = \lub X$; continuity at $c$ shows $c = b$ and $b \in X$.", "thm-bounded")
s.card("extreme-value", r"State the extreme value theorem.",
       r"A continuous $f \colon [a, b] \to \R$ attains a maximum and a minimum: there are $x_1, x_2 \in [a, b]$ with $f(x_2) \le f(x) \le f(x_1)$ for all $x$.", "thm-extreme-value")
s.card("ivt", r"State the intermediate value theorem and the idea of its proof.",
       r"If $f$ is continuous on $[a, b]$ and $\gamma$ is strictly between $f(a)$ and $f(b)$, then $f(c) = \gamma$ for some $c \in (a, b)$. For $f(a) < \gamma < f(b)$ take $c = \lub\set{x : f(x) < \gamma}$; both $f(c) < \gamma$ and $f(c) > \gamma$ contradict the choice of $c$.", "thm-ivt")
s.card("counterexamples", r"Give a continuous unbounded function on $(0, 1]$, and a bounded continuous function on $(0, 1)$ with no maximum.",
       r"$1/x$ on $(0, 1]$; the identity $x$ on $(0, 1)$.")
s.card("range", r"What is the range of a continuous function on $[a, b]$?",
       r"The closed interval $[m, M]$ between its minimum and maximum values.", "cor-range-interval")
s.card("ivt-over-q", r"Why must the proof of the intermediate value theorem use completeness?",
       r"Over $\Q$ it is false: $x^2 - 2$ changes sign on the rationals of $[0, 2]$ and has no rational zero.")

s.write()
