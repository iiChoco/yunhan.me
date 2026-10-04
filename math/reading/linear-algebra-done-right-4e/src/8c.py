from common import Section

s = Section('8c')

s.p(
    'intro-roots-jordan',
    'Constructing roots and organizing invariant chains',
    r'''Throughout this section, $V$ is finite-dimensional over $\F$, where $\F$ is $\R$ or $\C$. We first construct roots by solving finitely many coefficient equations. We then use generalized eigenspaces to assemble bases in which an operator has especially simple blocks.''',
    '319',
)

s.d(
    'def-operator-root',
    'Roots of an operator',
    r'''For a positive integer $k$, a \emph{$k$th root} of $T\in\Lin(V)$ is an operator $R\in\Lin(V)$ satisfying $R^k=T$. A root with $k=2$ is called a \emph{square root}.''',
    '', '319',
)

s.r(
    'ex-nilpotent-without-square-root',
    'A complex operator without a square root',
    r'''The operator $T\in\Lin(\C^3)$ defined by
    \[
    T(z_1,z_2,z_3)=(z_2,z_3,0)
    \]
    has no square root.''',
    r'''Successive application gives
    \[
    T^2(z_1,z_2,z_3)=(z_3,0,0),\qquad T^3=0.
    \]
    In particular, $T^2\ne0$. Suppose $R^2=T$. Then $R^6=T^3=0$, so $R$ is nilpotent. The dimension bound for nilpotent operators gives $R^3=0$ on $\C^3$. Consequently
    \[
    T^2=R^4=R R^3=0,
    \]
    contradicting the computed value of $T^2$.''',
    3, 30,
    [
        r'''A square root of this operator would itself be nilpotent.''',
        r'''Compare $R^6=0$ with the dimension bound on a nilpotent operator on $\C^3$.''',
    ],
    ['def-operator-root', 'thm-nilpotent-index-bound', 'c5-lem-operator-power-laws'],
    '', '319', kind='example',
)

s.r(
    'thm-identity-nilpotent-square-root',
    'The identity plus a nilpotent operator has a square root',
    r'''If $N\in\Lin(V)$ is nilpotent, then $I+N$ has a square root. The square root can be chosen to be a polynomial in $N$ with real coefficients, even when $\F=\C$.''',
    r'''Choose a positive integer $m$ such that $N^m=0$. We construct a polynomial
    \[
    q(z)=1+a_1z+\cdots+a_{m-1}z^{m-1}
    \]
    for which $q(z)^2-(1+z)$ is divisible by $z^m$. If $m=1$, take $q=1$; the difference is $-z$, which is divisible by $z$.
    For $m\ge2$, set $a_0=1$ and choose the coefficients successively. For $1\le j<m$, the coefficient of $z^j$ in $q(z)^2$ is
    \[
    2a_j+\sum_{i=1}^{j-1}a_i a_{j-i}.
    \]
    Put $d_1=1$ and $d_j=0$ for $j\ge2$, and define
    \[
    a_j=\frac12\left(d_j-\sum_{i=1}^{j-1}a_i a_{j-i}\right).
    \]
    Each right side involves only previously chosen real coefficients. This makes the coefficients of degrees $0,1,\ldots,m-1$ in $q^2$ agree with those of $1+z$. Therefore $q(z)^2-(1+z)=z^m h(z)$ for a polynomial $h$.
    Polynomial evaluation respects sums and products, so
    \[
    q(N)^2-(I+N)=N^m h(N)=0.
    \]
    Thus $q(N)$ is a square root of $I+N$. The argument includes the zero space because the chosen positive power still vanishes there.''',
    3, 40,
    [
        r'''Seek a root of the form $I+a_1N+\cdots+a_{m-1}N^{m-1}$ when $N^m=0$.''',
        r'''In the square, the coefficient of $N^j$ is $2a_j$ plus an expression involving only earlier coefficients.''',
    ],
    [
        'def-operator-root', 'def-nilpotent',
        'c5-thm-polynomial-evaluation-linear',
        'c5-thm-polynomial-evaluation-product',
    ],
    '8.39', '319',
)

s.r(
    'ex-real-invertible-without-square-root',
    'Invertibility alone does not give a real square root',
    r'''The operator $T:\R\to\R$ defined by $Tx=-x$ is invertible but has no square root in $\Lin(\R)$.''',
    r'''Because $T^2=I$, the operator $T$ is its own inverse. Every real-linear operator $R:\R\to\R$ has the form $Rx=ax$, where $a=R1$, because $Rx=R(x\cdot1)=xR1$. Hence $R^2x=a^2x$. The equation $R^2=T$ would imply $a^2=-1$ upon evaluation at $1$, which is impossible for a real scalar.''',
    1, 10,
    [r'''A linear operator on $\R$ is multiplication by its value at $1$.'''],
    ['def-operator-root', 'c3-def-linear-map', 'c3-def-invertible-map'],
    '', '320', kind='example',
)

s.r(
    'lem-complex-scalar-roots',
    'Complex scalars have roots of every positive order',
    r'''If $\lambda\in\C$ and $k\ge1$ is an integer, then some $\mu\in\C$ satisfies $\mu^k=\lambda$. If $\lambda\ne0$, every such $\mu$ is nonzero.''',
    r'''The polynomial $z^k-\lambda$ is nonconstant, so the fundamental theorem of algebra supplies a root $\mu$. The root equation is $\mu^k=\lambda$. If $\mu=0$, this equation gives $\lambda=0$, proving the last assertion.''',
    1, 10,
    [r'''Apply the fundamental theorem of algebra to a polynomial whose root equation is the desired identity.'''],
    ['c4-thm-fundamental-algebra'],
    '', '320', kind='lemma',
)

s.r(
    'thm-invertible-square-root',
    'Every invertible complex operator has a square root',
    r'''If $V$ is complex and $T\in\Lin(V)$ is invertible, then $T$ has a square root.''',
    r'''If $V=\{0\}$, its only operator squares to itself, proving the assertion. Suppose $V\ne\{0\}$, and let $\lambda_1,\ldots,\lambda_p$ be the distinct eigenvalues of $T$. They are nonzero because $T$ is invertible. The generalized eigenspace decomposition gives
    \[
    V=G(\lambda_1,T)\oplus\cdots\oplus G(\lambda_p,T).
    \]
    Write $G_j=G(\lambda_j,T)$ and
    \[
    N_j=(T-\lambda_j I)|_{G_j}.
    \]
    Each $G_j$ is invariant under $T$, and each $N_j$ is nilpotent. Hence $M_j=\lambda_j^{-1}N_j$ is nilpotent: if $N_j^{a}=0$, then $M_j^{a}=\lambda_j^{-a}N_j^{a}=0$.
    Choose $Q_j\in\Lin(G_j)$ with $Q_j^2=I_{G_j}+M_j$, and choose $\mu_j\in\C$ with $\mu_j^2=\lambda_j$. Then $R_j=\mu_jQ_j$ satisfies
    \[
    R_j^2=\lambda_j(I_{G_j}+M_j)
    =\lambda_j I_{G_j}+N_j=T|_{G_j}.
    \]
    For the unique decomposition $v=v_1+\cdots+v_p$, with $v_j\in G_j$, define
    \[
    Rv=R_1v_1+\cdots+R_pv_p.
    \]
    Uniqueness makes this definition well-defined. The components of $av+bw$ are $av_j+bw_j$, so linearity of the $R_j$ proves linearity of $R$. Since $R_jv_j$ remains in $G_j$, applying $R$ twice gives
    \[
    R^2v=\sum_{j=1}^p R_j^2v_j
    =\sum_{j=1}^p Tv_j=Tv.
    \]
    Therefore $R^2=T$.''',
    3, 45,
    [
        r'''Construct a square root separately on each generalized eigenspace.''',
        r'''On $G(\lambda,T)$, write $T=\lambda(I+\lambda^{-1}N)$ with $N$ nilpotent.''',
        r'''Use the direct-sum decomposition to combine the roots on the summands.''',
    ],
    [
        'thm-identity-nilpotent-square-root', 'lem-complex-scalar-roots',
        'thm-generalized-eigenspace-decomposition',
        'thm-generalized-restriction-nilpotent',
        'c5-thm-eigenvalue-tests', 'c5-lem-operator-power-laws',
        'c1-def-direct-sum',
    ],
    '8.41', '320',
)

s.r(
    'lem-identity-nilpotent-kth-root',
    'Finite coefficient recursion constructs higher roots',
    r'''Let $N\in\Lin(V)$ be nilpotent and let $k\ge1$ be an integer. Then $I+N$ has a $k$th root that is a polynomial in $N$ with real coefficients.''',
    r'''Choose $m\ge1$ with $N^m=0$. Set $a_0=1$ and seek
    \[
    q(z)=\sum_{j=0}^{m-1}a_jz^j
    \]
    such that $q(z)^k-(1+z)$ is divisible by $z^m$. Its constant coefficient already agrees with that of $1+z$.
    Suppose $1\le j<m$ and $a_1,\ldots,a_{j-1}$ have been chosen. In expanding the product of $k$ copies of $q$, a contribution to the coefficient of $z^j$ that involves $a_j$ must choose $a_jz^j$ from exactly one copy and the constant term from every other copy. These $k$ contributions total $ka_j$. Every remaining contribution has the form
    $a_{i_1}\cdots a_{i_k}$ with
    \[
    0\le i_\ell<j,\qquad i_1+\cdots+i_k=j.
    \]
    Let $B_j$ be the sum of these remaining contributions, with an empty sum interpreted as zero. It depends only on already chosen coefficients. If $d_1=1$ and $d_j=0$ for $j\ge2$, choose
    \[
    a_j=\frac{d_j-B_j}{k}.
    \]
    Division by the positive integer $k$ is valid over $\R$ and $\C$. This recursion produces real coefficients making every coefficient of degree less than $m$ agree with that of $1+z$. For $m=1$, there are no recursive steps and the same coefficient statement holds.
    Thus $q(z)^k-(1+z)=z^m h(z)$ for a polynomial $h$. Evaluating at $N$ gives
    \[
    q(N)^k-(I+N)=N^m h(N)=0,
    \]
    so $q(N)$ is the desired root.''',
    3, 40,
    [
        r'''In the coefficient of $z^j$ in $q(z)^k$, isolate the terms containing the coefficient $a_j$.''',
        r'''There are exactly $k$ such terms when $q(0)=1$; every other term uses coefficients of smaller index.''',
    ],
    [
        'def-nilpotent', 'def-operator-root',
        'c5-thm-polynomial-evaluation-linear',
        'c5-thm-polynomial-evaluation-product',
    ],
    '', '320', kind='lemma',
)

s.r(
    'thm-invertible-kth-root',
    'Invertible complex operators have roots of every positive order',
    r'''For every invertible operator $T$ on a finite-dimensional complex space and every positive integer $k$, there exists $R\in\Lin(V)$ such that $R^k=T$.''',
    r'''The zero-space case holds because its only operator has every positive power equal to itself. Otherwise use the generalized eigenspace decomposition
    \[
    V=G_1\oplus\cdots\oplus G_p,\qquad G_j=G(\lambda_j,T).
    \]
    Invertibility gives $\lambda_j\ne0$, and
    $N_j=(T-\lambda_j I)|_{G_j}$ is nilpotent. Hence $\lambda_j^{-1}N_j$ is nilpotent. By the preceding lemma, choose $Q_j$ with
    \[
    Q_j^k=I_{G_j}+\lambda_j^{-1}N_j.
    \]
    Choose a complex scalar $\mu_j$ with $\mu_j^k=\lambda_j$, and put $R_j=\mu_jQ_j$. Scalar multiplication commutes with composition, so
    \[
    R_j^k=\lambda_j Q_j^k=T|_{G_j}.
    \]
    Define $R(\sum_jv_j)=\sum_jR_jv_j$ using the unique components $v_j\in G_j$. Componentwise addition and scalar multiplication prove that $R$ is linear. Because every $R_j$ maps $G_j$ to itself, induction on the positive integer $\ell$ gives
    \[
    R^\ell\left(\sum_jv_j\right)=\sum_jR_j^\ell v_j.
    \]
    At $\ell=k$, this becomes $R^kv=\sum_jTv_j=Tv$, proving the assertion.''',
    3, 35,
    [
        r'''Repeat the generalized-eigenspace construction for square roots, using a $k$th root on each summand.''',
        r'''Both the scalar $\lambda$ and the operator $I+\lambda^{-1}N$ have the required $k$th roots.''',
    ],
    [
        'lem-identity-nilpotent-kth-root', 'lem-complex-scalar-roots',
        'thm-generalized-eigenspace-decomposition',
        'thm-generalized-restriction-nilpotent',
        'c5-thm-eigenvalue-tests', 'c5-lem-operator-power-laws',
        'c1-def-direct-sum',
    ],
    '', '320',
)

s.p(
    'intro-jordan-chains',
    'Arranging chains in reverse order',
    r'''If repeated application of a nilpotent operator eventually kills a vector, its successive images form a finite chain. Listing a nonvanishing chain in reverse order makes the operator send each vector to its immediate predecessor. Several such chains can supply a basis even when no single chain is long enough.''',
    '321',
)

s.r(
    'ex-jordan-single-chain',
    'A four-dimensional space filled by one chain',
    r'''Let $T\in\Lin(\C^4)$ be
    \[
    T(z_1,z_2,z_3,z_4)=(0,z_1,z_2,z_3).
    \]
    For $v=(1,0,0,0)$, the list $T^3v,T^2v,Tv,v$ is a basis, and the matrix of $T$ in this basis is
    \[
    \begin{pmatrix}
    0&1&0&0\\
    0&0&1&0\\
    0&0&0&1\\
    0&0&0&0
    \end{pmatrix}.
    \]''',
    r'''Write $e_1,e_2,e_3,e_4$ for the standard basis. The defining formula gives
    $Te_1=e_2$, $Te_2=e_3$, $Te_3=e_4$, and $Te_4=0$. Thus $T^4$ kills every standard basis vector and hence is zero. For $v=e_1$, the proposed list is $e_4,e_3,e_2,e_1$, a reordering of a basis.
    If its vectors are denoted by $b_1,b_2,b_3,b_4$, then
    \[
    Tb_1=0,\qquad Tb_2=b_1,\qquad Tb_3=b_2,\qquad Tb_4=b_3.
    \]
    The coordinate columns of these four images give exactly the displayed matrix.''',
    1, 15,
    [r'''Identify each vector in the proposed list as a standard basis vector, then read off the image of each list member.'''],
    ['c3-def-map-matrix', 'c2-def-basis', 'c5-def-operator-powers'],
    '8.42', '321', kind='example',
)

s.r(
    'ex-jordan-several-chains',
    'Three chains of different lengths',
    r'''Let $T\in\Lin(\C^6)$ be
    \[
    T(z_1,z_2,z_3,z_4,z_5,z_6)=(0,z_1,z_2,0,z_4,0).
    \]
    Then $T^3=0$, and no list $T^5v,T^4v,\ldots,Tv,v$ is a basis of $\C^6$.
    Nevertheless, with $v_1=e_1$, $v_2=e_4$, and $v_3=e_6$, the list
    \[
    T^2v_1,Tv_1,v_1,Tv_2,v_2,v_3
    \]
    is a basis in which the matrix is
    \[
    \begin{pmatrix}
    0&1&0&0&0&0\\
    0&0&1&0&0&0\\
    0&0&0&0&0&0\\
    0&0&0&0&1&0\\
    0&0&0&0&0&0\\
    0&0&0&0&0&0
    \end{pmatrix}.
    \]''',
    r'''The standard basis vectors satisfy
    \[
    Te_1=e_2,\quad Te_2=e_3,\quad Te_3=0,\quad
    Te_4=e_5,\quad Te_5=0,\quad Te_6=0.
    \]
    Applying $T$ three times kills each of them, so $T^3=0$. Hence $T^5v=0$ for every $v$, and the proposed six-vector single-chain list always contains a zero vector, preventing independence.
    The displayed multi-chain list is
    \[
    e_3,e_2,e_1,e_5,e_4,e_6,
    \]
    a reordering of the standard basis. Its first three vectors map respectively to zero, the first vector, and the second vector. Its fourth and fifth vectors map respectively to zero and the fourth vector, and its last vector maps to zero. The corresponding coordinate columns give the stated matrix.''',
    2, 20,
    [r'''Separate the standard basis vectors into the chains beginning at $e_1$, $e_4$, and $e_6$.'''],
    [
        'c3-def-map-matrix', 'c2-def-basis',
        'c2-def-linear-independence', 'c5-def-operator-powers',
    ],
    '8.43', '321', kind='example',
)

s.d(
    'def-jordan-basis',
    'Jordan blocks and Jordan bases',
    r'''For $\lambda\in\F$ and a positive integer $m$, the \emph{Jordan block} $J_m(\lambda)$ is the $m$-by-$m$ matrix with entries
    \[
    (J_m(\lambda))_{ij}=
    \begin{cases}
    \lambda,&i=j,\\
    1,&j=i+1,\\
    0,&\text{otherwise}.
    \end{cases}
    \]
    A \emph{Jordan basis} for $T$ is a basis in which its matrix is block diagonal, with every diagonal block a Jordan block. Blocks may have different sizes and may repeat the same scalar $\lambda$; a block of size one is the matrix $(\lambda)$. The empty basis is a Jordan basis for the operator on the zero space.''',
    '8.44', '322',
)

s.r(
    'lem-jordan-chain-description',
    'Jordan blocks described by their basis vectors',
    r'''A basis grouped into lists
    \[
    b_{j,1},\ldots,b_{j,m_j}\qquad (1\le j\le p)
    \]
    gives the block diagonal matrix with blocks $J_{m_j}(\lambda_j)$ if and only if
    \[
    Tb_{j,1}=\lambda_j b_{j,1},\qquad
    Tb_{j,\ell}=\lambda_j b_{j,\ell}+b_{j,\ell-1}
    \quad(2\le\ell\le m_j).
    \]
    In such a basis, every $\lambda_j$ is an eigenvalue and every basis vector in its block is a generalized eigenvector corresponding to $\lambda_j$.''',
    r'''The column for a basis vector consists of the coordinates of its image. In the first column of the $j$th block, the only possible nonzero entry is $\lambda_j$ in its first position. In every later column, the entries are $\lambda_j$ in that column's diagonal position and $1$ immediately above it. Entries outside the block are zero. Thus reading the columns gives exactly the displayed equations, and conversely those equations give exactly the required columns.
    A basis vector is nonzero, so the first equation makes $\lambda_j$ an eigenvalue. Put $A=T-\lambda_j I$. Within this block, $Ab_{j,1}=0$ and $Ab_{j,\ell}=b_{j,\ell-1}$ for $\ell\ge2$. Applying $A$ repeatedly therefore gives $A^\ell b_{j,\ell}=0$. Each $b_{j,\ell}$ is nonzero, so it is a generalized eigenvector corresponding to $\lambda_j$.''',
    2, 15,
    [r'''Read each column of a Jordan block as the coordinate vector of the image of a basis vector.'''],
    [
        'def-jordan-basis', 'def-generalized-eigenvector',
        'c3-def-map-matrix', 'c5-def-eigenvalue',
    ],
    '', '322', kind='lemma',
)

s.r(
    'lem-nilpotent-invariant-complement',
    'A longest nilpotent chain has an invariant complement',
    r'''Suppose $N\in\Lin(V)$, $m\ge1$, $N^m=0$, and $N^{m-1}u\ne0$. Set
    \[
    U=\Span(u,Nu,\ldots,N^{m-1}u).
    \]
    Then $U$ is invariant under $N$, has dimension $m$, and has a complement $W$ that is also invariant under $N$:
    \[
    V=U\oplus W.
    \]''',
    r'''The independent-chain lemma shows that $u,Nu,\ldots,N^{m-1}u$ is independent. It is therefore a basis of $U$, giving $\dim U=m$. Applying $N$ to any member of this list gives the next member or zero, so $U$ is invariant.
    Extend the list to a basis of $V$. Assign the value $1$ to $N^{m-1}u$ and $0$ to every other member of this extended basis. The theorem defining a linear map by its values on a basis gives a linear map $\varphi:V\to\F$ with these values.
    Define $S:V\to\F^m$ by
    \[
    Sv=\bigl(\varphi(v),\varphi(Nv),\ldots,\varphi(N^{m-1}v)\bigr),
    \qquad W=\Null S.
    \]
    Each coordinate of $S$ is linear, so $S$ is linear and $W$ is a subspace. If $v\in W$, then for $0\le k<m-1$,
    $\varphi(N^kNv)=\varphi(N^{k+1}v)=0$. For $k=m-1$ the same expression is $\varphi(N^mv)=0$. Hence $Nv\in W$, proving invariance.
    To show $U\cap W=\{0\}$, suppose a nonzero vector in the intersection is written
    \[
    v=\sum_{j=0}^{m-1}c_jN^ju.
    \]
    Let $j$ be the smallest index with $c_j\ne0$. Apply $N^{m-1-j}$. All earlier coefficients are zero, and every term of larger index contains a power at least $m$. Thus
    \[
    N^{m-1-j}v=c_jN^{m-1}u.
    \]
    Applying $\varphi$ gives $\varphi(N^{m-1-j}v)=c_j\ne0$, contradicting $v\in W$.
    Finally, rank-nullity and $\Range S\subseteq\F^m$ give
    \[
    \dim W=\dim V-\dim\Range S\ge\dim V-m.
    \]
    Since $U\cap W=\{0\}$, the dimension formula yields
    \[
    \dim(U+W)=\dim U+\dim W\ge m+(\dim V-m)=\dim V.
    \]
    The subspace $U+W$ cannot have dimension greater than $\dim V$, so it has full dimension and equals $V$. Its zero intersection makes the sum direct.''',
    4, 75,
    [
        r'''Choose a linear map $\varphi:V\to\F$ that takes a nonzero value on the last nonzero vector of the chain.''',
        r'''Require $\varphi(v),\varphi(Nv),\ldots,\varphi(N^{m-1}v)$ all to vanish in the proposed complement.''',
        r'''Use the first nonzero coefficient of a chain vector to prove the intersection is zero, then use rank-nullity to show that the sum fills $V$.''',
    ],
    [
        'lem-nilpotent-chain-independent', 'c2-thm-extend-independent',
        'c3-thm-linear-map-basis', 'c3-thm-null-subspace',
        'c3-thm-rank-nullity', 'c2-thm-subspace-dimension',
        'c2-ex-coordinate-dimension', 'c2-thm-dimension-sum',
        'c2-thm-full-dimension-equality', 'c1-thm-direct-intersection',
        'c5-def-invariant',
    ],
    '', '323', kind='lemma',
)

s.r(
    'thm-nilpotent-jordan',
    'Every nilpotent operator has a Jordan basis',
    r'''Every nilpotent operator on a finite-dimensional real or complex vector space has a Jordan basis. Every block in this basis has diagonal entry $0$.''',
    r'''We induct on $n=\dim V$. For $n=0$, the empty basis satisfies the assertion.
    Suppose $n>0$ and the assertion holds in all smaller dimensions. Let $m$ be the least positive integer for which $N^m=0$. The map $N^{m-1}$ is nonzero: for $m>1$ this follows from minimality, and for $m=1$ it follows because $N^0=I$ is nonzero on a nonzero space. Choose $u$ with $N^{m-1}u\ne0$.
    The invariant-complement lemma supplies
    \[
    V=U\oplus W,\qquad
    U=\Span(u,Nu,\ldots,N^{m-1}u),
    \]
    with both summands invariant under $N$ and $\dim U=m\ge1$. The reversed chain
    \[
    N^{m-1}u,N^{m-2}u,\ldots,Nu,u
    \]
    is a basis of $U$. Its first vector is sent to zero and each subsequent vector to its predecessor, so it gives the block $J_m(0)$.
    The restriction $N|_W$ is nilpotent because its $m$th power is zero. Moreover $\dim W=n-m<n$. By induction, $W$ has a Jordan basis for its restriction, with every diagonal block of the form $J_a(0)$.
    Concatenate the reversed-chain basis of $U$ with this basis of $W$. The direct sum makes the concatenated list a basis of $V$: it spans, and any relation separates into zero relations in the two summands. Invariance ensures that the image of a vector in either summand has no coordinates in the other. Hence the resulting matrix is block diagonal, consisting of $J_m(0)$ followed by the Jordan blocks from $W$. This is the desired Jordan basis.''',
    3, 40,
    [
        r'''Use a chain whose length is the nilpotency index.''',
        r'''Apply the invariant-complement lemma, then use induction on the complement.''',
    ],
    [
        'def-nilpotent', 'def-jordan-basis',
        'lem-nilpotent-invariant-complement', 'lem-jordan-chain-description',
        'c2-thm-direct-dimension', 'c5-def-invariant',
        'c5-lem-restriction-polynomial',
    ],
    '8.45', '322–323',
)

s.r(
    'thm-jordan-form',
    'Every complex operator has a Jordan basis',
    r'''Every operator on a finite-dimensional complex vector space has a Jordan basis.''',
    r'''For the zero space, use the empty basis. Otherwise let $\lambda_1,\ldots,\lambda_p$ be the distinct eigenvalues of $T$. The generalized eigenspace decomposition gives
    \[
    V=G(\lambda_1,T)\oplus\cdots\oplus G(\lambda_p,T).
    \]
    Each summand is invariant under $T$, and
    \[
    N_j=(T-\lambda_j I)|_{G(\lambda_j,T)}
    \]
    is nilpotent. Choose a Jordan basis for each $N_j$, using the nilpotent Jordan theorem. Its blocks all have the form $J_a(0)$.
    On this same basis of the $j$th summand, the operator $T$ is $N_j+\lambda_j I$. Its action adds $\lambda_j$ times each basis vector to its image under $N_j$, replacing every block $J_a(0)$ by $J_a(\lambda_j)$.
    Concatenating the bases of the generalized eigenspaces gives a basis of $V$ by the direct-sum decomposition. Invariance of each summand makes all matrix entries between different summands zero. The resulting matrix is therefore block diagonal with Jordan blocks, so the concatenated basis is a Jordan basis for $T$.''',
    3, 30,
    [
        r'''Apply the nilpotent Jordan theorem to $(T-\lambda I)|_{G(\lambda,T)}$.''',
        r'''Adding $\lambda I$ changes only the diagonal entries of each nilpotent Jordan block.''',
    ],
    [
        'thm-generalized-eigenspace-decomposition',
        'thm-generalized-restriction-nilpotent',
        'thm-nilpotent-jordan', 'lem-jordan-chain-description',
        'def-jordan-basis', 'c1-def-direct-sum',
    ],
    '8.46', '324',
)

s.card(
    'operator-root',
    'def-operator-root',
    r'''What is a $k$th root of an operator $T$?''',
    r'''An operator $R$ on the same space satisfying $R^k=T$, where $k$ is a positive integer.''',
)

s.card(
    'nilpotent-square-root-counterexample',
    'ex-nilpotent-without-square-root',
    r'''Give a complex operator that has no square root.''',
    r'''On $\C^3$, $T(z_1,z_2,z_3)=(z_2,z_3,0)$ has no square root. If $R^2=T$, then $R^6=0$, hence $R^3=0$ by the nilpotent dimension bound, contradicting $T^2=R^4\ne0$.''',
)

s.card(
    'identity-nilpotent-root',
    'thm-identity-nilpotent-square-root',
    r'''What finite construction gives a square root of $I+N$ when $N^m=0$?''',
    r'''Choose $q(z)=1+a_1z+\cdots+a_{m-1}z^{m-1}$ recursively so that $q(z)^2-(1+z)$ is divisible by $z^m$. Then $q(N)^2=I+N$.''',
)

s.card(
    'invertible-complex-roots',
    'thm-invertible-kth-root',
    r'''Which roots are guaranteed for an invertible operator on a finite-dimensional complex space?''',
    r'''It has a $k$th root for every positive integer $k$. Construct roots on the generalized eigenspaces and combine them using the direct sum.''',
)

s.card(
    'real-root-obstruction',
    'ex-real-invertible-without-square-root',
    r'''Why does the complex hypothesis matter in the theorem guaranteeing square roots of invertible operators?''',
    r'''On the one-dimensional real space, $T=-I$ is invertible but a square root would have to be multiplication by a real scalar $a$ satisfying $a^2=-1$.''',
)

s.card(
    'jordan-block',
    'def-jordan-basis',
    r'''Describe the entries of a Jordan block $J_m(\lambda)$.''',
    r'''Its diagonal entries are $\lambda$, its entries immediately above the diagonal are $1$, and every other entry is zero.''',
)

s.card(
    'jordan-chain-action',
    'lem-jordan-chain-description',
    r'''How does $T$ act on the ordered basis vectors of a Jordan block for $\lambda$?''',
    r'''It satisfies $Tb_1=\lambda b_1$ and $Tb_j=\lambda b_j+b_{j-1}$ for $j\ge2$.''',
)

s.card(
    'nilpotent-invariant-complement',
    'lem-nilpotent-invariant-complement',
    r'''What is the key complement construction for a longest nilpotent chain?''',
    r'''Choose $\varphi$ with $\varphi(N^{m-1}u)=1$, then take $W=\{v:\varphi(N^kv)=0\text{ for }0\le k<m\}$. This subspace is invariant and complements the chain span.''',
)

s.card(
    'complex-jordan-form',
    'thm-jordan-form',
    r'''How does the generalized eigenspace decomposition reduce complex Jordan form to the nilpotent case?''',
    r'''On $G(\lambda,T)$, the operator $(T-\lambda I)|_{G(\lambda,T)}$ is nilpotent. Its Jordan blocks become blocks for $T$ after adding $\lambda$ to their diagonal entries; concatenate the bases of the summands.''',
)

s.write()