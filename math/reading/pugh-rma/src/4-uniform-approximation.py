import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c4_lib import Section

s = Section("4-uniform-approximation")

s.text("c4-ua-intro", "prose", r"""
A continuous function can be very complicated, yet in the sup metric it is never far from a very simple one: the Weierstrass approximation theorem says that the polynomials are dense in $C^0[a,b]$. We prove it with explicit polynomials due to Bernstein. Then we ask what was special about polynomials. The answer, the Stone–Weierstrass theorem, is that almost nothing was: any family of continuous functions on a compact space that is closed under sums and products, separates points, and does not vanish identically at any point is dense.
""")

s.text("c4-def-bernstein", "definition", r"""
For $n \in \N$ and $k = 0, 1, \dots, n$ let
\[ r_{n,k}(x) = \binom{n}{k} x^k (1-x)^{n-k} . \]
For a function $f : [0,1] \to \R$ the $n$-th \emph{Bernstein polynomial} of $f$ is
\[ B_n f(x) = \sum_{k=0}^n f\!\left(\frac{k}{n}\right) r_{n,k}(x) . \]
It is a polynomial in $x$ of degree at most $n$. Note $r_{n,k}(x) \ge 0$ for $x \in [0,1]$. (Probabilistically, $r_{n,k}(x)$ is the chance of exactly $k$ heads in $n$ tosses of a coin that lands heads with probability $x$, and $B_nf(x)$ is the expected value of $f(k/n)$.)
""", "Bernstein polynomials")

s.gate("c4-lem-bernstein-identities", "lemma", "Three binomial identities", r"""
For every $n \in \N$ and every $x \in \R$,
\[ \sum_{k=0}^n r_{n,k}(x) = 1, \qquad \sum_{k=0}^n k\, r_{n,k}(x) = nx, \qquad \sum_{k=0}^n (k - nx)^2\, r_{n,k}(x) = n x (1-x) . \]
""", r"""
Fix $y \in \R$ and regard both sides of the binomial theorem
\[ (x + y)^n = \sum_{k=0}^n \binom{n}{k} x^k y^{n-k} \qquad (1) \]
as polynomials in $x$. Differentiate with respect to $x$ and multiply by $x$:
\[ n x (x+y)^{n-1} = \sum_{k=0}^n k \binom{n}{k} x^k y^{n-k} . \qquad (2) \]
Differentiate (2) with respect to $x$ and multiply by $x$ again:
\[ n x (x+y)^{n-1} + n(n-1) x^2 (x+y)^{n-2} = \sum_{k=0}^n k^2 \binom{n}{k} x^k y^{n-k} , \qquad (3) \]
where for $n = 1$ the second term on the left is absent (its coefficient $n(n-1)$ is $0$). These identities hold for all real $x$ and $y$. Now put $y = 1 - x$, so $x + y = 1$ and $\binom{n}{k} x^k y^{n-k} = r_{n,k}(x)$:
\[ \sum_k r_{n,k}(x) = 1, \qquad \sum_k k\, r_{n,k}(x) = nx, \qquad \sum_k k^2 r_{n,k}(x) = nx + n(n-1)x^2 . \]
The first two are the first two identities claimed. For the third, expand $(k - nx)^2 = k^2 - 2nx\,k + n^2x^2$ and use all three:
\[ \sum_k (k-nx)^2 r_{n,k}(x) = nx + n(n-1)x^2 - 2nx \cdot nx + n^2x^2 = nx - nx^2 = nx(1-x) . \]
""", 3, 30, [
    r"Start from the binomial theorem for $(x+y)^n$ with $y$ an independent variable, and only at the end set $y = 1-x$.",
    r"Applying $x \frac{\partial}{\partial x}$ to $\sum \binom nk x^k y^{n-k}$ brings down a factor $k$. Do it twice to get $\sum k$ and $\sum k^2$, then expand $(k-nx)^2$.",
], ["c4-def-bernstein"])

s.gate("c4-thm-bernstein", "theorem", "Bernstein polynomials converge uniformly", r"""
If $f \in C^0[0,1]$, then $B_n f \rightrightarrows f$ on $[0,1]$.
""", r"""
Let $\eps > 0$. Since $f$ is continuous on the compact interval $[0,1]$ it is uniformly continuous and bounded: there is a $\delta > 0$ with $\abs{f(s) - f(t)} < \eps/2$ whenever $\abs{s-t} < \delta$, and $\abs{f} \le B$ where $B = \norm{f}$.

Fix $n \in \N$ and $x \in [0,1]$, and write $r_k = r_{n,k}(x) \ge 0$. Since $\sum_k r_k = 1$,
\[ B_nf(x) - f(x) = \sum_{k=0}^n \bigl( f(k/n) - f(x) \bigr) r_k , \qquad\text{so}\qquad \abs{B_nf(x) - f(x)} \le \sum_{k=0}^n \abs{f(k/n) - f(x)}\, r_k . \]
Split the indices into $K_1 = \set{k : \abs{k/n - x} < \delta}$ and $K_2 = \set{k : \abs{k/n - x} \ge \delta}$. For $k \in K_1$, $\abs{f(k/n) - f(x)} < \eps/2$, so
\[ \sum_{k \in K_1} \abs{f(k/n) - f(x)}\, r_k \le \frac{\eps}{2} \sum_{k \in K_1} r_k \le \frac{\eps}{2} . \]
For $k \in K_2$ we have $(k - nx)^2 \ge n^2\delta^2$, i.e. $1 \le (k-nx)^2/(n^2\delta^2)$, and $\abs{f(k/n) - f(x)} \le 2B$. Hence, by the third binomial identity,
\[ \sum_{k \in K_2} \abs{f(k/n) - f(x)}\, r_k \le 2B \sum_{k \in K_2} \frac{(k-nx)^2}{n^2\delta^2}\, r_k \le \frac{2B}{n^2\delta^2} \sum_{k=0}^n (k-nx)^2 r_k = \frac{2B\, x(1-x)}{n\delta^2} \le \frac{B}{2n\delta^2} , \]
using $x(1-x) \le \tfrac14$ on $[0,1]$. Altogether
\[ \abs{B_nf(x) - f(x)} \le \frac{\eps}{2} + \frac{B}{2n\delta^2} \quad \text{for all } x \in [0,1] . \]
Choose $N$ with $N > B/(\eps\delta^2)$. For $n \ge N$ the second term is less than $\eps/2$, so $\abs{B_nf(x) - f(x)} < \eps$ for all $x \in [0,1]$. Since $N$ does not depend on $x$, $B_nf \rightrightarrows f$.
""", 4, 60, [
    r"Since $\sum_k r_{n,k}(x) = 1$, write $B_nf(x) - f(x) = \sum_k (f(k/n) - f(x))\,r_{n,k}(x)$ and use uniform continuity of $f$.",
    r"Split the sum: indices with $k/n$ within $\delta$ of $x$ (where $f(k/n) - f(x)$ is small) and the rest (where you only know $\abs{f(k/n)-f(x)} \le 2\norm{f}$).",
    r"On the far indices $1 \le (k-nx)^2/(n\delta)^2$; insert this factor and use $\sum_k (k-nx)^2 r_{n,k}(x) = nx(1-x) \le n/4$.",
], ["c4-def-bernstein", "c4-lem-bernstein-identities"])

s.gate("c4-thm-weierstrass", "theorem", "Weierstrass approximation theorem", r"""
Let $a < b$. The set of polynomial functions is dense in $C^0[a,b]$: for every $f \in C^0[a,b]$ and every $\eps > 0$ there is a polynomial $p$ with $\abs{p(x) - f(x)} < \eps$ for all $x \in [a,b]$.
""", r"""
Define $g : [0,1] \to \R$ by $g(u) = f(a + (b-a)u)$. As a composition of continuous functions, $g \in C^0[0,1]$. Since the Bernstein polynomials of $g$ converge uniformly to $g$, there is an $n$ with $\abs{B_ng(u) - g(u)} < \eps$ for all $u \in [0,1]$. Let $q = B_ng$, a polynomial, and define
\[ p(x) = q\!\left( \frac{x - a}{b - a} \right) . \]
Substituting a polynomial of degree one into a polynomial gives a polynomial, so $p$ is a polynomial. For $x \in [a,b]$ the number $u = (x-a)/(b-a)$ lies in $[0,1]$ and $a + (b-a)u = x$, so $g(u) = f(x)$ and
\[ \abs{p(x) - f(x)} = \abs{q(u) - g(u)} < \eps . \]
""", 2, 15, [
    r"Reduce to $[0,1]$ by an affine change of variable, and apply the theorem on Bernstein polynomials.",
], ["c4-thm-bernstein"])

s.gate("c4-ex-moments", "exercise", "A continuous function with vanishing moments is zero", r"""
Let $f \in C^0[0,1]$ satisfy $\int_0^1 f(x)\,x^n\,dx = 0$ for every $n = 0, 1, 2, \dots$. Then $f = 0$.
""", r"""
By linearity of the integral, $\int_0^1 f p = 0$ for every polynomial $p$.

By the Weierstrass approximation theorem there are polynomials $p_n$ with $\norm{p_n - f} \to 0$. Then $f p_n \rightrightarrows f^2$ on $[0,1]$, because $\norm{f p_n - f^2} = \norm{f(p_n - f)} \le \norm{f}\,\norm{p_n - f} \to 0$. Since uniform convergence allows passing to the limit under the integral,
\[ \int_0^1 f^2 = \lim_{n \to \infty} \int_0^1 f p_n = 0 . \]
Suppose $f(x_0) \ne 0$ for some $x_0 \in [0,1]$, and put $c = f(x_0)^2 > 0$. By continuity of $f^2$ there is a $\delta > 0$ such that $f(x)^2 > c/2$ for all $x \in [0,1]$ with $\abs{x - x_0} < \delta$. The set of such $x$ contains a closed interval $J \subseteq [0,1]$ of some positive length $\ell$. Let $h : [0,1] \to \R$ be $c/2$ on $J$ and $0$ elsewhere. It is bounded with at most two discontinuities, hence integrable, and by additivity over intervals $\int_0^1 h = \tfrac{c}{2}\,\ell$ (on the pieces of $[0,1]$ outside $J$ it vanishes except possibly at one endpoint, so its integral there is $0$). Since $f^2 \ge h$ everywhere on $[0,1]$, monotonicity of the integral gives $\int_0^1 f^2 \ge \int_0^1 h = \tfrac{c}{2}\,\ell > 0$, a contradiction. Hence $f(x) = 0$ for all $x$.
""", 3, 30, [
    r"The hypothesis says $f$ is ``orthogonal'' to every polynomial. What happens if you approximate $f$ itself by polynomials?",
    r"Show $\int_0^1 f^2 = 0$ by taking $p_n \rightrightarrows f$ and passing to the limit in $\int f p_n = 0$. Then use continuity of $f$.",
], ["c4-thm-weierstrass", "c4-thm-uniform-integral", "c4-prop-sup-norm", "c4-thm-sup-metric-uniform"])

s.gate("c4-lem-abs-approx", "lemma", "Approximating the absolute value", r"""
For every $a > 0$ and $\eps > 0$ there is a polynomial $p$ with $p(0) = 0$ and
\[ \bigl|\, p(y) - \abs{y} \,\bigr| < \eps \quad \text{for all } y \in [-a,a] . \]
""", r"""
The function $y \mapsto \abs{y}$ is continuous on $[-a,a]$, so by the Weierstrass approximation theorem there is a polynomial $q$ with $\bigl|\,q(y) - \abs{y}\,\bigr| < \eps/2$ for all $y \in [-a,a]$. At $y = 0$ this gives $\abs{q(0)} < \eps/2$. Let $p(y) = q(y) - q(0)$. Then $p$ is a polynomial, $p(0) = 0$, and for $y \in [-a,a]$
\[ \bigl|\, p(y) - \abs{y} \,\bigr| \le \bigl|\, q(y) - \abs{y} \,\bigr| + \abs{q(0)} < \frac{\eps}{2} + \frac{\eps}{2} = \eps . \]
""", 2, 10, [
    r"Weierstrass gives a polynomial $q$ close to $\abs{y}$; it may not vanish at $0$, but how big can $q(0)$ be?",
], ["c4-thm-weierstrass"])

s.text("c4-def-function-algebra", "definition", r"""
Let $M$ be a nonempty compact metric space. A subset $\mathcal{A} \subseteq C^0(M)$ is a \emph{function algebra} if it is nonempty and closed under addition, scalar multiplication and multiplication: for $f, g \in \mathcal{A}$ and $c \in \R$, the functions $f + g$, $cf$ and $fg$ belong to $\mathcal{A}$.

$\mathcal{A}$ \emph{vanishes at} $p \in M$ if $f(p) = 0$ for every $f \in \mathcal{A}$; it \emph{vanishes nowhere} if for each $p \in M$ there is an $f \in \mathcal{A}$ with $f(p) \ne 0$.

$\mathcal{A}$ \emph{separates points} if for each pair of distinct points $p, q \in M$ there is an $f \in \mathcal{A}$ with $f(p) \ne f(q)$.
""", "Function algebras")

s.text("c4-ex-function-algebras", "example", r"""
\begin{itemize}
\item The polynomials form a function algebra in $C^0[a,b]$. It vanishes nowhere (it contains the constant $1$) and separates points (it contains $x$).
\item The polynomials with zero constant term form a function algebra in $C^0[0,1]$ that separates points but vanishes at $0$.
\item The even polynomials (only even powers of $x$) form a function algebra in $C^0[-1,1]$ that vanishes nowhere but does not separate $x$ from $-x$.
\item The functions $a_0 + \sum_{k=1}^n (a_k \cos kx + b_k \sin kx)$, the trigonometric polynomials, form a function algebra in $C^0[0,\pi]$, because products of sines and cosines are sums of sines and cosines.
\end{itemize}
In the second and third examples the algebra is not dense in $C^0$; the next exercise shows why, and the Stone–Weierstrass theorem shows these are the only obstructions.
""", "Examples of function algebras")

s.gate("c4-ex-sw-necessary", "exercise", "The two hypotheses are necessary", r"""
Let $M$ be a nonempty compact metric space and $\mathcal{A} \subseteq C^0(M)$ a function algebra.
\begin{enumerate}
\item If $\mathcal{A}$ vanishes at some point $p \in M$, then $\mathcal{A}$ is not dense in $C^0(M)$.
\item If there are distinct points $p, q \in M$ with $f(p) = f(q)$ for all $f \in \mathcal{A}$, then $\mathcal{A}$ is not dense in $C^0(M)$.
\end{enumerate}
""", r"""
(1) Let $F$ be the constant function $1$, which is in $C^0(M)$. For every $f \in \mathcal{A}$, $\norm{f - F} \ge \abs{f(p) - F(p)} = \abs{0 - 1} = 1$. So no element of $\mathcal{A}$ is within distance $\tfrac12$ of $F$, and $\mathcal{A}$ is not dense.

(2) Let $F(x) = d(x,p)$. This is continuous on $M$, since $\abs{d(x,p) - d(x',p)} \le d(x,x')$ by the triangle inequality; so $F \in C^0(M)$. We have $F(p) = 0$ and $F(q) = c$ where $c = d(p,q) > 0$. Let $f \in \mathcal{A}$ and put $v = f(p) = f(q)$. Then
\[ c = \abs{F(q) - F(p)} \le \abs{F(q) - v} + \abs{v - F(p)} = \abs{F(q) - f(q)} + \abs{f(p) - F(p)} \le 2\norm{f - F} . \]
So $\norm{f - F} \ge c/2$ for every $f \in \mathcal{A}$, and $\mathcal{A}$ is not dense.
""", 2, 20, [
    r"In each case exhibit one continuous function that stays a fixed distance away from every member of $\mathcal{A}$.",
    r"For (1) try a constant. For (2) you need a continuous function taking different values at $p$ and $q$; the metric provides one.",
], ["c4-def-function-algebra"])

s.gate("c4-lem-two-point", "lemma", "Two-point interpolation", r"""
Let $M$ be a nonempty compact metric space and let $\mathcal{A} \subseteq C^0(M)$ be a function algebra that vanishes nowhere and separates points.
\begin{enumerate}
\item For every $p \in M$ and $c \in \R$ there is an $f \in \mathcal{A}$ with $f(p) = c$.
\item For all distinct $p_1, p_2 \in M$ and all $c_1, c_2 \in \R$ there is an $f \in \mathcal{A}$ with $f(p_1) = c_1$ and $f(p_2) = c_2$.
\end{enumerate}
""", r"""
(1) Since $\mathcal{A}$ vanishes nowhere there is a $g \in \mathcal{A}$ with $g(p) \ne 0$. Then $f = \frac{c}{g(p)}\, g \in \mathcal{A}$ and $f(p) = c$.

(2) Choose $g_1, g_2 \in \mathcal{A}$ with $g_1(p_1) \ne 0$ and $g_2(p_2) \ne 0$, and let $g = g_1^2 + g_2^2 \in \mathcal{A}$. Then $g(p_1) \ge g_1(p_1)^2 > 0$ and $g(p_2) \ge g_2(p_2)^2 > 0$. Choose $h \in \mathcal{A}$ with $h(p_1) \ne h(p_2)$. We look for real numbers $\xi, \eta$ such that $f = \xi g + \eta\, gh \in \mathcal{A}$ has the required values, i.e.
\[ \xi\, g(p_1) + \eta\, g(p_1) h(p_1) = c_1, \qquad \xi\, g(p_2) + \eta\, g(p_2) h(p_2) = c_2 . \]
This is a linear system of two equations in the two unknowns $\xi,\eta$, whose determinant is
\[ g(p_1)\, g(p_2) h(p_2) - g(p_1) h(p_1)\, g(p_2) = g(p_1) g(p_2) \bigl( h(p_2) - h(p_1) \bigr) \ne 0 . \]
So it has a solution $(\xi,\eta)$, and the corresponding $f$ lies in $\mathcal{A}$ with $f(p_1) = c_1$, $f(p_2) = c_2$.
""", 3, 30, [
    r"First manufacture a $g \in \mathcal{A}$ that is nonzero at both $p_1$ and $p_2$; squares are useful.",
    r"With $g > 0$ at both points and $h$ separating them, look for $f = \xi g + \eta\, gh$. The two conditions are a $2 \times 2$ linear system; compute its determinant.",
], ["c4-def-function-algebra"])

s.gate("c4-lem-closure-algebra", "lemma", "The closure of a function algebra is a function algebra", r"""
Let $M$ be a nonempty compact metric space and $\mathcal{A} \subseteq C^0(M)$ a function algebra. Then its closure $\overline{\mathcal{A}}$ in $C^0(M)$ is a function algebra.
""", r"""
$\overline{\mathcal{A}} \supseteq \mathcal{A}$ is nonempty. Let $f, g \in \overline{\mathcal{A}}$ and $c \in \R$. A point is in the closure of a set exactly when it is the limit of a sequence from the set, so there are $f_n, g_n \in \mathcal{A}$ with $\norm{f_n - f} \to 0$ and $\norm{g_n - g} \to 0$. The functions $f_n + g_n$, $c f_n$, $f_n g_n$ are in $\mathcal{A}$, so it suffices to show they converge in the sup metric to $f + g$, $cf$, $fg$ respectively. By the properties of the sup norm,
\[ \norm{(f_n + g_n) - (f+g)} \le \norm{f_n - f} + \norm{g_n - g} \to 0, \qquad \norm{cf_n - cf} = \abs{c}\,\norm{f_n - f} \to 0 . \]
For the product, the convergent sequence $(f_n)$ is bounded: there is a $B$ with $\norm{f_n} \le B$ for all $n$ (for instance because $\norm{f_n} \le \norm{f} + \norm{f_n - f}$ and $\norm{f_n - f} \to 0$). Then
\[ \norm{f_n g_n - fg} = \norm{f_n (g_n - g) + (f_n - f) g} \le B\,\norm{g_n - g} + \norm{f_n - f}\,\norm{g} \to 0 . \]
Hence $f + g$, $cf$, $fg \in \overline{\mathcal{A}}$.
""", 2, 20, [
    r"Elements of the closure are sup-norm limits of sequences in $\mathcal{A}$. Show that sums, scalar multiples and products of convergent sequences converge to the right things.",
    r"For products write $f_ng_n - fg = f_n(g_n - g) + (f_n - f)g$ and use $\norm{uv} \le \norm{u}\norm{v}$ together with boundedness of $(\norm{f_n})$.",
], ["c4-def-function-algebra", "c4-prop-sup-norm"])

s.gate("c4-lem-lattice", "lemma", "A closed function algebra contains absolute values, maxima and minima", r"""
Let $M$ be a nonempty compact metric space and let $\mathcal{B} \subseteq C^0(M)$ be a function algebra that is a closed subset of $C^0(M)$. If $f, g \in \mathcal{B}$, then $\abs{f}$, $\max(f,g)$ and $\min(f,g)$ belong to $\mathcal{B}$ (these are defined pointwise). Consequently the maximum and the minimum of finitely many members of $\mathcal{B}$ belong to $\mathcal{B}$.
""", r"""
\emph{Absolute value.} Let $f \in \mathcal{B}$ and $a = \norm{f} + 1 > 0$, so $f(x) \in [-a,a]$ for all $x \in M$. For each $n \in \N$ the lemma on approximating the absolute value gives a polynomial $p_n$ with $p_n(0) = 0$ and $\bigl|\,p_n(y) - \abs{y}\,\bigr| < 1/n$ for $y \in [-a,a]$. Since $p_n$ has no constant term, $p_n(y) = \sum_{j=1}^{d} a_j y^j$ for some $d$ and real $a_j$, and so
\[ p_n \circ f = \sum_{j=1}^{d} a_j f^j \]
belongs to $\mathcal{B}$, because $\mathcal{B}$ is closed under products, scalar multiples and sums (if $p_n$ is the zero polynomial, $p_n \circ f = 0 = 0 \cdot f \in \mathcal{B}$). For every $x \in M$, taking $y = f(x)$,
\[ \bigl|\, p_n(f(x)) - \abs{f(x)} \,\bigr| < 1/n , \]
so $\norm{p_n \circ f - \abs{f}} \le 1/n \to 0$. (Here $\abs{f}$ is continuous, so it is an element of $C^0(M)$.) Thus $\abs{f}$ is the limit in $C^0(M)$ of a sequence in $\mathcal{B}$, and since $\mathcal{B}$ is closed, $\abs{f} \in \mathcal{B}$.

\emph{Max and min.} For real numbers $u, v$ we have $\max(u,v) = \tfrac12(u+v) + \tfrac12\abs{u-v}$ and $\min(u,v) = \tfrac12(u+v) - \tfrac12\abs{u-v}$. Hence
\[ \max(f,g) = \tfrac12 (f+g) + \tfrac12 \abs{f-g}, \qquad \min(f,g) = \tfrac12(f+g) - \tfrac12\abs{f-g} , \]
and these belong to $\mathcal{B}$ because $f - g \in \mathcal{B}$, hence $\abs{f-g} \in \mathcal{B}$, and $\mathcal{B}$ is closed under sums and scalar multiples.

\emph{Finitely many.} Since $\max(f_1,\dots,f_{n+1}) = \max(\max(f_1,\dots,f_n), f_{n+1})$, and similarly for $\min$, the statement for finitely many functions follows by induction on their number.
""", 4, 45, [
    r"$\max$ and $\min$ can be written with $\abs{\cdot}$, so the heart of the matter is $\abs{f} \in \mathcal{B}$.",
    r"If $p$ is a polynomial with no constant term then $p \circ f \in \mathcal{B}$. Why is the constant term a problem?",
    r"Choose polynomials $p_n$ with $p_n(0)=0$ converging uniformly to $\abs{y}$ on $[-a,a]$, $a \ge \norm{f}$. Then $p_n\circ f \to \abs{f}$ in the sup norm, and $\mathcal{B}$ is closed.",
], ["c4-lem-abs-approx", "c4-def-function-algebra"])

s.gate("c4-lem-one-sided", "lemma", "One-sided approximation fixing a point", r"""
Let $M$ be a nonempty compact metric space, $\mathcal{A} \subseteq C^0(M)$ a function algebra that vanishes nowhere and separates points, and $\mathcal{B} = \overline{\mathcal{A}}$ its closure in $C^0(M)$. Let $F \in C^0(M)$, $p \in M$ and $\eps > 0$. Then there is a $G_p \in \mathcal{B}$ such that
\[ G_p(p) = F(p) \qquad \text{and} \qquad G_p(x) > F(x) - \eps \ \text{ for all } x \in M . \]
""", r"""
For each $q \in M$ choose $H_q \in \mathcal{A}$ with $H_q(p) = F(p)$ and $H_q(q) = F(q)$: if $q \ne p$ this is possible by two-point interpolation with $c_1 = F(p)$, $c_2 = F(q)$, and if $q = p$ by its one-point version.

Let $U_q = \set{ x \in M : H_q(x) > F(x) - \eps }$. Since $H_q - F$ is continuous, $U_q$ is open, being the preimage of the open set $(-\eps, \infty)$. It contains $q$, because $H_q(q) - F(q) = 0 > -\eps$. So $\set{U_q : q \in M}$ is an open covering of the compact space $M$, and since compact metric spaces are covering compact (Chapter 2) it has a finite subcovering $U_{q_1}, \dots, U_{q_n}$, with $n \ge 1$ because $M$ is nonempty.

By the lemma on closures, $\mathcal{B}$ is a function algebra, and it is closed; it contains each $H_{q_i}$. So by the lemma on absolute values, maxima and minima,
\[ G_p = \max(H_{q_1}, \dots, H_{q_n}) \in \mathcal{B} . \]
Since $H_{q_i}(p) = F(p)$ for every $i$, $G_p(p) = F(p)$. If $x \in M$ then $x \in U_{q_i}$ for some $i$, so $G_p(x) \ge H_{q_i}(x) > F(x) - \eps$.
""", 4, 45, [
    r"For each $q$ take a function in $\mathcal{A}$ agreeing with $F$ at both $p$ and $q$. Near $q$ it is not much below $F$.",
    r"The sets where $H_q > F - \eps$ are open and cover $M$. Use compactness, then combine finitely many $H_q$ into one function that is above $F - \eps$ everywhere. Which operation does that?",
], ["c4-lem-two-point", "c4-lem-closure-algebra", "c4-lem-lattice"])

s.gate("c4-thm-stone-weierstrass", "theorem", "Stone–Weierstrass theorem", r"""
Let $M$ be a nonempty compact metric space and let $\mathcal{A} \subseteq C^0(M)$ be a function algebra that vanishes nowhere and separates points. Then $\mathcal{A}$ is dense in $C^0(M)$: for every $F \in C^0(M)$ and $\eps > 0$ there is an $f \in \mathcal{A}$ with $\norm{F - f} < \eps$.
""", r"""
Let $\mathcal{B} = \overline{\mathcal{A}}$, a closed function algebra by the lemma on closures. Let $F \in C^0(M)$. We show that for every $\eps > 0$ there is a $G \in \mathcal{B}$ with
\[ F(x) - \eps < G(x) < F(x) + \eps \quad \text{for all } x \in M . \qquad (*) \]
Then $\norm{F - G} \le \eps$; as $\eps$ is arbitrary, $F$ is a limit of elements of $\mathcal{B}$, and since $\mathcal{B}$ is closed, $F \in \mathcal{B} = \overline{\mathcal{A}}$. That says precisely that every sup-ball about $F$ contains an element of $\mathcal{A}$, which is the theorem.

Fix $\eps > 0$. For each $p \in M$ the one-sided approximation lemma gives $G_p \in \mathcal{B}$ with $G_p(p) = F(p)$ and $G_p > F - \eps$ on $M$. Let
\[ V_p = \set{ x \in M : G_p(x) < F(x) + \eps } . \]
$V_p$ is open because $G_p - F$ is continuous, and $p \in V_p$ because $G_p(p) - F(p) = 0 < \eps$. So the sets $V_p$, $p \in M$, form an open covering of $M$, and by covering compactness finitely many of them cover $M$, say $V_{p_1}, \dots, V_{p_m}$ with $m \ge 1$. Put
\[ G = \min(G_{p_1}, \dots, G_{p_m}) , \]
which lies in $\mathcal{B}$ by the lemma on absolute values, maxima and minima. For every $x \in M$: each $G_{p_i}(x) > F(x) - \eps$, so $G(x) > F(x) - \eps$; and $x \in V_{p_i}$ for some $i$, so $G(x) \le G_{p_i}(x) < F(x) + \eps$. This is $(*)$.
""", 4, 45, [
    r"Work in the closure $\mathcal{B}$ of $\mathcal{A}$, where maxima and minima are available, and aim for $G \in \mathcal{B}$ with $F - \eps < G < F + \eps$.",
    r"The one-sided lemma gives, for each $p$, a $G_p \in \mathcal{B}$ above $F - \eps$ everywhere and equal to $F$ at $p$. Near $p$ it is also below $F + \eps$.",
    r"Cover $M$ by finitely many sets $\set{G_p < F + \eps}$ and take the minimum of the corresponding $G_p$.",
], ["c4-lem-closure-algebra", "c4-lem-lattice", "c4-lem-one-sided"])

s.text("c4-rem-sw-consequences", "remark", r"""
The Weierstrass approximation theorem is the special case $M = [a,b]$, $\mathcal{A} = $ polynomials; but this is not a new proof of it, since the absolute-value lemma used the Weierstrass theorem (for the single function $\abs{y}$). What is new is the range of applications. Polynomials in $m$ variables are dense in $C^0(K)$ for every nonempty compact $K \subseteq \R^m$: they form an algebra containing the constants, and the coordinate functions separate points. Likewise the trigonometric polynomials are dense in $C^0[0,\pi]$, since they contain the constants and $\cos x$ is injective on $[0,\pi]$.
""")

s.card("c4-card-weierstrass", r"State the Weierstrass approximation theorem.",
       r"Polynomials are dense in $C^0[a,b]$: every continuous $f$ on $[a,b]$ is a uniform limit of polynomials.", "c4-thm-weierstrass")
s.card("c4-card-bernstein", r"Define the Bernstein polynomial $B_nf$ of $f \in C^0[0,1]$ and give the idea of the proof that $B_nf \rightrightarrows f$.",
       r"$B_nf(x) = \sum_{k=0}^n f(k/n)\binom nk x^k(1-x)^{n-k}$. Since the weights sum to $1$, $B_nf - f = \sum (f(k/n)-f(x)) r_k$; terms with $k/n$ near $x$ are small by uniform continuity, and the rest have total weight $\le \frac{1}{4n\delta^2}$ by $\sum (k-nx)^2 r_k = nx(1-x)$.", "c4-thm-bernstein")
s.card("c4-card-bernstein-identities", r"State the three identities for $r_{n,k}(x) = \binom nk x^k (1-x)^{n-k}$.",
       r"$\sum_k r_{n,k} = 1$, $\sum_k k\,r_{n,k} = nx$, $\sum_k (k-nx)^2 r_{n,k} = nx(1-x)$ (total probability, mean and variance of a binomial distribution).", "c4-lem-bernstein-identities")
s.card("c4-card-function-algebra", r"Define: function algebra in $C^0(M)$; vanishes nowhere; separates points.",
       r"A nonempty subset closed under $f+g$, $cf$, $fg$. Vanishes nowhere: for each $p$ some $f \in \mathcal{A}$ has $f(p) \ne 0$. Separates points: for $p \ne q$ some $f \in \mathcal{A}$ has $f(p) \ne f(q)$.", "c4-def-function-algebra")
s.card("c4-card-stone-weierstrass", r"State the Stone–Weierstrass theorem.",
       r"If $M$ is a compact metric space and $\mathcal{A} \subseteq C^0(M)$ is a function algebra that vanishes nowhere and separates points, then $\mathcal{A}$ is dense in $C^0(M)$.", "c4-thm-stone-weierstrass")
s.card("c4-card-sw-proof", r"Outline the proof of the Stone–Weierstrass theorem.",
       r"(1) Two-point interpolation in $\mathcal{A}$. (2) The closure $\mathcal{B}$ is an algebra containing $\abs{f}$ (polynomial approximation of $\abs{y}$ with no constant term), hence max and min. (3) For fixed $p$, a max of finitely many interpolants gives $G_p > F-\eps$ with $G_p(p)=F(p)$. (4) A min of finitely many $G_p$ gives $F-\eps<G<F+\eps$. Compactness is used twice.", "c4-thm-stone-weierstrass")
s.card("c4-card-sw-necessary", r"Why are ``vanishes nowhere'' and ``separates points'' needed in Stone–Weierstrass? Give examples.",
       r"If all $f \in \mathcal{A}$ vanish at $p$, the constant $1$ is at distance $\ge 1$ from $\mathcal{A}$ (polynomials without constant term on $[0,1]$). If all $f$ agree at $p \ne q$, then $d(\cdot,p)$ cannot be approximated (even polynomials on $[-1,1]$).", "c4-ex-sw-necessary")
s.card("c4-card-moments", r"If $f \in C^0[0,1]$ and $\int_0^1 f(x)x^n\,dx = 0$ for all $n \ge 0$, why is $f = 0$?",
       r"Then $\int f p = 0$ for all polynomials $p$; taking polynomials $p_n \rightrightarrows f$ gives $\int f^2 = 0$, and a continuous nonnegative function with zero integral is zero.", "c4-ex-moments")

s.write()
