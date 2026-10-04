from c5lib import Section
S = Section("5-higher-derivatives")
b, c = S.b, S.c

b("hd-intro", "prose", r"""
The derivative of $f : U \to \R^m$ is itself a function on $U$, namely $x \mapsto (Df)_x$, but its values are
linear maps rather than vectors. To differentiate it again we need derivatives of functions with values in the
finite-dimensional normed space $\mathcal{L}(\R^n,\R^m)$. Once that is set up, the second derivative at a point
turns out to be a \emph{bilinear} map, and the central theorem of the section says it is symmetric. Equality of
mixed partial derivatives is the coordinate form of that symmetry.
""")

b("def-derivative-w", "definition", r"""
Let $W$ be a finite-dimensional normed space, $U \subseteq \R^n$ open, $g : U \to W$, and $p \in U$. We say $g$ is
\emph{differentiable at $p$} if there is a linear map $T : \R^n \to W$ with
\[ \lim_{v \to 0} \frac{\abs{g(p+v) - g(p) - Tv}_W}{\abs{v}} = 0 , \]
and we write $(Dg)_p = T$. For $W = \R^m$ this is the definition of the previous section. The derivative
$(Dg)_p$ is an element of $\mathcal{L}(\R^n, W)$, which is again a finite-dimensional normed space under the
operator norm.
""", title="Derivative of a map into a finite-dimensional normed space")

b("prop-change-target", "proposition", r"""
Let $W$, $W'$ be finite-dimensional normed spaces, $g : U \to W$, $p \in U$, and $\Psi : W \to W'$ linear.
\begin{enumerate}
\item If $g$ is differentiable at $p$ with derivative $T$, then $\Psi \circ g$ is differentiable at $p$ with
derivative $\Psi \circ T$.
\item If $\Psi$ is a bijection, then $g$ is differentiable at $p$ if and only if $\Psi \circ g$ is.
\item The derivative of $g$ at $p$, if it exists, is unique, and $g$ is then continuous at $p$.
\end{enumerate}
""", title="Changing the target by a linear map", proof=r"""
Recall that every linear map between finite-dimensional normed spaces is bounded.

(1) Let $R(v) = g(p+v) - g(p) - Tv$. By linearity of $\Psi$,
$\Psi g(p+v) - \Psi g(p) - \Psi T v = \Psi(R(v))$, and
$\abs{\Psi(R(v))}_{W'} / \abs{v} \le \norm{\Psi}\,\abs{R(v)}_W/\abs{v} \to 0$. The map $\Psi \circ T$ is linear.

(2) One direction is (1). For the other, $\Psi^{-1}$ is linear, so if $\Psi \circ g$ is differentiable at $p$ then
by (1) so is $\Psi^{-1} \circ (\Psi \circ g) = g$.

(3) If $W = \set{0}$ everything is trivial. Otherwise choose a basis of $W$ and the corresponding linear bijection
$\Phi : \R^N \to W$. If $T$ and $T'$ are both derivatives of $g$ at $p$, then by (1) $\Phi^{-1}T$ and
$\Phi^{-1}T'$ are both derivatives at $p$ of $\Phi^{-1} \circ g : U \to \R^N$. Derivatives of maps into $\R^N$
are unique, so $\Phi^{-1}T = \Phi^{-1}T'$ and $T = T'$. Moreover $\Phi^{-1} \circ g$ is differentiable, hence
continuous, at $p$, and $g = \Phi \circ (\Phi^{-1} \circ g)$ is its composite with the continuous map $\Phi$.
""", d=2, m=15, hints=[
r"A linear map between finite-dimensional normed spaces is bounded, so it carries a sublinear remainder to a sublinear remainder.",
r"For (3), transport the question to $\R^N$ with a linear bijection $\Phi : \R^N \to W$.",
], uses=["def-derivative-w", "cor-finite-dim", "thm-derivative-unique", "thm-diff-continuous"])

b("rem-transport", "remark", r"""
Through a linear bijection $\Phi : \R^N \to W$, a map $g : U \to W$ becomes the map $\Phi^{-1} \circ g : U \to \R^N$
of the previous section, and the proposition says that nothing about differentiability is lost or gained. Two
rules carry over at once. \emph{Linearity:} if $g, h : U \to W$ are differentiable at $p$ and $c \in \R$, then
$\Phi^{-1} \circ (g + ch) = \Phi^{-1} \circ g + c\,\Phi^{-1} \circ h$ is differentiable at $p$ with derivative
$\Phi^{-1} \circ (Dg)_p + c\,\Phi^{-1} \circ (Dh)_p$, by part (1) of the proposition and the linearity rule in
$\R^N$; applying part (1) again with $\Psi = \Phi$ shows that $g + ch$ is differentiable at $p$ with
$(D(g + ch))_p = (Dg)_p + c(Dh)_p$. \emph{Linear maps:} if $T : \R^n \to W$ is linear then
$T(p+v) - T(p) - Tv = 0$, so $(DT)_p = T$ at every $p$, straight from the definition.
""")

b("cor-entries", "corollary", r"""
Let $G : U \to \mathcal{L}(\R^n,\R^m)$ and let $g_{ij} : U \to \R$ be the $(i,j)$ entry of the matrix of $G(x)$.
Then $G$ is differentiable at $p$ if and only if every $g_{ij}$ is differentiable at $p$, and in that case, for
each $v \in \R^n$, the matrix of the linear map $(DG)_p(v) \in \mathcal{L}(\R^n,\R^m)$ has entries
$(Dg_{ij})_p(v)$.
""", title="Operator-valued maps are differentiated entry by entry", proof=r"""
Let $E : \mathcal{L}(\R^n,\R^m) \to \R^{mn}$ send a linear map to the list of its matrix entries. It is a linear
bijection, so $G$ is differentiable at $p$ if and only if $E \circ G : U \to \R^{mn}$ is, and then
$(D(E \circ G))_p = E \circ (DG)_p$. The components of $E \circ G$ are the functions $g_{ij}$. Since
differentiability of a map into $\R^{mn}$ is componentwise, $E \circ G$ is differentiable at $p$ if and only if
every $g_{ij}$ is, and the $(i,j)$ component of $(D(E \circ G))_p(v) = E\big( (DG)_p(v) \big)$ is $(Dg_{ij})_p(v)$.
That is exactly the statement that the $(i,j)$ entry of $(DG)_p(v)$ is $(Dg_{ij})_p(v)$.
""", d=2, m=15, hints=[
r"Taking matrix entries is a linear bijection onto $\R^{mn}$; combine the previous proposition with the componentwise criterion.",
], uses=["prop-change-target", "prop-components"])

b("def-second-derivative", "definition", r"""
Let $f : U \to \R^m$ be differentiable on $U$. If the map $Df : U \to \mathcal{L}(\R^n,\R^m)$, $x \mapsto (Df)_x$,
is differentiable at $p$, we say $f$ is \emph{second-differentiable at $p$}, and its \emph{second derivative} is
\[ (D^2 f)_p = (D(Df))_p \in \mathcal{L}\big( \R^n, \mathcal{L}(\R^n,\R^m) \big) . \]
We regard it as a function of two vectors,
\[ (D^2 f)_p(v, w) = \big( (D(Df))_p(v) \big)(w) \in \R^m , \]
which is linear in $v$ and in $w$ separately, that is, bilinear. Its defining property reads
\[ (Df)_{p+v} = (Df)_p + (D^2f)_p(v, \cdot) + R(v), \qquad \frac{\norm{R(v)}}{\abs{v}} \to 0 \text{ as } v \to 0 , \]
where $(D^2f)_p(v, \cdot)$ denotes the linear map $w \mapsto (D^2f)_p(v,w)$.

The \emph{second partial derivatives} of $f$ are the partial derivatives of its partial derivatives:
\[ \frac{\partial^2 f_i}{\partial x_k \partial x_j} = \frac{\partial}{\partial x_k} \Big( \frac{\partial f_i}{\partial x_j} \Big) . \]
""", title="Second derivative")

b("prop-second-partials", "proposition", r"""
If $f : U \to \R^m$ is second-differentiable at $p$, then all second partial derivatives of $f$ exist at $p$, and
\[ \text{the $i$-th component of } (D^2f)_p(e_k, e_j) \ =\ \frac{\partial^2 f_i}{\partial x_k \partial x_j}(p) . \]
Consequently the $i$-th component of $(D^2f)_p(v,w)$ is
$\sum_{k,j} \frac{\partial^2 f_i}{\partial x_k \partial x_j}(p)\, v_k w_j$, and it equals $(D^2 f_i)_p(v,w)$: the
component $f_i$ is second-differentiable at $p$ too.
""", title="The second derivative in coordinates", proof=r"""
The matrix entries of $G = Df$ are $g_{ij} = \frac{\partial f_i}{\partial x_j}$. Since $G$ is differentiable at
$p$, each $g_{ij}$ is differentiable at $p$ and the $(i,j)$ entry of $(DG)_p(v)$ is $(Dg_{ij})_p(v)$. Take
$v = e_k$. Because $g_{ij}$ is differentiable at $p$, its partial derivative in the $x_k$ direction exists and
equals $(Dg_{ij})_p(e_k)$. So
\[ \frac{\partial^2 f_i}{\partial x_k \partial x_j}(p) = (Dg_{ij})_p(e_k) = \text{the $(i,j)$ entry of } (DG)_p(e_k) . \]
The $(i,j)$ entry of a linear map is the $i$-th component of its value at $e_j$, and
$\big((DG)_p(e_k)\big)(e_j) = (D^2f)_p(e_k,e_j)$. This is the displayed formula. Expanding
$v = \sum_k v_ke_k$ and $w = \sum_j w_je_j$ and using bilinearity gives the formula for $(D^2f)_p(v,w)$.

For the last claim, the derivative of $f_i$ is the $i$-th row of $Df$: $(Df_i)_x = \pi_i \circ (Df)_x$, where
$\pi_i : \R^m \to \R$ is the $i$-th coordinate. The map $A \mapsto \pi_i \circ A$ from $\mathcal{L}(\R^n,\R^m)$ to
$\mathcal{L}(\R^n,\R)$ is linear, so composing $Df$ with it preserves differentiability at $p$ and
$(D(Df_i))_p(v) = \pi_i \circ (D(Df))_p(v)$. Evaluating at $w$ gives
$(D^2f_i)_p(v,w) = \pi_i\big( (D^2f)_p(v,w) \big)$.
""", d=2, m=20, hints=[
r"The matrix entries of $Df$ are the first partial derivatives. Differentiate entry by entry.",
r"Apply the entrywise derivative in the direction $e_k$, then evaluate the resulting linear map at $e_j$.",
], uses=["def-second-derivative", "cor-entries", "prop-jacobian", "prop-change-target", "prop-components"])

b("ex-quadratic", "exercise", r"""
Let $A : \R^n \to \R^n$ be linear and $f(x) = \inner{x}{Ax}$ for $x \in \R^n$. Show that $f$ is second-differentiable
at every $p$, with
\[ (Df)_p(w) = \inner{p}{Aw} + \inner{w}{Ap}, \qquad (D^2f)_p(v,w) = \inner{v}{Aw} + \inner{w}{Av} . \]
""", title="A quadratic form", proof=r"""
Expanding by bilinearity of the inner product and linearity of $A$,
\[ f(p+w) = f(p) + \inner{p}{Aw} + \inner{w}{Ap} + \inner{w}{Aw} . \]
The map $w \mapsto \inner{p}{Aw} + \inner{w}{Ap}$ is linear, and
$\abs{\inner{w}{Aw}} \le \abs{w}\,\abs{Aw} \le \norm{A}\abs{w}^2$, so $\abs{\inner{w}{Aw}}/\abs{w} \le \norm{A}\abs{w} \to 0$.
Hence $f$ is differentiable at every $p$ with $(Df)_p(w) = \inner{p}{Aw} + \inner{w}{Ap}$.

This formula shows that $G = Df : \R^n \to \mathcal{L}(\R^n,\R)$ is a linear map of $p$:
$G(p + cq) = G(p) + cG(q)$. Therefore $G(p+v) - G(p) - G(v) = 0$ for all $p, v$, so $G$ is differentiable at
every $p$ with $(DG)_p = G$, that is, $(DG)_p(v) = (Df)_v$. Evaluating at $w$,
\[ (D^2f)_p(v,w) = (Df)_v(w) = \inner{v}{Aw} + \inner{w}{Av} . \]
""", d=2, m=20, hints=[
r"Expand $f(p+w)$ and separate the part linear in $w$ from the quadratic part.",
r"Notice that $p \mapsto (Df)_p$ is linear in $p$, and a linear map is its own derivative.",
], uses=["def-second-derivative", "def-derivative-w", "prop-opnorm-bound"])

b("hd-prose-symmetry", "prose", r"""
In the example the second derivative came out symmetric in $v$ and $w$. This is no accident. The reason is that
$(D^2f)_p(v,w)$ can be computed from a \emph{second difference} of $f$ over a small parallelogram with sides
$tv$ and $tw$, and that second difference does not care which side is called first.
""")

b("lem-second-difference", "lemma", r"""
Let $f : U \to \R$ be differentiable on $U$ and second-differentiable at $p$. For $v, w \in \R^n$ and small
$t \ne 0$ put
\[ \Delta(t) = f(p + tv + tw) - f(p + tv) - f(p + tw) + f(p) . \]
Then
\[ \lim_{t \to 0} \frac{\Delta(t)}{t^2} = (D^2f)_p(v,w) . \]
""", title="The second difference computes the second derivative", proof=r"""
Choose $\rho > 0$ with $\set{x : \abs{x - p} < \rho} \subseteq U$, and for $\abs{x} < \rho$ write
\[ (Df)_{p+x} = (Df)_p + (D^2f)_p(x, \cdot) + R(x), \]
where $R(x) \in \mathcal{L}(\R^n,\R)$ and $\norm{R(x)}/\abs{x} \to 0$ as $x \to 0$. Let $\eps > 0$ and choose
$\delta \in (0,\rho]$ with $\norm{R(x)} \le \eps\abs{x}$ whenever $\abs{x} < \delta$.

Fix $t \ne 0$ with $\abs{t}(\abs{v} + \abs{w}) < \delta$ and define
\[ g(s) = f(p + tv + stw) - f(p + stw) . \]
For $s$ in an open interval containing $[0,1]$ the points $p + tv + stw$ and $p + stw$ are within $\rho$ of $p$,
so $g$ is defined there, and by the chain rule it is differentiable with
\[ g'(s) = (Df)_{p + tv + stw}(tw) - (Df)_{p + stw}(tw) . \]
Now $\Delta(t) = g(1) - g(0)$, so by the one-variable mean value theorem there is a $\theta \in (0,1)$ with
$\Delta(t) = g'(\theta)$. Substituting the expansion of $Df$ at $x = tv + \theta tw$ and at $x = \theta tw$, the
terms $(Df)_p(tw)$ cancel, and by linearity of $(D^2f)_p$ in its first argument
\[ \Delta(t) = (D^2f)_p(tv, tw) + R(tv + \theta tw)(tw) - R(\theta tw)(tw)
= t^2 (D^2f)_p(v,w) + R(tv + \theta tw)(tw) - R(\theta tw)(tw) . \]
Both $\abs{tv + \theta tw}$ and $\abs{\theta tw}$ are at most $\abs{t}(\abs{v} + \abs{w}) < \delta$, so
\[ \abs{ \frac{\Delta(t)}{t^2} - (D^2f)_p(v,w) } \le \frac{ \big( \norm{R(tv + \theta tw)} + \norm{R(\theta tw)} \big) \abs{tw} }{t^2}
\le \frac{ 2\eps\,\abs{t}(\abs{v} + \abs{w})\,\abs{t}\abs{w} }{t^2} = 2\eps(\abs{v} + \abs{w})\abs{w} . \]
This holds for all sufficiently small $t \ne 0$, and $\eps$ was arbitrary, so the limit is $(D^2f)_p(v,w)$.
""", d=4, m=60, hints=[
r"Write $\Delta(t) = g(1) - g(0)$ for $g(s) = f(p + tv + stw) - f(p + stw)$ and use the mean value theorem.",
r"$g'(\theta)$ is a difference of two values of $Df$, applied to $tw$. Expand both with the definition of $(D^2f)_p$ as the derivative of $Df$ at $p$.",
r"The main terms give $t^2(D^2f)_p(v,w)$; the remainders are at most $\eps$ times $\abs{t}(\abs{v}+\abs{w})$ in operator norm, applied to a vector of length $\abs{t}\abs{w}$.",
], uses=["def-second-derivative", "thm-chain-rule", "prop-one-variable", "prop-opnorm-bound"])

b("thm-symmetry", "theorem", r"""
If $f : U \to \R^m$ is second-differentiable at $p$, then $(D^2f)_p$ is symmetric:
\[ (D^2f)_p(v,w) = (D^2f)_p(w,v) \qquad \text{for all } v, w \in \R^n . \]
""", title="Symmetry of the second derivative", proof=r"""
The $i$-th component of $(D^2f)_p(v,w)$ is $(D^2f_i)_p(v,w)$, where $f_i$ is the $i$-th component of $f$, which is
differentiable on $U$ and second-differentiable at $p$. So it suffices to treat a real-valued $f$.

For real-valued $f$, the second difference
$\Delta(t) = f(p + tv + tw) - f(p + tv) - f(p + tw) + f(p)$ is unchanged when $v$ and $w$ are interchanged. By the
lemma on second differences, applied once to the pair $(v,w)$ and once to the pair $(w,v)$,
\[ (D^2f)_p(v,w) = \lim_{t \to 0} \frac{\Delta(t)}{t^2} = (D^2f)_p(w,v) . \]
""", d=2, m=15, hints=[
r"Reduce to real-valued $f$, and find an expression for $(D^2f)_p(v,w)$ that is visibly symmetric in $v$ and $w$.",
], uses=["lem-second-difference", "prop-second-partials"])

b("cor-mixed-partials", "corollary", r"""
\begin{enumerate}
\item If $f : U \to \R^m$ is second-differentiable at $p$, then
$\dfrac{\partial^2 f_i}{\partial x_k \partial x_j}(p) = \dfrac{\partial^2 f_i}{\partial x_j \partial x_k}(p)$ for all
$i, j, k$.
\item If all first and second partial derivatives of $f$ exist and are continuous on $U$, then $f$ is
second-differentiable at every point of $U$; so the mixed partials are equal throughout $U$.
\end{enumerate}
""", title="Equality of mixed partial derivatives", proof=r"""
(1) By the coordinate description of the second derivative, the two numbers are the $i$-th components of
$(D^2f)_p(e_k,e_j)$ and $(D^2f)_p(e_j,e_k)$, which are equal by symmetry of the second derivative.

(2) Since the first partial derivatives are continuous on $U$, $f$ is differentiable on $U$ (indeed $C^1$), and
the matrix entries of $Df$ are the functions $g_{ij} = \frac{\partial f_i}{\partial x_j}$. Each $g_{ij} : U \to \R$
has partial derivatives, the second partials of $f$, that exist and are continuous on $U$; hence each $g_{ij}$ is
differentiable at every point of $U$. An operator-valued map whose matrix entries are differentiable at $p$ is
differentiable at $p$, so $Df$ is differentiable at every $p \in U$. Thus $f$ is second-differentiable on $U$ and
(1) applies.
""", d=2, m=20, hints=[
r"For (1), evaluate the symmetric bilinear map on basis vectors.",
r"For (2), apply the theorem that continuous partials imply differentiability twice: to $f$, and to each $\partial f_i/\partial x_j$.",
], uses=["thm-symmetry", "prop-second-partials", "thm-continuous-partials", "cor-entries"])

b("ex-mixed-partials-fail", "exercise", r"""
Define $f : \R^2 \to \R$ by $f(x,y) = \dfrac{xy(x^2 - y^2)}{x^2 + y^2}$ for $(x,y) \ne (0,0)$ and $f(0,0) = 0$. Show
that
\[ \frac{\partial^2 f}{\partial y\,\partial x}(0,0) = -1 \qquad \text{while} \qquad \frac{\partial^2 f}{\partial x\,\partial y}(0,0) = 1 . \]
(So $f$ is not second-differentiable at the origin.)
""", title="Mixed partials that disagree", proof=r"""
Note $f(0,y) = 0$ and $f(x,0) = 0$ for all $x, y$.

For fixed $y \ne 0$,
\[ \frac{\partial f}{\partial x}(0,y) = \lim_{h \to 0} \frac{f(h,y) - f(0,y)}{h} = \lim_{h \to 0} \frac{y(h^2 - y^2)}{h^2 + y^2} = -y , \]
and $\frac{\partial f}{\partial x}(0,0) = \lim_{h \to 0} (f(h,0) - 0)/h = 0$. So $\frac{\partial f}{\partial x}(0,y) = -y$
for every $y$, and differentiating this function of $y$ at $y = 0$ gives
$\frac{\partial^2 f}{\partial y\,\partial x}(0,0) = -1$.

For fixed $x \ne 0$,
\[ \frac{\partial f}{\partial y}(x,0) = \lim_{h \to 0} \frac{f(x,h) - f(x,0)}{h} = \lim_{h \to 0} \frac{x(x^2 - h^2)}{x^2 + h^2} = x , \]
and $\frac{\partial f}{\partial y}(0,0) = 0$. So $\frac{\partial f}{\partial y}(x,0) = x$ for every $x$, and
$\frac{\partial^2 f}{\partial x\,\partial y}(0,0) = 1$.

If $f$ were second-differentiable at the origin, the mixed partials there would agree.
""", d=2, m=20, hints=[
r"You only need $\partial f/\partial x$ along the $y$-axis and $\partial f/\partial y$ along the $x$-axis; compute them straight from the limit definition.",
], uses=["def-second-derivative", "cor-mixed-partials"])

b("def-higher-derivatives", "definition", r"""
Higher derivatives are defined by repeating the step from $f$ to $Df$. Put $\mathcal{L}^0 = \R^m$ and
$\mathcal{L}^k = \mathcal{L}(\R^n, \mathcal{L}^{k-1})$ for $k \ge 1$, each with the operator norm; these are
finite-dimensional normed spaces. Set $D^0 f = f$. If $D^{r-1}f : U \to \mathcal{L}^{r-1}$ exists on $U$ and is
differentiable at every point of $U$, we say $f$ is \emph{$r$ times differentiable} on $U$ and put
\[ D^r f = D(D^{r-1}f) : U \to \mathcal{L}^r . \]
An element $\beta \in \mathcal{L}^r$ is regarded as a function of $r$ vectors, linear in each (an $r$-linear map):
$\beta(v_1, \dots, v_r) = \big( \cdots (\beta(v_1))(v_2) \cdots \big)(v_r) \in \R^m$. Unwinding the definition of
the operator norm, $\norm{\beta} = \sup \set{ \abs{\beta(v_1,\dots,v_r)} : \abs{v_1}, \dots, \abs{v_r} \le 1 }$.

A \emph{partial derivative of order $r$} of $f_i$ is the result of $r$ successive partial differentiations:
\[ \frac{\partial^r f_i}{\partial x_{j_1} \cdots \partial x_{j_r}}
= \frac{\partial}{\partial x_{j_1}} \Big( \frac{\partial^{r-1} f_i}{\partial x_{j_2} \cdots \partial x_{j_r}} \Big) . \]
""", title="Higher derivatives")

b("cor-higher-mixed", "corollary", r"""
Let $f : U \to \R$ and $r \ge 2$. Suppose all partial derivatives of $f$ of orders $1, \dots, r$ exist and are
continuous on $U$. Then a partial derivative of order $r$ does not depend on the order of differentiation: for
every permutation $\pi$ of $\set{1, \dots, r}$,
\[ \frac{\partial^r f}{\partial x_{j_1} \cdots \partial x_{j_r}} = \frac{\partial^r f}{\partial x_{j_{\pi(1)}} \cdots \partial x_{j_{\pi(r)}}} . \]
""", title="Higher mixed partials commute", proof=r"""
Write $\partial_j$ for $\frac{\partial}{\partial x_j}$, so the left side is
$\partial_{j_1} \partial_{j_2} \cdots \partial_{j_r} f$. Every permutation is a product of transpositions of
adjacent positions, so it is enough to show that interchanging two adjacent operators
$\partial_{j_s}$, $\partial_{j_{s+1}}$ $(1 \le s < r)$ does not change the result.

Let $g = \partial_{j_{s+2}} \cdots \partial_{j_r} f$ (and $g = f$ if $s = r - 1$). This is a partial derivative of
$f$ of order $r - s - 1$, so the first and second partial derivatives of $g$ are partial derivatives of $f$ of
orders $r - s$ and $r - s + 1$, which are at least $1$ and at most $r$. They therefore exist and are continuous
on $U$. By the equality of mixed partial derivatives for functions with continuous first and second partials,
\[ \partial_{j_s} \partial_{j_{s+1}} g = \partial_{j_{s+1}} \partial_{j_s} g \quad \text{on } U . \]
Applying $\partial_{j_1} \cdots \partial_{j_{s-1}}$ to both sides of this identity of functions gives the claim.
""", d=3, m=30, hints=[
r"Every permutation is a product of adjacent transpositions, so swap two neighbouring differentiations.",
r"Apply the second-order result to the function obtained after the inner differentiations have been carried out.",
], uses=["cor-mixed-partials", "def-higher-derivatives"])

b("rem-higher-symmetric", "remark", r"""
In the multilinear language: when $f$ is $r$ times differentiable, the values of $(D^rf)_p$ on basis vectors are
the partial derivatives of order $r$ at $p$, just as for $r = 2$, and $(D^rf)_p$ is a \emph{symmetric}
$r$-linear map, unchanged by any permutation of its arguments. We shall not need more than the statement about
partial derivatives proved above, and take the multilinear version on faith.
""")

c("d2-def", r"What kind of object is $(D^2f)_p$, and what is its defining property?",
  r"The derivative at $p$ of $x \mapsto (Df)_x$: a bilinear map with $(Df)_{p+v} = (Df)_p + (D^2f)_p(v,\cdot) + R(v)$, $\norm{R(v)}/\abs{v} \to 0$.", item="def-second-derivative")
c("d2-coords", r"Express $(D^2f)_p(v,w)$ for real-valued $f$ through partial derivatives.",
  r"$\sum_{k,j} \frac{\partial^2 f}{\partial x_k\partial x_j}(p)\,v_kw_j$: the Hessian matrix as a bilinear form.", item="prop-second-partials")
c("symmetry", "State the symmetry theorem for the second derivative.",
  r"If $f$ is second-differentiable at $p$ then $(D^2f)_p(v,w) = (D^2f)_p(w,v)$; in coordinates, mixed partials at $p$ are equal.", item="thm-symmetry")
c("symmetry-idea", "What is the idea of the proof of symmetry?",
  r"$(D^2f)_p(v,w) = \lim_{t\to0} \Delta(t)/t^2$ with $\Delta(t) = f(p+tv+tw) - f(p+tv) - f(p+tw) + f(p)$, which is symmetric in $v, w$. The limit comes from the mean value theorem applied to $s \mapsto f(p+tv+stw) - f(p+stw)$.", item="lem-second-difference")
c("mixed", "Give a practical sufficient condition for equality of mixed partials on $U$.",
  r"All first and second partial derivatives exist and are continuous on $U$ (then $f$ is second-differentiable everywhere).", item="cor-mixed-partials")
c("mixed-counter", "Give a function whose mixed second partials at the origin differ.",
  r"$f(x,y) = xy(x^2-y^2)/(x^2+y^2)$, $f(0,0)=0$: $f_x(0,y) = -y$ and $f_y(x,0) = x$, so the mixed partials are $-1$ and $1$.", item="ex-mixed-partials-fail")
c("op-entries", r"How do you differentiate a map $G : U \to \mathcal{L}(\R^n,\R^m)$?",
  r"Entry by entry: $G$ is differentiable at $p$ iff each matrix entry $g_{ij}$ is, and $(DG)_p(v)$ has entries $(Dg_{ij})_p(v)$.", item="cor-entries")
S.write()
