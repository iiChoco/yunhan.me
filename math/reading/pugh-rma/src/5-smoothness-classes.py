from c5lib import Section
S = Section("5-smoothness-classes")
b, c = S.b, S.c

b("sc-intro", "prose", r"""
Functions are sorted by how many times they can be differentiated with a continuous result: $C^0$, $C^1$,
$C^2$, and so on up to $C^\infty$. This section does two things with that scale. First it shows that the
classes are robust: membership can be tested on partial derivatives, and sums, products, quotients and
composites of $C^r$ functions are $C^r$. Then it makes $C^r$ into a normed space, measuring a function by the
size of all its derivatives up to order $r$, and proves that this space is complete. Completeness is what allows
a function to be built as a limit or a series while keeping control of its derivatives. Throughout,
$U \subseteq \R^n$ is a nonempty open set and $W$, $W'$ denote finite-dimensional normed spaces.
""")

b("def-cr", "definition", r"""
Let $g : U \to W$. Put $\mathcal{L}^0(W) = W$ and $\mathcal{L}^k(W) = \mathcal{L}(\R^n, \mathcal{L}^{k-1}(W))$
for $k \ge 1$, with the operator norms; these are finite-dimensional normed spaces. Set $D^0g = g$. For $r \ge 1$,
$g$ is \emph{$r$ times differentiable} on $U$ if $D^{r-1}g : U \to \mathcal{L}^{r-1}(W)$ exists and is
differentiable at every point of $U$, and then $D^rg = D(D^{r-1}g) : U \to \mathcal{L}^r(W)$. (For $W = \R^m$
this is the definition of higher derivatives already given.)

The map $g$ is \emph{of class $C^r$} if it is $r$ times differentiable on $U$ and $D^rg$ is continuous; $C^0$
means continuous. It is \emph{of class $C^\infty$}, or \emph{smooth}, if it is $C^r$ for every $r$.
""", title="Class $C^r$")

b("prop-peel", "proposition", r"""
Let $g : U \to W$ and $r \ge 1$.
\begin{enumerate}
\item $g$ is $r$ times differentiable on $U$ if and only if $g$ is differentiable on $U$ and
$Dg : U \to \mathcal{L}(\R^n, W)$ is $r - 1$ times differentiable on $U$; in that case
$D^{r-1}(Dg) = D^r g$.
\item $g$ is $C^r$ if and only if $g$ is differentiable on $U$ and $Dg$ is $C^{r-1}$.
\item If $g$ is $C^r$, then $g$ is $C^{r-1}$.
\end{enumerate}
""", title="Peeling off one derivative")

b("rem-peel", "remark", r"""
This proposition is bookkeeping and is stated without proof. For (1) one checks by induction on $k$ that
$\mathcal{L}^k\big(\mathcal{L}(\R^n, W)\big) = \mathcal{L}^{k+1}(W)$ and that $D^k(Dg)$ exists exactly when
$D^{k+1}g$ does, the two then being equal; the inductive step only unwinds the definition
$D^{k+1} = D \circ D^k$. Part (2) is (1) together with the definition of $C^r$. Part (3) holds because
$D^{r-1}g$ is differentiable at every point of $U$, and a differentiable map into a finite-dimensional normed
space is continuous.
""")

b("lem-cr-linear", "lemma", r"""
Let $r \ge 0$.
\begin{enumerate}
\item If $g, h : U \to W$ are $C^r$ and $c \in \R$, then $g + ch$ is $C^r$ and $D^k(g + ch) = D^kg + cD^kh$ for
$0 \le k \le r$.
\item If $g : U \to W$ is $C^r$ and $\Psi : W \to W'$ is linear, then $\Psi \circ g$ is $C^r$.
\item Constant maps $U \to W$, and restrictions to $U$ of linear maps $\R^n \to W$, are $C^r$.
\item A map $f = (f_1, \dots, f_m) : U \to \R^m$ is $C^r$ if and only if each $f_i : U \to \R$ is $C^r$. A map
$G : U \to \mathcal{L}(\R^n,\R^m)$ is $C^r$ if and only if each of its matrix entries $g_{ij} : U \to \R$ is $C^r$.
\end{enumerate}
""", title="Linear operations preserve $C^r$", proof=r"""
Each of (1), (2), (3) is proved by induction on $r$, for all spaces $W$, $W'$ at once, using that for $r \ge 1$ a
map is $C^r$ if and only if it is differentiable with $C^{r-1}$ derivative.

(1) For $r = 0$: $g + ch$ is continuous, since
$\abs{(g+ch)(x) - (g+ch)(p)} \le \abs{g(x) - g(p)} + \abs{c}\abs{h(x) - h(p)}$. Let $r \ge 1$ and assume the
claim for $r - 1$. At each $p$, if $R$ and $Q$ are the remainders of $g$ and $h$ then $g + ch$ has remainder
$R + cQ$ relative to the linear map $(Dg)_p + c(Dh)_p$, and $\abs{R(v) + cQ(v)}/\abs{v} \to 0$. So $g + ch$ is
differentiable with $D(g + ch) = Dg + cDh$. Here $Dg$ and $Dh$ are $C^{r-1}$ maps into $\mathcal{L}(\R^n, W)$, so
by the inductive hypothesis $Dg + cDh$ is $C^{r-1}$ and $D^{k}(Dg + cDh) = D^k(Dg) + cD^k(Dh)$ for $k \le r - 1$.
Hence $g + ch$ is $C^r$, and $D^{k+1}(g + ch) = D^{k+1}g + cD^{k+1}h$.

(2) For $r = 0$: $\Psi$ is bounded, hence continuous, so $\Psi \circ g$ is continuous. Let $r \ge 1$ and assume
the claim for $r - 1$ and all linear maps between finite-dimensional normed spaces. By the rule for changing
the target, $\Psi \circ g$ is differentiable with $(D(\Psi \circ g))_x = \Psi \circ (Dg)_x$. In other words
$D(\Psi \circ g) = \Psi_* \circ Dg$, where $\Psi_* : \mathcal{L}(\R^n, W) \to \mathcal{L}(\R^n, W')$,
$\Psi_*(A) = \Psi \circ A$, is linear. Since $Dg$ is $C^{r-1}$, the inductive hypothesis applied to $\Psi_*$
shows $D(\Psi \circ g)$ is $C^{r-1}$. Hence $\Psi \circ g$ is $C^r$.

(3) A constant map is continuous, and differentiable with derivative the constant map $x \mapsto 0$. So if
constant maps are $C^{r-1}$ (into any $W$), then they are $C^r$. A linear $T : \R^n \to W$ is bounded, hence
continuous, and $T(p+v) - T(p) - Tv = 0$ shows it is differentiable with $(DT)_p = T$ for all $p$; thus $DT$ is a
constant map into $\mathcal{L}(\R^n,W)$, which is $C^{r-1}$ for every $r \ge 1$. So $T$ is $C^r$.

(4) If $f$ is $C^r$ then $f_i = \pi_i \circ f$ is $C^r$ by (2), where $\pi_i : \R^m \to \R$ is the $i$-th
coordinate. Conversely $f = \sum_i \iota_i \circ f_i$, where $\iota_i : \R \to \R^m$, $\iota_i(t) = te_i$, is
linear; so if every $f_i$ is $C^r$ then $f$ is $C^r$ by (2) and (1). The same argument works for $G$: the entry
$g_{ij}$ is $G$ followed by the linear map taking a linear map to its $(i,j)$ entry, and
$G = \sum_{i,j} \iota_{ij} \circ g_{ij}$, where $\iota_{ij} : \R \to \mathcal{L}(\R^n,\R^m)$ sends $t$ to $t$ times
the linear map whose matrix has a $1$ in position $(i,j)$ and zeros elsewhere.
""", d=3, m=35, hints=[
r"Induct on $r$, using: $C^r$ means differentiable with $C^{r-1}$ derivative. Make the inductive hypothesis range over all target spaces.",
r"For (2), $D(\Psi\circ g) = \Psi_* \circ Dg$ with $\Psi_*(A) = \Psi\circ A$ again linear. For (4), write $f$ as a sum of linear maps applied to its components.",
], uses=["prop-peel", "prop-change-target", "cor-finite-dim", "def-derivative-w"])

b("thm-cr-partials", "theorem", r"""
Let $r \ge 1$. A map $f : U \to \R^m$ is of class $C^r$ if and only if all partial derivatives of its components
$f_i$ of orders $1, \dots, r$ exist and are continuous on $U$.
""", title="$C^r$ in terms of partial derivatives", proof=r"""
By induction on $r$. For $r = 1$ this is the statement that $f$ is $C^1$ if and only if its first partial
derivatives exist and are continuous.

Let $r \ge 2$ and assume the theorem for $r - 1$ (for real-valued maps). By peeling off one derivative, $f$ is
$C^r$ if and only if $f$ is differentiable on $U$ and $Df : U \to \mathcal{L}(\R^n,\R^m)$ is $C^{r-1}$. When $f$
is differentiable the matrix entries of $Df$ are the functions $\frac{\partial f_i}{\partial x_j}$, and an
operator-valued map is $C^{r-1}$ if and only if its entries are. So:
\[ f \text{ is } C^r \iff f \text{ is differentiable on } U \text{ and each } \tfrac{\partial f_i}{\partial x_j} : U \to \R \text{ is } C^{r-1} . \]
By the inductive hypothesis, $\frac{\partial f_i}{\partial x_j}$ is $C^{r-1}$ if and only if its partial
derivatives of orders $1, \dots, r-1$ exist and are continuous; these are partial derivatives of $f_i$ of orders
$2, \dots, r$, and every partial derivative of $f_i$ of order between $2$ and $r$ arises this way.

Suppose $f$ is $C^r$. Then $f$ is $C^1$, so its first partials exist and are continuous, and by the above so are
the partials of orders $2, \dots, r$.

Conversely suppose all partials of orders $1, \dots, r$ exist and are continuous. Continuity of the first
partials makes $f$ differentiable on $U$. Each $\frac{\partial f_i}{\partial x_j}$ has continuous partial
derivatives of orders $1, \dots, r - 1$, so it is $C^{r-1}$ by the inductive hypothesis. Hence $f$ is $C^r$.
""", d=3, m=30, hints=[
r"Induct on $r$. The case $r = 1$ is already known.",
r"$f$ is $C^r$ iff it is differentiable and the entries $\partial f_i/\partial x_j$ of $Df$ are $C^{r-1}$; apply the inductive hypothesis to those entries.",
], uses=["prop-peel", "lem-cr-linear", "prop-c1-partials", "prop-jacobian", "thm-continuous-partials"])

b("thm-cr-algebra", "theorem", r"""
Let $r \ge 0$.
\begin{enumerate}
\item If $u, v : U \to \R$ are $C^r$, then $uv$ is $C^r$.
\item If $u : U \to \R$ is $C^r$ and never zero, then $1/u$ is $C^r$.
\item If $f : U \to \R^m$ is $C^r$ with $f(U) \subseteq V$, where $V \subseteq \R^m$ is open, and
$g : V \to \R^l$ is $C^r$, then $g \circ f$ is $C^r$.
\end{enumerate}
""", title="Products, reciprocals and composites of $C^r$ maps are $C^r$", proof=r"""
We prove the three statements together by induction on $r$, for all dimensions and all open sets. For $r = 0$
they are the familiar facts about continuous functions. Let $r \ge 1$ and assume all three for $r - 1$.

We use the following criterion, which combines peeling off one derivative with the entrywise test for
operator-valued maps: a map $h : U \to \R^m$ is $C^r$ if and only if it is differentiable on $U$ and all its
first partial derivatives $\frac{\partial h_i}{\partial x_j}$ are $C^{r-1}$. Also, a $C^r$ map is $C^{r-1}$, and
sums and scalar multiples of $C^{r-1}$ functions are $C^{r-1}$. Write $\partial_j$ for
$\frac{\partial}{\partial x_j}$.

(1) By the Leibniz rule $uv$ is differentiable and $\partial_j(uv) = u\,\partial_jv + v\,\partial_ju$. The
functions $u$, $v$, $\partial_ju$, $\partial_jv$ are all $C^{r-1}$, so by (1) for $r - 1$ the products
$u\,\partial_jv$ and $v\,\partial_ju$ are $C^{r-1}$, and so is their sum. Hence $uv$ is $C^r$.

(2) The function $\varphi(t) = 1/t$ is differentiable on the open set $\R \setminus \set{0}$ with
$\varphi'(t) = -1/t^2$, and $1/u = \varphi \circ u$. By the chain rule $1/u$ is differentiable with
\[ \partial_j(1/u) = -\frac{1}{u} \cdot \frac{1}{u} \cdot \partial_ju . \]
Since $u$ is $C^{r-1}$ and never zero, $1/u$ is $C^{r-1}$ by (2) for $r - 1$; also $\partial_ju$ is $C^{r-1}$. By
(1) for $r - 1$ the product is $C^{r-1}$. Hence $1/u$ is $C^r$.

(3) By the chain rule $g \circ f$ is differentiable, and since the Jacobian matrix of a composite is the product
of the Jacobian matrices,
\[ \partial_j (g \circ f)_i = \sum_{k=1}^m \big( \partial_k g_i \circ f \big) \cdot \partial_j f_k , \]
where $\partial_k g_i$ denotes the partial derivative of $g_i$ in its $k$-th variable. Here
$\partial_k g_i : V \to \R$ is $C^{r-1}$ and $f : U \to V$ is $C^{r-1}$, so $\partial_k g_i \circ f$ is $C^{r-1}$
by (3) for $r - 1$. Also $\partial_j f_k$ is $C^{r-1}$. By (1) for $r-1$ each product is $C^{r-1}$, and so is the
sum. Hence $g \circ f$ is $C^r$.
""", d=3, m=40, hints=[
r"Prove all three together by induction on $r$. A map is $C^r$ iff it is differentiable and its first partials are $C^{r-1}$.",
r"Write the first partials of $uv$, $1/u$ and $g\circ f$ by the Leibniz and chain rules; each is built from $C^{r-1}$ functions by the three operations at level $r-1$.",
], uses=["prop-peel", "lem-cr-linear", "thm-leibniz", "thm-chain-rule", "prop-jacobian"])

b("cor-inversion-smooth", "corollary", r"""
Identify $\mathcal{L}(\R^n,\R^n)$ with $\R^{n^2}$ by listing matrix entries, and let $\mathcal{U} \subseteq \R^{n^2}$
be the set of invertible matrices. Then $\mathcal{U}$ is open, and inversion $A \mapsto A^{-1}$ is a $C^\infty$
map $\mathcal{U} \to \R^{n^2}$.
""", title="Matrix inversion is smooth", proof=r"""
Fix $r \ge 0$. Each coordinate function on $\R^{n^2}$ (a single matrix entry) is linear, hence $C^r$. A polynomial
in the entries is a finite sum of constant multiples of products of coordinate functions, so it is $C^r$ on
$\R^{n^2}$, because products, sums and scalar multiples of $C^r$ functions are $C^r$. In particular the
determinant and all cofactors are $C^r$ functions of the matrix.

Since $\det$ is continuous, $\mathcal{U} = \set{A : \det A \ne 0}$ is open. By Cramer's rule each entry of
$A^{-1}$ is a cofactor of $A$ divided by $\det A$. On $\mathcal{U}$ the function $\det$ is $C^r$ and never zero,
so $1/\det$ is $C^r$, and each entry of $A^{-1}$ is a product of two $C^r$ functions on $\mathcal{U}$, hence
$C^r$. A map into $\R^{n^2}$ with $C^r$ components is $C^r$. As $r$ was arbitrary, inversion is $C^\infty$.
""", d=2, m=15, hints=[
r"Cramer's rule writes each entry of $A^{-1}$ as a polynomial in the entries of $A$ divided by $\det A$.",
], uses=["thm-cr-algebra", "lem-cr-linear"])

b("sc-prose-norm", "prose", r"""
Now the analysis. In Chapter 4 the sup norm made $C^0$ a complete space and uniform convergence its notion of
convergence. The $C^r$ norm does the same while keeping track of derivatives: two functions are $C^r$-close when
their values and all their derivatives up to order $r$ are uniformly close.
""")

b("def-cr-norm", "definition", r"""
For a $C^r$ map $f : U \to \R^m$ the \emph{$C^r$ norm} is
\[ \norm{f}_r = \max_{0 \le k \le r}\ \sup_{x \in U} \norm{(D^kf)_x} \ \in [0, \infty] , \]
where $\norm{(D^kf)_x}$ is the norm of $(D^kf)_x$ in $\mathcal{L}^k(\R^m)$ (for $k = 0$ it is $\abs{f(x)}$). The set
of $C^r$ maps $f : U \to \R^m$ with $\norm{f}_r < \infty$ is denoted $C^r(U, \R^m)$.

A sequence $(f_k)$ in $C^r(U,\R^m)$ \emph{converges uniformly $C^r$} to $f$ if $\norm{f_k - f}_r \to 0$; that is,
if $D^jf_k \to D^jf$ uniformly on $U$ for each $j = 0, \dots, r$. It is \emph{uniformly $C^r$ Cauchy} if for
every $\eps > 0$ there is a $K$ with $\norm{f_k - f_l}_r < \eps$ for all $k, l \ge K$.
""", title="The $C^r$ norm and uniform $C^r$ convergence")

b("prop-cr-norm", "proposition", r"""
$C^r(U,\R^m)$ is a vector space under pointwise operations, and $\norm{\cdot}_r$ is a norm on it.
""", title="The $C^r$ norm is a norm", proof=r"""
Let $f, g \in C^r(U,\R^m)$ and $c \in \R$. Then $f + cg$ is $C^r$ and $D^k(f + cg) = D^kf + cD^kg$ for $k \le r$.
For each $x \in U$ and $k \le r$, the triangle inequality and homogeneity of the norm of $\mathcal{L}^k(\R^m)$ give
\[ \norm{(D^k(f + cg))_x} \le \norm{(D^kf)_x} + \abs{c}\,\norm{(D^kg)_x} \le \norm{f}_r + \abs{c}\,\norm{g}_r . \]
Taking the supremum over $x$ and the maximum over $k$, $\norm{f + cg}_r \le \norm{f}_r + \abs{c}\norm{g}_r < \infty$.
So $C^r(U,\R^m)$ is closed under sums and scalar multiples, hence a vector space, and with $c = 1$ this is the
triangle inequality. Homogeneity: $D^k(cf) = cD^kf$, so $\sup_x \norm{(D^k(cf))_x} = \abs{c}\sup_x\norm{(D^kf)_x}$ for
each $k$, and $\norm{cf}_r = \abs{c}\norm{f}_r$. Finally $\norm{f}_r \ge \sup_x \abs{f(x)}$, so $\norm{f}_r = 0$ forces
$f = 0$, and the zero function has norm $0$.
""", d=1, m=10, hints=[
r"Everything follows from $D^k(f + cg) = D^kf + cD^kg$ and the norm properties in each $\mathcal{L}^k$.",
], uses=["def-cr-norm", "lem-cr-linear"])

b("lem-uniform-limit", "lemma", r"""
Let $X$ be a metric space and $Y$ a normed space. Let $g_k : X \to Y$ be continuous maps and $g : X \to Y$ a map
with $\sup_{x \in X} \abs{g_k(x) - g(x)} \to 0$ as $k \to \infty$. Then $g$ is continuous.
""", title="Uniform limits of continuous maps are continuous", proof=r"""
Let $p \in X$ and $\eps > 0$. Choose $k$ with $\sup_x \abs{g_k(x) - g(x)} < \eps/3$, and then, by continuity of
$g_k$ at $p$, a $\delta > 0$ such that $d(x,p) < \delta$ implies $\abs{g_k(x) - g_k(p)} < \eps/3$. For such $x$,
\[ \abs{g(x) - g(p)} \le \abs{g(x) - g_k(x)} + \abs{g_k(x) - g_k(p)} + \abs{g_k(p) - g(p)} < \eps . \]
""", d=2, m=15, hints=[
r"The $\eps/3$ argument of Chapter 4 works unchanged.",
], uses=[])

b("lem-c1-limit", "lemma", r"""
Let $f_k : U \to \R^m$ be $C^1$ maps. Suppose $f_k \to f$ pointwise on $U$, and suppose there is a map
$G : U \to \mathcal{L}(\R^n,\R^m)$ such that $Df_k \to G$ uniformly on $U$:
$\sup_{x \in U} \norm{(Df_k)_x - G(x)} \to 0$. Then $f$ is $C^1$ and $Df = G$.
""", title="The limit of the derivatives is the derivative of the limit", proof=r"""
Each $Df_k$ is continuous, so $G$ is continuous, being a uniform limit of continuous maps.

Fix $p \in U$, choose $\rho > 0$ with $\set{x : \abs{x-p} < \rho} \subseteq U$, and let $0 < \abs{v} < \rho$. The
segment $[p, p+v]$ lies in $U$, so by the $C^1$ mean value theorem
\[ f_k(p+v) - f_k(p) = T_k v, \qquad T_k = \int_0^1 (Df_k)_{p+tv}\,dt . \]
Put $T = \int_0^1 G(p+tv)\,dt$, which makes sense because $t \mapsto G(p+tv)$ is continuous. The integral of
operator-valued functions is linear (it is computed entry by entry), so
\[ \norm{T_k - T} = \norm{ \int_0^1 \big( (Df_k)_{p+tv} - G(p+tv) \big)\,dt } \le \int_0^1 \norm{(Df_k)_{p+tv} - G(p+tv)}\,dt
\le \sup_{x \in U} \norm{(Df_k)_x - G(x)} , \]
which tends to $0$. Hence $T_kv \to Tv$. Since also $f_k(p+v) - f_k(p) \to f(p+v) - f(p)$, we get
\[ f(p+v) - f(p) = Tv = \Big( \int_0^1 G(p+tv)\,dt \Big) v . \]
Because $G(p) = \int_0^1 G(p)\,dt$, it follows that
\[ \abs{f(p+v) - f(p) - G(p)v} = \abs{ \Big( \int_0^1 \big( G(p+tv) - G(p) \big)\,dt \Big) v }
\le \Big( \int_0^1 \norm{G(p+tv) - G(p)}\,dt \Big) \abs{v} . \]
Let $\eps > 0$. By continuity of $G$ at $p$ there is a $\delta \in (0,\rho]$ with $\norm{G(x) - G(p)} < \eps$ for
$\abs{x - p} < \delta$. If $0 < \abs{v} < \delta$ then every $p + tv$, $0 \le t \le 1$, is within $\delta$ of $p$,
so the last integral is at most $\eps$ and
$\abs{f(p+v) - f(p) - G(p)v} \le \eps\abs{v}$. Thus $f$ is differentiable at $p$ with $(Df)_p = G(p)$. Since $G$ is
continuous, $f$ is $C^1$.
""", d=3, m=45, hints=[
r"Differentiability of $f_k$ cannot be passed to the limit directly. Pass an integral formula to the limit instead.",
r"By the $C^1$ mean value theorem, $f_k(p+v) - f_k(p) = \big(\int_0^1 (Df_k)_{p+tv}\,dt\big)v$. Let $k \to \infty$ using uniform convergence of $Df_k$.",
r"You get $f(p+v) - f(p) = \big(\int_0^1 G(p+tv)\,dt\big)v$; compare with $G(p)v$ and use continuity of $G$ at $p$.",
], uses=["lem-uniform-limit", "thm-c1-mvt", "lem-integral-norm", "def-c1"])

b("cor-c1-limit-w", "corollary", r"""
Let $W$ be a finite-dimensional normed space and $g_k : U \to W$ be $C^1$ maps. Suppose $g_k \to g$ pointwise on
$U$ and $Dg_k \to G$ uniformly on $U$ for some $G : U \to \mathcal{L}(\R^n, W)$. Then $g$ is $C^1$ and $Dg = G$.
""", title="The same for maps into a finite-dimensional normed space", proof=r"""
If $W = \set{0}$ there is nothing to prove. Otherwise choose a linear bijection $\Phi : \R^N \to W$; both $\Phi$
and $\Phi^{-1}$ are bounded. Put $f_k = \Phi^{-1} \circ g_k$ and $f = \Phi^{-1} \circ g$, maps $U \to \R^N$.

By the rule for changing the target, $f_k$ is differentiable with $(Df_k)_x = \Phi^{-1} \circ (Dg_k)_x$. Since
$\norm{\Phi^{-1} \circ A - \Phi^{-1} \circ B} \le \norm{\Phi^{-1}}\,\norm{A - B}$ for $A, B \in \mathcal{L}(\R^n,W)$,
the map $x \mapsto (Df_k)_x$ is continuous, so $f_k$ is $C^1$, and
\[ \sup_{x \in U} \norm{(Df_k)_x - \Phi^{-1} \circ G(x)} \le \norm{\Phi^{-1}}\,\sup_{x \in U}\norm{(Dg_k)_x - G(x)} \to 0 . \]
Also $f_k \to f$ pointwise because $\Phi^{-1}$ is continuous. By the lemma, $f$ is $C^1$ with
$(Df)_x = \Phi^{-1} \circ G(x)$. Changing the target back by $\Phi$, the map $g = \Phi \circ f$ is differentiable
with $(Dg)_x = \Phi \circ \Phi^{-1} \circ G(x) = G(x)$. Finally $G$ is continuous as a uniform limit of the
continuous maps $Dg_k$, so $g$ is $C^1$.
""", d=2, m=20, hints=[
r"Transport everything to $\R^N$ by a linear bijection $\Phi : \R^N \to W$; $\Phi$ and $\Phi^{-1}$ are bounded, so uniform convergence survives.",
], uses=["lem-c1-limit", "prop-change-target", "cor-finite-dim", "prop-opnorm-is-norm", "lem-uniform-limit"])

b("thm-cr-complete", "theorem", r"""
$C^r(U,\R^m)$ is complete with respect to the $C^r$ norm: every uniformly $C^r$ Cauchy sequence $(f_k)$ in
$C^r(U,\R^m)$ converges uniformly $C^r$ to some $f \in C^r(U,\R^m)$.
""", title="$C^r$ is a complete normed space", proof=r"""
Let $(f_k)$ be Cauchy in $C^r(U,\R^m)$. Since $D^j$ is linear, for $0 \le j \le r$ and $x \in U$,
\[ \norm{(D^jf_k)_x - (D^jf_l)_x} = \norm{(D^j(f_k - f_l))_x} \le \norm{f_k - f_l}_r . \]
So $\big( (D^jf_k)_x \big)_k$ is a Cauchy sequence in the finite-dimensional normed space $\mathcal{L}^j(\R^m)$,
which is complete; call its limit $G_j(x)$. This defines maps $G_j : U \to \mathcal{L}^j(\R^m)$.

\emph{The convergence is uniform.} Given $\eps > 0$ choose $K$ with $\norm{f_k - f_l}_r \le \eps$ for
$k, l \ge K$. Fix $k \ge K$ and $x \in U$ and let $l \to \infty$ in
$\norm{(D^jf_k)_x - (D^jf_l)_x} \le \eps$; since the norm is continuous, $\norm{(D^jf_k)_x - G_j(x)} \le \eps$. Thus
\[ \sup_{x \in U} \norm{(D^jf_k)_x - G_j(x)} \le \eps \qquad \text{for all } k \ge K,\ 0 \le j \le r. \tag{$*$} \]
In particular each $G_j$ is continuous, as a uniform limit of the continuous maps $D^jf_k$.

\emph{The limits are the derivatives of $f = G_0$.} We show by induction on $j$ that $f$ is $j$ times
differentiable on $U$ with $D^jf = G_j$, for $0 \le j \le r$. This holds for $j = 0$. Suppose it holds for some
$j < r$. The maps $g_k = D^jf_k : U \to \mathcal{L}^j(\R^m)$ are differentiable with $Dg_k = D^{j+1}f_k$, which
is continuous because $f_k$ is $C^{j+1}$; so each $g_k$ is $C^1$. They converge pointwise to $G_j = D^jf$, and
$Dg_k = D^{j+1}f_k \to G_{j+1}$ uniformly on $U$ by $(*)$. By the limit theorem for maps into a
finite-dimensional normed space, $D^jf$ is $C^1$ with $D(D^jf) = G_{j+1}$. So $f$ is $j+1$ times differentiable
and $D^{j+1}f = G_{j+1}$.

\emph{Conclusion.} $f$ is $r$ times differentiable and $D^rf = G_r$ is continuous, so $f$ is $C^r$. By $(*)$ with
$D^jf = G_j$,
\[ \sup_{x}\norm{(D^jf)_x} \le \eps + \sup_x \norm{(D^jf_K)_x} \le \eps + \norm{f_K}_r < \infty \]
for each $j \le r$, so $f \in C^r(U,\R^m)$; and $(*)$ says $\norm{f_k - f}_r \le \eps$ for all $k \ge K$. Hence
$f_k \to f$ uniformly $C^r$.
""", d=4, m=60, hints=[
r"For each $j \le r$ and each $x$, the sequence $(D^jf_k)_x$ is Cauchy in a complete space. Call the limits $G_j(x)$ and show the convergence is uniform.",
r"The real issue is to show $G_{j+1}$ is the derivative of $G_j$. That is exactly what the lemma on limits of derivatives is for.",
r"Apply the limit lemma (in its version for maps into a finite-dimensional normed space) to $g_k = D^jf_k$, inductively in $j$.",
], uses=["def-cr-norm", "prop-cr-norm", "cor-c1-limit-w", "lem-uniform-limit", "cor-finite-dim", "lem-cr-linear", "prop-peel"])

b("thm-cr-m-test", "theorem", r"""
Let $(f_k)$ be a sequence in $C^r(U,\R^m)$ and let $M_k \ge 0$ be constants with $\norm{f_k}_r \le M_k$ and
$\sum_{k=1}^\infty M_k < \infty$. Then the series $\sum_k f_k$ converges uniformly $C^r$ to a function
$F \in C^r(U,\R^m)$, and it may be differentiated term by term: for $0 \le j \le r$,
\[ D^jF = \sum_{k=1}^\infty D^jf_k , \qquad \text{the series converging uniformly on } U . \]
""", title="The $C^r$ M-test", proof=r"""
Let $S_N = f_1 + \dots + f_N \in C^r(U,\R^m)$. For $N > L$, the triangle inequality for the $C^r$ norm gives
\[ \norm{S_N - S_L}_r = \norm{ \sum_{k=L+1}^N f_k }_r \le \sum_{k=L+1}^N M_k . \]
Since $\sum M_k$ converges, its partial sums are Cauchy: given $\eps > 0$ there is a $K$ with
$\sum_{k=L+1}^N M_k < \eps$ whenever $N > L \ge K$. So $(S_N)$ is uniformly $C^r$ Cauchy, and by completeness of
$C^r(U,\R^m)$ it converges uniformly $C^r$ to some $F \in C^r(U,\R^m)$.

By linearity of $D^j$, $D^jS_N = \sum_{k=1}^N D^jf_k$, and
$\sup_x \norm{(D^jS_N)_x - (D^jF)_x} \le \norm{S_N - F}_r \to 0$. That is, the series $\sum_k D^jf_k$ converges
uniformly on $U$ to $D^jF$.
""", d=2, m=20, hints=[
r"Show the partial sums are Cauchy in the $C^r$ norm and invoke completeness.",
], uses=["thm-cr-complete", "prop-cr-norm", "lem-cr-linear"])

b("ex-cr-series", "example", r"""
In one variable ($n = m = 1$), $(D^jf)_x$ is the $j$-linear map $(h_1, \dots, h_j) \mapsto f^{(j)}(x)h_1 \cdots h_j$,
whose norm is $\abs{f^{(j)}(x)}$; so $\norm{f}_r = \max_{j \le r} \sup_x \abs{f^{(j)}(x)}$. Take
\[ f_k(x) = \frac{\sin(kx)}{k^{r+2}}, \qquad x \in \R . \]
Its $j$-th derivative is $\pm k^{j-r-2}$ times $\sin(kx)$ or $\cos(kx)$, so $\norm{f_k}_r = k^{-2}$. Since
$\sum k^{-2} < \infty$, the $C^r$ M-test shows $F(x) = \sum_k \sin(kx)/k^{r+2}$ is of class $C^r$ on $\R$, with
derivatives up to order $r$ given by differentiating the series term by term.
""", title="A trigonometric series of class $C^r$")

c("cr-def", r"Define: $f : U \to \R^m$ is of class $C^r$; of class $C^\infty$.",
  r"$f$ is $r$ times differentiable on $U$ and $D^rf$ is continuous; equivalently all partials of orders $\le r$ exist and are continuous. $C^\infty$: $C^r$ for every $r$.", item="thm-cr-partials")
c("peel", r"What is the inductive description of $C^r$ that drives every proof in this section?",
  r"For $r \ge 1$: $f$ is $C^r$ iff $f$ is differentiable and $Df$ (equivalently every first partial) is $C^{r-1}$.", item="prop-peel")
c("cr-algebra", r"Which operations preserve $C^r$?",
  r"Linear combinations, composition with linear maps, products, reciprocals of nonvanishing functions, composition. Hence matrix inversion is $C^\infty$.", item="thm-cr-algebra")
c("cr-norm", r"Define the $C^r$ norm and uniform $C^r$ convergence.",
  r"$\norm{f}_r = \max_{k \le r}\sup_{x\in U}\norm{(D^kf)_x}$. $f_k \to f$ uniformly $C^r$ iff $\norm{f_k - f}_r \to 0$, i.e. $D^jf_k \to D^jf$ uniformly for all $j \le r$.", item="def-cr-norm")
c("c1-limit", r"If $f_k \to f$ pointwise and $Df_k \to G$ uniformly ($f_k$ of class $C^1$), what follows, and why?",
  r"$f$ is $C^1$ with $Df = G$. Pass to the limit in $f_k(p+v) - f_k(p) = \big(\int_0^1 (Df_k)_{p+tv}\,dt\big)v$ and use continuity of $G$.", item="lem-c1-limit")
c("cr-complete", r"State the completeness theorem for $C^r$.",
  r"$C^r(U,\R^m)$ with $\norm{\cdot}_r$ is a complete normed space (a Banach space): uniformly $C^r$ Cauchy sequences converge uniformly $C^r$.", item="thm-cr-complete")
c("cr-mtest", r"State the $C^r$ M-test.",
  r"If $\norm{f_k}_r \le M_k$ and $\sum M_k < \infty$, then $\sum f_k$ converges uniformly $C^r$ to a $C^r$ function, and $D^j\sum f_k = \sum D^jf_k$ for $j \le r$.", item="thm-cr-m-test")
S.write()
