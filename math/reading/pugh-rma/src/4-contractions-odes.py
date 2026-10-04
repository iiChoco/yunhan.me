import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c4_lib import Section

s = Section("4-contractions-odes")

s.text("c4-co-intro", "prose", r"""
Many problems ask for a solution of an equation of the form $f(p) = p$, a \emph{fixed point} of a map $f$. When $f$ shrinks distances by a definite factor and the space is complete, a fixed point exists, is unique, and is found by simply iterating $f$. Applied in the complete metric space $C^0$, with $f$ an integral operator, this simple principle proves that an ordinary differential equation with a Lipschitz right-hand side has exactly one solution through each initial point.
""")

s.text("c4-def-contraction", "definition", r"""
Let $M$ be a metric space and $f : M \to M$. A point $p \in M$ is a \emph{fixed point} of $f$ if $f(p) = p$. The map $f$ is a \emph{contraction} if there is a constant $k$ with $0 \le k < 1$ such that
\[ d(f(x), f(y)) \le k\, d(x,y) \quad \text{for all } x, y \in M . \]
We write $f^n$ for the $n$-fold composite $f \circ \cdots \circ f$, with $f^0 = \id$. The sequence $x, f(x), f^2(x), \dots$ is the \emph{orbit} of $x$.
""", "Contractions and fixed points")

s.gate("c4-lem-orbit-cauchy", "lemma", "Orbits of a contraction are Cauchy", r"""
Let $M$ be a metric space and $f : M \to M$ a contraction with constant $k < 1$. Let $x \in M$ and $x_n = f^n(x)$ for $n \ge 0$. Then for all $n \ge 0$ and all $m > n$,
\[ d(x_n, x_{n+1}) \le k^n\, d(x_0,x_1) \qquad \text{and} \qquad d(x_n, x_m) \le \frac{k^n}{1-k}\, d(x_0, x_1) . \]
Consequently $(x_n)$ is a Cauchy sequence.
""", r"""
The first inequality is proved by induction on $n$. For $n = 0$ it is an equality. If it holds for $n$, then
\[ d(x_{n+1}, x_{n+2}) = d(f(x_n), f(x_{n+1})) \le k\, d(x_n, x_{n+1}) \le k^{n+1} d(x_0,x_1) . \]
For $m > n$, the triangle inequality and the formula for a finite geometric sum give
\[ d(x_n, x_m) \le \sum_{j=n}^{m-1} d(x_j, x_{j+1}) \le d(x_0,x_1) \sum_{j=n}^{m-1} k^j = d(x_0,x_1)\, \frac{k^n - k^m}{1-k} \le \frac{k^n}{1-k}\, d(x_0,x_1) . \]
Let $\eps > 0$. Since $0 \le k < 1$, $k^n \to 0$, so there is an $N$ with $\frac{k^N}{1-k}\, d(x_0,x_1) < \eps$. For $m > n \ge N$ we get $d(x_n,x_m) \le \frac{k^n}{1-k} d(x_0,x_1) \le \frac{k^N}{1-k} d(x_0,x_1) < \eps$, and $d(x_n,x_n) = 0$. So $(x_n)$ is Cauchy.
""", 2, 20, [
    r"First bound the distance between consecutive points of the orbit, by induction.",
    r"For $d(x_n,x_m)$ add up consecutive steps with the triangle inequality and sum a geometric series.",
], ["c4-def-contraction"])

s.gate("c4-thm-banach", "theorem", "Banach contraction principle", r"""
Let $M$ be a nonempty complete metric space and $f : M \to M$ a contraction. Then $f$ has exactly one fixed point $p$, and for every $x \in M$ the orbit $f^n(x)$ converges to $p$ as $n \to \infty$.
""", r"""
Let $k < 1$ be a contraction constant for $f$.

\emph{Uniqueness.} If $f(p) = p$ and $f(q) = q$ then $d(p,q) = d(f(p),f(q)) \le k\,d(p,q)$, so $(1-k)\,d(p,q) \le 0$. Since $1 - k > 0$ this forces $d(p,q) = 0$, i.e. $p = q$.

\emph{Existence and convergence.} Let $x \in M$ be any point (there is one, as $M$ is nonempty) and $x_n = f^n(x)$. The orbit $(x_n)$ is Cauchy, and $M$ is complete, so $x_n \to p$ for some $p \in M$. Then
\[ d(x_{n+1}, f(p)) = d(f(x_n), f(p)) \le k\, d(x_n, p) \to 0 , \]
so $x_{n+1} \to f(p)$. But $(x_{n+1})$ is a subsequence of $(x_n)$ and so converges to $p$. By uniqueness of limits $f(p) = p$.

Thus the orbit of every point $x \in M$ converges to a fixed point of $f$; since the fixed point is unique, every orbit converges to the same point $p$.
""", 3, 30, [
    r"Uniqueness is one line from the contraction inequality. For existence, where could a fixed point come from? Iterate.",
    r"The orbit $x_n = f^n(x)$ is Cauchy, so it converges to some $p$. Compare the limits of $x_{n+1}$ and $f(x_n)$.",
], ["c4-def-contraction", "c4-lem-orbit-cauchy"])

s.gate("c4-cor-banach-rate", "corollary", "Rate of convergence", r"""
In the setting of the Banach contraction principle, with contraction constant $k$, fixed point $p$, and $x_n = f^n(x)$,
\[ d(x_n, p) \le \frac{k^n}{1-k}\, d(x_0, x_1) \quad \text{for all } n \ge 0 . \]
""", r"""
Fix $n$. For every $m > n$, the triangle inequality and the estimate for orbits give
\[ d(x_n, p) \le d(x_n, x_m) + d(x_m, p) \le \frac{k^n}{1-k}\, d(x_0,x_1) + d(x_m, p) . \]
By the Banach contraction principle $d(x_m,p) \to 0$ as $m \to \infty$. Letting $m \to \infty$ in the inequality (the left side and the first term on the right do not depend on $m$) gives the claim.
""", 2, 10, [
    r"You have a bound on $d(x_n, x_m)$ that does not depend on $m$. Let $m \to \infty$.",
], ["c4-lem-orbit-cauchy", "c4-thm-banach"])

s.gate("c4-ex-weak-contraction", "exercise", "Shrinking distances is not enough", r"""
Let $M = [1, \infty)$ with the usual metric and $f(x) = x + \dfrac1x$. Then $M$ is complete, $f$ maps $M$ into $M$, and
\[ \abs{f(x) - f(y)} < \abs{x - y} \quad \text{for all } x \ne y \text{ in } M , \]
but $f$ has no fixed point. (So in the contraction principle a constant $k < 1$ is essential.)
""", r"""
$M$ is a closed subset of the complete space $\R$, hence complete. If $x \ge 1$ then $f(x) = x + 1/x > x \ge 1$, so $f(x) \in M$.

For $x, y \in M$,
\[ f(x) - f(y) = (x - y) + \left( \frac1x - \frac1y \right) = (x-y) - \frac{x - y}{xy} = (x-y)\left( 1 - \frac{1}{xy} \right) . \]
Since $xy \ge 1$ we have $0 < \frac{1}{xy} \le 1$, so $0 \le 1 - \frac{1}{xy} < 1$. Hence for $x \ne y$, $\abs{f(x) - f(y)} = \abs{x-y}\left(1 - \frac{1}{xy}\right) < \abs{x - y}$.

A fixed point would satisfy $x + 1/x = x$, i.e. $1/x = 0$, which is impossible.
""", 2, 15, [
    r"Compute $f(x) - f(y)$ and factor out $x - y$.",
], ["c4-def-contraction"])

s.gate("c4-ex-iterate-contraction", "exercise", "A map with a contracting iterate", r"""
Let $M$ be a nonempty complete metric space and $f : M \to M$ a map (not assumed continuous) such that for some $n \in \N$ the iterate $f^n$ is a contraction. Then $f$ has exactly one fixed point.
""", r"""
Let $g = f^n$. By the Banach contraction principle $g$ has a unique fixed point $p$.

\emph{$p$ is a fixed point of $f$.} Since $g$ and $f$ are both iterates of $f$, they commute: $g \circ f = f^{n+1} = f \circ g$. Hence $g(f(p)) = f(g(p)) = f(p)$, so $f(p)$ is a fixed point of $g$. By uniqueness of the fixed point of $g$, $f(p) = p$.

\emph{Uniqueness.} If $f(q) = q$ then $g(q) = f^n(q) = q$, so $q$ is a fixed point of $g$ and therefore $q = p$.
""", 3, 20, [
    r"$f^n$ has a unique fixed point $p$. What can you say about the point $f(p)$?",
    r"$f$ commutes with $f^n$, so $f(p)$ is again fixed by $f^n$.",
], ["c4-thm-banach"])

s.text("c4-thm-brouwer", "theorem", r"""
Let $B = \set{x \in \R^m : \abs{x} \le 1}$ be the closed unit ball. Every continuous map $f : B \to B$ has a fixed point.
""", "Brouwer fixed-point theorem")

s.text("c4-rem-brouwer", "remark", r"""
Brouwer's theorem needs no contraction hypothesis, but it gives neither uniqueness nor a way to find the fixed point, and its proof is much deeper than that of the contraction principle (for $m = 1$ it is the intermediate value theorem applied to $f(x) - x$). It is stated here for contrast and taken on faith; nothing below uses it.
""")

s.text("c4-co-ode-intro", "prose", r"""
We now apply the contraction principle to differential equations. For clarity we treat a single equation $y' = f(t,y)$; the same proof, with absolute values replaced by norms in $\R^m$ and integrals taken componentwise, handles systems $y' = F(y)$ in $\R^m$.

\textbf{Standing notation.} Fix $t_0, y_0 \in \R$ and $a, b > 0$, and let
\[ Q = [t_0 - a,\, t_0 + a] \times [y_0 - b,\, y_0 + b] \subseteq \R^2 . \]
Let $f : Q \to \R$ be continuous. For $0 < \tau \le a$ put $I_\tau = [t_0 - \tau, t_0 + \tau]$. For $s, t \in I_\tau$ and an integrable $g$ we use the convention $\int_s^t g = -\int_t^s g$ when $t < s$; then $\abs{\int_s^t g} \le \abs{t - s}\,\sup\abs{g}$ in all cases.
""")

s.text("c4-def-ivp", "definition", r"""
With the standing notation, a \emph{solution of the initial value problem}
\[ y' = f(t,y), \qquad y(t_0) = y_0 \]
on $I_\tau$ is a differentiable function $y : I_\tau \to [y_0 - b, y_0 + b]$ such that $y(t_0) = y_0$ and $y'(t) = f(t, y(t))$ for every $t \in I_\tau$ (one-sided derivatives at the endpoints).

$f$ satisfies a \emph{Lipschitz condition in $y$} with constant $L \ge 0$ if
\[ \abs{f(t,y) - f(t,z)} \le L \abs{y - z} \quad \text{for all } (t,y), (t,z) \in Q . \]
""", "Initial value problem; Lipschitz condition")

s.gate("c4-lem-integral-equation", "lemma", "The integral equation", r"""
With the standing notation, let $0 < \tau \le a$ and let $y : I_\tau \to [y_0 - b, y_0 + b]$ be a function. Then $y$ is a solution of the initial value problem $y' = f(t,y)$, $y(t_0) = y_0$ on $I_\tau$ if and only if $y$ is continuous and
\[ y(t) = y_0 + \int_{t_0}^t f(s, y(s))\,ds \quad \text{for all } t \in I_\tau . \]
""", r"""
In both directions $y$ is continuous (a differentiable function is continuous). Then $s \mapsto (s, y(s))$ is a continuous map from $I_\tau$ into $Q$, because both of its components are continuous, and so the composite $g(s) = f(s, y(s))$ is a continuous real function on $I_\tau$; in particular it is integrable on every subinterval.

Suppose $y$ is a solution. Then $y' = g$ on $I_\tau$, so on any closed subinterval of $I_\tau$ the function $y$ is an antiderivative of the continuous, hence integrable, function $g$. For $t > t_0$ the antiderivative theorem of Chapter 3 on $[t_0,t]$ gives $\int_{t_0}^t g = y(t) - y(t_0)$; for $t < t_0$ it gives $\int_t^{t_0} g = y(t_0) - y(t)$, which is the same equation by the convention for reversed limits; and for $t = t_0$ both sides are $0$. So for every $t \in I_\tau$
\[ y(t) - y(t_0) = \int_{t_0}^t f(s,y(s))\,ds . \]
Since $y(t_0) = y_0$ this is the integral equation.

Conversely suppose $y$ is continuous and satisfies the integral equation. Setting $t = t_0$ gives $y(t_0) = y_0$. Fix $t \in I_\tau$ and let $\eps > 0$. By continuity of $g$ at $t$ there is a $\delta > 0$ such that $\abs{g(s) - g(t)} < \eps$ for all $s \in I_\tau$ with $\abs{s - t} < \delta$. Let $h \ne 0$ with $\abs{h} < \delta$ and $t + h \in I_\tau$. By the integral equation and additivity of the integral (with the convention for reversed limits), $y(t+h) - y(t) = \int_t^{t+h} g(s)\,ds$, and $\int_t^{t+h} g(t)\,ds = g(t)\,h$, so
\[ \abs{\frac{y(t+h) - y(t)}{h} - g(t)} = \frac{1}{\abs{h}} \abs{\int_t^{t+h} \bigl( g(s) - g(t) \bigr)\,ds} \le \frac{1}{\abs{h}}\,\abs{h}\,\eps = \eps , \]
because every $s$ between $t$ and $t+h$ has $\abs{s - t} < \delta$. Hence $y$ is differentiable at $t$ with $y'(t) = g(t) = f(t,y(t))$; at an endpoint of $I_\tau$ only $h$ of one sign occurs, and this is the one-sided derivative. (At interior points this is the fundamental theorem of calculus; the direct argument also covers the endpoints.)
""", 2, 20, [
    r"Both directions are the fundamental theorem of calculus: integrate $y'$ one way, differentiate the integral the other way (at the endpoints of $I_\tau$, check the one-sided derivative directly). What do you need to know about $s \mapsto f(s,y(s))$ first?",
], ["c4-def-ivp"])

s.gate("c4-lem-picard-space", "lemma", "The space of candidate solutions is complete", r"""
With the standing notation and $0 < \tau \le a$, let
\[ X = \set{ y \in C^0(I_\tau) : \abs{y(t) - y_0} \le b \text{ for all } t \in I_\tau } . \]
Then $X$ is a nonempty closed subset of $C^0(I_\tau)$, and hence a complete metric space in the sup metric.
""", r"""
The constant function $y_0$ belongs to $X$, so $X$ is nonempty.

Let $(y_n)$ be a sequence in $X$ converging in the sup metric to $y \in C^0(I_\tau)$. For each fixed $t \in I_\tau$, $\abs{y_n(t) - y(t)} \le \norm{y_n - y} \to 0$, so $y_n(t) \to y(t)$, and letting $n \to \infty$ in $\abs{y_n(t) - y_0} \le b$ gives $\abs{y(t) - y_0} \le b$. So $y \in X$, and $X$ is closed in $C^0(I_\tau)$.

$C^0(I_\tau)$ is complete, and a closed subset of a complete metric space is complete.
""", 1, 10, [
    r"Convergence in the sup metric implies convergence at each point, and weak inequalities survive limits.",
], ["c4-cor-c0-complete"])

s.gate("c4-lem-picard-operator", "lemma", "The Picard operator is a contraction", r"""
With the standing notation, suppose $\abs{f(t,y)} \le K$ for all $(t,y) \in Q$ and $f$ satisfies a Lipschitz condition in $y$ with constant $L$. Let $\tau > 0$ satisfy
\[ \tau \le a, \qquad K\tau \le b, \qquad L\tau < 1 , \]
and let $X$ be the space of the previous lemma. For $y \in X$ define $Ty : I_\tau \to \R$ by
\[ (Ty)(t) = y_0 + \int_{t_0}^t f(s, y(s))\,ds . \]
Then $Ty \in X$ for every $y \in X$, and $\norm{Ty - Tz} \le L\tau\, \norm{y - z}$ for all $y, z \in X$. Thus $T : X \to X$ is a contraction.
""", r"""
Let $y \in X$. As $y$ is continuous with values in $[y_0-b,y_0+b]$, the function $g(s) = f(s,y(s))$ is continuous on $I_\tau$ (a composite of continuous maps), so the integral is defined; and $\abs{g} \le K$.

\emph{$Ty$ is continuous.} For $t, t' \in I_\tau$, $\abs{(Ty)(t) - (Ty)(t')} = \abs{\int_{t'}^{t} g} \le K\abs{t - t'}$. So $Ty$ is Lipschitz, hence continuous.

\emph{$Ty$ stays in the strip.} For $t \in I_\tau$, $\abs{(Ty)(t) - y_0} = \abs{\int_{t_0}^t g} \le K\abs{t - t_0} \le K\tau \le b$. Hence $Ty \in X$.

\emph{Contraction.} Let $y, z \in X$. For every $s \in I_\tau$ the Lipschitz condition gives
\[ \abs{f(s,y(s)) - f(s,z(s))} \le L\abs{y(s) - z(s)} \le L\norm{y - z} . \]
Therefore, for $t \in I_\tau$,
\[ \abs{(Ty)(t) - (Tz)(t)} = \abs{\int_{t_0}^t \bigl( f(s,y(s)) - f(s,z(s)) \bigr)\,ds} \le \abs{t - t_0}\, L\norm{y-z} \le L\tau\,\norm{y - z} . \]
Taking the supremum over $t$, $\norm{Ty - Tz} \le L\tau\norm{y-z}$, and $L\tau < 1$.
""", 3, 35, [
    r"Three things to check: $Ty$ is continuous, its graph stays within $b$ of $y_0$, and $T$ shrinks sup distances.",
    r"Each uses $\abs{\int_s^t g} \le \abs{t-s}\sup\abs{g}$: with the bound $K$ for the first two, and with the Lipschitz condition applied inside the integral for the third.",
], ["c4-lem-picard-space", "c4-def-ivp", "c4-def-contraction"])

s.gate("c4-thm-picard", "theorem", "Picard's theorem", r"""
With the standing notation, suppose $f : Q \to \R$ is continuous, $\abs{f} \le K$ on $Q$, and $f$ satisfies a Lipschitz condition in $y$ with constant $L$. Let $\tau > 0$ satisfy $\tau \le a$, $K\tau \le b$ and $L\tau < 1$. Then the initial value problem
\[ y' = f(t,y), \qquad y(t_0) = y_0 \]
has exactly one solution on $I_\tau = [t_0 - \tau, t_0 + \tau]$. Moreover, for any $u_0 \in X$ (for instance the constant function $y_0$), the \emph{Picard iterates} $u_{n+1} = Tu_n$ converge uniformly on $I_\tau$ to the solution.
""", r"""
Let $X$ and $T$ be as in the two preceding lemmas. $X$ is a nonempty complete metric space and $T : X \to X$ is a contraction, so by the Banach contraction principle $T$ has exactly one fixed point $y \in X$, and $T^n u_0 \to y$ in the sup metric, i.e. uniformly on $I_\tau$, for every $u_0 \in X$.

\emph{Existence.} The fixed point $y$ is continuous, takes values in $[y_0-b,y_0+b]$, and satisfies $y = Ty$, which is the integral equation $y(t) = y_0 + \int_{t_0}^t f(s,y(s))\,ds$. By the lemma on the integral equation $y$ is a solution of the initial value problem on $I_\tau$.

\emph{Uniqueness.} Let $z$ be any solution on $I_\tau$. By definition $z$ maps $I_\tau$ into $[y_0-b,y_0+b]$, and by the lemma on the integral equation $z$ is continuous and satisfies the integral equation. So $z \in X$ and $Tz = z$. Since $T$ has only one fixed point, $z = y$.
""", 3, 30, [
    r"Translate ``solution'' into ``fixed point of an operator on a complete metric space''.",
    r"The integral equation says $y = Ty$. Check the hypotheses of the Banach contraction principle for $T$ on $X$, and for uniqueness check that \emph{every} solution lies in $X$.",
], ["c4-thm-banach", "c4-lem-integral-equation", "c4-lem-picard-space", "c4-lem-picard-operator"])

s.text("c4-ex-picard-iterates", "example", r"""
Take $y' = y$, $y(0) = 1$, so $f(t,y) = y$, which is Lipschitz in $y$ with $L = 1$. Starting from $u_0 = 1$ the Picard iterates are
\[ u_1(t) = 1 + \int_0^t 1\,ds = 1 + t, \qquad u_2(t) = 1 + \int_0^t (1+s)\,ds = 1 + t + \frac{t^2}{2}, \qquad \dots, \qquad u_n(t) = \sum_{k=0}^n \frac{t^k}{k!} , \]
the partial sums of the exponential series. Picard's theorem recovers $e^t$ as the unique solution near $0$.
""", "Picard iteration for $y' = y$")

s.gate("c4-ex-non-uniqueness", "exercise", "Without a Lipschitz condition uniqueness can fail", r"""
Let $f(y) = \abs{y}^{2/3}$ for $y \in \R$.
\begin{enumerate}
\item Both $y(t) = 0$ and $y(t) = t^3/27$ are differentiable on $\R$ and satisfy $y'(t) = f(y(t))$ for all $t \in \R$, with $y(0) = 0$.
\item For every $b > 0$ there is no constant $L$ with $\abs{f(y) - f(z)} \le L\abs{y - z}$ for all $y,z \in [-b,b]$.
\end{enumerate}
""", r"""
(1) For $y = 0$: $y' = 0 = \abs{0}^{2/3}$ and $y(0)=0$. For $y(t) = t^3/27$: $y(0) = 0$, $y'(t) = t^2/9$, and
\[ f(y(t)) = \left( \frac{\abs{t}^3}{27} \right)^{2/3} = \frac{\abs{t}^2}{9} = \frac{t^2}{9} = y'(t) . \]

(2) Suppose such an $L$ existed for some $b > 0$. Taking $z = 0$ and $0 < y \le b$ gives $y^{2/3} \le L y$, i.e. $y^{-1/3} \le L$, i.e. $y \ge L^{-3}$ (note $L > 0$, since $y^{2/3} > 0$). But $y = \min(b, L^{-3}/2)$ lies in $(0,b]$ and is smaller than $L^{-3}$, a contradiction.
""", 2, 15, [
    r"Part (1) is a direct computation. For (2), compare $f(y)$ with $f(0)$ for small $y > 0$: the ratio $\abs{f(y)-f(0)}/\abs{y}$ is unbounded.",
], ["c4-def-ivp"])

s.text("c4-rem-picard-scope", "remark", r"""
The solution produced by Picard's theorem is \emph{local}: it lives on a short interval $I_\tau$ about $t_0$, and the theorem can be reapplied at the endpoints to extend it. Continuity of $f$ alone still gives existence of a solution (a theorem of Peano, proved with the Arzelà–Ascoli theorem rather than the contraction principle), but, as the exercise shows, not uniqueness.
""")

s.card("c4-card-contraction", r"Define a contraction of a metric space $M$.",
       r"A map $f : M \to M$ with a constant $k < 1$ such that $d(f(x),f(y)) \le k\,d(x,y)$ for all $x,y$.", "c4-def-contraction")
s.card("c4-card-banach", r"State the Banach contraction principle.",
       r"A contraction of a nonempty complete metric space has exactly one fixed point $p$, and $f^n(x) \to p$ for every $x$; moreover $d(f^n(x),p) \le \frac{k^n}{1-k} d(x,f(x))$.", "c4-thm-banach")
s.card("c4-card-banach-proof", r"What is the idea of the proof of the contraction principle?",
       r"The orbit $x_n = f^n(x)$ has $d(x_n,x_{n+1}) \le k^n d(x_0,x_1)$, so it is Cauchy by a geometric series; its limit $p$ satisfies $f(p)=p$ by continuity of $f$. Uniqueness: $d(p,q) \le k\,d(p,q)$ forces $d(p,q)=0$.", "c4-thm-banach")
s.card("c4-card-weak-contraction", r"Does $d(f(x),f(y)) < d(x,y)$ for $x \ne y$ on a complete space guarantee a fixed point?",
       r"No: $f(x) = x + 1/x$ on $[1,\infty)$ shrinks all distances but has no fixed point. A uniform constant $k<1$ is needed.", "c4-ex-weak-contraction")
s.card("c4-card-integral-equation", r"Which integral equation is equivalent to $y' = f(t,y)$, $y(t_0) = y_0$ (for continuous $f$)?",
       r"$y(t) = y_0 + \int_{t_0}^t f(s,y(s))\,ds$ with $y$ continuous; the equivalence is the fundamental theorem of calculus.", "c4-lem-integral-equation")
s.card("c4-card-picard", r"State Picard's theorem.",
       r"If $f$ is continuous and bounded by $K$ on $[t_0-a,t_0+a] \times [y_0-b,y_0+b]$ and Lipschitz in $y$ with constant $L$, then for $\tau \le a$, $K\tau \le b$, $L\tau<1$ the problem $y'=f(t,y)$, $y(t_0)=y_0$ has exactly one solution on $[t_0-\tau,t_0+\tau]$.", "c4-thm-picard")
s.card("c4-card-picard-proof", r"How is Picard's theorem proved?",
       r"The operator $(Ty)(t) = y_0 + \int_{t_0}^t f(s,y(s))\,ds$ maps the complete space $X = \set{y \in C^0(I_\tau) : \abs{y - y_0} \le b}$ into itself (since $K\tau \le b$) and is a contraction with constant $L\tau<1$. Its unique fixed point is the unique solution.", "c4-thm-picard")
s.card("c4-card-non-unique", r"Give an initial value problem with continuous right-hand side and more than one solution.",
       r"$y' = \abs{y}^{2/3}$, $y(0)=0$: both $y=0$ and $y = t^3/27$ are solutions. $\abs{y}^{2/3}$ is not Lipschitz near $0$.", "c4-ex-non-uniqueness")

s.write()
