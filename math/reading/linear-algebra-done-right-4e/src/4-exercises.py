from common import Section

s = Section('4-exercises')

s.p(
    'exercises-intro',
    'Optional practice with scalars and polynomials',
    r'''These optional exercises develop complex arithmetic, polynomial
    division, interpolation, and factorization. Each exercise can be
    solved using the chapter's results and Chapters 1 and 2, without
    relying on another exercise in this section.''',
    129,
)

s.r(
    'ex-parallelogram-modulus',
    'A quadratic identity for complex moduli',
    r'''For $z,w\in\C$, prove
    \[
    |z+w|^2+|z-w|^2=2|z|^2+2|w|^2.
    \]''',
    r'''The conjugation identities and the formula
    $|u|^2=u\overline u$ give
    \[
    |z+w|^2=(z+w)(\overline z+\overline w)
    =z\overline z+z\overline w+w\overline z+w\overline w
    \]
    and
    \[
    |z-w|^2=(z-w)(\overline z-\overline w)
    =z\overline z-z\overline w-w\overline z+w\overline w.
    \]
    Adding cancels the two mixed terms and yields
    $2z\overline z+2w\overline w=2|z|^2+2|w|^2$.''',
    1,
    10,
    [r'''Replace each squared modulus by a number times its conjugate.'''],
    ['def-conjugate-modulus', 'thm-complex-properties'],
    page=129,
    kind='exercise',
    optional=True,
)

s.r(
    'ex-stability-of-distance',
    'Moving a point changes its distance by at most the movement',
    r'''For $a,z,w\in\C$, prove
    \[
    \bigl||z-a|-|w-a|\bigr|\le |z-w|.
    \]''',
    r'''Using $z-a=(z-w)+(w-a)$, the triangle inequality gives
    $|z-a|\le |z-w|+|w-a|$. Therefore
    $|z-a|-|w-a|\le |z-w|$.
    Interchanging $z$ and $w$ gives
    $|w-a|-|z-a|\le |w-z|=|z-w|$.
    The real number $|z-a|-|w-a|$ thus lies between
    $-|z-w|$ and $|z-w|$, which is exactly the asserted
    absolute-value bound.''',
    2,
    15,
    [r'''Apply the triangle inequality once with each point playing the role of the endpoint.'''],
    ['def-conjugate-modulus', 'thm-complex-properties', 'c1-foundations'],
    page=129,
    kind='exercise',
    optional=True,
)

s.r(
    'ex-unit-circle-quotient',
    'Recognizing real numbers through a quotient',
    r'''For $z\in\C$ with $z\ne-i$, prove
    \[
    \left|\frac{z-i}{z+i}\right|=1
    \quad\Longleftrightarrow\quad z\in\R.
    \]''',
    r'''For any nonzero complex number $u$, multiplicativity
    of modulus applied to $uu^{-1}=1$ gives
    $|u||u^{-1}|=1$. Hence $|u^{-1}|=1/|u|$.
    The hypothesis $z\ne-i$ therefore gives
    \[
    \left|\frac{z-i}{z+i}\right|
    =\frac{|z-i|}{|z+i|}.
    \]
    Since the denominator is positive, this equals $1$
    exactly when $|z-i|=|z+i|$.

    Write $z=a+bi$ with real $a,b$. Squaring the two
    nonnegative moduli shows that their equality is equivalent to
    \[
    a^2+(b-1)^2=a^2+(b+1)^2.
    \]
    Expanding and cancelling gives $4b=0$, and hence $b=0$.
    Conversely, $b=0$ makes the two squared moduli, and therefore
    the two moduli, equal. Finally $b=0$ means exactly that
    $z$ is real.''',
    2,
    20,
    [
        r'''First turn the modulus of the quotient into a quotient of moduli.''',
        r'''Write $z=a+bi$ and compare the squares of the two moduli.''',
    ],
    [
        'def-real-imaginary',
        'def-conjugate-modulus',
        'thm-complex-properties',
        'c1-thm-complex-inverses',
        'c1-lem-scalar-cancellation',
    ],
    page=129,
    kind='exercise',
    optional=True,
)

s.r(
    'ex-polynomial-cancellation',
    'Cancellation and equality of polynomial squares',
    r'''Let $p,q,r\in\Poly(\F)$ with $p\ne0$. Prove that
    $pq=pr$ implies $q=r$. Deduce that, for arbitrary
    $f,g\in\Poly(\F)$, the identity $f^2=g^2$ implies
    $f=g$ or $f=-g$.''',
    r'''From $pq=pr$, distributivity gives $p(q-r)=0$.
    If $q-r$ were nonzero, the product-degree theorem would
    make $p(q-r)$ a nonzero polynomial of degree
    $\deg p+\deg(q-r)$. This contradicts its being zero.
    Thus $q-r=0$, so $q=r$.

    Now suppose $f^2=g^2$. The polynomial identity
    $(f-g)(f+g)=f^2-g^2$ gives $(f-g)(f+g)=0$.
    If $f-g=0$, then $f=g$. Otherwise the first part,
    with nonzero factor $f-g$, cancels that factor from
    $(f-g)(f+g)=(f-g)0$ and gives $f+g=0$.
    Thus $f=-g$ in the remaining case.''',
    2,
    15,
    [r'''A product of two nonzero polynomials cannot be the zero polynomial.'''],
    [
        'lem-polynomial-product-degree',
        'c2-def-polynomial',
        'c1-thm-complex-laws',
    ],
    page=130,
    kind='exercise',
    optional=True,
)

s.r(
    'ex-even-polynomials',
    'Even functions and even degrees are different conditions',
    r'''For a nonnegative integer $m$, let
    \[
    E_m=\{p\in\Poly_{2m}(\F):p(-x)=p(x)\text{ for all }x\in\F\}.
    \]
    Prove that $E_m$ is a subspace with basis
    $1,x^2,\ldots,x^{2m}$ and dimension $m+1$.
    In contrast, prove that the set consisting of zero and all
    nonzero polynomials of even degree is not a subspace of
    $\Poly(\F)$.''',
    r'''Write $p(x)=\sum_{j=0}^{2m}a_jx^j$. Then
    \[
    p(-x)-p(x)=\sum_{j=0}^{2m}\bigl((-1)^j-1\bigr)a_jx^j.
    \]
    Coefficient uniqueness says that this polynomial is zero
    exactly when every displayed coefficient is zero.
    For even $j$ there is no restriction. For odd $j$ the
    condition is $-2a_j=0$, which is equivalent to $a_j=0$
    because $2\ne0$ in $\F$.
    Hence $E_m$ is precisely the span of $1,x^2,\ldots,x^{2m}$,
    and is a subspace. Coefficient uniqueness also shows that
    this list is independent. It is therefore a basis with
    $m+1$ entries. The argument includes $m=0$, when the
    list consists just of $1$.

    For the contrasting set, both $x^2+x$ and $-x^2$ have
    even degree $2$, whereas their sum is the nonzero
    polynomial $x$, of odd degree $1$. The set is not closed
    under addition and thus is not a subspace.''',
    2,
    20,
    [
        r'''Compare coefficients in $p(-x)=p(x)$.''',
        r'''For the second assertion, arrange for the leading even-degree terms to cancel.''',
    ],
    [
        'c2-def-polynomial',
        'c2-def-polynomial-space',
        'c2-lem-polynomial-coefficients',
        'c2-thm-span-smallest',
        'c2-def-basis',
        'c2-def-dimension',
        'c1-thm-subspace-test',
        'c1-lem-scalar-cancellation',
        'c1-lem-scalar-powers',
    ],
    page=130,
    kind='exercise',
    optional=True,
)

s.r(
    'ex-two-point-remainder',
    'A remainder determined by two values',
    r'''Let $a,b\in\F$ be distinct and $p\in\Poly(\F)$.
    Prove that the remainder after division of $p(x)$ by
    $(x-a)(x-b)$ is
    \[
    r(x)=p(a)\frac{x-b}{a-b}+p(b)\frac{x-a}{b-a}.
    \]''',
    r'''Polynomial division gives
    $p(x)=(x-a)(x-b)q(x)+u(x)$, where $u=0$ or
    $\deg u<2$. Thus $u\in\Poly_1(\F)$, and evaluating
    at $a$ and $b$ gives $u(a)=p(a)$ and $u(b)=p(b)$.

    The displayed candidate $r$ is well-defined because
    $a-b$ and $b-a$ are nonzero. It belongs to
    $\Poly_1(\F)$ and satisfies $r(a)=p(a)$ and $r(b)=p(b)$.
    Therefore $u-r$ belongs to $\Poly_1(\F)$ and vanishes
    at the two distinct points $a,b$. If $u-r$ were nonzero,
    the root bound would allow at most one distinct root.
    Hence $u-r=0$, so the division remainder is $r$.''',
    2,
    20,
    [
        r'''Evaluate the division identity at the two roots of the divisor.''',
        r'''A polynomial of degree at most one is determined by its values at two distinct points.''',
    ],
    [
        'thm-polynomial-division',
        'thm-root-bound',
        'c2-def-polynomial-space',
        'c1-thm-complex-inverses',
    ],
    page=130,
    kind='exercise',
    optional=True,
)

s.r(
    'ex-imaginary-values-real-inputs',
    'Imaginary values force imaginary coefficients',
    r'''Let $p\in\Poly_n(\C)$, where $n\ge0$. Suppose there are
    $n+1$ distinct real numbers $t_0,\ldots,t_n$ for which
    $p(t_j)\in i\R$. Prove that $p=iq$ for some
    $q\in\Poly_n(\R)$.''',
    r'''Write $p(z)=\sum_{k=0}^n a_kz^k$, and define the real
    polynomial
    \[
    u(x)=\sum_{k=0}^n\operatorname{Re}(a_k)x^k.
    \]
    Because $x$ is real, the real part of $p(x)$ equals
    $u(x)$. Thus $u(t_j)=0$ for all $j$, by the hypothesis
    on the values of $p$. A nonzero polynomial of degree
    at most $n$ cannot have $n+1$ distinct roots, so
    $u=0$. Coefficient uniqueness gives
    $\operatorname{Re}(a_k)=0$ for every $k$.

    Write $a_k=ib_k$ with $b_k\in\R$. Then
    $q(x)=\sum_{k=0}^n b_kx^k$ belongs to $\Poly_n(\R)$
    and $p=iq$. This also covers the zero polynomial and
    the case $n=0$.''',
    2,
    20,
    [
        r'''Form a real polynomial from the real parts of the coefficients.''',
        r'''Use the number of prescribed zeros of that real polynomial.''',
    ],
    [
        'def-real-imaginary',
        'thm-complex-properties',
        'thm-root-bound',
        'c2-def-polynomial-space',
        'c2-lem-polynomial-coefficients',
    ],
    page=131,
    kind='exercise',
    optional=True,
)

s.r(
    'ex-real-polynomial-prescribed-root-set',
    'Which finite sets are root sets of real polynomials?',
    r'''Let $S$ be a finite subset of $\C$. Prove that there is a
    nonzero polynomial with real coefficients whose complex root
    set is exactly $S$ if and only if $S$ is closed under
    complex conjugation. When this condition holds, prove that
    there is exactly one such polynomial of degree $|S|$
    whose leading coefficient is $1$.''',
    r'''If a polynomial has real coefficients, the conjugate-root
    theorem shows that conjugation preserves its root set.
    This proves necessity.

    Conversely, suppose $S$ is closed under conjugation.
    For $S\ne\varnothing$, define
    \[
    P(z)=\prod_{\lambda\in S}(z-\lambda).
    \]
    Each real member of $S$ supplies a factor with real
    coefficients. The nonreal members can be partitioned
    into disjoint pairs $\lambda,\overline\lambda$, and
    each pair supplies
    \[
    (z-\lambda)(z-\overline\lambda)
    =z^2-2\operatorname{Re}(\lambda)z+|\lambda|^2,
    \]
    also with real coefficients. Hence $P$ has real
    coefficients. Its leading coefficient is $1$ and its
    degree is $|S|$ by the product-degree theorem.
    At a member of $S$ one factor is zero. Outside $S$
    every factor is nonzero, and their product is nonzero
    by repeated scalar cancellation. Its root set is
    therefore exactly $S$.
    If $S=\varnothing$, take the constant polynomial $P=1$.

    For uniqueness when $r=|S|\ge1$, let $Q$ be another
    polynomial of degree $r$ with leading coefficient $1$
    that vanishes at every member of $S$. The leading
    terms cancel in $P-Q$, so this difference is zero or
    has degree at most $r-1$. It vanishes at the $r$
    distinct elements of $S$, and the root bound forces
    it to be zero. When $r=0$, the only degree-zero
    polynomial with leading coefficient $1$ is $1$.
    Thus uniqueness holds in every case.''',
    3,
    30,
    [
        r'''Pair each nonreal prescribed root with its conjugate.''',
        r'''For uniqueness, subtract two candidates so their leading terms cancel.''',
    ],
    [
        'thm-conjugate-roots',
        'thm-complex-properties',
        'lem-polynomial-product-degree',
        'thm-root-bound',
        'c2-def-polynomial',
        'c1-lem-scalar-cancellation',
    ],
    page=130,
    kind='exercise',
    optional=True,
)

s.r(
    'ex-polynomial-conjugate-product',
    'A polynomial encoding a squared modulus',
    r'''For $p(z)=\sum_{j=0}^n a_jz^j\in\Poly(\C)$, define
    \[
    p^*(z)=\sum_{j=0}^n\overline{a_j}z^j.
    \]
    Prove that $p(z)p^*(z)$ has real coefficients and that,
    for real $x$,
    \[
    p(x)p^*(x)=|p(x)|^2.
    \]
    If $p\ne0$ has degree $n$, determine the degree and
    leading coefficient of $pp^*$.''',
    r'''The coefficient of $z^k$ in $pp^*$ is
    \[
    c_k=\sum_{\substack{0\le j,\ell\le n\\j+\ell=k}}
    a_j\overline{a_\ell}.
    \]
    Conjugating gives
    \[
    \overline{c_k}
    =\sum_{j+\ell=k}\overline{a_j}a_\ell
    =\sum_{j+\ell=k}a_j\overline{a_\ell}=c_k,
    \]
    where the middle equality exchanges the two finite
    summation indices. A complex number equal to its
    conjugate has zero imaginary part, so each $c_k$ is real.

    For real $x$, conjugation fixes every $x^j$.
    Therefore $p^*(x)=\overline{p(x)}$, and
    $p(x)p^*(x)=p(x)\overline{p(x)}=|p(x)|^2$.

    If $p$ has degree $n$, then $a_n\ne0$, and
    $\overline{a_n}\ne0$ by involution of conjugation.
    Thus $p^*$ also has degree $n$. The product-degree
    theorem gives degree $2n$, and the leading coefficient
    is $a_n\overline{a_n}=|a_n|^2>0$.
    The first two assertions also hold when $p=0$.''',
    2,
    20,
    [
        r'''Compare each coefficient of the product with its own conjugate.''',
        r'''At real inputs, coefficientwise conjugation agrees with conjugation of the polynomial value.''',
    ],
    [
        'def-conjugate-modulus',
        'thm-complex-properties',
        'lem-polynomial-product-degree',
        'c2-def-polynomial',
    ],
    page=130,
    kind='exercise',
    optional=True,
)

s.r(
    'ex-dimension-vanishing-constraints',
    'Counting independent root constraints',
    r'''Let $n\ge0$, let $0\le r\le n+1$, and let
    $a_1,\ldots,a_r$ be distinct elements of $\F$. Set
    \[
    U=\{p\in\Poly_n(\F):p(a_j)=0\text{ for }1\le j\le r\},
    \qquad Q(x)=\prod_{j=1}^r(x-a_j),
    \]
    with empty product $Q=1$. Prove that $U$ is a subspace
    of dimension $n+1-r$. For $r\le n$, prove that
    $Q,xQ,\ldots,x^{n-r}Q$ is a basis; for $r=n+1$,
    identify the basis.''',
    r'''First suppose $r\le n$. We show that the members of
    $U$ are exactly the polynomials $Qh$ with
    $h\in\Poly_{n-r}(\F)$.
    Such products belong to $\Poly_n(\F)$ by the product-degree
    formula when $h\ne0$, and the zero case also belongs.
    They vanish at every prescribed point.

    For the converse, take nonzero $p\in U$. Factor off
    $(x-a_1)$ using the factor-root theorem. More generally,
    if
    \[
    p(x)=\prod_{j=1}^{k-1}(x-a_j)h(x),
    \]
    evaluation at $a_k$ shows $h(a_k)=0$, because all
    factors $a_k-a_j$ are nonzero. Factor off $(x-a_k)$.
    Continuing through all $r$ points gives $p=Qh$.
    The product-degree theorem gives
    $\deg h=\deg p-r\le n-r$. For $p=0$ take $h=0$.
    If $r=0$, the same conclusion is simply $p=1p$.

    Expanding $h$ in powers of $x$ now proves that
    $U=\Span(Q,xQ,\ldots,x^{n-r}Q)$, so $U$ is a subspace.
    If a combination of this list is zero, it has the
    form $Qg=0$, where
    $g=\sum_{k=0}^{n-r}b_kx^k$. The polynomial $Q$ is
    nonzero. If $g$ were nonzero, the product-degree
    theorem would make $Qg$ nonzero. Thus $g=0$,
    and coefficient uniqueness gives all $b_k=0$.
    The list is therefore a basis with $n+1-r$ entries.

    If $r=n+1$, the root bound forces every $p\in U$
    to be zero. Hence $U=\{0\}$, its basis is the
    empty list, and its dimension is $0=n+1-r$.''',
    3,
    40,
    [
        r'''Factor out the product of the prescribed linear factors.''',
        r'''After removing those factors, identify the remaining degree bound.''',
    ],
    [
        'thm-factor-root',
        'thm-root-bound',
        'lem-polynomial-product-degree',
        'c1-lem-scalar-cancellation',
        'c2-def-polynomial-space',
        'c2-lem-polynomial-coefficients',
        'c2-thm-span-smallest',
        'c2-def-basis',
        'c2-def-dimension',
        'c2-lem-zero-dimension',
    ],
    page=130,
    kind='exercise',
    optional=True,
)

s.r(
    'ex-lagrange-basis',
    'Interpolation and identities from a nodal basis',
    r'''Let $a_0,\ldots,a_n$ be distinct elements of $\F$,
    where $n\ge0$, and define
    \[
    L_j(x)=\prod_{\substack{0\le k\le n\\k\ne j}}
    \frac{x-a_k}{a_j-a_k}.
    \]
    Prove that $L_0,\ldots,L_n$ is a basis of $\Poly_n(\F)$
    and that
    \[
    p(x)=\sum_{j=0}^n p(a_j)L_j(x)
    \qquad(p\in\Poly_n(\F)).
    \]
    When $n\ge1$, deduce
    \[
    \sum_{j=0}^n\frac{1}{\prod_{k\ne j}(a_j-a_k)}=0,
    \qquad
    \sum_{j=0}^n\frac{a_j^n}{\prod_{k\ne j}(a_j-a_k)}=1.
    \]''',
    r'''The denominators are nonzero because the nodes are
    distinct. Each $L_j$ has degree at most $n$, and direct
    substitution gives $L_j(a_i)=0$ for $i\ne j$ and
    $L_j(a_j)=1$.
    Therefore a relation $\sum_j c_jL_j=0$, evaluated at
    $a_i$, gives $c_i=0$. The list is independent.
    It has $n+1=\dim\Poly_n(\F)$ entries, so it is a basis.

    For a given $p$, subtract the proposed interpolation
    expression from $p$. The difference belongs to
    $\Poly_n(\F)$ and is zero at every $a_i$. The root
    bound makes the difference zero, proving the formula.
    When $n=0$, the empty product gives $L_0=1$, and
    the argument states that a constant polynomial is
    its constant value.

    For $n\ge1$, apply the interpolation formula first
    to $p=1$ and then to $p=x^n$. The coefficient of
    $x^n$ in $L_j$ is
    $1/\prod_{k\ne j}(a_j-a_k)$. Comparing the coefficients
    of $x^n$ in the two identities gives respectively
    the claimed sums $0$ and $1$.''',
    3,
    30,
    [
        r'''Compute the values of each $L_j$ at every node.''',
        r'''For the final identities, compare the leading coefficients in the interpolation formulas for two simple polynomials.''',
    ],
    [
        'thm-root-bound',
        'c2-def-polynomial-space',
        'c2-lem-polynomial-coefficients',
        'c2-ex-polynomial-dimension',
        'c2-thm-full-length-independent',
        'c2-def-basis',
    ],
    page=130,
    kind='exercise',
    optional=True,
)

s.r(
    'ex-no-real-roots-sign',
    'A real polynomial without real roots',
    r'''Suppose a nonzero real polynomial $p$ has no real roots.
    Prove that its degree is even and that $p(x)$ has the
    same sign for every real $x$, namely the sign of its
    leading coefficient. Deduce that every real polynomial
    of odd degree has a real root.''',
    r'''A nonzero constant polynomial has degree zero and
    already satisfies the assertions. For a nonconstant
    $p$, its real factorization cannot contain a real
    linear factor, because such a factor would give a
    real root. Thus
    \[
    p(x)=c\prod_{j=1}^M(x^2+b_jx+d_j),
    \qquad b_j^2<4d_j,
    \]
    with nonzero real $c$. Each quadratic satisfies
    \[
    x^2+b_jx+d_j
    =\left(x+\frac{b_j}{2}\right)^2+
    d_j-\frac{b_j^2}{4}>0
    \]
    for every real $x$. Hence the product has sign equal
    to the sign of $c$ at every real input.
    Its degree is $2M$, and $c$ is its leading coefficient.
    This proves both assertions.

    A polynomial of odd degree is nonzero and has degree
    that is not even. It therefore cannot satisfy the
    no-real-root hypothesis just analyzed. It must have
    a real root.''',
    2,
    20,
    [
        r'''Use the real factorization theorem and determine which factors are permitted.''',
        r'''Complete the square in each irreducible quadratic factor.''',
    ],
    [
        'thm-real-factorization',
        'thm-real-quadratic',
        'lem-polynomial-product-degree',
        'c1-foundations',
    ],
    page=130,
    kind='exercise',
    optional=True,
)

s.r(
    'ex-imaginary-roots-parity',
    'Purely imaginary roots force a parity pattern',
    r'''Let $p$ be a nonzero real polynomial of degree $n$.
    Suppose every complex root of $p$ is purely imaginary,
    where zero is allowed. Prove
    \[
    p(-x)=(-1)^n p(x).
    \]
    Deduce that the coefficients whose indices have parity
    opposite to $n$ are zero.''',
    r'''A constant polynomial has $n=0$ and satisfies the
    conclusion. For a nonconstant polynomial, use its real
    factorization. A real root that is also purely imaginary
    must be zero, so every real linear factor is $x$.
    Consider an irreducible quadratic factor
    $x^2+bx+d$, where $b^2<4d$. The complex number
    \[
    \lambda=-\frac b2+i\sqrt{d-\frac{b^2}{4}}
    \]
    is a root, because substituting it into
    $(x+b/2)^2+d-b^2/4$ gives zero. It is therefore a
    root of $p$. The hypothesis gives
    $\operatorname{Re}\lambda=-b/2=0$, so $b=0$.

    Consequently the factorization has the form
    \[
    p(x)=c x^r\prod_{j=1}^M(x^2+d_j),
    \qquad d_j>0,
    \]
    with $n=r+2M$. Replacing $x$ by $-x$ multiplies this
    expression by $(-1)^r=(-1)^n$, proving the identity.

    Write $p(x)=\sum_{k=0}^n a_kx^k$. Coefficient uniqueness
    in $p(-x)=(-1)^n p(x)$ gives
    $\bigl((-1)^k-(-1)^n\bigr)a_k=0$ for every $k$.
    When $k$ has parity opposite to $n$, the first factor
    is $2$ or $-2$, so $a_k=0$.''',
    3,
    35,
    [
        r'''Inspect the real linear and irreducible quadratic factors separately.''',
        r'''A root of $x^2+bx+d$ with negative discriminant has real part $-b/2$.''',
    ],
    [
        'def-real-imaginary',
        'thm-real-factorization',
        'thm-real-quadratic',
        'lem-polynomial-product-degree',
        'c1-def-complex',
        'c1-foundations',
        'c1-lem-scalar-cancellation',
        'c2-lem-polynomial-coefficients',
    ],
    page=130,
    kind='exercise',
    optional=True,
)

s.r(
    'ex-degree-bounded-bezout',
    'A degree-bounded Bezout identity without linear maps',
    r'''Let $p,q\in\Poly(\C)$ be nonconstant and have no common
    root. Put $m=\deg p$ and $n=\deg q$.
    Prove that there exist $a\in\Poly_{n-1}(\C)$ and
    $b\in\Poly_{m-1}(\C)$ such that
    \[
    ap+bq=1.
    \]''',
    r'''Consider all nonzero polynomials of the form $Ap+Bq$,
    where $A,B\in\Poly(\C)$. This collection is nonempty
    because it contains $p$. Choose one, say
    $h=A_0p+B_0q$, with the smallest possible degree.

    Divide $p$ by $h$ to obtain $p=th+r$, where either
    $r=0$ or $\deg r<\deg h$. The remainder also has
    the form
    \[
    r=(1-tA_0)p+(-tB_0)q.
    \]
    If $r\ne0$, this contradicts the minimal degree of
    $h$. Thus $h$ divides $p$. Dividing $q$ by $h$
    in the same way shows that its remainder is zero:
    that remainder would be $(-tA_0)p+(1-tB_0)q$
    for the relevant quotient $t$. Hence $h$ divides $q$.

    If $h$ were nonconstant, the fundamental theorem of
    algebra would provide a root $\lambda$ of $h$.
    Since $h$ divides both $p$ and $q$, evaluation would
    give $p(\lambda)=q(\lambda)=0$, contrary to the
    hypothesis. Therefore $h$ is a nonzero constant $c$.
    Dividing its representation by $c$ yields
    $Ap+Bq=1$ for some polynomials $A,B$.

    Divide $A$ by $q$, writing $A=tq+a$, where
    $a\in\Poly_{n-1}(\C)$. Then
    \[
    1=ap+(B+tp)q.
    \]
    Put $b=B+tp$. If $b=0$, its required degree bound
    already holds. If $b\ne0$, then $bq=1-ap$ is
    nonzero. The right side has degree at most
    $m+n-1$, because $a$ has degree at most $n-1$
    when nonzero, and the zero case gives the same bound.
    The product-degree theorem now gives
    \[
    \deg b+n=\deg(bq)\le m+n-1,
    \]
    so $\deg b\le m-1$. Thus both coefficients have
    the stated bounds.''',
    4,
    60,
    [
        r'''Among nonzero polynomial combinations of $p$ and $q$, choose one of least degree.''',
        r'''Divide $p$ and $q$ by that combination; use the absence of a common root to determine its degree.''',
        r'''After obtaining an identity, reduce one coefficient by polynomial division to obtain the degree bounds.''',
    ],
    [
        'thm-polynomial-division',
        'thm-fundamental-algebra',
        'lem-polynomial-product-degree',
        'c2-def-polynomial',
        'c2-def-polynomial-space',
        'c1-foundations',
    ],
    page=131,
    kind='exercise',
    optional=True,
)

s.r(
    'ex-hermite-interpolation',
    'Prescribing values and first derivatives',
    r'''Let $a_1,\ldots,a_s$ be distinct real numbers, where
    $s\ge1$. For arbitrary real numbers
    $u_1,\ldots,u_s,v_1,\ldots,v_s$, prove that there is
    exactly one $p\in\Poly_{2s-1}(\R)$ satisfying
    \[
    p(a_j)=u_j,\qquad p'(a_j)=v_j
    \quad(1\le j\le s).
    \]''',
    r'''We first justify a derivative rule needed below.
    If $f(x)=\sum_r c_rx^r$ and $g(x)=\sum_t d_tx^t$,
    expand their product and differentiate each term.
    The constant term differentiates to zero, and the
    remaining terms give
    \[
    (fg)'(x)=
    \sum_{r+t\ge1}(r+t)c_rd_tx^{r+t-1}
    =f'(x)g(x)+f(x)g'(x).
    \]
    The last equality separates the coefficient $r+t$
    into $r$ and $t$, with the zero-index terms contributing
    zero. Thus the product rule follows from the accepted
    polynomial differentiation rule.

    Define
    \[
    L_j(x)=\prod_{\substack{1\le k\le s\\k\ne j}}
    \frac{x-a_k}{a_j-a_k},
    \qquad d_j=L_j'(a_j).
    \]
    The empty product is $1$ if $s=1$.
    These polynomials satisfy $L_j(a_k)=0$ for $k\ne j$
    and $L_j(a_j)=1$. Set
    \[
    H_j(x)=\bigl(1-2d_j(x-a_j)\bigr)L_j(x)^2,
    \qquad K_j(x)=(x-a_j)L_j(x)^2.
    \]
    Their degrees are at most $2s-1$.
    The product rule gives
    \[
    H_j'=-2d_jL_j^2+
    2\bigl(1-2d_j(x-a_j)\bigr)L_jL_j',
    \qquad
    K_j'=L_j^2+2(x-a_j)L_jL_j'.
    \]
    At $a_j$, these formulas give
    $H_j(a_j)=1$, $H_j'(a_j)=-2d_j+2d_j=0$,
    $K_j(a_j)=0$, and $K_j'(a_j)=1$.
    At any other node, the factor $L_j$ makes all four
    corresponding values zero. Hence
    \[
    p=\sum_{j=1}^s\bigl(u_jH_j+v_jK_j\bigr)
    \]
    has the desired values and derivatives, and belongs
    to $\Poly_{2s-1}(\R)$.

    For uniqueness, let $f$ be the difference of two
    candidates. Then $f(a_j)=f'(a_j)=0$ at every node.
    If $f\ne0$, we show successively that
    $\prod_{j=1}^s(x-a_j)^2$ divides $f$.
    Suppose the factors for earlier nodes have been
    extracted, so $f=Qh$, where
    $Q=\prod_{k<j}(x-a_k)^2$.
    Because the nodes are distinct, $Q(a_j)\ne0$.
    The equality $f(a_j)=0$ therefore gives $h(a_j)=0$.
    The product rule and $f'(a_j)=0$ then give
    $0=Q(a_j)h'(a_j)$, so $h'(a_j)=0$.
    By the factor-root theorem, write $h=(x-a_j)t$.
    Differentiation gives $h'(a_j)=t(a_j)$, so
    $t(a_j)=0$ and a second application of the
    factor-root theorem extracts another $(x-a_j)$.
    This proves the inductive step.

    The resulting divisor has degree $2s$. Since $f$
    was assumed nonzero, the product-degree theorem
    would force $\deg f\ge2s$, contradicting
    $f\in\Poly_{2s-1}(\R)$. Thus $f=0$ and the
    interpolating polynomial is unique.''',
    4,
    90,
    [
        r'''Begin with a polynomial that is $1$ at one node and $0$ at all the other nodes.''',
        r'''Squaring produces double zeros at the other nodes; then adjust the value and derivative at the chosen node.''',
        r'''For uniqueness, show that a zero value and zero derivative force a squared linear factor.''',
    ],
    [
        'thm-factor-root',
        'lem-polynomial-product-degree',
        'c2-thm-polynomial-differentiation',
        'c2-def-polynomial-space',
        'c2-lem-polynomial-coefficients',
        'c1-lem-scalar-cancellation',
    ],
    page=130,
    kind='exercise',
    optional=True,
)

s.r(
    'ex-nonnegative-two-squares',
    'A nonnegative real polynomial is a sum of two squares',
    r'''Let $p$ be a nonzero real polynomial satisfying
    $p(x)\ge0$ for every real $x$. Prove that $\deg p=2d$
    for some nonnegative integer $d$, and that there are
    $A,B\in\Poly_d(\R)$ such that
    \[
    p=A^2+B^2.
    \]''',
    r'''If $p$ is constant, it is a positive constant $c$.
    Take $d=0$, $A=\sqrt c$, and $B=0$.
    Now suppose $p$ is nonconstant, and use its real
    factorization. Group repeated real linear factors,
    writing
    \[
    p(x)=c\prod_{\ell=1}^r(x-t_\ell)^{e_\ell}
    \prod_{j=1}^M(x^2+b_jx+c_j),
    \]
    where the $t_\ell$ are distinct, each $e_\ell\ge1$,
    $c\ne0$, and $b_j^2<4c_j$.

    We show that every $e_\ell$ is even. Fix a real
    root $t=t_\ell$, put $e=e_\ell$, and write
    $p(x)=(x-t)^e q(x)$. All remaining linear factors
    are nonzero at $t$, and every irreducible quadratic
    is positive there by completing the square.
    Thus $q(t)\ne0$.

    Expanding $q(t+h)$ as a polynomial in $h$ gives
    \[
    q(t+h)=q(t)+\sum_{k=1}^N\beta_kh^k.
    \]
    Put $L=\sum_{k=1}^N|\beta_k|$. If $L=0$, the
    value is constantly $q(t)$. If $L>0$, choose
    \[
    0<\delta\le\min\left\{1,\frac{|q(t)|}{2L}\right\}.
    \]
    For $|h|<\delta$,
    \[
    |q(t+h)-q(t)|
    \le\sum_{k=1}^N|\beta_k||h|^k
    \le L|h|<\frac{|q(t)|}{2}.
    \]
    Hence for sufficiently small positive $h$, both
    $q(t+h)$ and $q(t-h)$ have the same nonzero sign
    as $q(t)$. If $e$ were odd, the quantities
    $h^e q(t+h)$ and $(-h)^e q(t-h)$ would have
    opposite signs. One of $p(t+h),p(t-h)$ would
    be negative, contradicting the hypothesis.
    Therefore all exponents are even; write
    $e_\ell=2f_\ell$.

    Every quadratic factor is positive on $\R$.
    Choose a real input different from all the
    finitely many $t_\ell$, for example
    $1+\sum_{\ell=1}^r|t_\ell|$.
    At that input all factors other than $c$ are
    positive, and $p$ is nonzero and nonnegative.
    Thus $c>0$. The degree is
    $2\sum_\ell f_\ell+2M=2d$, where
    $d=\sum_\ell f_\ell+M$.

    For each quadratic, let
    \[
    \lambda_j=-\frac{b_j}{2}
       +i\sqrt{c_j-\frac{b_j^2}{4}}.
    \]
    Direct multiplication gives
    $(x-\lambda_j)(x-\overline{\lambda_j})
    =x^2+b_jx+c_j$. Define the complex polynomial
    \[
    h(x)=\sqrt c\,
    \prod_{\ell=1}^r(x-t_\ell)^{f_\ell}
    \prod_{j=1}^M(x-\lambda_j).
    \]
    Its degree is $d$. Split each coefficient into
    real and imaginary parts to write $h=A+iB$
    with $A,B\in\Poly_d(\R)$.
    For real $x$, conjugation of the finite product
    gives
    \[
    h(x)\overline{h(x)}
    =c\prod_\ell(x-t_\ell)^{2f_\ell}
       \prod_j(x-\lambda_j)(x-\overline{\lambda_j})
    =p(x).
    \]
    The left side is also
    $(A(x)+iB(x))(A(x)-iB(x))=A(x)^2+B(x)^2$.
    Equality at every real input proves the stated
    identity of real polynomial functions.''',
    4,
    90,
    [
        r'''Start with real linear factors and irreducible real quadratic factors.''',
        r'''Nonnegativity prevents a sign change at a real root, constraining how often its factor occurs.''',
        r'''Choose one factor from each nonreal conjugate pair and consider the modulus square of their product.''',
    ],
    [
        'thm-real-factorization',
        'thm-real-quadratic',
        'def-real-imaginary',
        'def-conjugate-modulus',
        'thm-complex-properties',
        'lem-polynomial-product-degree',
        'c2-def-polynomial',
        'c2-def-polynomial-space',
        'c1-foundations',
        'c1-lem-scalar-powers',
    ],
    page=131,
    kind='exercise',
    optional=True,
)

s.card(
    'exercise-modulus-expansion',
    'ex-parallelogram-modulus',
    r'''What substitution is useful when expanding squared complex moduli?''',
    r'''Use $|z|^2=z\overline z$ and the algebraic rules for conjugation.''',
)

s.card(
    'exercise-even-polynomial',
    'ex-even-polynomials',
    r'''How can an even polynomial function be recognized from its coefficients?''',
    r'''All coefficients of odd powers are zero. Having even degree
    alone does not imply that the polynomial function is even.''',
)

s.card(
    'exercise-remainder-two-values',
    'ex-two-point-remainder',
    r'''Which two values determine the remainder modulo
    $(x-a)(x-b)$ when $a\ne b$?''',
    r'''The values $p(a)$ and $p(b)$ determine the remainder,
    which has degree at most one.''',
)

s.card(
    'exercise-vanishing-dimension',
    'ex-dimension-vanishing-constraints',
    r'''What is the dimension of the polynomials in $\Poly_n(\F)$
    vanishing at $r$ distinct prescribed points, for $r\le n+1$?''',
    r'''It is $n+1-r$. For $r\le n$, factor out the product of
    the $r$ prescribed linear factors; for $r=n+1$, only zero remains.''',
)

s.card(
    'exercise-lagrange-values',
    'ex-lagrange-basis',
    r'''What property characterizes the values of a Lagrange basis
    polynomial $L_j$ at the interpolation nodes?''',
    r'''It equals $1$ at its own node and $0$ at every other node.''',
)

s.card(
    'exercise-no-real-root',
    'ex-no-real-roots-sign',
    r'''Why must a real polynomial without real roots have even degree?''',
    r'''Its real factorization has only quadratic factors and a
    nonzero constant factor, so the total degree is even.''',
)

s.card(
    'exercise-bezout-idea',
    'ex-degree-bounded-bezout',
    r'''What is the key minimality argument for a polynomial Bezout identity?''',
    r'''A nonzero combination of least degree divides both input
    polynomials, because any nonzero division remainder would be
    a combination of smaller degree.''',
)

s.card(
    'exercise-hermite-uniqueness',
    'ex-hermite-interpolation',
    r'''Why do zero value and zero first derivative at a point
    impose a squared linear factor?''',
    r'''Write $f=(x-a)g$ from $f(a)=0$; the product rule gives
    $f'(a)=g(a)$, so $f'(a)=0$ supplies another factor $(x-a)$.''',
)

s.card(
    'exercise-two-squares',
    'ex-nonnegative-two-squares',
    r'''How does a complex polynomial produce a sum of two real
    polynomial squares?''',
    r'''Write its real and imaginary coefficient parts as $h=A+iB$.
    At real inputs, $h\overline h=A^2+B^2$.''',
)

s.write()
