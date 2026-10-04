from c5lib import Section
S = Section("5-implicit-inverse")
b, c = S.b, S.c

b("ii-intro", "prose", r"""
An equation $f(x,y) = z_0$ in the unknown $y$ may or may not determine $y$ as a function of $x$. For a linear
equation $Ax + By = z_0$ the answer is plain: it does exactly when $B$ is invertible, and then
$y = B^{-1}(z_0 - Ax)$. The implicit function theorem says that a $C^r$ equation behaves, near a solution, like its
linear approximation there: if the derivative with respect to $y$ is invertible at one solution, the nearby
solutions form the graph of a $C^r$ function $y = g(x)$. The proof turns the equation into a fixed point problem
and solves it with the Banach contraction principle of Chapter 4. The inverse function theorem is then a short
corollary.
""")

b("def-partial-maps", "definition", r"""
Points of $\R^n \times \R^m = \R^{n+m}$ are written $(x,y)$, with the Euclidean norm
$\abs{(x,y)} = \sqrt{\abs{x}^2 + \abs{y}^2}$; note $\abs{(x,y)} \le \abs{x} + \abs{y}$. Let $U \subseteq \R^n \times \R^m$
be open and let $f : U \to \R^m$ be differentiable at $(x,y)$. The \emph{partial derivatives of $f$ with respect to
$x$ and to $y$} are the linear maps
\[ \frac{\partial f}{\partial x}(x,y) = (Df)_{(x,y)} \circ \iota_1 : \R^n \to \R^m, \qquad
\frac{\partial f}{\partial y}(x,y) = (Df)_{(x,y)} \circ \iota_2 : \R^m \to \R^m , \]
where $\iota_1(u) = (u, 0)$ and $\iota_2(w) = (0,w)$. Thus
\[ (Df)_{(x,y)}(u,w) = \frac{\partial f}{\partial x}(x,y)\,u + \frac{\partial f}{\partial y}(x,y)\,w . \]
In matrix terms, $\frac{\partial f}{\partial x}$ consists of the first $n$ columns of the Jacobian matrix and
$\frac{\partial f}{\partial y}$ of the last $m$ columns. Since $\abs{\iota_1 u} = \abs{u}$ and
$\abs{\iota_2 w} = \abs{w}$, both $\iota_1$ and $\iota_2$ have operator norm $1$.
""", title="Partial derivatives with respect to a block of variables")

b("def-ift-setup", "definition", r"""
The following standing assumptions are called the \emph{implicit function setup}. $U \subseteq \R^n \times \R^m$ is
an open set containing $(0,0)$; $f : U \to \R^m$ is of class $C^1$ with $f(0,0) = 0$; we write
\[ A = \frac{\partial f}{\partial x}(0,0), \qquad B = \frac{\partial f}{\partial y}(0,0), \]
and assume that $B : \R^m \to \R^m$ is invertible. The \emph{remainder} is
\[ R(x,y) = f(x,y) - Ax - By, \qquad (x,y) \in U . \]
Since $B$ is invertible, the equation $f(x,y) = 0$ is equivalent to the fixed point equation
\[ y = K_x(y), \qquad K_x(y) = -B^{-1}\big( Ax + R(x,y) \big) . \]
""", title="The implicit function setup")

b("lem-ift-remainder", "lemma", r"""
In the implicit function setup, there is a $\rho > 0$ such that the set
$N = \set{(x,y) : \abs{x} \le \rho,\ \abs{y} \le \rho}$ is contained in $U$ and:
\begin{enumerate}
\item for all $(x_1,y_1), (x_2,y_2) \in N$,
\[ \abs{R(x_1,y_1) - R(x_2,y_2)} \le \frac{1}{2\norm{B^{-1}}}\,\abs{(x_1 - x_2,\ y_1 - y_2)} ; \]
\item $\frac{\partial f}{\partial y}(x,y)$ is invertible for every $(x,y) \in N$.
\end{enumerate}
""", title="The remainder is a gentle Lipschitz map", proof=r"""
Let $L(x,y) = Ax + By$. This is the linear map $(Df)_{(0,0)}$, and $R = f - L$ on $U$. Since a linear map is its
own derivative, $R$ is differentiable on $U$ with $(DR)_z = (Df)_z - L$. As $f$ is $C^1$, $z \mapsto (DR)_z$ is
continuous, and $(DR)_{(0,0)} = 0$.

Put $c = 1/(2\norm{B^{-1}})$. Because $U$ is open and $DR$ is continuous at the origin, there is a $\delta > 0$ such
that every $z$ with $\abs{z} < \delta$ lies in $U$ and satisfies $\norm{(DR)_z} \le c$. Let $\rho = \delta/2$. If
$(x,y) \in N$ then $\abs{(x,y)} \le \sqrt{2}\,\rho < \delta$, so $N \subseteq U$ and $\norm{(DR)_z} \le c$ on $N$.

(1) $N$ is convex: if $(x_1,y_1), (x_2,y_2) \in N$ and $0 \le t \le 1$ then
$\abs{(1-t)x_1 + tx_2} \le (1-t)\rho + t\rho = \rho$ and likewise for $y$. So the segment between two points of
$N$ lies in $N$, where $\norm{DR} \le c$, and the mean value inequality gives (1).

(2) For $z \in N$,
\[ \frac{\partial f}{\partial y}(z) = (Df)_z \circ \iota_2 = L \circ \iota_2 + (DR)_z \circ \iota_2 = B + (DR)_z \circ \iota_2 , \]
and $\norm{(DR)_z \circ \iota_2} \le \norm{(DR)_z}\,\norm{\iota_2} \le c < 1/\norm{B^{-1}}$. An operator this close to
the invertible operator $B$ is invertible.
""", d=3, m=30, hints=[
r"$R$ is $C^1$ and its derivative vanishes at the origin, so $\norm{DR}$ is small near the origin.",
r"Choose a box on which $\norm{DR} \le 1/(2\norm{B^{-1}})$ and use the mean value inequality on it; for (2), $\partial f/\partial y = B + (DR)\circ\iota_2$ is a small perturbation of $B$.",
], uses=["def-ift-setup", "def-partial-maps", "thm-linear-rules", "thm-mvt", "thm-inverse-open", "prop-opnorm-is-norm"])

b("lem-ift-existence", "lemma", r"""
In the implicit function setup, let $\rho > 0$ be such that $N = \set{(x,y) : \abs{x} \le \rho, \abs{y} \le \rho}$
lies in $U$ and
$\abs{R(x_1,y_1) - R(x_2,y_2)} \le \frac{1}{2\norm{B^{-1}}}\abs{(x_1 - x_2, y_1 - y_2)}$ on $N$. Put
\[ \Lambda = 2\norm{B^{-1}}\,\norm{A} + 1, \qquad \tau = \rho/\Lambda . \]
Then:
\begin{enumerate}
\item for every $x \in \R^n$ with $\abs{x} \le \tau$ there is exactly one $y \in \R^m$ with $\abs{y} \le \rho$ and
$f(x,y) = 0$; call it $g(x)$;
\item $g(0) = 0$, and $\abs{g(x_1) - g(x_2)} \le \Lambda\,\abs{x_1 - x_2}$ whenever $\abs{x_1}, \abs{x_2} \le \tau$.
\end{enumerate}
""", title="Existence and uniqueness of the implicit function", proof=r"""
Note $\Lambda \ge 1$, so $\tau \le \rho$, and $R(0,0) = f(0,0) = 0$. Let $Y = \set{y \in \R^m : \abs{y} \le \rho}$.
It is a nonempty closed subset of the complete space $\R^m$, hence a complete metric space.

Fix $x$ with $\abs{x} \le \tau$. For $y \in Y$ the point $(x,y)$ lies in $N$, so
$K_x(y) = -B^{-1}(Ax + R(x,y))$ is defined, and, since $B$ is invertible,
\[ y = K_x(y) \iff By = -Ax - R(x,y) \iff f(x,y) = 0 . \]
So (1) says that $K_x$ has exactly one fixed point in $Y$.

\emph{$K_x$ contracts.} For $y_1, y_2 \in Y$,
\[ \abs{K_x(y_1) - K_x(y_2)} = \abs{B^{-1}\big( R(x,y_1) - R(x,y_2) \big)}
\le \norm{B^{-1}} \cdot \frac{1}{2\norm{B^{-1}}}\abs{(0, y_1 - y_2)} = \tfrac12 \abs{y_1 - y_2} . \]

\emph{$K_x$ maps $Y$ into $Y$.} First,
$\abs{R(x,0)} = \abs{R(x,0) - R(0,0)} \le \frac{1}{2\norm{B^{-1}}}\abs{x}$, so
\[ \abs{K_x(0)} \le \norm{B^{-1}}\big( \norm{A}\abs{x} + \abs{R(x,0)} \big) \le \big( \norm{B^{-1}}\norm{A} + \tfrac12 \big)\abs{x}
= \tfrac{\Lambda}{2}\abs{x} \le \tfrac{\Lambda}{2}\tau = \tfrac{\rho}{2} . \]
Hence for $y \in Y$, $\abs{K_x(y)} \le \abs{K_x(y) - K_x(0)} + \abs{K_x(0)} \le \frac12\abs{y} + \frac{\rho}{2} \le \rho$.

By the Banach contraction principle, $K_x : Y \to Y$ has a unique fixed point $g(x)$. This proves (1).

(2) Since $f(0,0) = 0$ and $\abs{0} \le \rho$, uniqueness gives $g(0) = 0$. Let $\abs{x_1}, \abs{x_2} \le \tau$ and
write $y_i = g(x_i) = K_{x_i}(y_i)$. Then
\begin{align*}
\abs{y_1 - y_2} &= \abs{ B^{-1}\big( A(x_1 - x_2) + R(x_1,y_1) - R(x_2,y_2) \big) } \\
&\le \norm{B^{-1}}\norm{A}\abs{x_1 - x_2} + \tfrac12 \abs{(x_1 - x_2, y_1 - y_2)} \\
&\le \big( \norm{B^{-1}}\norm{A} + \tfrac12 \big)\abs{x_1 - x_2} + \tfrac12\abs{y_1 - y_2} .
\end{align*}
Subtracting $\frac12\abs{y_1 - y_2}$ and doubling, $\abs{y_1 - y_2} \le \Lambda\abs{x_1 - x_2}$.
""", d=4, m=60, hints=[
r"Solutions of $f(x,y) = 0$ are fixed points of $K_x(y) = -B^{-1}(Ax + R(x,y))$. Apply the contraction principle on the closed ball $\abs{y} \le \rho$.",
r"The Lipschitz bound on $R$ makes $K_x$ a contraction with constant $\frac12$. The work is to check that $K_x$ maps the ball into itself: bound $\abs{K_x(0)}$ by $\rho/2$ when $\abs{x} \le \tau$.",
r"For the Lipschitz estimate on $g$, subtract the fixed point equations for $x_1$ and $x_2$ and absorb the $\frac12\abs{y_1-y_2}$ term on the left.",
], uses=["def-ift-setup", "prop-opnorm-bound"])

b("lem-ift-differentiable", "lemma", r"""
In the implicit function setup, let $\rho, \tau, \Lambda > 0$ and
$g : \set{x : \abs{x} \le \tau} \to \set{y : \abs{y} \le \rho}$ be such that
$N = \set{(x,y) : \abs{x} \le \rho, \abs{y} \le \rho} \subseteq U$, $\tau \le \rho$, $\frac{\partial f}{\partial y}$ is
invertible at every point of $N$, $f(x,g(x)) = 0$ for all $\abs{x} \le \tau$, and
$\abs{g(x_1) - g(x_2)} \le \Lambda\abs{x_1 - x_2}$ whenever $\abs{x_1}, \abs{x_2} \le \tau$. Then $g$ is of class $C^1$ on the open ball
$\set{x : \abs{x} < \tau}$, and
\[ (Dg)_x = -\Big( \frac{\partial f}{\partial y}(x, g(x)) \Big)^{-1} \circ \frac{\partial f}{\partial x}(x,g(x)) . \]
""", title="The implicit function is $C^1$", proof=r"""
Fix $x$ with $\abs{x} < \tau$ and put $y = g(x)$, so $(x,y) \in N \subseteq U$. Let
$A' = \frac{\partial f}{\partial x}(x,y)$ and $B' = \frac{\partial f}{\partial y}(x,y)$; $B'$ is invertible.
Differentiability of $f$ at $(x,y)$ says
\[ f(x+h, y+k) = f(x,y) + A'h + B'k + Q(h,k), \qquad \frac{\abs{Q(h,k)}}{\abs{(h,k)}} \to 0 \text{ as } (h,k) \to 0 . \]
For $h \ne 0$ with $\abs{x + h} < \tau$ set $k = k(h) = g(x+h) - g(x)$. Then $\abs{k} \le \Lambda\abs{h}$, and both
$f(x+h,y+k) = f(x+h, g(x+h))$ and $f(x,y)$ are $0$. Hence $0 = A'h + B'k + Q(h,k)$, that is,
\[ g(x+h) - g(x) = k = -B'^{-1}A'h - B'^{-1}Q(h,k) . \]
The map $-B'^{-1}A'$ is linear. To see that the last term is sublinear in $h$, let $\eps > 0$ and choose
$\delta_1 > 0$ with $\abs{Q(z)} \le \eps\abs{z}$ whenever $\abs{z} < \delta_1$. Since
$\abs{(h,k)} \le \abs{h} + \abs{k} \le (1 + \Lambda)\abs{h}$, for $0 < \abs{h} < \delta_1/(1+\Lambda)$ we get
\[ \frac{\abs{B'^{-1}Q(h,k)}}{\abs{h}} \le \norm{B'^{-1}}\,\eps\,(1+\Lambda) . \]
As $\eps$ is arbitrary, the quotient tends to $0$ with $h$. So $g$ is differentiable at $x$ with
$(Dg)_x = -B'^{-1}A'$, which is the stated formula.

\emph{Continuity of $Dg$.} The map $x \mapsto (x, g(x))$ is continuous because $g$ is Lipschitz. The maps
$z \mapsto \frac{\partial f}{\partial x}(z) = (Df)_z \circ \iota_1$ and
$z \mapsto \frac{\partial f}{\partial y}(z) = (Df)_z \circ \iota_2$ are continuous for the operator norm, because
$\norm{(Df)_z \circ \iota - (Df)_{z'} \circ \iota} \le \norm{(Df)_z - (Df)_{z'}}$ when $\norm{\iota} = 1$, and $f$ is
$C^1$. Inversion is continuous on the invertible operators. Finally composition of operators is continuous:
$\norm{ST - S_0T_0} \le \norm{S}\norm{T - T_0} + \norm{S - S_0}\norm{T_0}$. So
$x \mapsto (Dg)_x$ is a composite of continuous maps, and $g$ is $C^1$.
""", d=3, m=45, hints=[
r"Differentiate the identity $f(x, g(x)) = 0$ by hand: expand $f(x+h, g(x+h))$ to first order at $(x, g(x))$.",
r"With $k = g(x+h) - g(x)$ you get $0 = A'h + B'k + Q(h,k)$; solve for $k$. The Lipschitz bound $\abs{k} \le \Lambda\abs{h}$ makes $Q(h,k)$ sublinear in $h$.",
], uses=["def-ift-setup", "def-partial-maps", "def-derivative", "cor-gl-open", "prop-opnorm-is-norm", "def-c1"])

b("lem-ift-cr", "lemma", r"""
In the situation of the previous lemma, suppose in addition that $f$ is of class $C^r$ for some $r \ge 1$. Then
$g$ is of class $C^r$ on the open ball $\set{x : \abs{x} < \tau}$.
""", title="The implicit function is as smooth as the equation", proof=r"""
Let $\Omega = \set{x : \abs{x} < \tau}$. We show by induction on $k$ that $g$ is $C^k$ on $\Omega$ for
$1 \le k \le r$. The case $k = 1$ is the previous lemma. Suppose $g$ is $C^k$ with $1 \le k < r$.

The map $P : \Omega \to U$, $P(x) = (x, g(x))$, is $C^k$, because its components are coordinate functions
(linear, hence $C^k$) and components of $g$. The first partial derivatives of the components of $f$ are $C^{r-1}$
functions on $U$, hence $C^k$ since $k \le r - 1$. These are the matrix entries of
$\frac{\partial f}{\partial x}$ and $\frac{\partial f}{\partial y}$. Composing with $P$, the matrix entries of
\[ a(x) = \frac{\partial f}{\partial x}(x, g(x)), \qquad b(x) = \frac{\partial f}{\partial y}(x,g(x)) \]
are $C^k$ functions on $\Omega$, since composites of $C^k$ maps are $C^k$. Each $b(x)$ is invertible, so $b$ is a
$C^k$ map from $\Omega$ into the open set of invertible $m \times m$ matrices; as matrix inversion is $C^\infty$,
the entries of $b(x)^{-1}$ are $C^k$ functions of $x$. By the formula $(Dg)_x = -b(x)^{-1}a(x)$, each matrix entry
of $(Dg)_x$ is a sum of products of entries of $b(x)^{-1}$ and $a(x)$, multiplied by $-1$, hence $C^k$. So the
first partial derivatives of $g$ are $C^k$, the operator-valued map $Dg$ is $C^k$, and therefore $g$ is $C^{k+1}$.
""", d=3, m=30, hints=[
r"Bootstrap from the formula $(Dg)_x = -(\partial f/\partial y)^{-1}\circ(\partial f/\partial x)$ at $(x, g(x))$.",
r"If $g$ is $C^k$ with $k < r$, the right side of the formula is built from $C^k$ pieces by composition, matrix inversion and products; so $Dg$ is $C^k$ and $g$ is $C^{k+1}$.",
], uses=["lem-ift-differentiable", "thm-cr-algebra", "cor-inversion-smooth", "lem-cr-linear", "prop-peel", "thm-cr-partials"])

b("thm-implicit", "theorem", r"""
Let $U \subseteq \R^n \times \R^m$ be open and $f : U \to \R^m$ of class $C^r$, $r \ge 1$. Let $(x_0,y_0) \in U$,
$z_0 = f(x_0,y_0)$, and suppose $\frac{\partial f}{\partial y}(x_0,y_0)$ is invertible. Then there are numbers
$\rho > 0$ and $\tau > 0$ such that $\set{(x,y) : \abs{x - x_0} \le \rho, \abs{y - y_0} \le \rho} \subseteq U$,
$\tau \le \rho$, and:
\begin{enumerate}
\item for every $x$ with $\abs{x - x_0} < \tau$ there is exactly one $y$ with $\abs{y - y_0} \le \rho$ and
$f(x,y) = z_0$; call it $g(x)$;
\item $g(x_0) = y_0$ and $g$ is of class $C^r$ on $\set{x : \abs{x - x_0} < \tau}$;
\item $(Dg)_x = -\big( \frac{\partial f}{\partial y}(x,g(x)) \big)^{-1} \circ \frac{\partial f}{\partial x}(x,g(x))$.
\end{enumerate}
In words: near $(x_0,y_0)$, the set where $f = z_0$ is the graph of a $C^r$ function $y = g(x)$.
""", title="Implicit function theorem", proof=r"""
\emph{Reduction to the setup.} Let $\tilde U = \set{(x,y) : (x_0 + x, y_0 + y) \in U}$, an open set containing
$(0,0)$, and $\tilde f(x,y) = f(x_0 + x, y_0 + y) - z_0$ on $\tilde U$. The translation
$(x,y) \mapsto (x_0 + x, y_0 + y)$ is a constant plus the identity, so it is $C^r$ with derivative the identity
everywhere; hence $\tilde f$ is $C^r$, being a composite of $C^r$ maps minus a constant, and by the chain rule
$(D\tilde f)_{(x,y)} = (Df)_{(x_0 + x, y_0 + y)}$. In particular the partial derivatives of $\tilde f$ at $(x,y)$
are those of $f$ at $(x_0 + x, y_0 + y)$, $\tilde f(0,0) = 0$, and
$\frac{\partial \tilde f}{\partial y}(0,0)$ is invertible. So $\tilde f$ satisfies the implicit function setup.

\emph{Applying the lemmas to $\tilde f$.} The lemma on the remainder gives $\rho > 0$ with
$N = \set{\abs{x} \le \rho, \abs{y} \le \rho} \subseteq \tilde U$, the Lipschitz estimate for the remainder on
$N$, and invertibility of $\frac{\partial \tilde f}{\partial y}$ on $N$. The existence lemma then gives
$\tau \le \rho$ and, for each $\abs{x} \le \tau$, a unique $\tilde g(x)$ with $\abs{\tilde g(x)} \le \rho$ and
$\tilde f(x, \tilde g(x)) = 0$; moreover $\tilde g(0) = 0$ and $\tilde g$ is Lipschitz. By the two lemmas on
smoothness, $\tilde g$ is $C^r$ on $\set{\abs{x} < \tau}$ with
$(D\tilde g)_x = -\big(\frac{\partial \tilde f}{\partial y}\big)^{-1} \circ \frac{\partial \tilde f}{\partial x}$ at
$(x, \tilde g(x))$.

\emph{Translating back.} Define $g(x) = y_0 + \tilde g(x - x_0)$ for $\abs{x - x_0} < \tau$. For such $x$ and any
$y$ with $\abs{y - y_0} \le \rho$, the point $(x,y)$ lies in $U$, and
$f(x,y) = z_0$ if and only if $\tilde f(x - x_0, y - y_0) = 0$, if and only if $y - y_0 = \tilde g(x - x_0)$, that
is, $y = g(x)$. This is (1). Also $g(x_0) = y_0 + \tilde g(0) = y_0$, and $g$ is $C^r$ as a composite of the $C^r$
map $\tilde g$ with a translation, plus a constant, with $(Dg)_x = (D\tilde g)_{x - x_0}$. Substituting the
formula for $D\tilde g$ and the relation between the partial derivatives of $\tilde f$ and $f$ gives (3).
""", d=3, m=30, hints=[
r"Translate so that $(x_0,y_0)$ becomes the origin and $z_0$ becomes $0$; then you are in the implicit function setup.",
r"Assemble the four lemmas for $\tilde f(x,y) = f(x_0+x, y_0+y) - z_0$, and translate the conclusion back.",
], uses=["lem-ift-remainder", "lem-ift-existence", "lem-ift-differentiable", "lem-ift-cr", "thm-chain-rule", "thm-cr-algebra", "lem-cr-linear"])

b("ex-circle", "example", r"""
Let $f(x,y) = x^2 + y^2$ on $\R \times \R$ and $z_0 = 1$, so the locus is the unit circle. At $(0,1)$ we have
$\frac{\partial f}{\partial y} = 2y = 2 \ne 0$, and indeed near $(0,1)$ the circle is the graph of
$g(x) = \sqrt{1 - x^2}$, with $g'(x) = -x/\sqrt{1-x^2} = -(2y)^{-1}(2x)$ at $y = g(x)$, as the theorem predicts. At
$(1,0)$ the partial derivative $\frac{\partial f}{\partial y}$ vanishes and the conclusion fails: for $x$ slightly
less than $1$ there are two nearby solutions $y = \pm\sqrt{1-x^2}$, and for $x > 1$ there are none. (There the
roles of $x$ and $y$ can be exchanged, since $\frac{\partial f}{\partial x}(1,0) = 2 \ne 0$.)
""", title="The circle")

b("def-diffeo", "definition", r"""
Let $U_0$, $V_0$ be open subsets of $\R^m$. A map $f : U_0 \to V_0$ is a \emph{$C^r$ diffeomorphism} ($r \ge 1$) if
it is a bijection and both $f$ and $f^{-1} : V_0 \to U_0$ are of class $C^r$.
""", title="Diffeomorphism")

b("prop-diffeo-derivative", "proposition", r"""
Let $U_0, V_0 \subseteq \R^m$ be open and $f : U_0 \to V_0$ a bijection. If $f$ is differentiable at $p$ and
$f^{-1}$ is differentiable at $f(p)$, then $(Df)_p$ is invertible and
\[ (D(f^{-1}))_{f(p)} = \big( (Df)_p \big)^{-1} . \]
""", title="A differentiable inverse forces an invertible derivative", proof=r"""
The composite $f^{-1} \circ f$ is the identity map of $U_0$, which is the restriction of a linear map and so has
derivative $I$ at $p$. By the chain rule,
\[ (D(f^{-1}))_{f(p)} \circ (Df)_p = I . \]
Thus the linear map $(Df)_p : \R^m \to \R^m$ has a left inverse, so it is injective, hence invertible, and its
inverse is $(D(f^{-1}))_{f(p)}$.
""", d=1, m=10, hints=[
r"Differentiate $f^{-1}\circ f = \id$ with the chain rule.",
], uses=["thm-chain-rule", "thm-linear-rules"])

b("ex-cube", "example", r"""
The hypothesis that the derivative be invertible cannot be dropped from the inverse function theorem below. The
map $f(x) = x^3$ is a $C^\infty$ bijection $\R \to \R$ with continuous inverse $x \mapsto x^{1/3}$, but
$f'(0) = 0$, so by the proposition the inverse cannot be differentiable at $0$; and indeed the difference quotient
$h^{1/3}/h = h^{-2/3}$ is unbounded as $h \to 0$.
""", title="A smooth homeomorphism that is not a diffeomorphism")

b("thm-inverse", "theorem", r"""
Let $U \subseteq \R^m$ be open, $f : U \to \R^m$ of class $C^r$, $r \ge 1$, and $p \in U$. If $(Df)_p$ is
invertible, then there are open sets $U_0 \subseteq U$ containing $p$ and $V_0 \subseteq \R^m$ containing $f(p)$
such that $f$ restricts to a $C^r$ diffeomorphism $U_0 \to V_0$. Moreover
$(D(f^{-1}))_{f(y)} = \big( (Df)_y \big)^{-1}$ for $y \in U_0$.
""", title="Inverse function theorem", proof=r"""
Let $q = f(p)$. Define $F : \R^m \times U \to \R^m$ by $F(x,y) = f(y) - x$. The set $\R^m \times U$ is open in
$\R^m \times \R^m$. The projections $(x,y) \mapsto x$ and $(x,y) \mapsto y$ are linear, hence $C^r$, so $F$ is
$C^r$ as a composite of $C^r$ maps minus a $C^r$ map, and by the chain rule
$(DF)_{(x,y)}(u,w) = (Df)_y w - u$. Thus $\frac{\partial F}{\partial y}(x,y) = (Df)_y$ and
$\frac{\partial F}{\partial x}(x,y) = -I$. We have $F(q,p) = 0$ and $\frac{\partial F}{\partial y}(q,p) = (Df)_p$ is
invertible.

By the implicit function theorem applied to $F$ at $(q,p)$ with $z_0 = 0$, there are $\rho, \tau > 0$ and a $C^r$
map $g : \set{x : \abs{x - q} < \tau} \to \R^m$ with $g(q) = p$ such that, for every $x$ with $\abs{x - q} < \tau$:
$\abs{g(x) - p} \le \rho$, $g(x) \in U$, $f(g(x)) = x$, and
\[ \text{if } y \in U,\ \abs{y - p} \le \rho \text{ and } f(y) = x, \text{ then } y = g(x) . \tag{$*$} \]
Define
\[ V_0 = \set{x : \abs{x - q} < \tau,\ \abs{g(x) - p} < \rho}, \qquad
U_0 = \set{y \in U : \abs{y - p} < \rho,\ f(y) \in V_0} . \]
$V_0$ is open because $g$ is continuous, and $q \in V_0$ because $g(q) = p$. $U_0$ is open because $U$ and $V_0$
are open and $f$ is continuous, and $p \in U_0$ because $f(p) = q \in V_0$.

By definition $f(U_0) \subseteq V_0$. If $y \in U_0$ then $x = f(y)$ satisfies $\abs{x - q} < \tau$ and
$\abs{y - p} < \rho$, so $y = g(f(y))$ by $(*)$; hence $f$ is injective on $U_0$. If $x \in V_0$ then $y = g(x)$
lies in $U$, satisfies $\abs{y - p} < \rho$ and $f(y) = x \in V_0$, so $y \in U_0$; hence $f(U_0) = V_0$, and the
inverse of $f : U_0 \to V_0$ is the restriction of $g$ to $V_0$, which is $C^r$. So $f : U_0 \to V_0$ is a $C^r$
diffeomorphism. The formula for the derivative of the inverse follows from the proposition on differentiable
inverses.
""", d=4, m=60, hints=[
r"Solving $f(y) = x$ for $y$ is an implicit function problem: consider $F(x,y) = f(y) - x$.",
r"The implicit function theorem gives a $C^r$ map $g$ near $q = f(p)$ with $f(g(x)) = x$, unique among $y$ with $\abs{y-p} \le \rho$. It remains to choose open sets on which $f$ and $g$ are mutually inverse.",
r"Take $V_0 = \set{x : \abs{x-q} < \tau, \abs{g(x)-p} < \rho}$ and $U_0 = \set{y : \abs{y-p} < \rho, f(y) \in V_0}$, and use the uniqueness clause.",
], uses=["thm-implicit", "def-diffeo", "prop-diffeo-derivative", "thm-cr-algebra", "lem-cr-linear", "thm-chain-rule"])

b("cor-open-mapping", "corollary", r"""
Let $U \subseteq \R^m$ be open and $f : U \to \R^m$ of class $C^1$ with $(Df)_x$ invertible for every $x \in U$.
Then $f$ is an open map: $f(U')$ is open in $\R^m$ for every open $U' \subseteq U$.
""", title="Maps with invertible derivative are open", proof=r"""
Let $U' \subseteq U$ be open and $y \in f(U')$, say $y = f(x)$ with $x \in U'$. The restriction of $f$ to the
open set $U'$ is $C^1$ with invertible derivative at $x$, so by the inverse function theorem there are open sets
$U_0 \subseteq U'$ containing $x$ and $V_0$ containing $y$ with $f(U_0) = V_0$. Then
$V_0 \subseteq f(U')$ is an open set containing $y$. So every point of $f(U')$ is interior, and $f(U')$ is open.
""", d=2, m=15, hints=[
r"Apply the inverse function theorem to the restriction of $f$ to $U'$ at each point.",
], uses=["thm-inverse"])

b("ex-local-not-global", "example", r"""
The inverse function theorem is local, and cannot be improved to a global statement in dimension $m \ge 2$. Let
$f : \R^2 \to \R^2$, $f(x,y) = (e^x \cos y, e^x \sin y)$. Its Jacobian determinant is
$e^{2x}(\cos^2 y + \sin^2 y) = e^{2x} \ne 0$, so $(Df)_{(x,y)}$ is invertible at every point and $f$ is a
diffeomorphism near each point. But $f(x, y + 2\pi) = f(x,y)$, so $f$ is not injective. (In dimension one, by
contrast, a function on an interval with nowhere vanishing derivative is strictly monotone, hence injective.)
""", title="Locally invertible everywhere, but not invertible")

b("thm-rank", "theorem", r"""
The \emph{rank} of a linear map is the dimension of its image. Let $U \subseteq \R^n$ be open and let
$f : U \to \R^m$ be of class $C^r$, $r \ge 1$, such that $(Df)_x$ has the same rank $k$ at every $x \in U$. Then for
each $p \in U$ there are open sets $U_0 \subseteq U$ containing $p$ and $V_0 \subseteq \R^m$ containing $f(U_0)$,
and $C^r$ diffeomorphisms $\varphi$ of $U_0$ onto an open subset of $\R^n$ and $\psi$ of $V_0$ onto an open subset
of $\R^m$, such that
\[ \psi \circ f \circ \varphi^{-1}(x_1, \dots, x_n) = (x_1, \dots, x_k, 0, \dots, 0) . \]
That is, in suitable $C^r$ coordinates a map of constant rank $k$ is a linear projection followed by a linear
inclusion.
""", title="Rank theorem")

b("rem-rank", "remark", r"""
The rank theorem is stated here without proof. Its proof is a longer application of the inverse function
theorem: one first straightens the domain so that $f$ takes the form $(x_1, \dots, x_k, \text{something})$, then
uses constancy of the rank to show that the remaining components depend only on $x_1, \dots, x_k$, and
straightens the target. The inverse function theorem is the case $k = n = m$, and the implicit function theorem
is contained in the case $k = m$.
""")

c("ift", "State the implicit function theorem.",
  r"If $f : U \to \R^m$ is $C^r$ on an open $U \subseteq \R^n\times\R^m$, $f(x_0,y_0) = z_0$ and $\partial f/\partial y(x_0,y_0)$ is invertible, then near $(x_0,y_0)$ the set $f = z_0$ is the graph of a unique function $y = g(x)$, and $g$ is $C^r$.", item="thm-implicit")
c("ift-derivative", "What is the derivative of the implicit function?",
  r"$(Dg)_x = -(\partial f/\partial y)^{-1}\circ(\partial f/\partial x)$ at $(x,g(x))$: differentiate $f(x,g(x)) = z_0$.", item="lem-ift-differentiable")
c("ift-idea", "What is the fixed point problem in the proof of the implicit function theorem?",
  r"With $f(x,y) = Ax + By + R(x,y)$ near the origin: $f(x,y) = 0$ iff $y = K_x(y) = -B^{-1}(Ax + R(x,y))$. Since $DR$ is small near the origin, $K_x$ is a contraction of a small closed ball for small $x$.", item="lem-ift-existence")
c("ift-smooth", r"How does one pass from $g \in C^1$ to $g \in C^r$?",
  r"Bootstrap on the formula $Dg = -(\partial_yf)^{-1}\partial_xf$ at $(x,g(x))$: if $g$ is $C^k$, $k<r$, the right side is $C^k$ (composition, smooth matrix inversion, products), so $g$ is $C^{k+1}$.", item="lem-ift-cr")
c("inverse", "State the inverse function theorem.",
  r"If $f : U \to \R^m$ is $C^r$ ($r\ge1$, $U \subseteq \R^m$ open) and $(Df)_p$ is invertible, then $f$ is a $C^r$ diffeomorphism of a neighbourhood of $p$ onto a neighbourhood of $f(p)$, and $D(f^{-1})_{f(y)} = ((Df)_y)^{-1}$.", item="thm-inverse")
c("inverse-idea", "How does the inverse function theorem follow from the implicit function theorem?",
  r"Apply the implicit function theorem to $F(x,y) = f(y) - x$, whose $y$-derivative is $(Df)_y$: the implicit function $g$ satisfies $f(g(x)) = x$.", item="thm-inverse")
c("cube", "Why is invertibility of the derivative necessary for a differentiable inverse? Give the standard example.",
  r"Chain rule: $D(f^{-1})_{f(p)}\circ(Df)_p = I$. Example: $x \mapsto x^3$ is a smooth homeomorphism of $\R$ whose inverse is not differentiable at $0$.", item="ex-cube")
c("local-global", "Give a map with invertible derivative everywhere that is not injective.",
  r"$(x,y) \mapsto (e^x\cos y, e^x\sin y)$: Jacobian determinant $e^{2x} \ne 0$, but periodic in $y$.", item="ex-local-not-global")
c("rank", "State the rank theorem.",
  r"A $C^r$ map whose derivative has constant rank $k$ is, in suitable local $C^r$ coordinates on domain and target, $(x_1,\dots,x_n) \mapsto (x_1,\dots,x_k,0,\dots,0)$.", item="thm-rank")
S.write()
