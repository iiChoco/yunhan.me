from common import Section

s = Section('2c')

s.p(
    'intro-dimension',
    'Measuring a vector space by a basis',
    r'''A finite-dimensional vector space can have many different bases.
    We first show that their lengths agree, then use this common length
    to compare subspaces and to recognize bases more efficiently.''',
    44,
)

s.r(
    'thm-basis-length',
    'All bases have the same length',
    r'''Any two bases of a finite-dimensional vector space have equal lengths.''',
    r'''Let the two bases have lengths $m$ and $n$. The first basis
    is linearly independent, and the second spans the space, so the
    independent-list length bound gives $m\le n$. Applying that bound
    with the two bases exchanged gives $n\le m$. Therefore $m=n$.
    The argument includes empty bases because the length bound also
    applies to lists of length zero.''',
    2,
    15,
    [r'''Apply the comparison between an independent list and a spanning list in both directions.'''],
    ['def-basis', 'thm-independent-length'],
    '2.34',
    44,
)

s.d(
    'def-dimension',
    'Dimension',
    r'''The \emph{dimension} of a finite-dimensional vector space $V$,
    denoted by $\dim V$, is the length of a basis of $V$. A basis exists
    by the basis existence theorem, and the basis-length theorem shows
    that the answer does not depend on the choice of basis.''',
    '2.35',
    44,
)

s.r(
    'lem-zero-dimension',
    'Dimension zero characterizes the zero space',
    r'''A finite-dimensional vector space $V$ satisfies $\dim V=0$
    if and only if $V=\{0\}$.''',
    r'''If $\dim V=0$, a basis of $V$ has length zero. The span of
    the empty list is $\{0\}$, and a basis spans its entire space,
    so $V=\{0\}$.

    Conversely, the empty list is linearly independent: there are
    no coefficients for which the independence condition could fail.
    Its span is $\{0\}$, so it is a basis of the zero space.
    Hence that space has dimension zero.''',
    1,
    10,
    [r'''What is the span of the empty list?'''],
    [
        'def-span',
        'def-linear-independence',
        'def-basis',
        'thm-basis-existence',
        'def-dimension',
    ],
    page=44,
    kind='lemma',
)

s.r(
    'ex-coordinate-dimension',
    'Dimension of a coordinate space',
    r'''For every integer $n\ge0$, $\dim\F^n=n$.''',
    r'''For $n\ge1$, let $e_j$ have coordinate $j$ equal to $1$
    and every other coordinate equal to $0$. Every vector
    $x=(x_1,\ldots,x_n)$ has the expression
    $x=x_1e_1+\cdots+x_ne_n$, as can be checked in each coordinate.
    Thus $e_1,\ldots,e_n$ spans $\F^n$. If
    $a_1e_1+\cdots+a_ne_n=0$, coordinate $j$ gives $a_j=0$.
    The list is therefore independent and hence a basis.
    Its length is $n$, proving the formula.

    For $n=0$, the space $\F^0$ consists of its single zero vector,
    the empty coordinate list. Its dimension is zero by the
    zero-dimension lemma.''',
    1,
    10,
    [r'''Check the spanning and independence properties of the standard coordinate vectors.'''],
    [
        'c1-def-coordinate-space',
        'c1-def-coordinate-addition',
        'c1-def-coordinate-scaling',
        'def-span',
        'def-linear-independence',
        'def-basis',
        'def-dimension',
        'lem-zero-dimension',
    ],
    '2.36',
    44,
    'example',
)

s.r(
    'ex-polynomial-dimension',
    'Dimension of bounded-degree polynomial spaces',
    r'''For every nonnegative integer $m$,
    \[
    \dim\Poly_m(\F)=m+1.
    \]''',
    r'''Every member of $\Poly_m(\F)$ is a linear combination of
    the functions $1,z,\ldots,z^m$, so that list spans the space.
    If $a_0+a_1z+\cdots+a_mz^m$ is the zero function, uniqueness of
    polynomial coefficients gives $a_0=\cdots=a_m=0$.
    Thus the list is independent and is a basis. It has $m+1$
    entries, so the definition of dimension gives the formula.
    When $m=0$, the list consists only of the constant function
    $1$, and the same argument applies.''',
    1,
    10,
    [r'''Use uniqueness of polynomial coefficients to establish independence.'''],
    [
        'def-polynomial-space',
        'lem-polynomial-coefficients',
        'def-basis',
        'def-dimension',
    ],
    '2.36',
    44,
    'example',
)

s.r(
    'ex-repeated-coordinate-dimension',
    'A two-dimensional coordinate constraint',
    r'''The set
    \[
    U=\{(x,x,y):x,y\in\F\}
    \]
    is a subspace of $\F^3$ with dimension $2$.''',
    r'''Set $u=(1,1,0)$ and $v=(0,0,1)$. The identity
    $(x,x,y)=xu+yv$ shows that every member of $U$ lies in
    $\Span(u,v)$, and every combination $au+bv=(a,a,b)$ belongs
    to $U$. Hence $U=\Span(u,v)$, which is a subspace.

    If $au+bv=0$, its first coordinate gives $a=0$ and its third
    gives $b=0$. Thus $u,v$ is independent and spans $U$, making
    it a basis of length $2$. Therefore $\dim U=2$.''',
    1,
    10,
    [r'''Express a general element using one vector for each free parameter.'''],
    [
        'c1-def-coordinate-addition',
        'c1-def-coordinate-scaling',
        'def-span',
        'thm-span-smallest',
        'def-linear-independence',
        'def-basis',
        'def-dimension',
    ],
    '2.36',
    44,
    'example',
)

s.r(
    'ex-zero-sum-dimension',
    'The plane where three coordinates add to zero',
    r'''The set
    \[
    U=\{(x,y,z)\in\F^3:x+y+z=0\}
    \]
    is a subspace of dimension $2$.''',
    r'''Put $u=(1,-1,0)$ and $v=(1,0,-1)$. A combination
    $au+bv=(a+b,-a,-b)$ has coordinate sum zero.
    Conversely, if $x+y+z=0$, then
    \[
    (x,y,z)=(-y)u+(-z)v,
    \]
    because $x=-y-z$. Therefore $U=\Span(u,v)$ and is a subspace.

    In a relation $au+bv=0$, the second coordinate gives $-a=0$
    and the third gives $-b=0$. Adding $a$ to the first scalar
    equality and $b$ to the second gives $a=b=0$. Thus $u,v$
    is a basis of $U$, proving $\dim U=2$.''',
    2,
    15,
    [r'''Find two vectors satisfying the constraint, then solve for their coefficients in a general vector.'''],
    [
        'c1-def-coordinate-addition',
        'c1-def-coordinate-scaling',
        'def-span',
        'thm-span-smallest',
        'def-linear-independence',
        'def-basis',
        'def-dimension',
    ],
    '2.36',
    44,
    'example',
)

s.r(
    'thm-subspace-dimension',
    'A subspace cannot have larger dimension',
    r'''If $U$ is a subspace of a finite-dimensional vector space $V$,
    then $U$ is finite-dimensional and
    \[
    \dim U\le\dim V.
    \]''',
    r'''The finite-dimensional subspace theorem ensures that $U$
    is finite-dimensional. Choose a basis of $U$ and a basis of $V$.
    The basis of $U$ is also an independent list in $V$: a relation
    among its entries uses the same operations and the same zero
    vector in the two spaces, so its coefficients must vanish.
    The basis of $V$ is a spanning list in $V$. The independent-list
    length bound therefore compares their lengths as
    $\dim U\le\dim V$.''',
    2,
    15,
    [r'''Regard a basis of the subspace as an independent list in the ambient space.'''],
    [
        'c1-def-subspace',
        'thm-subspaces-finite',
        'thm-basis-existence',
        'def-basis',
        'thm-independent-length',
        'def-dimension',
    ],
    '2.37',
    45,
)

s.r(
    'ex-dimension-depends-on-field',
    'Dimension depends on the scalar field',
    r'''The complex numbers have dimension $1$ as a vector space
    over $\C$, but dimension $2$ as a vector space over $\R$.
    Here the notation $\dim_{\C}\C$ or $\dim_{\R}\C$ specifies the
    scalar field.''',
    r'''Over $\C$, the list consisting of $1$ spans because every
    $z\in\C$ equals $z1$. A relation $a1=0$ forces $a=0$,
    so this list is a basis and $\dim_{\C}\C=1$.

    Restricting scalars to $\R$ still gives a vector space: the
    vector-space identities remain valid, and multiplying a complex
    number by a real scalar produces a complex number.
    Every complex number is $a+bi$ for real $a,b$, so $1,i$ spans
    this real vector space. If $a+bi=0$ with real $a,b$, equality
    of the real and imaginary coordinates gives $a=b=0$.
    Thus $1,i$ is a real basis, and $\dim_{\R}\C=2$.''',
    2,
    15,
    [r'''The coefficients allowed in a linear combination change when the scalar field changes.'''],
    [
        'c1-def-complex',
        'c1-thm-complex-laws',
        'c1-def-vector-space',
        'def-span',
        'def-linear-independence',
        'def-basis',
        'def-dimension',
    ],
    page=45,
    kind='example',
)

s.r(
    'thm-full-length-independent',
    'An independent list of full length is a basis',
    r'''If $V$ is finite-dimensional, every independent list in $V$
    with length $\dim V$ is a basis of $V$.''',
    r'''Let the list have length $n=\dim V$. Extend it to a basis
    by the independent-list extension theorem. If $k$ new entries
    were appended, this basis would have length $n+k$.
    Every basis has length $\dim V=n$, so $n+k=n$ and hence
    $k=0$. Thus the original list was already a basis.
    This also handles $n=0$: the extension cannot append an entry
    to the empty list.''',
    2,
    15,
    [r'''Extend the list to a basis and compare lengths.'''],
    [
        'thm-extend-independent',
        'thm-basis-length',
        'def-dimension',
    ],
    '2.38',
    45,
)

s.r(
    'thm-full-dimension-equality',
    'A subspace of full dimension is the whole space',
    r'''If $U$ is a subspace of a finite-dimensional vector space $V$
    and $\dim U=\dim V$, then $U=V$.''',
    r'''Choose a basis of $U$. Its length is $\dim U=\dim V$,
    and it is independent in $V$ because $U$ uses the same operations.
    The full-length independence theorem makes this list a basis
    of $V$. Consequently every vector in $V$ is a linear combination
    of members of $U$, and belongs to $U$ because $U$ is a subspace.
    Thus $V\subseteq U$. The given inclusion $U\subseteq V$
    proves equality. Empty bases cause no exception to this argument.''',
    2,
    15,
    [r'''Show that a basis of the subspace is also a basis of the ambient space.'''],
    [
        'c1-def-subspace',
        'c1-thm-subspace-test',
        'thm-subspaces-finite',
        'thm-basis-existence',
        'def-basis',
        'def-dimension',
        'thm-full-length-independent',
    ],
    '2.39',
    45,
)

s.r(
    'thm-proper-subspace-dimension',
    'Proper subspaces have strictly smaller dimension',
    r'''For a subspace $U$ of a finite-dimensional vector space $V$,
    \[
    U\ne V\quad\Longleftrightarrow\quad \dim U<\dim V.
    \]''',
    r'''If $U\ne V$, the subspace dimension inequality gives
    $\dim U\le\dim V$. Equality would imply $U=V$ by the
    full-dimension equality theorem, so the inequality is strict.
    Conversely, if $\dim U<\dim V$, equality of the two spaces
    would give equality of their dimensions, a contradiction.
    Therefore $U\ne V$.''',
    1,
    10,
    [r'''Combine the dimension inequality with its equality case.'''],
    ['thm-subspace-dimension', 'thm-full-dimension-equality', 'def-dimension'],
    page=45,
    kind='corollary',
)

s.r(
    'ex-two-vector-basis',
    'Recognizing a basis without solving every spanning equation',
    r'''The list $(5,7),(4,3)$ is a basis of $\F^2$.''',
    r'''Suppose $a(5,7)+b(4,3)=(0,0)$. Comparing coordinates gives
    $5a+4b=0$ and $7a+3b=0$. Multiply the first equation by $3$
    and the second by $4$, then subtract to obtain $13a=0$.
    Since $13\ne0$ in $\F$, scalar cancellation gives $a=0$.
    The first equation then becomes $4b=0$, and $4\ne0$ gives
    $b=0$. Thus the list is independent. Its length is $2$,
    which equals $\dim\F^2$, so the full-length independence
    theorem makes it a basis.''',
    2,
    15,
    [r'''An independence calculation is enough because the dimension is already known.'''],
    [
        'c1-def-coordinate-addition',
        'c1-def-coordinate-scaling',
        'c1-lem-scalar-cancellation',
        'def-linear-independence',
        'ex-coordinate-dimension',
        'thm-full-length-independent',
    ],
    '2.40',
    46,
    'example',
)

s.add(
    'theorem',
    'thm-polynomial-differentiation',
    'Differentiating powers of a shifted variable',
    r'''Every real polynomial is differentiable on $\R$.
    For real $a$ and an integer $k\ge1$,
    \[
    \frac{d}{dx}(x-a)^k=k(x-a)^{k-1}.
    \]
    A constant polynomial has derivative zero. Derivatives of
    real linear combinations of these functions are obtained by
    taking the same linear combination of their derivatives.''',
    page=46,
)

s.note(
    'remark-polynomial-differentiation-faith',
    'A calculus rule accepted for the polynomial example',
    r'''The preceding differentiation rule is taken on faith here
    as elementary calculus background. The derivative itself was
    defined in the subspace section, and linearity of differentiation
    was included among that section's accepted analysis facts.''',
    46,
)

s.r(
    'ex-prescribed-polynomial-derivative-basis',
    'A basis for polynomials with a vanishing derivative',
    r'''Let
    \[
    U=\{p\in\Poly_3(\R):p'(5)=0\}.
    \]
    Then $U$ is a three-dimensional subspace of $\Poly_3(\R)$,
    and the list
    \[
    1,\quad (x-5)^2,\quad (x-5)^3
    \]
    is a basis of $U$.''',
    r'''The zero polynomial has derivative zero and lies in $U$.
    For $p,q\in U$, linearity of differentiation gives
    $(p+q)'(5)=p'(5)+q'(5)=0$. For $a\in\R$ and $p\in U$,
    it gives $(ap)'(5)=ap'(5)=0$. Addition and scalar multiplication
    stay inside $\Poly_3(\R)$ because it is a vector space.
    Thus the subspace test applies, and $U$ is finite-dimensional
    as a subspace of the four-dimensional space $\Poly_3(\R)$.

    The derivatives of the displayed functions are respectively
    $0$, $2(x-5)$, and $3(x-5)^2$, so all three functions lie in $U$.
    Suppose their linear combination
    \[
    a+b(x-5)^2+c(x-5)^3
    \]
    is the zero polynomial. Expanding the powers, its coefficient
    of $x^3$ is $c$. Coefficient uniqueness gives $c=0$.
    With $c=0$, its coefficient of $x^2$ is $b$, so $b=0$.
    The remaining constant polynomial is $a$, giving $a=0$.
    Hence the three functions are independent.

    Comparing this independent list with a basis of $U$ gives
    $3\le\dim U$. On the other hand, the polynomial $x$ belongs
    to $\Poly_3(\R)$ and has derivative $1$ at $5$, so it does
    not belong to $U$. Thus $U$ is a proper subspace of
    $\Poly_3(\R)$, and the proper-subspace dimension theorem gives
    $\dim U<4$. Since dimension is an integer, $\dim U=3$.
    The displayed independent list has this length and is
    therefore a basis of $U$.''',
    3,
    35,
    [
        r'''Verify independence by considering the highest powers that can occur.''',
        r'''Bound the dimension from below using the independent list and from above by showing that the subspace is proper.''',
    ],
    [
        'c1-thm-subspace-test',
        'def-polynomial-space',
        'lem-polynomial-coefficients',
        'def-linear-independence',
        'thm-independent-length',
        'thm-subspaces-finite',
        'thm-basis-existence',
        'ex-polynomial-dimension',
        'thm-full-length-independent',
        'thm-proper-subspace-dimension',
        'thm-polynomial-differentiation',
    ],
    '2.41',
    46,
    'example',
)

s.r(
    'thm-full-length-spanning',
    'A spanning list of full length is a basis',
    r'''If $V$ is finite-dimensional, every spanning list in $V$
    with length $\dim V$ is a basis of $V$.''',
    r'''Let the spanning list have length $n=\dim V$. Reduce it
    to a basis by deleting entries as in the spanning-list
    reduction theorem. If $k$ entries were deleted, the resulting
    basis would have length $n-k$. Since every basis has length
    $n$, we have $n-k=n$ and hence $k=0$. No entries were deleted,
    so the original list is a basis. When $n=0$, this argument
    says that the empty spanning list is already a basis.''',
    2,
    15,
    [r'''Reduce the spanning list to a basis and count how many entries could have been deleted.'''],
    ['thm-reduce-spanning', 'thm-basis-length', 'def-dimension'],
    '2.42',
    46,
)

s.r(
    'lem-intersection-subspace',
    'An intersection of two subspaces is a subspace',
    r'''If $U,W$ are subspaces of a vector space $V$, then
    $U\cap W$ is also a subspace of $V$.''',
    r'''Both $U$ and $W$ contain zero, so $0\in U\cap W$.
    If $x,y\in U\cap W$, then both vectors belong to $U$ and to $W$.
    Closure under addition in each subspace places $x+y$ in both,
    hence in their intersection. If $a\in\F$ and $x\in U\cap W$,
    closure under scalar multiplication in each subspace places
    $ax$ in both. The subspace test now proves the assertion.''',
    1,
    10,
    [r'''Check each of the subspace conditions simultaneously in both sets.'''],
    ['c1-thm-subspace-test'],
    page=47,
    kind='lemma',
)

s.r(
    'thm-dimension-sum',
    'Dimension of the sum of two subspaces',
    r'''If $U,W$ are subspaces of a finite-dimensional vector space,
    then
    \[
    \dim(U+W)=\dim U+\dim W-\dim(U\cap W).
    \]''',
    r'''The spaces $U$, $W$, and $U\cap W$ are finite-dimensional:
    the intersection is a subspace by the preceding lemma, and
    all three are subspaces of the given finite-dimensional space.
    Choose a basis $b_1,\ldots,b_r$ of $U\cap W$.
    Extend it to a basis
    \[
    b_1,\ldots,b_r,u_1,\ldots,u_p
    \]
    of $U$, and also to a basis
    \[
    b_1,\ldots,b_r,w_1,\ldots,w_q
    \]
    of $W$. The extension theorem applies because the intersection
    basis remains independent when viewed in either containing space.

    Consider the concatenated list
    \[
    b_1,\ldots,b_r,u_1,\ldots,u_p,w_1,\ldots,w_q.
    \]
    Every entry belongs to $U+W$. If $x\in U+W$, write $x=u+w$
    with $u\in U$ and $w\in W$, expand $u$ and $w$ in their
    respective bases, and combine the two coefficients of each
    $b_i$. This expresses $x$ as a linear combination of the
    concatenated list, so that list spans $U+W$.

    To prove independence, suppose
    \[
    \sum_{i=1}^r a_i b_i+
    \sum_{j=1}^p c_j u_j+
    \sum_{k=1}^q d_k w_k=0.
    \]
    Put $y=\sum_{k=1}^q d_k w_k$. This vector belongs to $W$.
    The displayed relation also expresses it as
    $-\sum_i a_i b_i-\sum_j c_j u_j$, which belongs to $U$.
    Thus $y\in U\cap W$, and we can write
    $y=\sum_{i=1}^r e_i b_i$. Consequently
    \[
    \sum_{i=1}^r(-e_i)b_i+\sum_{k=1}^q d_k w_k=0.
    \]
    Independence of the chosen basis of $W$ gives $d_k=0$ for
    every $k$, as well as $e_i=0$ for every $i$. Substituting
    $d_k=0$ in the original relation leaves a relation in the
    chosen basis of $U$, so all $a_i$ and all $c_j$ vanish.
    The concatenated list is therefore independent and is a
    basis of $U+W$.

    Counting basis entries now gives
    \[
    \dim(U+W)=r+p+q=(r+p)+(r+q)-r
    =\dim U+\dim W-\dim(U\cap W).
    \]
    Any of $r,p,q$ may be zero. In that event the corresponding
    sums are empty and equal zero, and the same spanning and
    independence arguments apply without omitted coefficients.''',
    3,
    45,
    [
        r'''Start with a basis of the intersection and extend it separately to bases of the two subspaces.''',
        r'''When checking independence of the joined list, move one group of added vectors to the other side and show that its sum lies in the intersection.''',
    ],
    [
        'c1-thm-subspace-test',
        'c1-def-subspace-sum',
        'c1-thm-smallest-sum',
        'def-span',
        'def-linear-independence',
        'def-basis',
        'thm-subspaces-finite',
        'thm-basis-existence',
        'thm-extend-independent',
        'def-dimension',
        'lem-intersection-subspace',
    ],
    '2.43',
    47,
)

s.r(
    'cor-two-summand-dimension',
    'Dimension addition detects a direct sum of two subspaces',
    r'''For subspaces $U,W$ of a finite-dimensional vector space,
    \[
    U+W\text{ is direct}
    \quad\Longleftrightarrow\quad
    \dim(U+W)=\dim U+\dim W.
    \]''',
    r'''The dimension formula shows that the displayed equality
    holds exactly when $\dim(U\cap W)=0$. The intersection is
    finite-dimensional, and the zero-dimension lemma says that
    this happens exactly when $U\cap W=\{0\}$. The two-subspace
    intersection criterion identifies the latter condition
    precisely with directness of $U+W$.''',
    1,
    10,
    [r'''Identify the term that must vanish in the dimension formula.'''],
    [
        'c1-thm-direct-intersection',
        'lem-zero-dimension',
        'lem-intersection-subspace',
        'thm-subspaces-finite',
        'thm-dimension-sum',
    ],
    page=48,
    kind='corollary',
)

s.r(
    'thm-direct-dimension',
    'Dimension addition and directness for finitely many summands',
    r'''Let $V_1,\ldots,V_m$ be finite-dimensional subspaces of a
    vector space $V$, where $m\ge1$. Their sum $S=V_1+\cdots+V_m$
    is finite-dimensional, and
    \[
    \dim S\le\sum_{j=1}^m\dim V_j.
    \]
    Equality holds if and only if the sum is direct.''',
    r'''Choose a basis $B_j$ of each $V_j$, and concatenate these
    lists to form a list $B$. The list $B$ spans $S$: express
    a vector in $S$ as a sum of vectors from the $V_j$, and
    expand each of those vectors in $B_j$. Thus $S$ is
    finite-dimensional. The length of $B$ is
    $N=\sum_{j=1}^m\dim V_j$. Comparing a basis of $S$ with
    the spanning list $B$ gives $\dim S\le N$.

    Suppose the sum is direct. In a relation expressing zero
    as a linear combination of $B$, group the terms belonging
    to $B_j$ into a vector $x_j\in V_j$. Then
    $\sum_{j=1}^m x_j=0$. The zero criterion for direct sums
    gives $x_j=0$ for every $j$. Independence of each $B_j$
    then makes every coefficient in the relation zero.
    Thus $B$ is independent as well as spanning, and
    $\dim S=N$.

    Conversely, suppose $\dim S=N$. The spanning list $B$
    has length $\dim S$, so it is a basis by the full-length
    spanning theorem. If $\sum_{j=1}^m x_j=0$ with $x_j\in V_j$,
    expand each $x_j$ in $B_j$. These expansions give a
    zero linear combination of $B$. Its independence makes
    all the coefficients zero, and hence every $x_j=0$.
    The zero criterion proves directness.

    If some $V_j=\{0\}$, its chosen basis is empty, and its
    contribution to both the concatenated list and every
    grouped relation is empty. In particular, the argument
    also covers $N=0$.''',
    3,
    35,
    [
        r'''Concatenate a basis from each summand and first check that the resulting list spans the sum.''',
        r'''Relate independence of that concatenated list to the zero criterion for directness.''',
    ],
    [
        'c1-def-subspace-sum',
        'c1-thm-smallest-sum',
        'c1-thm-direct-zero',
        'def-span',
        'def-finite-dimensional',
        'def-linear-independence',
        'def-basis',
        'thm-independent-length',
        'thm-basis-existence',
        'def-dimension',
        'thm-full-length-spanning',
    ],
    page=48,
)

s.note(
    'remark-dimension-counting',
    'Dimension as a counting principle',
    r'''The dimension formula plays a role similar to the formula
    for the size of a union of two finite sets. A shared subspace
    is counted twice when the two dimensions are added, and its
    dimension must be subtracted once. For several summands,
    directness is exactly the condition under which their
    dimensions add without a correction.''',
    48,
)

s.r(
    'thm-low-dimensional-subspaces',
    'Classifying subspaces of the plane and of three-dimensional space',
    r'''The subspaces of $\R^2$ are exactly $\{0\}$, the lines through
    the origin, and $\R^2$. The subspaces of $\R^3$ are exactly
    $\{0\}$, the lines through the origin, the planes through
    the origin, and $\R^3$.

    Here a line through the origin is a set
    $\{au:a\in\R\}$ with $u\ne0$. A plane through the origin
    is a set $\{au+bv:a,b\in\R\}$ in which neither $u$ nor $v$
    is a scalar multiple of the other.''',
    r'''First record how the geometric descriptions correspond to
    bases. If $u\ne0$, the list consisting of $u$ is independent:
    from $au=0$, a nonzero $a$ would give
    $u=a^{-1}(au)=a^{-1}0=0$, a contradiction. Its span is the
    specified line, so that line is a subspace of dimension $1$.

    Suppose neither $u$ nor $v$ is a scalar multiple of the other.
    In particular both vectors are nonzero, because zero is a
    scalar multiple of every vector. If $au+bv=0$ and $b\ne0$,
    multiplication by $b^{-1}$ would give $v=(-a/b)u$, contrary
    to the hypothesis. Hence $b=0$. Since $u\ne0$, the preceding
    one-vector argument gives $a=0$. Thus $u,v$ is independent;
    its span is the specified plane, which is a subspace of
    dimension $2$.

    Conversely, a basis of a one-dimensional space is a list
    consisting of a nonzero vector: a zero basis vector would
    give a nontrivial zero relation with coefficient $1$.
    Its span is therefore a line of the stated kind.
    A basis $u,v$ of a two-dimensional space cannot have
    $v=au$, because $au-v=0$ would be a nontrivial relation.
    It also cannot have $u=bv$, by the relation $u-bv=0$.
    Hence its span is a plane of the stated kind.

    Now let $U$ be a subspace of $\R^2$. It is finite-dimensional,
    and $0\le\dim U\le2$. If the dimension is zero, the
    zero-dimension lemma gives $U=\{0\}$. If it is one, the
    preceding basis argument makes $U$ a line. If it is two,
    the full-dimension equality theorem gives $U=\R^2$.
    All three listed types are subspaces: lines are spans,
    and the zero space and the whole space are subspaces
    by the subspace test.

    For $U\subseteq\R^3$, the possible dimensions are
    $0,1,2,3$. Dimension zero gives $\{0\}$, dimension one
    gives a line, and dimension two gives a plane by the
    preceding arguments. Dimension three gives $\R^3$
    by the full-dimension equality theorem. Conversely,
    lines and planes are spans and hence subspaces, while
    $\{0\}$ and $\R^3$ are subspaces by the subspace test.
    This proves that both classifications are exhaustive.''',
    3,
    35,
    [
        r'''List the possible dimensions of a subspace of each ambient space.''',
        r'''Interpret a basis of length one or two geometrically, and use the full-dimension equality theorem for the largest case.''',
    ],
    [
        'c1-def-vector-space',
        'c1-thm-scalar-zero',
        'c1-thm-subspace-test',
        'c1-thm-complex-inverses',
        'def-span',
        'thm-span-smallest',
        'def-linear-independence',
        'def-basis',
        'thm-subspaces-finite',
        'thm-basis-existence',
        'def-dimension',
        'lem-zero-dimension',
        'ex-coordinate-dimension',
        'thm-subspace-dimension',
        'thm-full-dimension-equality',
    ],
    page=48,
)

s.card(
    'dimension-definition',
    'def-dimension',
    r'''How is the dimension of a finite-dimensional vector space defined,
    and what makes this definition independent of choices?''',
    r'''It is the length of a basis. Bases exist, and the basis-length
    theorem says that any two bases have the same length.''',
)

s.card(
    'dimension-zero',
    'lem-zero-dimension',
    r'''Which finite-dimensional vector space has dimension zero?''',
    r'''Exactly the zero space $\{0\}$; its basis is the empty list.''',
)

s.card(
    'standard-dimensions',
    'ex-polynomial-dimension',
    r'''What is $\dim\Poly_m(\F)$ for a nonnegative integer $m$?''',
    r'''It is $m+1$, because $1,z,\ldots,z^m$ is a basis.''',
)

s.card(
    'field-and-dimension',
    'ex-dimension-depends-on-field',
    r'''What are the dimensions of $\C$ over $\C$ and over $\R$?''',
    r'''They are $1$ and $2$, respectively: bases are $1$ over $\C$
    and $1,i$ over $\R$.''',
)

s.card(
    'independent-full-length',
    'thm-full-length-independent',
    r'''When does the length of an independent list guarantee that it is a basis?''',
    r'''In a finite-dimensional space $V$, length $\dim V$ is enough.
    An extension to a basis cannot add any entries.''',
)

s.card(
    'proper-dimension',
    'thm-proper-subspace-dimension',
    r'''How does a proper subspace of a finite-dimensional space compare in dimension?''',
    r'''Its dimension is strictly smaller. A subspace with equal
    dimension must be the whole space.''',
)

s.card(
    'dimension-of-sum',
    'thm-dimension-sum',
    r'''State the dimension formula for two subspaces of a finite-dimensional space.''',
    r'''$\dim(U+W)=\dim U+\dim W-\dim(U\cap W)$.''',
)

s.card(
    'intersection-basis-idea',
    'thm-dimension-sum',
    r'''What basis construction proves the dimension formula for a sum?''',
    r'''Extend one basis of the intersection to bases of both subspaces,
    then join the added vectors while keeping the intersection basis once.''',
)

s.card(
    'direct-dimension',
    'thm-direct-dimension',
    r'''When does $\dim(V_1+\cdots+V_m)$ equal
    $\dim V_1+\cdots+\dim V_m$ for finite-dimensional summands?''',
    r'''Exactly when the sum is direct. Concatenating bases of the
    summands then gives a basis of the sum.''',
)

s.card(
    'subspaces-three-space',
    'thm-low-dimensional-subspaces',
    r'''Which subspaces can occur in $\R^3$?''',
    r'''The zero space, lines through the origin, planes through
    the origin, and the whole space, corresponding to dimensions
    $0,1,2,3$.''',
)

s.write()
