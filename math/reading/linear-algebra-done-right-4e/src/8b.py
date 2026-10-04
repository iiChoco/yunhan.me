from common import Section

s = Section('8b')

s.p(
    'intro-generalized-decomposition',
    'Decomposing an operator into generalized eigenspaces',
    r'''Throughout this section, $V$ is finite-dimensional. Definitions and statements over $\F$ apply over either $\R$ or $\C$; statements requiring the complex field say so explicitly. Generalized eigenspaces separate an operator into invariant pieces on which subtracting an eigenvalue leaves a nilpotent operator. Their dimensions lead to a definition of the characteristic polynomial without determinants.''',
    308,
)

s.d(
    'def-generalized-eigenspace',
    'Generalized eigenspaces',
    r'''For $T\in\Lin(V)$ and $\lambda\in\F$, define
\[
G(\lambda,T)
=\{v\in V:(T-\lambda I)^kv=0
\text{ for some integer }k\ge1\}.
\]
This set contains zero as well as the generalized eigenvectors corresponding to $\lambda$.''',
    '8.19',
    308,
)

s.r(
    'thm-generalized-eigenspace-kernel',
    'A single kernel describes a generalized eigenspace',
    r'''Let $T\in\Lin(V)$, $\lambda\in\F$, and $n=\dim V$. Then
\[
G(\lambda,T)=\Null(T-\lambda I)^n.
\]
In particular, $G(\lambda,T)$ is a subspace and contains $E(\lambda,T)$. Furthermore,
\[
G(\lambda,T)\ne\{0\}
\quad\Longleftrightarrow\quad
\lambda\text{ is an eigenvalue of }T.
\]''',
    r'''Put $A=T-\lambda I$. First suppose $n\ge1$. If $A^nv=0$, the positive exponent $n$ shows directly that $v\in G(\lambda,T)$. Conversely, suppose $A^kv=0$ for some $k\ge1$. If $k\le n$, increasing kernels of powers give $v\in\Null A^n$. If $k>n$, stabilization at the dimension gives $\Null A^k=\Null A^n$, so the same conclusion holds. This proves the kernel equality.

If $n=0$, then $V=\{0\}$. The generalized eigenspace is $\{0\}$, and $\Null A^0=\Null I_V=\{0\}$, so the equality still holds. A kernel of a linear map is a subspace, which proves the subspace assertion in all cases.

If $v\in E(\lambda,T)$, then $Av=0$, so the exponent $1$ puts $v$ in $G(\lambda,T)$. In particular, an eigenvalue supplies a nonzero member of the generalized eigenspace.

Conversely, let $v\ne0$ belong to $G(\lambda,T)$, and choose the least positive integer $k$ with $A^kv=0$. Then $u=A^{k-1}v$ is nonzero: for $k=1$ it equals $v$, and for $k>1$ its vanishing would contradict minimality. Because $Au=A^kv=0$, we have $Tu=\lambda u$. Thus $\lambda$ is an eigenvalue.''',
    2,
    20,
    [
        r'''Compare every kernel of a power with the kernel at exponent $\dim V$.''',
        r'''From a nonzero vector killed by a power, take its last nonzero image before it reaches zero.''',
    ],
    [
        'def-generalized-eigenspace',
        'thm-kernel-powers-increasing',
        'thm-stabilization-dimension',
        'c3-thm-null-subspace',
        'c5-def-operator-powers',
        'c5-def-eigenspace',
        'c5-def-eigenvalue',
        'c2-lem-zero-dimension',
        'c1-foundations',
    ],
    '8.20',
    308,
)

s.r(
    'ex-generalized-coordinate-decomposition',
    'A plane and a line as generalized eigenspaces',
    r'''On $\C^3$, let
\[
T(z_1,z_2,z_3)=(4z_2,0,5z_3).
\]
Its eigenvalues are $0$ and $5$, and
\[
G(0,T)=\{(z_1,z_2,0):z_1,z_2\in\C\},
\qquad
G(5,T)=\{(0,0,z_3):z_3\in\C\}.
\]
These spaces give the direct sum
\[
\C^3=G(0,T)\oplus G(5,T).
\]''',
    r'''The coordinate formula is linear. Its standard matrix is upper triangular with diagonal entries $0,0,5$, so its eigenvalues are exactly $0$ and $5$.

For any $z=(z_1,z_2,z_3)$, repeated application gives
\[
T^2z=(0,0,25z_3),\qquad T^3z=(0,0,125z_3).
\]
Consequently $\Null T^3$ is the displayed coordinate plane. For $A=T-5I$,
\[
Az=(-5z_1+4z_2,-5z_2,0),
\]
and further applications give
\[
A^2z=(25z_1-40z_2,25z_2,0),\qquad
A^3z=(-125z_1+300z_2,-125z_2,0).
\]
The last expression vanishes exactly when $z_2=0$ and then $z_1=0$. Thus $\Null A^3$ is the displayed coordinate line. The generalized-eigenspace kernel theorem identifies these kernels with $G(0,T)$ and $G(5,T)$.

Every vector has the expression
\[
(z_1,z_2,z_3)=(z_1,z_2,0)+(0,0,z_3)
\]
with terms in the stated spaces. If a vector in the plane plus a vector in the line is zero, comparison of the three coordinates makes both terms zero. The zero criterion for direct sums therefore proves the asserted direct sum.''',
    2,
    20,
    [
        r'''Compute the third powers of $T$ and $T-5I$.''',
        r'''Use the resulting coordinate descriptions to check directness.''',
    ],
    [
        'thm-generalized-eigenspace-kernel',
        'c3-thm-coordinate-linear-maps',
        'c3-def-map-matrix',
        'c5-thm-triangular-eigenvalues',
        'c1-thm-direct-zero',
        'c2-ex-coordinate-dimension',
    ],
    '8.21',
    308,
    'example',
)

s.r(
    'thm-generalized-restriction-nilpotent',
    'Invariant generalized eigenspaces and nilpotent restrictions',
    r'''For $T\in\Lin(V)$ and $\lambda\in\F$, the subspace $G=G(\lambda,T)$ is invariant under $T$. The operator
\[
N=(T-\lambda I)|_G
\]
is nilpotent. If $d=\dim G$, then
\[
(T-\lambda I)^dv=0\qquad\text{for every }v\in G.
\]
When $d=0$, the last statement concerns only the zero vector and uses the zeroth-power convention.''',
    r'''Write $n=\dim V$. The kernel description gives
\[
G=\Null(T-\lambda I)^n.
\]
The polynomial $p(z)=(z-\lambda)^n$ satisfies $p(T)=(T-\lambda I)^n$ by multiplicativity of polynomial evaluation. The kernel of a polynomial in $T$ is invariant under $T$, so $G$ is invariant. Because $G$ is also a subspace, $Tv-\lambda v$ belongs to $G$ for every $v\in G$. Thus $N$ is an operator on $G$.

For every nonnegative integer $k$ and $v\in G$,
\[
N^kv=(T-\lambda I)^kv.
\]
This follows by induction: it holds at $k=0$; if it holds at $k$, applying $N$, whose value agrees with $T-\lambda I$ on $G$, proves it at $k+1$. All intermediate vectors stay in $G$ by invariance.

If $n\ge1$, the kernel description now gives $N^n=0$, so $N$ is nilpotent. If $n=0$, then $G=\{0\}$ and $N=0$, which is also nilpotent. For $d\ge1$, the nilpotent index bound gives $N^d=0$, yielding the asserted formula. If $d=0$, every $v\in G$ is zero, and its image under $(T-\lambda I)^0=I$ is zero as well.''',
    2,
    20,
    [
        r'''Use the kernel of a polynomial in $T$ to obtain invariance.''',
        r'''Compare powers of the restriction with restrictions of powers, then use its own space's dimension.''',
    ],
    [
        'thm-generalized-eigenspace-kernel',
        'def-nilpotent',
        'thm-nilpotent-index-bound',
        'c5-thm-polynomial-invariant',
        'c5-thm-polynomial-evaluation-product',
        'c5-def-invariant',
        'c5-def-operator-powers',
        'c2-thm-subspaces-finite',
        'c2-lem-zero-dimension',
    ],
    '8.22(a,b)',
    309,
)

s.r(
    'thm-generalized-eigenspace-decomposition',
    'Generalized eigenspace decomposition over the complex field',
    r'''Suppose $V$ is a complex vector space and $T\in\Lin(V)$. If $\lambda_1,\ldots,\lambda_m$ are the distinct eigenvalues of $T$, then
\[
V=G(\lambda_1,T)\oplus\cdots\oplus G(\lambda_m,T).
\]
For $V=\{0\}$, the eigenvalue list is empty and the empty direct sum means $\{0\}$.''',
    r'''The number of distinct eigenvalues is finite because it is bounded by $\dim V$. Each generalized eigenspace is a subspace.

To prove directness, suppose
\[
v_1+\cdots+v_m=0,\qquad v_j\in G(\lambda_j,T).
\]
Discard every zero term. If any terms remain, they are nonzero generalized eigenvectors associated with distinct eigenvalues. The generalized-eigenvector independence theorem makes this remaining list independent. Its displayed sum is a relation with every coefficient equal to $1$, which contradicts independence. Therefore every original $v_j$ is zero. The zero criterion proves that the sum is direct.

The generalized-eigenvector basis theorem provides a basis of $V$ consisting of generalized eigenvectors of $T$. Each basis vector belongs to the generalized eigenspace for its associated scalar; that scalar is an eigenvalue by the nonzero generalized-eigenspace criterion. Consequently every basis vector belongs to one of the listed subspaces. Their sum therefore contains a basis of $V$ and hence contains all of $V$. The reverse inclusion holds because they are subspaces of $V$, proving equality.

If $V=\{0\}$, there are no eigenvalues, the generalized-eigenvector basis is empty, and its span is $\{0\}$. This gives the stated empty-sum convention.''',
    3,
    30,
    [
        r'''Prove directness by discarding zero terms from a proposed relation.''',
        r'''Use a basis of generalized eigenvectors to prove that the sum exhausts the space.''',
    ],
    [
        'thm-generalized-eigenspace-kernel',
        'thm-generalized-eigenvectors-independent',
        'thm-generalized-basis',
        'c5-cor-eigenvalue-bound',
        'c1-thm-direct-zero',
        'c2-def-basis',
        'c2-def-span',
    ],
    '8.22(c)',
    309,
)

s.d(
    'def-eigenvalue-multiplicity',
    'Multiplicity of an eigenvalue',
    r'''For an eigenvalue $\lambda$ of $T\in\Lin(V)$, its multiplicity is
\[
\dim G(\lambda,T)
=\dim\Null(T-\lambda I)^{\dim V}.
\]
The equality follows from the kernel description of generalized eigenspaces.''',
    '8.23',
    310,
)

s.r(
    'ex-generalized-multiplicities',
    'Multiplicity two without two independent eigenvectors',
    r'''Define $T\in\Lin(\C^3)$ by
\[
T(x,y,z)=(6x+3y+4z,6y+2z,7z).
\]
Its eigenvalues are $6$ and $7$, with generalized eigenspaces
\[
G(6,T)=\Span((1,0,0),(0,1,0)),
\qquad
G(7,T)=\Span((10,2,1)).
\]
Their respective multiplicities are $2$ and $1$. The list
\[
(1,0,0),\ (0,1,0),\ (10,2,1)
\]
is a basis of generalized eigenvectors, but $T$ has no basis of eigenvectors.''',
    r'''The formula defines a linear operator. Its standard matrix
\[
\begin{pmatrix}
6&3&4\\
0&6&2\\
0&0&7
\end{pmatrix}
\]
is upper triangular, so its eigenvalues are precisely $6$ and $7$.

Put $A=T-6I$. Direct substitution gives
\[
A(x,y,z)=(3y+4z,2z,z),\quad
A^2(x,y,z)=(10z,2z,z),\quad
A^3(x,y,z)=(10z,2z,z).
\]
Thus $\Null A^3$ is the plane $z=0$. For $B=T-7I$, the corresponding calculations give
\[
\begin{aligned}
B(x,y,z)&=(-x+3y+4z,-y+2z,0),\\
B^2(x,y,z)&=(x-6y+2z,y-2z,0),\\
B^3(x,y,z)&=(-x+9y-8z,-y+2z,0).
\end{aligned}
\]
The last expression is zero exactly when $y=2z$ and $x=10z$. The generalized-eigenspace kernel theorem therefore gives the two asserted subspaces.

The standard vectors $(1,0,0),(0,1,0)$ form a basis of the first subspace. The nonzero vector $(10,2,1)$ forms a basis of the second. Thus their dimensions, and hence the multiplicities, are $2$ and $1$.

For the concatenated list, a zero relation has third coordinate equal to the coefficient of $(10,2,1)$, so that coefficient is zero; the first two coordinates then make the other coefficients zero. The list spans because
\[
(x,y,z)=(x-10z)(1,0,0)+(y-2z)(0,1,0)+z(10,2,1).
\]
It is therefore a basis, and each vector lies in the indicated generalized eigenspace.

Finally, $A(x,y,z)=0$ forces $z=0$ and $y=0$, so
\[
E(6,T)=\Span((1,0,0)).
\]
Likewise, $B(x,y,z)=0$ gives
\[
E(7,T)=\Span((10,2,1)).
\]
Every eigenvector belongs to one of these two lines. Their sum has dimension $2$: their displayed generators are independent because their third coordinates differ as above. It cannot span $\C^3$, whose dimension is $3$. Hence no basis can consist entirely of eigenvectors.''',
    2,
    25,
    [
        r'''Compute the cubes of the two shifted operators.''',
        r'''Compare each generalized eigenspace with the kernel of the first power.''',
    ],
    [
        'thm-generalized-eigenspace-kernel',
        'def-eigenvalue-multiplicity',
        'c3-thm-coordinate-linear-maps',
        'c3-def-map-matrix',
        'c5-thm-triangular-eigenvalues',
        'c5-def-eigenspace',
        'c2-def-basis',
        'c2-def-dimension',
        'c2-ex-coordinate-dimension',
    ],
    '8.24',
    310,
    'example',
)

s.r(
    'thm-multiplicity-sum',
    'The multiplicities account for the whole dimension',
    r'''For an operator on a finite-dimensional complex vector space, the sum of the multiplicities of its distinct eigenvalues is $\dim V$.''',
    r'''Let the distinct eigenvalues be $\lambda_1,\ldots,\lambda_m$. The generalized eigenspace decomposition is a direct sum equal to $V$, so the dimension formula for a finite direct sum gives
\[
\dim V=\sum_{j=1}^m\dim G(\lambda_j,T).
\]
By definition, each summand on the right is the multiplicity of the corresponding eigenvalue. If $V=\{0\}$, there are no eigenvalues and the empty sum is $0=\dim V$.''',
    1,
    10,
    [
        r'''Take dimensions in the generalized eigenspace decomposition.''',
    ],
    [
        'thm-generalized-eigenspace-decomposition',
        'def-eigenvalue-multiplicity',
        'c3-thm-direct-sum-dimension',
    ],
    '8.25',
    311,
)

s.d(
    'def-algebraic-geometric-multiplicity',
    'Algebraic and geometric multiplicity',
    r'''The multiplicity $\dim G(\lambda,T)$ is also called the algebraic multiplicity of $\lambda$. Its geometric multiplicity is $\dim E(\lambda,T)$. These names distinguish two dimensions attached to the same eigenvalue.''',
    page=311,
)

s.r(
    'thm-diagonalizable-multiplicities',
    'Geometric multiplicity and diagonalizable operators',
    r'''For every eigenvalue $\lambda$ of an operator on a finite-dimensional space,
\[
1\le\dim E(\lambda,T)\le\dim G(\lambda,T).
\]
If $T$ is diagonalizable over $\F$, then
\[
G(\lambda,T)=E(\lambda,T)
\qquad\text{for every }\lambda\in\F.
\]
For a complex operator, diagonalizability is equivalent to equality of the algebraic and geometric multiplicities at every eigenvalue.''',
    r'''An eigenvalue has a nonzero eigenvector, so its eigenspace has dimension at least $1$. The inclusion $E(\lambda,T)\subseteq G(\lambda,T)$ and monotonicity of subspace dimension give the second inequality.

Suppose $T$ is diagonalizable. Choose an eigenvector basis $v_1,\ldots,v_n$, with $Tv_j=\mu_jv_j$. For $v=\sum_j a_jv_j$ and any integer $k\ge1$, induction on $k$ gives
\[
(T-\lambda I)^kv=\sum_{j=1}^n a_j(\mu_j-\lambda)^kv_j.
\]
If $v\in G(\lambda,T)$, choose $k$ making this expression zero. Basis independence implies
$a_j(\mu_j-\lambda)^k=0$ for every $j$. If $\mu_j\ne\lambda$, its nonzero difference has a nonzero power, so $a_j=0$. Hence only eigenvectors for $\lambda$ occur in the expansion of $v$, and $(T-\lambda I)v=0$. Thus $G(\lambda,T)\subseteq E(\lambda,T)$; the reverse inclusion was already proved. Empty bases cause no exception.

Now suppose the field is complex and the two multiplicities agree at every eigenvalue. Taking their sum and using the multiplicity-sum theorem gives
\[
\sum_{\lambda}\dim E(\lambda,T)=\dim V.
\]
The eigenspace-dimension characterization of diagonalizability then makes $T$ diagonalizable. The reverse implication follows from the equality of spaces just proved. On the zero space the dimension sum and eigenvalue list are empty, and the empty basis gives diagonalizability.''',
    2,
    20,
    [
        r'''In an eigenvector basis, a power of $T-\lambda I$ multiplies each coordinate by a scalar power.''',
        r'''For the complex converse, sum the geometric multiplicities.''',
    ],
    [
        'thm-generalized-eigenspace-kernel',
        'def-generalized-eigenspace',
        'def-algebraic-geometric-multiplicity',
        'thm-multiplicity-sum',
        'c5-thm-diagonalizable-equivalences',
        'c5-def-eigenspace',
        'c2-thm-basis-coordinates',
        'c2-thm-subspace-dimension',
        'c2-lem-zero-dimension',
        'c1-lem-scalar-cancellation',
    ],
    page=311,
)

s.d(
    'def-characteristic-polynomial',
    'Characteristic polynomial',
    r'''Let $T$ act on a finite-dimensional complex vector space. If its distinct eigenvalues are $\lambda_1,\ldots,\lambda_m$ with multiplicities $d_1,\ldots,d_m$, define its characteristic polynomial by
\[
q_T(z)=\prod_{j=1}^m(z-\lambda_j)^{d_j}.
\]
For the zero space, the product is empty and $q_T=1$.''',
    '8.26',
    311,
)

s.r(
    'ex-characteristic-polynomial-three',
    'A characteristic polynomial with a repeated factor',
    r'''The characteristic polynomial of
\[
T(x,y,z)=(6x+3y+4z,6y+2z,7z)
\]
on $\C^3$ is
\[
q_T(z)=(z-6)^2(z-7).
\]''',
    r'''The earlier multiplicity calculation gives eigenvalues $6$ and $7$, with multiplicities $2$ and $1$, respectively. The definition of the characteristic polynomial inserts one factor for each distinct eigenvalue with its multiplicity as exponent. It therefore gives precisely $(z-6)^2(z-7)$.''',
    1,
    10,
    [
        r'''Use the previously computed generalized eigenspace dimensions.''',
    ],
    [
        'ex-generalized-multiplicities',
        'def-characteristic-polynomial',
    ],
    '8.27',
    311,
    'example',
)

s.r(
    'thm-characteristic-degree-roots',
    'Degree and zeros of the characteristic polynomial',
    r'''For an operator $T$ on a finite-dimensional complex vector space, its characteristic polynomial is monic, has degree $\dim V$, and has exactly the eigenvalues of $T$ as its zeros.''',
    r'''Write the defining product as
\[
q_T(z)=\prod_{j=1}^m(z-\lambda_j)^{d_j}.
\]
Each $d_j$ is positive because an eigenvalue has a nonzero generalized eigenspace. Every factor is monic, so the product is monic. The product-degree rule gives
\[
\deg q_T=\sum_{j=1}^m d_j=\dim V,
\]
where the last equality is the multiplicity-sum theorem.

For any scalar $a$, the finite product $q_T(a)$ is zero exactly when one of its scalar factors is zero: a product of nonzero field elements is nonzero. Since each $d_j\ge1$, the factor $(a-\lambda_j)^{d_j}$ is zero exactly when $a=\lambda_j$. Thus the zeros are precisely the eigenvalues.

If $V=\{0\}$, then $q_T=1$, which is monic of degree zero and has no zeros. The operator on that space has no eigenvalues because it has no nonzero vector. This verifies every assertion in the empty-product case.''',
    1,
    10,
    [
        r'''Use degree addition for products and the sum of the multiplicities.''',
    ],
    [
        'def-characteristic-polynomial',
        'thm-multiplicity-sum',
        'thm-generalized-eigenspace-kernel',
        'c4-lem-polynomial-product-degree',
        'c5-def-monic',
        'c5-def-eigenvalue',
        'c1-lem-scalar-cancellation',
    ],
    '8.28',
    312,
)

s.r(
    'thm-cayley-hamilton',
    'Cayley–Hamilton theorem',
    r'''Let $T$ act on a finite-dimensional complex vector space, and let $q_T$ be its characteristic polynomial. Then
\[
q_T(T)=0.
\]''',
    r'''First suppose $V\ne\{0\}$. Let $\lambda_1,\ldots,\lambda_m$ be the distinct eigenvalues, and put
\[
G_j=G(\lambda_j,T),\qquad d_j=\dim G_j.
\]
Each $d_j\ge1$. On $G_j$, the operator $(T-\lambda_jI)|_{G_j}$ is nilpotent. The nilpotent restriction theorem therefore gives
\[
(T-\lambda_jI)^{d_j}v=0
\qquad(v\in G_j).
\]

Multiplicativity of polynomial evaluation gives
\[
q_T(T)=\prod_{j=1}^m(T-\lambda_jI)^{d_j}.
\]
All these factors are polynomials in $T$, so they commute. Fix an index $k$. Move the factor $(T-\lambda_kI)^{d_k}$ to the rightmost position. For $v\in G_k$, that factor sends $v$ to zero, and all the remaining linear factors preserve zero. Hence $q_T(T)v=0$ for every $v\in G_k$.

Every vector of $V$ is a sum of vectors in the $G_k$ by the generalized eigenspace decomposition. The operator $q_T(T)$ is linear and vanishes on each summand, so it vanishes on all of $V$.

If $V=\{0\}$, then $q_T=1$ and $q_T(T)=I_V$. The identity and zero operator coincide on the zero space, so the conclusion holds there as well.''',
    3,
    30,
    [
        r'''Show that the characteristic polynomial annihilates each generalized eigenspace separately.''',
        r'''Use the dimension of that generalized eigenspace, then move its factor to act first.''',
    ],
    [
        'def-characteristic-polynomial',
        'def-eigenvalue-multiplicity',
        'thm-generalized-restriction-nilpotent',
        'thm-generalized-eigenspace-decomposition',
        'c5-thm-polynomial-evaluation-product',
        'c5-def-polynomial-operator',
        'c3-thm-linear-zero',
        'c3-def-linear-map',
    ],
    '8.29',
    312,
)

s.r(
    'thm-characteristic-minimal-divisibility',
    'The minimal polynomial divides the characteristic polynomial',
    r'''Let $T$ act on a finite-dimensional complex vector space, with minimal polynomial $p_T$ and characteristic polynomial $q_T$. Then $p_T$ divides $q_T$. Moreover,
\[
p_T=q_T
\quad\Longleftrightarrow\quad
\deg p_T=\dim V.
\]''',
    r'''Cayley–Hamilton gives $q_T(T)=0$. The annihilating-divisibility theorem says that every polynomial vanishing at $T$ is a polynomial multiple of $p_T$. Hence
\[
q_T=p_Th
\]
for some polynomial $h$.

If $p_T=q_T$, the characteristic-degree theorem gives $\deg p_T=\dim V$. Conversely, suppose $\deg p_T=\dim V=\deg q_T$. Both $p_T$ and $q_T$ are nonzero, so $h$ is nonzero. Degree addition in the product implies $\deg h=0$, making $h$ a nonzero constant. Both $p_T$ and $q_T$ are monic, so comparison of leading coefficients gives $h=1$. Thus $p_T=q_T$.

On the zero space, both polynomials are $1$ by their definitions, and the same assertions hold with degree zero.''',
    1,
    10,
    [
        r'''Apply the general description of annihilating polynomials to Cayley–Hamilton.''',
        r'''If the degrees agree, compare the remaining constant factor using monicity.''',
    ],
    [
        'thm-cayley-hamilton',
        'thm-characteristic-degree-roots',
        'c5-thm-annihilating-divisibility',
        'c5-def-minimal-polynomial',
        'c5-def-monic',
        'c4-lem-polynomial-product-degree',
    ],
    '8.30',
    312,
)

s.r(
    'lem-triangular-nullity-bound',
    'Zero diagonal entries bound the nullities of powers',
    r'''Suppose $S\in\Lin(V)$ has an upper-triangular matrix in a basis $v_1,\ldots,v_n$. Let $d$ be the number of zero entries on its diagonal. Then
\[
\dim\Null S^k\le d
\qquad\text{for every integer }k\ge1.
\]''',
    r'''Write the diagonal entries as $a_1,\ldots,a_n$. First consider $S$ itself. Its triangular matrix gives
\[
Sv_j=a_jv_j+u_j,\qquad
u_j\in\Span(v_1,\ldots,v_{j-1}).
\]
The images $Sv_j$ at indices where $a_j\ne0$ form an independent list. Indeed, suppose a nontrivial relation among them is zero, and choose the largest index $j$ with a nonzero coefficient $c_j$ in that relation. Every image at a smaller index belongs to $\Span(v_1,\ldots,v_{j-1})$. Therefore the coefficient of $v_j$ in the relation is exactly $c_ja_j$, which is nonzero. This contradicts uniqueness of coordinates in the basis.

There are $n-d$ such independent images, all in $\Range S$. Hence $\dim\Range S\ge n-d$. Rank-nullity yields
\[
\dim\Null S=n-\dim\Range S\le d.
\]

Let $A$ be the triangular matrix of $S$. The matrix of $S^k$ is $A^k$. Induction using the triangular-product lemma shows that $A^k$ is upper triangular with diagonal entries $a_1^k,\ldots,a_n^k$. For $k\ge1$, the scalar $a_j^k$ vanishes exactly when $a_j$ vanishes. Thus $A^k$ has the same number $d$ of zero diagonal entries. Applying the nullity argument just proved to $S^k$ gives $\dim\Null S^k\le d$.

For $n=0$, the space and all kernels are $\{0\}$, and the diagonal is empty, so the inequality is $0\le0$.''',
    2,
    20,
    [
        r'''Select the columns whose diagonal entries are nonzero and prove their independence using a largest index.''',
        r'''Powers of an upper-triangular matrix raise its diagonal entries to the corresponding powers.''',
    ],
    [
        'c5-def-upper-triangular',
        'c5-thm-triangular-invariant',
        'c5-lem-triangular-sum-product',
        'c3-thm-matrix-composition',
        'c3-thm-rank-nullity',
        'c2-thm-basis-coordinates',
        'c2-thm-independent-length',
        'c2-thm-basis-existence',
        'c1-lem-scalar-cancellation',
    ],
    page=313,
    kind='lemma',
)

s.r(
    'thm-triangular-multiplicities',
    'Multiplicity counts occurrences on a triangular diagonal',
    r'''Suppose $V$ is complex, $\dim V=n$, and an upper-triangular matrix $A$ represents $T\in\Lin(V)$. The multiplicity of each eigenvalue $\lambda$ equals the number of indices $j$ for which $A_{j,j}=\lambda$. Consequently,
\[
q_T(z)=\prod_{j=1}^n(z-A_{j,j}).
\]''',
    r'''If $n=0$, there are no eigenvalues or diagonal entries, and the displayed empty product is $1=q_T$. Suppose now $n\ge1$.

For an eigenvalue $\lambda$, let $m_\lambda=\dim G(\lambda,T)$, and let $d_\lambda$ count its occurrences on the diagonal of $A$. The matrix $A-\lambda I_n$ represents $T-\lambda I$, is upper triangular, and has exactly $d_\lambda$ zero diagonal entries. The triangular nullity bound with exponent $n$ gives
\[
m_\lambda
=\dim\Null(T-\lambda I)^n
\le d_\lambda.
\]
The diagonal-eigenvalue theorem says that every diagonal entry of $A$ is an eigenvalue and that all eigenvalues occur there. Thus summing the counts $d_\lambda$ over the distinct eigenvalues gives $n$. The multiplicity-sum theorem also gives $\sum_\lambda m_\lambda=n$.

Every difference $d_\lambda-m_\lambda$ is nonnegative, and their sum is zero. Therefore each difference is zero, establishing the claimed multiplicity equality. In the definition of $q_T$, the factor $z-\lambda$ occurs $m_\lambda$ times. Replacing this count by the equal number of diagonal occurrences gives the displayed product.''',
    3,
    30,
    [
        r'''First prove that each multiplicity is at most its diagonal occurrence count.''',
        r'''Both collections of counts sum to $\dim V$; use this to turn every inequality into equality.''',
    ],
    [
        'lem-triangular-nullity-bound',
        'thm-generalized-eigenspace-kernel',
        'def-eigenvalue-multiplicity',
        'thm-multiplicity-sum',
        'def-characteristic-polynomial',
        'c5-thm-triangular-eigenvalues',
        'c3-thm-matrix-addition',
        'c3-thm-matrix-scaling',
        'c3-def-identity-matrix',
    ],
    '8.31',
    313,
)

s.d(
    'def-block-diagonal',
    'Block diagonal matrices',
    r'''A square matrix is block diagonal if its row and column indices can be divided, in the same order, into consecutive groups such that every entry connecting different groups is zero. The square submatrices within the groups are its diagonal blocks. If those blocks are $A_1,\ldots,A_m$, write
\[
\operatorname{diag}(A_1,\ldots,A_m)
=
\begin{pmatrix}
A_1& &0\\
 &\ddots& \\
0& &A_m
\end{pmatrix},
\]
where blank off-block regions also mean zero entries. The empty square matrix is the block diagonal matrix with no blocks.''',
    '8.35',
    314,
)

s.r(
    'ex-block-diagonal-matrix',
    'Three diagonal blocks of different sizes',
    r'''The matrix
\[
A=
\begin{pmatrix}
4&0&0&0&0\\
0&2&-3&0&0\\
0&0&2&0&0\\
0&0&0&1&7\\
0&0&0&0&1
\end{pmatrix}
\]
is block diagonal with blocks
\[
A_1=(4),\qquad
A_2=\begin{pmatrix}2&-3\\0&2\end{pmatrix},
\qquad
A_3=\begin{pmatrix}1&7\\0&1\end{pmatrix}.
\]
For the operator on $\C^5$ with standard matrix $A$, the eigenvalue multiplicities are $1$ for $4$, $2$ for $2$, and $2$ for $1$. Its characteristic polynomial is
\[
(z-4)(z-2)^2(z-1)^2.
\]''',
    r'''Partition the indices into the consecutive groups $\{1\}$, $\{2,3\}$, and $\{4,5\}$. Inspection of the displayed entries shows that every entry whose row and column belong to different groups is zero. The submatrices inside these groups are exactly $A_1,A_2,A_3$. This verifies the block diagonal definition.

The matrix is also upper triangular, with diagonal $4,2,2,1,1$. The triangular eigenvalue theorem gives precisely the three eigenvalues $4,2,1$. The triangular multiplicity theorem equates their multiplicities with the respective occurrence counts $1,2,2$, and its characteristic-polynomial formula gives the stated product.''',
    1,
    10,
    [
        r'''Partition the indices into groups of sizes $1,2,2$.''',
        r'''Use the upper-triangular diagonal for the multiplicities.''',
    ],
    [
        'def-block-diagonal',
        'thm-triangular-multiplicities',
        'c5-thm-triangular-eigenvalues',
        'c5-def-upper-triangular',
    ],
    '8.36',
    314,
    'example',
)

s.r(
    'thm-generalized-block-diagonal',
    'Triangular blocks associated with distinct eigenvalues',
    r'''Suppose $V$ is complex and $T\in\Lin(V)$. Let its distinct eigenvalues be $\lambda_1,\ldots,\lambda_m$ with multiplicities $d_1,\ldots,d_m$. There is a basis in which the matrix of $T$ is
\[
\operatorname{diag}(A_1,\ldots,A_m),
\]
where $A_j$ is a $d_j$-by-$d_j$ upper-triangular matrix whose diagonal entries all equal $\lambda_j$. For $V=\{0\}$, this means the empty matrix in the empty basis.''',
    r'''For each eigenvalue, put $G_j=G(\lambda_j,T)$. This is an invariant subspace of dimension $d_j$, and
\[
N_j=(T-\lambda_jI)|_{G_j}
\]
is nilpotent. The nilpotent triangularization theorem gives a basis $\mathcal B_j$ of $G_j$ in which $N_j$ has an upper-triangular matrix with every diagonal entry zero. Since
\[
T|_{G_j}=N_j+\lambda_jI_{G_j},
\]
the matrix of this restriction in $\mathcal B_j$ is upper triangular with every diagonal entry equal to $\lambda_j$. Call it $A_j$.

Concatenate the lists $\mathcal B_1,\ldots,\mathcal B_m$. They span $V$: the generalized eigenspace decomposition expresses every vector as a sum of vectors from the $G_j$, and each such component expands in its basis $\mathcal B_j$. To prove independence, group a zero linear relation on the concatenated list by its subspace $G_j$. Directness of the generalized eigenspace sum forces each grouped vector to be zero. Independence within each $\mathcal B_j$ then makes every coefficient in the original relation zero. Thus the concatenated list is a basis of $V$.

For a basis vector belonging to $\mathcal B_j$, invariance puts its image under $T$ in $G_j$. Its coordinates in all other groups are therefore zero, while its coordinates in group $j$ are precisely the corresponding column of $A_j$. This proves that the full matrix is block diagonal with the stated blocks.

If $V=\{0\}$, there are no eigenvalues or blocks. The empty basis and empty square matrix give the conclusion.''',
    3,
    30,
    [
        r'''Triangularize the nilpotent part separately on each generalized eigenspace.''',
        r'''Concatenate these bases and use invariance to locate all the zero off-block entries.''',
    ],
    [
        'thm-generalized-restriction-nilpotent',
        'thm-generalized-eigenspace-decomposition',
        'def-eigenvalue-multiplicity',
        'def-block-diagonal',
        'thm-nilpotent-triangular',
        'c3-def-map-matrix',
        'c3-thm-matrix-addition',
        'c3-thm-matrix-scaling',
        'c1-thm-direct-zero',
        'c2-def-basis',
    ],
    '8.37',
    315,
)

s.r(
    'ex-generalized-block-basis',
    'Changing a triangular matrix into two separate blocks',
    r'''For
\[
T(x,y,z)=(6x+3y+4z,6y+2z,7z),
\]
the basis
\[
\mathcal B=((1,0,0),(0,1,0),(10,2,1))
\]
gives
\[
\Mat(T,\mathcal B)=
\begin{pmatrix}
6&3&0\\
0&6&0\\
0&0&7
\end{pmatrix}
=
\operatorname{diag}\left(
\begin{pmatrix}6&3\\0&6\end{pmatrix},
(7)
\right).
\]
The first block represents the restriction to $G(6,T)$, and the second represents the restriction to $G(7,T)$.''',
    r'''The earlier multiplicity example proves that $\mathcal B$ is a basis, with its first two vectors forming a basis of $G(6,T)$ and its third vector forming a basis of $G(7,T)$. Write these vectors as $b_1,b_2,b_3$. Direct calculation gives
\[
Tb_1=6b_1,\qquad Tb_2=3b_1+6b_2,
\]
and
\[
Tb_3=T(10,2,1)=(70,14,7)=7b_3.
\]
Their coordinate columns in $\mathcal B$ are therefore $(6,0,0)$, $(3,6,0)$, and $(0,0,7)$. These are exactly the columns of the displayed matrix. The first two and the last index form its diagonal blocks, and the identified basis subspaces give the asserted interpretations as restriction matrices.''',
    1,
    10,
    [
        r'''Compute the three basis-vector images and express them in the same basis.''',
    ],
    [
        'ex-generalized-multiplicities',
        'def-block-diagonal',
        'c3-def-map-matrix',
        'c5-def-invariant',
    ],
    '8.38',
    315,
    'example',
)

s.card(
    'generalized-eigenspace',
    'def-generalized-eigenspace',
    r'''Define $G(\lambda,T)$.''',
    r'''$\displaystyle G(\lambda,T)=\{v:(T-\lambda I)^kv=0\text{ for some integer }k\ge1\}$. It includes the zero vector.''',
)

s.card(
    'generalized-fixed-power',
    'thm-generalized-eigenspace-kernel',
    r'''Which single power describes a generalized eigenspace in finite dimensions?''',
    r'''$\displaystyle G(\lambda,T)=\Null(T-\lambda I)^{\dim V}$.''',
)

s.card(
    'generalized-nilpotent-part',
    'thm-generalized-restriction-nilpotent',
    r'''What remains of $T$ on $G(\lambda,T)$ after subtracting $\lambda I$?''',
    r'''The restriction $(T-\lambda I)|_{G(\lambda,T)}$ is nilpotent. The generalized eigenspace is invariant under $T$.''',
)

s.card(
    'generalized-direct-sum',
    'thm-generalized-eigenspace-decomposition',
    r'''State the generalized eigenspace decomposition over $\C$.''',
    r'''If $\lambda_1,\ldots,\lambda_m$ are the distinct eigenvalues, then
$\displaystyle V=G(\lambda_1,T)\oplus\cdots\oplus G(\lambda_m,T)$.''',
)

s.card(
    'algebraic-geometric-multiplicity',
    'def-algebraic-geometric-multiplicity',
    r'''What are the algebraic and geometric multiplicities of an eigenvalue?''',
    r'''They are $\dim G(\lambda,T)$ and $\dim E(\lambda,T)$, respectively.''',
)

s.card(
    'characteristic-polynomial-definition',
    'def-characteristic-polynomial',
    r'''Define the characteristic polynomial using eigenvalues and multiplicities.''',
    r'''If the distinct eigenvalues are $\lambda_j$ with multiplicities $d_j$, then
$\displaystyle q_T(z)=\prod_j(z-\lambda_j)^{d_j}$.
For the zero space, $q_T=1$.''',
)

s.card(
    'cayley-hamilton-idea',
    'thm-cayley-hamilton',
    r'''Why does the characteristic polynomial annihilate each generalized eigenspace?''',
    r'''Its factor $(T-\lambda I)^{\dim G(\lambda,T)}$ annihilates that generalized eigenspace. All polynomial factors commute, so this factor can be applied first.''',
)

s.card(
    'minimal-characteristic',
    'thm-characteristic-minimal-divisibility',
    r'''How are the minimal and characteristic polynomials related?''',
    r'''The minimal polynomial divides the characteristic polynomial. They are equal exactly when the minimal polynomial has degree $\dim V$.''',
)

s.card(
    'triangular-multiplicity-count',
    'thm-triangular-multiplicities',
    r'''How is an eigenvalue's multiplicity read from an upper-triangular representing matrix?''',
    r'''It is the number of occurrences of that eigenvalue on the diagonal.''',
)

s.card(
    'generalized-block-form',
    'thm-generalized-block-diagonal',
    r'''What matrix form follows from generalized eigenspace decomposition over $\C$?''',
    r'''A block diagonal matrix with one block per distinct eigenvalue. Each block is upper triangular, its diagonal is constant at that eigenvalue, and its size is the eigenvalue's multiplicity.''',
)

s.write()
