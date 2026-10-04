"""Section 3.1, Differentiation: the editable source of 3-differentiation.json."""
from __future__ import annotations

from c3_common import card, definition, example, gate, prose, remark, write

B: list[dict] = []

B.append(prose("c3-diff-intro", r"""
The derivative measures how fast a function changes: it is the limit of the slopes of secant lines. In this section $f$ is a real-valued function on an open interval $(a,b)$, and we rebuild the differential calculus of one variable on the foundation of Chapters 1 and 2. The central result is the mean value theorem; almost everything after it (L'Hôpital's rule, the behaviour of inverse functions, Taylor's theorem) is the mean value theorem applied with some cunning.
"""))

B.append(definition("c3-def-derivative", "Derivative", r"""
Let $f : (a,b) \to \R$ and $x \in (a,b)$. We say that $f$ is \emph{differentiable at $x$} with \emph{derivative} $L \in \R$ if
\[ \lim_{t \to x} \frac{f(t) - f(x)}{t - x} = L, \]
that is: for every $\eps > 0$ there is a $\delta > 0$ such that
\[ t \in (a,b) \text{ and } 0 < \abs{t - x} < \delta \quad\Longrightarrow\quad \abs{\frac{f(t) - f(x)}{t - x} - L} < \eps . \]
We write $L = f'(x)$. The function $f$ is \emph{differentiable} if it is differentiable at every point of $(a,b)$; then $f' : (a,b) \to \R$ is its derivative. The limit, when it exists, is unique, as for any limit.

Here and throughout the section an open interval $(a,b)$ may be unbounded: $a = -\infty$ or $b = +\infty$ is allowed, so that $\R$ itself is included. A closed interval $[a,b]$ always has real endpoints.
"""))

B.append(gate("theorem", "c3-thm-diff-implies-continuous", "Differentiable implies continuous", r"""
If $f : (a,b) \to \R$ is differentiable at $x$, then $f$ is continuous at $x$.
""", r"""
Let $L = f'(x)$. Taking $\eps = 1$ in the definition of the derivative, there is a $\delta_1 > 0$ such that for $t \in (a,b)$ with $0 < \abs{t - x} < \delta_1$,
\[ \abs{\frac{f(t) - f(x)}{t - x}} < \abs{L} + 1, \qquad\text{so}\qquad \abs{f(t) - f(x)} \le (\abs{L} + 1)\abs{t - x}. \]
The last inequality also holds when $t = x$. Given $\eps > 0$, put $\delta = \min\set{\delta_1, \eps/(\abs{L}+1)}$. If $t \in (a,b)$ and $\abs{t - x} < \delta$, then $\abs{f(t) - f(x)} \le (\abs{L}+1)\abs{t-x} < \eps$. Hence $f$ is continuous at $x$.
""", 1, 10, [
    r"Write $f(t) - f(x)$ as the difference quotient times $(t - x)$.",
    r"Near $x$ the difference quotient is bounded by $\abs{f'(x)} + 1$, so $\abs{f(t) - f(x)} \le (\abs{f'(x)}+1)\abs{t - x}$.",
], ["c3-def-derivative"]))

B.append(example("c3-ex-abs-not-differentiable", r"""
The converse fails. The function $f(x) = \abs{x}$ is continuous on $\R$, but at $x = 0$ its difference quotient $\abs{t}/t$ equals $1$ for $t > 0$ and $-1$ for $t < 0$, so it has no limit as $t \to 0$. Thus $\abs{x}$ is not differentiable at $0$.
""", "A continuous function need not be differentiable"))

B.append(prose("c3-diff-rules-intro", r"""
The rules of differentiation follow from the limit laws: if $u(t) \to U$ and $v(t) \to V$ as $t \to x$, then $u(t) + v(t) \to U + V$ and $u(t)v(t) \to UV$, and $u(t)/v(t) \to U/V$ when $V \neq 0$. These may be used freely below.
"""))

B.append(gate("theorem", "c3-thm-sum-product-rule", "Linearity and the product rule", r"""
Let $f, g : (a,b) \to \R$ be differentiable at $x$ and let $c \in \R$. Then $f + g$, $cf$ and $fg$ are differentiable at $x$, and
\[ (f+g)'(x) = f'(x) + g'(x), \qquad (cf)'(x) = c f'(x), \qquad (fg)'(x) = f'(x)g(x) + f(x)g'(x). \]
Moreover a constant function has derivative $0$ and the identity function $x \mapsto x$ has derivative $1$ at every point.
""", r"""
For $t \neq x$ write $\Delta f = f(t) - f(x)$, $\Delta g = g(t) - g(x)$ and $\Delta t = t - x$.

\emph{Sum and scalar multiple.} The difference quotients are
\[ \frac{(f+g)(t) - (f+g)(x)}{\Delta t} = \frac{\Delta f}{\Delta t} + \frac{\Delta g}{\Delta t}, \qquad \frac{(cf)(t) - (cf)(x)}{\Delta t} = c\,\frac{\Delta f}{\Delta t}, \]
and by the limit laws they tend to $f'(x) + g'(x)$ and $c f'(x)$ as $t \to x$.

\emph{Product.} We have
\[ f(t)g(t) - f(x)g(x) = \bigl(f(t) - f(x)\bigr) g(t) + f(x)\bigl(g(t) - g(x)\bigr), \]
so
\[ \frac{(fg)(t) - (fg)(x)}{\Delta t} = \frac{\Delta f}{\Delta t}\, g(t) + f(x)\, \frac{\Delta g}{\Delta t}. \]
Since $g$ is differentiable at $x$ it is continuous at $x$, so $g(t) \to g(x)$ as $t \to x$. By the limit laws the right-hand side tends to $f'(x) g(x) + f(x) g'(x)$.

\emph{Constants and the identity.} If $f$ is constant, every difference quotient is $0$, so $f'(x) = 0$. If $f(t) = t$, every difference quotient is $(t - x)/(t - x) = 1$, so $f'(x) = 1$.
""", 2, 15, [
    r"Write out each difference quotient and use the limit laws.",
    r"For the product, add and subtract $f(x)g(t)$ in the numerator. You will need $g(t) \to g(x)$: why is that true?",
], ["c3-def-derivative", "c3-thm-diff-implies-continuous"]))

B.append(gate("theorem", "c3-thm-quotient-rule", "Quotient rule", r"""
Let $f, g : (a,b) \to \R$ be differentiable at $x$ with $g(x) \neq 0$. Then there is an open interval $J \subseteq (a,b)$ containing $x$ on which $g$ does not vanish, the function $f/g : J \to \R$ is differentiable at $x$, and
\[ \left(\frac{f}{g}\right)'(x) = \frac{f'(x) g(x) - f(x) g'(x)}{g(x)^2}. \]
""", r"""
Since $g$ is differentiable at $x$, it is continuous at $x$. Taking $\eps = \abs{g(x)}/2 > 0$ in the definition of continuity, there is a $\delta > 0$ such that $J = (x - \delta, x + \delta) \subseteq (a,b)$ and $\abs{g(t) - g(x)} < \abs{g(x)}/2$ for $t \in J$; then $\abs{g(t)} > \abs{g(x)}/2 > 0$ on $J$.

First consider $1/g$ on $J$. For $t \in J$, $t \neq x$,
\[ \frac{1}{t - x}\left(\frac{1}{g(t)} - \frac{1}{g(x)}\right) = -\frac{g(t) - g(x)}{t - x} \cdot \frac{1}{g(t) g(x)}. \]
As $t \to x$ the first factor tends to $g'(x)$, and $g(t) \to g(x) \neq 0$ by continuity, so by the limit laws the right-hand side tends to $-g'(x)/g(x)^2$. Thus $1/g$ is differentiable at $x$ with derivative $-g'(x)/g(x)^2$.

Now $f/g = f \cdot (1/g)$ on $J$, and the product rule gives
\[ \left(\frac{f}{g}\right)'(x) = f'(x)\frac{1}{g(x)} + f(x)\left(-\frac{g'(x)}{g(x)^2}\right) = \frac{f'(x)g(x) - f(x)g'(x)}{g(x)^2}. \]
""", 2, 15, [
    r"First explain why $g$ is nonzero near $x$. Then treat $1/g$ alone and finish with the product rule.",
    r"$\dfrac{1}{g(t)} - \dfrac{1}{g(x)} = -\dfrac{g(t) - g(x)}{g(t)g(x)}$.",
], ["c3-thm-diff-implies-continuous", "c3-thm-sum-product-rule"]))

B.append(gate("exercise", "c3-ex-power-rule", "Derivative of a power", r"""
For each integer $n \ge 1$, the function $f(x) = x^n$ on $\R$ is differentiable with $f'(x) = n x^{n-1}$ (where $x^0 = 1$). Consequently every polynomial is differentiable on $\R$.
""", r"""
By induction on $n$. For $n = 1$, $f$ is the identity function, whose derivative is $1 = 1 \cdot x^0$. Suppose $x^n$ has derivative $n x^{n-1}$. Since $x^{n+1} = x^n \cdot x$, the product rule gives
\[ (x^{n+1})' = n x^{n-1} \cdot x + x^n \cdot 1 = (n+1) x^n . \]
This completes the induction. A polynomial is a finite sum of constant multiples of powers $x^n$ and a constant, so it is differentiable by linearity of the derivative.
""", 1, 10, [
    r"Induct on $n$, writing $x^{n+1} = x^n \cdot x$.",
], ["c3-thm-sum-product-rule"]))

B.append(gate("theorem", "c3-thm-chain-rule", "Chain rule", r"""
Let $f : (a,b) \to (c,d)$ be differentiable at $x$ and let $g : (c,d) \to \R$ be differentiable at $y = f(x)$. Then $g \circ f$ is differentiable at $x$ and
\[ (g \circ f)'(x) = g'(y)\, f'(x). \]
""", r"""
Define $\varphi : (c,d) \to \R$ by
\[ \varphi(s) = \begin{cases} \dfrac{g(s) - g(y)}{s - y} & \text{if } s \neq y, \\[2mm] g'(y) & \text{if } s = y. \end{cases} \]
Differentiability of $g$ at $y$ says exactly that $\varphi(s) \to \varphi(y)$ as $s \to y$, so $\varphi$ is continuous at $y$. Also
\[ g(s) - g(y) = \varphi(s)(s - y) \qquad \text{for every } s \in (c,d), \]
including $s = y$, where both sides vanish.

Put $s = f(t)$. For $t \in (a,b)$, $t \neq x$,
\[ \frac{g(f(t)) - g(f(x))}{t - x} = \varphi(f(t)) \cdot \frac{f(t) - f(x)}{t - x}. \]
Now $f$ is continuous at $x$ (it is differentiable there) and $\varphi$ is continuous at $y = f(x)$, so $\varphi \circ f$ is continuous at $x$, and $\varphi(f(t)) \to \varphi(y) = g'(y)$ as $t \to x$. The second factor tends to $f'(x)$. By the limit law for products, the difference quotient of $g \circ f$ tends to $g'(y) f'(x)$.
""", 3, 30, [
    r"The tempting step of multiplying and dividing by $f(t) - f(x)$ fails when $f(t) = f(x)$ for $t$ arbitrarily near $x$. Find a formulation that avoids division.",
    r"Define $\varphi(s) = \dfrac{g(s) - g(y)}{s - y}$ for $s \ne y$ and $\varphi(y) = g'(y)$. Then $\varphi$ is continuous at $y$ and $g(s) - g(y) = \varphi(s)(s - y)$ for all $s$.",
], ["c3-def-derivative", "c3-thm-diff-implies-continuous"]))

B.append(prose("c3-mvt-intro", r"""
So far the derivative has been a local matter. The mean value theorem turns local information (the derivative at single points) into global information (how far $f(b)$ is from $f(a)$). It rests on one fact from Chapter 1: a continuous function on $[a,b]$ attains a maximum and a minimum.
"""))

B.append(gate("lemma", "c3-lem-interior-extremum", "Derivative vanishes at an interior extremum", r"""
Let $f : (a,b) \to \R$ and let $\theta \in (a,b)$ be a point where $f$ attains its maximum, $f(\theta) \ge f(t)$ for all $t \in (a,b)$, or its minimum, $f(\theta) \le f(t)$ for all $t \in (a,b)$. If $f$ is differentiable at $\theta$, then $f'(\theta) = 0$.
""", r"""
Suppose $f$ attains its maximum at $\theta$; the case of a minimum follows by applying this case to $-f$, whose derivative at $\theta$ is $-f'(\theta)$. Let $L = f'(\theta)$ and write $q(t) = \dfrac{f(t) - f(\theta)}{t - \theta}$ for $t \neq \theta$. The numerator is $\le 0$ for every $t$, so
\[ q(t) \le 0 \text{ for } t > \theta, \qquad q(t) \ge 0 \text{ for } t < \theta. \]
If $L > 0$, take $\eps = L$: there is a $\delta > 0$ with $\abs{q(t) - L} < L$, hence $q(t) > 0$, whenever $0 < \abs{t - \theta} < \delta$ and $t \in (a,b)$. Choosing such a $t$ with $t > \theta$ contradicts $q(t) \le 0$. If $L < 0$, take $\eps = -L$: then $q(t) < 0$ for $0 < \abs{t - \theta} < \delta$, and choosing such a $t$ with $t < \theta$ contradicts $q(t) \ge 0$. Hence $L = 0$.
""", 2, 15, [
    r"Look at the sign of the difference quotient on each side of $\theta$.",
    r"For $t > \theta$ the quotient is $\le 0$; for $t < \theta$ it is $\ge 0$. A nonzero limit would force one sign on both sides.",
], ["c3-def-derivative"]))

B.append(gate("theorem", "c3-thm-rolle", "Rolle's theorem", r"""
Let $f : [a,b] \to \R$ be continuous on $[a,b]$ and differentiable on $(a,b)$, where $a < b$. If $f(a) = f(b)$, then there is a $\theta \in (a,b)$ with $f'(\theta) = 0$.
""", r"""
Since $f$ is continuous on the compact interval $[a,b]$, it attains a maximum value $M$ and a minimum value $m$ on $[a,b]$. Let $c = f(a) = f(b)$; then $m \le c \le M$.

If $M > c$, then $M$ is attained at some $\theta \in [a,b]$ with $\theta \neq a, b$, so $\theta \in (a,b)$ and $f(\theta) \ge f(t)$ for all $t \in (a,b)$. By the interior extremum lemma, $f'(\theta) = 0$.

If $m < c$, the same argument at a point where the minimum is attained gives a $\theta \in (a,b)$ with $f'(\theta) = 0$.

Otherwise $m = c = M$, so $f$ is constant on $[a,b]$ and $f'(\theta) = 0$ for every $\theta \in (a,b)$; such $\theta$ exist because $a < b$.
""", 2, 15, [
    r"A continuous function on $[a,b]$ attains its maximum and minimum. Where?",
    r"If the maximum or the minimum differs from $f(a) = f(b)$, it is attained in the open interval. Otherwise $f$ is constant.",
], ["c3-lem-interior-extremum"]))

B.append(gate("theorem", "c3-thm-mvt", "Mean value theorem", r"""
Let $f : [a,b] \to \R$ be continuous on $[a,b]$ and differentiable on $(a,b)$, where $a < b$. Then there is a $\theta \in (a,b)$ such that
\[ f(b) - f(a) = f'(\theta)(b - a). \]
""", r"""
Let $S = \dfrac{f(b) - f(a)}{b - a}$ be the slope of the secant line and define
\[ \varphi(x) = f(x) - S\,(x - a), \qquad x \in [a,b]. \]
Then $\varphi$ is continuous on $[a,b]$ and differentiable on $(a,b)$ with $\varphi'(x) = f'(x) - S$, by linearity of the derivative. Moreover $\varphi(a) = f(a)$ and $\varphi(b) = f(b) - (f(b) - f(a)) = f(a)$. By Rolle's theorem there is a $\theta \in (a,b)$ with $\varphi'(\theta) = 0$, that is $f'(\theta) = S$, which is the claim.
""", 2, 15, [
    r"Reduce to Rolle's theorem by subtracting a suitable linear function from $f$.",
    r"Take $\varphi(x) = f(x) - S(x - a)$ with $S$ the slope of the secant through $(a, f(a))$ and $(b, f(b))$.",
], ["c3-thm-rolle", "c3-thm-sum-product-rule"]))

B.append(gate("corollary", "c3-cor-mvt-consequences", "Consequences of the mean value theorem", r"""
Let $f : (a,b) \to \R$ be differentiable.
\begin{enumerate}
\item If $\abs{f'(x)} \le M$ for all $x \in (a,b)$, then $\abs{f(t) - f(s)} \le M \abs{t - s}$ for all $s, t \in (a,b)$.
\item If $f'(x) = 0$ for all $x \in (a,b)$, then $f$ is constant.
\item If $f'(x) \ge 0$ for all $x \in (a,b)$, then $f$ is nondecreasing: $s < t$ implies $f(s) \le f(t)$. If $f'(x) > 0$ for all $x$, then $f$ is strictly increasing: $s < t$ implies $f(s) < f(t)$. Likewise with the inequalities reversed.
\end{enumerate}
""", r"""
Let $s < t$ be points of $(a,b)$. The restriction of $f$ to $[s,t]$ is continuous on $[s,t]$ (a differentiable function is continuous) and differentiable on $(s,t)$, so by the mean value theorem there is a $\theta \in (s,t)$ with
\[ f(t) - f(s) = f'(\theta)(t - s). \qquad (*) \]

(1) From $(*)$, $\abs{f(t) - f(s)} = \abs{f'(\theta)}\,\abs{t - s} \le M \abs{t - s}$. The inequality is symmetric in $s$ and $t$ and trivial when $s = t$, so it holds for all $s, t$.

(2) Apply (1) with $M = 0$: $f(t) = f(s)$ for all $s, t$.

(3) Since $t - s > 0$, the sign of $f(t) - f(s)$ in $(*)$ is the sign of $f'(\theta)$. If $f' \ge 0$ everywhere then $f(t) \ge f(s)$; if $f' > 0$ everywhere then $f(t) > f(s)$; if $f' \le 0$ everywhere then $f(t) \le f(s)$; and if $f' < 0$ everywhere then $f(t) < f(s)$.
""", 1, 10, [
    r"Apply the mean value theorem on $[s,t]$ for arbitrary $s < t$ in $(a,b)$.",
], ["c3-thm-mvt", "c3-thm-diff-implies-continuous"]))

B.append(gate("theorem", "c3-thm-ratio-mvt", "Ratio mean value theorem", r"""
Let $f, g : [a,b] \to \R$ be continuous on $[a,b]$ and differentiable on $(a,b)$, where $a < b$. Then there is a $\theta \in (a,b)$ such that
\[ \bigl(f(b) - f(a)\bigr)\, g'(\theta) = \bigl(g(b) - g(a)\bigr)\, f'(\theta). \]
""", r"""
Write $\Delta f = f(b) - f(a)$ and $\Delta g = g(b) - g(a)$, and define
\[ \Phi(x) = \Delta f \cdot \bigl(g(x) - g(a)\bigr) - \Delta g \cdot \bigl(f(x) - f(a)\bigr), \qquad x \in [a,b]. \]
Then $\Phi$ is continuous on $[a,b]$ and differentiable on $(a,b)$, with $\Phi'(x) = \Delta f \cdot g'(x) - \Delta g \cdot f'(x)$. Also $\Phi(a) = 0$ and $\Phi(b) = \Delta f \cdot \Delta g - \Delta g \cdot \Delta f = 0$. By Rolle's theorem there is a $\theta \in (a,b)$ with $\Phi'(\theta) = 0$, which is the asserted equation.
""", 3, 20, [
    r"Look for a combination of $f$ and $g$ that takes equal values at $a$ and $b$, and apply Rolle's theorem.",
    r"Try $\Phi(x) = \Delta f\,(g(x) - g(a)) - \Delta g\,(f(x) - f(a))$.",
], ["c3-thm-rolle", "c3-thm-sum-product-rule"]))

B.append(remark("c3-rem-ratio-mvt", r"""
With $g(x) = x$ this is the mean value theorem. When $g(b) \ne g(a)$ and $g'(\theta) \neq 0$ the conclusion reads $\dfrac{f(b) - f(a)}{g(b) - g(a)} = \dfrac{f'(\theta)}{g'(\theta)}$: the same $\theta$ serves both functions, which is more than two separate applications of the mean value theorem would give.
"""))

B.append(gate("theorem", "c3-thm-lhopital", "L'Hôpital's rule", r"""
Let $f, g : (a,b) \to \R$ be differentiable, with $b \in \R$, and suppose that
\begin{enumerate}
\item $f(x) \to 0$ and $g(x) \to 0$ as $x \to b$;
\item $g'(x) \neq 0$ for every $x \in (a,b)$;
\item $\dfrac{f'(x)}{g'(x)} \to L \in \R$ as $x \to b$.
\end{enumerate}
Then $g(x) \neq 0$ for every $x \in (a,b)$, and $\dfrac{f(x)}{g(x)} \to L$ as $x \to b$.

Here ``$u(x) \to \ell$ as $x \to b$'' means: for every $\eps > 0$ there is a $\delta > 0$ such that $\abs{u(x) - \ell} < \eps$ whenever $x \in (a,b)$ and $b - \delta < x < b$.
""", r"""
Extend $f$ and $g$ to $(a,b]$ by setting $f(b) = g(b) = 0$. By hypothesis (1) the extended functions are continuous at $b$, and they are continuous at each point of $(a,b)$ because they are differentiable there.

Fix $x \in (a,b)$. On $[x,b]$ the functions $f$ and $g$ are continuous, and on $(x,b)$ they are differentiable.

\emph{$g(x) \neq 0$.} If $g(x) = 0 = g(b)$, Rolle's theorem would give a $\theta \in (x,b)$ with $g'(\theta) = 0$, contrary to (2).

\emph{The limit.} By the ratio mean value theorem on $[x,b]$ there is a $\theta_x \in (x,b)$ with
\[ \bigl(f(b) - f(x)\bigr) g'(\theta_x) = \bigl(g(b) - g(x)\bigr) f'(\theta_x), \qquad\text{that is}\qquad f(x)\, g'(\theta_x) = g(x)\, f'(\theta_x). \]
Since $g(x) \neq 0$ and $g'(\theta_x) \neq 0$, we may divide:
\[ \frac{f(x)}{g(x)} = \frac{f'(\theta_x)}{g'(\theta_x)}. \]
Given $\eps > 0$, hypothesis (3) provides a $\delta > 0$ such that $\abs{f'(t)/g'(t) - L} < \eps$ whenever $t \in (a,b)$ and $b - \delta < t < b$. If $x \in (a,b)$ and $b - \delta < x < b$, then $b - \delta < x < \theta_x < b$, so
\[ \abs{\frac{f(x)}{g(x)} - L} = \abs{\frac{f'(\theta_x)}{g'(\theta_x)} - L} < \eps . \]
Hence $f(x)/g(x) \to L$ as $x \to b$.
""", 3, 30, [
    r"The hypothesis $f, g \to 0$ at $b$ lets you extend $f$ and $g$ continuously to $b$.",
    r"Apply the ratio mean value theorem on $[x, b]$ with $f(b) = g(b) = 0$: it gives $f(x)/g(x) = f'(\theta)/g'(\theta)$ for some $\theta$ between $x$ and $b$. Rolle's theorem shows $g(x) \ne 0$.",
], ["c3-thm-ratio-mvt", "c3-thm-rolle", "c3-thm-diff-implies-continuous"]))

B.append(remark("c3-rem-lhopital", r"""
The same statement holds, with the same proof after reflecting, for limits as $x \to a$ from the right. There are further versions (limits as $x \to \infty$, and the case in which $g(x) \to \pm\infty$ with no assumption on $f$) whose proofs need a more careful choice of the two points at which the ratio mean value theorem is applied. We do not use them.
"""))

B.append(prose("c3-darboux-intro", r"""
A derivative need not be continuous (an example follows). All the same, it cannot jump: like a continuous function, a derivative takes every value between any two of its values.
"""))

B.append(gate("theorem", "c3-thm-darboux", "Intermediate value property of derivatives", r"""
Let $f : (a,b) \to \R$ be differentiable. If $x_1 < x_2$ are points of $(a,b)$ and $\gamma$ lies strictly between $f'(x_1)$ and $f'(x_2)$, then there is a $\theta \in (x_1, x_2)$ with $f'(\theta) = \gamma$.
""", r"""
First suppose $f'(x_1) < \gamma < f'(x_2)$. Define $g(x) = f(x) - \gamma x$ on $(a,b)$. Then $g$ is differentiable with $g'(x) = f'(x) - \gamma$, so
\[ g'(x_1) < 0 < g'(x_2). \]
Since $g$ is continuous on the compact interval $[x_1, x_2]$, it attains a minimum over $[x_1,x_2]$ at some $\theta \in [x_1, x_2]$.

\emph{$\theta \neq x_1$.} Since $g'(x_1) < 0$, taking $\eps = -g'(x_1)$ in the definition of the derivative gives a $\delta > 0$ such that $\dfrac{g(t) - g(x_1)}{t - x_1} < 0$ for $0 < \abs{t - x_1} < \delta$, $t \in (a,b)$. Choosing such a $t$ with $x_1 < t < x_2$, we get $g(t) < g(x_1)$, so the minimum over $[x_1,x_2]$ is not attained at $x_1$.

\emph{$\theta \neq x_2$.} Since $g'(x_2) > 0$, there is a $\delta > 0$ such that $\dfrac{g(t) - g(x_2)}{t - x_2} > 0$ for $0 < \abs{t - x_2} < \delta$. Choosing such a $t$ with $x_1 < t < x_2$, the denominator is negative, so $g(t) < g(x_2)$, and the minimum is not attained at $x_2$.

Thus $\theta \in (x_1, x_2)$ and $g(\theta) \le g(t)$ for all $t \in (x_1,x_2)$. Applying the interior extremum lemma to $g$ on $(x_1,x_2)$ gives $g'(\theta) = 0$, i.e. $f'(\theta) = \gamma$.

If instead $f'(x_1) > \gamma > f'(x_2)$, apply the case just proved to $-f$ and $-\gamma$: there is a $\theta \in (x_1,x_2)$ with $-f'(\theta) = -\gamma$.
""", 3, 30, [
    r"Subtract $\gamma x$ from $f$ to reduce to the case $\gamma = 0$: a function $g$ with $g'(x_1) < 0 < g'(x_2)$.",
    r"$g$ has a minimum on the compact interval $[x_1, x_2]$. Use the signs of $g'(x_1)$ and $g'(x_2)$ to show the minimum is not at an endpoint.",
], ["c3-lem-interior-extremum", "c3-thm-diff-implies-continuous", "c3-thm-sum-product-rule"]))

B.append(example("c3-ex-discontinuous-derivative", r"""
Take for granted the sine and cosine functions and their derivatives. The function
\[ f(x) = \begin{cases} x^2 \sin(1/x) & x \neq 0, \\ 0 & x = 0 \end{cases} \]
is differentiable on $\R$: for $x \ne 0$ the rules give $f'(x) = 2x \sin(1/x) - \cos(1/x)$, and at $0$ the difference quotient $t \sin(1/t)$ tends to $0$, so $f'(0) = 0$. But $f'(x)$ has no limit as $x \to 0$, because of the term $\cos(1/x)$. So $f'$ exists everywhere and is discontinuous at $0$. In accordance with the theorem, the discontinuity is not a jump: $f'$ oscillates, taking every value in $[-1,1]$ in each interval around $0$.
""", "A discontinuous derivative"))

B.append(prose("c3-inverse-intro", r"""
When is the inverse of a differentiable function differentiable? Geometrically, the graph of $f^{-1}$ is the reflection of the graph of $f$ in the diagonal, so slopes should be reciprocal, and a zero slope of $f$ must be excluded.
"""))

B.append(gate("lemma", "c3-lem-nonvanishing-derivative-monotone", "A nonvanishing derivative forces strict monotonicity", r"""
Let $f : (a,b) \to \R$ be differentiable with $f'(x) \neq 0$ for every $x \in (a,b)$. Then either $f'(x) > 0$ for all $x$ and $f$ is strictly increasing, or $f'(x) < 0$ for all $x$ and $f$ is strictly decreasing. In particular $f$ is injective.
""", r"""
Suppose $f'$ takes both a positive and a negative value, say at points $x_1 \ne x_2$. Then $0$ lies strictly between $f'(x_1)$ and $f'(x_2)$, so by the intermediate value property of derivatives there is a $\theta$ between $x_1$ and $x_2$ with $f'(\theta) = 0$, contrary to hypothesis. Since $f'$ is never zero, it is therefore positive everywhere or negative everywhere. By the consequences of the mean value theorem, $f$ is strictly increasing in the first case and strictly decreasing in the second; in either case $s \neq t$ implies $f(s) \neq f(t)$.
""", 2, 10, [
    r"Could $f'$ be positive at one point and negative at another?",
], ["c3-thm-darboux", "c3-cor-mvt-consequences"]))

B.append(gate("lemma", "c3-lem-inverse-continuous", "The inverse of a strictly monotone surjection is continuous", r"""
Let $f : (a,b) \to (c,d)$ be strictly monotone (strictly increasing or strictly decreasing) and surjective. Then $f$ is a bijection and its inverse $g = f^{-1} : (c,d) \to (a,b)$ is continuous. (Nothing is assumed about continuity or differentiability of $f$.)
""", r"""
A strictly monotone function is injective, since $s \neq t$ implies $f(s) \neq f(t)$; being surjective, $f$ is a bijection.

\emph{The increasing case.} Let $f$ be strictly increasing. Then $g$ is strictly increasing too: if $y_1 < y_2$ and $g(y_1) \ge g(y_2)$, applying $f$ would give $y_1 \ge y_2$. Fix $y_0 \in (c,d)$, let $x_0 = g(y_0)$, and let $\eps > 0$. Shrinking $\eps$, we may assume $[x_0 - \eps, x_0 + \eps] \subseteq (a,b)$; a $\delta$ that works for the smaller $\eps$ works for the original one. Since $f$ is strictly increasing,
\[ f(x_0 - \eps) < y_0 < f(x_0 + \eps). \]
Let $\delta = \min\set{y_0 - f(x_0 - \eps),\ f(x_0 + \eps) - y_0} > 0$. If $\abs{y - y_0} < \delta$, then $f(x_0 - \eps) < y < f(x_0 + \eps)$; in particular $y$ lies between two points of the interval $(c,d)$, so $y \in (c,d)$, and applying the increasing function $g$ gives $x_0 - \eps < g(y) < x_0 + \eps$. Thus $\abs{g(y) - g(y_0)} < \eps$, and $g$ is continuous at $y_0$.

\emph{The decreasing case.} If $f$ is strictly decreasing, then $F = -f : (a,b) \to (-d,-c)$ is strictly increasing and surjective. Its inverse is $G(u) = g(-u)$, since $F(g(-u)) = -f(g(-u)) = u$ for $u \in (-d,-c)$. By the increasing case $G$ is continuous, and so $g(y) = G(-y)$ is continuous, as the composite of $G$ with the continuous map $y \mapsto -y$.
""", 3, 25, [
    r"Treat a strictly increasing $f$ first; then $g$ is increasing as well. Reduce the decreasing case to it by passing to $-f$.",
    r"For continuity of $g$ at $y_0 = f(x_0)$: the values $f(x_0 \pm \eps)$ bracket $y_0$, and $g$ carries the interval between them into $(x_0 - \eps, x_0 + \eps)$.",
], []))

B.append(gate("theorem", "c3-thm-inverse-function", "Inverse function theorem in dimension one", r"""
Let $f : (a,b) \to (c,d)$ be differentiable and surjective, with $f'(x) \neq 0$ for every $x \in (a,b)$. Then $f$ is a bijection, its inverse $g = f^{-1} : (c,d) \to (a,b)$ is differentiable (in particular continuous), and
\[ g'(y) = \frac{1}{f'(g(y))} \qquad \text{for every } y \in (c,d). \]
""", r"""
Since $f'$ never vanishes, $f$ is strictly monotone (a nonvanishing derivative forces strict monotonicity). Being a strictly monotone surjection, $f$ is a bijection and $g$ is continuous, by the preceding lemma.

Fix $y_0 \in (c,d)$, let $x_0 = g(y_0)$, and define
\[ \varphi(x) = \begin{cases} \dfrac{f(x) - f(x_0)}{x - x_0} & x \in (a,b),\ x \neq x_0, \\[2mm] f'(x_0) & x = x_0 . \end{cases} \]
Then $\varphi$ is continuous at $x_0$ by the definition of $f'(x_0)$, and $\varphi(x) \neq 0$ for every $x$: at $x_0$ by hypothesis, and elsewhere because $f$ is injective. For $y \in (c,d)$, $y \neq y_0$, put $x = g(y)$; then $x \neq x_0$ because $g$ is injective, $f(x) - f(x_0) = y - y_0$, and
\[ \frac{g(y) - g(y_0)}{y - y_0} = \frac{x - x_0}{f(x) - f(x_0)} = \frac{1}{\varphi(g(y))}. \]
Since $g$ is continuous at $y_0$ and $\varphi$ is continuous at $x_0 = g(y_0)$, the composite $\varphi \circ g$ is continuous at $y_0$, so $\varphi(g(y)) \to \varphi(x_0) = f'(x_0) \neq 0$ as $y \to y_0$. By the limit law for quotients,
\[ \lim_{y \to y_0} \frac{g(y) - g(y_0)}{y - y_0} = \frac{1}{f'(x_0)} = \frac{1}{f'(g(y_0))}. \]
So $g$ is differentiable at $y_0$ with the asserted derivative; in particular it is continuous there.
""", 3, 30, [
    r"First get a continuous inverse: $f$ is strictly monotone, and the preceding lemma applies.",
    r"With $x = g(y)$, $\dfrac{g(y) - g(y_0)}{y - y_0} = \dfrac{x - x_0}{f(x) - f(x_0)}$, the reciprocal of a difference quotient of $f$.",
    r"You need $x \to x_0$ as $y \to y_0$: that is the continuity of $g$. Package the difference quotient of $f$ as a function $\varphi$ that is continuous at $x_0$ and never zero, so that the limit of $1/\varphi(g(y))$ can be taken.",
], ["c3-lem-nonvanishing-derivative-monotone", "c3-lem-inverse-continuous", "c3-def-derivative"]))

B.append(remark("c3-rem-inverse", r"""
The hypothesis $f' \neq 0$ cannot be dropped: $f(x) = x^3$ is a differentiable bijection $\R \to \R$ whose inverse $y \mapsto y^{1/3}$ is not differentiable at $0$. Once we know $g$ is differentiable, the formula for $g'$ is also what the chain rule predicts from $f(g(y)) = y$; but the chain rule cannot be used to \emph{prove} that $g$ is differentiable.
"""))

B.append(definition("c3-def-higher-derivatives", "Higher derivatives and smoothness classes", r"""
Let $f : (a,b) \to \R$. Put $f^{(0)} = f$. For $r \ge 1$ we say $f$ is \emph{$r$ times differentiable at $x$} (or \emph{$r$-th order differentiable at $x$}) if $f^{(r-1)}$ is defined on an open interval containing $x$ and is differentiable at $x$; its derivative there is the \emph{$r$-th derivative} $f^{(r)}(x)$. We also write $f'' = f^{(2)}$, $f''' = f^{(3)}$. If this holds at every $x \in (a,b)$, then $f$ is \emph{$r$ times differentiable} and $f^{(r)} : (a,b) \to \R$.

The function $f$ is of class $C^r$ if it is $r$ times differentiable and $f^{(r)}$ is continuous; $C^0$ is the class of continuous functions. It is \emph{smooth}, or of class $C^\infty$, if it has derivatives of all orders. Since a differentiable function is continuous,
\[ C^0 \supseteq C^1 \supseteq C^2 \supseteq \cdots \supseteq C^\infty . \]
"""))

B.append(remark("c3-rem-smoothness", r"""
Each inclusion is strict. For instance $x \abs{x}$ is $C^1$ with derivative $2\abs{x}$, which is not differentiable at $0$; and the example $x^2 \sin(1/x)$ above is differentiable but not $C^1$. Beyond $C^\infty$ lies the class of \emph{analytic} functions, those that are locally given by convergent power series; these are studied in Chapter 4. The function equal to $e^{-1/x}$ for $x > 0$ and to $0$ for $x \le 0$ is smooth but not analytic, a fact we do not prove here.
"""))

B.append(prose("c3-taylor-intro", r"""
Differentiability at $x$ says that $f(x+h)$ is approximated by the linear polynomial $f(x) + f'(x)h$ with an error that is small compared to $h$. Higher derivatives give better polynomial approximations. For $f$ that is $r$ times differentiable at $x$, the \emph{Taylor polynomial of order $r$} at $x$ is
\[ P(h) = \sum_{k=0}^{r} \frac{f^{(k)}(x)}{k!}\, h^k = f(x) + f'(x)h + \frac{f''(x)}{2}h^2 + \dots + \frac{f^{(r)}(x)}{r!}h^r, \]
and the \emph{remainder} is $R(h) = f(x+h) - P(h)$, defined for all $h$ with $x + h \in (a,b)$. Differentiating $P$ term by term gives $P^{(k)}(0) = f^{(k)}(x)$ for $0 \le k \le r$.
"""))

B.append(gate("theorem", "c3-thm-taylor-flat", "Taylor approximation: the remainder is flat", r"""
Let $r \ge 1$ and let $f : (a,b) \to \R$ be $r$ times differentiable at $x$. Let $P$ be its Taylor polynomial of order $r$ at $x$ and $R(h) = f(x+h) - P(h)$. Then
\[ \lim_{h \to 0} \frac{R(h)}{h^r} = 0 . \]
""", r"""
By induction on $r$, the statement being for all functions $f$ that are $r$ times differentiable at $x$.

\emph{$r = 1$.} Here $R(h) = f(x+h) - f(x) - f'(x)h$, so for $h \neq 0$
\[ \frac{R(h)}{h} = \frac{f(x+h) - f(x)}{h} - f'(x), \]
which tends to $0$ as $h \to 0$ by the definition of $f'(x)$ (with $t = x + h$).

\emph{Inductive step.} Let $r \ge 2$ and assume the statement for $r - 1$. Since $f$ is $r$ times differentiable at $x$ and $r \ge 2$, there is an $\eta > 0$ such that $f$ is differentiable on $(x - \eta, x + \eta) \subseteq (a,b)$, and $f'$ is $r - 1$ times differentiable at $x$ with $(f')^{(j)}(x) = f^{(j+1)}(x)$. Hence $R$ is differentiable on $(-\eta, \eta)$, with
\[ R'(h) = f'(x + h) - \sum_{k=1}^{r} \frac{f^{(k)}(x)}{(k-1)!} h^{k-1} = f'(x+h) - \sum_{j=0}^{r-1} \frac{(f')^{(j)}(x)}{j!} h^{j}. \]
(The derivative of $h \mapsto f(x+h)$ is $f'(x+h)$ directly from the definition.) So $R'$ is the remainder of order $r - 1$ for the function $f'$ at $x$. By the inductive hypothesis, given $\eps > 0$ there is a $\delta$ with $0 < \delta \le \eta$ such that
\[ \abs{R'(s)} \le \eps \abs{s}^{r-1} \qquad \text{whenever } 0 < \abs{s} < \delta . \]
Let $0 < \abs{h} < \delta$. The function $R$ is differentiable, hence continuous, on $(-\eta,\eta)$, and $R(0) = f(x) - P(0) = 0$. By the mean value theorem on the closed interval with endpoints $0$ and $h$, there is a $\theta$ strictly between $0$ and $h$ with
\[ R(h) = R(h) - R(0) = R'(\theta)\, h . \]
Since $0 < \abs{\theta} < \abs{h} < \delta$,
\[ \abs{R(h)} = \abs{R'(\theta)}\,\abs{h} \le \eps \abs{\theta}^{r-1} \abs{h} \le \eps \abs{h}^{r} . \]
Thus $\abs{R(h)/h^r} \le \eps$ for $0 < \abs{h} < \delta$, which proves $R(h)/h^r \to 0$.
""", 4, 45, [
    r"Induct on $r$. The case $r = 1$ is the definition of the derivative.",
    r"Compute $R'(h)$: it is the remainder of order $r-1$ for the function $f'$.",
    r"Use the mean value theorem: $R(h) = R(h) - R(0) = R'(\theta)h$ with $\abs{\theta} < \abs{h}$, and the inductive estimate $\abs{R'(\theta)} \le \eps\abs{\theta}^{r-1}$.",
], ["c3-def-higher-derivatives", "c3-thm-mvt", "c3-ex-power-rule", "c3-thm-sum-product-rule", "c3-thm-diff-implies-continuous"]))

B.append(gate("theorem", "c3-thm-taylor-unique", "Taylor approximation: uniqueness", r"""
Let $r \ge 1$ and let $f : (a,b) \to \R$ be $r$ times differentiable at $x$. If $Q$ is a polynomial of degree at most $r$ such that
\[ \lim_{h \to 0} \frac{f(x+h) - Q(h)}{h^r} = 0, \]
then $Q$ is the Taylor polynomial of order $r$ of $f$ at $x$.
""", r"""
Let $P$ be the Taylor polynomial. By the previous theorem $(f(x+h) - P(h))/h^r \to 0$, so the polynomial $D = P - Q$, which has degree at most $r$, satisfies
\[ \frac{D(h)}{h^r} = \frac{f(x+h) - Q(h)}{h^r} - \frac{f(x+h) - P(h)}{h^r} \longrightarrow 0 \qquad (h \to 0). \]
Write $D(h) = d_0 + d_1 h + \dots + d_r h^r$ and suppose, for contradiction, that some coefficient is nonzero; let $j \le r$ be the least index with $d_j \neq 0$. Then for $h \neq 0$
\[ \frac{D(h)}{h^j} = d_j + d_{j+1} h + \dots + d_r h^{r-j} \longrightarrow d_j \qquad (h \to 0), \]
while also
\[ \frac{D(h)}{h^j} = \frac{D(h)}{h^r} \cdot h^{r-j} \longrightarrow 0 \qquad (h \to 0), \]
because $D(h)/h^r \to 0$ and $h^{r-j}$ is bounded near $0$ (it tends to $0$ if $j < r$ and equals $1$ if $j = r$). By uniqueness of limits $d_j = 0$, a contradiction. Hence $D = 0$ and $Q = P$.
""", 3, 25, [
    r"Consider the polynomial $D = P - Q$. What do you know about $D(h)/h^r$ as $h \to 0$?",
    r"If $D \neq 0$, look at its lowest-order nonzero coefficient $d_j$ and compute the limit of $D(h)/h^j$ in two ways.",
], ["c3-thm-taylor-flat"]))

B.append(gate("theorem", "c3-thm-taylor-lagrange", "Taylor approximation: the remainder formula", r"""
Let $r \ge 0$ and let $f : (a,b) \to \R$ be $r + 1$ times differentiable on $(a,b)$. Let $x \in (a,b)$, let $P$ be the Taylor polynomial of order $r$ of $f$ at $x$, and let $h \neq 0$ with $x + h \in (a,b)$. Then there is a $\theta$ strictly between $x$ and $x + h$ such that
\[ f(x+h) = P(h) + \frac{f^{(r+1)}(\theta)}{(r+1)!}\, h^{r+1}. \]
""", r"""
Let $I$ be the open interval of all $t$ with $x + t \in (a,b)$; it contains $0$ and $h$. Define the constant $c$ by $f(x+h) - P(h) = c\, h^{r+1}$, and let
\[ g(t) = f(x+t) - P(t) - c\, t^{r+1}, \qquad t \in I. \]
Then $g$ is $r+1$ times differentiable on $I$. Since $P^{(k)}(0) = f^{(k)}(x)$ for $0 \le k \le r$, and the $k$-th derivative of $t^{r+1}$ vanishes at $0$ for $0 \le k \le r$,
\[ g(0) = g'(0) = \dots = g^{(r)}(0) = 0 . \]
Also $g(h) = 0$ by the choice of $c$.

We claim that for each $k = 1, \dots, r+1$ there is a $t_k$ strictly between $0$ and $h$ with $g^{(k)}(t_k) = 0$. For $k = 1$: $g$ is continuous on the closed interval with endpoints $0$ and $h$, differentiable inside, and $g(0) = g(h) = 0$, so Rolle's theorem gives $t_1$ strictly between $0$ and $h$ with $g'(t_1) = 0$. If $t_k$ has been found for some $k \le r$, then $g^{(k)}$ is differentiable on $I$, hence continuous on the closed interval with endpoints $0$ and $t_k$, and $g^{(k)}(0) = 0 = g^{(k)}(t_k)$; Rolle's theorem gives $t_{k+1}$ strictly between $0$ and $t_k$, hence strictly between $0$ and $h$, with $g^{(k+1)}(t_{k+1}) = 0$.

Since $P$ has degree at most $r$, $P^{(r+1)} = 0$, and the $(r+1)$-st derivative of $t^{r+1}$ is $(r+1)!$. Hence
\[ 0 = g^{(r+1)}(t_{r+1}) = f^{(r+1)}(x + t_{r+1}) - (r+1)!\, c . \]
With $\theta = x + t_{r+1}$, which lies strictly between $x$ and $x+h$, this gives $c = f^{(r+1)}(\theta)/(r+1)!$, and the definition of $c$ is the asserted formula.
""", 4, 45, [
    r"For $r = 0$ this is the mean value theorem. In general, imitate its proof: subtract something from $f(x+t)$ so that Rolle's theorem applies.",
    r"Define $c$ by $f(x+h) - P(h) = c\,h^{r+1}$ and set $g(t) = f(x+t) - P(t) - c\,t^{r+1}$. Then $g$ and its first $r$ derivatives vanish at $0$, and $g(h) = 0$.",
    r"Apply Rolle's theorem $r+1$ times, each time between $0$ and the previous point.",
], ["c3-thm-rolle", "c3-def-higher-derivatives", "c3-ex-power-rule"]))

B.append(remark("c3-rem-taylor", r"""
The three statements together are Taylor's approximation theorem. The first two say the Taylor polynomial is the unique polynomial of degree at most $r$ that agrees with $f$ at $x$ to order $r$. The third is a quantitative version under one more derivative: if $\abs{f^{(r+1)}} \le M$ on $(a,b)$ then $\abs{R(h)} \le M\abs{h}^{r+1}/(r+1)!$. None of this says that the Taylor polynomials converge to $f$ as $r \to \infty$; that is the question of analyticity.
"""))

C = [
    card("c3-card-derivative", r"Define: $f : (a,b) \to \R$ is differentiable at $x$ with derivative $L$.",
         r"$\lim_{t \to x} \dfrac{f(t) - f(x)}{t - x} = L$: for every $\eps > 0$ there is $\delta > 0$ with $\abs{\frac{f(t)-f(x)}{t-x} - L} < \eps$ whenever $0 < \abs{t - x} < \delta$.", "c3-def-derivative"),
    card("c3-card-chain-rule-idea", r"What is the idea of the proof of the chain rule, and what pitfall does it avoid?",
         r"Set $\varphi(s) = \frac{g(s) - g(y)}{s - y}$ for $s \neq y$, $\varphi(y) = g'(y)$; then $g(s) - g(y) = \varphi(s)(s-y)$ for all $s$ and $\varphi$ is continuous at $y$. This avoids dividing by $f(t) - f(x)$, which may be $0$.", "c3-thm-chain-rule"),
    card("c3-card-mvt", r"State the mean value theorem and the idea of its proof.",
         r"If $f$ is continuous on $[a,b]$ and differentiable on $(a,b)$, then $f(b) - f(a) = f'(\theta)(b-a)$ for some $\theta \in (a,b)$. Subtract the secant line and apply Rolle's theorem (max or min of a continuous function on $[a,b]$ is interior, where the derivative vanishes).", "c3-thm-mvt"),
    card("c3-card-ratio-mvt", r"State the ratio mean value theorem.",
         r"If $f, g$ are continuous on $[a,b]$ and differentiable on $(a,b)$, there is $\theta \in (a,b)$ with $(f(b) - f(a))\,g'(\theta) = (g(b) - g(a))\,f'(\theta)$.", "c3-thm-ratio-mvt"),
    card("c3-card-lhopital", r"State L'Hôpital's rule (the $0/0$ case at a finite endpoint $b$).",
         r"If $f, g$ are differentiable on $(a,b)$, $f, g \to 0$ at $b$, $g' \neq 0$, and $f'/g' \to L$ at $b$, then $f/g \to L$ at $b$. Proof: ratio mean value theorem on $[x,b]$ with $f(b) = g(b) = 0$.", "c3-thm-lhopital"),
    card("c3-card-darboux-property", r"What property do all derivatives share with continuous functions? Must a derivative be continuous?",
         r"The intermediate value property: if $\gamma$ is strictly between $f'(x_1)$ and $f'(x_2)$ then $f'(\theta) = \gamma$ for some $\theta$ between. Derivatives need not be continuous: $x^2 \sin(1/x)$. Proof idea: $f(x) - \gamma x$ has an interior minimum on $[x_1,x_2]$.", "c3-thm-darboux"),
    card("c3-card-inverse", r"State the inverse function theorem in dimension one.",
         r"If $f : (a,b) \to (c,d)$ is a differentiable surjection with $f' \neq 0$ everywhere, then $f$ is a bijection with differentiable inverse and $(f^{-1})'(y) = 1/f'(f^{-1}(y))$.", "c3-thm-inverse-function"),
    card("c3-card-smoothness", r"Define the classes $C^r$ and $C^\infty$. Give a function that is $C^1$ but not $C^2$.",
         r"$C^r$: $r$ times differentiable with $f^{(r)}$ continuous. $C^\infty$: derivatives of all orders. $x\abs{x}$ has derivative $2\abs{x}$, which is not differentiable at $0$.", "c3-def-higher-derivatives"),
    card("c3-card-taylor", r"State Taylor's approximation theorem for $f$ that is $r$ times differentiable at $x$.",
         r"With $P(h) = \sum_{k=0}^r \frac{f^{(k)}(x)}{k!}h^k$ and $R(h) = f(x+h) - P(h)$: (a) $R(h)/h^r \to 0$ as $h \to 0$; (b) $P$ is the only polynomial of degree $\le r$ with this property; (c) if $f$ is $r+1$ times differentiable on $(a,b)$, then $R(h) = \frac{f^{(r+1)}(\theta)}{(r+1)!}h^{r+1}$ for some $\theta$ between $x$ and $x+h$.", "c3-thm-taylor-lagrange"),
]

write("3-differentiation", B, C)
