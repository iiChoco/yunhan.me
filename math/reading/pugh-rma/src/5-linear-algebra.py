from c5lib import Section
S = Section("5-linear-algebra")
b, c = S.b, S.c

b("la-intro", "prose", r"""
The derivative of a function of several variables is not a number but a linear map: the best linear approximation
to the function near a point. Before differentiating anything we therefore need to measure linear maps: how big
one is, when two are close, and what survives a small perturbation. This section builds that toolkit. Its main
points are that a linear map out of $\R^n$ is automatically continuous, that all norms on a finite-dimensional
space are comparable, and that an invertible operator stays invertible when it is nudged.
""")

b("def-normed-space", "definition", r"""
A \emph{norm} on a real vector space $V$ is a function $\abs{\cdot} : V \to [0,\infty)$ such that for all
$v, w \in V$ and $c \in \R$:
\begin{enumerate}
\item $\abs{v} = 0$ if and only if $v = 0$;
\item $\abs{cv} = \abs{c}\,\abs{v}$;
\item $\abs{v + w} \le \abs{v} + \abs{w}$.
\end{enumerate}
A vector space with a chosen norm is a \emph{normed space}; it is a metric space under $d(v,w) = \abs{v - w}$.
When two normed spaces are in play we write $\abs{\cdot}_V$ and $\abs{\cdot}_W$ if there is a risk of confusion.
Unless something else is said, $\R^n$ carries the Euclidean norm $\abs{v} = \sqrt{v_1^2 + \dots + v_n^2} =
\sqrt{\inner{v}{v}}$, for which the Cauchy--Schwarz inequality $\abs{\inner{v}{w}} \le \abs{v}\,\abs{w}$ holds.
The standard basis vectors of $\R^n$ are $e_1, \dots, e_n$.
""", title="Normed space")

b("def-linear-map", "definition", r"""
A map $T : V \to W$ between real vector spaces is \emph{linear} if $T(v + cw) = T(v) + cT(w)$ for all
$v, w \in V$ and $c \in \R$. We write $Tv$ for $T(v)$. The linear maps from $V$ to $W$ form a vector space
$\mathcal{L}(V, W)$ under pointwise addition and scalar multiplication.

A linear map $T : \R^n \to \R^m$ has a \emph{matrix} $A = (a_{ij})$, with $m$ rows and $n$ columns, where
$a_{ij}$ is the $i$-th component of $Te_j$. Then $(Tv)_i = \sum_{j=1}^n a_{ij} v_j$, so $T$ and $A$ determine one
another, and composition of linear maps corresponds to multiplication of matrices.
""", title="Linear map and its matrix")

b("rem-linear-facts", "remark", r"""
We take the following facts of linear algebra for granted. A linear map $T : \R^n \to \R^n$ is injective if and
only if it is surjective, if and only if it is bijective, if and only if $\det T \ne 0$; its inverse is then
linear, and the entries of the inverse matrix are given by Cramer's rule: each is a cofactor of the matrix
(a polynomial in its entries) divided by the determinant. A real vector space of dimension $N$ with basis
$w_1, \dots, w_N$ is the image of $\R^N$ under the linear bijection $x \mapsto x_1 w_1 + \dots + x_N w_N$.
""")

b("def-operator-norm", "definition", r"""
Let $T : V \to W$ be a linear map between normed spaces. Its \emph{operator norm} is
\[ \norm{T} = \sup \set{ \abs{Tv}_W : v \in V,\ \abs{v}_V \le 1 }, \]
a number in $[0, \infty]$. If $\norm{T} < \infty$ we call $T$ \emph{bounded}. The operator norm is the largest
factor by which $T$ stretches a vector.
""", title="Operator norm")

b("prop-opnorm-bound", "proposition", r"""
Let $T : V \to W$ be a linear map between normed spaces.
\begin{enumerate}
\item If $\norm{T} < \infty$, then $\abs{Tv} \le \norm{T}\,\abs{v}$ for every $v \in V$.
\item If $M \ge 0$ and $\abs{Tv} \le M \abs{v}$ for every $v \in V$, then $\norm{T} \le M$.
\item If $V \ne \set{0}$, then $\norm{T} = \sup \set{ \abs{Tv}/\abs{v} : v \ne 0 }$.
\end{enumerate}
Thus a finite $\norm{T}$ is the least constant $M$ with $\abs{Tv} \le M\abs{v}$ for all $v$.
""", title="The operator norm is the best stretching constant", proof=r"""
(1) If $v = 0$ both sides are $0$, since $T0 = 0$. If $v \ne 0$, put $u = v/\abs{v}$. Then $\abs{u} = 1$, so
$\abs{Tu} \le \norm{T}$ by the definition of the supremum, and by linearity
$\abs{Tv} = \abs{\,\abs{v}\,Tu\,} = \abs{v}\,\abs{Tu} \le \norm{T}\,\abs{v}$.

(2) If $\abs{v} \le 1$ then $\abs{Tv} \le M\abs{v} \le M$. So $M$ is an upper bound of the set whose supremum
is $\norm{T}$, and $\norm{T} \le M$.

(3) Let $s = \sup \set{\abs{Tv}/\abs{v} : v \ne 0} \in [0,\infty]$. If $0 < \abs{v} \le 1$ then
$\abs{Tv} \le \abs{Tv}/\abs{v} \le s$, and $\abs{T0} = 0 \le s$; hence $\norm{T} \le s$. Conversely, for $v \ne 0$
the vector $u = v/\abs{v}$ has norm $1$ and $\abs{Tv}/\abs{v} = \abs{Tu} \le \norm{T}$, so $s \le \norm{T}$.
""", d=1, m=10, hints=[
r"For (1), rescale a nonzero $v$ to the unit vector $v/\abs{v}$ and use linearity.",
], uses=["def-operator-norm"])

b("thm-bounded-continuous", "theorem", r"""
Let $T : V \to W$ be a linear map between normed spaces. The following are equivalent:
\begin{enumerate}
\item $\norm{T} < \infty$;
\item $T$ is uniformly continuous;
\item $T$ is continuous;
\item $T$ is continuous at the origin.
\end{enumerate}
""", title="Bounded means continuous", proof=r"""
(1) $\Rightarrow$ (2). Let $\eps > 0$ and put $\delta = \eps/(\norm{T} + 1)$. If $\abs{v - v'} < \delta$ then, by
linearity and the bound $\abs{Tu} \le \norm{T}\abs{u}$,
\[ \abs{Tv - Tv'} = \abs{T(v - v')} \le \norm{T}\,\abs{v - v'} \le \norm{T}\,\delta < \eps. \]

(2) $\Rightarrow$ (3) $\Rightarrow$ (4) are immediate from the definitions.

(4) $\Rightarrow$ (1). Since $T0 = 0$, continuity at the origin with $\eps = 1$ gives a $\delta > 0$ such that
$\abs{u} < \delta$ implies $\abs{Tu} < 1$. Let $v \ne 0$ and put $u = \frac{\delta}{2\abs{v}}\, v$. Then
$\abs{u} = \delta/2 < \delta$, so $\abs{Tu} < 1$, that is, $\frac{\delta}{2\abs{v}} \abs{Tv} < 1$. Hence
$\abs{Tv} \le \frac{2}{\delta}\abs{v}$ for every $v \ne 0$, and trivially for $v = 0$. Since $\norm{T}$ is at most
any constant $M$ with $\abs{Tv} \le M\abs{v}$ for all $v$, we get $\norm{T} \le 2/\delta < \infty$.
""", d=2, m=20, hints=[
r"The only implication with content is (4) $\Rightarrow$ (1). Continuity at $0$ controls $T$ on a small ball; linearity lets you rescale any vector into that ball.",
r"If $\abs{u} < \delta$ forces $\abs{Tu} < 1$, apply this to $u = \delta v/(2\abs{v})$.",
], uses=["def-operator-norm", "prop-opnorm-bound"])

b("prop-rn-bounded", "proposition", r"""
Let $T : \R^n \to \R^m$ be linear with matrix $A = (a_{ij})$. Then
\[ \max_{i,j} \abs{a_{ij}} \ \le\ \norm{T} \ \le\ \Big( \sum_{i=1}^m \sum_{j=1}^n a_{ij}^2 \Big)^{1/2}. \]
In particular $T$ is bounded.
""", title="Operator norm versus matrix entries", proof=r"""
\emph{Upper bound.} Let $a_i = (a_{i1}, \dots, a_{in}) \in \R^n$ be the $i$-th row of $A$. For $v \in \R^n$ the
$i$-th component of $Tv$ is $\sum_j a_{ij}v_j = \inner{a_i}{v}$, so by the Cauchy--Schwarz inequality
$(Tv)_i^2 \le \abs{a_i}^2 \abs{v}^2$. Summing over $i$,
\[ \abs{Tv}^2 = \sum_{i=1}^m (Tv)_i^2 \le \Big( \sum_{i=1}^m \abs{a_i}^2 \Big) \abs{v}^2 = \Big( \sum_{i,j} a_{ij}^2 \Big) \abs{v}^2 . \]
So $\abs{Tv} \le M\abs{v}$ for all $v$ with $M = (\sum_{i,j} a_{ij}^2)^{1/2}$, and therefore $\norm{T} \le M$.

\emph{Lower bound.} Now $\norm{T}$ is finite, so $\abs{Te_j} \le \norm{T}\abs{e_j} = \norm{T}$. The number $a_{ij}$
is the $i$-th component of $Te_j$, and the absolute value of a component of a vector is at most the vector's
Euclidean norm. Hence $\abs{a_{ij}} \le \abs{Te_j} \le \norm{T}$ for all $i, j$.
""", d=2, m=15, hints=[
r"Each component of $Tv$ is the dot product of a row of $A$ with $v$.",
r"Cauchy--Schwarz on each row, then sum the squares. For the lower bound look at $Te_j$.",
], uses=["def-linear-map", "prop-opnorm-bound"])

b("prop-opnorm-is-norm", "proposition", r"""
Let $V$, $W$, $X$ be normed spaces.
\begin{enumerate}
\item The bounded linear maps $V \to W$ form a vector subspace of $\mathcal{L}(V,W)$, and $T \mapsto \norm{T}$ is
a norm on it.
\item If $T : V \to W$ and $S : W \to X$ are bounded linear maps, then $S \circ T$ is bounded and
$\norm{S \circ T} \le \norm{S}\,\norm{T}$.
\end{enumerate}
In particular the operator norm is a norm on $\mathcal{L}(\R^n, \R^m)$, every element of which is bounded.
""", title="The operator norm is a norm, and is submultiplicative", proof=r"""
We use repeatedly that $\abs{Tv} \le \norm{T}\abs{v}$ for bounded $T$, and that $\norm{T} \le M$ whenever
$\abs{Tv} \le M\abs{v}$ for all $v$.

(1) Let $S, T : V \to W$ be bounded and $c \in \R$. For every $v$,
\[ \abs{(S + T)v} \le \abs{Sv} + \abs{Tv} \le (\norm{S} + \norm{T})\abs{v}, \]
so $S + T$ is bounded and $\norm{S + T} \le \norm{S} + \norm{T}$. Next,
$\norm{cT} = \sup_{\abs{v} \le 1} \abs{c}\,\abs{Tv} = \abs{c}\,\norm{T}$, so $cT$ is bounded and the norm is
homogeneous. Hence the bounded maps form a subspace. Finally $\norm{T} \ge 0$, the zero map has norm $0$, and if
$\norm{T} = 0$ then $\abs{Tv} \le 0 \cdot \abs{v} = 0$ for all $v$, so $T = 0$.

(2) For every $v \in V$, $\abs{S(Tv)} \le \norm{S}\,\abs{Tv} \le \norm{S}\,\norm{T}\,\abs{v}$. Hence
$\norm{S \circ T} \le \norm{S}\norm{T} < \infty$.

The last sentence follows because every linear map $\R^n \to \R^m$ is bounded.
""", d=2, m=15, hints=[
r"Prove each inequality pointwise, for $\abs{(S+T)v}$ and $\abs{S(Tv)}$, and then use that $\norm{\cdot}$ is the least stretching constant.",
], uses=["prop-opnorm-bound", "prop-rn-bounded"])

b("la-prose-findim", "prose", r"""
The bound on $\norm{T}$ by matrix entries used the Euclidean norm on both sides. The next theorem says that
finite dimensionality alone is what matters: whatever norm the target carries, a linear map out of $\R^n$ is
continuous, and a linear bijection from $\R^n$ is a homeomorphism. The proof of the second half is the first
place where compactness of the unit sphere earns its keep.
""")

b("thm-finite-dim-continuous", "theorem", r"""
Let $W$ be a normed space and let $T : \R^n \to W$ be linear, where $n \ge 1$.
\begin{enumerate}
\item $T$ is bounded, hence continuous.
\item If $T$ is a bijection, then $T^{-1} : W \to \R^n$ is bounded too. Thus $T$ is a homeomorphism.
\end{enumerate}
""", title="Linear maps on $\\R^n$ are continuous; isomorphisms are homeomorphisms", proof=r"""
(1) Write $v = \sum_j v_j e_j$. By linearity, the triangle inequality in $W$, and the Cauchy--Schwarz inequality
in $\R^n$,
\[ \abs{Tv}_W \le \sum_{j=1}^n \abs{v_j}\,\abs{Te_j}_W \le \Big( \sum_{j=1}^n \abs{Te_j}_W^2 \Big)^{1/2} \abs{v}. \]
So $\norm{T} \le (\sum_j \abs{Te_j}_W^2)^{1/2} < \infty$, and a bounded linear map is continuous.

(2) Let $\Sigma = \set{u \in \R^n : \abs{u} = 1}$ be the unit sphere. It is closed and bounded in $\R^n$, hence
compact by the Heine--Borel theorem, and it is nonempty because $n \ge 1$. The function
$\varphi(u) = \abs{Tu}_W$ is continuous on $\R^n$, because by the reverse triangle inequality
\[ \abs{\varphi(u) - \varphi(u')} \le \abs{Tu - Tu'}_W \le \norm{T}\,\abs{u - u'} . \]
A continuous real function on a nonempty compact set attains its minimum, so there is a $u_0 \in \Sigma$ with
$\varphi(u) \ge \varphi(u_0) =: c$ for all $u \in \Sigma$. Since $u_0 \ne 0$ and $T$ is injective, $Tu_0 \ne 0$,
so $c > 0$.

For $v \ne 0$ we have $v/\abs{v} \in \Sigma$, so $\abs{Tv}_W = \abs{v}\,\varphi(v/\abs{v}) \ge c\abs{v}$; this also
holds for $v = 0$. Now let $w \in W$ and put $v = T^{-1}w$. Then $\abs{w}_W = \abs{Tv}_W \ge c\,\abs{T^{-1}w}$, that is,
$\abs{T^{-1}w} \le \frac{1}{c}\abs{w}_W$. The inverse of a linear bijection is linear, so $T^{-1}$ is a linear map
with $\norm{T^{-1}} \le 1/c$. Bounded linear maps are continuous, so $T$ and $T^{-1}$ are both continuous.
""", d=3, m=35, hints=[
r"Part (1): expand $v$ in the standard basis and use the triangle inequality, then Cauchy--Schwarz.",
r"Part (2): you need a lower bound $\abs{Tv}_W \ge c\abs{v}$ with $c > 0$. By scaling it is enough to find one on the unit sphere.",
r"The unit sphere is compact and $u \mapsto \abs{Tu}_W$ is continuous and never zero on it, so it has a positive minimum.",
], uses=["prop-opnorm-bound", "thm-bounded-continuous"])

b("cor-norms-equivalent", "corollary", r"""
Let $\abs{\cdot}_*$ be any norm on $\R^n$, $n \ge 1$. Then there are constants $0 < c \le C$ such that
\[ c\,\abs{v} \le \abs{v}_* \le C\,\abs{v} \qquad \text{for all } v \in \R^n, \]
where $\abs{\cdot}$ is the Euclidean norm. Consequently the two norms have the same open sets, the same
convergent sequences, and the same Cauchy sequences.
""", title="All norms on $\\R^n$ are comparable", proof=r"""
Let $W$ be the vector space $\R^n$ with the norm $\abs{\cdot}_*$, and let $J : \R^n \to W$ be the identity map,
$Jv = v$. It is a linear bijection from Euclidean $\R^n$ to the normed space $W$, so $J$ and $J^{-1}$ are bounded.
Thus $\abs{v}_* = \abs{Jv}_* \le \norm{J}\,\abs{v}$ and $\abs{v} = \abs{J^{-1}v} \le \norm{J^{-1}}\,\abs{v}_*$.
Taking a unit vector $v$ in the second inequality shows $\norm{J^{-1}} > 0$, and in the two together
$1 \le \norm{J^{-1}}\norm{J}$. So $C = \norm{J}$ and $c = 1/\norm{J^{-1}}$ work, and $c \le C$.

For the consequences: $\abs{v_k - v}_* \to 0$ if and only if $\abs{v_k - v} \to 0$, and likewise for the Cauchy
condition, by the two inequalities. A ball of radius $r$ about $p$ for one norm contains the ball of radius $cr$
or $r/C$ about $p$ for the other, so a set is open for one norm exactly when it is open for the other.
""", d=2, m=15, hints=[
r"Apply the previous theorem to the identity map from Euclidean $\R^n$ to $\R^n$ with the new norm.",
], uses=["thm-finite-dim-continuous"])

b("cor-finite-dim", "corollary", r"""
Let $W$ and $W'$ be finite-dimensional normed spaces.
\begin{enumerate}
\item Every linear map $\Psi : W \to W'$ is bounded.
\item $W$ is complete: every Cauchy sequence in $W$ converges.
\item In $\mathcal{L}(\R^n,\R^m)$ with the operator norm, $T_k \to T$ if and only if every matrix entry of $T_k$
converges to the corresponding entry of $T$.
\end{enumerate}
In particular $\mathcal{L}(\R^n,\R^m)$ is a complete normed space under the operator norm.
""", title="Finite-dimensional normed spaces", proof=r"""
If $W = \set{0}$, (1) and (2) are trivial, so let $N = \dim W \ge 1$, pick a basis $w_1, \dots, w_N$ of $W$, and
let $\Phi : \R^N \to W$ be the linear bijection $\Phi(x) = \sum_j x_j w_j$. Since linear maps out of $\R^N$ are
bounded and linear bijections from $\R^N$ have bounded inverses, $\norm{\Phi}$ and $\norm{\Phi^{-1}}$ are finite.

(1) The map $\Psi \circ \Phi : \R^N \to W'$ is linear, hence bounded. So
$\Psi = (\Psi \circ \Phi) \circ \Phi^{-1}$ is a composite of bounded maps and
$\norm{\Psi} \le \norm{\Psi \circ \Phi}\,\norm{\Phi^{-1}} < \infty$.

(2) Let $(w_k)$ be Cauchy in $W$ and put $x_k = \Phi^{-1}w_k$. Then
$\abs{x_k - x_l} \le \norm{\Phi^{-1}}\,\abs{w_k - w_l}_W$, so $(x_k)$ is Cauchy in $\R^N$. Since $\R^N$ is complete,
$x_k \to x$ for some $x$, and $\abs{w_k - \Phi x}_W = \abs{\Phi(x_k - x)}_W \le \norm{\Phi}\,\abs{x_k - x} \to 0$. So
$w_k \to \Phi x$.

(3) Let $a^k_{ij}$ and $a_{ij}$ be the entries of $T_k$ and $T$. The entries of $T_k - T$ are
$a^k_{ij} - a_{ij}$, so the comparison of the operator norm with matrix entries gives
\[ \max_{i,j} \abs{a^k_{ij} - a_{ij}} \le \norm{T_k - T} \le \Big( \sum_{i,j} (a^k_{ij} - a_{ij})^2 \Big)^{1/2} . \]
The left side tends to $0$ if $\norm{T_k - T} \to 0$, and the right side tends to $0$ if every entry converges.

Finally, $\mathcal{L}(\R^n,\R^m)$ has dimension $mn$ and the operator norm is a norm on it, so it is complete by (2).
""", d=2, m=20, hints=[
r"Choose a basis: it gives a linear bijection $\Phi : \R^N \to W$ which is bounded with bounded inverse.",
r"Factor $\Psi = (\Psi\circ\Phi)\circ\Phi^{-1}$; carry a Cauchy sequence back to $\R^N$ with $\Phi^{-1}$.",
], uses=["thm-finite-dim-continuous", "prop-opnorm-is-norm", "prop-rn-bounded"])

b("ex-unbounded", "example", r"""
Finite dimension is essential. Let $P$ be the vector space of real polynomial functions on $[0,1]$ with the norm
$\abs{p} = \sup_{x \in [0,1]} \abs{p(x)}$, and let $D : P \to P$ be differentiation, $Dp = p'$. It is linear. The
polynomials $p_k(x) = x^k$ have $\abs{p_k} = 1$ while $\abs{Dp_k} = \sup_x \abs{k x^{k-1}} = k$. So
$\norm{D} \ge k$ for every $k$: the operator norm of $D$ is infinite, and $D$ is a linear map that is nowhere
continuous.
""", title="An unbounded linear map")

b("def-conorm", "definition", r"""
Let $T : \R^n \to \R^n$ be linear, $n \ge 1$. Its \emph{conorm} is
\[ m(T) = \inf \set{ \abs{Tv}/\abs{v} : v \ne 0 } . \]
Where the norm is the greatest stretch, the conorm is the least: $\abs{Tv} \ge m(T)\abs{v}$ for all $v$.
""", title="Conorm")

b("prop-conorm", "proposition", r"""
A linear map $T : \R^n \to \R^n$, $n \ge 1$, is invertible if and only if $m(T) > 0$, and in that case
\[ m(T) = \frac{1}{\norm{T^{-1}}} . \]
""", title="The conorm detects invertibility", proof=r"""
By definition of the infimum, $\abs{Tv} \ge m(T)\abs{v}$ for all $v \ne 0$, and also for $v = 0$.

Suppose $m(T) > 0$. If $Tv = 0$ then $0 \ge m(T)\abs{v}$, so $v = 0$. Thus $T$ is injective, and an injective
linear map from $\R^n$ to itself is invertible.

Suppose $T$ is invertible. Then $T^{-1}$ is linear, hence bounded, and $\norm{T^{-1}} > 0$ because $T^{-1} \ne 0$.
For $v \ne 0$ we have $\abs{v} = \abs{T^{-1}(Tv)} \le \norm{T^{-1}}\,\abs{Tv}$, so
$\abs{Tv}/\abs{v} \ge 1/\norm{T^{-1}}$. Taking the infimum, $m(T) \ge 1/\norm{T^{-1}} > 0$. In the other direction,
for any $w \in \R^n$ the vector $v = T^{-1}w$ satisfies $\abs{w} = \abs{Tv} \ge m(T)\abs{T^{-1}w}$, so
$\abs{T^{-1}w} \le \abs{w}/m(T)$ for all $w$. Hence $\norm{T^{-1}} \le 1/m(T)$, that is, $m(T) \le 1/\norm{T^{-1}}$.
""", d=2, m=20, hints=[
r"If $m(T) > 0$, what does $\abs{Tv} \ge m(T)\abs{v}$ say about the kernel of $T$?",
r"For the formula, substitute $w = Tv$: the ratio $\abs{T^{-1}w}/\abs{w}$ is the reciprocal of $\abs{Tv}/\abs{v}$.",
], uses=["def-conorm", "prop-opnorm-bound", "prop-rn-bounded"])

b("lem-perturb-identity", "lemma", r"""
Let $S : \R^n \to \R^n$ be linear with $\norm{S} < 1$, and let $I$ be the identity map of $\R^n$. Then $I - S$ is
invertible, and
\[ \norm{(I - S)^{-1}} \le \frac{1}{1 - \norm{S}}, \qquad \norm{(I - S)^{-1} - I} \le \frac{\norm{S}}{1 - \norm{S}} . \]
""", title="Small perturbations of the identity", proof=r"""
For every $v$, the reverse triangle inequality gives
\[ \abs{(I - S)v} = \abs{v - Sv} \ge \abs{v} - \abs{Sv} \ge (1 - \norm{S})\abs{v} . \]
Hence the conorm satisfies $m(I - S) \ge 1 - \norm{S} > 0$. Since a positive conorm means invertibility, $I - S$ is
invertible, and $\norm{(I - S)^{-1}} = 1/m(I - S) \le 1/(1 - \norm{S})$.

For the second estimate, note that $(I - S)^{-1} - I = (I - S)^{-1}\big(I - (I - S)\big) = (I - S)^{-1} S$. Since the
operator norm is submultiplicative,
\[ \norm{(I - S)^{-1} - I} \le \norm{(I - S)^{-1}}\,\norm{S} \le \frac{\norm{S}}{1 - \norm{S}} . \]
""", d=2, m=20, hints=[
r"Bound $\abs{(I-S)v}$ from below.",
r"The lower bound $(1 - \norm{S})\abs{v}$ says the conorm of $I - S$ is positive. For the second inequality, factor $(I-S)^{-1} - I$ as $(I-S)^{-1}S$.",
], uses=["prop-conorm", "prop-opnorm-bound", "prop-opnorm-is-norm"])

b("rem-neumann", "remark", r"""
One can also write the inverse down: $(I - S)^{-1} = \sum_{k=0}^\infty S^k$, a geometric series that converges in
the complete space $\mathcal{L}(\R^n,\R^n)$ because $\norm{S^k} \le \norm{S}^k$. The argument through the conorm
avoids series but is special to finite dimensions.
""")

b("thm-inverse-open", "theorem", r"""
Let $T : \R^n \to \R^n$ be an invertible linear map, and let $S : \R^n \to \R^n$ be linear with
$\norm{S - T} < 1/\norm{T^{-1}}$. Then $S$ is invertible, and
\[ \norm{S^{-1} - T^{-1}} \le \frac{\norm{T^{-1}}^2\,\norm{S - T}}{1 - \norm{T^{-1}}\,\norm{S - T}} . \]
""", title="Operators near an invertible operator are invertible", proof=r"""
Put $R = T^{-1}(T - S)$ and $\rho = \norm{T^{-1}}\,\norm{S - T}$. Then $\norm{R} \le \rho < 1$, and
\[ T(I - R) = T - (T - S) = S . \]
By the lemma on perturbations of the identity, $I - R$ is invertible. So $S$ is a composite of invertible maps,
hence invertible, with $S^{-1} = (I - R)^{-1} T^{-1}$. Therefore
\[ S^{-1} - T^{-1} = \big( (I - R)^{-1} - I \big) T^{-1}, \qquad
\norm{S^{-1} - T^{-1}} \le \frac{\norm{R}}{1 - \norm{R}}\,\norm{T^{-1}} , \]
using the same lemma and submultiplicativity. The function $t \mapsto t/(1-t) = \frac{1}{1-t} - 1$ is increasing
on $[0,1)$ and $\norm{R} \le \rho < 1$, so $\frac{\norm{R}}{1 - \norm{R}} \le \frac{\rho}{1 - \rho}$. This gives
\[ \norm{S^{-1} - T^{-1}} \le \frac{\rho\,\norm{T^{-1}}}{1 - \rho} = \frac{\norm{T^{-1}}^2\,\norm{S - T}}{1 - \norm{T^{-1}}\,\norm{S - T}} . \]
""", d=3, m=30, hints=[
r"Factor $S$ as $T$ times a perturbation of the identity.",
r"$S = T(I - R)$ with $R = T^{-1}(T - S)$, and $\norm{R} < 1$ by hypothesis. Then $S^{-1} - T^{-1} = ((I-R)^{-1} - I)T^{-1}$.",
], uses=["lem-perturb-identity", "prop-opnorm-is-norm"])

b("cor-gl-open", "corollary", r"""
Let $GL(n)$ be the set of invertible linear maps $\R^n \to \R^n$. With respect to the operator norm, $GL(n)$ is an
open subset of $\mathcal{L}(\R^n,\R^n)$, and inversion $\operatorname{Inv} : GL(n) \to GL(n)$, $T \mapsto T^{-1}$,
is continuous.
""", title="The invertible operators form an open set and inversion is continuous", proof=r"""
Let $T \in GL(n)$. Every $S$ in the open ball of radius $1/\norm{T^{-1}}$ about $T$ is invertible, by the theorem
on operators near an invertible operator. So $GL(n)$ is open.

For continuity at $T$, let $\eps > 0$ and put
$\delta = \min\set{ \frac{1}{2\norm{T^{-1}}},\ \frac{\eps}{2\norm{T^{-1}}^2} }$. If $\norm{S - T} < \delta$, then
$\norm{T^{-1}}\norm{S - T} < \frac12$, so $S \in GL(n)$ and the denominator in the estimate of that theorem is at
least $\frac12$. Hence
\[ \norm{S^{-1} - T^{-1}} \le 2\,\norm{T^{-1}}^2\,\norm{S - T} < 2\,\norm{T^{-1}}^2\,\delta \le \eps . \]
""", d=2, m=15, hints=[
r"Both statements are read off from the quantitative estimate of the previous theorem; for continuity keep $\norm{T^{-1}}\norm{S-T} \le \frac12$.",
], uses=["thm-inverse-open"])

c("opnorm", "Define the operator norm of a linear map $T : V \\to W$ between normed spaces, and give its characterization as a best constant.",
  r"$\norm{T} = \sup\set{\abs{Tv} : \abs{v} \le 1}$. When finite it is the least $M$ with $\abs{Tv} \le M\abs{v}$ for all $v$.", item="prop-opnorm-bound")
c("bounded-continuous", "For a linear map between normed spaces, which four conditions are equivalent?",
  r"$\norm{T} < \infty$; $T$ uniformly continuous; $T$ continuous; $T$ continuous at $0$.", item="thm-bounded-continuous")
c("entries", r"Compare $\norm{T}$ with the entries $a_{ij}$ of the matrix of $T : \R^n \to \R^m$.",
  r"$\max \abs{a_{ij}} \le \norm{T} \le (\sum a_{ij}^2)^{1/2}$. So convergence in operator norm is entrywise convergence.", item="prop-rn-bounded")
c("findim", r"Why does a linear bijection $T : \R^n \to W$ ($W$ normed) have a bounded inverse? Give the idea.",
  r"$u \mapsto \abs{Tu}_W$ is continuous and nonzero on the compact unit sphere, so it has a minimum $c > 0$; then $\abs{Tv} \ge c\abs{v}$ and $\norm{T^{-1}} \le 1/c$.", item="thm-finite-dim-continuous")
c("norms", r"State the comparability of norms on $\R^n$.",
  r"For any norm $\abs{\cdot}_*$ there are $0 < c \le C$ with $c\abs{v} \le \abs{v}_* \le C\abs{v}$ for all $v$.", item="cor-norms-equivalent")
c("unbounded", "Give a linear map that is not continuous.",
  r"Differentiation on polynomials on $[0,1]$ with the sup norm: $\abs{x^k} = 1$ but $\abs{(x^k)'} = k$.", item="ex-unbounded")
c("conorm", r"Define the conorm $m(T)$ of $T : \R^n \to \R^n$ and relate it to $T^{-1}$.",
  r"$m(T) = \inf_{v \ne 0} \abs{Tv}/\abs{v}$. $T$ is invertible iff $m(T) > 0$, and then $m(T) = 1/\norm{T^{-1}}$.", item="prop-conorm")
c("inverse-open", r"How close to an invertible $T$ must $S$ be to be surely invertible, and what is the proof idea?",
  r"$\norm{S - T} < 1/\norm{T^{-1}}$. Write $S = T(I - R)$ with $R = T^{-1}(T-S)$, $\norm{R} < 1$; $I - R$ is invertible because $\abs{(I-R)v} \ge (1 - \norm{R})\abs{v}$.", item="thm-inverse-open")
c("gl", r"What are the two topological facts about $GL(n) \subseteq \mathcal{L}(\R^n,\R^n)$?",
  r"It is open, and $T \mapsto T^{-1}$ is continuous on it.")
S.write()
