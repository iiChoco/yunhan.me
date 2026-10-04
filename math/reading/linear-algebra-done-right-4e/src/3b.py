from common import Section

s = Section('3b')

s.p(
    'intro-null-spaces-ranges',
    'Inputs sent to zero and outputs that occur',
    r'''Two subspaces describe important features of a linear map: the inputs it sends to zero and the outputs it produces. When the domain is finite-dimensional, the dimensions of these subspaces account for the entire dimension of the domain.''',
    59
)

s.d(
    'def-null-space',
    'Null space',
    r'''For $T\in\Lin(V,W)$, its \emph{null space}, also called its \emph{kernel}, is
\[
\Null T=\{v\in V:Tv=0_W\}.
\]
Thus membership in the null space is a condition on vectors in the domain.''',
    '3.11', 59
)

s.r(
    'ex-null-zero-map',
    'The null space of a zero map',
    r'''For the zero map $0:V\to W$, prove that $\Null 0=V$.''',
    r'''Every $v\in V$ is sent to $0_W$ by the definition of the zero map, so every $v\in V$ belongs to its null space. Conversely, a null space consists only of vectors from the domain, so it is contained in $V$. The two inclusions give the equality.''',
    1, 10,
    [r'Which inputs does the zero map send to zero?'],
    ['def-null-space', 'def-zero-identity-maps'],
    number='3.12', page=59, kind='example'
)

s.r(
    'ex-null-coordinate-functional',
    'The null space of a coordinate functional',
    r'''Define $\varphi:\C^3\to\C$ by
\[
\varphi(z_1,z_2,z_3)=z_1+2z_2+3z_3.
\]
Prove that $\varphi$ is linear and that
\[
\Null\varphi
=\{(z_1,z_2,z_3)\in\C^3:z_1+2z_2+3z_3=0\}.
\]''',
    r'''For $u,v\in\C^3$, distributing the scalar coefficients gives
\[
\varphi(u+v)
=(u_1+2u_2+3u_3)+(v_1+2v_2+3v_3)
=\varphi(u)+\varphi(v).
\]
For $a\in\C$, the same distributive laws give
$\varphi(au)=a(u_1+2u_2+3u_3)=a\varphi(u)$.
Thus $\varphi$ is linear. By the definition of its null space, a vector belongs to $\Null\varphi$ exactly when the displayed formula for its image equals zero. This is precisely the stated coordinate condition.''',
    1, 10,
    [r'For the null space, set the output formula equal to zero.'],
    ['def-linear-map', 'def-null-space',
     'c1-def-coordinate-addition', 'c1-def-coordinate-scaling'],
    number='3.12', page=59, kind='example'
)

s.r(
    'ex-null-polynomial-differentiation',
    'Polynomials with zero derivative',
    r'''For the differentiation map $D:\Poly(\R)\to\Poly(\R)$, prove that $\Null D$ consists exactly of the constant polynomials.''',
    r'''Write $p(x)=\sum_{j=0}^{m}a_jx^j$. The polynomial differentiation formula gives
\[
Dp=\sum_{j=1}^{m}ja_jx^{j-1}.
\]
If $Dp=0$, uniqueness of polynomial coefficients gives $ja_j=0$ for every $j=1,\ldots,m$. Each such integer $j$ is a nonzero real scalar, so $a_j=0$. Consequently $p(x)=a_0$ is constant. Conversely, the differentiation formula gives derivative zero for a constant polynomial, because its derivative is an empty sum. Hence every constant polynomial lies in the null space, proving the equality.''',
    2, 15,
    [
        r'Write the derivative in terms of the coefficients of the original polynomial.',
        r'Use coefficient uniqueness, then divide by each positive integer index.'
    ],
    ['def-null-space', 'ex-polynomial-differentiation',
     'c2-thm-polynomial-differentiation', 'c2-lem-polynomial-coefficients',
     'c1-lem-scalar-cancellation'],
    number='3.12', page=59, kind='example'
)

s.r(
    'ex-null-polynomial-square-multiplication',
    'Multiplication by a square loses no polynomial',
    r'''Let $M:\Poly(\R)\to\Poly(\R)$ be multiplication by $x^2$, so $(Mp)(x)=x^2p(x)$. Prove that $\Null M=\{0\}$.''',
    r'''For $p(x)=\sum_{j=0}^{m}a_jx^j$, multiplication gives
\[
(Mp)(x)=\sum_{j=0}^{m}a_jx^{j+2}.
\]
If $Mp=0$, uniqueness of coefficients of the zero polynomial gives $a_j=0$ for every $j$, so $p=0$. Conversely, multiplication of the zero polynomial by $x^2$ is again zero. Thus zero is the only member of the null space.''',
    1, 10,
    [r'Multiplication by $x^2$ shifts the coefficient list by two positions.'],
    ['def-null-space', 'ex-polynomial-multiplication',
     'c2-lem-polynomial-coefficients'],
    number='3.12', page=59, kind='example'
)

s.r(
    'ex-null-backward-shift',
    'The information discarded by a backward shift',
    r'''For the backward shift $B:\F^\infty\to\F^\infty$, defined by $(Bx)_k=x_{k+1}$, prove
\[
\Null B=\{(a,0,0,\ldots):a\in\F\}.
\]''',
    r'''The equation $Bx=0$ means that $(Bx)_k=0$ for every $k\ge1$. By the shift formula this is equivalent to $x_{k+1}=0$ for every $k\ge1$, which says that all entries of $x$ from its second entry onward vanish. There is no condition on $x_1$. Thus the solutions are exactly the displayed sequences, and each of those sequences is indeed shifted to zero.''',
    1, 10,
    [r'Which entries of an input sequence occur in its shifted output?'],
    ['def-null-space', 'ex-backward-shift', 'c1-def-sequences'],
    number='3.12', page=59, kind='example'
)

s.r(
    'thm-null-subspace',
    'The null space is a subspace of the domain',
    r'''For every $T\in\Lin(V,W)$, the set $\Null T$ is a subspace of $V$.''',
    r'''A linear map preserves zero, so $T0_V=0_W$ and $0_V\in\Null T$. If $u,v\in\Null T$, additivity gives
\[
T(u+v)=Tu+Tv=0_W+0_W=0_W.
\]
Hence $u+v\in\Null T$. If $a\in\F$ and $u\in\Null T$, homogeneity gives
\[
T(au)=aTu=a0_W=0_W.
\]
Thus $au\in\Null T$. The subspace test now proves the assertion.''',
    1, 10,
    [r'Check zero, addition, and scalar multiplication using linearity.'],
    ['def-null-space', 'def-linear-map', 'thm-linear-zero',
     'c1-thm-subspace-test', 'c1-thm-scalar-zero'],
    number='3.13', page=59
)

s.d(
    'def-injective',
    'Injective functions',
    r'''A function $T:V\to W$ is \emph{injective}, or \emph{one-to-one}, if for every $u,v\in V$, the equality $Tu=Tv$ implies $u=v$. Equivalently, distinct inputs must have distinct outputs.''',
    '3.14', 60
)

s.r(
    'thm-injective-null',
    'Injectivity is detected by the null space',
    r'''A linear map $T\in\Lin(V,W)$ is injective if and only if $\Null T=\{0_V\}$.''',
    r'''Suppose first that $T$ is injective. If $v\in\Null T$, then $Tv=0_W=T0_V$, where the second equality follows from preservation of zero. Injectivity gives $v=0_V$. Since $0_V$ belongs to the null space, this proves $\Null T=\{0_V\}$.

Conversely, suppose the null space is $\{0_V\}$ and $Tu=Tv$. Linearity and the negative-one identity give
\[
T(u-v)=T(u+(-1)v)=Tu+(-1)Tv=Tu-Tv=0_W.
\]
Hence $u-v\in\Null T$, so $u-v=0_V$. Adding $v$ gives $u=v$. This proves injectivity. Neither implication requires the domain or target to be nonzero.''',
    2, 15,
    [
        r'For a linear map, equal outputs turn a difference of inputs into a null-space vector.',
        r'For the other direction, compare the image of a null-space vector with the image of zero.'
    ],
    ['def-injective', 'def-null-space', 'def-linear-map',
     'thm-linear-zero', 'c1-def-vector-subtraction', 'c1-thm-negative-one'],
    number='3.15', page=60
)

s.r(
    'ex-injectivity-from-kernels',
    'Applying the null-space test to the examples',
    r'''Prove the following conclusions about the maps already considered:
\begin{itemize}
\item Multiplication by $x^2$ on $\Poly(\R)$ is injective.
\item Polynomial differentiation, the backward shift, and the coordinate functional $\varphi(z_1,z_2,z_3)=z_1+2z_2+3z_3$ are not injective.
\item The zero map $V\to W$ is injective exactly when $V=\{0\}$.
\end{itemize}''',
    r'''Multiplication by $x^2$ has null space $\{0\}$ by its computed null-space example, so it is injective.

The nonzero constant polynomial $1$ lies in the differentiation null space. The nonzero sequence $(1,0,0,\ldots)$ lies in the backward-shift null space. The vector $(-2,1,0)$ is nonzero and lies in $\Null\varphi$, because $-2+2\cdot1+3\cdot0=0$. Each of these three null spaces therefore differs from $\{0\}$, so none of those maps is injective.

Finally, the zero map has null space $V$. The injectivity criterion says that it is injective exactly when this null space equals $\{0\}$, which is exactly the condition $V=\{0\}$.''',
    1, 10,
    [r'Use the null spaces already computed; exhibit a nonzero member when injectivity fails.'],
    ['thm-injective-null', 'ex-null-polynomial-square-multiplication',
     'ex-null-polynomial-differentiation', 'ex-null-backward-shift',
     'ex-null-coordinate-functional', 'ex-null-zero-map'],
    page=60, kind='example'
)

s.d(
    'def-range',
    'Range',
    r'''For $T\in\Lin(V,W)$, its \emph{range} is the set of outputs that actually occur:
\[
\Range T=\{Tv:v\in V\}\subseteq W.
\]
A vector $w\in W$ belongs to this set precisely when there exists an input $v\in V$ with $Tv=w$.''',
    '3.16', 61
)

s.r(
    'ex-range-zero-map',
    'The range of a zero map',
    r'''For the zero map $0:V\to W$, prove that $\Range 0=\{0_W\}$.''',
    r'''Every output of this map is $0_W$, so the range is contained in $\{0_W\}$. The domain contains $0_V$, and its image is $0_W$, so $0_W$ actually belongs to the range. Thus the range equals the stated singleton, including when the domain itself is the zero space.''',
    1, 10,
    [r'Check both that no other output occurs and that zero does occur.'],
    ['def-range', 'def-zero-identity-maps', 'c1-def-vector-space'],
    number='3.17', page=61, kind='example'
)

s.r(
    'ex-range-coordinate-map',
    'Describing a range by an equation',
    r'''Let $T:\R^2\to\R^3$ be given by $T(x,y)=(2x,5y,x+y)$. Prove that $T$ is linear and that
\[
\Range T
=\{(2x,5y,x+y):x,y\in\R\}
=\{(a,b,c)\in\R^3:5a+2b=10c\}.
\]
Prove also that this range is a subspace of $\R^3$.''',
    r'''Each output coordinate is a fixed linear combination of the input coordinates, so the coordinate-map theorem proves that $T$ is linear. The first range description follows from the definition of range.

For an output $(a,b,c)=(2x,5y,x+y)$, one has
$5a+2b=10x+10y=10c$, giving one inclusion in the second description. Conversely, suppose $5a+2b=10c$. Set $x=a/2$ and $y=b/5$. Then
\[
x+y=\frac{5a+2b}{10}=c,
\]
so $T(x,y)=(a,b,c)$. This proves the reverse inclusion.

Finally, every output can be written as
\[
T(x,y)=x(2,0,1)+y(0,5,1),
\]
and every such combination is an output. Thus the range is the span of these two vectors and is a subspace by the span theorem.''',
    2, 20,
    [
        r'Eliminate the input parameters from the three output coordinates.',
        r'To prove the reverse inclusion, recover the inputs from the first two output coordinates.'
    ],
    ['def-range', 'thm-coordinate-linear-maps',
     'c2-def-span', 'c2-thm-span-smallest'],
    number='3.17', page=61, kind='example'
)

s.r(
    'ex-range-polynomial-differentiation',
    'Every polynomial is a derivative',
    r'''For $D:\Poly(\R)\to\Poly(\R)$ given by differentiation, prove that $\Range D=\Poly(\R)$.''',
    r'''The range is contained in $\Poly(\R)$ because differentiation maps polynomials to polynomials. To prove the opposite inclusion, take an arbitrary
\[
q(x)=\sum_{j=0}^{m}a_jx^j
\]
and define
\[
p(x)=\sum_{j=0}^{m}\frac{a_j}{j+1}x^{j+1}.
\]
All denominators are nonzero real numbers, and this finite expression defines a polynomial. Its derivative is
\[
p'(x)=\sum_{j=0}^{m}(j+1)\frac{a_j}{j+1}x^j
=\sum_{j=0}^{m}a_jx^j=q(x).
\]
Thus $q=Dp$ belongs to the range. The construction also applies to the zero polynomial by taking every coefficient zero.''',
    2, 15,
    [
        r'Construct an input separately for each monomial in the desired output.',
        r'Raise each exponent by one and divide its coefficient by the new exponent.'
    ],
    ['def-range', 'ex-polynomial-differentiation',
     'c2-def-polynomial', 'c2-thm-polynomial-differentiation'],
    number='3.17', page=61, kind='example'
)

s.r(
    'thm-range-subspace',
    'The range is a subspace of the target',
    r'''For every $T\in\Lin(V,W)$, the set $\Range T$ is a subspace of $W$.''',
    r'''Since $T0_V=0_W$, the target's zero vector belongs to the range. If $y,z\in\Range T$, choose $u,v\in V$ with $Tu=y$ and $Tv=z$. Then
\[
y+z=Tu+Tv=T(u+v),
\]
so $y+z$ also belongs to the range. If $a\in\F$ and $y=Tu$ is in the range, then $ay=aTu=T(au)$ is in the range. These facts verify the subspace test.''',
    1, 10,
    [
        r'For each output in the range, choose an input producing it.'
    ],
    ['def-range', 'def-linear-map', 'thm-linear-zero',
     'c1-thm-subspace-test'],
    number='3.18', page=61
)

s.d(
    'def-surjective',
    'Surjective functions',
    r'''A function $T:V\to W$ is \emph{surjective}, or \emph{onto}, when every element of $W$ occurs as an output. For a linear map this says $\Range T=W$; the specified target space is part of this condition.''',
    '3.19', 62
)

s.r(
    'ex-surjectivity-from-ranges',
    'Reading surjectivity from the range',
    r'''Prove that polynomial differentiation $\Poly(\R)\to\Poly(\R)$ is surjective, that $T:\R^2\to\R^3$ given by $T(x,y)=(2x,5y,x+y)$ is not surjective, and that the zero map $V\to W$ is surjective exactly when $W=\{0\}$.''',
    r'''The computed range of differentiation is all of $\Poly(\R)$, so it is surjective.

Every vector $(a,b,c)$ in the range of the coordinate map satisfies $5a+2b=10c$. The target vector $(0,0,1)$ violates this equation, because its two sides are $0$ and $10$. It is therefore outside the range, so this map is not surjective.

The zero map has range $\{0_W\}$. That range equals its target $W$ exactly when $W$ is the zero space, proving the last assertion.''',
    1, 10,
    [
        r'Compare each computed range with the specified target.'
    ],
    ['def-surjective', 'ex-range-polynomial-differentiation',
     'ex-range-coordinate-map', 'ex-range-zero-map'],
    page=62, kind='example'
)

s.r(
    'ex-surjectivity-depends-on-target',
    'The target can change surjectivity',
    r'''The formulas
\[
D_5:\Poly_5(\R)\to\Poly_5(\R),\quad D_5p=p',
\qquad
S:\Poly_5(\R)\to\Poly_4(\R),\quad Sp=p'
\]
define linear maps. Prove that both have range $\Poly_4(\R)$, so $D_5$ is not surjective whereas $S$ is surjective.''',
    r'''The derivative of a polynomial of degree at most $5$ has degree at most $4$, or is the zero polynomial, by the coefficient formula for differentiation. Hence both formulas have outputs in their stated targets. The linearity identities are inherited from differentiation on all polynomials, so both maps are linear.

Their outputs belong to $\Poly_4(\R)$. Conversely, for
$q(x)=\sum_{j=0}^{4}a_jx^j$, the polynomial
\[
p(x)=\sum_{j=0}^{4}\frac{a_j}{j+1}x^{j+1}
\]
belongs to $\Poly_5(\R)$ and satisfies $p'=q$. Thus every member of $\Poly_4(\R)$ is an output of both maps, proving the asserted common range.

The polynomial $x^5$ belongs to $\Poly_5(\R)$ but not to $\Poly_4(\R)$, because uniqueness of coefficients prevents a nonzero coefficient at exponent $5$ from being represented using lower exponents. Therefore $D_5$ misses a vector in its target. The target of $S$ is exactly the common range, so $S$ is surjective.''',
    2, 20,
    [
        r'Find the precise degree bound on the derivative.',
        r'Construct an antiderivative of each polynomial of degree at most four.'
    ],
    ['def-surjective', 'def-range', 'ex-polynomial-differentiation',
     'c2-def-polynomial-space', 'c2-def-degree',
     'c2-thm-polynomial-differentiation', 'c2-lem-polynomial-coefficients'],
    number='3.20', page=62, kind='example'
)

s.p(
    'intro-rank-nullity',
    'Counting the lost and retained coordinates',
    r'''A basis of the null space records directions that disappear under the map. Extending that basis to the domain will reveal a basis of the range among the images of the added vectors.''',
    62
)

s.r(
    'thm-rank-nullity',
    'Fundamental theorem of linear maps',
    r'''Let $V$ be finite-dimensional, let $W$ be any vector space over $\F$, and let $T\in\Lin(V,W)$. Then $\Range T$ is finite-dimensional and
\[
\dim V=\dim\Null T+\dim\Range T.
\]
This equality is also called the \emph{rank-nullity formula}.''',
    r'''The null space is a subspace of the finite-dimensional space $V$, so it is finite-dimensional. Choose a basis $u_1,\ldots,u_m$ of $\Null T$, and extend it to a basis
\[
u_1,\ldots,u_m,v_1,\ldots,v_n
\]
of $V$. Thus $\dim\Null T=m$ and $\dim V=m+n$.

We prove that $Tv_1,\ldots,Tv_n$ is a basis of $\Range T$. First, any $x\in V$ can be written as
\[
x=\sum_{j=1}^{m}a_ju_j+\sum_{k=1}^{n}b_kv_k.
\]
Applying linearity, and using $Tu_j=0$ for every $j$, gives
\[
Tx=\sum_{k=1}^{n}b_kTv_k.
\]
Thus every vector in the range is in the span of the displayed image list. Conversely, each $Tv_k$ lies in the range, which is a subspace, so every combination of the image list lies in the range. This proves that the list spans the range, and in particular that the range is finite-dimensional.

For independence, suppose $\sum_{k=1}^{n}c_kTv_k=0$. By linearity,
$T(\sum_kc_kv_k)=0$, so $\sum_kc_kv_k\in\Null T$. The chosen basis of the null space supplies coefficients $d_j$ with
\[
\sum_{k=1}^{n}c_kv_k=\sum_{j=1}^{m}d_ju_j.
\]
Rearranging gives a relation on the extended basis with coefficients $-d_j$ and $c_k$. Its independence forces every $c_k=0$, as well as every $d_j=0$. Hence the image list is independent.

Its basis length is $n$, so $\dim\Range T=n$. Substituting the three basis lengths gives the stated formula. Empty lists are permitted throughout: finite linearity with an empty sum uses $T0=0$, and the independence condition for an empty image list is vacuous. Therefore the proof covers a zero domain, a zero target, and a zero map without exceptions.''',
    3, 45,
    [
        r'Begin with a basis of the null space and extend it to a basis of the domain.',
        r'Try the images of the added basis vectors as a basis of the range.',
        r'A relation among those images puts a combination of the added vectors into the null space.'
    ],
    ['def-null-space', 'def-range', 'thm-null-subspace',
     'thm-range-subspace', 'def-linear-map', 'thm-linear-zero',
     'c2-thm-subspaces-finite', 'c2-thm-basis-existence',
     'c2-thm-extend-independent', 'c2-def-basis',
     'c2-def-dimension', 'c2-def-finite-dimensional',
     'c2-def-linear-independence'],
    number='3.21', page=62
)

s.r(
    'thm-no-injection-lower',
    'A smaller target prevents injectivity',
    r'''If $V,W$ are finite-dimensional and $\dim V>\dim W$, then no linear map $T:V\to W$ is injective.''',
    r'''Let $T:V\to W$ be linear. Its range is finite-dimensional by the fundamental theorem. A basis of the range is an independent list in $W$, so comparison with a basis of $W$ gives
\[
\dim\Range T\le\dim W.
\]
The fundamental theorem therefore yields
\[
\dim\Null T
=\dim V-\dim\Range T
\ge\dim V-\dim W>0.
\]
The zero space has the empty list as a basis and consequently dimension zero. Thus $\Null T$ cannot equal $\{0\}$. The null-space criterion then shows that $T$ is not injective. The proof also permits $W=\{0\}$; the strict inequality in the hypothesis already rules out a zero domain in that case.''',
    2, 20,
    [
        r'Use the fundamental theorem to bound the dimension of the null space from below.',
        r'The range lies in the target, so compare their basis lengths.'
    ],
    ['thm-rank-nullity', 'thm-injective-null', 'thm-range-subspace',
     'c2-def-dimension', 'c2-def-basis', 'c2-thm-basis-existence',
     'c2-thm-independent-length'],
    number='3.22', page=63
)

s.r(
    'ex-four-to-three-not-injective',
    'A dimension count replaces solving equations',
    r'''Consider
\[
T:\F^4\to\F^3,\qquad
T(z_1,z_2,z_3,z_4)
=\bigl(\sqrt7\,z_1+\pi z_2+z_4,\,
97z_1+3z_2+2z_3,\,
z_2+6z_3+7z_4\bigr).
\]
Prove that $T$ is linear and not injective, without solving explicitly for a nonzero null-space vector.''',
    r'''All coefficients in the formula are scalars in $\F$, and each output coordinate is a fixed scalar combination of the input coordinates. Thus the coordinate-map theorem proves linearity.

The standard coordinate bases have lengths $4$ and $3$, so $\dim\F^4=4$ and $\dim\F^3=3$. The theorem excluding injectivity into a smaller finite-dimensional target now applies, giving that $T$ is not injective. No value of a null-space vector needs to be computed.''',
    1, 10,
    [r'Compare the lengths of the standard bases of the domain and target.'],
    ['thm-coordinate-linear-maps', 'thm-no-injection-lower',
     'c2-ex-standard-basis', 'c2-def-dimension'],
    number='3.23', page=63, kind='example'
)

s.r(
    'thm-no-surjection-higher',
    'A larger target prevents surjectivity',
    r'''If $V,W$ are finite-dimensional and $\dim V<\dim W$, then no linear map $T:V\to W$ is surjective.''',
    r'''Let $T:V\to W$ be linear. Dimensions of finite-dimensional spaces are nonnegative integers, because they are basis lengths. The fundamental theorem gives
\[
\dim\Range T=\dim V-\dim\Null T
\le\dim V<\dim W.
\]
If $T$ were surjective, its range would be $W$, and the two spaces would have the same dimension, contradicting the strict inequality. Hence $T$ is not surjective. When $V=\{0\}$, its dimension is zero and the same argument applies to every nonzero finite-dimensional target.''',
    2, 15,
    [
        r'Bound the dimension of the range from above using the fundamental theorem.'
    ],
    ['thm-rank-nullity', 'def-surjective', 'c2-def-dimension'],
    number='3.24', page=64
)

s.d(
    'def-coordinate-linear-system',
    'Systems of scalar linear equations',
    r'''Fix nonnegative integers $m,n$, scalars $A_{jk}\in\F$ for $1\le j\le m$, $1\le k\le n$, and prescribed scalars $c_1,\ldots,c_m$. The corresponding system in the unknowns $x_1,\ldots,x_n$ is
\[
\sum_{k=1}^{n}A_{jk}x_k=c_j
\qquad(1\le j\le m).
\]
A \emph{solution} is a vector $x\in\F^n$ satisfying every equation. The system is \emph{homogeneous} if every $c_j=0$. If $n=0$, each left side is an empty sum equal to zero; if $m=0$, there are no conditions to satisfy.''',
    page=64
)

s.r(
    'lem-system-map-correspondence',
    'A system as one equation for a linear map',
    r'''For the fixed coefficients of a scalar linear system, define $T:\F^n\to\F^m$ by
\[
(Tx)_j=\sum_{k=1}^{n}A_{jk}x_k.
\]
Then $T$ is linear, and the solutions with prescribed right side $c=(c_1,\ldots,c_m)$ are exactly the inputs satisfying $Tx=c$. In particular, the homogeneous solution set is $\Null T$, and a solution for a prescribed $c$ exists exactly when $c\in\Range T$.''',
    r'''The coordinate-map theorem proves that the displayed formula defines a linear map, including the cases of empty input or output lists. Equality $Tx=c$ means equality at each output coordinate. Its $j$th coordinate equation is precisely
$\sum_kA_{jk}x_k=c_j$, so equality of these vectors is equivalent to satisfaction of the system.

For $c=0$, the inputs satisfying $Tx=0$ form $\Null T$ by definition. For general $c$, the existence of an input with image $c$ is exactly the defining condition for $c\in\Range T$. If $m=0$, the output equality and the list of equations are both empty conditions. If $n=0$, the only input is zero and its output is zero, agreeing with the empty-sum equations.''',
    1, 10,
    [r'Compare the two statements one output coordinate at a time.'],
    ['def-coordinate-linear-system', 'thm-coordinate-linear-maps',
     'def-null-space', 'def-range', 'c1-def-list'],
    page=64, kind='lemma'
)

s.r(
    'thm-homogeneous-system',
    'More unknowns give a nonzero homogeneous solution',
    r'''For fixed scalar coefficients, a homogeneous system with $n$ unknowns and $m$ equations has a nonzero solution whenever $n>m$. In particular, every homogeneous system of four scalar linear equations in five unknowns has a nonzero solution.''',
    r'''Let $T:\F^n\to\F^m$ be the associated coordinate map. It is linear, and the homogeneous solutions are exactly $\Null T$ by the system-map correspondence.

The standard bases give $\dim\F^n=n$ and $\dim\F^m=m$, including dimension zero for an empty coordinate space. Since $n>m$, the smaller-target theorem says that $T$ is not injective. The null-space criterion implies $\Null T\ne\{0\}$. Because zero belongs to the null space, this inequality means that some nonzero vector belongs to it. That vector is the required nonzero solution.

The numerical instance follows by taking $n=5$ and $m=4$. If $m=0$, the same argument applies; in that case there are no equations and every vector is a solution, with $n>0$ ensuring that nonzero vectors exist.''',
    2, 20,
    [
        r'Interpret the homogeneous solutions as the null space of a coordinate map.',
        r'Compare the dimension of its domain with the dimension of its target.'
    ],
    ['def-coordinate-linear-system', 'lem-system-map-correspondence',
     'thm-no-injection-lower', 'thm-injective-null',
     'thm-null-subspace', 'c2-ex-standard-basis', 'c2-def-dimension'],
    number='3.26', page=65
)

s.r(
    'thm-overdetermined-system',
    'More equations allow an inconsistent right side',
    r'''Fix the coefficients of a system with $m$ equations in $n$ unknowns. If $m>n$, then there is a choice of right side $(c_1,\ldots,c_m)$ for which the system has no solution. In particular, this conclusion holds for five equations in four unknowns.''',
    r'''For the fixed coefficients, form the associated linear map $T:\F^n\to\F^m$. The standard basis lengths give
\[
\dim\F^n=n<m=\dim\F^m.
\]
The larger-target theorem implies that $T$ is not surjective. Thus $\Range T$ is a proper subset of $\F^m$, so choose $c\in\F^m\setminus\Range T$. The system-map correspondence says that the system with right side $c$ has a solution exactly when $c$ lies in the range. Our choice therefore makes the system inconsistent.

Taking $m=5$, $n=4$ gives the stated instance. If $n=0$, the associated map has only the zero input and zero output; because $m>0$, its target has nonzero vectors and the same argument still supplies an inconsistent right side.''',
    2, 20,
    [
        r'The coefficients determine a map before the right side is chosen.',
        r'Choose a right side outside the range of that map.'
    ],
    ['def-coordinate-linear-system', 'lem-system-map-correspondence',
     'thm-no-surjection-higher', 'def-surjective',
     'c2-ex-standard-basis', 'c2-def-dimension'],
    number='3.28', page=65
)

s.note(
    'remark-some-right-sides',
    'What the inconsistency conclusion says',
    r'''The last theorem asserts that some choice of right side is inconsistent. It does not assert that every right side is inconsistent: choosing the zero right side always permits the zero solution, since each left side is then a sum of zero terms.''',
    65
)

s.card(
    'null-space',
    'def-null-space',
    r'What is the null space of $T:V\to W$, and in which space does it lie?',
    r'$\Null T=\{v\in V:Tv=0_W\}$; it lies in the domain $V$.'
)

s.card(
    'injective-null',
    'thm-injective-null',
    r'How can injectivity of a linear map be checked using a single output?',
    r'Check that the only input sent to zero is zero: $T$ is injective exactly when $\Null T=\{0\}$.'
)

s.card(
    'range',
    'def-range',
    r'What does it mean for $w\in W$ to belong to $\Range T$?',
    r'There exists $v\in V$ such that $Tv=w$.'
)

s.card(
    'surjective-target',
    'ex-surjectivity-depends-on-target',
    r'Why does surjectivity depend on the specified target space?',
    r'The range must equal that target. Differentiation on $\Poly_5(\R)$ has range $\Poly_4(\R)$, so it is onto $\Poly_4(\R)$ but not onto $\Poly_5(\R)$.'
)

s.card(
    'rank-nullity',
    'thm-rank-nullity',
    r'State the fundamental theorem of linear maps, including its finiteness hypothesis.',
    r'If $V$ is finite-dimensional and $T\in\Lin(V,W)$, then $\Range T$ is finite-dimensional and $\dim V=\dim\Null T+\dim\Range T$. The target $W$ need not be finite-dimensional.'
)

s.card(
    'rank-nullity-proof',
    'thm-rank-nullity',
    r'Which basis construction proves the rank-nullity formula?',
    r'Extend a basis of the null space to a basis of the domain. The images of the added vectors form a basis of the range.'
)

s.card(
    'homogeneous-count',
    'thm-homogeneous-system',
    r'What does having more unknowns than equations guarantee for a homogeneous scalar linear system?',
    r'It guarantees a nonzero solution.'
)

s.card(
    'overdetermined-quantifier',
    'thm-overdetermined-system',
    r'When there are more equations than unknowns, does every right side make the system inconsistent?',
    r'No. The theorem guarantees an inconsistent right side for some choice; the zero right side always has the zero solution.'
)

s.write()
