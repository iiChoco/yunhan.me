from common import Section

s = Section('6c')

s.p(
    'intro-orthogonal-complements',
    'Decomposition, nearest points, and approximate solutions',
    r'''Orthogonality supplies a natural way to separate a vector into
    a component in a subspace and a component perpendicular to it.
    We use this separation to solve distance-minimization problems
    and then construct a pseudoinverse for linear equations.
    Subspaces carry the restricted inner product, and the ambient
    inner product space need not be finite-dimensional unless this
    is stated explicitly.''',
    211,
)

s.d(
    'def-orthogonal-complement',
    'Orthogonal complements',
    r'''For a subset $U$ of an inner product space $V$, define
    \[
    U^\perp=\{v\in V:\ip{u}{v}=0\text{ for every }u\in U\}.
    \]
    This orthogonal complement is taken inside the specified ambient
    space $V$. By conjugate symmetry, the same condition can be
    written as $\ip{v}{u}=0$ for every $u\in U$.''',
    '6.46',
    211,
)

s.r(
    'ex-normal-vector-complements',
    'A normal vector and its perpendicular plane',
    r'''In $\R^3$ with its standard inner product, put
    \[
    a=(2,3,5),\qquad
    H=\{(x,y,z):2x+3y+5z=0\}.
    \]
    Prove that $\{a\}^\perp=H$ and
    $H^\perp=\{ta:t\in\R\}$.''',
    r'''For $v=(x,y,z)$, the equality $\ip{a}{v}=0$ is exactly
    $2x+3y+5z=0$. This proves $\{a\}^\perp=H$.

    If $v=(x,y,z)\in H^\perp$, test orthogonality against
    $(3,-2,0)$ and $(5,0,-2)$, both of which belong to $H$.
    The resulting equations are $3x-2y=0$ and $5x-2z=0$.
    Hence $y=3x/2$ and $z=5x/2$, so
    $v=(x/2)(2,3,5)$.
    Conversely, if $v=ta$ and $h\in H$, then
    $\ip{h}{v}=t\ip{h}{a}=0$ by the defining equation of $H$.
    Thus every such multiple belongs to $H^\perp$, proving
    the second equality.''',
    2,
    15,
    [r'''For the second equality, test against two convenient vectors in the plane.'''],
    ['def-orthogonal-complement', 'thm-standard-inner-product'],
    '6.47',
    211,
    'example',
)

s.r(
    'ex-lines-planes-complements',
    'Lines and planes exchange under orthogonal complementation',
    r'''In $\R^3$, the orthogonal complement of a plane through
    the origin is a line through the origin, and the orthogonal
    complement of a line through the origin is a plane through
    the origin. In each case every vector of either subspace
    is orthogonal to every vector of the other.''',
    r'''For a plane $U$, choose an orthonormal basis $e_1,e_2$
    of $U$ and extend it to an orthonormal basis $e_1,e_2,e_3$
    of $\R^3$. If $v=c_1e_1+c_2e_2+c_3e_3$, orthonormality
    gives $\ip{v}{e_1}=c_1$ and $\ip{v}{e_2}=c_2$.
    Orthogonality to every vector in $U$ is therefore equivalent
    to $c_1=c_2=0$: necessity follows by testing the basis
    vectors, and sufficiency follows by taking inner products
    with their arbitrary linear combinations.
    Thus $U^\perp=\Span(e_3)$, a line.

    For a line $L$, choose its orthonormal basis $e_1$ and
    extend it to an orthonormal basis $e_1,e_2,e_3$ of
    $\R^3$. The same coefficient calculation shows that
    $L^\perp=\Span(e_2,e_3)$, a plane.
    The final orthogonality statement is the definition
    of an orthogonal complement, together with symmetry
    of orthogonality.''',
    2,
    20,
    [r'''Choose an orthonormal basis of the given subspace and extend it to one of the ambient space.'''],
    [
        'def-orthogonal-complement',
        'thm-orthonormal-basis-existence',
        'thm-orthonormal-extension',
        'thm-orthonormal-coordinates',
        'thm-inner-product-properties',
        'c2-thm-low-dimensional-subspaces',
    ],
    '6.47',
    211,
    'example',
)

s.r(
    'ex-coordinate-orthogonal-complement',
    'Complementary coordinate positions',
    r'''In $\F^5$ with the standard inner product, let
    \[
    U=\{(a,b,0,0,0):a,b\in\F\}.
    \]
    Then
    \[
    U^\perp=\{(0,0,x,y,z):x,y,z\in\F\}.
    \]''',
    r'''If $v\in U^\perp$, then $\ip{v}{e_1}=0$ and
    $\ip{v}{e_2}=0$, where $e_1,e_2$ are the first
    two standard coordinate vectors. These inner
    products are the first two coordinates of $v$,
    so both coordinates vanish.
    Conversely, if the first two coordinates of $v$
    vanish, the standard inner product of $v$ with
    every vector $(a,b,0,0,0)$ is zero. Thus $v$ lies
    in $U^\perp$, proving both inclusions.''',
    1,
    10,
    [r'''Test orthogonality against the first two standard basis vectors.'''],
    ['def-orthogonal-complement', 'thm-standard-inner-product'],
    '6.47',
    211,
    'example',
)

s.r(
    'ex-orthonormal-block-complement',
    'Splitting an orthonormal basis into two groups',
    r'''If $e_1,\ldots,e_m,f_1,\ldots,f_n$ is an orthonormal
    basis of $V$, where either group may be empty, then
    \[
    \Span(e_1,\ldots,e_m)^\perp=\Span(f_1,\ldots,f_n).
    \]''',
    r'''Expand an arbitrary $v\in V$ in the given orthonormal
    basis:
    \[
    v=\sum_{j=1}^m\ip{v}{e_j}e_j+
      \sum_{k=1}^n\ip{v}{f_k}f_k.
    \]
    Orthogonality to the span of the $e_j$ implies
    $\ip{v}{e_j}=0$ for every $j$, so the expansion
    places $v$ in the span of the $f_k$.
    Conversely, every $f_k$ is orthogonal to every
    $e_j$, and the inner product identities extend
    these equalities to arbitrary linear combinations
    in the two spans. Thus the second span is contained
    in the stated orthogonal complement.
    Empty sums and empty spans give the same conclusions
    when one or both groups are empty.''',
    1,
    10,
    [r'''Expand a vector in the full orthonormal basis and identify the coefficients forced to vanish.'''],
    [
        'def-orthogonal-complement',
        'thm-orthonormal-coordinates',
        'thm-inner-product-properties',
        'c2-def-span',
    ],
    '6.47',
    211,
    'example',
)

s.r(
    'thm-orthogonal-complement-subspace',
    'An orthogonal complement is always a subspace',
    r'''For every subset $U$ of an inner product space $V$,
    the set $U^\perp$ is a subspace of $V$.''',
    r'''For every $u\in U$, $\ip{u}{0}=0$, so
    $0\in U^\perp$. If $v,w\in U^\perp$, then for
    every $u\in U$,
    \[
    \ip{u}{v+w}=\ip{u}{v}+\ip{u}{w}=0.
    \]
    Hence $v+w\in U^\perp$. If $a\in\F$ and
    $v\in U^\perp$, then
    \[
    \ip{u}{av}=\overline a\,\ip{u}{v}=0
    \]
    for every $u\in U$, so $av\in U^\perp$.
    The subspace test proves the assertion.
    If $U$ is empty, the universal conditions are
    vacuous, and the same proof gives $U^\perp=V$.''',
    1,
    10,
    [r'''Use additivity and conjugate homogeneity in the second argument.'''],
    [
        'def-orthogonal-complement',
        'thm-inner-product-properties',
        'c1-thm-subspace-test',
    ],
    '6.48(a)',
    211,
)

s.r(
    'thm-orthogonal-complement-properties',
    'Basic containment properties of orthogonal complements',
    r'''For subsets $U,G,H$ of an inner product space $V$,
    \[
    \{0\}^\perp=V,\qquad V^\perp=\{0\},\qquad
    U\cap U^\perp\subseteq\{0\}.
    \]
    If $G\subseteq H$, then $H^\perp\subseteq G^\perp$.
    When $U$ is a subspace, $U\cap U^\perp=\{0\}$.''',
    r'''Every vector is orthogonal to zero, so
    $\{0\}^\perp=V$. If $v\in V^\perp$, then
    $v\in V$ allows us to test against $v$ itself:
    $\ip{v}{v}=0$, which forces $v=0$.
    The zero vector belongs to $V^\perp$, establishing
    the second equality.

    If $u\in U\cap U^\perp$, its membership in $U$
    lets us test its orthogonality against itself.
    Again $\ip{u}{u}=0$ implies $u=0$.
    If $U$ is a subspace, zero belongs to both sets,
    turning this inclusion into equality.

    Finally, a vector orthogonal to every member of
    $H$ is orthogonal to every member of its subset
    $G$. Thus $H^\perp\subseteq G^\perp$.''',
    1,
    10,
    [r'''For an intersection with an orthogonal complement, test a vector against itself.'''],
    [
        'def-orthogonal-complement',
        'def-inner-product',
        'thm-inner-product-properties',
        'c1-thm-subspace-test',
    ],
    '6.48(b-e)',
    211,
)

s.r(
    'thm-orthogonal-direct-sum',
    'A finite-dimensional subspace gives an orthogonal decomposition',
    r'''If $U$ is a finite-dimensional subspace of an inner
    product space $V$, then
    \[
    V=U\oplus U^\perp.
    \]
    The ambient space $V$ may be infinite-dimensional.''',
    r'''Choose an orthonormal basis $e_1,\ldots,e_m$
    of $U$. For $v\in V$, define
    \[
    u=\sum_{j=1}^m\ip{v}{e_j}e_j,\qquad w=v-u.
    \]
    The vector $u$ belongs to $U$. For each $k$,
    orthonormality gives
    \[
    \ip{w}{e_k}
    =\ip{v}{e_k}-\sum_{j=1}^m
       \ip{v}{e_j}\ip{e_j}{e_k}=0.
    \]
    If $y=\sum_k a_ke_k\in U$, conjugate linearity
    in the second argument gives
    $\ip{w}{y}=\sum_k\overline{a_k}\ip{w}{e_k}=0$.
    By conjugate symmetry, $w\in U^\perp$.
    Thus every $v$ belongs to $U+U^\perp$.

    Both summands are subspaces, and their intersection
    is $\{0\}$ by the preceding result. The two-subspace
    direct-sum criterion therefore makes the representation
    unique. If $U=\{0\}$, its orthonormal basis is empty;
    the construction gives $u=0$ and $w=v$, so this
    case is included.''',
    2,
    20,
    [
        r'''Subtract the sum of the components along an orthonormal basis of $U$.''',
        r'''Check that the remainder is orthogonal to every basis vector and then to their entire span.''',
    ],
    [
        'thm-orthonormal-basis-existence',
        'def-orthonormal',
        'thm-inner-product-properties',
        'def-orthogonal-complement',
        'thm-orthogonal-complement-subspace',
        'thm-orthogonal-complement-properties',
        'c1-thm-direct-intersection',
        'c2-def-basis',
    ],
    '6.49',
    212,
)

s.r(
    'thm-orthogonal-dimension',
    'Dimension of an orthogonal complement',
    r'''If $V$ is finite-dimensional and $U$ is a subspace,
    then
    \[
    \dim U^\perp=\dim V-\dim U.
    \]''',
    r'''Both $U$ and $U^\perp$ are finite-dimensional
    subspaces of $V$. The orthogonal decomposition
    theorem gives $V=U\oplus U^\perp$.
    Dimension addition for a direct sum yields
    $\dim V=\dim U+\dim U^\perp$.
    Subtracting $\dim U$ gives the claimed formula,
    including the zero-space and whole-space cases.''',
    1,
    10,
    [r'''Apply dimension addition to the orthogonal direct sum.'''],
    [
        'thm-orthogonal-complement-subspace',
        'thm-orthogonal-direct-sum',
        'c2-thm-subspaces-finite',
        'c2-thm-direct-dimension',
    ],
    '6.51',
    213,
)

s.r(
    'thm-double-orthogonal',
    'Taking the orthogonal complement twice',
    r'''If $U$ is a finite-dimensional subspace of an inner
    product space $V$, then
    \[
    (U^\perp)^\perp=U.
    \]
    This conclusion does not require $V$ to be finite-dimensional.''',
    r'''If $u\in U$ and $w\in U^\perp$, then
    $\ip{u}{w}=0$, and conjugate symmetry gives
    $\ip{w}{u}=0$. Hence $u\in(U^\perp)^\perp$,
    proving one inclusion.

    Now let $v\in(U^\perp)^\perp$. Decompose it as
    $v=u+w$ with $u\in U$ and $w\in U^\perp$.
    Since $v$ is orthogonal to $w$ and $u$ is also
    orthogonal to $w$, we have
    \[
    \ip{w}{w}=\ip{w}{v-u}
    =\ip{w}{v}-\ip{w}{u}=0.
    \]
    Positive definiteness gives $w=0$, so $v=u\in U$.
    This proves the reverse inclusion without applying
    any finite-dimensionality assumption to $U^\perp$.''',
    2,
    20,
    [
        r'''One inclusion follows from symmetry of orthogonality.''',
        r'''For the other, decompose a vector using the finite-dimensional subspace $U$.''',
    ],
    [
        'def-orthogonal-complement',
        'thm-orthogonal-direct-sum',
        'thm-inner-product-properties',
        'def-inner-product',
    ],
    '6.52',
    213,
)

s.r(
    'thm-trivial-orthogonal-complement',
    'When the orthogonal complement vanishes',
    r'''For a finite-dimensional subspace $U$ of an inner
    product space $V$,
    \[
    U^\perp=\{0\}\quad\Longleftrightarrow\quad U=V.
    \]''',
    r'''If $U^\perp=\{0\}$, the decomposition
    $V=U\oplus U^\perp$ says that every vector of
    $V$ lies in $U$, so $U=V$.
    Conversely, if $U=V$, then
    $U^\perp=V^\perp=\{0\}$ by the basic complement
    properties.''',
    1,
    10,
    [r'''Use the decomposition of every ambient vector.'''],
    ['thm-orthogonal-direct-sum', 'thm-orthogonal-complement-properties'],
    '6.54',
    214,
)

s.d(
    'def-orthogonal-projection',
    'Orthogonal projection',
    r'''Let $U$ be a finite-dimensional subspace of $V$.
    For the unique decomposition $v=u+w$ with
    $u\in U$ and $w\in U^\perp$, define
    \[
    P_Uv=u.
    \]
    Thus $P_U:V\to V$ is a well-defined function whose
    values lie in $U$. It is called the orthogonal
    projection onto $U$; its linearity is proved below.''',
    '6.55',
    214,
)

s.r(
    'ex-projection-line',
    'Projection onto a line',
    r'''If $u\ne0$ and $U=\Span(u)$, then for every $v\in V$,
    \[
    P_Uv=\frac{\ip{v}{u}}{\norm{u}^2}u.
    \]''',
    r'''Positive definiteness gives $\norm{u}^2>0$.
    Put $a=\ip{v}{u}/\norm{u}^2$.
    The vector $au$ belongs to $U$, and
    \[
    \ip{v-au}{u}
    =\ip{v}{u}-a\ip{u}{u}=0.
    \]
    Conjugate homogeneity then makes $v-au$
    orthogonal to every scalar multiple of $u$,
    so $v-au\in U^\perp$.
    Thus $v=au+(v-au)$ is the defining orthogonal
    decomposition, and uniqueness gives $P_Uv=au$.''',
    1,
    10,
    [r'''Choose the multiple of $u$ that makes the remainder orthogonal to $u$.'''],
    [
        'def-orthogonal-projection',
        'def-orthogonal-complement',
        'thm-inner-product-properties',
        'def-norm',
        'thm-norm-properties',
        'c2-def-span',
    ],
    '6.56',
    214,
    'example',
)

s.r(
    'thm-projection-properties',
    'Algebra and geometry of orthogonal projection',
    r'''For a finite-dimensional subspace $U$ of $V$,
    $P_U$ is a linear operator satisfying
    \[
    P_Uu=u\ (u\in U),\qquad
    P_Uw=0\ (w\in U^\perp),
    \]
    \[
    \Range P_U=U,\qquad \Null P_U=U^\perp,\qquad
    v-P_Uv\in U^\perp,
    \]
    \[
    P_U^2=P_U,\qquad \norm{P_Uv}\le\norm v.
    \]
    If $e_1,\ldots,e_m$ is an orthonormal basis of $U$, then
    \[
    P_Uv=\sum_{j=1}^m\ip{v}{e_j}e_j.
    \]''',
    r'''Write $v_i=u_i+w_i$ with $u_i\in U$ and
    $w_i\in U^\perp$ for $i=1,2$.
    Since both components lie in subspaces,
    \[
    v_1+v_2=(u_1+u_2)+(w_1+w_2)
    \]
    is its orthogonal decomposition. Uniqueness gives
    $P_U(v_1+v_2)=u_1+u_2=P_Uv_1+P_Uv_2$.
    For a scalar $a$, the decomposition
    $av_1=au_1+aw_1$ similarly gives
    $P_U(av_1)=aP_Uv_1$. Thus $P_U$ is linear.

    The decompositions $u=u+0$ and $w=0+w$
    prove that $P_U$ fixes $U$ and kills $U^\perp$.
    Every projection value lies in $U$, and every
    $u\in U$ is its own projection value, so
    $\Range P_U=U$.
    If $v=u+w$ is the orthogonal decomposition,
    $P_Uv=0$ exactly when $u=0$, or equivalently
    when $v\in U^\perp$. This proves the kernel
    formula. The same decomposition gives
    $v-P_Uv=w\in U^\perp$.
    Since $P_Uv\in U$ and $P_U$ fixes $U$,
    applying $P_U$ again changes nothing:
    $P_U^2v=P_Uv$.

    The two components are orthogonal, so Pythagoras gives
    \[
    \norm v^2=\norm{P_Uv}^2+\norm{v-P_Uv}^2
    \ge\norm{P_Uv}^2.
    \]
    Both norms are nonnegative, proving the norm bound.

    Finally, expand $P_Uv$ in the orthonormal basis of $U$.
    The residual is orthogonal to each $e_j$, so
    $\ip{P_Uv}{e_j}=\ip{v}{e_j}$.
    The orthonormal coordinate formula yields the asserted
    projection formula. If $U=\{0\}$, this is an empty
    sum and all the preceding statements give the zero
    projection, as required.''',
    2,
    20,
    [
        r'''Use uniqueness of orthogonal decomposition to prove linearity.''',
        r'''Apply Pythagoras to the two components of $v$.''',
    ],
    [
        'def-orthogonal-projection',
        'thm-orthogonal-direct-sum',
        'thm-orthogonal-complement-subspace',
        'thm-pythagorean',
        'thm-norm-properties',
        'thm-orthonormal-coordinates',
        'thm-inner-product-properties',
        'c3-def-linear-map',
        'c3-def-range',
        'c3-def-null-space',
    ],
    '6.57',
    215,
)

s.r(
    'thm-riesz-complement-proof',
    'Riesz representation through an orthogonal complement',
    r'''Let $V$ be a finite-dimensional inner product space.
    For each $v\in V$, define the functional
    $\varphi_v(u)=\ip{u}{v}$.
    The correspondence $v\mapsto\varphi_v$ is a bijection
    from $V$ to its dual space $V'$.
    Moreover,
    \[
    \varphi_{v+w}=\varphi_v+\varphi_w,\qquad
    \varphi_{av}=\overline a\,\varphi_v.
    \]''',
    r'''Linearity of the inner product in its first argument
    makes every $\varphi_v$ a linear functional.
    If $\varphi_v=\varphi_w$, then
    $\ip{u}{v-w}=0$ for every $u\in V$.
    Taking $u=v-w$ gives $\norm{v-w}^2=0$ and
    hence $v=w$. Thus the correspondence is injective.

    To prove surjectivity using complements, let
    $\varphi\in V'$. If $\varphi=0$, take $v=0$.
    Otherwise $N=\Null\varphi$ is a proper
    finite-dimensional subspace. The trivial-complement
    criterion gives $N^\perp\ne\{0\}$.
    Choose $w\in N^\perp$ with $w\ne0$.
    Since $N\cap N^\perp=\{0\}$, we have $w\notin N$
    and therefore $\varphi(w)\ne0$. Put
    \[
    v=\frac{\overline{\varphi(w)}}{\norm w^2}w.
    \]
    For any $u\in V$, the vector
    \[
    u-\frac{\varphi(u)}{\varphi(w)}w
    \]
    belongs to $N$, so it is orthogonal to $w$.
    Taking the inner product with $w$ gives
    \[
    \ip{u}{w}
    =\frac{\varphi(u)}{\varphi(w)}\norm w^2.
    \]
    Conjugate homogeneity in the second argument now yields
    \[
    \ip{u}{v}
    =\frac{\varphi(w)}{\norm w^2}\ip{u}{w}
    =\varphi(u).
    \]
    Thus $\varphi=\varphi_v$, proving surjectivity.
    The zero-dimensional case is included in the
    zero-functional case.

    The two displayed algebraic identities follow by
    evaluating at an arbitrary $u$ and using additivity
    and conjugate homogeneity in the second inner-product
    argument. Over $\R$ this makes the correspondence
    linear; over $\C$ the scalar rule is conjugate linear.''',
    3,
    30,
    [
        r'''For a nonzero functional, choose a nonzero vector perpendicular to its kernel.''',
        r'''Subtract a suitable multiple of that vector from an arbitrary input to obtain a kernel vector.''',
        r'''The scalar multiplying the representing vector must account for conjugate linearity in the second argument.''',
    ],
    [
        'thm-inner-product-properties',
        'thm-norm-properties',
        'thm-trivial-orthogonal-complement',
        'thm-orthogonal-complement-properties',
        'c2-thm-subspaces-finite',
        'c3-def-linear-functional',
        'c3-def-dual-space',
        'c3-thm-null-subspace',
        'c3-def-null-space',
    ],
    '6.58',
    216,
)

s.r(
    'thm-minimization',
    'The unique nearest point in a finite-dimensional subspace',
    r'''Let $U$ be a finite-dimensional subspace of $V$.
    For $v\in V$ and $u\in U$,
    \[
    \norm{v-u}^2
    =\norm{v-P_Uv}^2+\norm{P_Uv-u}^2.
    \]
    Consequently,
    \[
    \norm{v-P_Uv}\le\norm{v-u},
    \]
    with equality exactly when $u=P_Uv$.''',
    r'''Decompose
    \[
    v-u=(v-P_Uv)+(P_Uv-u).
    \]
    The first summand belongs to $U^\perp$ by the
    projection properties. The second belongs to $U$,
    because both $P_Uv$ and $u$ do. They are orthogonal,
    so Pythagoras gives the asserted squared-norm identity.

    The second term on its right is nonnegative, which
    gives the squared inequality and then the norm
    inequality. Equality of the norms is equivalent
    to $\norm{P_Uv-u}^2=0$. Positive definiteness
    makes this equivalent to $u=P_Uv$.
    If $U=\{0\}$, its only candidate is zero and
    the same identities apply.''',
    2,
    15,
    [r'''Split the error into the orthogonal residual and the difference between two points of $U$.'''],
    [
        'thm-projection-properties',
        'def-orthogonal-complement',
        'thm-pythagorean',
        'thm-norm-properties',
        'c1-thm-subspace-test',
    ],
    '6.61',
    217,
)

s.d(
    'def-sine-approximation-setting',
    'The function space for the sine approximation',
    r'''For the following example, $\pi$ is the usual positive
    circle constant and $\sin$ is the real sine function.
    Write $C[-\pi,\pi]$ for the continuous real-valued functions
    on $[-\pi,\pi]$, with pointwise operations.
    We use the integral pairing
    \[
    \ip{f}{g}=\int_{-\pi}^{\pi}f(x)g(x)\,dx.
    \]
    The analytic properties needed for this example are
    recorded explicitly in the next theorem.''',
    page=218,
)

s.add(
    'theorem',
    'thm-sine-integral-data',
    'Analytic input for the sine approximation',
    r'''The integral pairing just specified is an inner product
    on $C[-\pi,\pi]$. Polynomial restrictions and the function
    $x\mapsto\sin x$ belong to this space.
    An odd continuous function has integral zero over
    $[-\pi,\pi]$, and $\sin$ is odd.
    For nonnegative integers $r$,
    \[
    \int_{-\pi}^{\pi}x^{2r}\,dx
    =\frac{2\pi^{2r+1}}{2r+1},
    \qquad
    \int_{-\pi}^{\pi}x^{2r+1}\,dx=0.
    \]
    The following additional integrals hold:
    \[
    \int_{-\pi}^{\pi}x\sin x\,dx=2\pi,
    \]
    \[
    \int_{-\pi}^{\pi}x^3\sin x\,dx=2\pi^3-12\pi,
    \]
    \[
    \int_{-\pi}^{\pi}x^5\sin x\,dx
    =2\pi^5-40\pi^3+240\pi.
    \]''',
    page=218,
)

s.note(
    'remark-sine-integral-faith',
    'Explicit analytic prerequisites',
    r'''The preceding facts about continuous functions, sine,
    and integration are taken on faith as calculus background.
    The approximation below is derived from these exact
    identities and the proved projection theorem.''',
    218,
)

s.r(
    'ex-best-sine-polynomial',
    'The exact best polynomial approximation to sine in degree five',
    r'''For $t=x/\pi$, define
    \[
    L_1(x)=t,\qquad
    L_3(x)=\frac{5t^3-3t}{2},\qquad
    L_5(x)=\frac{63t^5-70t^3+15t}{8}.
    \]
    Among all real polynomials of degree at most $5$,
    the unique minimizer of
    \[
    \int_{-\pi}^{\pi}|\sin x-p(x)|^2\,dx
    \]
    is
    \[
    \begin{aligned}
    u(x)={}&\frac3\pi L_1(x)
    +\left(\frac7\pi-\frac{105}{\pi^3}\right)L_3(x)\\
    &+\left(\frac{11}\pi-\frac{1155}{\pi^3}
           +\frac{10395}{\pi^5}\right)L_5(x).
    \end{aligned}
    \]
    In particular, its integrated squared error is no larger
    than that of $x-x^3/6+x^5/120$.''',
    r'''Let $U$ be the span of the restrictions of
    $1,x,\ldots,x^5$ in $C[-\pi,\pi]$.
    It is a finite-dimensional subspace consisting of
    exactly the indicated polynomial restrictions.
    Distinct polynomials of degree at most $5$ have
    distinct restrictions: a nonzero difference cannot
    vanish at the infinitely many points of this interval,
    by the polynomial root bound.

    The moment formulas give the following inner products:
    \[
    \norm{L_1}^2=\frac{2\pi}{3},
    \qquad
    \ip{L_1}{L_3}
    =\pi\left(\frac55-\frac33\right)=0,
    \]
    \[
    \ip{L_1}{L_5}
    =\frac\pi4\left(\frac{63}7-\frac{70}5+\frac{15}3\right)=0,
    \]
    \[
    \norm{L_3}^2
    =\frac\pi2\left(\frac{25}7-\frac{30}5+\frac93\right)
    =\frac{2\pi}{7},
    \]
    \[
    \ip{L_3}{L_5}
    =\frac\pi8\left(\frac{315}9-\frac{539}7
                   +\frac{285}5-\frac{45}3\right)=0,
    \]
    \[
    \norm{L_5}^2
    =\frac\pi{32}\left(\frac{3969}{11}-\frac{8820}9
        +\frac{6790}7-\frac{2100}5+\frac{225}3\right)
    =\frac{2\pi}{11}.
    \]
    Each expression follows by multiplying the displayed
    polynomials in $t$ and using
    $\int_{-\pi}^{\pi}t^{2r}\,dx=2\pi/(2r+1)$.

    Put $s(x)=\sin x$ and denote the three accepted
    sine moments by $M_1,M_3,M_5$ in increasing order.
    Substitution into the definitions gives
    \[
    \ip{s}{L_1}=\frac{M_1}{\pi}=2,
    \]
    \[
    \ip{s}{L_3}
    =\frac{5M_3}{2\pi^3}-\frac{3M_1}{2\pi}
    =2-\frac{30}{\pi^2},
    \]
    \[
    \ip{s}{L_5}
    =\frac{63M_5}{8\pi^5}-\frac{70M_3}{8\pi^3}
       +\frac{15M_1}{8\pi}
    =2-\frac{210}{\pi^2}+\frac{1890}{\pi^4}.
    \]
    The coefficient of each $L_j$ in the stated $u$
    is exactly $\ip{s}{L_j}/\norm{L_j}^2$.
    Pairwise orthogonality therefore gives
    $\ip{s-u}{L_j}=0$ for $j=1,3,5$.

    Both $s$ and $u$ are odd. Their difference is
    orthogonal to $1,t^2,t^4$, because its product
    with each of these even functions is odd and
    has integral zero. Moreover the six functions
    $1,t^2,t^4,L_1,L_3,L_5$ span $U$:
    \[
    t=L_1,\qquad
    t^3=\frac{2L_3+3t}{5},\qquad
    t^5=\frac{8L_5+70t^3-15t}{63},
    \]
    and powers of $x$ are nonzero scalar multiples
    of the corresponding powers of $t$.
    Thus $s-u$ is orthogonal to all of $U$.

    Since $u\in U$ and $s-u\in U^\perp$, uniqueness
    of orthogonal decomposition identifies $u=P_Us$.
    The minimization theorem makes it the unique
    closest element of $U$ to $s$. The square of
    the distance is precisely the displayed integral.
    Injectivity of polynomial restriction transfers
    uniqueness to the polynomials themselves.
    Finally $x-x^3/6+x^5/120$ belongs to $U$,
    so inserting it as a competitor gives the final inequality.''',
    3,
    45,
    [
        r'''Use the three displayed odd polynomials as an orthogonal basis for the odd part of the approximation space.''',
        r'''Show that the proposed residual is orthogonal to those three polynomials and to the even powers.''',
    ],
    [
        'def-sine-approximation-setting',
        'thm-sine-integral-data',
        'thm-minimization',
        'thm-orthogonal-direct-sum',
        'def-orthogonal-projection',
        'def-orthogonal-complement',
        'thm-inner-product-properties',
        'c2-thm-span-smallest',
        'c2-def-finite-dimensional',
        'c4-thm-root-bound',
    ],
    '6.63',
    218,
    'example',
)

s.note(
    'remark-sine-rounded-coefficients',
    'Reading the approximation numerically',
    r'''Expanding the exact expression gives approximately
    \[
    u(x)=0.9878621356x-0.1552714106x^3+0.0056431180x^5.
    \]
    These decimal coefficients are rounded. The preceding
    exact formula specifies the unique minimizer.''',
    219,
)

s.r(
    'thm-kernel-complement-restriction',
    'Removing the kernel produces an invertible restriction',
    r'''Let $V,W$ be inner product spaces, with $V$
    finite-dimensional, and let $T\in\Lin(V,W)$.
    Put $N=\Null T$ and $R=\Range T$.
    The map
    \[
    A:N^\perp\to R,\qquad Ax=Tx,
    \]
    is an invertible linear map. The spaces $N$, $N^\perp$,
    and $R$ are finite-dimensional, even if $W$ is not.''',
    r'''The kernel and range are subspaces. The subspaces
    $N$ and $N^\perp$ of the finite-dimensional space
    $V$ are finite-dimensional; the range is
    finite-dimensional by the finite-dimensional
    range conclusion of rank-nullity.
    The restriction has its stated target by the
    definition of range, and is linear because
    it uses the same formula as $T$.

    If $Ax=0$ for $x\in N^\perp$, then also $x\in N$.
    The intersection $N\cap N^\perp=\{0\}$ gives $x=0$.
    Thus $A$ has zero kernel and is injective.
    For $y\in R$, choose $v\in V$ with $Tv=y$.
    Decompose $v=n+x$ with $n\in N$ and $x\in N^\perp$.
    Then $Ax=Tx=Tv-Tn=y$, so $A$ is surjective.
    The bijective invertibility theorem makes $A$
    invertible with a linear inverse from $R$ to $N^\perp$.

    If $T=0$, both $N^\perp$ and $R$ are the zero
    space, and the argument gives their unique
    invertible map. Thus the degenerate case is included.''',
    2,
    20,
    [
        r'''Injectivity follows from the intersection of the kernel and its orthogonal complement.''',
        r'''For surjectivity, decompose any preimage into its kernel and perpendicular components.''',
    ],
    [
        'thm-orthogonal-complement-subspace',
        'thm-orthogonal-complement-properties',
        'thm-orthogonal-direct-sum',
        'c2-thm-subspaces-finite',
        'c3-thm-null-subspace',
        'c3-thm-range-subspace',
        'c3-thm-rank-nullity',
        'c3-thm-injective-null',
        'c3-thm-invertible-bijective',
        'c3-def-null-space',
        'c3-def-range',
    ],
    '6.67',
    220,
)

s.d(
    'def-pseudoinverse',
    'Pseudoinverse',
    r'''Let $V,W$ be inner product spaces, with $V$
    finite-dimensional, and let $T\in\Lin(V,W)$.
    Put $N=\Null T$, $R=\Range T$, and regard
    $A=T|_{N^\perp}$ as the invertible map
    $A:N^\perp\to R$ just constructed.
    Define the pseudoinverse $T^\dagger:W\to V$ by
    \[
    T^\dagger w=A^{-1}(P_Rw).
    \]
    Here $P_R$ is the orthogonal projection in $W$
    onto the finite-dimensional subspace $R$.
    Its value lies in the domain $R$ of $A^{-1}$,
    and the resulting value of $T^\dagger$ lies
    in $N^\perp\subseteq V$.''',
    '6.68',
    221,
)

s.r(
    'thm-pseudoinverse-properties',
    'The two projection identities for the pseudoinverse',
    r'''Under the hypotheses defining $T^\dagger$, it is
    a linear map from $W$ to $V$ and satisfies
    \[
    TT^\dagger=P_{\Range T},\qquad
    T^\dagger T=P_{(\Null T)^\perp}.
    \]
    If $T$ is invertible, then $T^\dagger=T^{-1}$.
    In particular, surjectivity gives $TT^\dagger=I_W$,
    and injectivity gives $T^\dagger T=I_V$.
    Also, $T^\dagger$ vanishes on $(\Range T)^\perp$;
    for $w\in\Range T$, it returns the unique
    $x\in(\Null T)^\perp$ satisfying $Tx=w$.''',
    r'''Use the notation $N,R,A$ from the definition.
    The projection $P_R$, regarded as a map into $R$,
    is linear, and $A^{-1}:R\to N^\perp$ is linear.
    Their composition, with values regarded as elements
    of $V$, is therefore linear.

    For every $w\in W$, the vector $P_Rw$ lies in $R$,
    and $T$ agrees with $A$ on the image of $A^{-1}$.
    Hence
    \[
    TT^\dagger w=A(A^{-1}(P_Rw))=P_Rw,
    \]
    proving the first projection identity.

    For $v\in V$, write $v=n+x$ with
    $n\in N$ and $x\in N^\perp$.
    Then $Tv=Tx\in R$, so
    \[
    T^\dagger Tv=A^{-1}(P_RTx)=A^{-1}(Ax)=x.
    \]
    The vector $n$ is orthogonal to all of $N^\perp$,
    so the same decomposition identifies
    $x=P_{N^\perp}v$. This proves the second identity.

    If $T$ is invertible, its kernel is zero and its
    range is $W$. Thus $N^\perp=V$, $A=T$, and
    $P_R=I_W$, giving $T^\dagger=T^{-1}$.
    If $T$ is merely surjective, $R=W$ still gives
    $TT^\dagger=I_W$. If it is merely injective,
    $N=\{0\}$ gives $T^\dagger T=I_V$.

    Finally, if $w\in R^\perp$, then $P_Rw=0$,
    and linearity of $A^{-1}$ gives $T^\dagger w=0$.
    If $w\in R$, then $P_Rw=w$ and $T^\dagger w=A^{-1}w$.
    The definition of this inverse gives exactly the
    stated existence and uniqueness in $N^\perp$.
    All identities include zero spaces and the zero map.''',
    2,
    20,
    [
        r'''Use the inverse identities for the restricted map onto the range.''',
        r'''To compute $T^\dagger Tv$, decompose $v$ into a kernel component and an orthogonal component.''',
    ],
    [
        'def-pseudoinverse',
        'thm-kernel-complement-restriction',
        'thm-projection-properties',
        'thm-orthogonal-direct-sum',
        'thm-orthogonal-complement-properties',
        'c3-def-map-inverse',
        'c3-thm-invertible-bijective',
        'c3-thm-injective-null',
        'c3-lem-composition-linear',
        'c3-thm-linear-zero',
    ],
    '6.69',
    221,
)

s.r(
    'thm-pseudoinverse-minimum',
    'The least residual and the least norm',
    r'''Let $V,W$ be inner product spaces with $V$
    finite-dimensional, let $T\in\Lin(V,W)$, and let $w\in W$.
    Then for every $v\in V$,
    \[
    \norm{T(T^\dagger w)-w}\le\norm{Tv-w},
    \]
    with equality exactly when
    $v\in T^\dagger w+\Null T$.
    Among those minimizing vectors,
    \[
    \norm{T^\dagger w}\le\norm v,
    \]
    with equality exactly when $v=T^\dagger w$.''',
    r'''Put $x=T^\dagger w$ and $R=\Range T$.
    The pseudoinverse identity gives $Tx=P_Rw$.
    Decompose the residual as
    \[
    Tv-w=(Tv-Tx)+(Tx-w).
    \]
    The first term belongs to $R$, and the second
    belongs to $R^\perp$, because $Tx=P_Rw$ and
    $w-P_Rw\in R^\perp$.
    Pythagoras gives the exact identity
    \[
    \norm{Tv-w}^2
    =\norm{Tv-Tx}^2+\norm{Tx-w}^2.
    \]
    Nonnegativity proves the first inequality.
    Equality holds exactly when $Tv-Tx=0$,
    equivalently when $v-x\in\Null T$, which is
    the stated translate condition.

    For such a vector write $v=x+n$ with
    $n\in\Null T$. By definition of the pseudoinverse,
    $x\in(\Null T)^\perp$. A second use of Pythagoras
    gives
    \[
    \norm v^2=\norm x^2+\norm n^2.
    \]
    Thus $\norm x\le\norm v$, with equality
    exactly when $n=0$, or $v=x$.
    These identities also cover the zero map and
    zero-dimensional domain or target, without
    requiring a separate existence assumption for
    the equation $Tv=w$.''',
    2,
    20,
    [
        r'''Separate the residual into its range component and its orthogonal component.''',
        r'''Within the set of residual minimizers, separate a vector into its pseudoinverse value and a kernel vector.''',
    ],
    [
        'def-pseudoinverse',
        'thm-pseudoinverse-properties',
        'thm-projection-properties',
        'thm-pythagorean',
        'thm-norm-properties',
        'def-orthogonal-complement',
        'c3-def-null-space',
        'c3-def-range',
        'c3-def-vector-set-sum',
        'c3-def-linear-map',
    ],
    '6.70',
    222,
)

s.r(
    'ex-coordinate-pseudoinverse',
    'Computing a pseudoinverse from the kernel and range',
    r'''Give $\F^4$ and $\F^3$ their standard inner products,
    and define
    \[
    T(a,b,c,d)=(a+b+c,2c+d,0).
    \]
    Prove that $T$ is neither injective nor surjective,
    and that
    \[
    T^\dagger(x,y,z)=\frac1{11}
    (5x-2y,\ 5x-2y,\ x+4y,\ -2x+3y).
    \]''',
    r'''The coordinate formula is linear.
    Every output has third coordinate zero, and
    $T(x,0,0,y)=(x,y,0)$. Hence
    \[
    R=\Range T=\{(x,y,0):x,y\in\F\}.
    \]
    This is a proper subspace of $\F^3$, so $T$
    is not surjective.
    The kernel equations give
    \[
    N=\Null T
    =\{(-b-c,b,c,-2c):b,c\in\F\}.
    \]
    Thus $N$ is spanned by
    $n_1=(-1,1,0,0)$ and $n_2=(-1,0,1,-2)$.
    A zero combination of these vectors has its
    second and third coordinates equal to the
    two coefficients, so both coefficients are zero.
    They are a basis of $N$, and $n_1\ne0$
    proves that $T$ is not injective.

    The decomposition
    $(x,y,z)=(x,y,0)+(0,0,z)$ is orthogonal between
    $R$ and $R^\perp$, so $P_R(x,y,z)=(x,y,0)$.
    By the pseudoinverse characterization,
    $T^\dagger(x,y,z)$ is the unique
    $(a,b,c,d)\in N^\perp$ with
    $T(a,b,c,d)=(x,y,0)$.
    Orthogonality to the displayed kernel basis,
    using symmetry of orthogonality, is equivalent to
    $-a+b=0$ and $-a+c-2d=0$.
    Therefore the four required scalar equations are
    \[
    a+b+c=x,\qquad 2c+d=y,\qquad
    b=a,\qquad a=c-2d.
    \]
    Substitute $b=a$ to obtain $c=x-2a$,
    then $d=y-2c=y-2x+4a$.
    The last equation now becomes
    \[
    a=(x-2a)-2(y-2x+4a)=5x-2y-10a.
    \]
    Thus
    \[
    a=b=\frac{5x-2y}{11},\qquad
    c=\frac{x+4y}{11},\qquad
    d=\frac{-2x+3y}{11}.
    \]
    Substituting these values into the four equations
    verifies both the required image and orthogonality,
    so uniqueness proves the formula.
    In particular, applying $T$ to this vector gives
    $(x,y,0)$, as required by $TT^\dagger=P_R$.
    All equations are valid over either $\R$ or $\C$.''',
    3,
    35,
    [
        r'''Find the range and a basis of the kernel first.''',
        r'''Solve $Tv=P_{\Range T}w$ together with the equations making $v$ perpendicular to the kernel.''',
    ],
    [
        'def-pseudoinverse',
        'thm-pseudoinverse-properties',
        'def-orthogonal-projection',
        'def-orthogonal-complement',
        'thm-standard-inner-product',
        'thm-inner-product-properties',
        'c3-thm-coordinate-linear-maps',
        'c3-def-null-space',
        'c3-def-range',
        'c3-thm-injective-null',
        'c2-def-basis',
        'c1-lem-scalar-cancellation',
    ],
    '6.71',
    223,
    'example',
)

s.card(
    'orthogonal-complement',
    'def-orthogonal-complement',
    r'''What is the orthogonal complement of a subset $U\subseteq V$?''',
    r'''It is the set of vectors of $V$ orthogonal to every
    member of $U$. The ambient inner product space is part
    of the definition.''',
)

s.card(
    'orthogonal-dimension',
    'thm-orthogonal-dimension',
    r'''What is $\dim U^\perp$ for a subspace of a finite-dimensional inner product space $V$?''',
    r'''$\dim U^\perp=\dim V-\dim U$.''',
)

s.card(
    'projection-formula',
    'thm-projection-properties',
    r'''How is projection onto $U$ computed from an orthonormal basis $e_1,\ldots,e_m$ of $U$?''',
    r'''$P_Uv=\sum_{j=1}^m\ip{v}{e_j}e_j$.''',
)

s.card(
    'projection-kernel-range',
    'thm-projection-properties',
    r'''What are the range and kernel of the orthogonal projection onto $U$?''',
    r'''$\Range P_U=U$ and $\Null P_U=U^\perp$.
    Also $P_U^2=P_U$.''',
)

s.card(
    'nearest-point-identity',
    'thm-minimization',
    r'''Which identity proves both optimality and uniqueness of the nearest point in $U$?''',
    r'''For $u\in U$,
    $\norm{v-u}^2=\norm{v-P_Uv}^2+\norm{P_Uv-u}^2$.''',
)

s.card(
    'riesz-scalar-conjugation',
    'thm-riesz-complement-proof',
    r'''Under the convention that the inner product is linear in its first argument, how does the representing functional change when its representing vector is multiplied by $a$?''',
    r'''$\varphi_{av}=\overline a\,\varphi_v$.''',
)

s.card(
    'pseudoinverse-definition',
    'def-pseudoinverse',
    r'''How is $T^\dagger w$ constructed when the domain of $T$ is finite-dimensional?''',
    r'''Project $w$ onto $\Range T$, then invert the restriction
    $T:(\Null T)^\perp\to\Range T$ on that projected vector.''',
)

s.card(
    'pseudoinverse-projections',
    'thm-pseudoinverse-properties',
    r'''What are $TT^\dagger$ and $T^\dagger T$?''',
    r'''They are $P_{\Range T}$ and $P_{(\Null T)^\perp}$,
    respectively.''',
)

s.card(
    'pseudoinverse-minimizer-set',
    'thm-pseudoinverse-minimum',
    r'''Which vectors minimize $\norm{Tv-w}$?''',
    r'''Exactly the vectors in $T^\dagger w+\Null T$.''',
)

s.card(
    'pseudoinverse-least-norm',
    'thm-pseudoinverse-minimum',
    r'''Which residual-minimizing vector has the smallest norm?''',
    r'''The unique one is $T^\dagger w$. Adding a kernel vector
    increases its squared norm by the squared norm of that
    kernel vector.''',
)

s.write()
