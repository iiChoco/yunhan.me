from common import Section

s = Section('7f')

s.p(
    'intro-svd-consequences',
    'Measuring and interpreting linear maps',
    r'''Throughout this section, $V$ and $W$ are finite-dimensional inner product spaces over $\F$. Singular value decomposition supplies sharp estimates, optimal approximations, and geometric descriptions of linear maps. Volume will require a separately stated analytic prerequisite.''',
    280,
)

s.r(
    'thm-singular-norm-bound',
    'The largest singular value bounds every output',
    r'''Suppose $V\ne\{0\}$, $T\in\Lin(V,W)$, and $s_1$ is the largest singular value of $T$, including zero singular values in the list. Then
    \[
    \norm{Tv}\le s_1\norm v
    \qquad(v\in V).
    \]''',
    r'''If $T=0$, all its singular values are zero and the inequality is an equality. Otherwise let $s_1\ge\cdots\ge s_m>0$ be its positive singular values and choose a reduced singular value decomposition
    \[
    Tv=\sum_{j=1}^m s_j\ip{v}{e_j}f_j.
    \]
    Orthonormality of the $f_j$ gives
    \[
    \norm{Tv}^2
    =\sum_{j=1}^m s_j^2|\ip{v}{e_j}|^2
    \le s_1^2\sum_{j=1}^m|\ip{v}{e_j}|^2
    \le s_1^2\norm v^2,
    \]
    where the last inequality is Bessel's inequality. Taking nonnegative square roots proves the assertion.''',
    2, 15,
    [r'''Expand the image using singular value decomposition.''',
     r'''Bound every squared singular value by the largest one and use Bessel's inequality.'''],
    ['thm-singular-value-decomposition', 'thm-singular-rank',
     'c6-thm-orthonormal-norm', 'c6-thm-bessel'],
    '7.82', 280,
)

s.r(
    'lem-operator-norm-maximum',
    'The maximum over the closed unit ball exists',
    r'''For every $T\in\Lin(V,W)$, the set
    \[
    \{\norm{Tv}:v\in V,\ \norm v\le1\}
    \]
    has a maximum. If $V\ne\{0\}$, that maximum is the largest singular value of $T$. If $V=\{0\}$, it is zero.''',
    r'''If $T=0$, every value in the set is zero, and the set contains zero because $v=0$ is allowed. This covers a zero domain as well. If $T\ne0$, the singular-value bound makes every displayed value at most $s_1$. In a reduced singular value decomposition, $e_1$ is a unit vector and $Te_1=s_1f_1$, where $f_1$ is a unit vector. Thus $\norm{Te_1}=s_1$, so the bound is attained. Finally, when the domain is nonzero and $T=0$, the nonempty singular-value list consists of zeros, giving the stated description of its maximum.''',
    1, 10,
    [r'''Find a unit vector at which the singular-value bound is attained.'''],
    ['thm-singular-norm-bound', 'thm-singular-value-decomposition',
     'thm-singular-rank', 'c6-thm-norm-properties'],
    page=280, kind='lemma',
)

s.d(
    'def-operator-norm',
    'The norm of a linear map',
    r'''For $T\in\Lin(V,W)$, define
    \[
    \norm T=\max_{\norm v\le1}\norm{Tv}.
    \]
    The preceding lemma guarantees existence of this maximum. The same norm notation is used for vectors and linear maps; its argument specifies which meaning applies.''',
    '7.86', 280,
)

s.r(
    'thm-operator-norm-properties',
    'Basic properties of the operator norm',
    r'''For $S,T\in\Lin(V,W)$ and $\lambda\in\F$,
    \[
    \norm T\ge0,\qquad
    \norm T=0\Longleftrightarrow T=0,\qquad
    \norm{\lambda T}=|\lambda|\norm T,
    \]
    and
    \[
    \norm{S+T}\le\norm S+\norm T.
    \]''',
    r'''Every vector norm is nonnegative, so their maximum is nonnegative. If $T=0$, all values in its defining maximum vanish, giving $\norm T=0$. Conversely, suppose $\norm T=0$. For every nonzero $v$, the vector $u=v/\norm v$ has norm one, so $\norm{Tu}=0$ and hence $Tu=0$. Linearity gives $Tv=\norm v\,Tu=0$. Also $T0=0$, proving $T=0$.

    For $\norm v\le1$, vector norm homogeneity gives
    $\norm{\lambda Tv}=|\lambda|\norm{Tv}$. If $\lambda=0$, both sides of the proposed norm identity are zero. If $\lambda\ne0$, multiplying all the values in the defining maximum by the positive number $|\lambda|$ multiplies their maximum by that number. Thus $\norm{\lambda T}=|\lambda|\norm T$.

    Finally, for every $\norm v\le1$, the vector triangle inequality gives
    \[
    \norm{(S+T)v}\le\norm{Sv}+\norm{Tv}
    \le\norm S+\norm T.
    \]
    Taking the maximum on the left proves the last inequality. These arguments include the zero domain, where the defining set of values is $\{0\}$.''',
    2, 20,
    [r'''To prove definiteness, scale each nonzero vector to have norm one.''',
     r'''Apply the vector triangle inequality before taking a maximum.'''],
    ['def-operator-norm', 'c6-thm-norm-properties',
     'c6-thm-triangle-inequality', 'c3-thm-linear-zero',
     'c3-def-map-operations'],
    '7.87', 281,
)

s.r(
    'thm-operator-norm-formulas',
    'Equivalent descriptions of the operator norm',
    r'''For $T\in\Lin(V,W)$:
    \begin{enumerate}
    \item If $V\ne\{0\}$, then $\norm T$ is its largest singular value.
    \item If $V\ne\{0\}$, then
    \[
    \norm T=\max_{\norm v=1}\norm{Tv}.
    \]
    \item In every dimension, $\norm T$ is the least nonnegative real number $c$ such that
    \[
    \norm{Tv}\le c\norm v\qquad(v\in V).
    \]
    \end{enumerate}
    For $V=\{0\}$, the norm is zero; no maximum over the empty unit sphere is asserted.''',
    r'''The first assertion is the maximum lemma. If $T\ne0$, its proof also supplies a unit vector attaining $\norm T$, so restricting the maximum to the unit sphere does not change its value. If $T=0$ and $V\ne\{0\}$, choose any nonzero vector and normalize it; thus the unit sphere is nonempty, and all values on it are zero. This proves the second assertion.

    For the third assertion, let $v\ne0$. The norm definition and linearity give
    \[
    \norm{Tv}
    =\norm v\,\norm{T(v/\norm v)}
    \le\norm T\,\norm v.
    \]
    The same inequality holds at zero because $T0=0$. Thus $\norm T$ is an admissible nonnegative constant. If another $c\ge0$ satisfies the asserted bound, then $\norm{Tv}\le c$ whenever $\norm v\le1$. Taking the maximum yields $\norm T\le c$, proving minimality. This argument also applies when $V=\{0\}$; restricting $c$ to nonnegative numbers then makes the least value zero.''',
    2, 20,
    [r'''Normalize a nonzero vector.''',
     r'''An admissible nonnegative constant bounds all values on the closed unit ball.'''],
    ['def-operator-norm', 'lem-operator-norm-maximum',
     'thm-operator-norm-properties', 'c6-thm-norm-properties',
     'c3-thm-linear-zero'],
    '7.88', 282,
)

s.r(
    'ex-identity-norm',
    'The norm of the identity',
    r'''The identity on a nonzero inner product space has norm one. On the zero space its norm is zero.''',
    r'''For a nonzero domain, $\norm{Iv}=\norm v\le1$ throughout the closed unit ball. A unit vector exists by normalizing a nonzero vector, and its image has norm one. Thus the maximum is one. On the zero space the identity sends its only vector to zero, so its norm is zero.''',
    1, 10,
    [r'''Use a unit vector to attain the upper bound.'''],
    ['def-operator-norm', 'c3-def-zero-identity-maps',
     'c6-thm-norm-properties'],
    '7.90(a)', 283, 'example',
)

s.r(
    'ex-all-ones-norm',
    'The norm of the all-ones matrix',
    r'''Let $T\in\Lin(\F^n)$ have every standard matrix entry equal to one. Then $\norm T=n$, including $n=0$.''',
    r'''For $n=0$, the domain is zero and the norm is zero. Suppose $n>0$, and put $a=(1,\ldots,1)$. Then $\norm a=\sqrt n$ and
    \[
    Tv=(v_1+\cdots+v_n)a=\ip{v}{a}a.
    \]
    Cauchy--Schwarz gives
    \[
    \norm{Tv}=|\ip{v}{a}|\sqrt n
    \le\norm v\,\norm a\sqrt n=n\norm v.
    \]
    Therefore $\norm T\le n$. The vector $u=a/\sqrt n$ has norm one and satisfies $Tu=nu$. Hence $\norm{Tu}=n$, giving the reverse inequality and the conclusion.''',
    2, 15,
    [r'''Express the map using the vector whose coordinates are all one.''',
     r'''Use that same direction to attain the norm bound.'''],
    ['thm-operator-norm-formulas', 'c6-thm-standard-inner-product',
     'c6-thm-cauchy-schwarz', 'c6-thm-norm-properties',
     'c3-thm-matrix-action'],
    '7.90(b)', 283, 'example',
)

s.r(
    'ex-orthonormal-eigenbasis-norm',
    'Reading a norm from an orthonormal eigenbasis',
    r'''Suppose $e_1,\ldots,e_n$ is an orthonormal basis and $Te_j=\lambda_je_j$. If $n>0$, then
    \[
    \norm T=\max_{1\le j\le n}|\lambda_j|.
    \]
    If $n=0$, then $\norm T=0$. When using this formula in all dimensions, we assign the value zero to this maximum of an empty list of nonnegative numbers.''',
    r'''The zero-dimensional assertion follows from the norm definition. For $n>0$, set $M=\max_j|\lambda_j|$. Write $v=\sum_j a_je_j$. The orthonormal norm formula gives
    \[
    \norm{Tv}^2=\sum_j|\lambda_j|^2|a_j|^2
    \le M^2\sum_j|a_j|^2=M^2\norm v^2.
    \]
    Thus $\norm T\le M$. Choose $k$ with $|\lambda_k|=M$. Because $\norm{e_k}=1$ and $\norm{Te_k}=|\lambda_k|$, the norm definition gives $\norm T\ge M$.''',
    2, 15,
    [r'''Expand an arbitrary vector in the orthonormal eigenbasis.'''],
    ['thm-operator-norm-formulas', 'def-operator-norm',
     'c6-thm-orthonormal-norm', 'c2-thm-basis-coordinates'],
    '7.90(c)', 283, 'example',
)

s.r(
    'thm-inverse-norm',
    'The norm of an inverse',
    r'''Suppose $V\ne\{0\}$ and $T\in\Lin(V)$ is invertible. If $s_n$ is its smallest singular value, then $s_n>0$ and
    \[
    \norm{T^{-1}}=\frac1{s_n}.
    \]''',
    r'''Invertibility implies $\Range T=V$, so the singular-rank theorem gives $n=\dim V$ positive singular values. Choose the corresponding orthonormal bases with $Te_j=s_jf_j$. Every $w\in V$ has a unique expression $w=\sum_j b_jf_j$, and
    \[
    T^{-1}w=\sum_j\frac{b_j}{s_j}e_j.
    \]
    Consequently
    \[
    \norm{T^{-1}w}^2
    =\sum_j\frac{|b_j|^2}{s_j^2}
    \le\frac1{s_n^2}\sum_j|b_j|^2
    =\frac{\norm w^2}{s_n^2}.
    \]
    This gives $\norm{T^{-1}}\le1/s_n$. The unit vector $f_n$ has image $e_n/s_n$ under $T^{-1}$, so equality is attained.''',
    2, 20,
    [r'''Invert the equations $Te_j=s_jf_j$.'''],
    ['thm-singular-value-decomposition', 'thm-singular-rank',
     'thm-operator-norm-formulas', 'def-operator-norm',
     'c6-thm-orthonormal-norm', 'c3-thm-invertible-bijective'],
    page=283,
)

s.r(
    'ex-cauchy-type-matrix-invertible',
    'An invertible matrix with very different singular values',
    r'''The operator $T\in\Lin(\R^5)$ whose standard matrix is
    \[
    A_{jk}=\frac1{j^2+k}\qquad(1\le j,k\le5)
    \]
    is invertible.''',
    r'''Suppose $Tx=0$, where $x=(x_1,\ldots,x_5)$. Define the polynomial
    \[
    p(t)=\sum_{k=1}^5x_k
    \prod_{\substack{1\le\ell\le5\\\ell\ne k}}(t+\ell).
    \]
    Its degree is at most four unless it is zero. For each $j=1,\ldots,5$, the equation $\sum_kx_k/(j^2+k)=0$, multiplied by the nonzero number $\prod_{\ell=1}^5(j^2+\ell)$, gives $p(j^2)=0$. These are five distinct roots. The root bound therefore forces $p$ to be the zero polynomial. Evaluating at $t=-k$ gives
    \[
    0=x_k\prod_{\ell\ne k}(\ell-k).
    \]
    Each factor in this product is nonzero, so $x_k=0$. This holds for all five coordinates. Thus $\Null T=\{0\}$, and the finite-dimensional injectivity criterion makes $T$ invertible.''',
    3, 35,
    [r'''Convert a vector in the kernel into a polynomial of degree at most four.''',
     r'''Clear denominators at the five numbers $1^2,\ldots,5^2$, then evaluate the resulting zero polynomial at negative integers.'''],
    ['c3-thm-matrix-action', 'c4-thm-root-bound',
     'c4-lem-polynomial-product-degree', 'c1-lem-scalar-cancellation',
     'c3-thm-injective-null', 'c3-thm-equal-dimension-invertibility'],
    '7.90(d)', 283, 'example',
)

s.add(
    'theorem',
    'thm-numerical-norm-estimates',
    'Numerical values for the preceding matrix',
    r'''For the operator in the preceding example, numerical evaluation gives, to three significant digits,
    \[
    s_{\max}\approx0.811,\qquad
    s_{\min}\approx9.64\cdot10^{-7}.
    \]
    Consequently,
    \[
    \norm T\approx0.811,\qquad
    \norm{T^{-1}}\approx1.04\cdot10^6.
    \]''',
    page=283,
)
s.note(
    'note-numerical-norm-estimates',
    'Accepted numerical computation',
    r'''These numerical approximations are taken on faith; this module does not develop certified numerical eigenvalue computation. Their interpretation as norms follows from the operator-norm and inverse-norm formulas. No assertion about the impossibility of exact symbolic descriptions is needed.''',
    283,
)

s.r(
    'thm-adjoint-norm',
    'A map and its adjoint have the same norm',
    r'''For every $T\in\Lin(V,W)$,
    \[
    \norm{T^*}=\norm T.
    \]''',
    r'''Let $w\in W$. The adjoint identity, Cauchy--Schwarz, and the operator-norm bound give
    \[
    \norm{T^*w}^2
    =\ip{TT^*w}{w}
    \le|\ip{TT^*w}{w}|
    \le\norm{TT^*w}\norm w
    \le\norm T\,\norm{T^*w}\norm w.
    \]
    If $\norm{T^*w}>0$, divide by it to obtain
    $\norm{T^*w}\le\norm T\,\norm w$. If it is zero, the same bound holds because its right side is nonnegative. Thus $\norm T$ is an admissible nonnegative constant for $T^*$, and the least-constant formula yields $\norm{T^*}\le\norm T$. Applying this inequality to $T^*$ and using $(T^*)^*=T$ yields $\norm T\le\norm{T^*}$. Both inequalities hold even if either space is zero.''',
    2, 20,
    [r'''Write the squared norm of $T^*w$ using the adjoint identity.''',
     r'''After obtaining one inequality, apply it again to $T^*$.'''],
    ['def-adjoint', 'thm-adjoint-properties',
     'thm-operator-norm-formulas', 'c6-thm-cauchy-schwarz',
     'c6-thm-norm-properties'],
    '7.91', 283,
)

s.r(
    'thm-low-rank-approximation',
    'Optimal approximation with restricted range dimension',
    r'''Let $T\in\Lin(V,W)$ have positive singular values
    $s_1\ge\cdots\ge s_m>0$, with reduced singular value decomposition
    \[
    Tv=\sum_{j=1}^m s_j\ip{v}{e_j}f_j.
    \]
    For a nonnegative integer $k$, put $d=\min\{k,m\}$ and define
    \[
    T_kv=\sum_{j=1}^d s_j\ip{v}{e_j}f_j.
    \]
    Then $\dim\Range T_k=d$ and
    \[
    \min_{\substack{S\in\Lin(V,W)\\\dim\Range S\le k}}\norm{T-S}
    =\norm{T-T_k}
    =
    \begin{cases}
    s_{k+1},&0\le k<m,\\
    0,&k\ge m.
    \end{cases}
    \]
    Empty sums define the zero map.''',
    r'''Linearity of the inner product in its first variable shows that $T_k$ is linear. Its range is contained in $\Span(f_1,\ldots,f_d)$. For each $1\le j\le d$, the equation $T_ke_j=s_jf_j$ and $s_j>0$ show that $f_j$ is in the range. Thus the range equals this span, which has dimension $d$ because the list is orthonormal.

    If $k\ge m$, then $T_k=T$, giving error zero. Nonnegativity of every operator norm proves optimality in this case, including $m=0$.

    Suppose $0\le k<m$. For every $v$,
    \[
    \norm{(T-T_k)v}^2
    =\sum_{j=k+1}^m s_j^2|\ip{v}{e_j}|^2
    \le s_{k+1}^2\norm v^2
    \]
    by Bessel's inequality. Thus $\norm{T-T_k}\le s_{k+1}$. At the unit vector $e_{k+1}$, the image is $s_{k+1}f_{k+1}$, proving equality.

    Now take any $S$ with $\dim\Range S\le k$. The $k+1$ vectors $Se_1,\ldots,Se_{k+1}$ in $\Range S$ are linearly dependent, since an independent list cannot be longer than a basis. Choose scalars $a_1,\ldots,a_{k+1}$, not all zero, with $\sum_j a_jSe_j=0$. The vector $u=\sum_j a_je_j$ is nonzero by orthonormal independence, and $Su=0$. Consequently,
    \[
    \norm{(T-S)u}^2
    =\norm{Tu}^2
    =\sum_{j=1}^{k+1}s_j^2|a_j|^2
    \ge s_{k+1}^2\sum_{j=1}^{k+1}|a_j|^2
    =s_{k+1}^2\norm u^2.
    \]
    The operator-norm bound also gives
    $\norm{(T-S)u}\le\norm{T-S}\norm u$.
    Taking square roots and dividing by $\norm u>0$ yields
    $\norm{T-S}\ge s_{k+1}$. Since $T_k$ attains this value and satisfies the range constraint, it realizes the stated minimum. The argument also covers $k=0$, when the dependent list has one vector.''',
    4, 75,
    [r'''First bound the error left after deleting the initial singular-value terms.''',
     r'''A map with range dimension at most $k$ must kill a nonzero vector in $\Span(e_1,\ldots,e_{k+1})$.''',
     r'''Compare the action of $T$ on that vector with the $(k+1)$st singular value.'''],
    ['thm-singular-value-decomposition', 'thm-operator-norm-formulas',
     'thm-operator-norm-properties', 'def-operator-norm',
     'c6-thm-inner-product-properties', 'c6-thm-orthonormal-norm',
     'c6-thm-orthonormal-independent', 'c6-thm-bessel',
     'c2-thm-independent-length', 'c2-def-dimension',
     'c3-thm-range-subspace'],
    '7.92', 284,
)

s.p(
    'intro-polar-decomposition',
    'Separating a unitary factor from a positive factor',
    r'''A nonzero complex number is its modulus multiplied by a scalar of modulus one. Polar decomposition gives an operator version of that factorization, with $\sqrt{T^*T}$ playing the role of the modulus.''',
    285,
)

s.r(
    'thm-polar-decomposition',
    'Polar decomposition',
    r'''For every $T\in\Lin(V)$ there is a unitary operator $S\in\Lin(V)$ such that
    \[
    T=S\sqrt{T^*T}.
    \]''',
    r'''Choose a reduced singular value decomposition
    \[
    Tv=\sum_{j=1}^m s_j\ip{v}{e_j}f_j
    \]
    and extend both orthonormal lists to orthonormal bases
    $e_1,\ldots,e_n$ and $f_1,\ldots,f_n$ of $V$.
    Define $S$ by $Se_j=f_j$ on this basis. It sends an orthonormal basis to an orthonormal basis, so the unitary equivalences show that $S$ is unitary.

    Define $R$ on the $e$-basis by $Re_j=s_je_j$ for $j\le m$ and $Re_j=0$ for $j>m$. Its matrix in that orthonormal basis is real diagonal, so $R$ is self-adjoint. For $v=\sum_j a_je_j$,
    \[
    \ip{Rv}{v}=\sum_{j=1}^m s_j|a_j|^2\ge0.
    \]
    Thus $R$ is positive.

    For $j\le m$ and arbitrary $v$, the singular value formula gives
    \[
    \ip{Tv}{f_j}=s_j\ip{v}{e_j}
    =\ip{v}{s_je_j},
    \]
    since $s_j$ is real. Uniqueness in the adjoint identity therefore gives $T^*f_j=s_je_j$. Also $Te_j=0$ for $j>m$, directly from the singular value formula. Hence
    $T^*Te_j=s_j^2e_j=R^2e_j$ for $j\le m$, and both sides vanish for $j>m$.
    Equality on a basis proves $R^2=T^*T$. Because $R$ is positive, uniqueness of the positive square root yields $R=\sqrt{T^*T}$.

    Finally $SRe_j=Te_j$ for every basis vector, so $SR=T$. For $n=0$, both bases are empty; their basis prescription gives the unique operator, which is the identity and is unitary on the zero space. The same equalities remain valid.''',
    3, 45,
    [r'''Extend both singular-vector lists to orthonormal bases.''',
     r'''Map the domain singular basis to the target singular basis.''',
     r'''Identify the positive square root by checking its square and positivity.'''],
    ['thm-singular-value-decomposition', 'thm-unitary-equivalences',
     'thm-self-adjoint-tests', 'def-positive',
     'thm-positive-square-root-unique', 'def-positive-square-root',
     'def-adjoint', 'lem-adjoint-existence',
     'c6-thm-orthonormal-extension', 'c6-thm-orthonormal-coordinates',
     'c3-thm-linear-map-basis'],
    '7.93', 286,
)

s.r(
    'thm-polar-common-eigenbasis',
    'When the polar factors can share an orthonormal eigenbasis',
    r'''On a complex inner product space, $T$ is normal if and only if there is a polar decomposition
    \[
    T=S\sqrt{T^*T}
    \]
    for which $S$ and $\sqrt{T^*T}$ have diagonal matrices in the same orthonormal basis.''',
    r'''Suppose $T$ is normal. The complex spectral theorem supplies an orthonormal basis with $Te_j=\lambda_je_j$. The adjoint-matrix formula gives $T^*e_j=\overline{\lambda_j}e_j$. Hence $T^*Te_j=|\lambda_j|^2e_j$. The operator defined by $Re_j=|\lambda_j|e_j$ is positive and has square $T^*T$, so $R=\sqrt{T^*T}$ by uniqueness.

    Set $\mu_j=\lambda_j/|\lambda_j|$ when $\lambda_j\ne0$, and set $\mu_j=1$ when $\lambda_j=0$. Define $Se_j=\mu_je_j$. Every $|\mu_j|=1$, so $Se_1,\ldots,Se_n$ is an orthonormal basis and $S$ is unitary. The identity $\mu_j|\lambda_j|=\lambda_j$ at every index shows that $SR=T$. Both factors are diagonal in the chosen basis.

    Conversely, suppose both factors are diagonal in one orthonormal basis. Their product is diagonal in that basis, because applying the two diagonal maps successively multiplies the corresponding diagonal entries. Thus $T$ is diagonal in an orthonormal basis, and the complex spectral theorem makes it normal. For the zero space all lists are empty and the construction still applies.''',
    3, 35,
    [r'''For a normal operator, separate each eigenvalue into a modulus and a unit-modulus factor.''',
     r'''At a zero eigenvalue, choose the unit-modulus factor to be one.'''],
    ['thm-complex-spectral', 'thm-adjoint-matrix',
     'def-positive', 'thm-self-adjoint-tests',
     'thm-positive-square-root-unique', 'thm-unitary-equivalences',
     'c3-thm-linear-map-basis', 'c4-thm-complex-properties'],
    page=286,
)

s.d(
    'def-ball',
    'The open unit ball',
    r'''The open unit ball of $V$ is
    \[
    B=\{v\in V:\norm v<1\}.
    \]
    In particular, the open unit ball of the zero space is $\{0\}$.''',
    '7.95', 287,
)

s.d(
    'def-ellipsoid',
    'Ellipsoids and their principal axes',
    r'''Let $f_1,\ldots,f_n$ be an orthonormal basis and let $s_1,\ldots,s_n$ be positive real numbers. Define
    \[
    E(s_1f_1,\ldots,s_nf_n)
    =
    \left\{v\in V:
    \sum_{j=1}^n\frac{|\ip{v}{f_j}|^2}{s_j^2}<1
    \right\}.
    \]
    This is the ellipsoid with principal axes $s_1f_1,\ldots,s_nf_n$. The empty sum gives $E()=\{0\}$ when $V=\{0\}$.''',
    '7.96', 287,
)

s.r(
    'ex-ellipsoid-equations',
    'Coordinate descriptions of ellipsoids',
    r'''In standard real coordinate spaces:
    \begin{enumerate}
    \item For the standard basis $f_1,f_2$ of $\R^2$,
    \[
    E(2f_1,f_2)=\{(x,y):x^2/4+y^2<1\}.
    \]
    \item For $f_1=(1,1)/\sqrt2$ and $f_2=(-1,1)/\sqrt2$,
    \[
    E(2f_1,f_2)
    =
    \{(x,y):(x+y)^2/8+(y-x)^2/2<1\}.
    \]
    \item For the standard basis of $\R^3$,
    \[
    E(4f_1,3f_2,2f_3)
    =\{(x,y,z):x^2/16+y^2/9+z^2/4<1\}.
    \]
    \end{enumerate}
    Moreover, $E(f_1,\ldots,f_n)=B$ for every orthonormal basis of any $V$.''',
    r'''The standard coordinate vectors are orthonormal, and their inner products with a vector are its coordinates. Substitution into the definition gives the first and third equations. For the second equation, the two displayed vectors each have squared norm $(1+1)/2=1$ and have inner product $(-1+1)/2=0$. They form a basis because an orthonormal list of length two in $\R^2$ is a basis. Their inner products with $(x,y)$ are $(x+y)/\sqrt2$ and $(y-x)/\sqrt2$. Dividing the first squared inner product by $2^2$ and the second by $1^2$ gives the asserted equation.

    Finally, Parseval's identity gives
    $\sum_j|\ip{v}{f_j}|^2=\norm v^2$. Thus the defining inequality for $E(f_1,\ldots,f_n)$ is exactly $\norm v^2<1$, equivalent to $\norm v<1$. This includes the empty basis.''',
    1, 10,
    [r'''Insert the relevant inner products into the ellipsoid definition.'''],
    ['def-ellipsoid', 'def-ball', 'c6-thm-standard-inner-product',
     'c6-thm-full-orthonormal', 'c6-thm-orthonormal-coordinates'],
    '7.97', 287, 'example',
)

s.d(
    'def-set-image',
    'The image of a subset',
    r'''If $T$ is a function on $V$ and $\Omega\subseteq V$, write
    \[
    T(\Omega)=\{Tv:v\in\Omega\}.
    \]''',
    '7.98', 288,
)

s.r(
    'thm-ball-ellipsoid',
    'An invertible operator sends the ball onto an ellipsoid',
    r'''Let $T\in\Lin(V)$ be invertible, and choose a singular value decomposition
    \[
    Tv=\sum_{j=1}^n s_j\ip{v}{e_j}f_j
    \]
    with orthonormal bases on both sides. Then every $s_j>0$ and
    \[
    T(B)=E(s_1f_1,\ldots,s_nf_n).
    \]''',
    r'''Invertibility implies $\dim\Range T=\dim V=n$, so the singular-rank theorem gives $n$ positive singular values. The singular vectors on both sides therefore form orthonormal bases.

    If $v\in B$, orthonormality gives
    $\ip{Tv}{f_j}=s_j\ip{v}{e_j}$. Consequently
    \[
    \sum_j\frac{|\ip{Tv}{f_j}|^2}{s_j^2}
    =\sum_j|\ip{v}{e_j}|^2
    =\norm v^2<1,
    \]
    so $Tv$ belongs to the asserted ellipsoid.

    Conversely, let $w$ belong to that ellipsoid and set
    \[
    v=\sum_j\frac{\ip{w}{f_j}}{s_j}e_j.
    \]
    The orthonormal norm formula gives
    $\norm v^2=\sum_j|\ip{w}{f_j}|^2/s_j^2<1$.
    Applying $T$ to this expansion gives
    $Tv=\sum_j\ip{w}{f_j}f_j=w$ by orthonormal coordinates.
    Thus $w\in T(B)$, proving equality. For $n=0$, both sets are $\{0\}$ and the sums are empty.''',
    2, 20,
    [r'''Calculate the ellipsoid expression at $Tv$.''',
     r'''For the reverse inclusion, divide the target coordinates by their singular values.'''],
    ['thm-singular-value-decomposition', 'thm-singular-rank',
     'def-ball', 'def-ellipsoid', 'def-set-image',
     'c3-thm-invertible-bijective', 'c6-thm-orthonormal-coordinates',
     'c6-thm-orthonormal-norm'],
    '7.99', 288,
)

s.r(
    'thm-ellipsoid-image',
    'Invertible operators preserve the class of ellipsoids',
    r'''If $T\in\Lin(V)$ is invertible and $E$ is an ellipsoid, then $T(E)$ is an ellipsoid.''',
    r'''Write $E=E(r_1g_1,\ldots,r_ng_n)$, where the $g_j$ form an orthonormal basis and every $r_j>0$. Define $Dg_j=r_jg_j$. The prescription $D^{-1}g_j=g_j/r_j$ gives a two-sided inverse on each basis vector and hence on every vector.

    For $v=\sum_j a_jg_j$, one has
    \[
    \sum_j\frac{|\ip{Dv}{g_j}|^2}{r_j^2}
    =\sum_j|a_j|^2=\norm v^2.
    \]
    Conversely, a vector $\sum_j b_jg_j$ in $E$ is the image under $D$ of $\sum_j(b_j/r_j)g_j$, whose squared norm is less than one. These two statements show $D(B)=E$.

    The operator $TD$ is invertible, with inverse $D^{-1}T^{-1}$, as direct composition verifies. Therefore the ball-to-ellipsoid theorem applies to $TD$, and
    $T(E)=T(D(B))=(TD)(B)$ is an ellipsoid. Empty bases yield the same conclusion on the zero space.''',
    2, 20,
    [r'''Express the given ellipsoid as a diagonal stretching of the unit ball.'''],
    ['def-ellipsoid', 'def-set-image', 'thm-ball-ellipsoid',
     'c3-thm-linear-map-basis', 'c3-thm-composition-laws',
     'c6-thm-orthonormal-coordinates'],
    '7.101', 289,
)

s.p(
    'intro-real-parallelepipeds',
    'Boxes and their images',
    r'''For the geometric and volume discussion that follows, take $V$ to be a real inner product space. Coefficients in the interval $(0,1)$ describe the interior of a parallelepiped.''',
    289,
)

s.d(
    'def-parallelepiped',
    'Parallelepipeds and edges',
    r'''For a basis $v_1,\ldots,v_n$ of a real vector space, define
    \[
    P(v_1,\ldots,v_n)
    =
    \left\{\sum_{j=1}^n a_jv_j:0<a_j<1\text{ for every }j\right\}.
    \]
    A parallelepiped is a translate $u+P(v_1,\ldots,v_n)$; its displayed edges are $v_1,\ldots,v_n$. In dimension zero, $P()=\{0\}$.''',
    '7.102', 289,
)

s.r(
    'ex-parallelepiped-coordinates',
    'A translated parallelogram in coordinates',
    r'''In $\R^2$,
    \[
    (3/10,1/2)+P((1,0),(1,1))
    =
    \{(x,y):1/2<y<3/2,\ -1/5<x-y<4/5\}.
    \]''',
    r'''The two edge vectors form a basis: every $(x,y)$ equals $(x-y)(1,0)+y(1,1)$, and these coefficients are forced by the second and then the first coordinate. A point in the displayed parallelepiped has the form
    \[
    (x,y)=(3/10+a+b,\ 1/2+b),\qquad0<a,b<1.
    \]
    Thus $b=y-1/2$ and $a=x-y+1/5$. The restrictions on $b$ are exactly $1/2<y<3/2$, and those on $a$ are exactly $-1/5<x-y<4/5$. Conversely, these inequalities produce parameters $a,b$ in $(0,1)$ through the same formulas and hence produce a point of the parallelepiped.''',
    1, 10,
    [r'''Solve for the two edge coefficients in terms of $x$ and $y$.'''],
    ['def-parallelepiped', 'c1-def-coordinate-space',
     'c2-def-basis'],
    '7.103', 289, 'example',
)

s.r(
    'thm-parallelepiped-image',
    'Images of parallelepipeds',
    r'''If $T\in\Lin(V)$ is invertible and $v_1,\ldots,v_n$ is a basis, then
    \[
    T\bigl(u+P(v_1,\ldots,v_n)\bigr)
    =Tu+P(Tv_1,\ldots,Tv_n),
    \]
    and the set on the right is a parallelepiped.''',
    r'''The images $Tv_1,\ldots,Tv_n$ form a basis under the isomorphism $T$. Linearity gives
    \[
    T\left(u+\sum_j a_jv_j\right)
    =Tu+\sum_j a_jTv_j
    \]
    for every choice of coefficients. Taking all choices with $0<a_j<1$ gives inclusion of the left set in the right set. Each vector in the right set comes from exactly such a choice of coefficients and is the image of the corresponding vector $u+\sum_j a_jv_j$, proving the reverse inclusion. Because the image edges form a basis, the result is a parallelepiped by definition. The same reasoning applies to an empty list of edges.''',
    1, 10,
    [r'''Apply linearity to a point written using its edge coefficients.'''],
    ['def-parallelepiped', 'def-set-image',
     'c3-lem-isomorphism-basis', 'c3-def-isomorphism'],
    '7.104', 290,
)

s.d(
    'def-box',
    'Boxes',
    r'''A box in a real inner product space is a set of the form
    \[
    u+P(r_1e_1,\ldots,r_ne_n),
    \]
    where $e_1,\ldots,e_n$ is an orthonormal basis and $r_1,\ldots,r_n$ are positive real numbers. Its edge lengths are the $r_j$.''',
    '7.105', 290,
)

s.r(
    'ex-box-coordinates',
    'A rotated square and a rectangular box',
    r'''Let $e_1=(1,1)/\sqrt2$ and $e_2=(-1,1)/\sqrt2$ in $\R^2$. Then
    \[
    (1,0)+P(\sqrt2e_1,\sqrt2e_2)
    =
    \{(x,y):1<x+y<3,\ -1<y-x<1\}.
    \]
    In $\R^3$, with standard basis $g_1,g_2,g_3$,
    \[
    P(g_1,2g_2,g_3)
    =\{(x,y,z):0<x<1,\ 0<y<2,\ 0<z<1\}.
    \]
    Both sets are boxes.''',
    r'''The vectors $e_1,e_2$ are orthonormal, as verified in the ellipsoid example. A point in the first set has coordinates
    \[
    (x,y)=(1+a-b,\ a+b),\qquad0<a,b<1.
    \]
    Solving gives $a=(x+y-1)/2$ and $b=(y-x+1)/2$. Thus the coefficient restrictions are equivalent to the asserted inequalities, in both directions. Its edge lengths are $\sqrt2,\sqrt2$, so it is a box.

    A point in the second set is $(a,2b,c)$ with $0<a,b,c<1$. These inequalities are equivalent to the three displayed coordinate inequalities. Its edges are positive multiples of the standard orthonormal basis, so it too is a box.''',
    1, 10,
    [r'''Write each point using the displayed edge vectors, then solve for the coefficients.'''],
    ['def-box', 'def-parallelepiped', 'ex-ellipsoid-equations',
     'c6-thm-standard-inner-product'],
    '7.106', 290, 'example',
)

s.r(
    'thm-svd-boxes',
    'Singular directions give boxes whose images are boxes',
    r'''Suppose $T\in\Lin(V)$ is invertible and $Te_j=s_jf_j$ in a singular value decomposition with orthonormal bases. For positive numbers $r_1,\ldots,r_n$,
    \[
    T\bigl(u+P(r_1e_1,\ldots,r_ne_n)\bigr)
    =
    Tu+P(r_1s_1f_1,\ldots,r_ns_nf_n).
    \]
    Both sets are boxes.''',
    r'''Invertibility makes every singular value positive. The vectors $r_je_j$ are a basis: multiplying an orthonormal basis by nonzero scalars preserves its unique coordinate expansions. The parallelepiped-image theorem therefore gives the displayed identity, since $T(r_je_j)=r_js_jf_j$. The original edges have positive lengths $r_j$ along an orthonormal basis, so the original set is a box. The image edges have positive lengths $r_js_j$ along the orthonormal basis $f_1,\ldots,f_n$, so the image is also a box. When $n=0$, both sets are the singleton zero space.''',
    1, 10,
    [r'''Use $T(r_je_j)=r_js_jf_j$ in the parallelepiped-image formula.'''],
    ['thm-parallelepiped-image', 'thm-singular-rank',
     'thm-singular-value-decomposition', 'def-box',
     'c2-thm-basis-coordinates'],
    '7.107', 291,
)

s.d(
    'def-box-volume',
    'The assigned volume of a box',
    r'''For a real box with orthogonal edge lengths $r_1,\ldots,r_n$, its volume is
    \[
    \Vol\bigl(u+P(r_1e_1,\ldots,r_ne_n)\bigr)
    =\prod_{j=1}^n r_j.
    \]
    The empty product is one, so the singleton zero space has zero-dimensional volume one. The analytic prerequisite below guarantees that this assignment depends on the set, rather than its presentation as a box, and agrees with the general volume definition.''',
    '7.108', 291,
)

s.d(
    'def-volume',
    'Lebesgue measurable sets and volume',
    r'''For $n>0$ and $A\subseteq\R^n$, define its Lebesgue outer measure by
    \[
    m_n^*(A)
    =
    \inf\left\{
    \sum_{k=1}^{\infty}\prod_{j=1}^n(b_{kj}-a_{kj}):
    A\subseteq\bigcup_{k=1}^{\infty}
    \prod_{j=1}^n(a_{kj},b_{kj})
    \right\},
    \]
    where all endpoints are finite real numbers with $a_{kj}<b_{kj}$; finite or empty covers are allowed. The sums and infimum may have value $+\infty$. A subset $A$ is Lebesgue measurable when, for every $E\subseteq\R^n$,
    \[
    m_n^*(E)=m_n^*(E\cap A)+m_n^*(E\setminus A).
    \]
    For such $A$, write $m_n(A)=m_n^*(A)$. In $\R^0=\{0\}$, both subsets are measurable, with $m_0(\varnothing)=0$ and $m_0(\{0\})=1$.

    For a real $n$-dimensional inner product space, choose an orthonormal basis $\mathcal E=(e_1,\ldots,e_n)$ and let
    \[
    C_{\mathcal E}(v)=(\ip{v}{e_1},\ldots,\ip{v}{e_n}).
    \]
    A subset $\Omega\subseteq V$ is measurable if $C_{\mathcal E}(\Omega)$ is Lebesgue measurable, and its volume is
    \[
    \Vol(\Omega)=m_n(C_{\mathcal E}(\Omega)).
    \]
    The next analytic result makes both notions independent of the chosen orthonormal basis.''',
    '7.109', 292,
)

s.add(
    'theorem',
    'thm-lebesgue-prerequisites',
    'Analytic facts used for volume',
    r'''For the preceding definition of Lebesgue measure:
    \begin{enumerate}
    \item Every open subset of $\R^n$ is measurable, and
    \[
    m_n\left(\prod_{j=1}^n(a_j,b_j)\right)
    =\prod_{j=1}^n(b_j-a_j).
    \]
    \item If $Q$ is a real orthogonal linear map on $\R^n$ and $a\in\R^n$, then $A$ is measurable if and only if $a+Q(A)$ is measurable; for measurable $A$,
    \[
    m_n(a+Q(A))=m_n(A).
    \]
    Here orthogonal means that $Q$ preserves the standard inner product.
    \item If $D(x_1,\ldots,x_n)=(d_1x_1,\ldots,d_nx_n)$ with every $d_j>0$, then $A$ is measurable if and only if $D(A)$ is measurable; for measurable $A$,
    \[
    m_n(D(A))=\left(\prod_{j=1}^n d_j\right)m_n(A).
    \]
    \end{enumerate}
    These assertions include dimension zero with the preceding conventions. Multiplication of $+\infty$ by a positive number has value $+\infty$.''',
    page=292,
)
s.note(
    'note-volume-prerequisites',
    'Accepted analysis behind volume',
    r'''The analytic facts just stated are taken on faith. Their proofs belong to measure theory, which is outside this module. In particular, finite collections of approximating boxes alone do not supply a proof for arbitrary measurable sets; the linear-algebraic arguments below use the stated analytic theorem explicitly.''',
    292,
)

s.r(
    'lem-volume-well-defined',
    'Orthonormal coordinates define volume consistently',
    r'''Measurability and volume in a real inner product space do not depend on the orthonormal basis used in their definition. The general volume definition gives each box the product of its orthogonal edge lengths.''',
    r'''Let $\mathcal E$ and $\mathcal F$ be two orthonormal bases. The coordinate maps are linear bijections by the orthonormal expansion theorem. The transition
    $Q=C_{\mathcal F}C_{\mathcal E}^{-1}$ preserves the standard inner product: for vectors $v,w\in V$, the orthonormal coordinate formula says that both coordinate inner products equal $\ip{v}{w}$. Thus $Q$ is orthogonal. Since
    $C_{\mathcal F}(\Omega)=Q(C_{\mathcal E}(\Omega))$,
    orthogonal invariance in the accepted analytic theorem proves both the equivalence of measurability and equality of the two volumes.

    For a box $u+P(r_1e_1,\ldots,r_ne_n)$, use its own orthonormal edge basis. Its coordinate image is the rectangle
    \[
    \prod_{j=1}^n
    \bigl(\ip{u}{e_j},\ip{u}{e_j}+r_j\bigr).
    \]
    The rectangle formula gives volume $\prod_jr_j$. Basis independence shows that this value is its volume in every orthonormal coordinate system. This also proves that two presentations of the same box give the same product. In dimension zero the only box is the singleton, whose volume and empty product are both one.''',
    2, 20,
    [r'''The transition between two orthonormal coordinate systems is orthogonal.''',
     r'''Compute a box in coordinates aligned with its own edges.'''],
    ['def-volume', 'def-box-volume', 'def-box',
     'thm-lebesgue-prerequisites', 'c6-thm-orthonormal-coordinates',
     'c3-thm-composition-laws'],
    page=292, kind='lemma',
)

s.r(
    'ex-box-volumes',
    'Volumes of the two coordinate boxes',
    r'''Each box in the preceding box example has volume two.''',
    r'''The first box has edge lengths $\sqrt2,\sqrt2$, whose product is two. The second has edge lengths $1,2,1$, whose product is also two. The box-volume formula therefore gives the claimed volumes.''',
    1, 10,
    [r'''Multiply the orthogonal edge lengths.'''],
    ['ex-box-coordinates', 'lem-volume-well-defined'],
    page=292, kind='example',
)

s.r(
    'ex-planar-volume-stretch',
    'Doubling one coordinate doubles area',
    r'''Let $T:\R^2\to\R^2$ be given by $T(x,y)=(2x,y)$. For every Lebesgue measurable $\Omega\subseteq\R^2$,
    \[
    \Vol(T(\Omega))=2\Vol(\Omega).
    \]
    In particular, $T$ takes the unit ball onto
    $\{(x,y):x^2/4+y^2<1\}$, and this ellipsoid has twice the volume of the ball.''',
    r'''In the standard orthonormal coordinates, $T$ is the positive diagonal scaling with factors two and one. The accepted diagonal-scaling theorem gives measurability of the image and multiplies its volume by $2\cdot1=2$.

    A point $(x,y)$ is in $T(B)$ exactly when its unique preimage $(x/2,y)$ satisfies $(x/2)^2+y^2<1$. This proves the asserted ellipsoid description. The ball is open and therefore measurable by the accepted analytic theorem, so the volume identity applies to it.''',
    1, 10,
    [r'''Use the accepted diagonal-scaling formula in standard coordinates.'''],
    ['def-volume', 'thm-lebesgue-prerequisites', 'def-ball',
     'def-set-image', 'c6-thm-standard-inner-product'],
    '7.110', 292, 'example',
)

s.r(
    'thm-volume-scaling',
    'Singular values determine the volume multiplier',
    r'''Let $V$ be a finite-dimensional real inner product space, let $T\in\Lin(V)$ be invertible, and let $\Omega\subseteq V$ be Lebesgue measurable in orthonormal coordinates. Then $T(\Omega)$ is measurable and
    \[
    \Vol(T(\Omega))
    =
    \left(\prod_{j=1}^n s_j\right)\Vol(\Omega),
    \]
    where $s_1,\ldots,s_n$ are all singular values of $T$. The identity holds for finite or infinite volume and for $n=0$, with empty product one.''',
    r'''Invertibility gives a singular value decomposition with positive singular values and orthonormal bases:
    \[
    Tv=\sum_{j=1}^n s_j\ip{v}{e_j}f_j.
    \]
    Let $C_{\mathcal E}$ and $C_{\mathcal F}$ be the corresponding orthonormal coordinate maps. If
    $D(x_1,\ldots,x_n)=(s_1x_1,\ldots,s_nx_n)$, the singular value formula gives the identity of linear maps
    \[
    C_{\mathcal F}T=DC_{\mathcal E}.
    \]
    Hence
    \[
    C_{\mathcal F}(T(\Omega))
    =D(C_{\mathcal E}(\Omega)).
    \]
    Measurability of $\Omega$ makes the set on the right an image of a measurable set under positive diagonal scaling. The accepted analytic theorem therefore makes it measurable and gives
    \[
    m_n(C_{\mathcal F}(T(\Omega)))
    =
    \left(\prod_j s_j\right)m_n(C_{\mathcal E}(\Omega)).
    \]
    Basis independence of volume identifies the two measures with the required volumes. Each $s_j$ is positive, so the accepted scaling formula also covers infinite volume without a product of zero and infinity. In dimension zero, the coordinate maps and $D$ are the identity on a singleton, and the same statement holds for each of its two subsets.''',
    3, 30,
    [r'''Use the right singular vectors as domain coordinates and the left singular vectors as target coordinates.''',
     r'''In these two orthonormal coordinate systems, the map is positive diagonal scaling.'''],
    ['thm-singular-value-decomposition', 'thm-singular-rank',
     'def-volume', 'lem-volume-well-defined',
     'thm-lebesgue-prerequisites', 'def-set-image',
     'c3-thm-invertible-bijective'],
    '7.111', 293,
)

s.d(
    'def-skew-adjoint',
    'Skew-adjoint operators',
    r'''An operator $T$ on an inner product space is skew-adjoint, or skew, if
    \[
    T^*=-T.
    \]''',
    page=293,
)

s.r(
    'thm-normal-eigenvalue-classification',
    'Seven properties read from the eigenvalues of a normal operator',
    r'''Let $T$ be a normal operator on a finite-dimensional complex inner product space. Each property below is equivalent to the indicated condition on every eigenvalue $\lambda$ of $T$:
    \begin{enumerate}
    \item $T$ is invertible if and only if $\lambda\ne0$.
    \item $T$ is self-adjoint if and only if $\lambda\in\R$.
    \item $T$ is skew-adjoint if and only if $\operatorname{Re}\lambda=0$.
    \item $T$ is an orthogonal projection onto some subspace if and only if $\lambda\in\{0,1\}$.
    \item $T$ is positive if and only if $\lambda\ge0$.
    \item $T$ is unitary if and only if $|\lambda|=1$.
    \item $\norm T<1$ if and only if $|\lambda|<1$.
    \end{enumerate}
    All statements include the zero space, where eigenvalue conditions are vacuous and $\norm T=0$. The invertibility equivalence in fact holds for every finite-dimensional operator, without normality.''',
    r'''Choose an orthonormal eigenbasis $e_1,\ldots,e_n$ using the complex spectral theorem, and write $Te_j=\lambda_je_j$. The adjoint-matrix formula gives
    $T^*e_j=\overline{\lambda_j}e_j$.

    If some $\lambda_j=0$, then $T$ has a nonzero kernel vector and is not invertible. If every $\lambda_j\ne0$, the prescription $Re_j=\lambda_j^{-1}e_j$ defines a linear map and gives $RT=TR=I$ on the basis, hence everywhere. More generally, without normality, zero is an eigenvalue exactly when the kernel contains a nonzero vector; finite-dimensional injectivity is equivalent to invertibility. This proves the first row and its extra assertion.

    For the second row, $T=T^*$ holds exactly when $\lambda_j=\overline{\lambda_j}$ for every basis vector, which is equivalent to all $\lambda_j$ being real. For the third row, $T^*=-T$ holds exactly when $\overline{\lambda_j}=-\lambda_j$ for every $j$. Since $\lambda_j+\overline{\lambda_j}=2\operatorname{Re}\lambda_j$, this is equivalent to vanishing real parts.

    For the fourth row, suppose first $T=P_U$ is an orthogonal projection. Its identity $P_U^2=P_U$ gives
    $\lambda_j^2e_j=\lambda_je_j$ on each eigenvector. Since $e_j\ne0$, the scalar equation $\lambda_j(\lambda_j-1)=0$ forces $\lambda_j\in\{0,1\}$. Conversely, assume every $\lambda_j$ is zero or one. Let $U$ be the span of those $e_j$ with eigenvalue one. That sublist is an orthonormal basis of $U$, including the empty sublist if $U=\{0\}$. The orthogonal projection formula gives
    \[
    P_Uv=\sum_{\lambda_j=1}\ip{v}{e_j}e_j
    =\sum_j\lambda_j\ip{v}{e_j}e_j=Tv.
    \]
    Thus $T=P_U$.

    For the fifth row, positivity implies self-adjointness, and its eigenvalue characterization makes every $\lambda_j$ nonnegative. Conversely, if every $\lambda_j$ is nonnegative, the second row makes $T$ self-adjoint, and for $v=\sum_ja_je_j$,
    \[
    \ip{Tv}{v}=\sum_j\lambda_j|a_j|^2\ge0.
    \]
    Thus $T$ is positive by definition.

    For the sixth row, a unitary operator preserves norms, so
    $|\lambda_j|=\norm{\lambda_je_j}=\norm{Te_j}=\norm{e_j}=1$.
    Conversely, if all $|\lambda_j|=1$, the list
    $\lambda_1e_1,\ldots,\lambda_ne_n$ is an orthonormal basis. The unitary equivalences therefore make $T$ unitary.

    For the last row and $n>0$, the eigenbasis norm formula gives
    $\norm T=\max_j|\lambda_j|$. A finite maximum is less than one exactly when each entry is less than one. If $n=0$, the norm is zero, so the claimed strict inequality holds. In that case the unique operator is the identity and its own inverse, adjoint, and negative; it is the projection onto $\{0\}$, is positive, and is unitary. Thus every other row also agrees with its vacuous eigenvalue condition.''',
    3, 45,
    [r'''Use one orthonormal eigenbasis throughout and note the corresponding diagonal entries of the adjoint.''',
     r'''For the projection row, first use idempotence; for the converse, span the eigenvectors with eigenvalue one.''',
     r'''Use the orthonormal-eigenbasis norm formula for the final row.'''],
    ['thm-complex-spectral', 'thm-adjoint-matrix',
     'def-self-adjoint', 'def-skew-adjoint', 'def-positive',
     'thm-positive-characterizations', 'thm-unitary-equivalences',
     'def-unitary', 'def-isometry',
     'ex-orthonormal-eigenbasis-norm',
     'c6-thm-projection-properties', 'c6-thm-orthonormal-coordinates',
     'c6-thm-orthonormal-independent', 'c6-thm-norm-properties',
     'c3-thm-linear-map-basis', 'c3-thm-injective-null',
     'c3-thm-equal-dimension-invertibility',
     'c5-def-eigenvalue', 'c4-thm-complex-properties',
     'c1-lem-scalar-cancellation'],
    page=293,
)

s.card(
    'operator-norm',
    'def-operator-norm',
    r'''How is the norm of a linear map defined, including when its domain is zero?''',
    r'''$\norm T=\max_{\norm v\le1}\norm{Tv}$. For a zero domain the defining set of values is $\{0\}$, so the norm is zero.''',
)

s.card(
    'operator-norm-formulas',
    'thm-operator-norm-formulas',
    r'''What is the sharp constant in $\norm{Tv}\le c\norm v$? When may one maximize over the unit sphere?''',
    r'''The least nonnegative such $c$ is $\norm T$. The unit-sphere maximum formula requires a nonzero domain.''',
)

s.card(
    'adjoint-norm',
    'thm-adjoint-norm',
    r'''How do $\norm{T^*}$ and $\norm T$ compare?''',
    r'''They are equal. Bound $\norm{T^*w}^2$ using the adjoint identity and Cauchy--Schwarz, then apply the resulting inequality to $T^*$ as well.''',
)

s.card(
    'low-rank-approximation',
    'thm-low-rank-approximation',
    r'''What is the smallest operator-norm error when approximating a rank-$m$ map by maps of range dimension at most $k<m$?''',
    r'''It is $s_{k+1}$, attained by retaining the first $k$ terms of a singular value decomposition.''',
)

s.card(
    'low-rank-lower-bound',
    'thm-low-rank-approximation',
    r'''What supplies the lower bound in the optimal approximation theorem?''',
    r'''Any map with range dimension at most $k$ kills a nonzero vector in the span of the first $k+1$ right singular vectors. On that span, $T$ stretches every vector by at least $s_{k+1}$.''',
)

s.card(
    'polar-decomposition',
    'thm-polar-decomposition',
    r'''State polar decomposition and identify the positive factor.''',
    r'''Every $T\in\Lin(V)$ has $T=S\sqrt{T^*T}$ with $S$ unitary. The positive factor is the unique positive square root of $T^*T$.''',
)

s.card(
    'ball-ellipsoid',
    'thm-ball-ellipsoid',
    r'''Which axes describe the image of the unit ball under an invertible operator?''',
    r'''If $Te_j=s_jf_j$ is a singular value decomposition, the image is $E(s_1f_1,\ldots,s_nf_n)$.''',
)

s.card(
    'svd-boxes',
    'thm-svd-boxes',
    r'''Which boxes are sent to boxes by an invertible operator?''',
    r'''Boxes whose edges follow its right singular vectors. An edge $r_je_j$ becomes $r_js_jf_j$, so the image edges follow the left singular vectors.''',
)

s.card(
    'volume-scaling',
    'thm-volume-scaling',
    r'''State the volume multiplier and the hypotheses needed for the measurable-set version.''',
    r'''For invertible $T$ on a finite-dimensional real inner product space and measurable $\Omega$, $\Vol(T(\Omega))=(\prod_js_j)\Vol(\Omega)$. Volume uses orthonormal-coordinate Lebesgue measure.''',
)

s.card(
    'normal-eigenvalue-classes',
    'thm-normal-eigenvalue-classification',
    r'''For a normal complex operator, which eigenvalue restrictions characterize an orthogonal projection, a skew-adjoint operator, and a unitary operator?''',
    r'''Respectively: all eigenvalues lie in $\{0,1\}$; all have real part zero; all have modulus one.''',
)

s.write()