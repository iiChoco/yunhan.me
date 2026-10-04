from common import Section

s = Section('6a')

s.p(
    'intro-inner-products',
    'Adding geometry to vector spaces',
    r'''Vector-space operations describe combinations of vectors but do not by themselves assign lengths or orthogonality. An inner product supplies this additional structure, beginning with the familiar coordinate dot product.''',
    182
)

s.d(
    'def-dot-product',
    'Real coordinate dot product',
    r'''For $x,y\in\R^n$, define
\[
x\cdot y=\sum_{j=1}^{n}x_jy_j.
\]
The output is a real scalar. For $n=0$, the sum is empty and equals zero.''',
    '6.1', 182
)

s.r(
    'thm-dot-product-properties',
    'Positivity, linearity, and symmetry of the dot product',
    r'''The real dot product satisfies
\[
x\cdot x\ge0,\qquad
x\cdot x=0\Longleftrightarrow x=0,\qquad
x\cdot y=y\cdot x.
\]
For each fixed $y$, the function $x\mapsto x\cdot y$ is linear.''',
    r'''The expression $x\cdot x=\sum_jx_j^2$ is a sum of nonnegative real numbers. If that sum is zero, none of its terms can be positive, so every $x_j^2=0$ and hence every $x_j=0$. Conversely, the zero vector gives a sum of zero terms. If $n=0$, there is only the zero vector and the same assertion holds.

Scalar commutativity gives $x_jy_j=y_jx_j$ for every index, so summing proves symmetry. For $x,u,y\in\R^n$ and $a\in\R$, distributivity gives
\[
(x+u)\cdot y
=\sum_j(x_j+u_j)y_j=x\cdot y+u\cdot y,
\qquad
(ax)\cdot y=\sum_jax_jy_j=a(x\cdot y).
\]
These are precisely additivity and homogeneity for the function with fixed second input.''',
    1, 10,
    [r'Use real scalar arithmetic in each coordinate.'],
    ['def-dot-product', 'c1-foundations',
     'c1-def-coordinate-addition', 'c1-def-coordinate-scaling',
     'c3-def-linear-map'],
    page=182
)

s.d(
    'def-inner-product',
    'Inner product',
    r'''An \emph{inner product} on a vector space $V$ over $\F$ assigns a scalar $\ip{u}{v}\in\F$ to each ordered pair of vectors, with the following properties:
\begin{enumerate}
\item $\ip{v}{v}$ is real and nonnegative for every $v$.
\item $\ip{v}{v}=0$ if and only if $v=0$.
\item $\ip{u+v}{w}=\ip{u}{w}+\ip{v}{w}$.
\item $\ip{au}{v}=a\ip{u}{v}$ for every $a\in\F$.
\item $\ip{u}{v}=\overline{\ip{v}{u}}$.
\end{enumerate}
Our convention is linearity in the first variable. Over $\R$, conjugation fixes every scalar, so the last property is ordinary symmetry.''',
    '6.2', 183
)

s.r(
    'thm-standard-inner-product',
    'The Euclidean inner product',
    r'''The formula
\[
\ip{u}{v}=\sum_{j=1}^{n}u_j\overline{v_j}
\]
defines an inner product on $\F^n$, called its \emph{Euclidean inner product}. It also defines an inner product when $n=0$.''',
    r'''For $u\in\F^n$,
\[
\ip{u}{u}=\sum_ju_j\overline{u_j}=\sum_j|u_j|^2,
\]
which is real and nonnegative. The sum vanishes exactly when every nonnegative term vanishes. The scalar modulus is zero exactly at zero, so this is equivalent to every coordinate of $u$ being zero. The zero vector conversely gives zero.

For $u,v,w\in\F^n$ and $a\in\F$,
\[
\ip{u+v}{w}
=\sum_j(u_j+v_j)\overline{w_j}
=\ip{u}{w}+\ip{v}{w},
\]
and
$\ip{au}{v}=\sum_jau_j\overline{v_j}=a\ip{u}{v}$.
Finally, the conjugation rules give
\[
\overline{\ip{v}{u}}
=\overline{\sum_jv_j\overline{u_j}}
=\sum_j\overline{v_j}u_j
=\ip{u}{v}.
\]
These are all the inner-product axioms. For $n=0$, every sum is zero and the coordinate space has only its zero vector, so all the axioms remain valid.''',
    2, 20,
    [r'Use $z\overline z=|z|^2$ for positivity and the conjugation rules for symmetry.'],
    ['def-inner-product', 'c4-thm-complex-properties',
     'c1-def-coordinate-addition', 'c1-def-coordinate-scaling',
     'c1-def-coordinate-space'],
    number='6.3(a)', page=184, kind='example'
)

s.r(
    'ex-weighted-inner-product',
    'Positive coordinate weights',
    r'''For positive real numbers $c_1,\ldots,c_n$, the formula
\[
\ip{u}{v}_c=\sum_{j=1}^{n}c_ju_j\overline{v_j}
\]
defines an inner product on $\F^n$.''',
    r'''Its value on $(u,u)$ is $\sum_jc_j|u_j|^2$, a sum of nonnegative real terms. If the sum is zero, each term is zero. Because $c_j>0$, this implies $|u_j|=0$ and hence $u_j=0$ for every index. Conversely, $u=0$ gives zero.

For fixed $w$, distributing in
$\sum_jc_j(u_j+v_j)\overline{w_j}$
proves additivity in the first variable, and factoring a scalar from
$\sum_jc_j(au_j)\overline{v_j}$
proves homogeneity there. Because every $c_j$ is real,
\[
\overline{\ip{v}{u}_c}
=\sum_jc_j\overline{v_j}u_j
=\ip{u}{v}_c.
\]
Thus conjugate symmetry holds as well, proving all the axioms. If $n=0$, the formula is the already verified zero-dimensional Euclidean inner product.''',
    2, 20,
    [
        r'Positivity of every weight is needed when recovering a coordinate from a zero squared value.'
    ],
    ['def-inner-product', 'thm-standard-inner-product',
     'c4-thm-complex-properties', 'c1-foundations'],
    number='6.3(b)', page=184, kind='example'
)

s.d(
    'def-integral-notation',
    'Integral notation for the function examples',
    r'''Write $C([a,b],\R)$ for the real-valued continuous functions on $[a,b]$, where $a<b$. The notation $\int_a^b h(x)\,dx$ denotes the Riemann integral: a real number $I$ such that, for every $\varepsilon>0$, sufficiently fine tagged partitions
\[
a=t_0<t_1<\cdots<t_m=b,\qquad
\xi_j\in[t_{j-1},t_j],
\]
satisfy
\[
\left|\sum_{j=1}^{m}h(\xi_j)(t_j-t_{j-1})-I\right|<\varepsilon.
\]
Here sufficiently fine means that $\max_j(t_j-t_{j-1})<\delta$ for some $\delta>0$ depending only on $\varepsilon$.

The improper integral $\int_0^\infty h(x)\,dx$ denotes the finite limit of $\int_0^b h(x)\,dx$ as $b\to\infty$, when it exists. A limit $L$ here means that for every $\varepsilon>0$ there is $M$ such that $b>M$ implies $\left|\int_0^b h-L\right|<\varepsilon$.''',
    page=184
)

s.add(
    'theorem',
    'thm-continuous-integral-facts',
    'Analysis facts used by the integral examples',
    r'''The following elementary analysis facts are available for the examples in this chapter.
\begin{enumerate}
\item Real polynomials are continuous, and products of continuous real functions are continuous.
\item Every continuous real function on a compact interval $[a,b]$ has a unique Riemann integral. Integration is linear:
\[
\int_a^b(\alpha f+\beta g)
=\alpha\int_a^b f+\beta\int_a^b g.
\]
If $h$ is continuous and nonnegative, its integral is nonnegative. If in addition $h(t)>0$ for at least one $t\in[a,b]$, then $\int_a^b h>0$.
\item For every integer $k\ge0$,
\[
\int_a^b x^k\,dx
=\frac{b^{k+1}-a^{k+1}}{k+1}.
\]
In particular, integration of polynomials on $[0,1]$ agrees with the earlier coefficient definition.
\item The real exponential function $x\mapsto e^x$ is continuous and strictly positive. For every real polynomial $r$, the improper integral
\[
\int_0^\infty |r(x)|e^{-x}\,dx
\]
is finite. The resulting integrals of $r(x)e^{-x}$ are linear in $r$.
\item If a continuous nonnegative function $h$ on $[0,\infty)$ has a finite improper integral, that integral is nonnegative. It is strictly positive if $h$ is positive at at least one point of $[0,\infty)$.
\end{enumerate}''',
    page=184
)

s.note(
    'remark-integral-facts-faith',
    'Analysis prerequisites taken on faith',
    r'''The preceding analysis theorem is taken on faith. It supplies the continuity, integration, and exponential-decay facts needed below; the verification of each inner product remains a proof task.''',
    184
)

s.r(
    'ex-continuous-integral-inner-product',
    'An inner product on continuous functions',
    r'''For real $a<b$, the set $C([a,b],\R)$ is a real vector space with pointwise operations, and
\[
\ip{f}{g}=\int_a^bf(x)g(x)\,dx
\]
defines an inner product on it. In particular this applies to $[-1,1]$.''',
    r'''The zero function is continuous, and sums and real scalar multiples of continuous functions are continuous by the earlier analysis closure theorem. Thus this set is a subspace of the vector space of all real-valued functions on $[a,b]$, and hence is a real vector space.

The product $fg$ is continuous, so the displayed integral exists and is real. Since $f^2\ge0$, positivity of integration gives $\ip{f}{f}\ge0$. If $f$ is not the zero function, there is a point $t\in[a,b]$ with $f(t)\ne0$. Then $f(t)^2>0$, so strict positivity of the integral of the continuous nonnegative function $f^2$ gives $\ip{f}{f}>0$. Conversely, the zero function gives zero integral.

Linearity of integration and pointwise multiplication give
\[
\ip{f+g}{h}=\int_a^b(fh+gh)=\ip{f}{h}+\ip{g}{h},
\qquad
\ip{af}{g}=\int_a^bafg=a\ip{f}{g}.
\]
Finally $fg=gf$ pointwise, so $\ip{f}{g}=\ip{g}{f}$. The scalar field is real, making this the required conjugate symmetry. All inner-product axioms are established.''',
    2, 20,
    [
        r'For definiteness, use a point where a nonzero function has a nonzero value.',
        r'Apply the strict positivity clause of the accepted integration theorem to its square.'
    ],
    ['def-inner-product', 'def-integral-notation',
     'thm-continuous-integral-facts', 'c1-thm-analysis-closure',
     'c1-def-function-space', 'c1-thm-function-space',
     'c1-thm-subspace-test'],
    number='6.3(c)', page=184, kind='example'
)

s.r(
    'thm-polynomial-integral-inner-product',
    'The unweighted polynomial integral inner product',
    r'''On $\Poly(\R)$ the formula
\[
\ip{p}{q}=\int_{-1}^{1}p(x)q(x)\,dx
\]
is an inner product. Restricting the same formula to any bounded-degree polynomial space $\Poly_m(\R)$ also gives an inner product.''',
    r'''Real polynomials restrict to continuous functions on $[-1,1]$. Thus the preceding continuous-function example supplies positivity, first-variable additivity and homogeneity, and symmetry for the displayed formula on polynomials.

For definiteness, suppose $\int_{-1}^{1}p(x)^2\,dx=0$. The continuous-function definiteness result implies that $p$ vanishes at every point of $[-1,1]$. This interval contains infinitely many distinct real numbers. A nonzero polynomial has only finitely many roots by the polynomial root bound, so $p$ must be the zero polynomial. Conversely, the zero polynomial has zero integral. Therefore the formula satisfies all the inner-product axioms on $\Poly(\R)$.

Every $\Poly_m(\R)$ is a vector subspace of $\Poly(\R)$. The same identities continue to hold for its elements, and a member with zero squared value is still the zero polynomial. Hence the restricted formula is an inner product there as well.''',
    2, 20,
    [
        r'First use the continuous-function example on the restrictions of the polynomials.',
        r'Explain why vanishing throughout an interval forces a polynomial to be the zero polynomial.'
    ],
    ['def-inner-product', 'ex-continuous-integral-inner-product',
     'thm-continuous-integral-facts', 'c4-thm-root-bound',
     'c2-thm-bounded-polynomials'],
    page=184
)

s.r(
    'ex-derivative-integral-inner-product',
    'An inner product combining a value and a derivative',
    r'''The formula
\[
\ip{p}{q}
=p(0)q(0)+\int_{-1}^{1}p'(x)q'(x)\,dx
\]
defines an inner product on $\Poly(\R)$.''',
    r'''Derivatives of real polynomials are polynomials, so the integral exists. At $q=p$, both terms
$p(0)^2$ and $\int_{-1}^{1}(p')^2$
are nonnegative. If their sum is zero, each term is zero. The polynomial integral inner-product result applied to $p'$ gives $p'=0$ as a polynomial.

Write $p(x)=\sum_{j=0}^{m}a_jx^j$. The coefficient formula
$p'(x)=\sum_{j=1}^{m}ja_jx^{j-1}$ and uniqueness of polynomial coefficients imply $ja_j=0$ for every $j\ge1$. Thus all these $a_j$ vanish, and $p$ is constant. The other zero term gives $p(0)^2=0$, so this constant is zero. Conversely, the zero polynomial makes both terms zero. This proves definiteness.

Evaluation at zero is linear, differentiation is linear, and integration is linear. Consequently, for polynomials $p,q,r$,
\[
\begin{aligned}
\ip{p+q}{r}
&=(p(0)+q(0))r(0)+\int_{-1}^{1}(p'+q')r'\\
&=\ip{p}{r}+\ip{q}{r},
\end{aligned}
\]
and, for real $a$,
\[
\ip{ap}{q}=ap(0)q(0)+\int_{-1}^{1}ap'q'=a\ip{p}{q}.
\]
Both products in the defining formula are symmetric in $p,q$, so $\ip{p}{q}=\ip{q}{p}$. These observations complete the axioms.''',
    3, 30,
    [
        r'If the squared value is zero, both nonnegative summands must vanish.',
        r'A polynomial with zero derivative is constant; the value at zero determines that constant.'
    ],
    ['def-inner-product', 'thm-polynomial-integral-inner-product',
     'thm-continuous-integral-facts', 'c3-ex-polynomial-differentiation',
     'c2-thm-polynomial-differentiation', 'c2-lem-polynomial-coefficients'],
    number='6.3(d)', page=184, kind='example'
)

s.r(
    'ex-exponential-polynomial-inner-product',
    'An inner product with exponential weight',
    r'''The formula
\[
\ip{p}{q}=\int_0^\infty p(x)q(x)e^{-x}\,dx
\]
defines an inner product on $\Poly(\R)$.''',
    r'''The product $pq$ is a polynomial. The accepted exponential-integrability statement therefore makes the displayed improper integral finite. For $p=q$, its integrand $p(x)^2e^{-x}$ is continuous and nonnegative, so the integral is nonnegative.

If $p$ is not the zero polynomial, the polynomial root bound ensures that it cannot vanish at every point of $[0,\infty)$, which contains infinitely many distinct points. Choose $t\ge0$ with $p(t)\ne0$. Strict positivity of the exponential gives $p(t)^2e^{-t}>0$. The strict positivity assertion for convergent improper integrals now gives $\ip{p}{p}>0$. The zero polynomial conversely gives zero integral, proving definiteness.

The accepted linearity for polynomial-times-exponential integrals yields
\[
\ip{p+q}{r}
=\int_0^\infty (pr+qr)e^{-x}
=\ip{p}{r}+\ip{q}{r},
\]
and $\ip{ap}{q}=a\ip{p}{q}$ for every real scalar $a$. Pointwise commutativity $pq=qp$ proves symmetry. Since the field is real, this is conjugate symmetry, and all axioms follow.''',
    2, 20,
    [
        r'Use the accepted convergence statement with the polynomial $pq$.',
        r'For definiteness, find a nonnegative point that is not a root of a nonzero polynomial.'
    ],
    ['def-inner-product', 'def-integral-notation',
     'thm-continuous-integral-facts', 'c4-lem-polynomial-product-degree',
     'c4-thm-root-bound'],
    number='6.3(e)', page=184, kind='example'
)

s.d(
    'def-inner-product-space',
    'Inner product spaces',
    r'''An \emph{inner product space} is a vector space together with a specified inner product. Unless another choice is stated, $\F^n$ as an inner product space uses the Euclidean inner product.''',
    '6.4', 184
)

s.r(
    'lem-inherited-inner-product',
    'Subspaces inherit inner products',
    r'''If $U$ is a vector subspace of an inner product space $V$, then restricting the inner product to pairs of vectors in $U$ makes $U$ an inner product space.''',
    r'''Because $U$ is a subspace, its vector operations and zero are those inherited from $V$. Positivity and definiteness hold on its vectors because they hold on all vectors of $V$. For vectors in $U$, sums and scalar multiples remain in $U$, and the first-variable additivity and homogeneity equations are the same equations already valid in $V$. Conjugate symmetry also remains valid for every pair in $U$. Thus the restricted function satisfies all inner-product axioms on the vector space $U$, with no finiteness assumption.''',
    1, 10,
    [r'Check which axioms change when the allowed vectors are restricted to a subspace.'],
    ['def-inner-product', 'def-inner-product-space', 'c1-def-subspace'],
    page=184, kind='lemma'
)

s.d(
    'convention-inner-product-spaces',
    'Standing inner product convention',
    r'''Throughout this chapter and the next, $V$ and $W$ denote inner product spaces over $\F$, where $\F$ is $\R$ or $\C$, unless a different setting is explicitly stated. They need not be finite-dimensional unless a result requires that hypothesis.''',
    '6.5', 185
)

s.r(
    'thm-inner-product-properties',
    'Zero values and conjugate linearity in the second variable',
    r'''In an inner product space:
\begin{enumerate}
\item For fixed $v$, the function $u\mapsto\ip{u}{v}$ is a linear functional.
\item $\ip{0}{v}=\ip{v}{0}=0$.
\item $\ip{u}{v+w}=\ip{u}{v}+\ip{u}{w}$.
\item $\ip{u}{av}=\overline a\,\ip{u}{v}$.
\end{enumerate}
In particular, $\ip{au}{bv}=a\overline b\,\ip{u}{v}$ for all scalars $a,b$.''',
    r'''First-variable additivity and homogeneity are axioms, and the output belongs to $\F$. Thus for fixed $v$ the stated function is a linear functional. It sends zero to zero, giving $\ip{0}{v}=0$. Conjugate symmetry then gives
$\ip{v}{0}=\overline{\ip{0}{v}}=\overline0=0$.

Using conjugate symmetry followed by first-variable additivity,
\[
\begin{aligned}
\ip{u}{v+w}
&=\overline{\ip{v+w}{u}}\\
&=\overline{\ip{v}{u}+\ip{w}{u}}\\
&=\overline{\ip{v}{u}}+\overline{\ip{w}{u}}\\
&=\ip{u}{v}+\ip{u}{w}.
\end{aligned}
\]
For a scalar $a$, first-variable homogeneity instead gives
\[
\ip{u}{av}
=\overline{\ip{av}{u}}
=\overline{a\ip{v}{u}}
=\overline a\,\overline{\ip{v}{u}}
=\overline a\,\ip{u}{v}.
\]
Applying first-variable homogeneity and then this last formula yields
$\ip{au}{bv}=a\ip{u}{bv}=a\overline b\,\ip{u}{v}$, proving the final identity.''',
    2, 20,
    [
        r'Use conjugate symmetry to move a calculation in the second variable into the first.',
        r'Conjugating a scalar factor changes it to its complex conjugate.'
    ],
    ['def-inner-product', 'c3-def-linear-functional',
     'c3-thm-linear-zero', 'c4-thm-complex-properties'],
    number='6.6', page=185
)

s.d(
    'def-norm',
    'Norm determined by an inner product',
    r'''For a vector $v$ in an inner product space, define its \emph{norm} by
\[
\norm{v}=\sqrt{\ip{v}{v}},
\]
using the nonnegative real square root. The inner-product positivity axiom ensures that this square root is defined.''',
    '6.7', 186
)

s.r(
    'ex-coordinate-norm',
    'The Euclidean coordinate norm',
    r'''In $\F^n$ with the Euclidean inner product,
\[
\norm{(z_1,\ldots,z_n)}
=\sqrt{\sum_{j=1}^{n}|z_j|^2}.
\]''',
    r'''The Euclidean inner product gives
$\ip{z}{z}=\sum_jz_j\overline{z_j}=\sum_j|z_j|^2$.
Taking the nonnegative square root, as required by the norm definition, gives the formula. If $n=0$, the sum is zero and the only vector has norm zero.''',
    1, 10,
    [r'Put the same vector into both positions of the inner product.'],
    ['def-norm', 'thm-standard-inner-product', 'c4-thm-complex-properties'],
    number='6.8(a)', page=186, kind='example'
)

s.r(
    'ex-continuous-integral-norm',
    'The integral norm of a continuous function',
    r'''For the integral inner product on $C([-1,1],\R)$,
\[
\norm{f}=\sqrt{\int_{-1}^{1}f(x)^2\,dx}.
\]''',
    r'''By the defining formula for this inner product,
$\ip{f}{f}=\int_{-1}^{1}f(x)f(x)\,dx=\int_{-1}^{1}f(x)^2\,dx$.
The integral is nonnegative, as established in the verification of that inner product. Substitution into the definition of norm gives the asserted formula.''',
    1, 10,
    [r'Substitute the integral inner product into the norm definition.'],
    ['def-norm', 'ex-continuous-integral-inner-product'],
    number='6.8(b)', page=186, kind='example'
)

s.r(
    'thm-norm-properties',
    'Definiteness and absolute homogeneity of the norm',
    r'''For every vector $v$ and scalar $a$,
\[
\norm{v}\ge0,\qquad
\norm{v}=0\Longleftrightarrow v=0,\qquad
\norm{av}=|a|\norm{v}.
\]''',
    r'''The norm is nonnegative by its square-root definition. It vanishes exactly when its square $\ip{v}{v}$ vanishes, which by inner-product definiteness happens exactly when $v=0$.

For absolute homogeneity, the inner-product scalar rules give
\[
\norm{av}^2
=\ip{av}{av}
=a\overline a\,\ip{v}{v}
=|a|^2\norm{v}^2.
\]
Both $\norm{av}$ and $|a|\norm{v}$ are nonnegative real numbers. They have equal squares, so they are equal. This proof also applies when $a=0$ or $v=0$.''',
    1, 10,
    [r'Prove the scaling identity after squaring both sides.'],
    ['def-norm', 'def-inner-product',
     'thm-inner-product-properties', 'c4-thm-complex-properties'],
    number='6.9', page=186
)

s.r(
    'ex-norm-not-linear',
    'A norm on a nonzero space is not linear',
    r'''If $V\ne\{0\}$ is an inner product space, the function $v\mapsto\norm{v}$, viewed as taking values in $\F$, is not linear.''',
    r'''Choose $v\ne0$. Then $\norm{v}>0$ by norm definiteness and nonnegativity. Absolute homogeneity gives
$\norm{-v}=|-1|\norm{v}=\norm{v}$.
If the norm function were linear, homogeneity with scalar $-1$ would instead give $\norm{-v}=-\norm{v}$. These equations imply $2\norm{v}=0$, contradicting $\norm{v}>0$. Thus linearity fails.''',
    1, 10,
    [r'Compare the required linearity rule at $-v$ with absolute homogeneity.'],
    ['thm-norm-properties', 'c3-def-linear-map', 'c1-foundations'],
    page=186, kind='example'
)

s.d(
    'def-orthogonal',
    'Orthogonal vectors',
    r'''Vectors $u,v$ are \emph{orthogonal} if $\ip{u}{v}=0$. We write $u\perp v$ for this condition.''',
    '6.10', 187
)

s.r(
    'thm-zero-orthogonality',
    'Symmetry of orthogonality and the role of zero',
    r'''Orthogonality is symmetric. The zero vector is orthogonal to every vector, and a vector is orthogonal to itself exactly when it is zero.''',
    r'''If $\ip{u}{v}=0$, conjugate symmetry gives
$\ip{v}{u}=\overline{\ip{u}{v}}=\overline0=0$.
Interchanging the vectors proves the converse, so orthogonality is symmetric.

The earlier zero identities give $\ip{0}{v}=\ip{v}{0}=0$, establishing that zero is orthogonal to every vector. Finally, self-orthogonality means $\ip{v}{v}=0$, which is equivalent to $v=0$ by the definiteness axiom.''',
    1, 10,
    [r'Apply conjugate symmetry and definiteness.'],
    ['def-orthogonal', 'def-inner-product', 'thm-inner-product-properties'],
    number='6.11', page=187
)

s.r(
    'lem-squared-norm-expansion',
    'Expanding the squared norm of a sum or difference',
    r'''For all $u,v$ in an inner product space,
\[
\norm{u+v}^2
=\norm{u}^2+\norm{v}^2+2\operatorname{Re}\ip{u}{v},
\]
and
\[
\norm{u-v}^2
=\norm{u}^2+\norm{v}^2-2\operatorname{Re}\ip{u}{v}.
\]''',
    r'''Expanding in both inner-product variables gives
\[
\begin{aligned}
\norm{u+v}^2
&=\ip{u+v}{u+v}\\
&=\ip{u}{u}+\ip{u}{v}+\ip{v}{u}+\ip{v}{v}\\
&=\norm{u}^2+\norm{v}^2+\ip{u}{v}+\overline{\ip{u}{v}}.
\end{aligned}
\]
For any scalar $z$, $z+\overline z=2\operatorname{Re}z$, so this is the first identity.

Apply that identity to $u,-v$. Norm homogeneity gives $\norm{-v}=\norm{v}$, and conjugate linearity in the second variable gives
$\ip{u}{-v}=-\ip{u}{v}$ because $-1$ is real. The real part of $-z$ is the negative of the real part of $z$, directly from real and imaginary coordinates. Substitution gives the second identity.''',
    2, 15,
    [r'Expand before simplifying the two mixed terms.'],
    ['def-norm', 'thm-inner-product-properties', 'def-inner-product',
     'thm-norm-properties', 'c4-thm-complex-properties',
     'c4-def-real-imaginary'],
    page=187, kind='lemma'
)

s.r(
    'thm-pythagorean',
    'Pythagorean theorem',
    r'''If $u\perp v$, then
\[
\norm{u+v}^2=\norm{u}^2+\norm{v}^2.
\]''',
    r'''Orthogonality gives $\ip{u}{v}=0$, whose real part is zero. Substituting into the squared-norm expansion yields
\[
\norm{u+v}^2
=\norm{u}^2+\norm{v}^2+2\operatorname{Re}0
=\norm{u}^2+\norm{v}^2.
\]
The calculation allows either vector to be zero.''',
    1, 10,
    [r'Expand the squared norm and use the vanishing mixed inner product.'],
    ['def-orthogonal', 'lem-squared-norm-expansion'],
    number='6.12', page=187
)

s.r(
    'thm-orthogonal-decomposition',
    'Separating a component along one vector',
    r'''Let $v\ne0$ and $u\in V$. There is a unique expression
\[
u=cv+w,\qquad c\in\F,\quad w\perp v.
\]
It is given by
\[
c=\frac{\ip{u}{v}}{\norm{v}^2},
\qquad
w=u-\frac{\ip{u}{v}}{\norm{v}^2}v.
\]''',
    r'''Because $v\ne0$, norm definiteness gives $\norm{v}^2>0$, so the displayed coefficient is defined. Set $c$ and $w$ by those formulas. Then $cv+w=u$ by the definition of $w$. First-variable linearity gives
\[
\ip{w}{v}
=\ip{u-cv}{v}
=\ip{u}{v}-c\ip{v}{v}
=\ip{u}{v}-\frac{\ip{u}{v}}{\norm{v}^2}\norm{v}^2
=0.
\]
Thus $w\perp v$, proving existence.

For uniqueness, suppose also $u=dv+y$ with $y\perp v$. Taking the inner product with $v$ in the second position gives
\[
\ip{u}{v}=d\ip{v}{v}+\ip{y}{v}=d\norm{v}^2.
\]
Division by the positive number $\norm{v}^2$ forces $d=c$, and then $y=u-dv=u-cv=w$. Hence both components are unique.''',
    2, 20,
    [
        r'Write $u=cv+(u-cv)$ and solve the condition $\ip{u-cv}{v}=0$.',
        r'For uniqueness, take the inner product of any proposed decomposition with $v$.'
    ],
    ['thm-norm-properties', 'def-norm', 'def-orthogonal',
     'def-inner-product', 'thm-inner-product-properties',
     'c1-def-vector-subtraction'],
    number='6.13', page=188
)

s.r(
    'thm-cauchy-schwarz',
    'Cauchy-Schwarz inequality and its equality case',
    r'''For all $u,v$ in an inner product space,
\[
|\ip{u}{v}|\le\norm{u}\norm{v}.
\]
Equality holds exactly when one of the two vectors is a scalar multiple of the other.''',
    r'''If $v=0$, the inner product is zero and the product of norms is zero. Equality holds, and $v=0u$ is a scalar multiple of $u$. We may therefore assume $v\ne0$.

Use the orthogonal decomposition $u=cv+w$, where
$c=\ip{u}{v}/\norm{v}^2$ and $\ip{w}{v}=0$.
Conjugate symmetry gives $\ip{v}{w}=0$, and first-variable homogeneity gives $\ip{cv}{w}=0$. Thus the Pythagorean theorem and norm homogeneity imply
\[
\norm{u}^2
=|c|^2\norm{v}^2+\norm{w}^2
=\frac{|\ip{u}{v}|^2}{\norm{v}^2}+\norm{w}^2.
\]
The denominator is positive real, so the modulus of division by it is division of the modulus by that same number. Multiplying by $\norm{v}^2$ yields
\[
\norm{u}^2\norm{v}^2
=|\ip{u}{v}|^2+\norm{v}^2\norm{w}^2
\ge|\ip{u}{v}|^2.
\]
Comparison of nonnegative square roots proves the inequality.

All operations leading to it preserve equality, and $\norm{v}^2>0$. Hence equality holds exactly when $\norm{w}^2=0$, or equivalently $w=0$. This condition says $u=cv$. Conversely, if $u=av$, then
$\ip{u}{v}=a\norm{v}^2$, so the decomposition coefficient is $c=a$ and $w=0$, giving equality.

When $v\ne0$, the assertion that either vector is a scalar multiple of the other is equivalent to $u$ being a scalar multiple of $v$: if $v=au$, then $a\ne0$ and $u=a^{-1}v$. Together with the already treated case $v=0$, this proves the stated equality characterization in all cases.''',
    3, 35,
    [
        r'Decompose $u$ into a multiple of $v$ and a vector orthogonal to $v$.',
        r'Apply the Pythagorean theorem and keep track of the nonnegative remainder.',
        r'Equality occurs exactly when that orthogonal remainder vanishes.'
    ],
    ['thm-orthogonal-decomposition', 'thm-pythagorean',
     'thm-norm-properties', 'thm-inner-product-properties',
     'thm-zero-orthogonality', 'c4-thm-complex-properties',
     'c1-foundations'],
    number='6.14', page=189
)

s.r(
    'ex-coordinate-cauchy-schwarz',
    'Cauchy-Schwarz for finite real sums',
    r'''For real numbers $x_1,\ldots,x_n,y_1,\ldots,y_n$,
\[
\left(\sum_{j=1}^{n}x_jy_j\right)^2
\le
\left(\sum_{j=1}^{n}x_j^2\right)
\left(\sum_{j=1}^{n}y_j^2\right).
\]
Equality holds exactly when one of the coordinate vectors is a real scalar multiple of the other.''',
    r'''Apply Cauchy-Schwarz in the Euclidean inner product space $\R^n$ to $x=(x_j)$ and $y=(y_j)$. Its inner product is $\sum_jx_jy_j$, and the squared norms are the two sums of squares on the right. Squaring the nonnegative inequality therefore gives the displayed formula, because the square of the absolute value of a real number equals its ordinary square.

Squaring preserves equality between nonnegative quantities. Thus the equality condition is exactly the scalar-multiple condition in Cauchy-Schwarz over the real field, including either vector being zero.''',
    1, 10,
    [r'Apply the vector inequality in the standard real coordinate space and square it.'],
    ['thm-cauchy-schwarz', 'thm-standard-inner-product',
     'ex-coordinate-norm'],
    number='6.16(a)', page=189, kind='example'
)

s.r(
    'ex-integral-cauchy-schwarz',
    'Cauchy-Schwarz for continuous-function integrals',
    r'''For $f,g\in C([-1,1],\R)$,
\[
\left|\int_{-1}^{1}f(x)g(x)\,dx\right|^2
\le
\left(\int_{-1}^{1}f(x)^2\,dx\right)
\left(\int_{-1}^{1}g(x)^2\,dx\right).
\]
Equality holds exactly when one function is a real scalar multiple of the other on the entire interval.''',
    r'''The continuous-function integral formula is an inner product by its earlier verification. Apply Cauchy-Schwarz in that space. The inner product on the left is the integral of $fg$, while the squared norms are the integrals of $f^2$ and $g^2$. Squaring the inequality gives the displayed statement.

Both sides before squaring are nonnegative, so equality is preserved by squaring. The equality characterization in the vector-space theorem says that one vector is a scalar multiple of the other. In this function space, that means equality of the corresponding functions at every point of $[-1,1]$, as asserted.''',
    1, 10,
    [r'Use the integral inner product on continuous functions.'],
    ['thm-cauchy-schwarz', 'ex-continuous-integral-inner-product',
     'ex-continuous-integral-norm'],
    number='6.16(b)', page=190, kind='example'
)

s.r(
    'thm-triangle-inequality',
    'Triangle inequality and its equality case',
    r'''For all $u,v$ in an inner product space,
\[
\norm{u+v}\le\norm{u}+\norm{v}.
\]
Equality holds exactly when one of $u,v$ is a nonnegative real multiple of the other, even when the scalar field is $\C$.''',
    r'''Write $\alpha=\ip{u}{v}$. The squared-norm expansion, the scalar real-part bound, and Cauchy-Schwarz give
\[
\begin{aligned}
\norm{u+v}^2
&=\norm{u}^2+\norm{v}^2+2\operatorname{Re}\alpha\\
&\le\norm{u}^2+\norm{v}^2+2|\alpha|\\
&\le\norm{u}^2+\norm{v}^2+2\norm{u}\norm{v}\\
&=(\norm{u}+\norm{v})^2.
\end{aligned}
\]
Both norms and their sum are nonnegative. Taking nonnegative square roots proves the inequality.

If either vector is zero, equality holds, and that zero vector is zero times the other vector, satisfying the stated condition. Now suppose both vectors are nonzero and equality holds. The first and last quantities in the chain of inequalities are equal, so each intervening inequality is an equality. Thus
\[
\operatorname{Re}\alpha=|\alpha|=\norm{u}\norm{v}>0.
\]
To see that this forces $\alpha$ to be real, write $\alpha=a+bi$. Then $a=|\alpha|\ge0$, and squaring gives
$a^2=a^2+b^2$, so $b=0$. Consequently $\alpha=\norm{u}\norm{v}$ is positive real.

Equality in Cauchy-Schwarz makes the two nonzero vectors scalar multiples. Because $v\ne0$, write $u=cv$. Then
\[
c=\frac{\ip{u}{v}}{\norm{v}^2}
=\frac{\norm{u}\norm{v}}{\norm{v}^2}>0,
\]
so the scalar is positive real.

Conversely, if $u=tv$ with real $t\ge0$, norm homogeneity gives
\[
\norm{u+v}=\norm{(t+1)v}
=(t+1)\norm{v}
=t\norm{v}+\norm{v}
=\norm{u}+\norm{v}.
\]
If instead $v=tu$ with $t\ge0$, the same computation with the two vectors exchanged proves equality. This includes $t=0$ and completes all cases.''',
    3, 35,
    [
        r'Expand the squared norm and bound the real part of the mixed inner product.',
        r'For equality, both the real-part bound and Cauchy-Schwarz must be equalities.',
        r'A complex number whose real part equals its modulus is nonnegative real.'
    ],
    ['lem-squared-norm-expansion', 'thm-cauchy-schwarz',
     'thm-norm-properties', 'thm-inner-product-properties',
     'c4-thm-complex-properties', 'c4-def-real-imaginary',
     'c4-def-conjugate-modulus'],
    number='6.17', page=190
)

s.r(
    'thm-parallelogram',
    'Parallelogram identity',
    r'''For all $u,v$ in an inner product space,
\[
\norm{u+v}^2+\norm{u-v}^2
=2\bigl(\norm{u}^2+\norm{v}^2\bigr).
\]''',
    r'''The squared-norm expansion gives
\[
\norm{u+v}^2
=\norm{u}^2+\norm{v}^2+2\operatorname{Re}\ip{u}{v}
\]
and
\[
\norm{u-v}^2
=\norm{u}^2+\norm{v}^2-2\operatorname{Re}\ip{u}{v}.
\]
Adding these equations cancels the mixed terms and leaves
$2\norm{u}^2+2\norm{v}^2$, which is the asserted right side. No nonzero-vector hypothesis is used.''',
    2, 15,
    [r'Add the two squared-norm expansions so the mixed terms cancel.'],
    ['lem-squared-norm-expansion'],
    number='6.21', page=191
)

s.card(
    'inner-product-convention',
    'def-inner-product',
    r'''Which variable of the inner product is linear in this module?''',
    r'''The first variable: $\ip{au+bv}{w}=a\ip{u}{w}+b\ip{v}{w}$.'''
)

s.card(
    'inner-product-second-scalar',
    'thm-inner-product-properties',
    r'''What happens when a scalar is moved out of the second variable?''',
    r'''It is conjugated: $\ip{u}{av}=\overline a\,\ip{u}{v}$.'''
)

s.card(
    'euclidean-inner-product',
    'thm-standard-inner-product',
    r'''What is the Euclidean inner product on $\F^n$?''',
    r'''$\ip{u}{v}=\sum_{j=1}^{n}u_j\overline{v_j}$.'''
)

s.card(
    'norm-homogeneity',
    'thm-norm-properties',
    r'''How does the norm change under scalar multiplication?''',
    r'''$\norm{av}=|a|\norm{v}$.'''
)

s.card(
    'self-orthogonality',
    'thm-zero-orthogonality',
    r'''Which vectors can be orthogonal to themselves?''',
    r'''Only the zero vector, because $\ip{v}{v}=0$ forces $v=0$.'''
)

s.card(
    'one-vector-orthogonal-decomposition',
    'thm-orthogonal-decomposition',
    r'''For $v\ne0$, what is the component of $u$ along $v$ in its orthogonal decomposition?''',
    r'''It is $\dfrac{\ip{u}{v}}{\norm{v}^2}v$; subtracting it from $u$ gives a vector orthogonal to $v$.'''
)

s.card(
    'cauchy-schwarz-equality',
    'thm-cauchy-schwarz',
    r'''State Cauchy-Schwarz and its equality condition.''',
    r'''$|\ip{u}{v}|\le\norm{u}\norm{v}$, with equality exactly when one vector is a scalar multiple of the other, including zero-vector cases.'''
)

s.card(
    'triangle-equality',
    'thm-triangle-inequality',
    r'''When does equality hold in the triangle inequality, including over complex scalars?''',
    r'''Exactly when one vector is a nonnegative real multiple of the other.'''
)

s.card(
    'parallelogram',
    'thm-parallelogram',
    r'''State the parallelogram identity.''',
    r'''$\norm{u+v}^2+\norm{u-v}^2=2(\norm{u}^2+\norm{v}^2)$.'''
)

s.write()
