import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c4_lib import Section

s = Section("4-power-series")

s.text("c4-ps-intro", "prose", r"""
A power series $\sum c_k x^k$ is the simplest series of functions, and the machinery of the previous section applies to it almost perfectly. Inside its interval of convergence a power series converges uniformly on every compact subinterval, so it may be differentiated and integrated term by term as if it were a polynomial. As a result, functions given by power series are infinitely differentiable and their coefficients are determined by their derivatives at the centre.
""")

s.text("c4-def-power-series", "definition", r"""
A \emph{power series} (centred at $0$) is a series of functions $\sum_{k=0}^\infty c_k x^k$ with real coefficients $c_k$. Put
\[ L = \limsup_{k \to \infty} \abs{c_k}^{1/k} \in [0, \infty] . \]
The \emph{radius of convergence} of the series is $R = 1/L$, with the conventions $R = \infty$ if $L = 0$ and $R = 0$ if $L = \infty$. The interval $(-R, R)$ is its \emph{interval of convergence}.

A power series centred at $x_0$ is $\sum c_k (x - x_0)^k$; substituting $h = x - x_0$ reduces every statement about it to the case $x_0 = 0$.
""", "Power series and radius of convergence")

s.gate("c4-thm-radius", "theorem", "Radius of convergence (Cauchy–Hadamard)", r"""
Let $\sum c_k x^k$ be a power series with radius of convergence $R$. If $\abs{x} < R$ the series converges absolutely. If $\abs{x} > R$ the terms $c_k x^k$ do not tend to $0$, so the series diverges.
""", r"""
Let $a_k = \abs{c_k}^{1/k}$ and $L = \limsup a_k$. Recall two facts about the limit superior of a sequence in $[0,\infty)$: if $L < c$ then $a_k < c$ for all sufficiently large $k$; if $L > c$ then $a_k > c$ for infinitely many $k$.

\emph{Suppose $\abs{x} < R$.} Then $R > 0$, so $L < \infty$. If $x = 0$ every term with $k \ge 1$ vanishes and the series converges absolutely. Otherwise choose a real number $\rho$ with $\abs{x} < \rho < R$. Then $1/\rho > L$: this is clear if $L = 0$, and if $L > 0$ it is $\rho < 1/L = R$. So there is a $K$ such that $\abs{c_k}^{1/k} < 1/\rho$ for all $k \ge K$, and for such $k$
\[ \abs{c_k x^k} < \left( \frac{\abs{x}}{\rho} \right)^{k} . \]
The geometric series with ratio $\abs{x}/\rho < 1$ converges, so $\sum \abs{c_k x^k}$ converges by the comparison test.

\emph{Suppose $\abs{x} > R$.} Then $R < \infty$, so $L > 0$, and $x \ne 0$. We have $1/\abs{x} < L$: this is clear if $L = \infty$, and if $L < \infty$ it is $\abs{x} > 1/L = R$. So $\abs{c_k}^{1/k} > 1/\abs{x}$ for infinitely many $k$, and for each such $k$, $\abs{c_k x^k} > 1$. Hence $c_k x^k$ does not tend to $0$ and $\sum c_k x^k$ diverges.
""", 3, 30, [
    r"Compare with a geometric series. If $\abs{x} < R$, squeeze a number $\rho$ between: $\abs{x} < \rho < R$.",
    r"$\limsup \abs{c_k}^{1/k} < 1/\rho$ means $\abs{c_k} < \rho^{-k}$ for all large $k$. For $\abs{x} > R$, $\limsup \abs{c_k}^{1/k} > 1/\abs{x}$ means $\abs{c_k x^k} > 1$ infinitely often.",
], ["c4-def-power-series"])

s.text("c4-ex-radius-examples", "example", r"""
The theorem says nothing about $\abs{x} = R$, and anything can happen there.
\begin{itemize}
\item $\sum x^k$ has $R = 1$ and diverges at both $x = 1$ and $x = -1$.
\item $\sum_{k \ge 1} x^k / k$ has $R = 1$ (because $k^{1/k} \to 1$, proved below); it diverges at $x = 1$ and converges at $x = -1$.
\item $\sum_{k \ge 1} x^k/k^2$ has $R = 1$ and converges at both endpoints.
\item $\sum x^k/k!$ converges for every real $x$ by the ratio test, so by the theorem its radius is $R = \infty$.
\item $\sum k!\, x^k$ diverges for every $x \ne 0$ by the ratio test, so $R = 0$.
\end{itemize}
""", "Behaviour at the endpoints")

s.gate("c4-thm-ps-uniform", "theorem", "Uniform convergence on compact subintervals", r"""
Let $\sum c_k x^k$ be a power series and let $r \ge 0$ be such that $\sum \abs{c_k} r^k$ converges. Then $\sum c_k x^k$ converges uniformly on $[-r, r]$. In particular, if the series has radius of convergence $R > 0$, then it converges uniformly on $[-r,r]$ for every $r$ with $0 \le r < R$.
""", r"""
For $x \in [-r,r]$ and every $k$, $\abs{c_k x^k} \le \abs{c_k} r^k =: M_k$, and $\sum M_k$ converges by hypothesis. By the Weierstrass M-test the series converges uniformly on $[-r,r]$.

If $0 \le r < R$, the Cauchy–Hadamard theorem applied at the point $x = r$ says $\sum c_k r^k$ converges absolutely, i.e. $\sum \abs{c_k} r^k$ converges, so the first part applies.
""", 2, 15, [
    r"Use the Weierstrass M-test. What is the largest $\abs{c_k x^k}$ can be on $[-r,r]$?",
], ["c4-thm-m-test", "c4-thm-radius"])

s.gate("c4-cor-ps-continuous", "corollary", "A power series is continuous on its interval of convergence", r"""
Let $\sum c_k x^k$ have radius of convergence $R > 0$ and let $f(x) = \sum_{k=0}^\infty c_k x^k$ for $\abs{x} < R$. Then $f$ is continuous on $(-R,R)$.
""", r"""
Fix $x_0 \in (-R,R)$ and choose $r$ with $\abs{x_0} < r < R$. On $[-r,r]$ the series converges uniformly to $f$, and each term $c_k x^k$ is continuous, so the restriction of $f$ to $[-r,r]$ is continuous, since a uniformly convergent series of continuous functions has a continuous sum. Because $(-r,r)$ is an open interval containing $x_0$ on which $f$ agrees with this restriction, $f$ is continuous at $x_0$.
""", 2, 10, [
    r"Convergence need not be uniform on all of $(-R,R)$. Continuity is a local property: trap $x_0$ inside some $[-r,r]$ with $r<R$.",
], ["c4-thm-ps-uniform", "c4-thm-term-integration"])

s.text("c4-rem-not-uniform-on-open", "remark", r"""
The convergence is in general \emph{not} uniform on the whole interval $(-R,R)$. The partial sums of $\sum x^k$ are polynomials, bounded on $(-1,1)$, whereas the sum $1/(1-x)$ is unbounded there; a uniform limit of bounded functions is bounded.
""")

s.gate("c4-lem-kth-root-k", "lemma", r"$k^{1/k} \to 1$", r"""
$\lim_{k \to \infty} k^{1/k} = 1$.
""", r"""
For $k \ge 2$ write $k^{1/k} = 1 + h_k$. Since $k \ge 1$ we have $k^{1/k} \ge 1$, so $h_k \ge 0$. By the binomial theorem, all of whose terms are nonnegative here,
\[ k = (1 + h_k)^k \ge \binom{k}{2} h_k^2 = \frac{k(k-1)}{2}\, h_k^2 . \]
Hence $h_k^2 \le 2/(k-1)$, so $0 \le h_k \le \sqrt{2/(k-1)} \to 0$. By the squeeze theorem $h_k \to 0$, that is $k^{1/k} \to 1$.
""", 2, 15, [
    r"Write $k^{1/k} = 1 + h_k$ with $h_k \ge 0$ and expand $(1+h_k)^k = k$.",
    r"Keep only the quadratic term of the binomial expansion: $k \ge \binom{k}{2} h_k^2$.",
])

s.gate("c4-lem-derived-series", "lemma", "The derived and integrated series have the same radius", r"""
Let $\sum_{k \ge 0} c_k x^k$ have radius of convergence $R$. Then each of the series
\[ \sum_{k=1}^\infty k\, c_k\, x^{k-1} \qquad \text{and} \qquad \sum_{k=0}^\infty \frac{c_k}{k+1}\, x^{k+1} \]
converges absolutely when $\abs{x} < R$ and diverges when $\abs{x} > R$.
""", r"""
\emph{Claim.} If $a_k > 0$, $a_k \to 1$ and $b_k \ge 0$, then $\limsup a_k b_k = \limsup b_k$ in $[0,\infty]$.

Let $L = \limsup b_k$ and $L' = \limsup a_k b_k$. Fix $\eps \in (0,1)$ and choose $K$ with $1 - \eps < a_k < 1 + \eps$ for $k \ge K$. Then $(1-\eps) b_k \le a_k b_k \le (1+\eps) b_k$ for $k \ge K$, so for every $n \ge K$
\[ (1-\eps) \sup_{k \ge n} b_k \le \sup_{k \ge n} a_k b_k \le (1+\eps) \sup_{k \ge n} b_k \]
in $[0,\infty]$. Letting $n \to \infty$ gives $(1-\eps)L \le L' \le (1+\eps)L$. If $L = \infty$ the left inequality gives $L' = \infty$. If $L < \infty$, letting $\eps \to 0$ gives $L' = L$. This proves the claim.

\emph{The derived series.} Consider the power series $\sum_{k \ge 1} (k c_k) x^k$. Its coefficients satisfy $\abs{k c_k}^{1/k} = k^{1/k} \abs{c_k}^{1/k}$, and $k^{1/k} \to 1$, so by the claim $\limsup \abs{k c_k}^{1/k} = \limsup \abs{c_k}^{1/k}$. Thus $\sum k c_k x^k$ has the same radius of convergence $R$, and by the Cauchy–Hadamard theorem it converges absolutely for $\abs{x} < R$ and diverges for $\abs{x} > R$. For $x \ne 0$ the terms of $\sum k c_k x^{k-1}$ are those of $\sum k c_k x^k$ multiplied by the constant $1/x$, so the one converges absolutely (respectively diverges) exactly when the other does. At $x = 0$ the series $\sum k c_k x^{k-1}$ has only one nonzero term at most and converges absolutely. This gives the statement for the derived series.

\emph{The integrated series.} Consider $\sum_{k \ge 1} \frac{c_k}{k+1} x^k$; here $\abs{c_k/(k+1)}^{1/k} = (k+1)^{-1/k} \abs{c_k}^{1/k}$. For $k \ge 2$,
\[ 1 \le (k+1)^{1/k} \le (2k)^{1/k} = 2^{1/k} k^{1/k} \le \bigl(k^{1/k}\bigr)^2 , \]
and the right side tends to $1$, so $(k+1)^{1/k} \to 1$ and hence $(k+1)^{-1/k} \to 1$. By the claim this series also has radius of convergence $R$; adding the single term with $k=0$ does not affect convergence. So $\sum_{k \ge 0} \frac{c_k}{k+1} x^k$ converges absolutely for $\abs{x} < R$ and diverges for $\abs{x} > R$, and multiplying every term by the constant $x$ (nonzero when $\abs{x} > R$) preserves both properties.
""", 3, 40, [
    r"Multiplying or dividing every term by $x \ne 0$ does not change convergence, so compare with the power series whose coefficients are $k c_k$ and $c_k/(k+1)$.",
    r"$\abs{k c_k}^{1/k} = k^{1/k} \abs{c_k}^{1/k}$ and $k^{1/k} \to 1$. Prove that multiplying by a factor tending to $1$ does not change a limit superior.",
], ["c4-def-power-series", "c4-thm-radius", "c4-lem-kth-root-k"])

s.gate("c4-thm-ps-term-by-term", "theorem", "Power series may be differentiated and integrated term by term", r"""
Let $\sum c_k x^k$ have radius of convergence $R > 0$ and let $f(x) = \sum_{k=0}^\infty c_k x^k$ for $\abs{x} < R$. Then $f$ is differentiable on $(-R,R)$, and for every $x$ with $\abs{x} < R$
\[ f'(x) = \sum_{k=1}^\infty k\, c_k\, x^{k-1} \qquad \text{and} \qquad \int_0^x f(t)\,dt = \sum_{k=0}^\infty \frac{c_k}{k+1}\, x^{k+1} . \]
""", r"""
Fix $x$ with $\abs{x} < R$ and choose $r$ with $\abs{x} < r < R$. Work on the interval $[-r,r]$ with the functions $f_k(t) = c_k t^k$.

\emph{Derivative.} Each $f_k$ is differentiable with $f_k'(t) = k c_k t^{k-1}$ (and $f_0' = 0$). The series $\sum f_k$ converges pointwise to $f$ on $[-r,r]$. The series $\sum f_k' = \sum_{k \ge 1} k c_k t^{k-1}$ is a power series $\sum_{j \ge 0} d_j t^j$ with $d_j = (j+1)c_{j+1}$, and by the lemma on the derived series it converges absolutely at $t = r$ because $r < R$; that is, $\sum \abs{d_j} r^j$ converges. By the theorem on uniform convergence on compact subintervals, $\sum f_k'$ converges uniformly on $[-r,r]$. The theorem on term-by-term differentiation now shows that $f$ is differentiable on $[-r,r]$ with $f'(t) = \sum_{k \ge 1} k c_k t^{k-1}$; in particular this holds at $t = x$, and since $x$ is an interior point of $[-r,r]$ this is the ordinary two-sided derivative.

\emph{Integral.} The series $\sum f_k$ converges uniformly to $f$ on $[-r,r]$, hence on the closed interval $J$ with endpoints $0$ and $x$ (if $x = 0$ both sides of the formula are $0$). Each $f_k$ is continuous, hence integrable. If $x > 0$, term-by-term integration on $J = [0,x]$ gives
\[ \int_0^x f(t)\,dt = \sum_{k=0}^\infty \int_0^x c_k t^k\,dt = \sum_{k=0}^\infty \frac{c_k}{k+1}\,x^{k+1} . \]
If $x < 0$, the same theorem on $J = [x,0]$ gives $\int_x^0 f = \sum_k \int_x^0 c_k t^k\,dt = -\sum_k \frac{c_k}{k+1} x^{k+1}$, and $\int_0^x f = -\int_x^0 f$.
""", 3, 30, [
    r"Fix $x$ and work on $[-r,r]$ with $\abs{x} < r < R$, where the theorems for uniformly convergent series apply.",
    r"For the derivative you need the series of \emph{derivatives} to converge uniformly on $[-r,r]$. Which lemma tells you $\sum k\abs{c_k} r^{k-1}$ converges?",
], ["c4-thm-ps-uniform", "c4-lem-derived-series", "c4-thm-term-differentiation", "c4-thm-term-integration"])

s.gate("c4-cor-ps-smooth", "corollary", "Power series are smooth; the coefficients are Taylor coefficients", r"""
Let $\sum c_k x^k$ have radius of convergence $R > 0$ and $f(x) = \sum_{k=0}^\infty c_k x^k$ for $\abs{x} < R$. Then $f$ has derivatives of all orders on $(-R,R)$, for every $m \ge 0$ and $\abs{x} < R$
\[ f^{(m)}(x) = \sum_{k=m}^\infty \frac{k!}{(k-m)!}\, c_k\, x^{k-m} , \]
and in particular $c_m = \dfrac{f^{(m)}(0)}{m!}$ for every $m \ge 0$.
""", r"""
First an observation: if a power series $\sum d_j x^j$ converges at every $x$ with $\abs{x} < R$, then its radius of convergence $R'$ satisfies $R' \ge R$. Indeed, if $R' < R$ there would be an $x$ with $R' < \abs{x} < R$, at which the series diverges by the Cauchy–Hadamard theorem.

We prove by induction on $m$ that $f$ is $m$ times differentiable on $(-R,R)$ and the displayed formula holds for all $\abs{x} < R$. For $m = 0$ it is the definition of $f$. Assume it for $m$. Then on $(-R,R)$ the function $f^{(m)}$ is the sum of the power series $\sum_{j \ge 0} d_j x^j$ with $d_j = \frac{(j+m)!}{j!} c_{j+m}$ (substitute $k = j + m$). This series converges for all $\abs{x} < R$, so its radius is $R' \ge R$. By the theorem on term-by-term differentiation of power series, its sum is differentiable on $(-R',R') \supseteq (-R,R)$ with derivative $\sum_{j \ge 1} j d_j x^{j-1}$. Hence $f^{(m)}$ is differentiable on $(-R,R)$ and, putting $k = j+m$ again,
\[ f^{(m+1)}(x) = \sum_{j=1}^\infty j\,\frac{(j+m)!}{j!}\, c_{j+m}\, x^{j-1} = \sum_{k=m+1}^\infty \frac{k!}{(k-m-1)!}\, c_k\, x^{k-(m+1)} , \]
which is the formula for $m+1$. This completes the induction.

Setting $x = 0$ in the formula, every term with $k > m$ vanishes and the term $k = m$ equals $m!\,c_m$. So $f^{(m)}(0) = m!\, c_m$.
""", 3, 30, [
    r"Induct on $m$: the derivative of a power series is again a power series converging on $(-R,R)$.",
    r"To reapply the term-by-term theorem you need the radius of the differentiated series to be at least $R$. A power series that converges at every $\abs{x}<R$ cannot have smaller radius.",
], ["c4-thm-ps-term-by-term", "c4-thm-radius"])

s.gate("c4-cor-ps-unique", "corollary", "Uniqueness of power series coefficients", r"""
Suppose $\delta > 0$ and the power series $\sum a_k x^k$ and $\sum b_k x^k$ both converge for all $\abs{x} < \delta$, with
\[ \sum_{k=0}^\infty a_k x^k = \sum_{k=0}^\infty b_k x^k \quad \text{for all } \abs{x} < \delta . \]
Then $a_k = b_k$ for every $k$.
""", r"""
Let $c_k = a_k - b_k$. For $\abs{x} < \delta$ the series $\sum c_k x^k$ converges, with sum $\sum a_k x^k - \sum b_k x^k = 0$. Since it converges at every $x$ with $\abs{x} < \delta$, its radius of convergence $R$ is at least $\delta$ (otherwise it would diverge at some $x$ with $R < \abs{x} < \delta$ by the Cauchy–Hadamard theorem); in particular $R > 0$. Let $f(x) = \sum c_k x^k$ on $(-R,R)$. Then $f = 0$ on the open interval $(-\delta,\delta)$ around $0$, so all derivatives of $f$ at $0$ vanish. Since power series are smooth with $c_m = f^{(m)}(0)/m!$, we get $c_m = 0$, that is $a_m = b_m$, for all $m$.
""", 2, 15, [
    r"Subtract the two series and show that a power series which sums to $0$ near the origin has all coefficients $0$.",
    r"The coefficients are recovered from the sum: $c_m = f^{(m)}(0)/m!$.",
], ["c4-cor-ps-smooth", "c4-thm-radius"])

s.text("c4-def-analytic", "definition", r"""
Let $f : (a,b) \to \R$ and $x_0 \in (a,b)$.

If $f$ has derivatives of all orders at $x_0$, the \emph{Taylor series} of $f$ at $x_0$ is the power series
\[ \sum_{k=0}^\infty \frac{f^{(k)}(x_0)}{k!}\,(x - x_0)^k . \]

$f$ is \emph{analytic at $x_0$} if there are a $\delta > 0$ and coefficients $c_k$ such that $f(x) = \sum_{k=0}^\infty c_k (x - x_0)^k$ for all $x$ with $\abs{x - x_0} < \delta$. $f$ is \emph{analytic} on $(a,b)$ if it is analytic at each point of $(a,b)$.

By the preceding corollaries (applied after the substitution $h = x - x_0$), if $f$ is analytic at $x_0$ then $f$ is infinitely differentiable near $x_0$ and the only possible coefficients are $c_k = f^{(k)}(x_0)/k!$: an analytic function is the sum of its Taylor series near each point.
""", "Taylor series and analytic functions")

s.text("c4-thm-ps-analytic", "theorem", r"""
Let $\sum c_k x^k$ have radius of convergence $R > 0$. Then $f(x) = \sum_{k=0}^\infty c_k x^k$ is analytic on $(-R,R)$: for each $x_0 \in (-R,R)$, $f$ is the sum of its Taylor series at $x_0$ on the interval $\abs{x - x_0} < R - \abs{x_0}$.
""", "A power series is analytic on its interval of convergence")

s.text("c4-rem-ps-analytic", "remark", r"""
The definition of the sum $f$ only exhibits a power series centred at $0$; the theorem asserts one centred at every other point of the interval. Its proof expands $(x_0 + h)^k$ by the binomial theorem and rearranges an absolutely convergent double series, a tool we have not developed. We take the theorem on faith; nothing later in this chapter depends on it.
""")

s.text("c4-ex-smooth-not-analytic", "example", r"""
Being infinitely differentiable does not make a function analytic. Let
\[ e(x) = \begin{cases} e^{-1/x^2} & x \ne 0, \\ 0 & x = 0. \end{cases} \]
One shows by induction that for $x \ne 0$ each derivative $e^{(m)}(x)$ is $e^{-1/x^2}$ times a polynomial in $1/x$, and that such a product tends to $0$ as $x \to 0$; it follows that $e$ is infinitely differentiable on $\R$ with $e^{(m)}(0) = 0$ for every $m$. So the Taylor series of $e$ at $0$ is identically zero and converges everywhere, but it does not converge to $e$, since $e(x) > 0$ for $x \ne 0$. By uniqueness of power series coefficients no other power series centred at $0$ can represent $e$ either, so $e$ is smooth but not analytic at $0$.
""", "A smooth function that is not analytic")

s.gate("c4-ex-geometric-derivative", "exercise", "Differentiating the geometric series", r"""
For $\abs{x} < 1$,
\[ \sum_{k=1}^\infty k\,x^{k-1} = \frac{1}{(1-x)^2} . \]
""", r"""
The geometric series $\sum_{k \ge 0} x^k$ has all coefficients $c_k = 1$, so $\limsup \abs{c_k}^{1/k} = 1$ and its radius of convergence is $R = 1$. For $\abs{x} < 1$ its sum is $f(x) = 1/(1-x)$. By term-by-term differentiation of power series, $f'(x) = \sum_{k \ge 1} k x^{k-1}$ for $\abs{x} < 1$. On the other hand, differentiating $f(x) = (1-x)^{-1}$ directly gives $f'(x) = (1-x)^{-2}$. Comparing the two expressions gives the identity.
""", 1, 10, [
    r"Which familiar power series has sum $1/(1-x)$? Differentiate both sides.",
], ["c4-thm-ps-term-by-term"])

s.gate("c4-ex-log-series", "exercise", "The logarithm series", r"""
For $\abs{x} < 1$,
\[ \int_0^x \frac{dt}{1+t} = \sum_{k=0}^\infty \frac{(-1)^k}{k+1}\,x^{k+1} = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots . \]
(The left side is $\log(1+x)$.)
""", r"""
Consider the power series $\sum_{k \ge 0} (-1)^k t^k$. Its coefficients have absolute value $1$, so its radius of convergence is $R = 1$. For $\abs{t} < 1$ it is a geometric series with ratio $-t$, $\abs{-t} < 1$, so its sum is $f(t) = \dfrac{1}{1 - (-t)} = \dfrac{1}{1+t}$. By term-by-term integration of power series, for $\abs{x} < 1$
\[ \int_0^x \frac{dt}{1+t} = \int_0^x f(t)\,dt = \sum_{k=0}^\infty \frac{(-1)^k}{k+1}\,x^{k+1} . \]
""", 2, 15, [
    r"Expand the integrand $1/(1+t)$ as a geometric series and integrate term by term.",
], ["c4-thm-ps-term-by-term"])

s.card("c4-card-radius", r"Give the formula for the radius of convergence $R$ of $\sum c_k x^k$ and say what it guarantees.",
       r"$R = 1/\limsup_{k} \abs{c_k}^{1/k}$ (with $1/0 = \infty$, $1/\infty = 0$). The series converges absolutely for $\abs{x}<R$ and diverges for $\abs{x}>R$; at $\abs{x} = R$ anything can happen.", "c4-thm-radius")
s.card("c4-card-radius-idea", r"What is the idea of the proof of the Cauchy–Hadamard theorem?",
       r"Comparison with a geometric series: for $\abs{x} < \rho < R$, eventually $\abs{c_k} < \rho^{-k}$, so $\abs{c_k x^k} < (\abs{x}/\rho)^k$. For $\abs{x} > R$, $\abs{c_k x^k} > 1$ infinitely often.", "c4-thm-radius")
s.card("c4-card-ps-uniform", r"Where does a power series with radius $R$ converge uniformly? Why?",
       r"On every $[-r,r]$ with $r<R$, by the M-test with $M_k = \abs{c_k} r^k$. In general not on all of $(-R,R)$ (e.g. $\sum x^k$ on $(-1,1)$).", "c4-thm-ps-uniform")
s.card("c4-card-ps-term", r"State the theorem on term-by-term differentiation and integration of a power series.",
       r"If $f(x) = \sum c_k x^k$ on $(-R,R)$, $R > 0$, then $f'(x) = \sum_{k\ge1} k c_k x^{k-1}$ and $\int_0^x f = \sum c_k x^{k+1}/(k+1)$ for $\abs{x} < R$. The new series have the same radius $R$, because $k^{1/k} \to 1$.", "c4-thm-ps-term-by-term")
s.card("c4-card-ps-coeff", r"How are the coefficients of a power series $f(x) = \sum c_k x^k$ (with $R>0$) determined by $f$?",
       r"$c_k = f^{(k)}(0)/k!$. Hence two power series that agree on a neighbourhood of $0$ have the same coefficients.", "c4-cor-ps-smooth")
s.card("c4-card-analytic", r"Define ``$f$ is analytic at $x_0$''. Give a smooth function that is not analytic.",
       r"$f(x) = \sum c_k (x-x_0)^k$ for all $x$ in some interval $\abs{x-x_0}<\delta$. The function $e^{-1/x^2}$ (with value $0$ at $0$) is smooth with all derivatives $0$ at the origin, so its Taylor series there is $0 \ne e$.", "c4-ex-smooth-not-analytic")
s.card("c4-card-kth-root", r"Why does $k^{1/k} \to 1$?",
       r"Write $k^{1/k} = 1 + h_k$; then $k = (1+h_k)^k \ge \binom{k}{2}h_k^2$, so $h_k \le \sqrt{2/(k-1)} \to 0$.", "c4-lem-kth-root-k")

s.write()
