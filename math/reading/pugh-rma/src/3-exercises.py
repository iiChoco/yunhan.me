"""Chapter 3 exercises: the editable source of 3-exercises.json."""
from __future__ import annotations

from c3_common import gate, prose, write

B: list[dict] = []


def ex(id: str, title: str, tex: str, proof: str, difficulty: int, minutes: int, hints: list[str], uses: list[str]) -> dict:
    block = gate("exercise", id, title, tex, proof, difficulty, minutes, hints, uses)
    block["optional"] = True
    return block


B.append(prose("c3-exercises-intro", r"""
These exercises are extra credit: none is a gate, and the chapter clears on its theorems alone. Take them in any order; each can be solved from the definitions and results of this chapter together with what Chapters 1 and 2 provide.
"""))

# ── Differentiation ──────────────────────────────────────────────────────────

B.append(ex("c3-ex-lipschitz-bounded-derivative", "Bounded derivative means Lipschitz", r"""
Let $f : (a,b) \to \R$ be differentiable. A function is \emph{Lipschitz} if there is an $M$ with $\abs{f(t) - f(s)} \le M\abs{t - s}$ for all $s, t \in (a,b)$.
\begin{enumerate}
\item $f'$ is bounded on $(a,b)$ if and only if $f$ is Lipschitz.
\item If $f$ is Lipschitz and $a \in \R$, then $\lim_{t \to a^+} f(t)$ exists: there is an $L \in \R$ such that for every $\eps > 0$ there is a $\delta > 0$ with $\abs{f(t) - L} < \eps$ whenever $a < t < a + \delta$.
\end{enumerate}
""", r"""
(1) If $\abs{f'} \le M$ on $(a,b)$, then $\abs{f(t) - f(s)} \le M\abs{t - s}$ for all $s,t$ by the first consequence of the mean value theorem. Conversely suppose $\abs{f(t) - f(s)} \le M\abs{t-s}$ for all $s,t$. Fix $x \in (a,b)$. For every $t \ne x$ in $(a,b)$ the difference quotient satisfies
\[ \abs{\frac{f(t) - f(x)}{t - x}} \le M . \]
If $\abs{f'(x)} > M$, take $\eps = \abs{f'(x)} - M > 0$ in the definition of the derivative: there is a $t \neq x$ with $\abs{\frac{f(t)-f(x)}{t-x} - f'(x)} < \eps$, and then $\abs{\frac{f(t)-f(x)}{t-x}} > \abs{f'(x)} - \eps = M$, a contradiction. So $\abs{f'(x)} \le M$ for every $x$.

(2) Let $M$ be a Lipschitz constant for $f$ and choose a sequence $(t_n)$ in $(a,b)$ with $t_n \to a$. Then $\abs{f(t_n) - f(t_m)} \le M\abs{t_n - t_m}$, and $(t_n)$ is a Cauchy sequence, so $(f(t_n))$ is a Cauchy sequence; by completeness of $\R$ it converges to some $L$. Given $\eps > 0$, choose $N$ with $\abs{f(t_N) - L} < \eps/2$ and $\abs{t_N - a} < \dfrac{\eps}{4(M+1)}$, and put $\delta = \dfrac{\eps}{4(M+1)}$. If $a < t < a + \delta$, then $\abs{t - t_N} \le \abs{t - a} + \abs{a - t_N} < \dfrac{\eps}{2(M+1)}$, so
\[ \abs{f(t) - L} \le \abs{f(t) - f(t_N)} + \abs{f(t_N) - L} \le M\abs{t - t_N} + \frac{\eps}{2} < \frac{\eps}{2} + \frac{\eps}{2} = \eps . \]
""", 2, 20, [
    r"One direction of (1) is a consequence of the mean value theorem. For the other, a Lipschitz bound is a bound on every difference quotient.",
    r"For (2), the images under $f$ of a sequence tending to $a$ form a Cauchy sequence.",
], ["c3-def-derivative", "c3-cor-mvt-consequences"]))

B.append(ex("c3-ex-inverse-zero-derivative", "Where the derivative vanishes, the inverse is not differentiable", r"""
Let $f : (a,b) \to (c,d)$ be a differentiable bijection with inverse $g : (c,d) \to (a,b)$, and suppose $f'(x_0) = 0$ for some $x_0 \in (a,b)$. Then $g$ is not differentiable at $y_0 = f(x_0)$. So the hypothesis $f' \neq 0$ in the inverse function theorem cannot be dropped.
""", r"""
Suppose $g$ were differentiable at $y_0$. Since $f : (a,b) \to (c,d)$ is differentiable at $x_0$ and $g : (c,d) \to \R$ is differentiable at $y_0 = f(x_0)$, the chain rule says that $g \circ f$ is differentiable at $x_0$ with
\[ (g \circ f)'(x_0) = g'(y_0)\, f'(x_0) = g'(y_0) \cdot 0 = 0 . \]
But $g \circ f$ is the identity function on $(a,b)$, whose derivative is $1$ at every point. Since the derivative is unique, $0 = 1$, a contradiction. Hence $g$ is not differentiable at $y_0$.
""", 1, 10, [
    r"Differentiate $g \circ f = \id$ at $x_0$ with the chain rule.",
], ["c3-thm-chain-rule", "c3-thm-sum-product-rule", "c3-thm-inverse-function"]))

B.append(ex("c3-ex-positive-derivative-not-increasing", "A positive derivative at a point does not make the function increasing near it", r"""
Prove or disprove: if $f : \R \to \R$ is differentiable and $f'(0) > 0$, then there is a $\delta > 0$ such that $f$ is nondecreasing on $(-\delta, \delta)$. (As in the example of a discontinuous derivative, take the sine and cosine functions and their derivatives for granted.)
""", r"""
The statement is false. Let
\[ f(x) = \begin{cases} x + 2x^2 \sin(1/x) & x \neq 0, \\ 0 & x = 0 . \end{cases} \]

\emph{$f'(0) = 1$.} For $h \neq 0$ the difference quotient at $0$ is $\dfrac{f(h) - f(0)}{h} = 1 + 2h\sin(1/h)$, and $\abs{2h \sin(1/h)} \le 2\abs{h} \to 0$ as $h \to 0$. So $f'(0) = 1 > 0$.

\emph{$f'$ away from $0$.} On $(0,\infty)$ and on $(-\infty,0)$ the rules of differentiation apply: $x \mapsto 1/x$ has derivative $-1/x^2$ by the quotient rule, so $\sin(1/x)$ has derivative $-\cos(1/x)/x^2$ by the chain rule, and the product and sum rules give
\[ f'(x) = 1 + 4x\sin(1/x) + 2x^2 \cdot \Bigl(-\frac{\cos(1/x)}{x^2}\Bigr) = 1 + 4x\sin(1/x) - 2\cos(1/x) \qquad (x \neq 0). \]
At the points $x_n = \dfrac{1}{2\pi n}$, $n \ge 1$, we have $\sin(1/x_n) = 0$ and $\cos(1/x_n) = 1$, so $f'(x_n) = -1 < 0$.

\emph{A nondecreasing function has nonnegative derivative.} Suppose $f$ were nondecreasing on some open interval $J$ and let $x \in J$. For $t \in J$, $t \neq x$, the numerator and denominator of $\dfrac{f(t) - f(x)}{t - x}$ have the same sign (or the numerator is $0$), so every such difference quotient is $\ge 0$. If $f'(x) < 0$, taking $\eps = -f'(x)$ in the definition of the derivative gives a $\delta > 0$ such that $\dfrac{f(t)-f(x)}{t-x} < f'(x) + \eps = 0$ whenever $0 < \abs{t - x} < \delta$; since $J$ is open, such a $t$ can be chosen in $J$, a contradiction. So $f' \ge 0$ on $J$.

Now $x_n \to 0$, so every interval $(-\delta,\delta)$ contains some $x_n$, where $f'(x_n) = -1 < 0$. By the previous paragraph $f$ is nondecreasing on no interval $(-\delta,\delta)$. (Note that this does not contradict the consequences of the mean value theorem: $f' > 0$ \emph{on a whole interval} does force $f$ to increase there. Here $f' > 0$ only at the single point $0$, and $f'$ is not continuous at $0$.)
""", 3, 30, [
    r"Look for a counterexample built from $x^2\sin(1/x)$, which has a derivative that is discontinuous at $0$.",
    r"Try $f(x) = x + 2x^2\sin(1/x)$. Compute $f'(0)$ from the definition and $f'(x)$ for $x \neq 0$ from the rules; find points near $0$ where $f' < 0$.",
    r"Show that a function nondecreasing on an open interval has derivative $\ge 0$ there (look at the sign of the difference quotients).",
], ["c3-def-derivative", "c3-thm-sum-product-rule", "c3-thm-quotient-rule", "c3-thm-chain-rule", "c3-ex-discontinuous-derivative"]))

B.append(ex("c3-ex-derivative-no-jump", "A derivative has no jump", r"""
Let $f : (a,b) \to \R$ be differentiable and let $x \in (a,b)$. Suppose that the one-sided limits
\[ L^+ = \lim_{t \to x^+} f'(t), \qquad L^- = \lim_{t \to x^-} f'(t) \]
both exist in $\R$; here $L^+ = \lim_{t \to x^+} f'(t)$ means that for every $\eps > 0$ there is a $\delta > 0$ with $\abs{f'(t) - L^+} < \eps$ whenever $t \in (a,b)$ and $x < t < x + \delta$, and $L^-$ is defined with $x - \delta < t < x$ instead. Then $L^+ = L^- = f'(x)$. Consequently a derivative has neither jump discontinuities nor removable discontinuities: at every point where $f'$ is discontinuous, at least one of its one-sided limits fails to exist.
""", r"""
Let $\eps > 0$. By the definitions of $L^+$, of $L^-$ and of $f'(x)$ there is a $\delta > 0$ (the least of the three) such that $(x - \delta, x + \delta) \subseteq (a,b)$, $\abs{f'(s) - L^+} < \eps$ for $x < s < x + \delta$, $\abs{f'(s) - L^-} < \eps$ for $x - \delta < s < x$, and $\abs{\frac{f(t) - f(x)}{t - x} - f'(x)} < \eps$ for $0 < \abs{t - x} < \delta$.

Fix $t$ with $x < t < x + \delta$. On $[x,t]$ the function $f$ is continuous (it is differentiable) and on $(x,t)$ it is differentiable, so the mean value theorem gives a $\theta \in (x,t)$ with
\[ \frac{f(t) - f(x)}{t - x} = f'(\theta) . \]
Since $x < \theta < x + \delta$, $\abs{f'(\theta) - L^+} < \eps$. Hence
\[ \abs{f'(x) - L^+} \le \abs{f'(x) - \frac{f(t)-f(x)}{t-x}} + \abs{f'(\theta) - L^+} < 2\eps . \]
As $\eps$ was arbitrary, $L^+ = f'(x)$. The same argument on $[t,x]$ for $x - \delta < t < x$ gives $L^- = f'(x)$.

For the consequence: if $f'$ is discontinuous at $x$ but both one-sided limits existed, they would both equal $f'(x)$ by what was just shown; then given $\eps > 0$ the two $\delta$'s from the one-sided limits would give $\abs{f'(t) - f'(x)} < \eps$ for all $t$ with $\abs{t - x}$ less than the smaller of them, so $f'$ would be continuous at $x$, a contradiction.
""", 2, 20, [
    r"Apply the mean value theorem on $[x,t]$ for $t$ slightly to the right of $x$: the difference quotient is a value of $f'$ at a point between.",
    r"As $t \to x^+$ the difference quotient tends to $f'(x)$, while the value of $f'$ at the intermediate point tends to $L^+$.",
], ["c3-thm-mvt", "c3-def-derivative", "c3-thm-diff-implies-continuous", "c3-thm-darboux"]))

B.append(ex("c3-ex-symmetric-second-derivative", "The symmetric second difference", r"""
\begin{enumerate}
\item If $f : (a,b) \to \R$ is twice differentiable at $x$, then
\[ \lim_{h \to 0} \frac{f(x+h) - 2f(x) + f(x-h)}{h^2} = f''(x) . \]
\item The limit may exist even when $f''(x)$ does not: give an example.
\end{enumerate}
""", r"""
(1) Choose $\eta > 0$ with $(x - \eta, x + \eta) \subseteq (a,b)$ and let $0 < \abs{h} < \eta$, so that both $x + h$ and $x - h$ lie in $(a,b)$. By Taylor's theorem (the remainder is flat) with $r = 2$, writing $P(h) = f(x) + f'(x)h + \frac{f''(x)}{2}h^2$ and $R(h) = f(x+h) - P(h)$, we have $R(h)/h^2 \to 0$ as $h \to 0$. Applying this at $h$ and at $-h$,
\[ f(x+h) = f(x) + f'(x)h + \frac{f''(x)}{2}h^2 + R(h), \qquad f(x-h) = f(x) - f'(x)h + \frac{f''(x)}{2}h^2 + R(-h) . \]
Adding and subtracting $2f(x)$,
\[ f(x+h) - 2f(x) + f(x-h) = f''(x)h^2 + R(h) + R(-h), \qquad\text{so}\qquad \frac{f(x+h) - 2f(x) + f(x-h)}{h^2} = f''(x) + \frac{R(h)}{h^2} + \frac{R(-h)}{(-h)^2} . \]
As $h \to 0$ both $h$ and $-h$ tend to $0$, so the last two terms tend to $0$, and the quotient tends to $f''(x)$.

(2) Let $f(x) = x\abs{x}$ on $\R$ and take $x = 0$. For $h \neq 0$, $f(h) - 2f(0) + f(-h) = h\abs{h} - h\abs{h} = 0$, so the quotient is $0$ for every $h \ne 0$ and the limit exists and equals $0$.

But $f''(0)$ does not exist. On $(0,\infty)$ the function $f$ agrees with $x^2$, and the difference quotients of $f$ at a point $x > 0$ involve only values at points $t$ with $\abs{t - x} < x$, hence only values of $x^2$; so $f'(x) = 2x$ there by the power rule. Likewise $f'(x) = -2x$ on $(-\infty,0)$. At $0$ the difference quotient is $h\abs{h}/h = \abs{h} \to 0$, so $f'(0) = 0$. Thus $f'(x) = 2\abs{x}$ for all $x$. If $f'$ were differentiable at $0$, then so would be $\abs{x} = \tfrac12 f'(x)$, by linearity of the derivative; but $\abs{x}$ is not differentiable at $0$. Hence $f'$ is not differentiable at $0$: $f''(0)$ does not exist.
""", 2, 20, [
    r"Use Taylor's theorem of order $2$ at $h$ and at $-h$, and add.",
    r"For (2), look for an odd function: then $f(h) + f(-h) = 0$ and the quotient vanishes identically. Which odd function is $C^1$ but not twice differentiable at $0$?",
], ["c3-thm-taylor-flat", "c3-def-higher-derivatives", "c3-ex-abs-not-differentiable", "c3-ex-power-rule", "c3-thm-sum-product-rule"]))

B.append(ex("c3-ex-landau-inequality", "A bounded function with bounded second derivative has bounded derivative", r"""
Let $f : \R \to \R$ be twice differentiable with $\abs{f(x)} \le A$ and $\abs{f''(x)} \le C$ for all $x \in \R$. Then
\[ \abs{f'(x)} \le 2\sqrt{AC} \qquad \text{for all } x \in \R . \]
""", r"""
Fix $x \in \R$ and $h > 0$. Since $f$ is $2$ times differentiable on $\R$, Taylor's theorem with the remainder formula, for $r = 1$, gives a $\theta$ strictly between $x$ and $x + h$ with
\[ f(x+h) = f(x) + f'(x)\,h + \frac{f''(\theta)}{2}\,h^2 . \]
Hence $f'(x)\,h = f(x+h) - f(x) - \frac{f''(\theta)}{2}h^2$, and the bounds give
\[ \abs{f'(x)}\, h \le 2A + \frac{C}{2}h^2, \qquad\text{that is}\qquad \abs{f'(x)} \le \frac{2A}{h} + \frac{C h}{2} \qquad \text{for every } h > 0 . \qquad (*) \]

If $A = 0$ then $f$ is identically $0$, so $f' = 0$ and the claim holds. If $C = 0$, then $(*)$ gives $\abs{f'(x)} \le 2A/h$ for every $h > 0$; since $2A/h$ can be made smaller than any positive number, $f'(x) = 0 = 2\sqrt{AC}$. If $A > 0$ and $C > 0$, choose $h = 2\sqrt{A/C}$ in $(*)$:
\[ \frac{2A}{h} = \frac{A}{\sqrt{A/C}} = A\sqrt{\frac{C}{A}} = \sqrt{AC}, \qquad \frac{Ch}{2} = C\sqrt{\frac{A}{C}} = \sqrt{AC}, \]
so $\abs{f'(x)} \le 2\sqrt{AC}$.
""", 3, 30, [
    r"Taylor's theorem with the remainder formula, order $1$, expresses $f(x+h)$ through $f(x)$, $f'(x)$ and a value of $f''$.",
    r"Solve for $f'(x)$ and bound: $\abs{f'(x)} \le 2A/h + Ch/2$ for every $h > 0$. Then choose $h$ to make the right side smallest.",
], ["c3-thm-taylor-lagrange", "c3-def-higher-derivatives"]))

B.append(ex("c3-ex-lhopital-infinity", "L'Hôpital's rule for $\\infty/\\infty$", r"""
Let $f, g : (a,b) \to \R$ be differentiable, with $b \in \R$, and suppose that
\begin{enumerate}
\item $g(x) \to +\infty$ as $x \to b$: for every $K$ there is a $\delta > 0$ with $g(x) > K$ whenever $x \in (a,b)$ and $b - \delta < x < b$;
\item $g'(x) \neq 0$ for every $x \in (a,b)$;
\item $\dfrac{f'(x)}{g'(x)} \to L \in \R$ as $x \to b$.
\end{enumerate}
Then $\dfrac{f(x)}{g(x)} \to L$ as $x \to b$. Nothing is assumed about the behaviour of $f$ at $b$.
""", r"""
Since $g'$ never vanishes, $g$ is strictly monotone, hence injective, and $g(x) \neq 0$ for all $x$ close to $b$ by (1).

Let $0 < \eps \le 1$. By (3) there is a $c \in (a,b)$ such that $\abs{f'(t)/g'(t) - L} < \eps$ for all $t \in (c,b)$. Fix $x \in (c,b)$. On $[c,x]$ the functions $f$ and $g$ are continuous, being differentiable on $(a,b)$, and on $(c,x)$ they are differentiable, so the ratio mean value theorem gives a $\theta \in (c,x)$ with
\[ \bigl(f(x) - f(c)\bigr)\, g'(\theta) = \bigl(g(x) - g(c)\bigr)\, f'(\theta) . \]
Since $g$ is injective, $g(x) \neq g(c)$, and $g'(\theta) \neq 0$ by (2); dividing,
\[ q(x) := \frac{f(x) - f(c)}{g(x) - g(c)} = \frac{f'(\theta)}{g'(\theta)}, \qquad\text{so}\qquad \abs{q(x) - L} < \eps \quad \text{for every } x \in (c,b) . \]

By (1) there is a $\delta > 0$ with $b - \delta > c$ such that for $b - \delta < x < b$,
\[ g(x) > \frac{\max\set{\abs{g(c)},\ \abs{f(c)},\ 1}}{\eps}, \qquad\text{hence}\qquad g(x) > 0, \quad \abs{\frac{g(c)}{g(x)}} < \eps, \quad \abs{\frac{f(c)}{g(x)}} < \eps . \]
For such $x$, the definition of $q(x)$ gives $f(x) = f(c) + q(x)\bigl(g(x) - g(c)\bigr)$, and dividing by $g(x)$,
\[ \frac{f(x)}{g(x)} - L = \frac{f(c)}{g(x)} + \bigl(q(x) - L\bigr) - q(x)\,\frac{g(c)}{g(x)} . \]
Since $\abs{q(x)} \le \abs{L} + \eps \le \abs{L} + 1$,
\[ \abs{\frac{f(x)}{g(x)} - L} \le \eps + \eps + (\abs{L} + 1)\,\eps = (\abs{L} + 3)\,\eps \qquad \text{whenever } b - \delta < x < b . \]
Since $(\abs{L} + 3)\eps$ can be made smaller than any prescribed positive number by the choice of $\eps$, this proves $f(x)/g(x) \to L$ as $x \to b$.
""", 4, 60, [
    r"In the $0/0$ case the ratio mean value theorem was applied on $[x,b]$. Here $b$ is unavailable; apply it on $[c,x]$ for a fixed $c$ close to $b$ instead.",
    r"For $c < x < b$ the ratio $\dfrac{f(x) - f(c)}{g(x) - g(c)}$ equals $f'(\theta)/g'(\theta)$ for some $\theta \in (c,x)$, so it is within $\eps$ of $L$ once $c$ is close enough to $b$. (Why is $g(x) \neq g(c)$?)",
    r"Write $\dfrac{f(x)}{g(x)} = \dfrac{f(c)}{g(x)} + \dfrac{f(x) - f(c)}{g(x) - g(c)}\cdot\Bigl(1 - \dfrac{g(c)}{g(x)}\Bigr)$ and let $g(x) \to \infty$ with $c$ fixed.",
], ["c3-thm-ratio-mvt", "c3-lem-nonvanishing-derivative-monotone", "c3-thm-diff-implies-continuous", "c3-thm-lhopital", "c3-rem-lhopital"]))

# ── Riemann integration ──────────────────────────────────────────────────────

B.append(ex("c3-ex-closed-zero-set-indicator", "The indicator of a closed zero set", r"""
Let $K \subseteq [a,b]$ be a closed zero set, and let $\chi_K : [a,b] \to \R$ be its indicator function: $\chi_K(x) = 1$ for $x \in K$ and $0$ otherwise. Then $\chi_K$ is discontinuous exactly at the points of $K$, it is integrable, and $\int_a^b \chi_K = 0$.

With $K$ the middle-thirds Cantor set of Chapter 2 (compact, uncountable, and a zero set), this gives a nonnegative integrable function with integral $0$ that is nonzero at uncountably many points.
""", r"""
\emph{$K$ contains no interval.} If $[p,q] \subseteq K$ with $p < q$, then $[p,q]$ would be a subset of a zero set, hence a zero set; but an interval of positive length is not a zero set.

\emph{Continuity off $K$.} Let $x \in [a,b] \setminus K$. Since $K$ is closed, $\R \setminus K$ is open, so there is an $r > 0$ with $(x - r, x + r) \cap K = \emptyset$. Then $\chi_K = 0$ on $(x-r,x+r) \cap [a,b]$, so $\chi_K$ is constant near $x$ and continuous at $x$.

\emph{Discontinuity on $K$.} Let $x \in K$ and $r > 0$. The set $(x - r, x+r) \cap [a,b]$ contains an interval of positive length: with $\rho = \tfrac12\min\set{r, b - a}$, it contains $[x, x + \rho]$ if $x + \rho \le b$, and otherwise $[x - \rho, x]$, since then $x > b - \rho \ge a + \rho$. So it contains a point $t \notin K$, and then $\abs{\chi_K(t) - \chi_K(x)} = 1$. So the continuity condition with $\eps = 1$ fails at $x$, for every $r$: $\chi_K$ is discontinuous at $x$.

\emph{Integrability.} $\chi_K$ is bounded, taking the values $0$ and $1$, and its set of discontinuities is $K$, a zero set. By the Riemann–Lebesgue theorem $\chi_K$ is integrable.

\emph{The integral.} Let $P = \set{x_0,\dots,x_n}$ be any partition of $[a,b]$. Each interval $[x_{i-1},x_i]$ has positive length, so it is not contained in $K$, and it contains a point where $\chi_K = 0$; since $\chi_K \ge 0$, the infimum $m_i$ of $\chi_K$ over the interval is $0$. Hence $L(\chi_K, P) = 0$ for every $P$, so $\underline{I}(\chi_K) = 0$. Since a Riemann integrable function has integral equal to its lower integral, $\int_a^b \chi_K = 0$.

For the Cantor set $C$: it is compact, hence closed, and it is a zero set (both from Chapter 2), so the above applies with $K = C$; and $\chi_C = 1$ on the uncountable set $C$.
""", 2, 25, [
    r"A zero set contains no interval of positive length. Use this both for the discontinuity set and for the lower sums.",
    r"Off $K$, the indicator is locally constant because $K$ is closed. On $K$, every neighbourhood contains a point of the complement.",
    r"Every lower sum is $0$; the integral equals the lower integral.",
], ["c3-def-zero-set", "c3-prop-zero-sets", "c3-prop-interval-not-zero", "c3-thm-riemann-lebesgue", "c3-def-darboux", "c3-lem-riemann-implies-darboux", "c3-rem-zero-sets"]))

B.append(ex("c3-ex-thomae", "Thomae's function is integrable", r"""
Define $f : [0,1] \to \R$ by $f(x) = 1/q$ if $x = p/q$ with $p \in \Z$ and $q \in \N$ having no common factor (so $f(0) = f(1) = 1$), and $f(x) = 0$ if $x$ is irrational. Then $f$ is continuous at every irrational point, discontinuous at every rational point, integrable, and $\int_0^1 f = 0$.
""", r"""
\emph{Rational points.} Let $x = p/q \in [0,1]$ in lowest terms, so $f(x) = 1/q > 0$. Every interval around $x$ contains an irrational number $t \in [0,1]$ (the irrationals are dense in $\R$), and $f(t) = 0$, so $\abs{f(t) - f(x)} = 1/q$. Hence the continuity condition with $\eps = 1/q$ fails: $f$ is discontinuous at $x$.

\emph{Irrational points.} Let $x \in [0,1]$ be irrational and let $\eps > 0$. Choose $Q \in \N$ with $1/Q < \eps$. The set $S$ of rational numbers in $[0,1]$ whose denominator in lowest terms is at most $Q$ is finite: for each $q \le Q$ the numerator is one of $0, 1, \dots, q$. Since $x \notin S$ and $S$ is finite, $\delta = \min\set{\abs{s - x} : s \in S} > 0$. Let $t \in [0,1]$ with $\abs{t - x} < \delta$. If $t$ is irrational, $f(t) = 0$. If $t$ is rational, $t \notin S$, so its denominator $q$ in lowest terms exceeds $Q$ and $f(t) = 1/q < 1/Q < \eps$. In either case $\abs{f(t) - f(x)} = f(t) < \eps$. So $f$ is continuous at $x$.

\emph{Integrability.} $f$ is bounded, $0 \le f \le 1$, and its set of discontinuities is $\Q \cap [0,1]$, which is countable and hence a zero set. By the Riemann–Lebesgue theorem $f$ is integrable.

\emph{The integral.} For any partition $P$ of $[0,1]$, each interval $[x_{i-1},x_i]$ contains an irrational point, where $f = 0$; as $f \ge 0$, the infimum of $f$ over the interval is $0$. So $L(f,P) = 0$ for every $P$, the lower integral is $0$, and the integral, which equals the lower integral, is $0$.
""", 3, 30, [
    r"Near a rational point there are irrational points, where $f = 0$.",
    r"Near an irrational $x$: only finitely many rationals in $[0,1]$ have denominator at most $Q$, and $x$ is at positive distance from all of them. Every other rational nearby has $f < 1/Q$.",
    r"For the integral, every lower sum is $0$.",
], ["c3-thm-riemann-lebesgue", "c3-prop-zero-sets", "c3-def-darboux", "c3-lem-riemann-implies-darboux", "c3-cor-continuous-integrable"]))

B.append(ex("c3-ex-composite-not-integrable", "A composite of integrable functions need not be integrable", r"""
Let $f : [0,1] \to [0,1]$ be Thomae's function (the previous exercise) and let $g : [0,1] \to \R$ be the indicator of $(0,1]$: $g(0) = 0$ and $g(y) = 1$ for $0 < y \le 1$. Then $f$ and $g$ are both integrable, but $g \circ f$ is not. (Compare: a continuous function of an integrable function is integrable.)
""", r"""
$f$ takes values in $[0,1]$, since each value is $0$ or $1/q$ with $q \ge 1$, so $g \circ f$ is defined, and $f$ is integrable by the previous exercise.

$g$ is bounded, and it is continuous at every $y \in (0,1]$: the points $t \in [0,1]$ with $\abs{t - y} < y$ all lie in $(0,1]$, where $g$ is constantly $1$. So $g$ has at most one discontinuity (at $0$), and a bounded function with countably many discontinuities is integrable.

Now $g(f(x)) = 1$ exactly when $f(x) > 0$, that is, exactly when $x$ is rational; and $g(f(x)) = 0$ when $x$ is irrational. So $g \circ f$ is the indicator function of the rationals on $[0,1]$, which is not integrable.
""", 2, 15, [
    r"Where is $g \circ f$ equal to $1$?",
], ["c3-ex-thomae", "c3-ex-dirichlet", "c3-cor-continuous-integrable", "c3-cor-composite-integrable", "c3-rem-composite"]))

B.append(ex("c3-ex-cauchy-schwarz-integral", "The Cauchy–Schwarz inequality for integrals", r"""
Let $f, g : [a,b] \to \R$ be integrable. Then $fg$, $f^2$ and $g^2$ are integrable and
\[ \Bigl(\int_a^b fg\Bigr)^2 \ \le\ \int_a^b f^2 \cdot \int_a^b g^2 . \]
""", r"""
Products of integrable functions are integrable, so $fg$, $f^2$ and $g^2$ are. Put
\[ F = \int_a^b f^2, \qquad G = \int_a^b g^2, \qquad H = \int_a^b fg . \]
Since $f^2 \ge 0$ and $g^2 \ge 0$, monotonicity of the integral (comparing with the constant function $0$, whose integral is $0$) gives $F \ge 0$ and $G \ge 0$.

Let $\lambda \in \R$. The function $f - \lambda g$ is integrable by linearity, its square is integrable, and $(f - \lambda g)^2 = f^2 - 2\lambda fg + \lambda^2 g^2 \ge 0$. By monotonicity and linearity,
\[ 0 \ \le\ \int_a^b (f - \lambda g)^2 \ =\ F - 2\lambda H + \lambda^2 G \qquad \text{for every } \lambda \in \R . \qquad (*) \]

If $G > 0$, take $\lambda = H/G$ in $(*)$: $0 \le F - 2H^2/G + H^2/G = F - H^2/G$, so $H^2 \le FG$.

If $G = 0$, then $(*)$ reads $0 \le F - 2\lambda H$ for every $\lambda$. If $H \neq 0$, the choice $\lambda = (F + 1)/(2H)$ gives $0 \le F - (F+1) = -1$, a contradiction; so $H = 0$, and $H^2 = 0 = FG$. In both cases $H^2 \le FG$.
""", 3, 25, [
    r"For every real $\lambda$, $\int (f - \lambda g)^2 \ge 0$. Expand.",
    r"The right side is a quadratic in $\lambda$ that is never negative. Choose $\lambda$ well; treat $\int g^2 = 0$ separately.",
], ["c3-cor-product-integrable", "c3-thm-integral-linear", "c3-thm-integral-monotone"]))

B.append(ex("c3-ex-indefinite-integral-jump", "The indefinite integral has a corner at a jump", r"""
Let $f : [a,b] \to \R$ be integrable, $F(x) = \int_a^x f$, and $x \in (a,b)$. Suppose the one-sided limits
\[ f(x^+) = \lim_{t \to x^+} f(t), \qquad f(x^-) = \lim_{t \to x^-} f(t) \]
exist in $\R$: that is, for every $\eps > 0$ there is a $\delta > 0$ with $\abs{f(t) - f(x^+)} < \eps$ whenever $x < t < x + \delta$, and likewise $\abs{f(t) - f(x^-)} < \eps$ whenever $x - \delta < t < x$. Then the one-sided derivatives of $F$ at $x$ exist and
\[ \lim_{h \to 0^+} \frac{F(x+h) - F(x)}{h} = f(x^+), \qquad \lim_{h \to 0^-} \frac{F(x+h) - F(x)}{h} = f(x^-) , \]
one-sided limits being understood in the same way ($0 < h < \delta$, respectively $-\delta < h < 0$). Consequently, if $f(x^+) \neq f(x^-)$, then $F$ is not differentiable at $x$. (The value $f(x)$ itself plays no role.)
""", r"""
$f$ is bounded, say $\abs{f} \le M$ on $[a,b]$. By additivity over intervals and the conventions for limits of integration, $f$ is integrable on every closed subinterval of $[a,b]$ and $F(y) - F(x) = \int_x^y f$ for all $x, y \in [a,b]$.

\emph{From the right.} Let $\eps > 0$ and choose $\delta > 0$ with $x + \delta \le b$ and $\abs{f(t) - f(x^+)} < \eps$ for $x < t < x + \delta$. Fix $h$ with $0 < h < \delta$ and let $0 < \eta < h$. By additivity,
\[ F(x+h) - F(x) = \int_x^{x+h} f = \int_x^{x+\eta} f + \int_{x+\eta}^{x+h} f . \]
The first integral has absolute value at most $M\eta$ by monotonicity. On $[x + \eta, x + h]$ we have $\abs{f(t) - f(x^+)} < \eps$ at every point, so by linearity (the constant $f(x^+)$ has integral $f(x^+)(h - \eta)$ over this interval) and monotonicity,
\[ \abs{\int_{x+\eta}^{x+h} f - f(x^+)(h - \eta)} = \abs{\int_{x+\eta}^{x+h} \bigl(f(t) - f(x^+)\bigr)\,dt} \le \eps (h - \eta) . \]
Therefore
\[ \abs{F(x+h) - F(x) - f(x^+)\,h} \le M\eta + \eps(h - \eta) + \abs{f(x^+)}\,\eta \le \eps h + \bigl(M + \abs{f(x^+)}\bigr)\eta . \]
This holds for every $\eta \in (0,h)$. If the left side exceeded $\eps h$, choosing $\eta$ with $(M + \abs{f(x^+)})\eta$ smaller than the excess would contradict it; hence $\abs{F(x+h) - F(x) - f(x^+)h} \le \eps h$, that is,
\[ \abs{\frac{F(x+h) - F(x)}{h} - f(x^+)} \le \eps \qquad \text{for } 0 < h < \delta . \]
So the right-hand difference quotient tends to $f(x^+)$.

\emph{From the left.} Choose $\delta > 0$ with $x - \delta \ge a$ and $\abs{f(t) - f(x^-)} < \eps$ for $x - \delta < t < x$. For $-\delta < h < 0$ put $k = -h > 0$; then $F(x+h) - F(x) = -\int_{x-k}^{x} f$, and the same argument with the splitting $\int_{x-k}^x f = \int_{x-k}^{x-\eta} f + \int_{x-\eta}^{x} f$ (now the piece of length $\eta$ is the one next to $x$) gives $\abs{\int_{x-k}^x f - f(x^-)\,k} \le \eps k$. Dividing by $h = -k$,
\[ \frac{F(x+h) - F(x)}{h} = \frac{\int_{x-k}^x f}{k}, \qquad \abs{\frac{F(x+h) - F(x)}{h} - f(x^-)} \le \eps \qquad \text{for } -\delta < h < 0 . \]
So the left-hand difference quotient tends to $f(x^-)$.

\emph{The corner.} If $F$ were differentiable at $x$, the difference quotient would tend to $F'(x)$ as $h \to 0$, hence also as $h \to 0^+$ and as $h \to 0^-$; by uniqueness of limits $f(x^+) = F'(x) = f(x^-)$. So if $f(x^+) \neq f(x^-)$, $F$ is not differentiable at $x$.
""", 3, 35, [
    r"Imitate the proof of the fundamental theorem, one side at a time, with $f(x^+)$ in place of $f(x)$.",
    r"The obstacle: the estimate $\abs{f(t) - f(x^+)} < \eps$ holds on $(x, x+h]$ but perhaps not at $t = x$. Split $[x,x+h]$ into a tiny piece $[x, x+\eta]$, where $f$ is merely bounded, and the rest, and let $\eta$ be arbitrarily small.",
], ["c3-thm-ftc", "c3-thm-integral-additive", "c3-def-integral-conventions", "c3-thm-integral-monotone", "c3-thm-integral-linear", "c3-thm-integrable-bounded"]))

B.append(ex("c3-ex-square-integrable-not-integrable", "Integrability of $\\abs{f}$ or $f^2$ does not give integrability of $f$", r"""
Prove or disprove: if $f : [a,b] \to \R$ and $\abs{f}$ is integrable, then $f$ is integrable. Prove or disprove the same statement with $f^2$ in place of $\abs{f}$.
""", r"""
Both statements are false. Let $f : [a,b] \to \R$ be $1$ at rational points and $-1$ at irrational points. Then $\abs{f} = f^2 = 1$ is a constant function, hence integrable. If $f$ were integrable, then by linearity so would be $\tfrac12(f + 1)$, which is $1$ at rational points and $0$ at irrational points, that is, the indicator function of the rationals. But that function is not integrable. So $f$ is not integrable, although $\abs{f}$ and $f^2$ are.

(In the other direction, $f$ integrable does imply $\abs{f}$ and $f^2$ integrable, as continuous functions of an integrable function.)
""", 1, 10, [
    r"Modify the indicator function of the rationals so that its absolute value is constant.",
], ["c3-ex-dirichlet", "c3-thm-integral-linear", "c3-thm-integral-monotone", "c3-cor-composite-integrable"]))

# ── Series ───────────────────────────────────────────────────────────────────

B.append(ex("c3-ex-positive-negative-parts", "Positive and negative parts of a series", r"""
For $u \in \R$ put $u^+ = \max\set{u, 0}$ and $u^- = \max\set{-u, 0}$, so that $u^+, u^- \ge 0$, $u = u^+ - u^-$ and $\abs{u} = u^+ + u^-$. Let $\sum a_k$ be a series.
\begin{enumerate}
\item $\sum a_k$ converges absolutely if and only if $\sum a_k^+$ and $\sum a_k^-$ both converge.
\item If $\sum a_k$ converges conditionally, then $\sum a_k^+$ and $\sum a_k^-$ both diverge; indeed their partial sums tend to $+\infty$ (for every $K$ they exceed $K$ from some index on).
\end{enumerate}
""", r"""
(1) Suppose $\sum \abs{a_k}$ converges. Since $0 \le a_k^+ \le \abs{a_k}$ and $0 \le a_k^- \le \abs{a_k}$ for every $k$, the comparison test shows that $\sum a_k^+$ and $\sum a_k^-$ converge. Conversely, if both converge, then $\sum \abs{a_k} = \sum (a_k^+ + a_k^-)$ converges, since a sum of two convergent series converges.

(2) Suppose $\sum a_k$ converges conditionally. If $\sum a_k^+$ converged, then $\sum a_k^- = \sum (a_k^+ - a_k)$ would converge, as the difference of two convergent series, and by (1) $\sum a_k$ would converge absolutely, contrary to assumption. So $\sum a_k^+$ diverges; by the same argument with the roles exchanged ($a_k^+ = a_k^- + a_k$), $\sum a_k^-$ diverges. The terms $a_k^+$ are nonnegative, so the partial sums of $\sum a_k^+$ form a nondecreasing sequence, which is unbounded above because the series diverges. A nondecreasing sequence that is unbounded above tends to $+\infty$: given $K$, some partial sum exceeds $K$, and all later ones are at least as large. Likewise for $\sum a_k^-$.
""", 2, 15, [
    r"$a^\pm \le \abs{a}$, and $\abs{a} = a^+ + a^-$, $a = a^+ - a^-$. Compare, and use linearity.",
], ["c3-def-absolute-convergence", "c3-thm-comparison-test", "c3-cor-terms-to-zero", "c3-lem-nonnegative-series"]))

B.append(ex("c3-ex-bounded-multiplier", "Absolute convergence survives bounded multipliers; conditional convergence does not", r"""
\begin{enumerate}
\item If $\sum a_k$ converges absolutely and $(b_k)$ is a bounded sequence, then $\sum a_k b_k$ converges absolutely.
\item If $\sum a_k$ converges absolutely, then $\sum a_k^2$ converges.
\item Both statements fail for conditionally convergent series: with $a_k = (-1)^{k+1}/\sqrt{k}$ the series $\sum a_k$ converges, but $\sum a_k^2$ diverges, and so does $\sum a_k b_k$ for the bounded sequence $b_k = (-1)^{k+1}$. (Use the standard properties of real powers, as in the $p$-series exercise.)
\end{enumerate}
""", r"""
(1) Let $\abs{b_k} \le B$ for all $k$. Then $\abs{a_k b_k} \le B\abs{a_k}$, and $\sum B\abs{a_k}$ converges, being a constant multiple of the convergent series $\sum \abs{a_k}$. By the comparison test $\sum \abs{a_k b_k}$ converges.

(2) Since $\sum \abs{a_k}$ converges, $\abs{a_k} \to 0$, so the sequence $(a_k)$ is bounded (a convergent sequence is bounded). Apply (1) with $b_k = a_k$.

(3) Put $c_k = k^{-1/2} = 1/\sqrt{k}$. Then $c_k > 0$; $(c_k)$ is nonincreasing, because $\sqrt{k} = k^{1/2}$ is nondecreasing in $k$; and $c_k \to 0$, because given $\eps > 0$ we have $c_k^2 = 1/k < \eps^2$, hence $c_k < \eps$, for all $k > 1/\eps^2$. So the alternating series test shows that $\sum a_k = \sum (-1)^{k+1} c_k$ converges. But $a_k^2 = 1/k$, and the harmonic series diverges; and $a_k b_k = c_k = 1/k^{1/2}$, which is the $p$-series with $p = 1/2 \le 1$, and it diverges.
""", 2, 20, [
    r"For (1) and (2), compare with $B\abs{a_k}$.",
    r"For (3), the alternating series test applies to $\sum (-1)^{k+1}/\sqrt{k}$, and its termwise square is the harmonic series.",
], ["c3-thm-comparison-test", "c3-cor-terms-to-zero", "c3-thm-alternating-series", "c3-ex-harmonic", "c3-ex-p-series", "c3-def-absolute-convergence"]))

B.append(ex("c3-ex-terms-decay-faster", "Monotone terms of a convergent series decay faster than $1/k$", r"""
Let $a_1 \ge a_2 \ge a_3 \ge \dots \ge 0$ and suppose that $\sum a_k$ converges. Then $k\,a_k \to 0$ as $k \to \infty$.
""", r"""
Let $\eps > 0$. By the Cauchy convergence criterion there is an $N \ge 1$ such that $\sum_{k=n}^{m} a_k < \eps$ whenever $m \ge n \ge N$ (the terms are nonnegative, so the absolute value is the sum itself).

Let $n \ge N$. The block $a_{n+1} + \dots + a_{2n}$ has $n$ terms, each at least $a_{2n}$ because the sequence is nonincreasing, and $2n \ge n + 1 \ge N$; so
\[ n\,a_{2n} \ \le\ \sum_{k=n+1}^{2n} a_k \ <\ \eps, \qquad\text{hence}\qquad 2n\,a_{2n} < 2\eps . \]
For the odd indices, since $a_{2n+1} \le a_{2n}$ and $2n + 1 \le 3n$ for $n \ge 1$,
\[ (2n+1)\,a_{2n+1} \ \le\ 3n\,a_{2n} \ <\ 3\eps . \]
Thus $k\,a_k < 3\eps$ for every $k \ge 2N$, which proves $k\,a_k \to 0$.
""", 3, 25, [
    r"The terms are nonincreasing, so the block $a_{n+1} + \dots + a_{2n}$ is at least $n\,a_{2n}$.",
    r"The Cauchy criterion makes that block small. Handle odd indices by comparison with the preceding even one.",
], ["c3-thm-series-cauchy", "c3-cor-terms-to-zero"]))

B.append(ex("c3-ex-cauchy-condensation", "Cauchy's condensation test", r"""
Let $a_1 \ge a_2 \ge a_3 \ge \dots \ge 0$. Then
\[ \sum_{k=1}^\infty a_k \ \text{ converges} \quad\Longleftrightarrow\quad \sum_{j=0}^\infty 2^j a_{2^j} = a_1 + 2a_2 + 4a_4 + 8a_8 + \cdots \ \text{ converges.} \]
Deduce again that $\sum 1/k^p$ converges if and only if $p > 1$. (Use the standard properties of real powers, as in the $p$-series exercise, including that $2^s < 1$ exactly when $s < 0$.)
""", r"""
Write $A_n = \sum_{k=1}^n a_k$ and $B_J = \sum_{j=0}^J 2^j a_{2^j}$. Both series have nonnegative terms, so each converges if and only if its partial sums are bounded above.

\emph{The condensed series controls the original one.} Let $n \ge 1$ and choose $J$ with $n < 2^{J+1}$. For $0 \le j \le J$ the block of indices $2^j \le k \le 2^{j+1} - 1$ has $2^j$ terms, each at most $a_{2^j}$ since the sequence is nonincreasing. Hence
\[ A_n \ \le\ \sum_{j=0}^{J} \ \sum_{k=2^j}^{2^{j+1}-1} a_k \ \le\ \sum_{j=0}^J 2^j a_{2^j} = B_J . \]
So if the $B_J$ are bounded above by $B$, then every $A_n \le B$ and $\sum a_k$ converges.

\emph{The original series controls the condensed one.} Let $J \ge 1$. For $1 \le j \le J$ the block of indices $2^{j-1} + 1 \le k \le 2^j$ has $2^{j-1}$ terms, each at least $a_{2^j}$. Hence
\[ A_{2^J} \ =\ a_1 + \sum_{j=1}^{J} \ \sum_{k=2^{j-1}+1}^{2^j} a_k \ \ge\ a_1 + \sum_{j=1}^J 2^{j-1} a_{2^j} \ =\ a_1 + \tfrac12 \bigl(B_J - a_1\bigr) \ \ge\ \tfrac12 B_J . \]
So if the $A_n$ are bounded above by $A$, then every $B_J \le 2A$ and the condensed series converges.

\emph{The $p$-series.} If $p \le 0$ then $-p \ge 0$, so $k^{-p}$ is nondecreasing in $k$ and $1/k^p = k^{-p} \ge 1$ for all $k$; the terms do not tend to $0$ and the series diverges. If $p > 0$ the terms $a_k = 1/k^p$ are positive and nonincreasing, since $k^p$ is nondecreasing in $k$. The condensed series has terms
\[ 2^j a_{2^j} = 2^j \cdot 2^{-jp} = \bigl(2^{1-p}\bigr)^j , \]
so it is the geometric series with ratio $\lambda = 2^{1-p} > 0$, which converges if and only if $\lambda < 1$, that is, if and only if $1 - p < 0$. By the condensation test, $\sum 1/k^p$ converges if and only if $p > 1$.
""", 3, 35, [
    r"Both series have nonnegative terms: compare partial sums.",
    r"Group the terms of $\sum a_k$ into blocks $2^j \le k < 2^{j+1}$; each block is at most $2^j a_{2^j}$. For the reverse, use blocks $2^{j-1} < k \le 2^j$, each at least $2^{j-1}a_{2^j}$.",
], ["c3-lem-nonnegative-series", "c3-thm-geometric-series", "c3-cor-terms-to-zero", "c3-ex-p-series"]))

B.append(ex("c3-ex-root-below-ratio", "The root test is at least as strong as the ratio test", r"""
Let $a_k \neq 0$ for all $k$. Then
\[ \limsup_{k \to \infty} \abs{a_k}^{1/k} \ \le\ \limsup_{k \to \infty} \abs{\frac{a_{k+1}}{a_k}} . \]
Consequently, whenever the ratio test proves absolute convergence, so does the root test. (You may use that $C^{1/k} \to 1$ as $k \to \infty$ for every constant $C > 0$, and that $u \mapsto u^{1/k}$ is nondecreasing on $[0,\infty)$.)
""", r"""
Let $\rho = \limsup \abs{a_{k+1}/a_k}$ and $\alpha = \limsup \abs{a_k}^{1/k}$. If $\rho = +\infty$ there is nothing to prove. Otherwise $\rho \ge 0$, since all the ratios are nonnegative and so are the suprema defining $\rho$. Let $r > \rho$ be arbitrary; then $r > 0$.

By the first property of the limit superior there is an $N$ with $\abs{a_{k+1}/a_k} < r$, that is $\abs{a_{k+1}} \le r\abs{a_k}$, for all $k \ge N$. By induction on $k$,
\[ \abs{a_k} \le \abs{a_N}\, r^{k-N} = C r^k \qquad (k \ge N), \qquad C = \abs{a_N}\, r^{-N} > 0 . \]
Taking $k$-th roots, which preserves the inequality, $\abs{a_k}^{1/k} \le C^{1/k}\, r$ for $k \ge N$.

Let $\eta > 0$. Since $C^{1/k} \to 1$, there is an $N' \ge N$ with $C^{1/k} < 1 + \eta$ for all $k \ge N'$, and then $\abs{a_k}^{1/k} < (1+\eta)\, r$ for all $k \ge N'$. So $\sup\set{\abs{a_k}^{1/k} : k \ge N'} \le (1+\eta)r$, and since $\alpha$ is the infimum over $n$ of the suprema $\sup\set{\abs{a_k}^{1/k} : k \ge n}$, we get $\alpha \le (1 + \eta) r$. As $\eta > 0$ was arbitrary, $\alpha \le r$; and as $r > \rho$ was arbitrary, $\alpha \le \rho$.

If the ratio test proves absolute convergence, then $\rho < 1$, so $\alpha \le \rho < 1$ and the root test proves it too.
""", 3, 30, [
    r"If $r > \limsup \abs{a_{k+1}/a_k}$, then $\abs{a_{k+1}} \le r \abs{a_k}$ from some index $N$ on, so $\abs{a_k} \le C r^k$ for $k \ge N$.",
    r"Take $k$-th roots: $\abs{a_k}^{1/k} \le C^{1/k} r$, and $C^{1/k} \to 1$. Conclude $\limsup \abs{a_k}^{1/k} \le r$ for every $r > \rho$.",
], ["c3-def-limsup", "c3-thm-root-test", "c3-thm-ratio-test", "c3-rem-root-ratio"]))

B.append(ex("c3-ex-dirichlet-test", "Dirichlet's test", r"""
Let $(a_k)$ be a nonincreasing sequence with $a_k \to 0$, and let $(b_k)$ be a sequence whose partial sums $B_n = b_1 + \dots + b_n$ are bounded, say $\abs{B_n} \le B$ for all $n$. Then $\sum a_k b_k$ converges. (The alternating series test is the case $b_k = (-1)^{k+1}$.)
""", r"""
\emph{The $a_k$ are nonnegative.} If $a_j < 0$ for some $j$, then $a_k \le a_j < 0$ for all $k \ge j$, so $a_k$ could not tend to $0$. Hence $a_k \ge 0$ for all $k$, and $a_k - a_{k+1} \ge 0$.

\emph{Summation by parts.} Put $B_0 = 0$, so that $b_k = B_k - B_{k-1}$ for all $k \ge 1$. For $m \ge n \ge 1$,
\begin{align*}
\sum_{k=n}^{m} a_k b_k &= \sum_{k=n}^{m} a_k B_k - \sum_{k=n}^{m} a_k B_{k-1} = \sum_{k=n}^{m} a_k B_k - \sum_{k=n-1}^{m-1} a_{k+1} B_k \\
&= a_m B_m - a_n B_{n-1} + \sum_{k=n}^{m-1} (a_k - a_{k+1})\, B_k ,
\end{align*}
where the second sum was reindexed by $k \mapsto k+1$, and then the terms with $n \le k \le m-1$ were collected.

\emph{The estimate.} Using $\abs{B_k} \le B$, $a_k \ge 0$ and $a_k - a_{k+1} \ge 0$,
\[ \abs{\sum_{k=n}^{m} a_k b_k} \le a_m B + a_n B + B \sum_{k=n}^{m-1} (a_k - a_{k+1}) = a_m B + a_n B + B(a_n - a_m) = 2B\,a_n , \]
the sum telescoping to $a_n - a_m$.

\emph{Convergence.} Let $\eps > 0$. Since $a_n \to 0$, there is an $N$ with $a_n < \eps/(2B + 1)$ for all $n \ge N$. Then for $m \ge n \ge N$, $\abs{\sum_{k=n}^m a_k b_k} \le 2B a_n < \eps$. By the Cauchy convergence criterion, $\sum a_k b_k$ converges.

For $b_k = (-1)^{k+1}$ the partial sums $B_n$ are $1$ for odd $n$ and $0$ for even $n$, so they are bounded by $1$, and the test recovers the convergence statement of the alternating series test.
""", 3, 45, [
    r"Aim for the Cauchy criterion: bound $\sum_{k=n}^m a_k b_k$ by a multiple of $a_n$.",
    r"Summation by parts: writing $b_k = B_k - B_{k-1}$ and regrouping, $\sum_{k=n}^m a_k b_k = a_m B_m - a_n B_{n-1} + \sum_{k=n}^{m-1}(a_k - a_{k+1})B_k$.",
    r"Every $a_k - a_{k+1}$ is nonnegative, and their sum telescopes. So the whole thing is bounded by $2B a_n$.",
], ["c3-thm-series-cauchy", "c3-thm-alternating-series", "c3-def-series"]))

B.append(ex("c3-ex-riemann-rearrangement-proof", "Riemann's rearrangement theorem, proved", r"""
Let $\sum a_k$ converge conditionally and let $s \in \R$. Then there is a bijection $\beta : \N \to \N$ such that the rearrangement $\sum_{j=1}^\infty a_{\beta(j)}$ converges to $s$.
""", r"""
\emph{The nonnegative and the negative terms.} Let $P = \set{k \in \N : a_k \ge 0}$ and $Q = \set{k \in \N : a_k < 0}$. Write $a_k^+ = \max\set{a_k,0}$ and $a_k^- = \max\set{-a_k,0}$ as in the exercise on positive and negative parts; since $\sum a_k$ converges conditionally, the partial sums of $\sum a_k^+$ and of $\sum a_k^-$ both tend to $+\infty$. In particular $P$ is infinite: if it were finite, $a_k^+ = 0$ for all large $k$ and $\sum a_k^+$ would converge. Likewise $Q$ is infinite. List $P$ in increasing order as $k_1 < k_2 < \cdots$ and $Q$ as $l_1 < l_2 < \cdots$, and put $p_i = a_{k_i} \ge 0$ and $q_i = a_{l_i} < 0$. Then
\[ \sum_{i=1}^{I} p_i = \sum_{k=1}^{k_I} a_k^+ \qquad\text{and}\qquad \sum_{i=1}^{I} q_i = -\sum_{k=1}^{l_I} a_k^- , \]
because $a_k^+ = a_k$ for $k \in P$ and $a_k^+ = 0$ for $k \in Q$, and symmetrically for $a_k^-$. Since $k_I \ge I$ and $l_I \ge I$, as $I \to \infty$ the first sum tends to $+\infty$ and the second to $-\infty$. The same holds for the sums $\sum_{i=i_0+1}^{I} p_i$ and $\sum_{i=i_0+1}^{I} q_i$ for any fixed $i_0$, since these differ from the full sums by constants. Finally $p_i \to 0$ and $q_i \to 0$, since $a_k \to 0$ (the terms of a convergent series tend to zero) and these are subsequences of $(a_k)$.

\emph{The greedy rearrangement.} Define $\beta(1), \beta(2), \dots$ inductively, together with the sums $S_n = \sum_{j=1}^{n} a_{\beta(j)}$, $S_0 = 0$. Suppose $\beta(1),\dots,\beta(n)$ have been chosen, distinct. If $S_n \le s$, let $\beta(n+1)$ be the least element of $P$ not among $\beta(1),\dots,\beta(n)$; call step $n+1$ a \emph{$P$-step}. If $S_n > s$, let $\beta(n+1)$ be the least element of $Q$ not among $\beta(1),\dots,\beta(n)$; a \emph{$Q$-step}. These least elements exist because $P$ and $Q$ are infinite. By construction $\beta$ is injective. Since each $P$-step takes the least unused element of $P$, the $i$-th $P$-step uses the index $k_i$ and adds $p_i$ to the sum; the $i$-th $Q$-step uses $l_i$ and adds $q_i$.

\emph{Both kinds of step occur infinitely often.} Suppose there were only finitely many $Q$-steps, the last one at step $n_0$ (or $n_0 = 0$ if there is none). Then every step after $n_0$ is a $P$-step, which means $S_n \le s$ for every $n \ge n_0$. But if $i_0$ is the number of $P$-steps among the first $n_0$, then $S_{n_0 + t} = S_{n_0} + p_{i_0+1} + \dots + p_{i_0+t}$, which tends to $+\infty$ as $t \to \infty$, contradicting $S_n \le s$. Suppose instead there were only finitely many $P$-steps, the last at step $n_0$. Then $S_n > s$ for all $n \ge n_0$, while $S_{n_0+t} = S_{n_0} + q_{i_0+1} + \dots + q_{i_0+t} \to -\infty$, a contradiction.

\emph{$\beta$ is a bijection.} Since there are infinitely many $P$-steps, the $i$-th $P$-step exists for every $i$, and it uses $k_i$; so every element of $P$ is a value of $\beta$. Likewise every element of $Q$ is. Hence $\beta : \N \to \N$ is surjective, and so a bijection, and $\sum_j a_{\beta(j)}$ is a rearrangement of $\sum a_k$ whose $n$-th partial sum is $S_n$.

\emph{The partial sums converge to $s$.} Let $\eps > 0$. Since $a_k \to 0$, there is a $K$ with $\abs{a_k} < \eps$ for all $k \ge K$. Since $\beta$ is injective, $\beta(n) < K$ for at most $K - 1$ values of $n$; let $n_1$ exceed all of them, so that $\abs{a_{\beta(n)}} < \eps$ for every $n \ge n_1$.

Because both kinds of step occur infinitely often, there are infinitely many $n$ such that step $n$ is a $P$-step and step $n+1$ is a $Q$-step: otherwise, from some step on, no $P$-step would be followed by a $Q$-step, so after the first $P$-step beyond that point all steps would be $P$-steps, leaving only finitely many $Q$-steps. Choose such an $n_2 \ge n_1$. Step $n_2$ being a $P$-step means $S_{n_2 - 1} \le s$, and step $n_2 + 1$ being a $Q$-step means $S_{n_2} > s$. Since $S_{n_2} = S_{n_2 - 1} + a_{\beta(n_2)}$ with $0 \le a_{\beta(n_2)} < \eps$,
\[ s < S_{n_2} < s + \eps . \]

We now show by induction that $s - \eps < S_m < s + \eps$ for every $m \ge n_2$. The case $m = n_2$ was just done. Suppose it holds for some $m \ge n_2$. If $S_m \le s$, then step $m+1$ is a $P$-step, so $S_{m+1} = S_m + a_{\beta(m+1)}$ with $0 \le a_{\beta(m+1)} < \eps$ (as $m + 1 > n_1$); hence $s - \eps < S_m \le S_{m+1} < s + \eps$. If $S_m > s$, then step $m+1$ is a $Q$-step, so $-\eps < a_{\beta(m+1)} < 0$, and $s - \eps < S_{m+1} < S_m < s + \eps$. This completes the induction.

Thus $\abs{S_m - s} < \eps$ for all $m \ge n_2$. As $\eps$ was arbitrary, $S_m \to s$: the rearrangement $\sum_j a_{\beta(j)}$ converges to $s$.
""", 5, 150, [
    r"Separate the nonnegative terms $p_1, p_2, \dots$ from the negative terms $q_1, q_2, \dots$, each in their original order. By the exercise on positive and negative parts, $\sum p_i$ has partial sums tending to $+\infty$ and $\sum q_i$ to $-\infty$; and $p_i, q_i \to 0$.",
    r"Build the rearrangement greedily: whenever the running sum is at most $s$, append the next unused $p_i$; whenever it exceeds $s$, append the next unused $q_i$. Show both kinds of step happen infinitely often, so every term is eventually used.",
    r"Once every term being appended has absolute value below $\eps$, and the running sum has just crossed $s$, it can never again leave $(s - \eps, s + \eps)$: a step upward happens only from at most $s$, a step downward only from above $s$.",
], ["c3-thm-riemann-rearrangement", "c3-rem-riemann-rearrangement", "c3-def-rearrangement", "c3-def-absolute-convergence", "c3-cor-terms-to-zero", "c3-lem-nonnegative-series", "c3-ex-positive-negative-parts"]))

write("3-exercises", B, [])
