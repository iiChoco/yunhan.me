from __future__ import annotations
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from c1_common import Section

s = Section("1-euclidean-space")

s.prose("euclid-intro", r"""
Analysis in several variables takes place in $\R^m$, the set of $m$-tuples of real numbers. Its geometry (length, distance, angle) comes from one algebraic object, the dot product, and from one inequality, Cauchy–Schwarz. This section sets up that geometry and isolates the abstract notions behind it, inner products and norms, which return later for spaces of functions. The algebra of vector spaces is assumed from linear algebra.
""")

s.definition("def-rm", "Euclidean space", r"""
For $m \in \N$, \emph{Euclidean $m$-space} $\R^m$ is the set of ordered $m$-tuples $x = (x_1, \dots, x_m)$ of real numbers; its elements are called \emph{vectors} or \emph{points}, and $x_i$ is the $i$th \emph{coordinate} of $x$. Vectors are added and multiplied by \emph{scalars} $c \in \R$ coordinatewise:
\[ x + y = (x_1 + y_1, \dots, x_m + y_m), \qquad cx = (cx_1, \dots, cx_m). \]
With these operations $\R^m$ is a real vector space; its zero vector is $0 = (0, \dots, 0)$, and $x - y = x + (-1)y$. The \emph{standard basis vectors} are $e_1 = (1, 0, \dots, 0), \dots, e_m = (0, \dots, 0, 1)$.
""")

s.definition("def-dot-product", "Dot product", r"""
The \emph{dot product} of $x, y \in \R^m$ is the real number
\[ \inner{x}{y} = x_1 y_1 + \dots + x_m y_m. \]
""")

s.result("prop-dot-properties", "proposition", "Properties of the dot product", r"""
For all $x, x', y \in \R^m$ and $c \in \R$:
\begin{enumerate}
\item $\inner{x + x'}{y} = \inner{x}{y} + \inner{x'}{y}$ and $\inner{cx}{y} = c\inner{x}{y}$ (linearity in the first variable);
\item $\inner{x}{y} = \inner{y}{x}$ (symmetry);
\item $\inner{x}{x} \ge 0$, and $\inner{x}{x} = 0$ if and only if $x = 0$ (positive definiteness).
\end{enumerate}
""", r"""
(1) By the distributive law in $\R$,
\[ \inner{x + x'}{y} = \sum_{i=1}^m (x_i + x_i')y_i = \sum_{i=1}^m x_i y_i + \sum_{i=1}^m x_i' y_i = \inner{x}{y} + \inner{x'}{y}, \]
and $\inner{cx}{y} = \sum_i (c x_i) y_i = c \sum_i x_i y_i = c \inner{x}{y}$.

(2) $\inner{x}{y} = \sum_i x_i y_i = \sum_i y_i x_i = \inner{y}{x}$ because multiplication in $\R$ is commutative.

(3) $\inner{x}{x} = \sum_i x_i^2$ is a sum of squares, each of which is $\ge 0$, so $\inner{x}{x} \ge 0$. If $x = 0$ every term is $0$ and $\inner{x}{x} = 0$. If $x \ne 0$ then some coordinate $x_j \ne 0$, so $x_j^2 > 0$, and since the other terms are $\ge 0$, $\inner{x}{x} \ge x_j^2 > 0$.
""", 1, 10, [
    r"Write each side as a sum over coordinates and use the field axioms of $\R$.",
    r"For (3): a sum of nonnegative numbers is at least as large as each of its terms.",
], ["def-rm", "def-dot-product"])

s.definition("def-inner-product", "Inner product, length", r"""
Let $V$ be a vector space over $\R$. An \emph{inner product} on $V$ is a function that assigns to each pair $x, y \in V$ a real number $\inner{x}{y}$ and has the three properties of the preceding proposition: it is linear in the first variable, symmetric, and positive definite. By symmetry it is then linear in the second variable as well, so it is \emph{bilinear}. A vector space with a chosen inner product is an \emph{inner product space}. The \emph{length} (or \emph{magnitude}) of $x \in V$ is
\[ \abs{x} = \sqrt{\inner{x}{x}}, \]
which makes sense because nonnegative real numbers have square roots. In $\R^m$ with the dot product this is the \emph{Euclidean length} $\abs{x} = \sqrt{x_1^2 + \dots + x_m^2}$; for $m = 1$ it is the absolute value.
""")

s.remark("rem-square-compare", r"""
Lengths are defined through their squares, so the following fact about real numbers is used repeatedly: if $u \ge 0$, $v \ge 0$ and $u^2 \le v^2$, then $u \le v$. (Otherwise $u > v \ge 0$ would give $u^2 > v^2$.) Note also that $\abs{x}^2 = \inner{x}{x}$, and that $\inner{x}{0} = \inner{x}{0 \cdot 0} = 0 \cdot \inner{x}{0} = 0$ for every $x$.
""")

s.result("thm-cauchy-schwarz", "theorem", "Cauchy–Schwarz inequality", r"""
Let $V$ be an inner product space. For all $x, y \in V$,
\[ \abs{\inner{x}{y}} \le \abs{x}\,\abs{y}. \]
In particular, for $x, y \in \R^m$: $\ \abs{x_1 y_1 + \dots + x_m y_m} \le \sqrt{x_1^2 + \dots + x_m^2}\,\sqrt{y_1^2 + \dots + y_m^2}$.
""", r"""
If $y = 0$ then $\inner{x}{y} = 0$ and $\abs{y} = 0$, so both sides are $0$. Assume $y \ne 0$, so that $\inner{y}{y} > 0$ by positive definiteness. For every $t \in \R$, positive definiteness and bilinearity give
\[ 0 \le \inner{x + ty}{x + ty} = \inner{x}{x} + 2t\inner{x}{y} + t^2 \inner{y}{y}. \]
Take $t = -\inner{x}{y}/\inner{y}{y}$. Then
\[ 0 \le \inner{x}{x} - \frac{2\inner{x}{y}^2}{\inner{y}{y}} + \frac{\inner{x}{y}^2}{\inner{y}{y}} = \inner{x}{x} - \frac{\inner{x}{y}^2}{\inner{y}{y}}, \]
and multiplying by $\inner{y}{y} > 0$ gives
\[ \inner{x}{y}^2 \le \inner{x}{x}\inner{y}{y} = \big(\abs{x}\abs{y}\big)^2. \]
The numbers $\abs{\inner{x}{y}}$ and $\abs{x}\abs{y}$ are nonnegative, and the square of the first is $\inner{x}{y}^2$; so the inequality between squares gives $\abs{\inner{x}{y}} \le \abs{x}\abs{y}$. The statement for $\R^m$ is the special case of the dot product.
""", 3, 40, [
    r"The only inequality available is positive definiteness: $\inner{v}{v} \ge 0$ for every vector $v$. Apply it to a well-chosen combination of $x$ and $y$.",
    r"Expand $\inner{x + ty}{x + ty} \ge 0$ as a quadratic in the real variable $t$.",
    r"Treat $y = 0$ separately; otherwise choose $t = -\inner{x}{y}/\inner{y}{y}$, the value that minimises the quadratic.",
], ["def-inner-product", "prop-dot-properties", "thm-square-roots"])

s.result("ex-cs-equality", "exercise", "Equality in Cauchy–Schwarz", r"""
Let $V$ be an inner product space and $x, y \in V$. Prove that $\abs{\inner{x}{y}} = \abs{x}\abs{y}$ if and only if $y = 0$ or $x = cy$ for some $c \in \R$.
""", r"""
Suppose $y = 0$. Then both sides are $0$ and equality holds. Suppose $x = cy$. Then $\inner{x}{y} = c\inner{y}{y} = c\abs{y}^2$, so $\abs{\inner{x}{y}} = \abs{c}\abs{y}^2$; and $\abs{x}^2 = \inner{cy}{cy} = c^2\abs{y}^2 = (\abs{c}\abs{y})^2$, so $\abs{x} = \abs{c}\abs{y}$ by uniqueness of nonnegative square roots, and $\abs{x}\abs{y} = \abs{c}\abs{y}^2$. Equality holds.

Conversely suppose $\abs{\inner{x}{y}} = \abs{x}\abs{y}$ and $y \ne 0$. Put $t = -\inner{x}{y}/\inner{y}{y}$. Expanding by bilinearity as in the proof of the Cauchy–Schwarz inequality,
\[ \inner{x + ty}{x + ty} = \inner{x}{x} - \frac{\inner{x}{y}^2}{\inner{y}{y}} = \frac{\abs{x}^2\abs{y}^2 - \inner{x}{y}^2}{\abs{y}^2} = 0, \]
because $\inner{x}{y}^2 = \abs{\inner{x}{y}}^2 = \abs{x}^2\abs{y}^2$. By positive definiteness $x + ty = 0$, so $x = cy$ with $c = -t$.
""", 3, 30, [
    r"One direction is a computation. For the other, go back to the proof of the inequality and ask where it could be an equality.",
    r"With $t = -\inner{x}{y}/\inner{y}{y}$, equality forces $\inner{x + ty}{x + ty} = 0$. What does positive definiteness say then?",
], ["thm-cauchy-schwarz", "def-inner-product"])

s.result("thm-vector-triangle", "theorem", "Triangle inequality for vectors", r"""
Let $V$ be an inner product space. For all $x, y \in V$,
\[ \abs{x + y} \le \abs{x} + \abs{y}. \]
""", r"""
By bilinearity and symmetry, and then the Cauchy–Schwarz inequality (with $\inner{x}{y} \le \abs{\inner{x}{y}}$),
\[ \abs{x + y}^2 = \inner{x + y}{x + y} = \abs{x}^2 + 2\inner{x}{y} + \abs{y}^2 \le \abs{x}^2 + 2\abs{x}\abs{y} + \abs{y}^2 = \big(\abs{x} + \abs{y}\big)^2. \]
Both $\abs{x + y}$ and $\abs{x} + \abs{y}$ are nonnegative, so the inequality between their squares gives $\abs{x + y} \le \abs{x} + \abs{y}$.
""", 2, 20, [
    r"Compare the squares of the two sides.",
    r"Expand $\inner{x + y}{x + y}$ and bound the cross term with Cauchy–Schwarz.",
], ["thm-cauchy-schwarz", "def-inner-product"])

s.definition("def-norm", "Norm", r"""
Let $V$ be a vector space over $\R$. A \emph{norm} on $V$ is a function $\norm{\cdot} \colon V \to \R$ such that for all $x, y \in V$ and $c \in \R$:
\begin{enumerate}
\item $\norm{x} \ge 0$, and $\norm{x} = 0$ if and only if $x = 0$;
\item $\norm{cx} = \abs{c}\,\norm{x}$;
\item $\norm{x + y} \le \norm{x} + \norm{y}$.
\end{enumerate}
A vector space with a chosen norm is a \emph{normed space}.
""")

s.result("prop-inner-product-norm", "proposition", "An inner product gives a norm", r"""
If $V$ is an inner product space, then $\abs{x} = \sqrt{\inner{x}{x}}$ is a norm on $V$. In particular the Euclidean length is a norm on $\R^m$.
""", r"""
(1) A square root is nonnegative by definition, so $\abs{x} \ge 0$. If $x = 0$ then $\inner{x}{x} = 0$ and $\abs{x} = 0$. If $\abs{x} = 0$ then $\inner{x}{x} = \abs{x}^2 = 0$, so $x = 0$ by positive definiteness.

(2) By bilinearity $\inner{cx}{cx} = c^2\inner{x}{x} = c^2\abs{x}^2 = (\abs{c}\abs{x})^2$. Since $\abs{c}\abs{x} \ge 0$ and a nonnegative number has only one nonnegative square root, $\abs{cx} = \abs{c}\abs{x}$.

(3) This is the triangle inequality for vectors.
""", 1, 10, [
    r"Check the three norm axioms. The third has already been proved.",
    r"For homogeneity, compute $\inner{cx}{cx}$ and use the uniqueness of nonnegative square roots.",
], ["def-norm", "def-inner-product", "thm-vector-triangle", "thm-square-roots"])

s.result("cor-norm-distance", "corollary", "The distance defined by a norm", r"""
Let $\norm{\cdot}$ be a norm on a vector space $V$ and put $d(x, y) = \norm{x - y}$. Then for all $x, y, z \in V$:
\begin{enumerate}
\item $d(x, y) \ge 0$, and $d(x, y) = 0$ if and only if $x = y$;
\item $d(x, y) = d(y, x)$;
\item $d(x, z) \le d(x, y) + d(y, z)$.
\end{enumerate}
For the Euclidean length on $\R^m$, $d(x, y) = \abs{x - y} = \sqrt{(x_1 - y_1)^2 + \dots + (x_m - y_m)^2}$ is the \emph{Euclidean distance}.
""", r"""
(1) $\norm{x - y} \ge 0$, with equality if and only if $x - y = 0$, that is, $x = y$.

(2) $\norm{y - x} = \norm{(-1)(x - y)} = \abs{-1}\,\norm{x - y} = \norm{x - y}$.

(3) $\norm{x - z} = \norm{(x - y) + (y - z)} \le \norm{x - y} + \norm{y - z}$.
""", 1, 10, [
    r"Each property of $d$ comes from the norm axiom with the same number.",
    r"For the third, write $x - z = (x - y) + (y - z)$.",
], ["def-norm"])

s.result("ex-other-norms", "exercise", "The maximum norm and the sum norm", r"""
For $x \in \R^m$ define
\[ \norm{x}_{\max} = \max\set{\abs{x_1}, \dots, \abs{x_m}}, \qquad \norm{x}_{\mathrm{sum}} = \abs{x_1} + \dots + \abs{x_m}. \]
Prove that both are norms on $\R^m$.
""", r"""
\emph{Axiom (1).} Both quantities are built from the nonnegative numbers $\abs{x_i}$, so both are $\ge 0$, and both are $0$ when $x = 0$. If $x \ne 0$ then $\abs{x_j} > 0$ for some $j$, and each of $\norm{x}_{\max}$, $\norm{x}_{\mathrm{sum}}$ is $\ge \abs{x_j} > 0$.

\emph{Axiom (2).} Since $\abs{cx_i} = \abs{c}\abs{x_i}$, we get $\norm{cx}_{\mathrm{sum}} = \sum_i \abs{c}\abs{x_i} = \abs{c}\norm{x}_{\mathrm{sum}}$. For the maximum: each $\abs{c}\abs{x_i} \le \abs{c}\norm{x}_{\max}$ because $\abs{c} \ge 0$, and equality holds for an index $i$ at which $\abs{x_i}$ is largest; so $\norm{cx}_{\max} = \abs{c}\norm{x}_{\max}$.

\emph{Axiom (3).} For each $i$, the triangle inequality in $\R$ gives $\abs{x_i + y_i} \le \abs{x_i} + \abs{y_i}$. Summing over $i$ gives $\norm{x + y}_{\mathrm{sum}} \le \norm{x}_{\mathrm{sum}} + \norm{y}_{\mathrm{sum}}$. Also $\abs{x_i} + \abs{y_i} \le \norm{x}_{\max} + \norm{y}_{\max}$ for each $i$, so every $\abs{x_i + y_i}$, and hence their maximum, is at most $\norm{x}_{\max} + \norm{y}_{\max}$.
""", 2, 20, [
    r"Verify the three axioms for each; everything reduces to properties of the absolute value on $\R$, one coordinate at a time.",
    r"For the triangle inequality of the maximum norm, bound each $\abs{x_i + y_i}$ by $\norm{x}_{\max} + \norm{y}_{\max}$ before taking the maximum.",
], ["def-norm", "prop-triangle-inequality"])

s.result("ex-norm-comparison", "exercise", "Comparing the three norms on Euclidean space", r"""
With the notation of the previous exercise, prove that for every $x \in \R^m$
\[ \norm{x}_{\max} \le \abs{x} \le \norm{x}_{\mathrm{sum}} \le m\,\norm{x}_{\max}, \]
where $\abs{x}$ is the Euclidean length.
""", r"""
\emph{First inequality.} For each $i$, $\abs{x_i}^2 = x_i^2 \le x_1^2 + \dots + x_m^2 = \abs{x}^2$, since the omitted terms are nonnegative. Both $\abs{x_i}$ and $\abs{x}$ are nonnegative, so $\abs{x_i} \le \abs{x}$. This holds for every $i$, hence for the maximum.

\emph{Second inequality.} Expanding the square,
\[ \norm{x}_{\mathrm{sum}}^2 = \Big(\sum_{i=1}^m \abs{x_i}\Big)^2 = \sum_{i=1}^m x_i^2 + 2\sum_{i < j} \abs{x_i}\abs{x_j} \ge \sum_{i=1}^m x_i^2 = \abs{x}^2, \]
and both $\norm{x}_{\mathrm{sum}}$ and $\abs{x}$ are nonnegative, so $\abs{x} \le \norm{x}_{\mathrm{sum}}$.

\emph{Third inequality.} Each of the $m$ terms $\abs{x_i}$ is at most $\norm{x}_{\max}$, so their sum is at most $m\,\norm{x}_{\max}$.
""", 2, 15, [
    r"Since the Euclidean length is a square root, compare squares of nonnegative numbers.",
    r"Expand $(\abs{x_1} + \dots + \abs{x_m})^2$ and discard the cross terms.",
], ["ex-other-norms", "def-inner-product"])

s.result("ex-parallelogram", "exercise", "Parallelogram law", r"""
\begin{enumerate}
\item Let $V$ be an inner product space. Prove that for all $x, y \in V$,
\[ \abs{x + y}^2 + \abs{x - y}^2 = 2\abs{x}^2 + 2\abs{y}^2. \]
\item Deduce that for $m \ge 2$ there is no inner product on $\R^m$ whose length function is the maximum norm $\norm{x}_{\max} = \max_i \abs{x_i}$.
\end{enumerate}
""", r"""
(1) By bilinearity and symmetry,
\[ \abs{x + y}^2 = \abs{x}^2 + 2\inner{x}{y} + \abs{y}^2, \qquad \abs{x - y}^2 = \abs{x}^2 - 2\inner{x}{y} + \abs{y}^2. \]
Adding the two equations gives the identity.

(2) Suppose some inner product on $\R^m$ had $\sqrt{\inner{x}{x}} = \norm{x}_{\max}$ for all $x$. Then by (1) the maximum norm would satisfy the parallelogram law. Take $x = e_1$ and $y = e_2$ (possible since $m \ge 2$). Then $x + y$ has coordinates $1, 1, 0, \dots, 0$ and $x - y$ has coordinates $1, -1, 0, \dots, 0$, so
\[ \norm{x + y}_{\max}^2 + \norm{x - y}_{\max}^2 = 1 + 1 = 2, \qquad 2\norm{x}_{\max}^2 + 2\norm{y}_{\max}^2 = 2 + 2 = 4. \]
Since $2 \ne 4$, the law fails, and no such inner product exists.
""", 2, 20, [
    r"Expand both squared lengths with bilinearity; the cross terms cancel.",
    r"For (2), any norm that comes from an inner product must satisfy the identity in (1). Test it on two standard basis vectors.",
], ["def-inner-product", "ex-other-norms"])

s.remark("rem-angle", r"""
For nonzero $x, y \in \R^m$ the Cauchy–Schwarz inequality says that $\inner{x}{y}/(\abs{x}\abs{y})$ lies in $[-1, 1]$. This is what allows the \emph{angle} between $x$ and $y$ to be defined as the number whose cosine is that ratio; vectors with $\inner{x}{y} = 0$ are \emph{orthogonal}.
""")

s.definition("def-balls-boxes", "Balls, spheres, boxes", r"""
In $\R^m$ with the Euclidean length:
\begin{itemize}
\item the (open) \emph{ball} of radius $r > 0$ about $p$ is $\set{x \in \R^m : \abs{x - p} < r}$, and the \emph{closed ball} is $\set{x \in \R^m : \abs{x - p} \le r}$;
\item the \emph{unit ball} is $B^m = \set{x \in \R^m : \abs{x} \le 1}$ and the \emph{unit sphere} is $S^{m-1} = \set{x \in \R^m : \abs{x} = 1}$;
\item a \emph{box} is a product of closed intervals $[a_1, b_1] \times \dots \times [a_m, b_m] = \set{x \in \R^m : a_i \le x_i \le b_i \text{ for } i = 1, \dots, m}$; the \emph{unit cube} is $[0, 1]^m$.
\end{itemize}
""")

s.definition("def-convex", "Convex set", r"""
Let $V$ be a vector space over $\R$. For $x, y \in V$, the points $(1 - t)x + ty$ with $0 \le t \le 1$ form the \emph{segment} from $x$ to $y$; such a point is a \emph{convex combination} of $x$ and $y$. A set $E \subset V$ is \emph{convex} if it contains the segment between any two of its points: whenever $x, y \in E$ and $0 \le t \le 1$, also $(1 - t)x + ty \in E$.
""")

s.result("prop-ball-convex", "proposition", "Balls are convex", r"""
Let $\norm{\cdot}$ be a norm on a vector space $V$, let $p \in V$ and $r > 0$. Then the open ball $\set{x \in V : \norm{x - p} < r}$ and the closed ball $\set{x \in V : \norm{x - p} \le r}$ are convex. In particular the unit ball $B^m \subset \R^m$ is convex.
""", r"""
Let $x, y \in V$ and $0 \le t \le 1$, and put $z = (1 - t)x + ty$. Since $p = (1 - t)p + tp$,
\[ z - p = (1 - t)(x - p) + t(y - p), \]
so by the triangle inequality and homogeneity of the norm (note $1 - t \ge 0$ and $t \ge 0$),
\[ \norm{z - p} \le (1 - t)\norm{x - p} + t\norm{y - p}. \]
\emph{Closed ball.} If $\norm{x - p} \le r$ and $\norm{y - p} \le r$, the right-hand side is at most $(1 - t)r + tr = r$, so $z$ is in the closed ball.

\emph{Open ball.} Suppose $\norm{x - p} < r$ and $\norm{y - p} < r$. Then $(1 - t)\norm{x - p} \le (1 - t)r$ and $t\norm{y - p} \le tr$. The numbers $1 - t$ and $t$ are not both zero; if $1 - t > 0$ the first inequality is strict, and if $t > 0$ the second is. Adding, $\norm{z - p} < (1 - t)r + tr = r$, so $z$ is in the open ball.

The unit ball is the closed ball of radius $1$ about $0$ for the Euclidean length, which is a norm.
""", 2, 20, [
    r"Take two points of the ball and a point $z = (1 - t)x + ty$ between them; you must estimate $\norm{z - p}$.",
    r"Write $p = (1 - t)p + tp$ so that $z - p = (1 - t)(x - p) + t(y - p)$, then use the triangle inequality and homogeneity.",
], ["def-norm", "def-convex", "prop-inner-product-norm", "def-balls-boxes"])

s.result("ex-convex-facts", "exercise", "Convex and not convex", r"""
\begin{enumerate}
\item Prove that the intersection of any nonempty class of convex subsets of a vector space $V$ is convex.
\item Prove that every box $[a_1, b_1] \times \dots \times [a_m, b_m]$ in $\R^m$ is convex.
\item Prove that the unit sphere $S^{m-1} \subset \R^m$ is not convex.
\end{enumerate}
""", r"""
(1) Let $\mathcal{C}$ be a nonempty class of convex sets and $E = \bigcap \mathcal{C}$. Let $x, y \in E$ and $0 \le t \le 1$. For each $C \in \mathcal{C}$ we have $x, y \in C$, so $(1 - t)x + ty \in C$ by convexity of $C$. As this holds for every member of $\mathcal{C}$, $(1 - t)x + ty \in E$.

(2) Let $x, y$ be in the box and $0 \le t \le 1$. For each $i$ we have $a_i \le x_i \le b_i$ and $a_i \le y_i \le b_i$. Multiplying by $1 - t \ge 0$ and $t \ge 0$ respectively and adding,
\[ a_i = (1 - t)a_i + ta_i \le (1 - t)x_i + ty_i \le (1 - t)b_i + tb_i = b_i. \]
The middle term is the $i$th coordinate of $(1 - t)x + ty$, so that point is in the box.

(3) The points $e_1$ and $-e_1$ have Euclidean length $1$, so they lie in $S^{m-1}$. With $t = 1/2$ the convex combination is $\tfrac12 e_1 + \tfrac12(-e_1) = 0$, whose length is $0 \ne 1$. So the segment from $e_1$ to $-e_1$ is not contained in $S^{m-1}$.
""", 2, 15, [
    r"For (1) and (2), take two points of the set and a convex combination, and check the defining condition of the set.",
    r"For (3), find two points of the sphere whose midpoint is not on the sphere.",
], ["def-convex", "def-balls-boxes"])

s.card("dot-product", r"Define the dot product on $\R^m$ and name its three key properties.",
       r"$\inner{x}{y} = \sum_i x_i y_i$. It is bilinear, symmetric, and positive definite ($\inner{x}{x} \ge 0$ with equality only for $x = 0$).", "prop-dot-properties")
s.card("cauchy-schwarz", r"State the Cauchy–Schwarz inequality.",
       r"In an inner product space, $\abs{\inner{x}{y}} \le \abs{x}\abs{y}$, where $\abs{x} = \sqrt{\inner{x}{x}}$.", "thm-cauchy-schwarz")
s.card("cauchy-schwarz-idea", r"What is the idea of the proof of Cauchy–Schwarz?",
       r"$\inner{x + ty}{x + ty} \ge 0$ for all real $t$; expand it as a quadratic in $t$ and take $t = -\inner{x}{y}/\inner{y}{y}$ (for $y \ne 0$).", "thm-cauchy-schwarz")
s.card("vector-triangle", r"How does the triangle inequality $\abs{x + y} \le \abs{x} + \abs{y}$ follow from Cauchy–Schwarz?",
       r"$\abs{x + y}^2 = \abs{x}^2 + 2\inner{x}{y} + \abs{y}^2 \le (\abs{x} + \abs{y})^2$, then compare nonnegative numbers through their squares.", "thm-vector-triangle")
s.card("norm", r"Define a norm on a real vector space.",
       r"A function $\norm{\cdot} \colon V \to \R$ with $\norm{x} \ge 0$ and $\norm{x} = 0$ only for $x = 0$; $\norm{cx} = \abs{c}\norm{x}$; $\norm{x + y} \le \norm{x} + \norm{y}$.", "def-norm")
s.card("norm-not-inner", r"Give a norm on $\R^2$ that does not come from an inner product, and the reason.",
       r"The maximum norm: it violates the parallelogram law $\abs{x + y}^2 + \abs{x - y}^2 = 2\abs{x}^2 + 2\abs{y}^2$ for $x = e_1$, $y = e_2$.", "ex-parallelogram")
s.card("convex", r"Define a convex set. Is the unit ball convex? The unit sphere?",
       r"$E$ is convex if $(1 - t)x + ty \in E$ whenever $x, y \in E$ and $0 \le t \le 1$. Balls of any norm are convex; the sphere is not (the midpoint of $e_1$ and $-e_1$ is $0$).", "prop-ball-convex")

s.write()
