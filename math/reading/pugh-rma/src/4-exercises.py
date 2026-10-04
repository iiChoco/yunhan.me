"""End-of-chapter exercises for Chapter 4 (Function Spaces): sections/4-exercises.json."""
import json, os

OUT = "/Users/choco/Projects/yunhan.me/math/reading/pugh-rma/sections/4-exercises.json"

blocks = []


def prose(bid, tex):
    blocks.append({"id": bid, "kind": "prose", "number": "", "tex": tex.strip()})


def ex(bid, title, tex, proof, difficulty, minutes, hints, uses):
    blocks.append({"id": bid, "kind": "exercise", "number": "", "title": title,
                   "tex": tex.strip(), "proof": proof.strip(),
                   "difficulty": difficulty, "minutes": minutes,
                   "hints": [h.strip() for h in hints], "uses": list(uses),
                   "optional": True})


prose("c4-exercises-intro", r"""
These exercises are extra credit: none of them gates the chapter, and they may be taken in any order. They range from unwinding a definition to results that a first course would state as theorems, and everything they need is in the five sections before them, apart from a few facts of Chapters 1–3 (the ratio and alternating series tests, the mean value theorem, the antiderivative theorem, countability of $\Q$) that are named where they are used.
""")

# ── Uniform convergence ──────────────────────────────────────────────────────

ex("c4-ex-sums-and-products", "Sums and products of uniformly convergent sequences", r"""
Let $X$ be a nonempty set and suppose $f_n \rightrightarrows f$ and $g_n \rightrightarrows g$ on $X$.
\begin{enumerate}
\item $f_n + g_n \rightrightarrows f + g$ on $X$.
\item If every $f_n$ and every $g_n$ belongs to $C_b(X)$, then $f_n g_n \rightrightarrows fg$ on $X$.
\item Prove or disprove: (2) holds without the boundedness assumption.
\end{enumerate}
""", r"""
(1) Let $\eps > 0$. Choose $N_1$ with $\abs{f_n(x) - f(x)} < \eps/2$ for $n \ge N_1$ and all $x$, and $N_2$ likewise for $g_n$ and $g$. For $n \ge \max(N_1,N_2)$ and every $x \in X$,
\[ \abs{(f_n + g_n)(x) - (f+g)(x)} \le \abs{f_n(x) - f(x)} + \abs{g_n(x) - g(x)} < \eps . \]

(2) First, $f \in C_b(X)$: choose $N$ with $\abs{f_N(x) - f(x)} < 1$ for all $x$; then $\abs{f(x)} < 1 + \norm{f_N}$ for all $x$. Likewise $g \in C_b(X)$. Since convergence in the sup metric is uniform convergence, $\norm{f_n - f} \to 0$ and $\norm{g_n - g} \to 0$. Choose $N'$ with $\norm{f_n - f} \le 1$ for $n \ge N'$ and put $B = \max(\norm{f_1}, \dots, \norm{f_{N'-1}}, \norm{f} + 1)$; then $\norm{f_n} \le B$ for every $n$, because for $n \ge N'$, $\norm{f_n} \le \norm{f} + \norm{f_n - f}$ by the triangle inequality for the sup norm. Now write $f_n g_n - fg = f_n(g_n - g) + (f_n - f)g$ and use the properties of the sup norm:
\[ \norm{f_n g_n - fg} \le \norm{f_n}\,\norm{g_n - g} + \norm{f_n - f}\,\norm{g} \le B\,\norm{g_n - g} + \norm{g}\,\norm{f_n - f} \to 0 . \]
So $f_n g_n \to fg$ in the sup metric, which is the same as $f_n g_n \rightrightarrows fg$.

(3) False. Take $X = \R$, $f_n(x) = x$ and $g_n(x) = 1/n$. Then $f_n \rightrightarrows f$ with $f(x) = x$ (the difference is $0$), and $g_n \rightrightarrows 0$ because $\abs{1/n - 0} < \eps$ for $n > 1/\eps$ independently of $x$. The products $f_n g_n (x) = x/n$ converge pointwise to $0 = f(x) \cdot 0$, so $0$ is the only candidate for a uniform limit. But for $\eps = 1$ and any $N$, the point $x = N$ gives $\abs{f_N(x) g_N(x) - 0} = N/N = 1$, which is not less than $\eps$. So the convergence is not uniform on $\R$.
""", 2, 20, [
    r"For (2) reduce to the sup norm: $\norm{f_ng_n - fg} \le \norm{f_n}\norm{g_n - g} + \norm{f_n - f}\norm{g}$. You will need the sequence $(\norm{f_n})$ to be bounded, and $f$ and $g$ to be bounded.",
    r"For (3), look for a counterexample on $\R$ in which one sequence is unbounded and the other tends to $0$ uniformly but slowly.",
], ["c4-def-uniform", "c4-def-sup-norm", "c4-prop-sup-norm", "c4-thm-sup-metric-uniform"])

ex("c4-ex-dini", "Dini's theorem: monotone pointwise convergence on a compact space is uniform", r"""
Let $M$ be a compact metric space and let $f_n : M \to \R$ $(n \in \N)$ and $f : M \to \R$ be continuous. Suppose $f_n(x) \ge f_{n+1}(x)$ for all $n$ and all $x \in M$, and $f_n \to f$ pointwise on $M$.
\begin{enumerate}
\item $f_n \rightrightarrows f$ on $M$.
\item Compactness of $M$ cannot be dropped: give a decreasing sequence of continuous functions on $[0,1)$ converging pointwise to a continuous function but not uniformly.
\end{enumerate}
""", r"""
(1) Put $g_n = f_n - f$, a continuous function on $M$. For fixed $x$ and $m \le n$ we have $f_m(x) \ge f_n(x)$; letting $n \to \infty$ gives $f_m(x) \ge f(x)$. So $g_m \ge 0$, and $g_n \ge g_{n+1}$ because $f_n \ge f_{n+1}$. Also $g_n(x) \to 0$ for every $x$.

Suppose the convergence is not uniform. Then there is an $\eps > 0$ such that for every $N$ there are $n \ge N$ and $x \in M$ with $\abs{g_n(x)} \ge \eps$, that is $g_n(x) \ge \eps$. Choose such a pair $(n_1, x_1)$ for $N = 1$, then, having chosen $(n_k, x_k)$, a pair $(n_{k+1}, x_{k+1})$ for $N = n_k + 1$. This gives $n_1 < n_2 < \cdots$ and points $x_k \in M$ with $g_{n_k}(x_k) \ge \eps$ for all $k$.

By compactness some subsequence $(x_{k_j})$ converges to a point $p \in M$. Fix $m \in \N$. For all $j$ large enough that $n_{k_j} \ge m$, monotonicity gives
\[ g_m(x_{k_j}) \ge g_{n_{k_j}}(x_{k_j}) \ge \eps . \]
Since $g_m$ is continuous at $p$, $g_m(p) = \lim_{j} g_m(x_{k_j}) \ge \eps$. This holds for every $m$, so $g_m(p) \ge \eps$ for all $m$, contradicting $g_m(p) \to 0$. Hence $g_n \rightrightarrows 0$, i.e. $f_n \rightrightarrows f$.

(2) On $[0,1)$ let $f_n(x) = x^n$. Each $f_n$ is continuous, $x^{n} \ge x^{n+1}$ for $x \in [0,1)$, and $f_n \to 0$ pointwise, the limit $0$ being continuous. By the exercise on the powers $x^n$ the convergence is not uniform on $[0,1)$.
""", 3, 40, [
    r"Replace $f_n$ by $g_n = f_n - f$, which decreases pointwise to $0$. Argue by contradiction: if the convergence is not uniform, find indices $n_k \to \infty$ and points $x_k$ with $g_{n_k}(x_k) \ge \eps$.",
    r"Pass to a convergent subsequence $x_{k_j} \to p$. For a fixed $m$, once $n_{k_j} \ge m$ you have $g_m(x_{k_j}) \ge g_{n_{k_j}}(x_{k_j}) \ge \eps$; now use continuity of the single function $g_m$ at $p$.",
    r"For (2), $x^n$ on $[0,1)$ is already in the chapter.",
], ["c4-def-pointwise", "c4-def-uniform", "c4-ex-xn"])

ex("c4-ex-sine-series", "A trigonometric series that can be differentiated and integrated term by term", r"""
Let $S(x) = \displaystyle\sum_{k=1}^\infty \frac{\sin(kx)}{k^3}$ for $x \in \R$. (Recall from Chapter 3 that $\sum 1/k^2$ and $\sum 1/k^3$ converge.)
\begin{enumerate}
\item The series converges uniformly on $\R$ and $S$ is continuous on $\R$.
\item $S$ is differentiable on $\R$ with $S'(x) = \displaystyle\sum_{k=1}^\infty \frac{\cos(kx)}{k^2}$, and $S'$ is continuous.
\item $\displaystyle\int_0^\pi S(x)\,dx = \sum_{k \text{ odd}} \frac{2}{k^4} = 2 + \frac{2}{3^4} + \frac{2}{5^4} + \cdots$.
\end{enumerate}
""", r"""
Let $f_k(x) = \sin(kx)/k^3$, a differentiable function on $\R$ with $f_k'(x) = \cos(kx)/k^2$.

(1) For all $x \in \R$, $\abs{f_k(x)} \le 1/k^3 =: M_k$ and $\sum M_k$ converges, so by the Weierstrass M-test $\sum f_k$ converges uniformly on $\R$. Each partial sum $S_n = \sum_{k=1}^n f_k$ is continuous on $\R$ and $S_n \rightrightarrows S$, so $S$ is continuous as a uniform limit of continuous functions (the theorem applies to any metric space, here $\R$).

(2) Likewise $\abs{f_k'(x)} \le 1/k^2$ for all $x$ and $\sum 1/k^2$ converges, so $\sum f_k'$ converges uniformly on $\R$, to some function $G$, which is continuous by the same argument as in (1). Fix $x_0 \in \R$ and consider the interval $[a,b] = [x_0 - 1, x_0 + 1]$. On it $\sum f_k$ converges (pointwise, even uniformly) to $S$ and $\sum f_k'$ converges uniformly to $G$, so by term-by-term differentiation $S$ is differentiable on $[a,b]$ with $S' = G$ there. Since $x_0$ is an interior point of $[a,b]$, the derivative at $x_0$ is the ordinary two-sided derivative, and $S'(x_0) = G(x_0) = \sum_k \cos(kx_0)/k^2$. As $x_0$ was arbitrary, (2) holds.

(3) On $[0,\pi]$ the series $\sum f_k$ converges uniformly to $S$ and each $f_k$ is continuous, hence Riemann integrable. By term-by-term integration
\[ \int_0^\pi S(x)\,dx = \sum_{k=1}^\infty \int_0^\pi \frac{\sin(kx)}{k^3}\,dx . \]
Since $x \mapsto -\cos(kx)/k$ is an antiderivative of $\sin(kx)$, the fundamental theorem of calculus gives $\int_0^\pi \sin(kx)\,dx = \frac{1 - \cos(k\pi)}{k} = \frac{1 - (-1)^k}{k}$, which is $0$ for even $k$ and $2/k$ for odd $k$. Dividing by $k^3$, the $k$-th integral is $0$ for even $k$ and $2/k^4$ for odd $k$, which is the claimed sum.
""", 2, 20, [
    r"The M-test with $M_k = 1/k^3$ handles (1); with $M_k = 1/k^2$ it handles the series of derivatives in (2).",
    r"The term-by-term theorems are stated on a closed interval $[a,b]$; for (2) trap each point inside one, and for (3) use $[0,\pi]$.",
], ["c4-thm-m-test", "c4-thm-uniform-limit-continuous", "c4-thm-term-differentiation", "c4-thm-term-integration"])

ex("c4-ex-equicontinuous-pointwise-limit", "Equicontinuity turns pointwise convergence into uniform convergence", r"""
Let $M$ be a compact metric space and let $(f_n)$ be an equicontinuous sequence of functions $M \to \R$ that converges pointwise on $M$ to a function $f$.
\begin{enumerate}
\item $f_n \rightrightarrows f$ on $M$.
\item $f$ is uniformly continuous on $M$.
\item Equicontinuity cannot be dropped from (1): give a pointwise convergent sequence of continuous functions on $[0,1]$ that does not converge uniformly.
\end{enumerate}
""", r"""
(1) The set $D = M$ is dense in $M$, and $(f_n(x))$ converges for every $x \in D$. By the Arzelà–Ascoli propagation theorem $(f_n)$ converges uniformly on $M$ to some function $g$. A uniform limit is also a pointwise limit, and pointwise limits are unique, so $g = f$ and $f_n \rightrightarrows f$.

(2) Let $\eps > 0$. By equicontinuity there is a $\delta > 0$ such that $\abs{f_n(s) - f_n(t)} < \eps/2$ for all $n$ whenever $d(s,t) < \delta$. Fix such $s, t$ and let $n \to \infty$: since $f_n(s) \to f(s)$ and $f_n(t) \to f(t)$, and weak inequalities pass to limits, $\abs{f(s) - f(t)} \le \eps/2 < \eps$. So $f$ is uniformly continuous.

(3) $f_n(x) = x^n$ on $[0,1]$: continuous, pointwise convergent to the function that is $0$ on $[0,1)$ and $1$ at $1$, and not uniformly convergent, by the exercise on the powers $x^n$. (Consistently with (2), this sequence is not equicontinuous, and its limit is not even continuous.)
""", 2, 15, [
    r"The propagation theorem allows any dense subset $D$ of $M$. Which $D$ is available here?",
    r"For (2), fix $s, t$ closer than the $\delta$ of equicontinuity and let $n \to \infty$ in $\abs{f_n(s) - f_n(t)} < \eps$.",
], ["c4-thm-propagation", "c4-def-equicontinuous", "c4-def-uniform", "c4-ex-xn"])

# ── Power series ─────────────────────────────────────────────────────────────

ex("c4-ex-radius-computations", "Three radii of convergence", r"""
Find the radius of convergence of each series and decide whether it converges at the endpoints of its interval of convergence.
\begin{enumerate}
\item $\displaystyle\sum_{k=1}^\infty k^2 x^k$.
\item $\displaystyle\sum_{k=0}^\infty x^{k^2} = 1 + x + x^4 + x^9 + \cdots$.
\item $\displaystyle\sum_{k=0}^\infty 2^k x^{2k}$.
\end{enumerate}
""", r"""
In each case $R = 1/L$ with $L = \limsup_n \abs{c_n}^{1/n}$, where $c_n$ is the coefficient of $x^n$.

(1) $c_k = k^2$, so $\abs{c_k}^{1/k} = (k^{1/k})^2 \to 1$ because $k^{1/k} \to 1$. A convergent sequence has its limit as its limit superior, so $L = 1$ and $R = 1$. At $x = \pm 1$ the terms $k^2 (\pm1)^k$ have absolute value $k^2 \to \infty$, so they do not tend to $0$ and the series diverges at both endpoints.

(2) Here $c_n = 1$ if $n$ is a perfect square and $c_n = 0$ otherwise, so $\abs{c_n}^{1/n}$ is $1$ for infinitely many $n$ and $0$ for the rest. Hence $\sup_{n \ge m} \abs{c_n}^{1/n} = 1$ for every $m$, so $L = 1$ and $R = 1$. At $x = \pm1$ the nonzero terms are $(\pm1)^{k^2}$, of absolute value $1$, so the terms do not tend to $0$ and the series diverges at both endpoints.

(3) Here $c_n = 2^{n/2}$ for even $n$ and $c_n = 0$ for odd $n$, so $\abs{c_n}^{1/n} = \sqrt 2$ for even $n$ and $0$ for odd $n$. Thus $\sup_{n \ge m}\abs{c_n}^{1/n} = \sqrt2$ for every $m$, $L = \sqrt 2$, and $R = 1/\sqrt2$. At $x = \pm 1/\sqrt2$ every term is $2^k (1/2)^k = 1$, so the series diverges at both endpoints.
""", 2, 20, [
    r"Write each series as $\sum c_n x^n$ first: in (2) and (3) most of the $c_n$ are $0$, and the limit superior of a sequence that takes a value infinitely often is at least that value.",
    r"For (1) use $k^{1/k} \to 1$. At an endpoint, check whether the terms tend to $0$.",
], ["c4-def-power-series", "c4-thm-radius", "c4-lem-kth-root-k"])

ex("c4-ex-abel-theorem", "Abel's theorem: convergence at the endpoint is uniform up to the endpoint", r"""
Suppose the series of numbers $\sum_{k=0}^\infty c_k$ converges, with sum $s$.
\begin{enumerate}
\item The power series $\sum c_k x^k$ converges uniformly on $[0,1]$.
\item Its sum $f(x) = \sum_{k=0}^\infty c_k x^k$ is continuous on $[0,1]$; in particular $f(x) \to s$ as $x \to 1^-$.
\item Deduce that $\displaystyle\sum_{k=0}^\infty \frac{(-1)^k}{k+1} = \int_0^1 \frac{dt}{1+t}$. (The series on the left converges by the alternating series test of Chapter 3.)
\end{enumerate}
""", r"""
(1) Let $s_n = \sum_{k=0}^n c_k$, so $s_n \to s$, and let $S_n(x) = \sum_{k=0}^n c_k x^k$. We show $(S_n)$ is uniformly Cauchy on $[0,1]$. Let $\eps > 0$ and choose $N$ with $\abs{s_n - s} < \eps/4$ for all $n \ge N$, so that $\abs{s_k - s_n} < \eps/2$ for all $k, n \ge N$.

Fix $m > n \ge N$ and $x \in [0,1]$. Put $t_k = s_k - s_n$ for $k \ge n$; then $t_n = 0$, $\abs{t_k} < \eps/2$ for $k \ge n$, and $c_k = t_k - t_{k-1}$ for $k \ge n+1$. Summation by parts:
\[ S_m(x) - S_n(x) = \sum_{k=n+1}^m (t_k - t_{k-1})\,x^k = \sum_{k=n+1}^m t_k x^k - \sum_{k=n}^{m-1} t_k x^{k+1} = \sum_{k=n+1}^{m-1} t_k \,(x^k - x^{k+1}) + t_m x^m - t_n x^{n+1} , \]
and the last term is $0$ (for $m = n+1$ the middle sum is empty). Since $0 \le x \le 1$, every $x^k - x^{k+1}$ is $\ge 0$, and the sum of these differences telescopes:
\[ \abs{S_m(x) - S_n(x)} \le \frac{\eps}{2} \sum_{k=n+1}^{m-1} (x^k - x^{k+1}) + \frac{\eps}{2} x^m = \frac{\eps}{2}\,(x^{n+1} - x^m) + \frac{\eps}{2}\,x^m = \frac{\eps}{2}\,x^{n+1} \le \frac{\eps}{2} < \eps . \]
This holds for all $m > n \ge N$ and all $x \in [0,1]$ (and trivially for $m = n$), so $(S_n)$ is uniformly Cauchy on $[0,1]$. By the Cauchy criterion it converges uniformly on $[0,1]$; its limit is $f$.

(2) Each $S_n$ is a polynomial, hence continuous on $[0,1]$, and $S_n \rightrightarrows f$ there, so $f$ is continuous on $[0,1]$. At $x = 1$, $f(1) = \sum c_k = s$. Continuity at $1$ gives $f(x) \to f(1) = s$ as $x \to 1^-$.

(3) Put $d_0 = 0$ and $d_j = (-1)^{j-1}/j$ for $j \ge 1$, so that $\sum_{j \ge 0} d_j x^j = \sum_{k \ge 0} \frac{(-1)^k}{k+1} x^{k+1}$ (substitute $j = k+1$). The series $\sum d_j$ converges, by the alternating series test, to $\sum_{k \ge 0} (-1)^k/(k+1)$. By (2) its sum $g(x) = \sum d_j x^j$ is continuous on $[0,1]$ with $g(1) = \sum_{k\ge0} (-1)^k/(k+1)$. By the exercise on the logarithm series, $g(x) = \int_0^x \frac{dt}{1+t}$ for $0 \le x < 1$. The function $\Phi(x) = \int_0^x \frac{dt}{1+t}$ is continuous on $[0,1]$: for $0 \le x < y \le 1$, $\abs{\Phi(y) - \Phi(x)} = \int_x^y \frac{dt}{1+t} \le y - x$, since the integrand lies between $0$ and $1$. Therefore
\[ \sum_{k=0}^\infty \frac{(-1)^k}{k+1} = g(1) = \lim_{x \to 1^-} g(x) = \lim_{x \to 1^-} \Phi(x) = \Phi(1) = \int_0^1 \frac{dt}{1+t} . \]
""", 4, 60, [
    r"The M-test does not apply (the $c_k$ need not be absolutely summable). Prove instead that the partial sums are uniformly Cauchy on $[0,1]$.",
    r"Summation by parts: with $t_k = s_k - s_n$, write $c_k = t_k - t_{k-1}$ and regroup $\sum_{k=n+1}^m c_k x^k$ as a sum of $t_k (x^k - x^{k+1})$ plus a boundary term. The $t_k$ are small for $k \ge n \ge N$.",
    r"On $[0,1]$ the differences $x^k - x^{k+1}$ are nonnegative and telescope to $x^{n+1} - x^m \le 1$.",
], ["c4-def-series-functions", "c4-lem-uniform-cauchy", "c4-thm-uniform-limit-continuous", "c4-ex-log-series"])

ex("c4-ex-exponential-series", "The exponential series solves $y' = y$", r"""
Let $E(x) = \displaystyle\sum_{k=0}^\infty \frac{x^k}{k!}$.
\begin{enumerate}
\item The series has radius of convergence $R = \infty$, so $E$ is defined on all of $\R$.
\item $E$ is differentiable on $\R$ with $E' = E$, and $E(0) = 1$.
\item $E(x)\,E(-x) = 1$ for every $x \in \R$; in particular $E(x) \ne 0$ for all $x$.
\item If $g : \R \to \R$ is differentiable with $g' = g$, then $g = g(0)\,E$. So $E$ is the only solution of $y' = y$ with $y(0) = 1$.
\end{enumerate}
""", r"""
(1) For every real $x \ne 0$ the ratio of consecutive terms has absolute value $\abs{x}/(k+1) \to 0$, so the series converges for every real $x$ by the ratio test (as noted among the examples of radii). If the radius $R$ were finite, the series would diverge at $x = R + 1$ by the Cauchy–Hadamard theorem. Hence $R = \infty$.

(2) By term-by-term differentiation of power series (valid for every $x$, since $R = \infty$),
\[ E'(x) = \sum_{k=1}^\infty \frac{k\,x^{k-1}}{k!} = \sum_{k=1}^\infty \frac{x^{k-1}}{(k-1)!} = \sum_{j=0}^\infty \frac{x^j}{j!} = E(x) . \]
Also $E(0) = 1$, every term with $k \ge 1$ vanishing at $0$.

(3) Let $h(x) = E(x)E(-x)$. By the chain rule $\frac{d}{dx} E(-x) = -E'(-x) = -E(-x)$, so by the product rule
\[ h'(x) = E'(x)E(-x) - E(x)E(-x) = E(x)E(-x) - E(x)E(-x) = 0 . \]
A differentiable function on $\R$ with zero derivative is constant (mean value theorem), so $h(x) = h(0) = E(0)^2 = 1$ for all $x$. In particular $E(x) \ne 0$.

(4) Let $u(x) = g(x)E(-x)$. As in (3), $u'(x) = g'(x)E(-x) - g(x)E(-x) = g(x)E(-x) - g(x)E(-x) = 0$, so $u$ is constant: $u(x) = u(0) = g(0)E(0) = g(0)$. Multiplying $g(x)E(-x) = g(0)$ by $E(x)$ and using (3), $g(x) = g(x)E(-x)E(x) = g(0)E(x)$. If moreover $g(0) = 1$ then $g = E$.
""", 2, 25, [
    r"For (1), the ratio test gives convergence everywhere; what does Cauchy–Hadamard say if the radius were finite?",
    r"For (3) and (4), differentiate $E(x)E(-x)$ and $g(x)E(-x)$: both derivatives vanish, and a function with zero derivative is constant.",
], ["c4-def-power-series", "c4-thm-radius", "c4-ex-radius-examples", "c4-thm-ps-term-by-term"])

ex("c4-ex-even-odd-coefficients", "Even and odd power series", r"""
Let $\sum c_k x^k$ have radius of convergence $R > 0$ and sum $f(x)$ for $\abs{x} < R$.
\begin{enumerate}
\item If $f(-x) = f(x)$ for all $\abs{x} < R$, then $c_k = 0$ for every odd $k$.
\item If $f(-x) = -f(x)$ for all $\abs{x} < R$, then $c_k = 0$ for every even $k$.
\end{enumerate}
""", r"""
For $\abs{x} < R$ also $\abs{-x} < R$, so $f(-x) = \sum c_k (-x)^k = \sum (-1)^k c_k x^k$, a power series converging for all $\abs{x} < R$.

(1) The hypothesis says $\sum (-1)^k c_k x^k = \sum c_k x^k$ for all $\abs{x} < R$. By uniqueness of power series coefficients (with $\delta = \min(R, 1)$, so that $0 < \delta \le R$ even when $R = \infty$), $(-1)^k c_k = c_k$ for every $k$. For odd $k$ this reads $-c_k = c_k$, so $c_k = 0$.

(2) Now $\sum (-1)^k c_k x^k = \sum (-c_k) x^k$ for all $\abs{x} < R$, so $(-1)^k c_k = -c_k$ for every $k$. For even $k$ this reads $c_k = -c_k$, so $c_k = 0$.
""", 1, 10, [
    r"Write $f(-x)$ as a power series in $x$ and compare coefficients with those of $f(x)$ or $-f(x)$.",
], ["c4-cor-ps-unique"])

ex("c4-ex-zeros-accumulate", "A power series vanishing on a sequence tending to $0$ is zero", r"""
Let $\sum c_k x^k$ have radius of convergence $R > 0$ and sum $f(x)$ for $\abs{x} < R$. Suppose there are points $x_n \in (-R,R)$ with $x_n \ne 0$, $x_n \to 0$, and $f(x_n) = 0$ for every $n$. Then $c_k = 0$ for every $k$, and so $f = 0$ on $(-R,R)$.
""", r"""
Suppose not all $c_k$ are $0$, and let $m$ be the least index with $c_m \ne 0$. Consider the power series $\sum_{j \ge 0} c_{j+m} x^j$.

\emph{It converges for every $\abs{x} < R$, with sum $g(x)$ satisfying $f(x) = x^m g(x)$.} At $x = 0$ this is clear, with $g(0) = c_m$, and $f(0) = c_0$ equals $0^m c_m$ in both cases $m = 0$ and $m > 0$. For $0 < \abs{x} < R$: the series $\sum_{k \ge 0} c_k x^k$ converges, its terms with $k < m$ are $0$, and its $n$-th partial sum for $n \ge m$ equals $x^m \sum_{j=0}^{n-m} c_{j+m} x^j$. Dividing by the nonzero constant $x^m$, the partial sums of $\sum_j c_{j+m} x^j$ converge, to $f(x)/x^m$. So $g$ is defined on $(-R,R)$ and $f(x) = x^m g(x)$ there.

\emph{$g$ is continuous on $(-R,R)$.} The series defining $g$ converges at every $x$ with $\abs{x} < R$, so its radius of convergence $R'$ is at least $R$: if $R' < R$ it would diverge at some $x$ with $R' < \abs{x} < R$ by the Cauchy–Hadamard theorem. In particular $R' > 0$, and a power series is continuous on its interval of convergence $(-R',R') \supseteq (-R,R)$.

\emph{Contradiction.} For every $n$, $0 = f(x_n) = x_n^m g(x_n)$ with $x_n \ne 0$, so $g(x_n) = 0$. Since $x_n \to 0$ and $g$ is continuous at $0$, $g(0) = \lim_n g(x_n) = 0$. But $g(0) = c_m \ne 0$. Hence every $c_k$ is $0$, and $f(x) = \sum 0 \cdot x^k = 0$ for all $\abs{x} < R$.
""", 3, 30, [
    r"Argue by contradiction with the \emph{first} nonzero coefficient $c_m$, and factor: $f(x) = x^m g(x)$ where $g$ is again a power series.",
    r"$g$ is continuous near $0$ (why does its radius of convergence equal at least $R$?) and $g(0) = c_m \ne 0$; but $g(x_n) = 0$ with $x_n \to 0$.",
], ["c4-def-power-series", "c4-thm-radius", "c4-cor-ps-continuous"])

# ── Compactness and equicontinuity ───────────────────────────────────────────

ex("c4-ex-holder-ball-compact", "A compact set of functions", r"""
Let $\mathcal{H}$ be the set of all $f \in C^0[0,1]$ such that
\[ \abs{f(0)} \le 1 \qquad \text{and} \qquad \abs{f(s) - f(t)} \le \sqrt{\abs{s - t}} \ \text{ for all } s, t \in [0,1] . \]
\begin{enumerate}
\item $\mathcal{H}$ is a compact subset of $C^0[0,1]$.
\item Every sequence $(f_n)$ in $\mathcal{H}$ has a uniformly convergent subsequence, and the limit again belongs to $\mathcal{H}$.
\end{enumerate}
(Compare the closed unit ball of $C^0[0,1]$, which is not compact.)
""", r"""
(1) By the Heine–Borel theorem in a function space it suffices to show that $\mathcal{H}$ is closed, bounded and equicontinuous.

\emph{Bounded.} For $f \in \mathcal{H}$ and $x \in [0,1]$, $\abs{f(x)} \le \abs{f(0)} + \abs{f(x) - f(0)} \le 1 + \sqrt{x} \le 2$. So $\norm{f} \le 2$.

\emph{Equicontinuous.} Let $\eps > 0$ and put $\delta = \eps^2$. If $\abs{s - t} < \delta$ then for every $f \in \mathcal{H}$, $\abs{f(s) - f(t)} \le \sqrt{\abs{s-t}} < \sqrt{\delta} = \eps$.

\emph{Closed.} Let $f_n \in \mathcal{H}$ and $f \in C^0[0,1]$ with $\norm{f_n - f} \to 0$. Then $f_n \to f$ pointwise, since $\abs{f_n(x) - f(x)} \le \norm{f_n - f}$. Weak inequalities pass to limits: $\abs{f(0)} = \lim_n \abs{f_n(0)} \le 1$, and for all $s,t$, $\abs{f(s) - f(t)} = \lim_n \abs{f_n(s) - f_n(t)} \le \sqrt{\abs{s-t}}$. So $f \in \mathcal{H}$, and $\mathcal{H}$ contains the limits of its convergent sequences, i.e. is closed in $C^0[0,1]$.

(2) A compact subset of a metric space is sequentially compact: every sequence in $\mathcal{H}$ has a subsequence converging, in the sup metric, to a point of $\mathcal{H}$. Convergence in the sup metric is uniform convergence, which is (2).
""", 2, 25, [
    r"Check the three conditions of the Heine–Borel theorem in a function space. For equicontinuity, $\delta$ can be written down in terms of $\eps$ alone.",
    r"For closedness, sup-norm convergence implies pointwise convergence, and both defining inequalities survive pointwise limits.",
], ["c4-thm-heine-borel-function-space", "c4-def-equicontinuous", "c4-thm-sup-metric-uniform"])

ex("c4-ex-ascoli-needs-compactness", "Arzelà–Ascoli needs a compact domain", r"""
Let $\varphi : \R \to \R$ be $\varphi(x) = \max(0, 1 - 2\abs{x})$, the tent of height $1$ on $[-\tfrac12, \tfrac12]$, and let $f_n(x) = \varphi(x - n)$ for $n \in \N$.
\begin{enumerate}
\item $(f_n)$ is a bounded sequence in $C_b(\R)$, and it is equicontinuous.
\item $f_n \to 0$ pointwise on $\R$.
\item No subsequence of $(f_n)$ converges uniformly on $\R$. So the compactness of $M$ in the Arzelà–Ascoli theorem cannot be dropped.
\end{enumerate}
""", r"""
(1) For every $x$, $0 \le \varphi(x) \le 1$, so $0 \le f_n \le 1$ and $f_n \in C_b(\R)$ with $\norm{f_n} \le 1$; in fact $\norm{f_n} = 1$ since $f_n(n) = \varphi(0) = 1$. For the Lipschitz bound, first note that for real $u, v$,
\[ \abs{\max(0,u) - \max(0,v)} = \tfrac12 \abs{(u - v) + (\abs{u} - \abs{v})} \le \tfrac12 \bigl( \abs{u-v} + \abs{u - v} \bigr) = \abs{u - v} , \]
using $\max(0,u) = \tfrac12 (u + \abs{u})$ and $\bigl|\abs{u} - \abs{v}\bigr| \le \abs{u-v}$. With $u = 1 - 2\abs{x}$ and $v = 1 - 2\abs{y}$ this gives $\abs{\varphi(x) - \varphi(y)} \le 2\bigl|\abs{x} - \abs{y}\bigr| \le 2\abs{x - y}$. Hence $\abs{f_n(x) - f_n(y)} = \abs{\varphi(x-n) - \varphi(y-n)} \le 2\abs{x - y}$ for all $n$: the $f_n$ share the Lipschitz constant $2$, so the sequence is equicontinuous (and each $f_n$ is continuous).

(2) Fix $x \in \R$. For $n > x + \tfrac12$ we have $x - n < -\tfrac12$, so $1 - 2\abs{x-n} < 0$ and $f_n(x) = 0$. Thus $f_n(x) \to 0$.

(3) Suppose a subsequence $(f_{n_k})$ converged uniformly on $\R$ to some $g$. A uniform limit is a pointwise limit, so by (2) $g = 0$. But $\sup_x \abs{f_{n_k}(x) - 0} = \norm{f_{n_k}} = 1$ for every $k$, so for $\eps = 1$ no $K$ makes $\abs{f_{n_k}(x)} < 1$ for all $x$ and all $k \ge K$. Contradiction. So $(f_n)$ is bounded and equicontinuous on $\R$ yet has no uniformly convergent subsequence, which the Arzelà–Ascoli theorem forbids on a compact domain.
""", 2, 20, [
    r"A common Lipschitz constant gives equicontinuity. Show $\varphi$ is $2$-Lipschitz; translating does not change that.",
    r"For (3): any uniform limit of a subsequence must be the pointwise limit $0$, but each $f_n$ has sup norm $1$.",
], ["c4-def-sup-norm", "c4-def-equicontinuous", "c4-prop-lipschitz-equicontinuous", "c4-def-uniform"])

ex("c4-ex-pointwise-bounded", "Pointwise bounded plus equicontinuous is bounded", r"""
Let $M$ be a nonempty compact metric space and $\mathcal{E}$ an equicontinuous set of functions $M \to \R$ that is \emph{pointwise bounded}: for each $x \in M$ there is a constant $B_x$ with $\abs{f(x)} \le B_x$ for all $f \in \mathcal{E}$. Then $\mathcal{E}$ is bounded: there is a constant $B$ with $\abs{f(x)} \le B$ for all $f \in \mathcal{E}$ and all $x \in M$. Consequently every pointwise bounded equicontinuous sequence in $C^0(M)$ has a uniformly convergent subsequence.
""", r"""
By equicontinuity with $\eps = 1$ there is a $\delta > 0$ such that $\abs{f(s) - f(t)} < 1$ for all $f \in \mathcal{E}$ whenever $d(s,t) < \delta$. By the lemma on finite nets there is a finite set $\set{x_1, \dots, x_J} \subseteq M$ (with $J \ge 1$, as $M$ is nonempty) such that every $x \in M$ is within $\delta$ of some $x_j$. Put $B = 1 + \max(B_{x_1}, \dots, B_{x_J})$.

Let $f \in \mathcal{E}$ and $x \in M$, and pick $j$ with $d(x, x_j) < \delta$. Then
\[ \abs{f(x)} \le \abs{f(x) - f(x_j)} + \abs{f(x_j)} < 1 + B_{x_j} \le B . \]
So $\mathcal{E}$ is bounded. A pointwise bounded equicontinuous sequence in $C^0(M)$ is therefore bounded and equicontinuous, and the Arzelà–Ascoli theorem gives a uniformly convergent subsequence.
""", 2, 15, [
    r"Equicontinuity with $\eps = 1$ gives a $\delta$; compactness gives finitely many points within $\delta$ of everything. Bound $f(x)$ through the nearest of them.",
], ["c4-def-equicontinuous", "c4-lem-finite-nets", "c4-thm-arzela-ascoli"])

# ── Uniform approximation ────────────────────────────────────────────────────

ex("c4-ex-c1-approximation", "Approximating a function and its derivative at once", r"""
Let $a < b$ and let $f : [a,b] \to \R$ be differentiable with continuous derivative $f'$. Then there are polynomials $p_n$ such that
\[ p_n \rightrightarrows f \quad \text{and} \quad p_n' \rightrightarrows f' \quad \text{on } [a,b] . \]
""", r"""
Since $f'$ is continuous on $[a,b]$, the Weierstrass approximation theorem gives, for each $n$, a polynomial $q_n$ with $\abs{q_n(t) - f'(t)} < 1/n$ for all $t \in [a,b]$; so $q_n \rightrightarrows f'$ on $[a,b]$. Define
\[ p_n(x) = f(a) + \int_a^x q_n(t)\,dt \qquad (x \in [a,b]) . \]
If $q_n(t) = \sum_{j=0}^d b_j t^j$ then $p_n(x) = f(a) + \sum_{j=0}^d b_j \frac{x^{j+1} - a^{j+1}}{j+1}$, a polynomial, and differentiating it term by term gives $p_n' = q_n$. Hence $p_n' = q_n \rightrightarrows f'$.

For $p_n$ itself: $f'$ is continuous, hence Riemann integrable, and $f$ is an antiderivative of $f'$ on $[a,x]$, so by the antiderivative theorem of Chapter 3, $f(x) = f(a) + \int_a^x f'(t)\,dt$ for every $x \in [a,b]$. Since the integrable functions $q_n$ converge uniformly to $f'$, the corollary on indefinite integrals gives $\int_a^x q_n \rightrightarrows \int_a^x f'$ on $[a,b]$; adding the constant $f(a)$ to both sides, $p_n \rightrightarrows f$. (Explicitly, $\abs{p_n(x) - f(x)} = \abs{\int_a^x (q_n - f')} \le (b-a)/n$.)
""", 2, 20, [
    r"Approximate the derivative first, then integrate: if $q_n \rightrightarrows f'$, what does $f(a) + \int_a^x q_n$ converge to?",
], ["c4-thm-weierstrass", "c4-cor-indefinite-integrals", "c4-def-uniform"])

ex("c4-ex-polynomial-limits-on-r", "Uniform limits of polynomials on the whole line", r"""
Prove or disprove: for every continuous $f : \R \to \R$ there are polynomials $p_n$ with $p_n \rightrightarrows f$ on $\R$.
""", r"""
The statement is false. We show that a uniform limit on $\R$ of polynomials is itself a polynomial, so that, for instance, $f(x) = 1/(1+x^2)$ is not such a limit.

\emph{A bounded polynomial on $\R$ is constant.} Let $p(x) = a_d x^d + \dots + a_1 x + a_0$ with $d \ge 1$ and $a_d \ne 0$, and put $A = \abs{a_{d-1}} + \dots + \abs{a_0}$. For $\abs{x} \ge 1$ we have $\abs{x}^j \le \abs{x}^{d-1}$ for $j \le d-1$, so
\[ \abs{p(x)} \ge \abs{a_d}\abs{x}^d - A\abs{x}^{d-1} = \abs{x}^{d-1} \bigl( \abs{a_d}\abs{x} - A \bigr) , \]
which tends to $\infty$ as $\abs{x} \to \infty$. So a polynomial of degree $d \ge 1$ is unbounded on $\R$, and a bounded one has degree $0$, i.e. is constant.

\emph{A uniform limit of polynomials on $\R$ is a polynomial.} Suppose $p_n \rightrightarrows f$ on $\R$. By the Cauchy criterion the sequence is uniformly Cauchy, so there is an $N$ with $\abs{p_n(x) - p_N(x)} < 1$ for all $n \ge N$ and all $x \in \R$. For each $n \ge N$ the polynomial $p_n - p_N$ is bounded on $\R$, hence equal to a constant $c_n$. Then $c_n = p_n(0) - p_N(0) \to f(0) - p_N(0) =: c$, and for every $x$,
\[ f(x) = \lim_{n \to \infty} p_n(x) = \lim_{n \to \infty} \bigl( p_N(x) + c_n \bigr) = p_N(x) + c . \]
So $f = p_N + c$ is a polynomial.

\emph{The counterexample.} $f(x) = 1/(1+x^2)$ is continuous on $\R$, bounded (by $1$), and not constant ($f(0) = 1 \ne \tfrac12 = f(1)$). A bounded polynomial is constant, so $f$ is not a polynomial, and therefore not a uniform limit of polynomials on $\R$. (On each compact interval $[-r,r]$, by contrast, the Weierstrass approximation theorem applies to $f$.)
""", 3, 30, [
    r"Think about what a uniform limit of polynomials on all of $\R$ could be. Compare two far-out terms of the sequence: $p_n - p_N$ is a polynomial that is bounded on $\R$.",
    r"Show a bounded polynomial on $\R$ is constant. Conclude that from some $N$ on, $p_n = p_N + c_n$ with constants $c_n$, and so the limit is $p_N$ plus a constant.",
    r"Any bounded, nonconstant continuous function on $\R$ is then a counterexample.",
], ["c4-def-uniform", "c4-lem-uniform-cauchy"])

ex("c4-ex-sw-injective", "Polynomials in one injective function", r"""
Let $M$ be a nonempty compact metric space and $h : M \to \R$ a continuous injective function. Let $\mathcal{A}_h = \set{ p \circ h : p \text{ a polynomial} }$.
\begin{enumerate}
\item $\mathcal{A}_h$ is dense in $C^0(M)$.
\item The polynomials in $x^2$, that is the functions $x \mapsto p(x^2)$, are dense in $C^0[0,1]$ but not in $C^0[-1,1]$.
\end{enumerate}
""", r"""
(1) Each $p \circ h$ is continuous as a composition of continuous functions, so $\mathcal{A}_h \subseteq C^0(M)$. It is a function algebra: it is nonempty, and for polynomials $p, q$ and $c \in \R$,
\[ p \circ h + q \circ h = (p + q) \circ h, \qquad c\,(p \circ h) = (cp) \circ h, \qquad (p \circ h)(q \circ h) = (pq) \circ h , \]
with $p+q$, $cp$, $pq$ again polynomials. It vanishes nowhere, since the constant polynomial $1$ gives the function $1 \in \mathcal{A}_h$. It separates points: the polynomial $p(y) = y$ gives $h \in \mathcal{A}_h$, and $h(x) \ne h(x')$ for $x \ne x'$ by injectivity. By the Stone–Weierstrass theorem $\mathcal{A}_h$ is dense in $C^0(M)$.

(2) On $M = [0,1]$ the function $h(x) = x^2$ is continuous and injective (if $x^2 = x'^2$ with $x, x' \ge 0$ then $x = x'$), so by (1) the polynomials in $x^2$ are dense in $C^0[0,1]$. On $[-1,1]$ every function $p(x^2)$ takes the same value at the distinct points $1$ and $-1$. The polynomials in $x^2$ form a function algebra (the computation in (1) did not use injectivity), so by the exercise on the necessity of the Stone–Weierstrass hypotheses, part (2), they are not dense in $C^0[-1,1]$.
""", 2, 20, [
    r"Verify the three hypotheses of Stone–Weierstrass for $\mathcal{A}_h$: it is an algebra because $(p \circ h)(q \circ h) = (pq) \circ h$; the constant $1$ and $h$ itself do the rest.",
    r"On $[-1,1]$, what do all functions $p(x^2)$ have in common at $\pm 1$?",
], ["c4-def-function-algebra", "c4-thm-stone-weierstrass", "c4-ex-sw-necessary"])

ex("c4-ex-c0-separable", r"$C^0[a,b]$ has a countable dense subset", r"""
Let $a < b$. The set $\mathcal{P}_\Q$ of polynomials with rational coefficients is a countable dense subset of $C^0[a,b]$.
""", r"""
\emph{Countable.} For each $d \ge 0$ the polynomials of degree at most $d$ with rational coefficients are the images of the $(d+1)$-tuples $(r_0, \dots, r_d) \in \Q^{d+1}$ under $(r_0,\dots,r_d) \mapsto \sum_j r_j x^j$; a finite product of countable sets is countable, and the image of a countable set is countable (Chapter 1). $\mathcal{P}_\Q$ is the union over $d = 0, 1, 2, \dots$ of these countable sets, hence countable.

\emph{Dense.} Let $f \in C^0[a,b]$ and $\eps > 0$. By the Weierstrass approximation theorem there is a polynomial $p(x) = \sum_{j=0}^d a_j x^j$ with $\abs{p(x) - f(x)} < \eps/2$ for all $x \in [a,b]$. Put $C = \max(1, \abs{a}, \abs{b})$, so that $\abs{x}^j \le C^j \le C^d$ for $x \in [a,b]$ and $0 \le j \le d$. Since $\Q$ is dense in $\R$, choose rationals $r_j$ with $\abs{r_j - a_j} < \dfrac{\eps}{2(d+1)C^d}$ and let $q(x) = \sum_{j=0}^d r_j x^j \in \mathcal{P}_\Q$. For every $x \in [a,b]$,
\[ \abs{q(x) - p(x)} \le \sum_{j=0}^d \abs{r_j - a_j}\,\abs{x}^j < (d+1) \cdot \frac{\eps}{2(d+1)C^d} \cdot C^d = \frac{\eps}{2} , \]
so $\abs{q(x) - f(x)} \le \abs{q(x) - p(x)} + \abs{p(x) - f(x)} < \eps$. Thus $\norm{q - f} \le \eps$; as $\eps$ was arbitrary (apply this with $\eps/2$ to get $\norm{q - f} < \eps$), every ball about $f$ meets $\mathcal{P}_\Q$, and $\mathcal{P}_\Q$ is dense in $C^0[a,b]$.
""", 2, 20, [
    r"Weierstrass gives a polynomial within $\eps/2$ of $f$; now perturb its finitely many coefficients to rationals without moving the polynomial more than $\eps/2$ on $[a,b]$.",
    r"On $[a,b]$, $\abs{x}^j \le C^d$ with $C = \max(1,\abs{a},\abs{b})$, so changing each of $d+1$ coefficients by less than $\eta$ moves the polynomial by less than $(d+1)\eta C^d$.",
], ["c4-thm-weierstrass", "c4-def-sup-norm", "c4-prop-sup-norm"])

# ── Contractions and ODEs ────────────────────────────────────────────────────

ex("c4-ex-shrinking-compact", "A distance-shrinking map of a compact space has a fixed point", r"""
Let $M$ be a nonempty compact metric space and $f : M \to M$ a map with
\[ d(f(x), f(y)) < d(x, y) \quad \text{for all } x \ne y \text{ in } M . \]
\begin{enumerate}
\item $f$ has exactly one fixed point $p$.
\item For every $x \in M$ the orbit $f^n(x)$ converges to $p$.
\end{enumerate}
(Without compactness this fails: see the exercise on $x + 1/x$.)
""", r"""
First, $f$ is continuous, indeed $d(f(x),f(y)) \le d(x,y)$ for all $x, y$ (with equality when $x = y$).

(1) \emph{Existence.} Let $g(x) = d(x, f(x))$. For $x, y \in M$ the triangle inequality gives
\[ \abs{g(x) - g(y)} \le d(x,y) + d(f(x), f(y)) \le 2\,d(x,y) , \]
so $g$ is continuous. A continuous real function on a nonempty compact metric space attains its minimum (Chapter 2); let $p$ be a point where $g$ is least. If $f(p) \ne p$, then
\[ g(f(p)) = d\bigl(f(p), f(f(p))\bigr) < d(p, f(p)) = g(p) , \]
contradicting minimality. So $f(p) = p$.

\emph{Uniqueness.} If $p \ne q$ were both fixed, then $d(p,q) = d(f(p), f(q)) < d(p,q)$, which is absurd.

(2) Let $x \in M$, $x_n = f^n(x)$ and $a_n = d(x_n, p)$. Since $p$ is fixed, $a_{n+1} = d(f(x_n), f(p)) \le d(x_n, p) = a_n$. So $(a_n)$ is decreasing and bounded below by $0$; let $a = \lim a_n \ge 0$. By compactness some subsequence $x_{n_j}$ converges to a point $q \in M$. By continuity of $y \mapsto d(y,p)$ (it is $1$-Lipschitz) and of $f$,
\[ d(q, p) = \lim_j d(x_{n_j}, p) = \lim_j a_{n_j} = a, \qquad d(f(q), p) = \lim_j d(f(x_{n_j}), p) = \lim_j a_{n_j + 1} = a . \]
If $a > 0$ then $q \ne p$, so $d(f(q), p) = d(f(q), f(p)) < d(q, p) = a$, contradicting $d(f(q),p) = a$. Hence $a = 0$, that is $d(x_n, p) \to 0$: the orbit converges to $p$.
""", 3, 40, [
    r"Minimise the continuous function $x \mapsto d(x, f(x))$ over the compact space $M$. What happens if you apply $f$ to a minimiser?",
    r"For (2), the distances $d(f^n(x), p)$ decrease, so they converge to some $a \ge 0$. Use compactness to find a limit point $q$ of the orbit and show $a > 0$ is impossible.",
], ["c4-def-contraction"])

ex("c4-ex-newton-sqrt2", r"Computing $\sqrt2$ with the contraction principle", r"""
Let $M = [1,2]$ and $f(x) = \dfrac{x}{2} + \dfrac{1}{x}$.
\begin{enumerate}
\item $f(M) \subseteq M$.
\item $f$ is a contraction of $M$ with constant $k = \tfrac12$.
\item The unique fixed point of $f$ is $\sqrt2$, and the orbit of $x_0 = 1$ satisfies $\abs{f^n(1) - \sqrt2} \le 2^{-n}$ for all $n \ge 0$.
\end{enumerate}
""", r"""
(1) For $x \in [1,2]$,
\[ f(x) - \sqrt2 = \frac{x^2 - 2\sqrt2\,x + 2}{2x} = \frac{(x - \sqrt2)^2}{2x} \ge 0 \qquad \text{and} \qquad f(x) - \tfrac32 = \frac{x^2 - 3x + 2}{2x} = \frac{(x-1)(x-2)}{2x} \le 0 , \]
the last because $x - 1 \ge 0$, $x - 2 \le 0$ and $2x > 0$. So $f(x) \in [\sqrt2, \tfrac32] \subseteq [1,2]$.

(2) For $x, y \in [1,2]$,
\[ f(x) - f(y) = \frac{x - y}{2} + \frac{y - x}{xy} = (x - y)\left( \frac12 - \frac{1}{xy} \right) . \]
Since $1 \le xy \le 4$ we have $\tfrac14 \le \tfrac{1}{xy} \le 1$, so $\tfrac12 - \tfrac{1}{xy}$ lies in $[-\tfrac12, \tfrac14]$ and has absolute value at most $\tfrac12$. Hence $\abs{f(x) - f(y)} \le \tfrac12 \abs{x - y}$.

(3) $M = [1,2]$ is a closed subset of the complete space $\R$, hence complete, and nonempty. By the Banach contraction principle $f$ has exactly one fixed point $p \in M$, and every orbit converges to it. A point $x \in M$ is fixed if and only if $x/2 + 1/x = x$, i.e. $1/x = x/2$, i.e. $x^2 = 2$; in $[1,2]$ the only such point is $\sqrt 2$. So $p = \sqrt2$. By the rate-of-convergence corollary, with $x_0 = 1$ and $x_1 = f(1) = \tfrac32$,
\[ \abs{f^n(1) - \sqrt2} \le \frac{k^n}{1-k}\,\abs{x_0 - x_1} = \frac{2^{-n}}{1/2} \cdot \frac12 = 2^{-n} . \]
""", 2, 20, [
    r"For (1), compute $f(x) - \sqrt2$ and $f(x) - \tfrac32$ as single fractions and factor the numerators.",
    r"For (2), $f(x) - f(y) = (x-y)\bigl(\tfrac12 - \tfrac{1}{xy}\bigr)$; bound the second factor on $[1,2]^2$.",
], ["c4-def-contraction", "c4-thm-banach", "c4-cor-banach-rate"])

ex("c4-ex-picard-applied", "Picard's theorem applied to $y' = t^2 + y^2$", r"""
Consider the initial value problem $y' = t^2 + y^2$, $y(0) = 0$, with the standing notation $t_0 = y_0 = 0$ and $a = b = 1$.
\begin{enumerate}
\item The hypotheses of Picard's theorem hold with $K = 2$ and $L = 2$, so the problem has exactly one solution on $[-\tfrac14, \tfrac14]$.
\item Starting from $u_0 = 0$, the first two Picard iterates are $u_1(t) = \dfrac{t^3}{3}$ and $u_2(t) = \dfrac{t^3}{3} + \dfrac{t^7}{63}$.
\end{enumerate}
""", r"""
(1) Here $Q = [-1,1] \times [-1,1]$ and $f(t,y) = t^2 + y^2$, a polynomial, hence continuous on $Q$. For $(t,y) \in Q$, $\abs{f(t,y)} \le 1 + 1 = 2 = K$. For $(t,y), (t,z) \in Q$,
\[ \abs{f(t,y) - f(t,z)} = \abs{y^2 - z^2} = \abs{y + z}\,\abs{y - z} \le 2\abs{y - z} , \]
so $f$ is Lipschitz in $y$ with constant $L = 2$. With $\tau = \tfrac14$: $\tau \le a = 1$, $K\tau = \tfrac12 \le b = 1$, and $L\tau = \tfrac12 < 1$. Picard's theorem gives exactly one solution on $I_\tau = [-\tfrac14, \tfrac14]$.

(2) With $u_0 = 0$ (the constant function $y_0$, which lies in $X$),
\[ u_1(t) = 0 + \int_0^t \bigl( s^2 + 0^2 \bigr)\,ds = \frac{t^3}{3}, \qquad u_2(t) = \int_0^t \left( s^2 + \frac{s^6}{9} \right) ds = \frac{t^3}{3} + \frac{t^7}{63} . \]
""", 1, 10, [
    r"Bound $f$ on the square and factor $y^2 - z^2$ for the Lipschitz constant; then check the three inequalities on $\tau$.",
], ["c4-def-ivp", "c4-lem-picard-space", "c4-lem-picard-operator", "c4-thm-picard"])

ex("c4-ex-global-uniqueness", "Uniqueness without the smallness condition", r"""
With the standing notation, let $f : Q \to \R$ be continuous and satisfy a Lipschitz condition in $y$ with constant $L$. Let $0 < \tau \le a$ be arbitrary (no condition such as $L\tau < 1$ is assumed), and let $y$ and $z$ be two solutions of the initial value problem $y' = f(t,y)$, $y(t_0) = y_0$ on $I_\tau$. Then $y = z$ on $I_\tau$.
""", r"""
By the lemma on the integral equation, $y$ and $z$ are continuous and satisfy
\[ y(t) = y_0 + \int_{t_0}^t f(s, y(s))\,ds, \qquad z(t) = y_0 + \int_{t_0}^t f(s, z(s))\,ds \qquad (t \in I_\tau) . \]
Let $w = \abs{y - z}$, a continuous function on the compact interval $I_\tau$, and let $W = \max_{I_\tau} w$. We prove by induction on $n \ge 0$ that
\[ w(t) \le W\, \frac{L^n \abs{t - t_0}^n}{n!} \quad \text{for all } t \in I_\tau . \qquad (*) \]
For $n = 0$ this is $w \le W$. Assume $(*)$ for $n$ and let $t \in I_\tau$ with $t \ge t_0$. Subtracting the two integral equations, using $\abs{\int g} \le \int \abs{g}$ and monotonicity of the integral (the integrands are continuous), the Lipschitz condition, and then $(*)$,
\[ w(t) = \abs{\int_{t_0}^t \bigl( f(s,y(s)) - f(s,z(s)) \bigr) ds} \le \int_{t_0}^t L\, w(s)\,ds \le \int_{t_0}^t L\, W\, \frac{L^n (s - t_0)^n}{n!}\,ds = W\, \frac{L^{n+1} (t - t_0)^{n+1}}{(n+1)!} . \]
For $t < t_0$ the same computation with $\int_t^{t_0}$ and $(t_0 - s)^n$ gives $w(t) \le W L^{n+1} (t_0 - t)^{n+1}/(n+1)!$. This is $(*)$ for $n+1$.

Since $\abs{t - t_0} \le \tau$ on $I_\tau$, $(*)$ gives $w(t) \le W\,(L\tau)^n/n!$ for every $n$. The series $\sum_n (L\tau)^n/n!$ converges (ratio test, as for the exponential series), so its terms tend to $0$, and letting $n \to \infty$ gives $w(t) \le 0$. Hence $w = 0$, i.e. $y = z$ on $I_\tau$.
""", 4, 60, [
    r"Both solutions satisfy the integral equation. Subtract, and use the Lipschitz condition to bound $w = \abs{y - z}$ by $L\abs{\int_{t_0}^t w}$.",
    r"Feed the bound back into itself. Starting from $w \le W$ (its maximum), show by induction that $w(t) \le W L^n \abs{t-t_0}^n / n!$.",
    r"$(L\tau)^n / n! \to 0$ for every value of $L\tau$: the exponential series converges.",
], ["c4-def-ivp", "c4-lem-integral-equation", "c4-ex-radius-examples"])


with open(OUT, "w") as fh:
    json.dump({"version": 1, "id": "4-exercises", "blocks": blocks, "cards": []}, fh, indent=1, ensure_ascii=False)
n = sum(1 for b in blocks if b["kind"] == "exercise")
print(f"4-exercises: {len(blocks)} blocks, {n} exercises")
