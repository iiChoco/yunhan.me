from common import Section

s = Section('5-exercises')

s.p('intro-exercises', 'Exercises on eigenvalues and operator structure', r'''These optional exercises connect eigenvalues, minimal polynomials, invariant subspaces, and changes of basis. Some require explicit calculations, while others ask for a construction or a proof that a proposed description is exhaustive. Each exercise uses only required material from this and earlier chapters.''')

s.r(
    'ex-affine-eigenspaces',
    'Scaling and shifting an operator',
    r'''Let $T\in\Lin(V)$, let $a,b\in\F$ with $a\ne0$, and put $S=aT+bI$. Prove that
\[E(a\lambda+b,S)=E(\lambda,T)\quad(\lambda\in\F).\]
Deduce that the eigenvalues of $S$ are exactly $a\lambda+b$ as $\lambda$ runs through the eigenvalues of $T$. If $V$ is finite-dimensional, prove that $S$ is diagonalizable exactly when $T$ is.''',
    r'''For every $v\in V$,
\[Sv=(a\lambda+b)v
\quad\Longleftrightarrow\quad
aTv+bv=a\lambda v+bv
\quad\Longleftrightarrow\quad Tv=\lambda v,\]
where cancellation of $b v$ and multiplication by $a^{-1}$ justify the last equivalence. Thus the eigenspaces agree. Every scalar $\mu$ has the unique form $a\lambda+b$, with $\lambda=(\mu-b)/a$. Requiring a nonzero vector in the common eigenspace therefore gives the asserted complete eigenvalue correspondence. In finite dimensions, a basis of eigenvectors for either operator is a basis of eigenvectors for the other, by the same equation. The eigenvector-basis criterion proves equivalence of diagonalizability. On the zero space both eigenvalue sets are empty and both operators are diagonalizable in the empty basis.''',
    2, 15,
    [r'Rewrite the eigenvector equation and cancel the common scalar shift.'],
    ['def-eigenspace', 'def-eigenvalue', 'thm-diagonalizable-equivalences', 'c1-def-field', 'c1-lem-vector-cancellation'],
    kind='exercise', optional=True,
)

s.r(
    'ex-rank-one-diagonalization',
    'A one-dimensional range with two eigenvalues',
    r'''On $\F^3$, define
\[T(x,y,z)=(x+2y,x+2y,0).\]
Find every eigenspace, determine the minimal polynomial, and prove that $T$ is diagonalizable.''',
    r'''The coordinate formula defines a linear operator. Put $u=(1,1,0)$. Then $Tv=(x+2y)u$ for $v=(x,y,z)$, and $Tu=3u$. It follows that $T^2=3T$. If $Tv=\lambda v$ with $v\ne0$, applying $T$ once more gives $\lambda^2v=3\lambda v$, so $\lambda(\lambda-3)=0$. Thus the only possible eigenvalues are $0,3$.
The equation $Tv=0$ is $x+2y=0$, giving
\[E(0,T)=\Span((-2,1,0),(0,0,1)).\]
These two generators are independent by their second and third coordinates. If $Tv=3v$, then $v=(x+2y)u/3$, so $E(3,T)\subseteq\Span(u)$; the equation $Tu=3u$ proves the reverse inclusion. Both eigenspaces contain nonzero vectors, so both eigenvalues occur, and every other eigenspace is $\{0\}$.
The monic polynomial $z(z-3)$ annihilates $T$. Its minimal polynomial divides this polynomial and vanishes at both distinct eigenvalues, so the root bound forces its degree to be at least two. Monicity and divisibility therefore make the minimal polynomial exactly $z(z-3)$. Its factors are distinct, so the minimal-polynomial criterion proves diagonalizability.''',
    2, 20,
    [r'Write the image as a scalar multiple of $(1,1,0)$.', r'Compute $T^2$ before solving all eigenvector equations.'],
    ['c3-thm-coordinate-linear-maps', 'def-eigenspace', 'lem-polynomial-eigenvector', 'thm-minimal-roots', 'thm-annihilating-divisibility', 'def-minimal-polynomial', 'thm-diagonalizable-minimal', 'c4-thm-root-bound', 'c4-lem-polynomial-product-degree'],
    kind='exercise', optional=True,
)

s.r(
    'ex-sum-of-projections',
    'When the sum of two commuting projections is a projection',
    r'''Suppose $P,Q\in\Lin(V)$ satisfy $P^2=P$, $Q^2=Q$, and $PQ=QP$. Prove that
\[(P+Q)^2=P+Q\quad\Longleftrightarrow\quad PQ=0.\]
When these conditions hold, prove
\[\Range(P+Q)=\Range P\oplus\Range Q.\]
No finite-dimensionality assumption is required.''',
    r'''Distributivity of composition and the hypotheses give
\[(P+Q)^2=P^2+PQ+QP+Q^2=P+Q+2PQ.\]
Thus $(P+Q)^2=P+Q$ is equivalent to $2PQ=0$. Since the scalar $2$ is nonzero, this is equivalent to $PQ=0$. Commutation then also gives $QP=0$.
Every image $(P+Q)v=Pv+Qv$ belongs to $\Range P+\Range Q$. Conversely, for $Px+Qy$ in that sum,
\[(P+Q)(Px+Qy)=P^2x+PQy+QPx+Q^2y=Px+Qy.\]
Hence every member of the sum lies in the range of $P+Q$.
If $u\in\Range P\cap\Range Q$, write $u=Px=Qy$. The first representation gives $Pu=P^2x=Px=u$, while the second gives $Pu=PQy=0$. Thus $u=0$. The intersection criterion makes the range sum direct.''',
    2, 20,
    [r'Expand the square using commutation.', r'Apply $P$ to a vector lying in both ranges.'],
    ['def-commute', 'c3-thm-composition-laws', 'c3-def-range', 'c3-thm-range-subspace', 'c1-thm-direct-intersection', 'c1-def-field'],
    kind='exercise', optional=True,
)

s.r(
    'ex-parameter-diagonalization',
    'A repeated diagonal entry with a variable coupling',
    r'''For $a,b,c\in\F$, let $T$ have standard matrix
\[\begin{pmatrix}2&a&b\\0&2&c\\0&0&5\end{pmatrix}\]
on $\F^3$. Prove that $T$ is diagonalizable exactly when $a=0$. Determine its minimal polynomial in both cases.''',
    r'''The diagonal-eigenvalue theorem gives precisely the eigenvalues $2,5$. The equation $(T-2I)(x,y,z)=0$ gives $3z=0$ and $ay+bz=0$, so $z=0$ and $ay=0$. Thus $E(2,T)$ has dimension two if $a=0$, and dimension one if $a\ne0$.
For eigenvalue $5$, the equations give
\[y=\frac c3z,\qquad
x=\left(\frac{ac}{9}+\frac b3\right)z.\]
Hence $E(5,T)$ is the line spanned by $\left(ac/9+b/3,c/3,1\right)$ and has dimension one. The eigenspace dimension criterion now proves that $T$ is diagonalizable exactly when $a=0$.
The diagonal-product theorem gives the annihilating polynomial $(z-2)^2(z-5)$. The minimal polynomial divides this cubic and has both $2$ and $5$ as roots. If $a=0$, diagonalizability forces distinct linear factors in the minimal polynomial, so it is $(z-2)(z-5)$. If $a\ne0$, compute
\[(T-2I)(T-5I)e_2=(T-2I)(ae_1-3e_2)=-3ae_1\ne0.\]
Thus the degree-two polynomial $(z-2)(z-5)$ does not annihilate $T$. A monic degree-two polynomial having both roots would equal this one, so the minimal polynomial must have degree three. Divisibility into the monic annihilating cubic then makes it $(z-2)^2(z-5)$.''',
    3, 35,
    [r'Compute the dimensions of the two eigenspaces.', r'Test the possible degree-two annihilator on $e_2$.'],
    ['thm-triangular-eigenvalues', 'thm-triangular-diagonal-product', 'def-eigenspace', 'thm-diagonalizable-equivalences', 'thm-diagonalizable-minimal', 'thm-minimal-roots', 'thm-annihilating-divisibility', 'c4-thm-factor-root', 'c4-lem-polynomial-product-degree', 'c2-ex-coordinate-dimension'],
    kind='exercise', optional=True,
)

s.r(
    'ex-similarity-invariants',
    'Changing an operator by an invertible relabeling',
    r'''Let $S\in\Lin(V)$ be invertible and set $R=STS^{-1}$. Prove that
\[E(\lambda,R)=S(E(\lambda,T))\quad(\lambda\in\F).\]
If $V$ is finite-dimensional, prove that $R,T$ have the same minimal polynomial and that one is diagonalizable exactly when the other is.''',
    r'''For $v\in V$, the identity $R(Sv)=STv$ shows that $Tv=\lambda v$ implies $R(Sv)=\lambda Sv$. Conversely, every $w\in V$ is uniquely $Sv$, and $Rw=\lambda w$ gives $STv=\lambda Sv$; applying $S^{-1}$ yields $Tv=\lambda v$. This proves the eigenspace equality.
Induction gives $R^k=ST^kS^{-1}$ for every $k\ge0$. The case $k=0$ is $I=SIS^{-1}$, and multiplication by $R$ gives the next case after cancelling $S^{-1}S$. Consequently, for every polynomial $p$,
\[p(R)=Sp(T)S^{-1},\]
by distributing the finite coefficient sum. Thus $p(R)=0$ if and only if $p(T)=0$. The two operators have exactly the same annihilating polynomials, so uniqueness of the monic annihilator of smallest degree gives the same minimal polynomial. Also an invertible map transports a basis to a basis, and the eigenspace equality shows that $S$ transports an eigenvector basis for $T$ to one for $R$. Applying $S^{-1}$ proves the converse. The diagonalizability criterion gives the claim, including the empty basis of the zero space.''',
    2, 20,
    [r'Write a candidate eigenvector for $R$ as $Sv$.', r'Prove the identity for powers before treating arbitrary polynomials.'],
    ['def-eigenspace', 'def-polynomial-operator', 'def-operator-powers', 'def-minimal-polynomial', 'thm-minimal-polynomial-existence', 'thm-diagonalizable-equivalences', 'c3-def-map-inverse', 'c3-thm-composition-laws', 'c3-lem-isomorphism-basis'],
    kind='exercise', optional=True,
)

s.r(
    'ex-inverse-minimal-polynomial',
    'Reversing the coefficients of a minimal polynomial',
    r'''Suppose $T$ is invertible on a finite-dimensional space and its minimal polynomial is
\[\mu(z)=\sum_{j=0}^d a_jz^j,\qquad a_d=1.\]
Prove that $a_0\ne0$ and that the minimal polynomial of $T^{-1}$ is
\[\nu(z)=\frac{1}{a_0}\sum_{j=0}^d a_jz^{d-j},\qquad a_d=1.\]
Also prove that $E(\lambda,T)=E(\lambda^{-1},T^{-1})$ for every nonzero scalar $\lambda$.''',
    r'''The invertibility criterion for the minimal polynomial gives $a_0=\mu(0)\ne0$. The displayed polynomial $\nu$ is monic of degree $d$. Using integer power laws for the invertible operator,
\[\nu(T^{-1})=\frac{1}{a_0}T^{-d}\mu(T)=0.\]
To prove minimality, suppose a nonzero polynomial $r(z)=\sum_{k=0}^e b_kz^k$ of degree $e<d$ annihilates $T^{-1}$. Define $h(z)=\sum_{k=0}^e b_kz^{e-k}$. Its coefficients are a reversal of those of $r$, so $h\ne0$ and $\deg h\le e<d$. But
\[h(T)=T^er(T^{-1})=0,\]
contradicting the defining minimal degree of $\mu$. Hence no lower-degree nonzero polynomial annihilates $T^{-1}$, and uniqueness of the monic minimal polynomial identifies it with $\nu$.
Finally, for $\lambda\ne0$, applying $T^{-1}$ to $Tv=\lambda v$ gives $T^{-1}v=\lambda^{-1}v$. Conversely, applying $T$ to the latter equation gives $Tv=\lambda v$. These equations also hold for $v=0$, proving equality of the entire eigenspaces. On the zero space, $\mu=\nu=1$, so $d=0$ and $a_0=1$; the same formula holds and every eigenspace is $\{0\}$.''',
    3, 35,
    [r'Multiply the equation $\mu(T)=0$ by a negative power of $T$.', r'Reverse any proposed lower-degree annihilator to contradict minimality.'],
    ['thm-invertible-minimal', 'def-minimal-polynomial', 'thm-minimal-polynomial-existence', 'lem-operator-power-laws', 'def-polynomial-operator', 'def-eigenspace', 'c3-def-map-inverse'],
    kind='exercise', optional=True,
)

s.r(
    'ex-polynomial-spectral-mapping',
    'Eigenvalues of a polynomial in an operator',
    r'''Let $T$ act on a finite-dimensional complex vector space, and let $p\in\Poly(\C)$. Prove that the eigenvalues of $p(T)$ are exactly the numbers $p(\lambda)$ where $\lambda$ is an eigenvalue of $T$. Include constant polynomials and the zero-dimensional space.''',
    r'''First consider two upper-triangular square matrices $A,B$ of the same size. If $i>j$, every summand $A_{ik}B_{kj}$ in $(AB)_{ij}$ vanishes: for $k<i$, the first factor vanishes, and for $k\ge i>j$, the second factor vanishes. Thus $AB$ is upper triangular. In a diagonal entry $(AB)_{jj}$, a term with $k<j$ has $A_{jk}=0$, and a term with $k>j$ has $B_{kj}=0$. Hence $(AB)_{jj}=A_{jj}B_{jj}$.
Choose a triangular basis for $T$, with matrix $A$ and diagonal entries $\lambda_1,\ldots,\lambda_n$. Repeatedly applying the preceding product observation shows that $A^k$ is triangular with diagonal entries $\lambda_j^k$ for every $k\ge0$, including $A^0=I$. Matrix representation respects sums, scalar multiples, and composition, so the matrix of $p(T)$ is $p(A)$. It is triangular with diagonal entries $p(\lambda_1),\ldots,p(\lambda_n)$. The triangular eigenvalue theorem identifies the eigenvalue sets of $T$ and $p(T)$ with the distinct values in the corresponding diagonal lists, proving the assertion. This includes constant $p$. If $n=0$, both diagonal lists and both eigenvalue sets are empty, so the statement still holds.''',
    3, 45,
    [r'Triangularize $T$ and determine the diagonal of a product of triangular matrices.'],
    ['thm-complex-triangularization', 'thm-triangular-eigenvalues', 'def-upper-triangular', 'def-polynomial-operator', 'def-operator-powers', 'c3-def-matrix-product', 'c3-thm-matrix-addition', 'c3-thm-matrix-scaling', 'c3-thm-matrix-composition', 'c3-lem-identity-matrix-laws'],
    kind='exercise', optional=True,
)

s.r(
    'ex-direct-sum-minimal-polynomial',
    'Minimal polynomials on an invariant direct sum',
    r'''Suppose $V=U\oplus W$ is finite-dimensional and both subspaces are invariant under $T$. Let $\mu_U,\mu_W,\mu$ be the minimal polynomials of $T|_U,T|_W,T$, respectively. Prove that $\mu$ is a common multiple of $\mu_U,\mu_W$ and divides every polynomial that is a common multiple of them. Deduce that if
\[\mu_U=(z-1)^2(z+2),\qquad \mu_W=(z-1)(z+2)^3,\]
then $\mu=(z-1)^2(z+2)^3$.''',
    r'''Polynomial evaluation commutes with restriction to an invariant subspace. Thus $p(T)=0$ implies that $p$ annihilates both restrictions. Conversely, if $p$ annihilates both restrictions, write any $v=u+w$ with $u\in U,w\in W$. Then
\[p(T)v=p(T)u+p(T)w=0,\]
so $p(T)=0$. The annihilating-divisibility theorem therefore says that $p$ is a multiple of $\mu$ exactly when it is a multiple of both $\mu_U$ and $\mu_W$. Taking $p=\mu$ proves that $\mu$ is a common multiple, and taking any common multiple proves that $\mu$ divides it.
For the stated example, $q=(z-1)^2(z+2)^3$ is a common multiple, so $\mu$ divides $q$. Since each restricted minimal polynomial divides $\mu$, the root $1$ must occur at least twice in $\mu$ and the root $-2$ at least three times. These multiplicity comparisons follow by factoring the divisibility equalities over $\C$ and using uniqueness of complex factorization; real coefficient equalities extend to complex arguments when necessary. Divisibility of $\mu$ into $q$ permits no additional factors or larger multiplicities. Monicity therefore gives $\mu=q$. Zero subspaces cause no exception to the first assertion, because their minimal polynomial is $1$.''',
    3, 40,
    [r'A polynomial annihilates the whole direct sum exactly when it annihilates both restrictions.', r'For the example, compare the required repetition counts of each factor.'],
    ['def-invariant', 'lem-restriction-polynomial', 'def-minimal-polynomial', 'thm-annihilating-divisibility', 'c1-def-direct-sum', 'c4-thm-complex-factorization', 'c4-lem-conjugate-polynomial'],
    kind='exercise', optional=True,
)

s.r(
    'ex-commuting-sums-products',
    'Paired eigenvalues in a simultaneous eigenvector basis',
    r'''Suppose $S,T$ are commuting diagonalizable operators on a finite-dimensional space. Prove that $S+T$ and $ST$ are diagonalizable. If a common eigenvector basis satisfies $Sv_j=\alpha_jv_j$ and $Tv_j=\beta_jv_j$, identify the eigenvalues of the sum and product. Give an example showing that an arbitrary eigenvalue of $S$ cannot always be paired with an arbitrary eigenvalue of $T$ to obtain an eigenvalue of $S+T$.''',
    r'''Simultaneous diagonalization supplies the stated common eigenvector basis. On each basis vector,
\[(S+T)v_j=(\alpha_j+\beta_j)v_j,\qquad
STv_j=S(\beta_jv_j)=\alpha_j\beta_jv_j.\]
Hence the same basis diagonalizes both operators. Their eigenvalues are exactly the distinct values among the paired sums $\alpha_j+\beta_j$ and paired products $\alpha_j\beta_j$, because these are their diagonal entries. For a zero-dimensional space, the basis and lists are empty.
For the requested distinction, on $\F^2$ take
\[S(x,y)=(0,y),\qquad T(x,y)=(x,0).\]
Their standard matrices are diagonal, so they commute and are diagonalizable. Each has both $0$ and $1$ as eigenvalues. But $S+T=I$, whose only eigenvalue is $1$. In particular, pairing the eigenvalue $0$ of $S$ with the eigenvalue $0$ of $T$ gives $0$, which is not an eigenvalue of their sum. The two eigenvalues must arise on the same common eigenvector for the paired formula to apply.''',
    2, 20,
    [r'Use a common eigenvector basis and keep the two eigenvalues attached to the same basis vector.'],
    ['thm-simultaneous-diagonalization', 'thm-diagonalizable-equivalences', 'thm-triangular-eigenvalues', 'c3-def-map-composition', 'c3-def-map-operations'],
    kind='exercise', optional=True,
)

s.r(
    'ex-power-zero-perturbation',
    'A commuting perturbation whose power vanishes',
    r'''Suppose $S$ is diagonalizable on a finite-dimensional space, $SN=NS$, and $N^r=0$ for some positive integer $r$. Prove that $S+N$ is diagonalizable if and only if $N=0$.''',
    r'''If $N=0$, then $S+N=S$ is diagonalizable. Conversely, suppose $S+N$ is diagonalizable. The commutation hypothesis gives
\[S(S+N)=S^2+SN=S^2+NS=(S+N)S.\]
Thus $S$ and $S+N$ are commuting diagonalizable operators and admit a common eigenvector basis. For a vector $v_j$ in this basis, write $Sv_j=\alpha_jv_j$ and $(S+N)v_j=\beta_jv_j$. Subtracting gives $Nv_j=(\beta_j-\alpha_j)v_j$. Therefore
\[0=N^rv_j=(\beta_j-\alpha_j)^rv_j.\]
Since $v_j\ne0$ and a nonzero scalar has nonzero positive integer powers, $\beta_j-\alpha_j=0$. Hence $N$ vanishes on every basis vector and is the zero operator. If the space is zero, its sole operator is already zero and the assertion holds.''',
    3, 30,
    [r'If both $S$ and $S+N$ are diagonalizable, diagonalize these two commuting operators together.'],
    ['thm-simultaneous-diagonalization', 'def-operator-powers', 'lem-polynomial-eigenvector', 'c3-thm-composition-laws', 'c3-thm-linear-map-basis', 'c1-lem-scalar-cancellation'],
    kind='exercise', optional=True,
)

s.r(
    'ex-invariant-subspaces-simple-spectrum',
    'All invariant subspaces when the eigenvalues are distinct',
    r'''Suppose $T$ acts on an $n$-dimensional space and has $n$ distinct eigenvalues $\lambda_1,\ldots,\lambda_n$. Choose corresponding eigenvectors $v_1,\ldots,v_n$. Prove that the invariant subspaces of $T$ are exactly the spans of subsets of this eigenvector basis. Deduce that there are exactly $2^n$ invariant subspaces.''',
    r'''The distinct eigenvectors are independent and number $n$, so they form a basis. The span of any subset is invariant because $T$ multiplies each of its generators by a scalar.
Conversely, let $U$ be invariant. Invariance under $T$ implies invariance under each power by induction, and hence under every polynomial in $T$ by closure under sums and scalar multiplication. For $1\le j\le n$, define
\[L_j(z)=\prod_{k\ne j}\frac{z-\lambda_k}{\lambda_j-\lambda_k}.\]
All denominators are nonzero, and evaluation gives $L_j(\lambda_i)=1$ if $i=j$ and zero otherwise. The polynomial-eigenvector identity therefore shows that, for $u=\sum_i c_iv_i\in U$,
\[L_j(T)u=c_jv_j\in U.\]
Whenever a member of $U$ has $c_j\ne0$, scalar multiplication by $c_j^{-1}$ proves $v_j\in U$. Let $J$ be the indices that occur with nonzero coefficient in at least one vector of $U$. The preceding argument gives $\Span(v_j:j\in J)\subseteq U$, and the definition of $J$ gives the reverse inclusion. Thus $U$ is the span of a subset.
Different subsets have different spans, because a basis vector cannot be expressed using the other basis vectors. There are $2^n$ subsets, yielding the count. If $n=0$, the space is $\{0\}$ and its only invariant subspace is the span of the empty subset; the count is $2^0=1$.''',
    3, 45,
    [r'Build polynomials that isolate one eigenvalue at a time.', r'Apply them to a vector of an invariant subspace to recover its individual eigenvector components.'],
    ['thm-distinct-eigenvectors', 'c2-thm-full-length-independent', 'def-invariant', 'def-polynomial-operator', 'lem-polynomial-eigenvector', 'c4-lem-polynomial-product-degree', 'c1-def-field'],
    kind='exercise', optional=True,
)

s.r(
    'ex-cyclic-commutant',
    'An operator determined by one vector controls its commuting maps',
    r'''Suppose $n=\dim V\ge1$ and there exists $v\in V$ such that
\[v,Tv,\ldots,T^{n-1}v\]
is a basis. Prove that an operator $S$ commutes with $T$ exactly when $S=p(T)$ for a polynomial $p$ of degree at most $n-1$. Prove that this polynomial is unique and that the vector space of operators commuting with $T$ has dimension $n$.''',
    r'''Every polynomial in $T$ commutes with $T$, by commutation of polynomial evaluations. Conversely, suppose $ST=TS$. Induction gives $ST^j=T^jS$ for all nonnegative integers $j$: the identity case holds, and multiplication by $T$ followed by $ST=TS$ proves the next case. Expand $Sv$ uniquely in the given basis, say
\[Sv=\sum_{k=0}^{n-1}a_kT^kv,\]
and put $p(z)=\sum_{k=0}^{n-1}a_kz^k$. For $0\le j<n$,
\[S(T^jv)=T^jSv=T^jp(T)v=p(T)T^jv.\]
Thus $S$ and $p(T)$ agree on a basis and are equal.
If $p(T)=q(T)$ for two polynomials of degree at most $n-1$, applying their difference to $v$ produces a zero combination of the displayed basis. All coefficient differences vanish, so $p=q$.
The commuting operators form a subspace: the zero operator commutes, and if $S,R$ commute, distributivity gives $(aS+bR)T=T(aS+bR)$ for any scalars $a,b$. The operators $I,T,\ldots,T^{n-1}$ span this subspace by the representation just proved. They are independent because a zero relation on them, applied to $v$, becomes a zero relation on the given basis. Consequently they form a basis of the commuting subspace, whose dimension is $n$.''',
    4, 60,
    [r'A commuting operator is determined by its value on $v$, because its values on all $T^jv$ then follow.'],
    ['def-commute', 'def-operator-powers', 'def-polynomial-operator', 'thm-polynomial-evaluation-product', 'c3-thm-linear-map-basis', 'c3-thm-composition-laws', 'c3-thm-linear-map-space', 'c2-thm-basis-coordinates', 'c2-def-basis', 'c2-def-dimension'],
    kind='exercise', optional=True,
)

s.r(
    'ex-gershgorin-shifts',
    'Invertible shifts from eigenvalue location',
    r'''Let $T$ on $\C^3$ have standard matrix
\[A=\begin{pmatrix}8&1&-1\\2&9&1\\-1&1&10\end{pmatrix}.\]
Prove that every eigenvalue $\lambda$ of $T$ satisfies $\operatorname{Re}\lambda\ge6$. Deduce that $T+tI$ is invertible for every real $t>-6$, and that every eigenvalue $\mu$ of $T^{-1}$ satisfies $|\mu|\le1/6$.''',
    r'''The Gershgorin disks have centers $8,9,10$ and respective radii $2,3,2$. If $\lambda$ belongs to a disk with real center $a$ and radius $r$, then
\[\operatorname{Re}\lambda
=a+\operatorname{Re}(\lambda-a)
\ge a-|\lambda-a|\ge a-r.\]
The three lower bounds are $6,6,8$, so Gershgorin gives $\operatorname{Re}\lambda\ge6$ for every eigenvalue.
If $T+tI$ were not invertible, the eigenvalue criterion would supply a nonzero vector $v$ with $Tv=-tv$. Thus $-t$ would be an eigenvalue of $T$. But $t>-6$ gives the real number $-t<6$, contradicting the bound. Hence every stated shift is invertible, including $T$ itself when $t=0$.
If $T^{-1}v=\mu v$ with $v\ne0$, then $\mu\ne0$ because $T^{-1}$ is injective. Applying $T$ gives $v=\mu Tv$, so $Tv=\mu^{-1}v$. The preceding bound yields
\[6\le\operatorname{Re}(\mu^{-1})\le|\mu^{-1}|=|\mu|^{-1}.\]
Multiplicativity of modulus justifies the reciprocal identity. Therefore $|\mu|\le1/6$.''',
    3, 30,
    [r'Find a common lower bound for the real parts of points in all three disks.', r'A failure of invertibility of $T+tI$ would make $-t$ an eigenvalue of $T$.'],
    ['def-gershgorin-disks', 'thm-gershgorin', 'thm-eigenvalue-tests', 'def-eigenvalue', 'c3-def-map-inverse', 'c3-thm-invertible-bijective', 'c4-thm-complex-properties'],
    kind='exercise', optional=True,
)

s.r(
    'ex-weighted-gershgorin',
    'Rescaling a basis sharpens Gershgorin bounds',
    r'''Let $A$ be the standard matrix of $T\in\Lin(\C^n)$, where $n\ge1$, and choose positive real numbers $w_1,\ldots,w_n$. Prove that every eigenvalue belongs to at least one disk
\[\left\{z\in\C:|z-A_{jj}|\le\sum_{k\ne j}|A_{jk}|\frac{w_k}{w_j}\right\}.\]
Deduce that $T$ is invertible if
\[|A_{jj}|w_j>\sum_{k\ne j}|A_{jk}|w_k\quad\text{for every }j.\]
Apply the result with $(w_1,w_2)=(8,1)$ to
\[A=\begin{pmatrix}1&4\\1/16&2\end{pmatrix},\]
and show that all its eigenvalues have real part at least $1/2$.''',
    r'''Because every $w_j$ is nonzero, the list $f_j=w_je_j$ is a basis: it is independent by comparing standard coordinates and spans because $e_j=w_j^{-1}f_j$. The image formula
\[Tf_k=w_k\sum_jA_{jk}e_j
=\sum_j A_{jk}\frac{w_k}{w_j}f_j\]
shows that the matrix in this basis has entries $B_{jk}=A_{jk}w_k/w_j$. Its diagonal entries are $A_{jj}$. Since the weights are positive, its Gershgorin radii are exactly the weighted sums in the statement. The disk theorem gives the asserted inclusion.
Under the strict inequalities, each disk has radius strictly smaller than the modulus of its center. None contains zero, because membership of zero would require $|A_{jj}|$ to be at most that radius. Thus zero is not an eigenvalue and $T$ is invertible.
For the displayed matrix and weights, the two radii are $4/8=1/2$ and $8/16=1/2$, with centers $1$ and $2$. Each disk has real part at least its center minus its radius, giving bounds $1/2$ and $3/2$. Hence every eigenvalue has real part at least $1/2$, and the matrix represents an invertible operator.''',
    3, 45,
    [r'Use the basis $w_1e_1,\ldots,w_ne_n$ and compute its matrix directly.'],
    ['c3-def-map-matrix', 'c2-def-basis', 'thm-gershgorin', 'def-gershgorin-disks', 'thm-eigenvalue-tests', 'c4-thm-complex-properties'],
    kind='exercise', optional=True,
)

s.r(
    'ex-count-square-roots',
    'Counting square roots of an operator with simple nonzero spectrum',
    r'''Suppose $T$ acts on an $n$-dimensional complex space and has $n$ distinct nonzero eigenvalues. Prove that exactly $2^n$ operators $R$ satisfy $R^2=T$. Include the case $n=0$.''',
    r'''For $n=0$, there is only one operator, and its square is the unique operator $T$. Thus the count is $1=2^0$. Suppose $n\ge1$. Choose corresponding eigenvectors $v_1,\ldots,v_n$ with eigenvalues $\lambda_1,\ldots,\lambda_n$. They form a basis. Each eigenspace is the line $\Span(v_j)$: comparison of coefficients in this basis shows that $Tv=\lambda_jv$ forces every coefficient at an eigenvector for another eigenvalue to vanish.
If $R^2=T$, then $RT=R^3=TR$. Commutation makes every eigenspace of $T$ invariant under $R$, so $Rv_j=r_jv_j$ for some scalar $r_j$. Squaring gives $r_j^2=\lambda_j$.
Each nonzero complex scalar $\lambda_j$ has exactly two square roots. Indeed, the fundamental theorem of algebra gives a root $\beta$ of $z^2-\lambda_j$; it is nonzero, and
\[z^2-\lambda_j=(z-\beta)(z+\beta).\]
The roots are therefore exactly $\beta,-\beta$, and they are distinct because $\beta\ne0$ and $2\ne0$.
There are two independent choices for each $r_j$, hence $2^n$ possible lists. Each list defines a unique linear operator by prescribing $Rv_j=r_jv_j$, and its square agrees with $T$ on every basis vector, so equals $T$. Different lists give different operators on at least one basis vector. The preceding commutation argument shows that every square root arises in this way, proving the exact count.''',
    4, 60,
    [r'Any square root of $T$ commutes with $T$.', r'Use the one-dimensional eigenspaces to reduce the problem to scalar square roots.'],
    ['thm-distinct-eigenvectors', 'c2-thm-full-length-independent', 'def-eigenspace', 'thm-commuting-eigenspace', 'c3-thm-linear-map-basis', 'c3-thm-composition-laws', 'c4-thm-fundamental-algebra', 'c1-lem-scalar-cancellation'],
    kind='exercise', optional=True,
)

s.r(
    'ex-reversed-products-minimal',
    'Reversing two factors changes only the possible zero factor',
    r'''Let $S,T\in\Lin(V)$ with $V$ finite-dimensional over $\C$. Put $A=ST$ and $B=TS$, with minimal polynomials $\mu_A,\mu_B$. Prove:
\begin{enumerate}
\item For every $\lambda\ne0$, the map $v\mapsto Tv$ is an isomorphism from $E(\lambda,A)$ onto $E(\lambda,B)$, with inverse $w\mapsto\lambda^{-1}Sw$.
\item $A,B$ have exactly the same eigenvalues, including zero.
\item $\mu_B$ divides $z\mu_A$ and $\mu_A$ divides $z\mu_B$. Consequently their nonzero roots have equal multiplicities, while the multiplicities of zero differ by at most one.
\end{enumerate}
Give an example in which the multiplicities of zero in the two minimal polynomials do differ.''',
    r'''If $Av=\lambda v$, associativity gives
\[B(Tv)=T(Av)=\lambda Tv.\]
Thus $T$ maps the first eigenspace into the second. Similarly, if $Bw=\lambda w$, then $A(Sw)=S(Bw)=\lambda Sw$. On these eigenspaces the two stated maps compose as
\[\lambda^{-1}STv=\lambda^{-1}Av=v,\qquad
\lambda^{-1}TSw=\lambda^{-1}Bw=w.\]
They are linear and mutually inverse, proving the first assertion. In particular, a nonzero eigenspace for a nonzero scalar exists for $A$ exactly when it exists for $B$.

For zero, suppose $A=ST$ is invertible. If $Tv=0$, then $Av=0$, so $v=0$; thus $T$ is injective. Surjectivity of $A$ implies surjectivity of $S$, because every $v$ equals $STu$ for some $u$ and is therefore in the range of $S$. In finite dimensions, both $S$ and $T$ are consequently invertible. Their product $B$ is invertible, with inverse $S^{-1}T^{-1}$, as checking both compositions shows. Reversing the roles of $S,T$ proves the converse. Thus $A$ is noninvertible exactly when $B$ is, and the eigenvalue test gives the same status for eigenvalue zero.

For the divisibility statements, induction on $k\ge0$ gives
\[TA^kS=B^{k+1}.\]
At $k=0$ this is $TS=B$. If it holds at $k$, then
\[TA^{k+1}S=TA^k(ST)S=(TA^kS)(TS)=B^{k+1}B=B^{k+2}.\]
Write $\mu_A(z)=\sum_k a_kz^k$. It follows that
\[0=T\mu_A(A)S=\sum_k a_kB^{k+1}=(z\mu_A)(B).\]
Thus $z\mu_A$ annihilates $B$, and the annihilating-divisibility theorem gives $\mu_B\mid z\mu_A$. Interchanging $S,T$ gives $\mu_A\mid z\mu_B$.
By uniqueness of complex factorization, divisibility compares root multiplicities. For a nonzero root $\lambda$, multiplication by $z$ changes no multiplicity at $\lambda$, so the two divisibilities give opposite inequalities and hence equality. At zero, each multiplication by $z$ raises the multiplicity by one; the two divisibilities give
\[m_B(0)\le m_A(0)+1,\qquad m_A(0)\le m_B(0)+1.\]
Their difference in either direction is therefore at most one. Absent roots have multiplicity zero. The zero-dimensional case has both minimal polynomials equal to $1$ and satisfies these statements as well.

For a strict difference, on $\C^2$ take $S(x,y)=(x,0)$ and $T(x,y)=(y,0)$. Then $ST=T\ne0$ and $TS=0$. The operator $T$ has square zero but is nonzero. Its minimal polynomial is $z^2$: a degree-one monic annihilator would make $T$ a scalar multiple of the identity, and applying it to $e_1$ would force that scalar to be zero, contradicting $Te_2=e_1$. The zero operator on this nonzero space has minimal polynomial $z$, since $z$ annihilates it and no nonzero constant polynomial does. Thus the zero multiplicities are two and one.''',
    4, 75,
    [
        r'Use $T(ST)=(TS)T$ to transport nonzero eigenspaces.',
        r'For minimal polynomials, insert $T$ on the left and $S$ on the right of an annihilating identity.',
        r'Test a coordinate projection and an operator that sends one coordinate vector to another.',
    ],
    ['def-eigenspace', 'thm-eigenvalue-tests', 'def-minimal-polynomial', 'thm-annihilating-divisibility', 'def-polynomial-operator', 'c3-thm-composition-laws', 'c3-thm-equal-dimension-invertibility', 'c3-def-map-inverse', 'c3-def-isomorphism', 'c4-thm-complex-factorization', 'c4-def-root-multiplicity'],
    kind='exercise', optional=True,
)

s.card('ex-affine-eigenvalues', 'ex-affine-eigenspaces',
r'For $a\ne0$, how does replacing $T$ by $aT+bI$ change its eigenspaces?',
r'$E(a\lambda+b,aT+bI)=E(\lambda,T)$.')

s.card('ex-inverse-minimal', 'ex-inverse-minimal-polynomial',
r'How is the minimal polynomial of an invertible operator transformed for its inverse?',
r'Reverse its coefficient list and divide by the original nonzero constant coefficient to make the result monic.')

s.card('ex-spectral-mapping', 'ex-polynomial-spectral-mapping',
r'Over $\C$ in finite dimensions, what are the eigenvalues of $p(T)$?',
r'Exactly the values $p(\lambda)$ at eigenvalues $\lambda$ of $T$.')

s.card('ex-invariant-simple-spectrum', 'ex-invariant-subspaces-simple-spectrum',
r'What are the invariant subspaces of an operator with $n$ distinct eigenvalues on an $n$-dimensional space?',
r'Exactly the spans of subsets of an eigenvector basis; there are $2^n$.')

s.card('ex-cyclic-commutant', 'ex-cyclic-commutant',
r'If $v,Tv,\ldots,T^{n-1}v$ is a basis, what do the operators commuting with $T$ look like?',
r'Each is uniquely $p(T)$ with $\deg p\le n-1$.')

s.card('ex-weighted-disks', 'ex-weighted-gershgorin',
r'Which basis gives weighted Gershgorin radii $\sum_{k\ne j}|A_{jk}|w_k/w_j$?',
r'The rescaled basis $w_1e_1,\ldots,w_ne_n$.')

s.card('ex-square-root-count', 'ex-count-square-roots',
r'How many square roots does a complex operator with $n$ distinct nonzero eigenvalues have?',
r'Exactly $2^n$, obtained by choosing one of two scalar square roots on each eigenvector line.')

s.card('ex-reversed-products', 'ex-reversed-products-minimal',
r'How can the minimal polynomials of $ST$ and $TS$ differ?',
r'Their nonzero roots have equal multiplicities; the multiplicities of zero can differ by at most one.')

s.write()
