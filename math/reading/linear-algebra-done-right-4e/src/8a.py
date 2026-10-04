from common import Section

s = Section('8a')

s.p(
    'intro-generalized-eigenvectors',
    'Replacing eigenvectors by vectors killed by a power',
    r'''Throughout this section, $V$ is a finite-dimensional vector space over $\F$, where $\F$ is $\R$ or $\C$, and $T\in\Lin(V)$. Write $n=\dim V$.
    Repeated application of an operator produces an increasing sequence of null spaces. Studying where that sequence stops will supply vectors that can replace missing eigenvectors.''',
    '298',
)

s.r(
    'thm-kernel-powers-increasing',
    'Null spaces of successive powers increase',
    r'''For every operator $T\in\Lin(V)$,
    \[
    \{0\}=\Null T^0\subseteq\Null T\subseteq\Null T^2\subseteq\cdots.
    \]''',
    r'''Because $T^0=I$, its null space is $\{0\}$. If $j\ge0$ and $v\in\Null T^j$, then
    \[
    T^{j+1}v=T(T^jv)=T0=0.
    \]
    Thus $v\in\Null T^{j+1}$, proving each inclusion.''',
    1, 10,
    [r'''Apply $T$ once more to a vector already killed by a power of $T$.'''],
    ['c5-def-operator-powers', 'c5-lem-operator-power-laws', 'c3-thm-linear-zero'],
    '8.1', '298',
)

s.r(
    'thm-kernel-stabilization',
    'One repeated null space forces permanent stabilization',
    r'''If $m\ge0$ and $\Null T^m=\Null T^{m+1}$, then
    \[
    \Null T^m=\Null T^{m+k}\qquad\text{for every integer }k\ge0.
    \]''',
    r'''We first show that every two consecutive null spaces starting at the $m$th are equal. Fix $j\ge0$ and suppose $v\in\Null T^{m+j+1}$. Then
    \[
    T^{m+1}(T^jv)=0.
    \]
    The hypothesis gives $T^jv\in\Null T^m$, so $T^{m+j}v=0$. Hence
    $\Null T^{m+j+1}\subseteq\Null T^{m+j}$. The reverse inclusion follows from the increasing-null-spaces theorem. Chaining these equalities from $j=0$ to $j=k-1$ proves the assertion for $k\ge1$; for $k=0$ it is an equality with itself.''',
    2, 20,
    [r'''If $T^{m+j+1}v=0$, apply the assumed equality to $T^jv$.'''],
    ['thm-kernel-powers-increasing', 'c5-lem-operator-power-laws'],
    '8.2', '298',
)

s.r(
    'thm-stabilization-dimension',
    'The dimension bounds when stabilization occurs',
    r'''If $n=\dim V$, then
    \[
    \Null T^n=\Null T^{n+1}=\Null T^{n+2}=\cdots.
    \]''',
    r'''Suppose $\Null T^n\ne\Null T^{n+1}$. If equality held between $\Null T^j$ and $\Null T^{j+1}$ for any $0\le j\le n$, permanent stabilization would imply equality at $n$, a contradiction. Thus all $n+1$ inclusions in
    \[
    \{0\}=\Null T^0\subseteq\Null T^1\subseteq\cdots\subseteq\Null T^{n+1}
    \]
    would be strict. Each null space is a subspace, and a proper inclusion of finite-dimensional subspaces strictly increases dimension. Starting from dimension $0$, this would give
    $\dim\Null T^{n+1}\ge n+1$, contrary to $\Null T^{n+1}\subseteq V$. Therefore the null spaces at $n$ and $n+1$ are equal, and permanent stabilization gives all remaining equalities. The same argument includes $n=0$.''',
    2, 20,
    [
        r'''Before stabilization, every step must increase dimension.''',
        r'''There cannot be $n+1$ strict increases starting from the zero subspace inside an $n$-dimensional space.''',
    ],
    [
        'thm-kernel-powers-increasing', 'thm-kernel-stabilization',
        'c3-thm-null-subspace', 'c2-thm-proper-subspace-dimension',
        'c2-thm-subspace-dimension',
    ],
    '8.3', '299',
)

s.r(
    'thm-kernel-range-decomposition',
    'A sufficiently high power separates kernel and range',
    r'''For $n=\dim V$,
    \[
    V=\Null T^n\oplus\Range T^n.
    \]''',
    r'''Let $K=\Null T^n$ and $R=\Range T^n$. These are subspaces. If $v\in K\cap R$, write $v=T^nu$. Since $T^nv=0$, we have $T^{2n}u=0$. Stabilization gives $\Null T^{2n}=\Null T^n$, including when $n=0$, so $T^nu=0$ and hence $v=0$. Therefore $K\cap R=\{0\}$.
    The dimension formula for a sum now gives
    \[
    \dim(K+R)=\dim K+\dim R.
    \]
    Rank-nullity applied to $T^n$ makes the right side $n$. Consequently the subspace $K+R$ equals $V$. The zero intersection makes this sum direct.''',
    3, 35,
    [
        r'''Start with a vector of the form $T^nu$ that is also killed by $T^n$.''',
        r'''Stabilization compares the kernels of $T^{2n}$ and $T^n$; rank-nullity then proves that the two summands fill $V$.''',
    ],
    [
        'thm-stabilization-dimension', 'c3-thm-null-subspace',
        'c3-thm-range-subspace', 'c3-thm-rank-nullity',
        'c2-thm-dimension-sum', 'c2-thm-full-dimension-equality',
        'c1-thm-direct-intersection',
    ],
    '8.4', '299',
)

s.r(
    'ex-power-decomposition',
    'Taking a power can repair the kernel-range decomposition',
    r'''Define $T\in\Lin(\F^3)$ by
    \[
    T(z_1,z_2,z_3)=(4z_2,0,5z_3).
    \]
    Then $\Null T+\Range T$ is neither a direct sum nor all of $\F^3$. In contrast,
    \[
    \Null T^3=\{(z_1,z_2,0):z_1,z_2\in\F\},\qquad
    \Range T^3=\{(0,0,z_3):z_3\in\F\},
    \]
    and these subspaces give a direct-sum decomposition of $\F^3$.''',
    r'''The coordinate formulas are linear, so $T$ is linear. Its value is zero exactly when $z_2=z_3=0$, and every vector $(a,0,b)$ is $T(0,a/4,b/5)$. Thus
    \[
    \Null T=\Span((1,0,0)),\qquad
    \Range T=\{(a,0,b):a,b\in\F\}.
    \]
    Their intersection contains $(1,0,0)$, and their sum is the displayed range, which does not contain $(0,1,0)$.
    Applying $T$ twice and three times gives
    \[
    T^2(z_1,z_2,z_3)=(0,0,25z_3),\qquad
    T^3(z_1,z_2,z_3)=(0,0,125z_3).
    \]
    The asserted kernel and range follow. Every $(z_1,z_2,z_3)$ equals
    $(z_1,z_2,0)+(0,0,z_3)$, and a vector in both displayed subspaces has all three coordinates zero. Hence their sum is all of $\F^3$ and is direct.''',
    2, 20,
    [r'''Compute $T^2$ and $T^3$ before describing their null spaces and ranges.'''],
    [
        'c3-def-linear-map', 'c3-def-null-space', 'c3-def-range',
        'c5-def-operator-powers', 'c1-thm-direct-intersection',
    ],
    '8.6', '299–300', kind='example',
)

s.d(
    'def-generalized-eigenvector',
    'Generalized eigenvectors',
    r'''Let $\lambda$ be an eigenvalue of $T$. A \emph{generalized eigenvector} of $T$ corresponding to $\lambda$ is a nonzero vector $v\in V$ for which
    \[
    (T-\lambda I)^kv=0
    \]
    for some positive integer $k$. An ordinary eigenvector satisfies this condition with $k=1$.''',
    '8.8', '300',
)

s.r(
    'thm-generalized-vector-power',
    'A single dimension bound tests generalized eigenvectors',
    r'''Let $\lambda\in\F$ and $v\ne0$. The following conditions are equivalent:
    \begin{enumerate}
    \item $v$ is a generalized eigenvector of $T$ corresponding to $\lambda$.
    \item $(T-\lambda I)^kv=0$ for some positive integer $k$.
    \item $(T-\lambda I)^nv=0$, where $n=\dim V$.
    \end{enumerate}
    In particular, the power equation in the second condition already forces $\lambda$ to be an eigenvalue.''',
    r'''Put $A=T-\lambda I$. Suppose $A^kv=0$ for some positive integer $k$, and choose the least positive integer $j$ with $A^jv=0$. Then $w=A^{j-1}v$ is nonzero and satisfies $Aw=0$. Hence $Tw=\lambda w$, making $\lambda$ an eigenvalue and $v$ a generalized eigenvector.
    Conversely, the definition of a generalized eigenvector supplies such a positive power.
    If $k\le n$, increasing null spaces give $v\in\Null A^n$; if $k>n$, stabilization gives $\Null A^k=\Null A^n$. Thus the second condition implies the third. Finally, $v\ne0$ forces $n\ge1$, so the third condition is itself a positive-power equation and implies the second.''',
    2, 20,
    [
        r'''To find an ordinary eigenvector, stop one step before the first power that kills $v$.''',
        r'''Apply kernel stabilization to $T-\lambda I$.''',
    ],
    [
        'def-generalized-eigenvector', 'thm-kernel-powers-increasing',
        'thm-stabilization-dimension', 'c5-def-eigenvalue',
        'c2-lem-zero-dimension',
    ],
    '', '301',
)

s.r(
    'thm-generalized-basis',
    'Complex operators have bases of generalized eigenvectors',
    r'''If $\F=\C$, then $V$ has a basis consisting of generalized eigenvectors of $T$. For $V=\{0\}$, this means the empty basis.''',
    r'''We use induction on $n=\dim V$. The assertion holds for $n=0$ because the empty list is a basis of the zero space.
    Suppose $n>0$ and the assertion holds for all smaller dimensions. A complex operator on a nonzero finite-dimensional space has an eigenvalue; choose one, $\lambda$. Set
    \[
    K=\Null(T-\lambda I)^n,\qquad R=\Range(T-\lambda I)^n.
    \]
    The kernel-range decomposition gives $V=K\oplus R$. An eigenvector for $\lambda$ belongs to $K$, so $\dim K\ge1$. Rank-nullity therefore gives $\dim R=n-\dim K<n$.
    The range of a polynomial in $T$ is invariant under $T$, so $S=T|_R$ is an operator on $R$. By induction, $R$ has a basis $r_1,\ldots,r_b$ of generalized eigenvectors of $S$, with the list empty if $R=\{0\}$. For each $r_j$ there are an eigenvalue $\mu_j$ of $S$ and a positive integer $k_j$ such that
    $(S-\mu_j I_R)^{k_j}r_j=0$. Successive applications of the restrictions agree with applications of the original operators, so
    $(T-\mu_j I)^{k_j}r_j=0$. Because $r_j\ne0$, the preceding power test shows that $r_j$ is a generalized eigenvector of $T$.
    Choose a basis $u_1,\ldots,u_a$ of $K$. Every $u_i$ is nonzero and killed by $(T-\lambda I)^n$, so each is a generalized eigenvector of $T$. The concatenated list
    \[
    u_1,\ldots,u_a,r_1,\ldots,r_b
    \]
    spans $V=K+R$. If a linear combination of this list is zero, its $K$ part is the negative of its $R$ part and hence belongs to $K\cap R=\{0\}$. Independence of the two separate bases then makes every coefficient zero. Thus this list is the required basis.''',
    4, 75,
    [
        r'''Use induction on dimension after choosing an eigenvalue $\lambda$.''',
        r'''Apply the kernel-range decomposition to $T-\lambda I$, and restrict $T$ to the range summand.''',
        r'''The kernel summand is nonzero, so the range summand has smaller dimension.''',
    ],
    [
        'thm-kernel-range-decomposition', 'thm-generalized-vector-power',
        'c5-thm-complex-eigenvalue', 'c5-thm-polynomial-invariant',
        'c5-def-invariant', 'c5-lem-restriction-polynomial',
        'c3-thm-rank-nullity', 'c2-thm-basis-existence',
        'c2-lem-zero-dimension', 'c1-thm-direct-intersection',
    ],
    '8.9', '301',
)

s.r(
    'ex-generalized-coordinate-vectors',
    'Generalized eigenvectors fill the missing coordinate direction',
    r'''On $\C^3$, let
    \[
    T(z_1,z_2,z_3)=(4z_2,0,5z_3).
    \]
    The eigenvalues are $0$ and $5$. The eigenvectors for $0$ are the nonzero vectors $(z_1,0,0)$, whereas those for $5$ are the nonzero vectors $(0,0,z_3)$.
    The generalized eigenvectors for $0$ are all nonzero vectors $(z_1,z_2,0)$; those for $5$ are all nonzero vectors $(0,0,z_3)$. Thus there is no basis of ordinary eigenvectors, but the standard basis is a basis of generalized eigenvectors.''',
    r'''The equation $Tz=\lambda z$ is
    \[
    4z_2=\lambda z_1,\qquad 0=\lambda z_2,\qquad 5z_3=\lambda z_3.
    \]
    If $\lambda\ne0,5$, the last two equations give $z_2=z_3=0$, and the first then gives $z_1=0$. Such a scalar is not an eigenvalue. For $\lambda=0$, the solutions are exactly $(z_1,0,0)$; for $\lambda=5$, they are exactly $(0,0,z_3)$. Each family has nonzero members, so both scalars are eigenvalues. Every ordinary eigenvector has second coordinate zero, preventing these vectors from spanning $\C^3$.
    The earlier coordinate calculation gives
    \[
    T^3z=(0,0,125z_3).
    \]
    If $A=T-5I$, direct successive application gives
    \[
    Az=(-5z_1+4z_2,-5z_2,0),\quad
    A^2z=(25z_1-40z_2,25z_2,0),
    \]
    and
    \[
    A^3z=(-125z_1+300z_2,-125z_2,0).
    \]
    Consequently $\Null T^3$ consists of the vectors with $z_3=0$, whereas $\Null A^3$ consists of those with $z_1=z_2=0$. The dimension-bound test identifies the stated generalized eigenvectors. The first two standard basis vectors belong to the first family, and the third belongs to the second.''',
    2, 25,
    [
        r'''Solve the ordinary eigenvector equations first.''',
        r'''For the generalized eigenvectors, calculate the third powers of $T$ and $T-5I$.''',
    ],
    [
        'ex-power-decomposition', 'thm-generalized-vector-power',
        'c5-def-eigenvalue', 'c5-def-eigenvector', 'c2-def-basis',
    ],
    '8.10', '302', kind='example',
)

s.r(
    'thm-generalized-eigenvalue-unique',
    'A generalized eigenvector determines its eigenvalue',
    r'''A nonzero vector cannot be a generalized eigenvector of the same operator for two different eigenvalues.''',
    r'''Suppose $v$ is a generalized eigenvector for both $\alpha$ and $\lambda$. Choose the least positive integer $m$ such that $(T-\alpha I)^mv=0$, and set
    \[
    w=(T-\alpha I)^{m-1}v.
    \]
    Minimality gives $w\ne0$, and $(T-\alpha I)w=0$, so $Tw=\alpha w$.
    There is a positive integer $k$ with $(T-\lambda I)^kv=0$. Polynomial operators in $T$ commute, and hence
    \[
    (T-\lambda I)^kw
    =(T-\alpha I)^{m-1}(T-\lambda I)^kv=0.
    \]
    Evaluating the polynomial $(z-\lambda)^k$ on the eigenvector $w$ gives
    $(\alpha-\lambda)^kw=0$. Since $w\ne0$, the scalar $(\alpha-\lambda)^k$ is zero. A real or complex scalar with a zero positive power is zero, so $\alpha=\lambda$.''',
    3, 35,
    [
        r'''Turn the vector into an ordinary eigenvector for one of the two proposed eigenvalues.''',
        r'''Powers of $T-\alpha I$ commute with powers of $T-\lambda I$.''',
    ],
    [
        'def-generalized-eigenvector', 'c5-thm-polynomial-evaluation-product',
        'c5-lem-polynomial-eigenvector',
    ],
    '8.11', '302',
)

s.r(
    'thm-generalized-eigenvectors-independent',
    'Distinct eigenvalues give independent generalized eigenvectors',
    r'''Suppose $\lambda_1,\ldots,\lambda_m$ are distinct eigenvalues of $T$ and $v_j$ is a generalized eigenvector corresponding to $\lambda_j$ for each $j$. Then $v_1,\ldots,v_m$ is linearly independent. The assertion includes the empty list.''',
    r'''We induct on $m$. The empty list is independent. A list containing one nonzero vector is independent.
    Suppose $m\ge2$ and the assertion holds for lists of length $m-1$. Write $n=\dim V$, and suppose
    \[
    a_1v_1+\cdots+a_mv_m=0.
    \]
    Apply $A=(T-\lambda_m I)^n$. The bounded-power test gives $Av_m=0$, so
    \[
    a_1Av_1+\cdots+a_{m-1}Av_{m-1}=0.
    \]
    For $j<m$, the vector $Av_j$ is nonzero: otherwise the bounded-power test would make $v_j$ a generalized eigenvector for $\lambda_m$, contradicting uniqueness of its eigenvalue.
    Polynomial operators commute, so
    \[
    (T-\lambda_j I)^nAv_j
    =A(T-\lambda_j I)^nv_j=0.
    \]
    Thus $Av_j$ is a generalized eigenvector for $\lambda_j$. The induction hypothesis applied to these $m-1$ nonzero vectors yields
    $a_1=\cdots=a_{m-1}=0$. The original relation is now $a_mv_m=0$, forcing $a_m=0$ because $v_m\ne0$. This completes the induction.''',
    3, 40,
    [
        r'''Use induction on the number of vectors, eliminating the last one by a suitable polynomial in $T$.''',
        r'''Apply $(T-\lambda_m I)^n$ and use uniqueness of the generalized eigenvalue to show that the other transformed vectors remain nonzero.''',
    ],
    [
        'thm-generalized-vector-power', 'thm-generalized-eigenvalue-unique',
        'c5-thm-polynomial-evaluation-product', 'c2-def-linear-independence',
    ],
    '8.12', '303',
)

s.d(
    'def-nilpotent',
    'Nilpotent operators',
    r'''An operator $N\in\Lin(V)$ is \emph{nilpotent} if $N^k=0$ for some positive integer $k$. Its \emph{nilpotency index} is the least such positive integer.
    This convention gives the zero operator, including the operator on the zero space, nilpotency index $1$.''',
    '8.14', '303',
)

s.r(
    'thm-pointwise-nilpotence',
    'Vectorwise vanishing becomes one operator equation',
    r'''An operator $N$ is nilpotent if and only if every nonzero vector is a generalized eigenvector of $N$ corresponding to $0$. The assertion about nonzero vectors is vacuous when $V=\{0\}$.''',
    r'''Suppose $N^k=0$ for some positive integer $k$. Every nonzero $v$ satisfies $N^kv=0$, so the generalized-vector power test makes $v$ a generalized eigenvector corresponding to $0$.
    Conversely, suppose every nonzero vector has the stated property. If $V=\{0\}$, its only operator is zero and hence nilpotent. If $n=\dim V>0$, the bounded-power test gives $N^nv=0$ for every nonzero vector. Linearity also gives $N^n0=0$. Thus $N^n=0$, proving nilpotence.''',
    2, 15,
    [r'''Use the dimension-bound test to replace powers that depend on the vector by a common power.'''],
    ['def-nilpotent', 'thm-generalized-vector-power', 'c3-thm-linear-zero'],
    '', '303',
)

s.r(
    'lem-nilpotent-chain-independent',
    'A chain ending at zero is independent',
    r'''Let $N\in\Lin(V)$, let $m\ge1$, and suppose
    \[
    N^mv=0,\qquad N^{m-1}v\ne0.
    \]
    Then
    \[
    v,Nv,\ldots,N^{m-1}v
    \]
    is linearly independent. The operator need not be nilpotent on all of $V$.''',
    r'''Suppose
    \[
    a_0v+a_1Nv+\cdots+a_{m-1}N^{m-1}v=0
    \]
    and some coefficient is nonzero. Let $j$ be the smallest index with $a_j\ne0$. Apply $N^{m-1-j}$ to the relation. Terms with index smaller than $j$ already have zero coefficient. The term with index $j$ becomes $a_jN^{m-1}v$. Every term with larger index contains a power $N^\ell v$ with $\ell\ge m$, and
    $N^\ell v=N^{\ell-m}N^mv=0$. Therefore
    $a_jN^{m-1}v=0$, contradicting both $a_j\ne0$ and $N^{m-1}v\ne0$. No coefficient can be nonzero, which proves independence.''',
    3, 30,
    [
        r'''In a nontrivial linear relation, consider the first nonzero coefficient.''',
        r'''Apply a power of $N$ that moves its vector to $N^{m-1}v$ and kills all later terms.''',
    ],
    ['c5-lem-operator-power-laws', 'c2-def-linear-independence'],
    '', '304', kind='lemma',
)

s.r(
    'ex-nilpotent-coordinate-shift',
    'A coordinate map that vanishes after two steps',
    r'''The operator on $\F^4$ defined by
    \[
    N(z_1,z_2,z_3,z_4)=(0,0,z_1,z_2)
    \]
    is nilpotent with nilpotency index $2$.''',
    r'''Each output coordinate is a linear combination of the input coordinates, so $N$ is linear. Applying it twice gives
    \[
    N^2(z_1,z_2,z_3,z_4)=N(0,0,z_1,z_2)=(0,0,0,0).
    \]
    Hence $N^2=0$. But $N(1,0,0,0)=(0,0,1,0)\ne0$, so $N\ne0$. Therefore the least positive vanishing power is $2$.''',
    1, 10,
    [r'''Compute the second iterate and then test whether the first iterate is already the zero operator.'''],
    ['def-nilpotent', 'c3-def-linear-map', 'c5-def-operator-powers'],
    '8.15(a)', '304', kind='example',
)

s.r(
    'ex-nilpotent-nontriangular-matrix',
    'Nilpotence can be hidden by the chosen basis',
    r'''The operator on $\F^3$ whose standard matrix is
    \[
    A=\begin{pmatrix}
    -3&9&0\\
    -7&9&6\\
    4&0&-6
    \end{pmatrix}
    \]
    is nilpotent with nilpotency index $3$.''',
    r'''Matrix multiplication gives
    \[
    A^2=
    \begin{pmatrix}
    -54&54&54\\
    -18&18&18\\
    -36&36&36
    \end{pmatrix}.
    \]
    Every row of $A^2$ is a scalar multiple of $(-1,1,1)$, and
    \[
    (-1,1,1)A=(3-7+4,-9+9,6-6)=(0,0,0).
    \]
    Thus $A^3=A^2A=0$, whereas $A^2\ne0$. Composition of operators corresponds to matrix multiplication, so the operator has zero third power and nonzero second power. Its first power cannot be zero because that would also make its second power zero. Its nilpotency index is therefore $3$.''',
    2, 20,
    [r'''Compute the square, then look for a common pattern in its rows before multiplying again.'''],
    ['def-nilpotent', 'c3-def-matrix-product', 'c3-thm-matrix-composition'],
    '8.15(b)', '304', kind='example',
)

s.r(
    'ex-nilpotent-differentiation',
    'Differentiation attains the dimension bound',
    r'''For every integer $m\ge0$, differentiation on $\Poly_m(\R)$ is nilpotent with nilpotency index $m+1=\dim\Poly_m(\R)$.''',
    r'''The differentiation rules make $D:p\mapsto p'$ a linear operator on $\Poly_m(\R)$. For $0\le j\le m$, repeated differentiation of $x^j$ gives zero after $j+1$ applications. Therefore $D^{m+1}$ kills every monomial in the basis $1,x,\ldots,x^m$, and linearity gives $D^{m+1}=0$.
    On the other hand,
    \[
    D^m(x^m)=m!\ne0,
    \]
    where $m!=1\cdot2\cdots m$ for $m\ge1$ and $0!=1$. If $m\ge1$ and some positive power $D^k$ with $k\le m$ were zero, then $D^m=D^{m-k}D^k$ would be zero, a contradiction. For $m=0$, $D=0$ and the least positive vanishing power is $1$. Thus the index is $m+1$ in every case, and the polynomial-space dimension formula identifies this number with the dimension.''',
    2, 20,
    [r'''Compare what repeated differentiation does to the monomial basis and to its highest-degree member.'''],
    [
        'def-nilpotent', 'c2-thm-polynomial-differentiation',
        'c2-ex-polynomial-dimension', 'c5-lem-operator-power-laws',
    ],
    '8.15(c)', '304', kind='example',
)

s.r(
    'thm-nilpotent-index-bound',
    'A nilpotent operator vanishes at the dimension power',
    r'''If $N\in\Lin(V)$ is nilpotent and $n=\dim V$, then $N^n=0$.
    When $n>0$, its nilpotency index is consequently at most $n$. When $n=0$, the equation means that $N^0=I$ is the zero map on the zero space.''',
    r'''Choose a positive integer $k$ with $N^k=0$, so $\Null N^k=V$. If $k\le n$, increasing null spaces give
    $V=\Null N^k\subseteq\Null N^n\subseteq V$, hence $\Null N^n=V$. If $k>n$, stabilization gives $\Null N^n=\Null N^k=V$. Thus in both cases $N^n$ sends every vector to zero.
    If $n>0$, this supplies a positive vanishing exponent no larger than $n$. If $n=0$, the identity and zero map on $V=\{0\}$ coincide, as asserted.''',
    2, 15,
    [r'''Compare a known vanishing power with the stabilized null space at exponent $\dim V$.'''],
    ['def-nilpotent', 'thm-kernel-powers-increasing', 'thm-stabilization-dimension'],
    '8.16', '304',
)

s.r(
    'thm-nilpotent-eigenvalues',
    'Eigenvalues of a nilpotent operator',
    r'''\begin{enumerate}
    \item A nilpotent operator has no nonzero eigenvalues. If its domain is nonzero, then $0$ is an eigenvalue.
    \item Over $\C$, an operator with no nonzero eigenvalues is nilpotent. In particular, on a nonzero complex space, nilpotence is equivalent to having $0$ as the only eigenvalue.
    \end{enumerate}
    The operator on the zero space is nilpotent and has no eigenvalues.''',
    r'''Suppose $N^k=0$ for a positive integer $k$. If $Nv=\lambda v$ with $v\ne0$, polynomial evaluation on an eigenvector gives
    \[
    0=N^kv=\lambda^kv.
    \]
    Thus $\lambda^k=0$, so $\lambda=0$. If $V\ne\{0\}$, choose $v\ne0$ and the least positive integer $j$ with $N^jv=0$. Then $w=N^{j-1}v\ne0$ and $Nw=0$, proving that $0$ is an eigenvalue.
    Conversely, suppose the field is $\C$ and $T$ has no nonzero eigenvalues. If $V=\{0\}$, then $T=0$ is nilpotent. Otherwise let $p$ be its minimal polynomial. Its degree is positive, because a monic polynomial of degree zero is $1$, and $1(T)=I$ is not the zero map on a nonzero space. Every root of $p$ is an eigenvalue of $T$, so every root is $0$. Complex factorization and the leading coefficient $1$ therefore give $p(z)=z^d$ for some $d\ge1$. Hence $T^d=p(T)=0$.
    Finally, an eigenvalue requires a nonzero eigenvector, so the zero space has no eigenvalues.''',
    2, 25,
    [
        r'''Apply a vanishing power to an ordinary eigenvector.''',
        r'''For the complex converse, factor the minimal polynomial and identify all of its roots.''',
    ],
    [
        'def-nilpotent', 'c5-lem-polynomial-eigenvector',
        'c5-def-eigenvalue', 'c5-def-minimal-polynomial',
        'c5-thm-minimal-roots', 'c4-thm-complex-factorization',
    ],
    '8.17', '304–305',
)

s.r(
    'thm-nilpotent-triangular',
    'Nilpotence, a monomial minimal polynomial, and a zero diagonal',
    r'''For $N\in\Lin(V)$, the following are equivalent:
    \begin{enumerate}
    \item $N$ is nilpotent.
    \item The minimal polynomial of $N$ is $z^m$ for some integer $m\ge0$.
    \item Some basis of $V$ gives $N$ a matrix all of whose entries on and below the diagonal are zero.
    \end{enumerate}
    If $V\ne\{0\}$, the exponent in the second condition is positive. If $V=\{0\}$, its minimal polynomial is $1=z^0$ and its matrix in the empty basis is the empty matrix.''',
    r'''Assume first that $N$ is nilpotent, and choose $r\ge1$ with $N^r=0$. Let $p$ be its minimal polynomial. The annihilating-polynomial divisibility theorem gives $z^r=pq$ for a polynomial $q$. Because $p$ is monic and divides a product of linear factors, the split-divisor lemma writes
    \[
    p(z)=\prod_{j=1}^m(z-\mu_j)
    \]
    for scalars $\mu_j\in\F$, allowing an empty product. For each factor, evaluation of $z^r=pq$ at $\mu_j$ gives $\mu_j^r=0$, so $\mu_j=0$. Thus $p(z)=z^m$, proving the second condition.
    Suppose next that the minimal polynomial is $z^m$. It splits into linear factors over $\F$, so the triangularization criterion supplies a basis in which the matrix of $N$ is upper triangular. If $V\ne\{0\}$, then $m\ge1$: otherwise $p=1$ would give $I=p(N)=0$, contrary to the existence of a nonzero vector. The roots of the minimal polynomial are exactly the eigenvalues, so every eigenvalue is $0$. Each diagonal entry of an upper-triangular matrix of an operator is an eigenvalue; hence every diagonal entry is zero. Together with upper triangularity, this is the third condition. On the zero space the empty basis gives the third condition directly.
    Finally, suppose the third condition holds and $n=\dim V>0$. The diagonal-product identity for a triangular operator gives
    \[
    N^n=\prod_{j=1}^n(N-0I)=0.
    \]
    Thus $N$ is nilpotent. If $n=0$, its only operator is already zero and is nilpotent. These implications establish the equivalence in all cases.
    On the zero space $1(N)=I=0$, and $1$ is the monic polynomial of least possible degree; hence its minimal polynomial is $1$.''',
    3, 40,
    [
        r'''A vanishing power says that the minimal polynomial divides a monomial.''',
        r'''Use the splitting criterion for triangularization, then identify the possible diagonal entries.''',
        r'''For the reverse implication, apply the diagonal-product identity to a triangular matrix with zero diagonal.''',
    ],
    [
        'def-nilpotent', 'c5-def-minimal-polynomial',
        'c5-thm-annihilating-divisibility', 'c5-lem-divisor-split-polynomial',
        'c5-thm-triangularizable-splitting', 'c5-thm-minimal-roots',
        'c5-thm-triangular-eigenvalues', 'c5-thm-triangular-diagonal-product',
    ],
    '8.18', '305',
)

s.card(
    'kernel-stabilization',
    'thm-kernel-stabilization',
    r'''What does one equality $\Null T^m=\Null T^{m+1}$ tell you about all later null spaces?''',
    r'''They are all equal to $\Null T^m$. Apply the equality to $T^jv$ to move from exponent $m+j+1$ back to $m+j$.''',
)

s.card(
    'kernel-dimension-bound',
    'thm-stabilization-dimension',
    r'''Why must the null spaces of powers stabilize by exponent $\dim V$?''',
    r'''Before stabilization each inclusion is strict, so the dimension increases by at least one. There cannot be more than $\dim V$ such increases starting from $\{0\}$.''',
)

s.card(
    'power-decomposition',
    'thm-kernel-range-decomposition',
    r'''State the kernel-range direct-sum decomposition supplied by a sufficiently high power.''',
    r'''For $n=\dim V$, $V=\Null T^n\oplus\Range T^n$.''',
)

s.card(
    'generalized-vector',
    'def-generalized-eigenvector',
    r'''What makes a vector a generalized eigenvector corresponding to $\lambda$?''',
    r'''It is nonzero and is killed by $(T-\lambda I)^k$ for some positive integer $k$. The scalar $\lambda$ is then an eigenvalue.''',
)

s.card(
    'generalized-basis',
    'thm-generalized-basis',
    r'''What replaces a possibly nonexistent eigenvector basis for a finite-dimensional complex operator?''',
    r'''A basis of generalized eigenvectors always exists. One proof uses induction and the decomposition into the kernel and range of a high power of $T-\lambda I$.''',
)

s.card(
    'generalized-independence',
    'thm-generalized-eigenvectors-independent',
    r'''What independence statement holds for generalized eigenvectors associated with distinct eigenvalues?''',
    r'''Choosing one generalized eigenvector for each of several distinct eigenvalues produces a linearly independent list.''',
)

s.card(
    'nilpotent-chain',
    'lem-nilpotent-chain-independent',
    r'''If $N^mv=0$ but $N^{m-1}v\ne0$, what can be said about $v,Nv,\ldots,N^{m-1}v$?''',
    r'''The list is linearly independent. In a proposed relation, isolate the first nonzero coefficient by applying a suitable power of $N$.''',
)

s.card(
    'nilpotent-characterizations',
    'thm-nilpotent-triangular',
    r'''Give the minimal-polynomial and matrix characterizations of a nilpotent operator.''',
    r'''Its minimal polynomial is $z^m$, and some basis gives it a matrix whose entries on and below the diagonal are zero. The exponent is positive on a nonzero space; on the zero space it is $0$.''',
)

s.write()