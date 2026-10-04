from common import Section

s = Section('5e')

s.p(
    'intro-commuting-operators',
    'Studying two operators together',
    r'''A single choice of coordinates becomes especially useful when
    it simplifies two operators at once. We examine how commutation
    preserves eigenspaces and use that preservation to construct
    common eigenvectors and shared diagonal or triangular bases.''',
    175,
)

s.d(
    'def-commute',
    'Commuting operators and matrices',
    r'''Operators $S,T\in\Lin(V)$ \emph{commute} when $ST=TS$.
    Square matrices $A,B$ of the same shape commute when
    $AB=BA$. For operators, this says that applying $S$ and $T$
    in either order gives the same output for every input.''',
    '5.71',
    175,
)

s.r(
    'ex-basic-commuting-operators',
    'Scalar operators and polynomials in one operator',
    r'''For every $A\in\Lin(V)$ and $\lambda\in\F$, the operators
    $\lambda I$ and $A$ commute. For any polynomials $p,q$,
    the operators $p(A)$ and $q(A)$ commute; in particular,
    $A^2$ and $A^3$ commute.''',
    r'''For $v\in V$, linearity of $A$ gives
    \[
    ((\lambda I)A)v=\lambda Av=A(\lambda v)
    =(A(\lambda I))v.
    \]
    Equality at every vector proves the first assertion.
    The polynomial evaluation product theorem gives
    \[
    p(A)q(A)=(pq)(A)=(qp)(A)=q(A)p(A),
    \]
    because scalar polynomial multiplication is commutative.
    Taking $p(z)=z^2$ and $q(z)=z^3$ proves the final claim.
    These calculations remain valid on the zero space.''',
    1,
    10,
    [r'''Evaluate the first identity on a vector; for the second use multiplication of polynomial evaluations.'''],
    [
        'def-commute',
        'thm-polynomial-evaluation-product',
        'def-polynomial-operator',
        'c3-def-linear-map',
        'c3-def-zero-identity-maps',
        'c3-def-map-operations',
        'c3-def-map-composition',
    ],
    page=175,
    kind='example',
)

s.d(
    'def-two-variable-polynomials',
    'Polynomials in two variables with bounded total degree',
    r'''For a nonnegative integer $m$, let $\Poly_m(\C^2,\C)$
    be the set of functions $p:\C^2\to\C$ admitting an expression
    \[
    p(w,z)=\sum_{\substack{j,k\ge0\\j+k\le m}}a_{j,k}w^jz^k,
    \qquad a_{j,k}\in\C.
    \]
    The function $(w,z)\mapsto w^jz^k$ is a monomial, and
    $j+k$ is its total degree. The operations on these
    functions are pointwise addition and scalar multiplication.
    The next result establishes coefficient uniqueness and
    the vector-space properties needed below.''',
    page=175,
)

s.r(
    'lem-two-variable-basis',
    'Unique coefficients and a monomial basis',
    r'''The coefficients in a representation of an element of
    $\Poly_m(\C^2,\C)$ are unique. This set is a nonzero
    finite-dimensional complex vector space whose monomials
    $w^jz^k$ with $j,k\ge0$ and $j+k\le m$, listed in any
    fixed order, form a basis. Its dimension is
    \[
    \frac{(m+1)(m+2)}2.
    \]''',
    r'''Suppose
    \[
    \sum_{\substack{j,k\ge0\\j+k\le m}}a_{j,k}w^jz^k=0
    \]
    for every $w,z\in\C$. Fix $z$ and regard the expression
    as a polynomial in $w$:
    \[
    \sum_{j=0}^m
    \left(\sum_{k=0}^{m-j}a_{j,k}z^k\right)w^j=0.
    \]
    Univariate coefficient uniqueness gives
    $\sum_{k=0}^{m-j}a_{j,k}z^k=0$ for every $j$.
    Since the fixed $z$ was arbitrary, each of these is
    a zero polynomial function of $z$. A second application
    of coefficient uniqueness gives $a_{j,k}=0$ for
    every permitted pair. Subtracting two representations
    now proves uniqueness of the coefficients.

    The space of all functions from $\C^2$ to $\C$ is
    a complex vector space with pointwise operations.
    The set under consideration is exactly the span in
    that function space of the finitely many displayed
    monomials, so it is a subspace. The calculation above
    proves independence of those monomials, and their
    spanning property is the definition of the set.
    Thus they form a basis.

    For each $j$ between $0$ and $m$, there are
    $m-j+1$ choices of $k$. The number of basis entries
    is therefore $1+2+\cdots+(m+1)=(m+1)(m+2)/2$.
    This finite-sum identity follows by induction:
    the case $m=0$ is $1=1$, and the next value adds
    $m+2$ to $(m+1)(m+2)/2$.
    The constant monomial $1$ is nonzero, so the space
    is nonzero even when $m=0$.''',
    2,
    20,
    [
        r'''Fix one variable and apply the univariate coefficient theorem to the other.''',
        r'''Apply that theorem a second time to the coefficient functions.''',
    ],
    [
        'def-two-variable-polynomials',
        'c1-thm-function-space',
        'c2-lem-polynomial-coefficients',
        'c2-thm-span-smallest',
        'c2-def-basis',
        'c2-def-dimension',
        'c1-foundations',
    ],
    page=175,
    kind='lemma',
)

s.d(
    'def-polynomial-partial-derivatives',
    'Algebraic partial differentiation',
    r'''For the unique coefficient expression of
    $p\in\Poly_m(\C^2,\C)$, define
    \[
    D_wp=
    \sum_{\substack{j\ge1,\ k\ge0\\j+k\le m}}
    j a_{j,k}w^{j-1}z^k,
    \qquad
    D_zp=
    \sum_{\substack{j\ge0,\ k\ge1\\j+k\le m}}
    k a_{j,k}w^jz^{k-1}.
    \]
    Empty sums denote the zero function. These are the
    polynomial partial differentiation formulas; the
    definitions use coefficients and do not require
    differentiation theory for general complex functions.''',
    page=175,
)

s.r(
    'ex-partial-derivatives-commute',
    'Partial differentiation operators commute',
    r'''The maps $D_w,D_z$ are linear operators on
    $\Poly_m(\C^2,\C)$, and they commute.''',
    r'''Coefficient uniqueness makes both formulas well-defined.
    Each monomial that occurs in either output has total
    degree at most $m-1$, so it belongs to the original
    space when $m\ge1$. If $m=0$, both sums are empty
    and give its zero vector. Thus both maps have the
    required target.

    If $p,q$ have coefficient arrays $a_{j,k},b_{j,k}$,
    their sum has array $a_{j,k}+b_{j,k}$ and a scalar
    multiple $cp$ has array $ca_{j,k}$. In the formula
    for $D_w$, multiplication of each coefficient by $j$
    therefore gives
    $D_w(p+q)=D_wp+D_wq$ and $D_w(cp)=cD_wp$.
    In the formula for $D_z$, multiplication by $k$
    gives the same two identities with $D_z$.
    Hence both maps are linear.

    Applying the two formulas successively gives
    \[
    D_wD_zp=
    \sum_{\substack{j,k\ge1\\j+k\le m}}
    jk a_{j,k}w^{j-1}z^{k-1}
    =D_zD_wp.
    \]
    Terms whose relevant exponent is zero disappear
    at the corresponding differentiation step.
    If $m=0$ or $m=1$, the displayed sum is empty
    in both orders. Thus the outputs agree for every
    $p$ and the operators commute.''',
    2,
    20,
    [
        r'''Check linearity by following the coefficients.''',
        r'''Only terms involving positive powers of both variables can survive both operations.''',
    ],
    [
        'def-commute',
        'def-two-variable-polynomials',
        'lem-two-variable-basis',
        'def-polynomial-partial-derivatives',
        'c3-def-linear-map',
        'c3-def-map-composition',
        'c1-thm-complex-laws',
    ],
    '5.72',
    175,
    'example',
)

s.r(
    'thm-matrix-commutation',
    'Commutation is preserved by a matrix representation',
    r'''Let $S,T\in\Lin(V)$, where $V$ is finite-dimensional,
    and use the same fixed basis of $V$ for both operators.
    Then $S,T$ commute if and only if their matrices commute.''',
    r'''For the fixed basis, the composition rule gives
    \[
    \Mat(ST)=\Mat(S)\Mat(T),\qquad
    \Mat(TS)=\Mat(T)\Mat(S).
    \]
    If $ST=TS$, the two represented matrices are equal,
    proving matrix commutation. Conversely, if the two
    matrix products are equal, these formulas give
    $\Mat(ST)=\Mat(TS)$. The matrix representation is
    injective, so $ST=TS$.
    The matrix representation theorem includes empty
    bases, so the argument also covers $V=\{0\}$.''',
    1,
    10,
    [r'''Use the composition rule and the fact that a fixed-basis matrix determines its linear map.'''],
    [
        'def-commute',
        'c3-thm-matrix-composition',
        'c3-thm-map-matrix-isomorphism',
    ],
    '5.74',
    176,
)

s.r(
    'thm-commuting-eigenspace',
    'A commuting operator preserves every eigenspace',
    r'''If $S,T\in\Lin(V)$ commute and $\lambda\in\F$,
    then the eigenspace $E(\lambda,S)$ is invariant under $T$.
    No finite-dimensionality assumption is needed.''',
    r'''The eigenspace is a subspace. For
    $v\in E(\lambda,S)$, the equation $Sv=\lambda v$
    and the commutation hypothesis give
    \[
    S(Tv)=(ST)v=(TS)v=T(Sv)=T(\lambda v)=\lambda Tv.
    \]
    Thus $Tv\in E(\lambda,S)$, which is exactly the
    required invariance. This applies also when the
    eigenspace consists only of zero.''',
    1,
    10,
    [r'''Apply $S$ to $Tv$ and use commutation before using the eigenvalue equation.'''],
    [
        'def-commute',
        'def-eigenspace',
        'lem-eigenspace-subspace',
        'def-invariant',
        'c3-def-linear-map',
        'c3-def-map-composition',
    ],
    '5.75',
    176,
)

s.r(
    'thm-simultaneous-diagonalization',
    'Commuting diagonalizable operators have a shared eigenvector basis',
    r'''Let $S,T$ be diagonalizable operators on the same
    finite-dimensional vector space over $\F$.
    There is one basis in which both matrices are diagonal
    if and only if $S$ and $T$ commute.''',
    r'''Suppose a basis $v_1,\ldots,v_n$ diagonalizes both
    operators. There are scalars $\alpha_j,\beta_j$ with
    $Sv_j=\alpha_jv_j$ and $Tv_j=\beta_jv_j$.
    Linearity gives
    \[
    STv_j=\beta_j\alpha_jv_j
    =\alpha_j\beta_jv_j=TSv_j.
    \]
    Thus $ST$ and $TS$ agree on a basis and hence are
    equal.

    Conversely, suppose $ST=TS$. If $V=\{0\}$, the
    empty basis gives two empty diagonal matrices,
    so assume $V\ne\{0\}$.
    Since $S$ is diagonalizable, its distinct eigenvalues
    $\lambda_1,\ldots,\lambda_r$ give the decomposition
    \[
    V=E(\lambda_1,S)\oplus\cdots\oplus E(\lambda_r,S)
    \]
    by the diagonalizability characterization.
    Each of these subspaces is invariant under $T$
    by the commuting-eigenspace theorem.
    Since $T$ is diagonalizable, its restriction to
    each such subspace is diagonalizable.
    Choose in each eigenspace a basis consisting of
    eigenvectors of that restriction.

    Concatenate these chosen bases. They span $V$
    because the eigenspaces sum to $V$ and each
    chosen list spans its eigenspace. In a zero linear
    combination of the concatenated list, group the
    terms coming from each eigenspace. Directness
    makes each group sum zero, and independence of
    each chosen basis then makes every coefficient
    zero. Thus the concatenated list is a basis.

    Each member of this basis lies in an eigenspace
    of $S$ and is also an eigenvector of the relevant
    restriction of $T$, hence of $T$ itself.
    Its two images are therefore scalar multiples
    of that same basis vector. The matrix definition
    now gives diagonal matrices for both operators.
    This proves the converse.''',
    3,
    40,
    [
        r'''Decompose the space into eigenspaces of one of the diagonalizable operators.''',
        r'''Restrict the other operator to each of those invariant subspaces.''',
    ],
    [
        'def-commute',
        'def-diagonalizable',
        'def-diagonal-matrix',
        'def-eigenspace',
        'thm-diagonalizable-equivalences',
        'thm-diagonalizable-restriction',
        'thm-commuting-eigenspace',
        'c1-thm-direct-zero',
        'c2-def-basis',
        'c3-thm-linear-map-basis',
        'c3-def-map-matrix',
        'c3-def-linear-map',
    ],
    '5.76',
    176,
)

s.r(
    'thm-common-eigenvector',
    'A common eigenvector for two commuting complex operators',
    r'''If $V$ is a nonzero finite-dimensional complex vector
    space and $S,T\in\Lin(V)$ commute, there exist a vector
    $v\ne0$ and scalars $\lambda,\mu\in\C$ such that
    \[
    Sv=\lambda v,\qquad Tv=\mu v.
    \]
    The two eigenvalues are allowed to differ.''',
    r'''The complex eigenvalue existence theorem gives
    an eigenvalue $\lambda$ of $S$. Its eigenspace
    $E=E(\lambda,S)$ is therefore nonzero.
    It is a subspace of the finite-dimensional space
    $V$, so it is finite-dimensional.
    Commutation makes $E$ invariant under $T$,
    and hence $T|_E$ is an operator on the nonzero
    finite-dimensional complex space $E$.
    Apply complex eigenvalue existence again to obtain
    $\mu\in\C$ and $v\in E$ with $v\ne0$ and
    $T|_E v=\mu v$. The restriction agrees with $T$,
    so $Tv=\mu v$, while membership in $E$ gives
    $Sv=\lambda v$.''',
    2,
    20,
    [
        r'''Start with a nonzero eigenspace of one operator.''',
        r'''Apply eigenvalue existence to the restriction of the other operator to that space.''',
    ],
    [
        'thm-complex-eigenvalue',
        'def-eigenvalue',
        'def-eigenvector',
        'def-eigenspace',
        'lem-eigenspace-subspace',
        'def-invariant',
        'thm-commuting-eigenspace',
        'c2-thm-subspaces-finite',
    ],
    '5.78',
    177,
)

s.r(
    'ex-partial-common-eigenvectors',
    'The common eigenvectors of polynomial partial differentiation',
    r'''For the operators $D_w,D_z$ on $\Poly_m(\C^2,\C)$,
    each operator has only the eigenvalue $0$. Their zero
    eigenspaces are
    \[
    E(0,D_w)=
    \left\{\sum_{k=0}^m a_kz^k:a_k\in\C\right\},
    \qquad
    E(0,D_z)=
    \left\{\sum_{j=0}^m b_jw^j:b_j\in\C\right\}.
    \]
    Their common eigenvectors are precisely the nonzero
    constant functions.''',
    r'''For a monomial $w^jz^k$, applying $D_w$ once
    gives $j w^{j-1}z^k$ if $j\ge1$, and zero if
    $j=0$. Induction on $j$ therefore shows that
    $j+1$ applications give zero. Since $j\le m$,
    $D_w^{m+1}$ vanishes on every monomial in the
    basis and hence on the entire space by linearity.
    The same argument using $k$ gives $D_z^{m+1}=0$.

    If $D_wp=\lambda p$ with $p\ne0$, the
    polynomial-eigenvector formula gives
    $0=D_w^{m+1}p=\lambda^{m+1}p$.
    If $\lambda\ne0$, multiplication by the inverse
    of $\lambda^{m+1}$ would force $p=0$.
    Hence $\lambda=0$. The identical argument for
    $D_z$ excludes its nonzero eigenvalues.
    The constant function $1$ is nonzero and is
    killed by both operators, so $0$ is indeed an
    eigenvalue of each.

    Write $p=\sum_{j+k\le m}a_{j,k}w^jz^k$.
    The monomials in the formula
    \[
    D_wp=\sum_{\substack{j\ge1,\ k\ge0\\j+k\le m}}
    j a_{j,k}w^{j-1}z^k
    \]
    have distinct exponent pairs. Coefficient uniqueness
    makes this output zero exactly when
    $j a_{j,k}=0$ for every $j\ge1$.
    Such positive integers are nonzero complex scalars,
    so this is equivalent to $a_{j,k}=0$ whenever
    $j\ge1$. Thus $p$ depends only on $z$, giving
    the first eigenspace. Applying the same reasoning
    to $D_z$ gives the second eigenspace.

    Membership in both eigenspaces leaves only the
    coefficient $a_{0,0}$, so their intersection is
    the space of constant functions. An eigenvector
    must be nonzero, and therefore the common
    eigenvectors are exactly the nonzero constants.
    For $m=0$ the whole space already consists of
    constants, and all these arguments and conclusions
    still apply.''',
    3,
    30,
    [
        r'''Repeated differentiation eventually kills every monomial.''',
        r'''Use coefficient uniqueness to describe the kernel of each partial differentiation operator.''',
    ],
    [
        'def-two-variable-polynomials',
        'lem-two-variable-basis',
        'def-polynomial-partial-derivatives',
        'ex-partial-derivatives-commute',
        'def-operator-powers',
        'lem-polynomial-eigenvector',
        'def-eigenvector',
        'def-eigenspace',
        'c1-thm-complex-inverses',
        'c1-lem-scalar-cancellation',
        'c3-thm-linear-zero',
        'c3-thm-linear-map-basis',
    ],
    '5.79',
    177,
    'example',
)

s.r(
    'lem-commuting-quotients',
    'Commuting operators descend to a common invariant quotient',
    r'''Let $S,T\in\Lin(V)$ commute, and let $U$ be a subspace
    invariant under both. The prescriptions
    \[
    \overline S(v+U)=Sv+U,\qquad
    \overline T(v+U)=Tv+U
    \]
    define commuting linear operators on $V/U$.''',
    r'''If $v+U=w+U$, the coset equality criterion gives
    $v-w\in U$. Since $U$ is invariant under $S$,
    $Sv-Sw=S(v-w)\in U$, and hence $Sv+U=Sw+U$.
    The same argument with $T$ gives $Tv+U=Tw+U$.
    Thus both prescriptions are independent of the
    chosen representative.

    For either $A=S$ or $A=T$, the quotient operation
    rules and linearity of $A$ give
    \[
    \begin{aligned}
    \overline A((v+U)+(w+U))
      &=A(v+w)+U\\
      &=(Av+U)+(Aw+U),\\
    \overline A(a(v+U))
      &=A(av)+U=a(Av+U).
    \end{aligned}
    \]
    Hence the induced maps are linear.
    Finally, for every coset $v+U$,
    \[
    (\overline S\,\overline T)(v+U)
    =STv+U=TSv+U
    =(\overline T\,\overline S)(v+U).
    \]
    Equality on all cosets proves commutation.''',
    2,
    20,
    [
        r'''Use the coset equality criterion to check that the prescriptions do not depend on representatives.''',
        r'''Evaluate both induced compositions on the same coset.''',
    ],
    [
        'def-commute',
        'def-invariant',
        'c3-thm-coset-equality',
        'c3-def-quotient-operations',
        'c3-thm-quotient-vector-space',
        'c3-def-linear-map',
        'c3-def-map-composition',
    ],
    page=178,
    kind='lemma',
)

s.r(
    'thm-simultaneous-triangularization',
    'Commuting complex operators have a shared triangular basis',
    r'''If $S,T$ are commuting operators on a finite-dimensional
    complex vector space $V$, then some basis of $V$ gives
    upper-triangular matrices for both operators.''',
    r'''We induct on $n=\dim V$. For $n=0$, the empty basis
    gives empty upper-triangular matrices.
    Assume $n\ge1$ and that the assertion holds for
    all complex spaces of dimension $n-1$.

    Choose a common eigenvector $v_1\ne0$ of $S,T$,
    using the common-eigenvector theorem. The line
    $L=\Span(v_1)$ has dimension one and is invariant
    under both operators. They therefore induce
    commuting operators $\overline S,\overline T$
    on $V/L$ by the preceding lemma.
    The quotient dimension theorem gives
    $\dim(V/L)=n-1$, so the induction hypothesis
    supplies a basis $\overline v_2,\ldots,\overline v_n$
    of $V/L$ that makes both induced operators
    upper triangular. For $n=1$, this is the empty
    basis of the zero quotient.

    Choose representatives $v_j\in V$ with
    $\overline v_j=v_j+L$ for $2\le j\le n$.
    To show that $v_1,\ldots,v_n$ spans $V$, expand
    $v+L$ in the quotient basis for an arbitrary
    $v\in V$. The expansion says that
    $v-\sum_{j=2}^n a_jv_j$ belongs to $L$,
    so it is a multiple of $v_1$.
    To prove independence, a zero relation among
    $v_1,\ldots,v_n$ gives in the quotient a zero
    relation among $\overline v_2,\ldots,\overline v_n$.
    Thus all coefficients except possibly the first
    are zero. The remaining coefficient is zero
    because $v_1\ne0$. Hence the lifted list is a
    basis of $V$.

    For $j\ge2$, upper triangularity in the quotient
    means that
    \[
    \overline S\,\overline v_j,\quad
    \overline T\,\overline v_j
    \in\Span(\overline v_2,\ldots,\overline v_j).
    \]
    Lifting either relation shows that the corresponding
    image $Sv_j$ or $Tv_j$ differs from a combination
    of $v_2,\ldots,v_j$ by a vector in
    $L=\Span(v_1)$. Therefore
    \[
    Sv_j,\ Tv_j\in\Span(v_1,\ldots,v_j).
    \]
    For $j=1$, the same assertion follows from
    the common eigenvector equations.
    The triangular basis criterion now shows that
    both matrices in the lifted basis are upper triangular,
    completing the induction.''',
    4,
    60,
    [
        r'''Begin with a common eigenvector and pass to the quotient by its span.''',
        r'''Apply induction to the two induced operators, then lift a quotient basis.''',
        r'''A triangular relation in the quotient may acquire only a multiple of the first basis vector when lifted.''',
    ],
    [
        'thm-common-eigenvector',
        'lem-invariant-line',
        'lem-commuting-quotients',
        'def-upper-triangular',
        'thm-triangular-invariant',
        'c2-def-span',
        'c2-def-basis',
        'c2-ex-single-independent',
        'c3-def-quotient-space',
        'c3-def-quotient-operations',
        'c3-thm-coset-equality',
        'c3-thm-quotient-dimension',
    ],
    '5.80',
    178,
)

s.r(
    'lem-triangular-sum-product',
    'Diagonals of sums and products of upper-triangular matrices',
    r'''If $A,B$ are upper-triangular $n$-by-$n$ matrices,
    then $A+B$ and $AB$ are upper triangular, and
    \[
    (A+B)_{j,j}=A_{j,j}+B_{j,j},\qquad
    (AB)_{j,j}=A_{j,j}B_{j,j}
    \quad(1\le j\le n).
    \]''',
    r'''For $j>k$, both $A_{j,k}$ and $B_{j,k}$ are zero,
    so $(A+B)_{j,k}=0$. The diagonal formula for the
    sum is the definition of matrix addition.

    For a product entry with $j>k$,
    \[
    (AB)_{j,k}=\sum_{r=1}^n A_{j,r}B_{r,k}.
    \]
    If $r<j$, upper triangularity gives $A_{j,r}=0$.
    If $r\ge j$, then $r>k$, so upper triangularity
    gives $B_{r,k}=0$. Every summand is therefore zero,
    proving that $AB$ is upper triangular.

    For $(AB)_{j,j}$, terms with $r<j$ have
    $A_{j,r}=0$, and terms with $r>j$ have
    $B_{r,j}=0$. Only $r=j$ remains, giving
    $(AB)_{j,j}=A_{j,j}B_{j,j}$.
    If $n=0$, the matrices and their sum and product
    have the empty square shape; triangularity holds
    and there are no diagonal entries to check.''',
    2,
    15,
    [r'''Determine which indices can give a nonzero summand in a product entry.'''],
    [
        'def-upper-triangular',
        'c3-def-matrix-addition',
        'c3-def-matrix-product',
    ],
    page=179,
    kind='lemma',
)

s.r(
    'thm-commuting-sum-product-eigenvalues',
    'Eigenvalues of sums and products of commuting operators',
    r'''Let $S,T$ be commuting operators on a finite-dimensional
    complex vector space. Every eigenvalue of $S+T$ is
    $\lambda+\mu$ for some eigenvalue $\lambda$ of $S$
    and some eigenvalue $\mu$ of $T$. Every eigenvalue
    of $ST$ is $\lambda\mu$ for some such pair.''',
    r'''If the space is zero, none of these operators has
    an eigenvalue, because no nonzero eigenvector exists.
    The two assertions then hold vacuously.

    Otherwise choose a basis giving upper-triangular
    matrices $A=\Mat(S)$ and $B=\Mat(T)$, using
    simultaneous triangularization. The matrix rules
    give $\Mat(S+T)=A+B$ and $\Mat(ST)=AB$.
    The preceding lemma makes both matrices upper
    triangular and identifies their diagonal entries.

    Let $\nu$ be an eigenvalue of $S+T$. The triangular
    eigenvalue theorem gives an index $j$ with
    \[
    \nu=(A+B)_{j,j}=A_{j,j}+B_{j,j}.
    \]
    The same theorem applied to $S$ and $T$ says
    that $A_{j,j}$ is an eigenvalue of $S$ and
    $B_{j,j}$ is an eigenvalue of $T$.
    These two scalars provide the required sum.
    If instead $\nu$ is an eigenvalue of $ST$,
    that theorem gives an index $j$ with
    \[
    \nu=(AB)_{j,j}=A_{j,j}B_{j,j}.
    \]
    The two factors are again eigenvalues of the
    original operators. This proves the product assertion.''',
    2,
    20,
    [
        r'''Use one basis that makes both operators upper triangular.''',
        r'''Read the eigenvalues from the diagonal entries of the sum and product matrices.''',
    ],
    [
        'def-eigenvalue',
        'thm-simultaneous-triangularization',
        'lem-triangular-sum-product',
        'thm-triangular-eigenvalues',
        'c3-thm-matrix-addition',
        'c3-thm-matrix-composition',
    ],
    '5.81',
    179,
)

s.card(
    'commute-definition',
    'def-commute',
    r'''What does it mean for two operators on the same space to commute?''',
    r'''Their compositions agree in the two orders: $ST=TS$.''',
)

s.card(
    'two-variable-coefficients',
    'lem-two-variable-basis',
    r'''How can uniqueness of coefficients for a polynomial in two variables be reduced to the univariate case?''',
    r'''Fix one variable, apply univariate coefficient uniqueness
    in the other variable, then apply it again to the resulting
    coefficient polynomials.''',
)

s.card(
    'commuting-eigenspace',
    'thm-commuting-eigenspace',
    r'''What does commutation imply about the eigenspaces of one operator?''',
    r'''Every eigenspace of either operator is invariant under
    the other operator.''',
)

s.card(
    'simultaneous-diagonalization',
    'thm-simultaneous-diagonalization',
    r'''When do two diagonalizable operators have a common diagonalizing basis?''',
    r'''Exactly when they commute.''',
)

s.card(
    'common-eigenvector-idea',
    'thm-common-eigenvector',
    r'''How do two commuting operators on a nonzero finite-dimensional complex space acquire a common eigenvector?''',
    r'''Choose a nonzero eigenspace of one operator and find
    an eigenvector of the restriction of the other operator
    to that invariant eigenspace.''',
)

s.card(
    'partial-common-eigenvectors',
    'ex-partial-common-eigenvectors',
    r'''Which functions are common eigenvectors of the two polynomial partial differentiation operators?''',
    r'''Exactly the nonzero constant functions. Both eigenvalues are zero.''',
)

s.card(
    'shared-triangular-basis',
    'thm-simultaneous-triangularization',
    r'''What quotient is used in the induction proving simultaneous triangularization?''',
    r'''The quotient by the line spanned by a common eigenvector.
    Both operators descend to commuting operators on this
    quotient of dimension one less.''',
)

s.card(
    'triangular-product-diagonal',
    'lem-triangular-sum-product',
    r'''What is the $j$th diagonal entry of a product of two upper-triangular matrices?''',
    r'''It is $A_{j,j}B_{j,j}$; every other term in the entry's
    defining sum vanishes.''',
)

s.card(
    'commuting-sum-product-spectrum',
    'thm-commuting-sum-product-eigenvalues',
    r'''How are the eigenvalues of the sum and product of two commuting complex operators related to those of the individual operators?''',
    r'''Each eigenvalue of the sum is a sum of one eigenvalue
    from each operator, and each eigenvalue of the product
    is a product of one eigenvalue from each operator.''',
)

s.write()
