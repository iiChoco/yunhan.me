import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c4_lib import Section

s = Section("4-uniform-convergence")

s.text("c4-uc-intro", "prose", r"""
Until now the points of our metric spaces were numbers or vectors. In this chapter the points are \emph{functions}, and the first question is what it should mean for a sequence of functions to converge. The obvious answer, convergence at each point separately, turns out to be too weak: it does not preserve continuity, integrals, or derivatives. The right notion is \emph{uniform} convergence, which is exactly convergence with respect to a metric on a space of functions. This section sets up that metric space and shows what survives a uniform limit.
""")

s.text("c4-def-pointwise", "definition", r"""
Let $X$ be a set and let $f_n : X \to \R$ $(n \in \N)$ and $f : X \to \R$ be functions. The sequence $(f_n)$ \emph{converges pointwise} to $f$ if for every $x \in X$ the sequence of real numbers $(f_n(x))$ converges to $f(x)$. Written out: for every $x \in X$ and every $\eps > 0$ there is an $N$ (which may depend on both $x$ and $\eps$) such that $\abs{f_n(x) - f(x)} < \eps$ for all $n \ge N$.
""", "Pointwise convergence")

s.text("c4-def-uniform", "definition", r"""
With $f_n, f : X \to \R$ as before, the sequence $(f_n)$ \emph{converges uniformly} to $f$ on $X$, written $f_n \rightrightarrows f$, if for every $\eps > 0$ there is an $N$ such that
\[ \abs{f_n(x) - f(x)} < \eps \quad \text{for all } n \ge N \text{ and all } x \in X. \]
The same $N$ must serve every $x$ at once. Uniform convergence implies pointwise convergence, to the same limit.
""", "Uniform convergence")

s.gate("c4-ex-xn", "exercise", "The powers $x^n$", r"""
Let $f_n(x) = x^n$ for $x \in [0,1]$.
\begin{enumerate}
\item $(f_n)$ converges pointwise on $[0,1]$ to the function $f$ with $f(x) = 0$ for $0 \le x < 1$ and $f(1) = 1$.
\item $(f_n)$ does not converge uniformly on $[0,1)$, and hence not on $[0,1]$.
\item For each $b$ with $0 < b < 1$, $(f_n)$ converges uniformly to $0$ on $[0,b]$.
\end{enumerate}
""", r"""
(1) If $0 \le x < 1$ then $x^n \to 0$, and $1^n = 1$ for every $n$. So $f_n(x) \to f(x)$ for each $x \in [0,1]$.

(2) A uniform limit is also a pointwise limit, so if $(f_n)$ converged uniformly on $[0,1)$ the limit would be the zero function. Taking $\eps = \tfrac12$ there would be an $N$ with $x^N < \tfrac12$ for all $x \in [0,1)$. But $x_0 = (1/2)^{1/N}$ lies in $[0,1)$ and $x_0^N = \tfrac12$, which is not less than $\tfrac12$. So the convergence is not uniform on $[0,1)$. Uniform convergence on $[0,1]$ would restrict to uniform convergence on the subset $[0,1)$, so it fails too.

(3) Let $\eps > 0$. Since $0 < b < 1$ we have $b^n \to 0$, so there is an $N$ with $b^N < \eps$. For $n \ge N$ and $x \in [0,b]$,
\[ \abs{x^n - 0} = x^n \le b^n \le b^N < \eps . \]
The number $N$ does not depend on $x$, so $f_n \rightrightarrows 0$ on $[0,b]$.
""", 2, 15, [
    r"For (2), a uniform limit must equal the pointwise limit. Fix $\eps = \tfrac12$ and a candidate $N$, then look for a point $x<1$ where $x^N$ is still large.",
    r"For (3), bound $x^n$ on $[0,b]$ by a single number that does not involve $x$.",
], ["c4-def-pointwise", "c4-def-uniform"])

s.text("c4-rem-xn", "remark", r"""
In the example each $f_n$ is continuous but the pointwise limit is not. Pointwise convergence can destroy continuity; the next theorem says uniform convergence cannot.
""")

s.gate("c4-thm-uniform-limit-continuous", "theorem", "A uniform limit of continuous functions is continuous", r"""
Let $M$ be a metric space, let $f_n, f : M \to \R$, and suppose $f_n \rightrightarrows f$ on $M$. If every $f_n$ is continuous at a point $x_0 \in M$, then $f$ is continuous at $x_0$. In particular, if every $f_n$ is continuous on $M$, then so is $f$.
""", r"""
Let $\eps > 0$. By uniform convergence choose $N$ such that $\abs{f_N(x) - f(x)} < \eps/3$ for all $x \in M$. Since $f_N$ is continuous at $x_0$ there is a $\delta > 0$ such that $d(x, x_0) < \delta$ implies $\abs{f_N(x) - f_N(x_0)} < \eps/3$. Then for every $x$ with $d(x,x_0) < \delta$,
\[ \abs{f(x) - f(x_0)} \le \abs{f(x) - f_N(x)} + \abs{f_N(x) - f_N(x_0)} + \abs{f_N(x_0) - f(x_0)} < \frac{\eps}{3} + \frac{\eps}{3} + \frac{\eps}{3} = \eps . \]
So $f$ is continuous at $x_0$. If every $f_n$ is continuous at every point, this applies at every $x_0 \in M$.
""", 2, 20, [
    r"Compare $f(x)$ with $f(x_0)$ by passing through a single well-chosen $f_N$.",
    r"Three terms: $f(x) - f_N(x)$, $f_N(x) - f_N(x_0)$, $f_N(x_0) - f(x_0)$. Uniform convergence controls the first and third for every $x$ at once; continuity of the one function $f_N$ controls the middle.",
], ["c4-def-uniform"])

s.text("c4-def-sup-norm", "definition", r"""
Let $X$ be a nonempty set. $C_b(X)$ denotes the set of all \emph{bounded} functions $f : X \to \R$. For $f \in C_b(X)$ the \emph{sup norm} of $f$ is
\[ \norm{f} = \sup \set{ \abs{f(x)} : x \in X } , \]
and the \emph{sup distance} between $f, g \in C_b(X)$ is $d(f,g) = \norm{f - g}$.

If $M$ is a nonempty compact metric space, $C^0(M)$ denotes the set of continuous functions $f : M \to \R$. A continuous function on a compact space is bounded, so $C^0(M) \subseteq C_b(M)$, and $C^0(M)$ carries the sup norm and sup distance. For $M = [a,b]$ we write $C^0[a,b]$ and $C_b[a,b]$.
""", r"The sup norm, $C_b$ and $C^0$")

s.gate("c4-prop-sup-norm", "proposition", "The sup norm is a norm", r"""
Let $X$ be a nonempty set, $f, g \in C_b(X)$ and $c \in \R$. Then $f + g$, $cf$ and $fg$ belong to $C_b(X)$, and
\begin{enumerate}
\item $\norm{f} \ge 0$, with $\norm{f} = 0$ if and only if $f$ is the zero function;
\item $\norm{cf} = \abs{c}\,\norm{f}$;
\item $\norm{f + g} \le \norm{f} + \norm{g}$;
\item $\norm{fg} \le \norm{f}\,\norm{g}$.
\end{enumerate}
Consequently $d(f,g) = \norm{f-g}$ is a metric on $C_b(X)$.
""", r"""
For every $x \in X$ we have $\abs{f(x)} \le \norm{f}$ and $\abs{g(x)} \le \norm{g}$.

(3) and (4): for every $x$, $\abs{f(x) + g(x)} \le \abs{f(x)} + \abs{g(x)} \le \norm{f} + \norm{g}$ and $\abs{f(x)g(x)} \le \norm{f}\norm{g}$. So $f+g$ and $fg$ are bounded, and since the right-hand sides are upper bounds for the sets whose suprema define $\norm{f+g}$ and $\norm{fg}$, (3) and (4) hold.

(2): for every $x$, $\abs{cf(x)} = \abs{c}\abs{f(x)} \le \abs{c}\norm{f}$, so $cf$ is bounded and $\norm{cf} \le \abs{c}\norm{f}$. If $c = 0$ both sides are $0$. If $c \ne 0$, apply what was just shown to the function $cf$ and the constant $1/c$: $\norm{f} = \norm{\tfrac1c (cf)} \le \tfrac{1}{\abs{c}}\norm{cf}$, that is $\abs{c}\norm{f} \le \norm{cf}$. So equality holds.

(1): $\norm{f}$ is the supremum of a nonempty set of nonnegative numbers, so $\norm{f} \ge 0$. If $f = 0$ then $\norm{f} = 0$. If $\norm{f} = 0$ then $\abs{f(x)} \le 0$ for all $x$, so $f = 0$.

Metric: $d(f,g) = \norm{f-g} \ge 0$, and $d(f,g) = 0$ exactly when $f - g = 0$, by (1). By (2) with $c = -1$, $d(f,g) = \norm{f - g} = \norm{(-1)(g - f)} = \norm{g-f} = d(g,f)$. For $h \in C_b(X)$, (3) gives $d(f,h) = \norm{(f-g) + (g-h)} \le \norm{f-g} + \norm{g-h} = d(f,g) + d(g,h)$.
""", 1, 15, [
    r"Everything follows from the pointwise inequality $\abs{f(x)} \le \norm{f}$ and the fact that a supremum is the \emph{least} upper bound.",
], ["c4-def-sup-norm"])

s.gate("c4-thm-sup-metric-uniform", "theorem", "Convergence in the sup metric is uniform convergence", r"""
Let $X$ be a nonempty set and let $f_n, f \in C_b(X)$. Then $f_n \to f$ in the metric space $(C_b(X), d)$, that is $\norm{f_n - f} \to 0$, if and only if $f_n \rightrightarrows f$ on $X$.
""", r"""
Suppose $\norm{f_n - f} \to 0$ and let $\eps > 0$. There is an $N$ with $\norm{f_n - f} < \eps$ for $n \ge N$. For such $n$ and every $x \in X$, $\abs{f_n(x) - f(x)} \le \norm{f_n - f} < \eps$. So $f_n \rightrightarrows f$.

Conversely suppose $f_n \rightrightarrows f$ and let $\eps > 0$. There is an $N$ such that $\abs{f_n(x) - f(x)} < \eps/2$ for all $n \ge N$ and all $x \in X$. Then $\eps/2$ is an upper bound for $\set{\abs{f_n(x) - f(x)} : x \in X}$, so $\norm{f_n - f} \le \eps/2 < \eps$ for $n \ge N$. Hence $\norm{f_n - f} \to 0$.
""", 1, 10, [
    r"Unwind both definitions. In one direction a supremum of numbers each less than $\eps$ is only known to be $\le \eps$, so leave yourself room.",
], ["c4-def-uniform", "c4-def-sup-norm"])

s.gate("c4-lem-uniform-cauchy", "lemma", "Cauchy criterion for uniform convergence", r"""
Let $X$ be a set and $f_n : X \to \R$. Call $(f_n)$ \emph{uniformly Cauchy} if for every $\eps > 0$ there is an $N$ such that $\abs{f_m(x) - f_n(x)} < \eps$ for all $m, n \ge N$ and all $x \in X$. Then $(f_n)$ converges uniformly on $X$ to some function $f : X \to \R$ if and only if $(f_n)$ is uniformly Cauchy.
""", r"""
Suppose $f_n \rightrightarrows f$ and let $\eps > 0$. Choose $N$ with $\abs{f_n(x) - f(x)} < \eps/2$ for all $n \ge N$ and all $x$. Then for $m, n \ge N$ and all $x$, $\abs{f_m(x) - f_n(x)} \le \abs{f_m(x) - f(x)} + \abs{f(x) - f_n(x)} < \eps$.

Conversely suppose $(f_n)$ is uniformly Cauchy. For each fixed $x \in X$ the sequence of real numbers $(f_n(x))$ is Cauchy, so by completeness of $\R$ it converges; call its limit $f(x)$. This defines $f : X \to \R$. Let $\eps > 0$ and choose $N$ such that $\abs{f_m(x) - f_n(x)} < \eps/2$ for all $m,n \ge N$ and all $x$. Fix $n \ge N$ and $x \in X$ and let $m \to \infty$: since $f_m(x) \to f(x)$ and weak inequalities pass to limits,
\[ \abs{f(x) - f_n(x)} \le \eps/2 < \eps . \]
This holds for all $n \ge N$ and all $x \in X$ with the same $N$, so $f_n \rightrightarrows f$.
""", 2, 20, [
    r"For the hard direction, first find a candidate limit: what does uniformly Cauchy say at a single point $x$?",
    r"Define $f(x) = \lim_n f_n(x)$ using completeness of $\R$. Then in $\abs{f_m(x) - f_n(x)} < \eps/2$ hold $n$ and $x$ fixed and let $m \to \infty$.",
], ["c4-def-uniform"])

s.gate("c4-thm-cb-complete", "theorem", r"$C_b$ is complete", r"""
For every nonempty set $X$, the metric space $C_b(X)$ with the sup distance is complete.
""", r"""
Let $(f_n)$ be a Cauchy sequence in $C_b(X)$. Given $\eps > 0$ there is an $N$ with $\norm{f_m - f_n} < \eps$ for $m,n \ge N$, and then $\abs{f_m(x) - f_n(x)} \le \norm{f_m - f_n} < \eps$ for all $x$. So $(f_n)$ is uniformly Cauchy, and by the Cauchy criterion for uniform convergence there is a function $f : X \to \R$ with $f_n \rightrightarrows f$.

$f$ is bounded: choose $N$ with $\abs{f_N(x) - f(x)} < 1$ for all $x$; then $\abs{f(x)} < 1 + \abs{f_N(x)} \le 1 + \norm{f_N}$ for all $x$. So $f \in C_b(X)$.

Since $f_n, f \in C_b(X)$ and $f_n \rightrightarrows f$, convergence in the sup metric being the same as uniform convergence gives $\norm{f_n - f} \to 0$. Thus every Cauchy sequence in $C_b(X)$ converges in $C_b(X)$.
""", 2, 20, [
    r"A Cauchy sequence for the sup distance is uniformly Cauchy.",
    r"After producing the uniform limit $f$, two things remain: $f$ is bounded, and the convergence is convergence in the metric.",
], ["c4-lem-uniform-cauchy", "c4-thm-sup-metric-uniform", "c4-def-sup-norm"])

s.gate("c4-cor-c0-complete", "corollary", r"$C^0$ is a closed subset of $C_b$, hence complete", r"""
Let $M$ be a nonempty compact metric space. Then $C^0(M)$ is a closed subset of $C_b(M)$, and $C^0(M)$ with the sup distance is a complete metric space. In particular $C^0[a,b]$ is complete.
""", r"""
Let $(f_n)$ be a sequence in $C^0(M)$ that converges in $C_b(M)$ to some $f \in C_b(M)$. Then $f_n \rightrightarrows f$, because convergence in the sup metric is uniform convergence, and a uniform limit of continuous functions is continuous, so $f \in C^0(M)$. Thus $C^0(M)$ contains the limit of each of its sequences that converges in $C_b(M)$, which means it is closed in $C_b(M)$.

$C_b(M)$ is complete, and a closed subset of a complete metric space is complete. So $C^0(M)$ is complete. The interval $[a,b]$ is compact, so this applies to $C^0[a,b]$.
""", 1, 10, [
    r"Closed means: contains the limits of its convergent sequences. Which two earlier theorems say a sup-metric limit of continuous functions is continuous?",
], ["c4-thm-sup-metric-uniform", "c4-thm-uniform-limit-continuous", "c4-thm-cb-complete"])

s.text("c4-uc-integral-intro", "prose", r"""
Next, integrals. Throughout, ``integrable'' means Riemann integrable on $[a,b]$ with $a < b$, and we use two results of Chapter 3. First, Riemann integrable functions are bounded. Second, Riemann's integrability criterion, in the form it takes once Riemann and Darboux integrability are known to agree: a bounded function $f$ on $[a,b]$ is Riemann integrable if and only if for every $\eps > 0$ there is a partition $P$ of $[a,b]$ whose upper and lower sums satisfy $U(f,P) - L(f,P) < \eps$. Here $U(f,P) = \sum_i M_i\,\Delta x_i$ and $L(f,P) = \sum_i m_i\,\Delta x_i$, with $M_i$ and $m_i$ the supremum and infimum of $f$ on the $i$-th interval of $P$.
""")

s.gate("c4-thm-uniform-integral", "theorem", "Uniform limits and integrals", r"""
Let $f_n : [a,b] \to \R$ be Riemann integrable for each $n$, and suppose $f_n \rightrightarrows f$ on $[a,b]$. Then $f$ is Riemann integrable and
\[ \lim_{n \to \infty} \int_a^b f_n(x)\,dx = \int_a^b f(x)\,dx . \]
""", r"""
\emph{$f$ is bounded.} Choose $N_0$ with $\abs{f(x) - f_{N_0}(x)} < 1$ for all $x$. The Riemann integrable function $f_{N_0}$ is bounded (integrable functions are bounded), say $\abs{f_{N_0}} \le B$, so $\abs{f(x)} < 1 + B$ for all $x$.

\emph{$f$ is integrable.} Let $\eps > 0$ and put $\eta = \eps / (3(b-a))$. Choose $N$ with $\abs{f(x) - f_N(x)} < \eta$ for all $x \in [a,b]$. Since $f_N$ is bounded and integrable, Riemann's integrability criterion gives a partition $P : a = x_0 < x_1 < \dots < x_k = b$ with $U(f_N, P) - L(f_N, P) < \eps/3$. On the $i$-th subinterval $I_i = [x_{i-1},x_i]$ let $M_i(g)$ and $m_i(g)$ denote the supremum and infimum of a bounded function $g$. For $x \in I_i$,
\[ f(x) < f_N(x) + \eta \le M_i(f_N) + \eta, \qquad f(x) > f_N(x) - \eta \ge m_i(f_N) - \eta , \]
so $M_i(f) \le M_i(f_N) + \eta$ and $m_i(f) \ge m_i(f_N) - \eta$. Therefore
\[ U(f,P) - L(f,P) = \sum_{i=1}^k \bigl(M_i(f) - m_i(f)\bigr)(x_i - x_{i-1}) \le U(f_N,P) - L(f_N,P) + 2\eta(b-a) < \frac{\eps}{3} + \frac{2\eps}{3} = \eps . \]
Since $f$ is bounded and $\eps > 0$ was arbitrary, Riemann's integrability criterion shows $f$ is integrable.

\emph{The integrals converge.} Let $\eps > 0$ and choose $N$ so that $\abs{f_n(x) - f(x)} < \eps/(2(b-a))$ for all $n \ge N$ and all $x$. For such $n$ the integrable function $f_n - f$ lies between the constants $-\eps/(2(b-a))$ and $\eps/(2(b-a))$, so by linearity and monotonicity of the integral
\[ \abs{\int_a^b f_n - \int_a^b f} = \abs{\int_a^b (f_n - f)} \le \frac{\eps}{2(b-a)}\,(b-a) = \frac{\eps}{2} < \eps . \]
Hence $\int_a^b f_n \to \int_a^b f$.
""", 3, 40, [
    r"There are two things to prove. For integrability use Riemann's integrability criterion: first check $f$ is bounded, then find one partition with $U(f,P) - L(f,P) < \eps$.",
    r"Take $f_N$ uniformly within $\eta$ of $f$ and a partition that works for $f_N$. How do $\sup f$ and $\inf f$ on a subinterval compare with those of $f_N$?",
    r"For the limit of the integrals, $\abs{\int (f_n - f)} \le (b-a)\sup\abs{f_n - f}$.",
], ["c4-def-uniform"])

s.gate("c4-cor-indefinite-integrals", "corollary", "Indefinite integrals converge uniformly", r"""
Let $f_n : [a,b] \to \R$ be Riemann integrable with $f_n \rightrightarrows f$ on $[a,b]$. Define $F_n(x) = \int_a^x f_n(t)\,dt$ and $F(x) = \int_a^x f(t)\,dt$ for $x \in [a,b]$. Then $F_n \rightrightarrows F$ on $[a,b]$.
""", r"""
By the theorem on uniform limits and integrals $f$ is integrable on $[a,b]$, hence on each $[a,x]$, so $F$ is defined. Let $\eps > 0$ and choose $N$ so that $\abs{f_n(t) - f(t)} < \eps/(2(b-a))$ for all $n \ge N$ and $t \in [a,b]$. For $n \ge N$ and $x \in (a,b]$, monotonicity of the integral on $[a,x]$ gives
\[ \abs{F_n(x) - F(x)} = \abs{\int_a^x (f_n - f)} \le \frac{\eps}{2(b-a)}\,(x - a) \le \frac{\eps}{2} < \eps , \]
and $F_n(a) - F(a) = 0$. The number $N$ does not depend on $x$, so $F_n \rightrightarrows F$.
""", 2, 15, [
    r"Estimate $\abs{F_n(x) - F(x)}$ by an integral of $\abs{f_n - f}$ over $[a,x]$, and bound the length of $[a,x]$ by $b-a$.",
], ["c4-thm-uniform-integral"])

s.text("c4-ex-steeple", "example", r"""
Pointwise convergence is not enough for either conclusion.

\emph{Growing steeples.} For $n \ge 2$ let $f_n : [0,1] \to \R$ be the continuous function whose graph is the triangle with vertices $(0,0)$, $(1/n, n)$, $(2/n, 0)$, and which is $0$ on $[2/n, 1]$. Then $f_n(0) = 0$ and for each $x > 0$, $f_n(x) = 0$ as soon as $2/n < x$; so $f_n \to 0$ pointwise. But $\int_0^1 f_n = 1$ for every $n$, while $\int_0^1 0 = 0$.

\emph{Losing integrability.} List the rationals in $[0,1]$ as $q_1, q_2, \dots$ and let $g_n$ be $1$ at $q_1,\dots,q_n$ and $0$ elsewhere. Each $g_n$ is integrable (it is zero except at finitely many points), and $g_n$ converges pointwise to the indicator function of $\Q \cap [0,1]$, which is not Riemann integrable.
""", "Pointwise limits and integrals")

s.text("c4-uc-derivative-intro", "prose", r"""
Derivatives are more delicate. The functions $f_n(x) = \sqrt{x^2 + 1/n}$ are differentiable on $[-1,1]$ and converge uniformly to $\abs{x}$, since $0 \le \sqrt{x^2 + 1/n} - \abs{x} \le 1/\sqrt{n}$; yet the limit is not differentiable at $0$. Uniform convergence of the functions says nothing about their slopes. What is needed is uniform convergence of the \emph{derivatives}. On a closed interval $[a,b]$, ``differentiable'' means differentiable at each point, with one-sided derivatives at $a$ and $b$.
""")

s.gate("c4-thm-uniform-derivative", "theorem", "Uniform limits and derivatives", r"""
Let $f_n : [a,b] \to \R$ be differentiable for each $n$. Suppose $(f_n)$ converges pointwise on $[a,b]$ to a function $f$, and the derivatives converge uniformly on $[a,b]$ to a function $g$: $f_n' \rightrightarrows g$. Then $f$ is differentiable on $[a,b]$ and $f' = g$.
""", r"""
Fix $x \in [a,b]$. For each $n$ define $\varphi_n : [a,b] \to \R$ by
\[ \varphi_n(t) = \frac{f_n(t) - f_n(x)}{t - x} \quad (t \ne x), \qquad \varphi_n(x) = f_n'(x) . \]
By the definition of the derivative, $\varphi_n(t) \to \varphi_n(x)$ as $t \to x$; that is, $\varphi_n$ is continuous at $x$.

\emph{$(\varphi_n)$ is uniformly Cauchy.} Let $\eps > 0$. Since $f_n' \rightrightarrows g$ there is an $N$ with $\abs{f_n'(\theta) - g(\theta)} < \eps/2$ for all $n \ge N$ and $\theta \in [a,b]$, hence $\abs{f_m'(\theta) - f_n'(\theta)} < \eps$ for all $m,n \ge N$ and all $\theta$. Fix $m, n \ge N$ and put $h = f_m - f_n$, a differentiable function on $[a,b]$. For $t \ne x$ the mean value theorem on the interval between $x$ and $t$ gives a $\theta$ between them with $h(t) - h(x) = h'(\theta)(t - x)$, so
\[ \abs{\varphi_m(t) - \varphi_n(t)} = \abs{\frac{h(t) - h(x)}{t - x}} = \abs{h'(\theta)} = \abs{f_m'(\theta) - f_n'(\theta)} < \eps . \]
At $t = x$, $\abs{\varphi_m(x) - \varphi_n(x)} = \abs{f_m'(x) - f_n'(x)} < \eps$ as well. So $(\varphi_n)$ is uniformly Cauchy on $[a,b]$.

\emph{The limit.} By the Cauchy criterion for uniform convergence, $\varphi_n \rightrightarrows \varphi$ for some $\varphi : [a,b] \to \R$. Each $\varphi_n$ is continuous at $x$, so $\varphi$ is continuous at $x$, because a uniform limit of functions continuous at a point is continuous at that point. The uniform limit is also the pointwise limit, and the pointwise limit can be computed: for $t \ne x$, $\varphi_n(t) \to \dfrac{f(t) - f(x)}{t - x}$ because $f_n \to f$ pointwise, while $\varphi_n(x) = f_n'(x) \to g(x)$. Hence
\[ \varphi(t) = \frac{f(t) - f(x)}{t - x} \quad (t \ne x), \qquad \varphi(x) = g(x) . \]
Continuity of $\varphi$ at $x$ now says $\lim_{t \to x} \dfrac{f(t) - f(x)}{t - x} = g(x)$. So $f$ is differentiable at $x$ with $f'(x) = g(x)$; and $x \in [a,b]$ was arbitrary.
""", 4, 60, [
    r"Fix $x$ and study the difference quotients $\varphi_n(t) = (f_n(t) - f_n(x))/(t-x)$, extended by $\varphi_n(x) = f_n'(x)$. What property of $\varphi_n$ at $t = x$ expresses differentiability?",
    r"Show $(\varphi_n)$ is uniformly Cauchy: apply the mean value theorem to $f_m - f_n$ to turn $\varphi_m(t) - \varphi_n(t)$ into a value of $f_m' - f_n'$.",
    r"The uniform limit $\varphi$ is continuous at $x$ and equals the pointwise limit; read off what continuity of $\varphi$ at $x$ says.",
], ["c4-lem-uniform-cauchy", "c4-thm-uniform-limit-continuous"])

s.text("c4-def-series-functions", "definition", r"""
Let $f_k : X \to \R$ for $k = 0, 1, 2, \dots$, with partial sums $S_n(x) = \sum_{k=0}^n f_k(x)$. The series $\sum f_k$ \emph{converges pointwise} (respectively \emph{uniformly}) on $X$ to $S : X \to \R$ if $S_n \to S$ pointwise (respectively $S_n \rightrightarrows S$ on $X$). We then write $S = \sum_{k=0}^\infty f_k$. The same language is used when the index starts at $k = 1$.
""", "Series of functions")

s.gate("c4-thm-m-test", "theorem", "Weierstrass M-test", r"""
Let $f_k : X \to \R$ and suppose there are constants $M_k \ge 0$ with $\abs{f_k(x)} \le M_k$ for all $x \in X$ and all $k$, such that $\sum M_k$ converges. Then $\sum f_k$ converges uniformly on $X$, and $\sum f_k(x)$ converges absolutely for each $x \in X$.
""", r"""
For each $x$, $\sum \abs{f_k(x)}$ converges by comparison with $\sum M_k$; this is the absolute convergence.

Let $S_n$ be the $n$-th partial sum of $\sum f_k$ and $T_n$ that of $\sum M_k$. Let $\eps > 0$. The convergent sequence $(T_n)$ is Cauchy, so there is an $N$ with $T_n - T_m = \sum_{k=m+1}^n M_k < \eps$ whenever $n > m \ge N$. For such $m,n$ and every $x \in X$,
\[ \abs{S_n(x) - S_m(x)} = \abs{\sum_{k=m+1}^n f_k(x)} \le \sum_{k=m+1}^n \abs{f_k(x)} \le \sum_{k=m+1}^n M_k < \eps . \]
When $m = n$ the left side is $0$. So $(S_n)$ is uniformly Cauchy, and by the Cauchy criterion for uniform convergence it converges uniformly on $X$.
""", 2, 20, [
    r"You do not know the limit in advance, so use the Cauchy criterion for uniform convergence on the partial sums.",
    r"$\abs{S_n(x) - S_m(x)} \le \sum_{k=m+1}^n M_k$, and the right side is a difference of partial sums of a convergent series of constants.",
], ["c4-lem-uniform-cauchy", "c4-def-series-functions"])

s.gate("c4-thm-term-integration", "theorem", "Term-by-term integration and continuity", r"""
Let $f_k : [a,b] \to \R$ and suppose $\sum f_k$ converges uniformly on $[a,b]$ to $S$.
\begin{enumerate}
\item If every $f_k$ is continuous, then $S$ is continuous.
\item If every $f_k$ is Riemann integrable, then $S$ is Riemann integrable and
\[ \int_a^b S(x)\,dx = \sum_{k=0}^\infty \int_a^b f_k(x)\,dx , \]
the series of numbers on the right being convergent.
\end{enumerate}
""", r"""
Let $S_n = \sum_{k=0}^n f_k$, so $S_n \rightrightarrows S$.

(1) A finite sum of continuous functions is continuous, so each $S_n$ is continuous, and a uniform limit of continuous functions is continuous.

(2) A finite sum of integrable functions is integrable and $\int_a^b S_n = \sum_{k=0}^n \int_a^b f_k$ by linearity. By the theorem on uniform limits and integrals, $S$ is integrable and $\int_a^b S_n \to \int_a^b S$. That is, the partial sums $\sum_{k=0}^n \int_a^b f_k$ of the series $\sum \int_a^b f_k$ converge to $\int_a^b S$, which is the assertion.
""", 1, 10, [
    r"A series is the sequence of its partial sums; apply the theorems about uniformly convergent sequences to $S_n$.",
], ["c4-def-series-functions", "c4-thm-uniform-limit-continuous", "c4-thm-uniform-integral"])

s.gate("c4-thm-term-differentiation", "theorem", "Term-by-term differentiation", r"""
Let $f_k : [a,b] \to \R$ be differentiable for each $k$. Suppose $\sum f_k$ converges pointwise on $[a,b]$ to $S$ and the series of derivatives $\sum f_k'$ converges uniformly on $[a,b]$ to $G$. Then $S$ is differentiable on $[a,b]$ and
\[ S'(x) = G(x) = \sum_{k=0}^\infty f_k'(x) \quad \text{for all } x \in [a,b] . \]
""", r"""
Let $S_n = \sum_{k=0}^n f_k$. Each $S_n$ is differentiable with $S_n' = \sum_{k=0}^n f_k'$, which is the $n$-th partial sum of $\sum f_k'$. By hypothesis $S_n \to S$ pointwise and $S_n' \rightrightarrows G$ on $[a,b]$. The theorem on uniform limits and derivatives, applied to the sequence $(S_n)$, says $S$ is differentiable with $S' = G$.
""", 1, 10, [
    r"Apply the theorem on uniform limits and derivatives to the partial sums.",
], ["c4-def-series-functions", "c4-thm-uniform-derivative"])

s.card("c4-card-pointwise-uniform", r"State the definitions of pointwise and of uniform convergence $f_n \to f$ on a set $X$. What is the difference?",
       r"Pointwise: for every $x$ and $\eps>0$ there is $N$ with $\abs{f_n(x)-f(x)}<\eps$ for $n\ge N$. Uniform: for every $\eps>0$ there is $N$ with $\abs{f_n(x)-f(x)}<\eps$ for all $n \ge N$ and all $x \in X$. In the uniform case $N$ may not depend on $x$.", "c4-def-uniform")
s.card("c4-card-xn", r"Give a sequence of continuous functions on $[0,1]$ converging pointwise but not uniformly.",
       r"$f_n(x) = x^n$: the limit is $0$ on $[0,1)$ and $1$ at $x=1$, which is discontinuous, so the convergence cannot be uniform. (It is uniform on $[0,b]$ for $b<1$.)", "c4-ex-xn")
s.card("c4-card-uniform-limit-continuous", r"Why is a uniform limit of continuous functions continuous? Give the idea in one line.",
       r"The $\eps/3$ argument: $\abs{f(x)-f(x_0)} \le \abs{f(x)-f_N(x)} + \abs{f_N(x)-f_N(x_0)} + \abs{f_N(x_0)-f(x_0)}$, with the outer terms small by uniform convergence and the middle one by continuity of $f_N$.", "c4-thm-uniform-limit-continuous")
s.card("c4-card-sup-norm", r"Define the sup norm on $C_b(X)$. What does convergence in the metric $d(f,g) = \norm{f-g}$ mean?",
       r"$\norm{f} = \sup\set{\abs{f(x)} : x \in X}$. $\norm{f_n - f} \to 0$ if and only if $f_n \rightrightarrows f$.", "c4-thm-sup-metric-uniform")
s.card("c4-card-cb-complete", r"Are $C_b(X)$ and $C^0[a,b]$ complete in the sup metric? Why?",
       r"Yes. A Cauchy sequence is uniformly Cauchy, so it converges pointwise by completeness of $\R$, and the convergence is uniform; the limit is bounded. $C^0$ is a closed subset of $C_b$ because uniform limits of continuous functions are continuous.", "c4-cor-c0-complete")
s.card("c4-card-uniform-integral", r"State the theorem on uniform convergence and the Riemann integral.",
       r"If $f_n$ are Riemann integrable on $[a,b]$ and $f_n \rightrightarrows f$, then $f$ is Riemann integrable and $\int_a^b f_n \to \int_a^b f$. (Pointwise convergence is not enough: growing steeples.)", "c4-thm-uniform-integral")
s.card("c4-card-uniform-derivative", r"State the theorem on uniform convergence and differentiation. Why is uniform convergence of $f_n$ alone not enough?",
       r"If $f_n$ are differentiable on $[a,b]$, $f_n \to f$ pointwise and $f_n' \rightrightarrows g$, then $f$ is differentiable and $f' = g$. Counterexample without the hypothesis on $f_n'$: $\sqrt{x^2+1/n} \rightrightarrows \abs{x}$.", "c4-thm-uniform-derivative")
s.card("c4-card-m-test", r"State the Weierstrass M-test and the idea of its proof.",
       r"If $\abs{f_k(x)} \le M_k$ for all $x$ and $\sum M_k < \infty$, then $\sum f_k$ converges uniformly (and absolutely). Idea: the partial sums are uniformly Cauchy because $\abs{S_n - S_m} \le \sum_{k=m+1}^n M_k$.", "c4-thm-m-test")
s.card("c4-card-term-by-term", r"When may a series of functions on $[a,b]$ be integrated term by term? Differentiated term by term?",
       r"Integrated: when the $f_k$ are integrable and $\sum f_k$ converges uniformly. Differentiated: when the $f_k$ are differentiable, $\sum f_k$ converges (pointwise) and $\sum f_k'$ converges uniformly.", "c4-thm-term-differentiation")

s.write()
