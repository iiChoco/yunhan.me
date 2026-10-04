from common import Section

s = Section('7e')

s.p(
    'intro-singular-values',
    'Singular values and orthonormal coordinates',
    r'''Throughout this section, $V$ and $W$ are finite-dimensional inner product spaces over $\F$. Singular values describe a linear map using a positive operator on its domain. The resulting decomposition uses separate orthonormal lists in the domain and codomain and also gives formulas for the adjoint and pseudoinverse.''',
    270,
)

s.r(
    'thm-adjoint-product-positive',
    'The positive operator associated with a linear map',
    r'''Let $T\in\Lin(V,W)$. Then:
\begin{enumerate}
\item $T^*T$ is positive.
\item $\Null(T^*T)=\Null T$.
\item $\Range(T^*T)=\Range T^*=(\Null T)^\perp$.
\item $\dim\Range T=\dim\Range T^*=\dim\Range(T^*T)$.
\end{enumerate}''',
    r'''The adjoint rules give
\[
(T^*T)^*=T^*(T^*)^*=T^*T.
\]
Moreover, applying the adjoint identity to $T^*$ gives
\[
\ip{T^*Tv}{v}=\ip{Tv}{Tv}=\norm{Tv}^2\ge0.
\]
Thus $T^*T$ is self-adjoint with nonnegative quadratic values, proving positivity.

If $T^*Tv=0$, the displayed norm identity yields $\norm{Tv}^2=0$, hence $Tv=0$. Conversely, $Tv=0$ implies $T^*Tv=T^*0=0$. Therefore the two null spaces agree.

For a self-adjoint operator $A$, the adjoint range identities give $\Range A=(\Null A)^\perp$. Apply this to $A=T^*T$ and then use the null-space equality:
\[
\Range(T^*T)=(\Null(T^*T))^\perp
=(\Null T)^\perp=\Range T^*.
\]
Finally, the orthogonal-complement dimension formula and rank-nullity give
\[
\dim\Range T^*=\dim V-\dim\Null T=\dim\Range T.
\]
The range equality already proved supplies the remaining dimension equality. These arguments also apply when either space has dimension zero.''',
    2,
    20,
    [
        r'''Express $\ip{T^*Tv}{v}$ as a squared norm.''',
        r'''Use the adjoint range identities after identifying the null spaces.''',
    ],
    [
        'def-positive',
        'def-adjoint',
        'thm-adjoint-properties',
        'thm-adjoint-range-null',
        'c6-thm-norm-properties',
        'c6-thm-orthogonal-dimension',
        'c3-thm-rank-nullity',
        'c3-thm-linear-zero',
    ],
    '7.64',
    270,
)

s.d(
    'def-singular-values',
    'Singular values',
    r'''For $T\in\Lin(V,W)$, its singular values are the nonnegative square roots of the eigenvalues of $T^*T$, arranged in nonincreasing order. The square root of an eigenvalue is repeated as many times as the dimension of that eigenvalue's eigenspace. For a zero-dimensional domain, the list is empty.''',
    '7.65',
    271,
)

s.r(
    'lem-singular-eigenbasis',
    'An eigenbasis indexed by the singular-value list',
    r'''If $n=\dim V$ and $T\in\Lin(V,W)$, its singular-value list has exactly $n$ entries. Writing this list as $s_1\ge\cdots\ge s_n\ge0$, there is an orthonormal basis $e_1,\ldots,e_n$ of $V$ satisfying
\[
T^*Te_j=s_j^2e_j\qquad(1\le j\le n).
\]''',
    r'''The operator $A=T^*T$ is positive, so the positivity characterization gives an orthonormal basis $b_1,\ldots,b_n$ with $Ab_j=\lambda_jb_j$ and $\lambda_j\ge0$.

For a scalar $\lambda$, write $v=\sum_j a_jb_j$. The equation $Av=\lambda v$ is equivalent, by independence of the basis, to
\[
(\lambda_j-\lambda)a_j=0\qquad\text{for every }j.
\]
Thus the eigenspace for $\lambda$ is exactly the span of those $b_j$ whose eigenvalue equals $\lambda$. If there are no such indices, that eigenspace is $\{0\}$ and $\lambda$ is not an eigenvalue. If there are such indices, their basis vectors form a basis of the eigenspace, so its dimension equals the number of these indices.

Consequently the multiplicities in the definition of singular values count exactly the $n$ basis vectors. Reorder the basis so that $\sqrt{\lambda_j}$ is nonincreasing and call the reordered vectors $e_j$ and square roots $s_j$. Then $Ae_j=s_j^2e_j$. For $n=0$, the empty basis and empty list satisfy every assertion.''',
    2,
    20,
    [
        r'''Diagonalize the positive operator $T^*T$.''',
        r'''In a diagonal basis, determine exactly which coordinates an eigenvector may have.''',
    ],
    [
        'def-singular-values',
        'thm-adjoint-product-positive',
        'thm-positive-characterizations',
        'c2-thm-basis-coordinates',
        'c2-def-dimension',
        'c5-def-eigenspace',
    ],
    page=271,
    kind='lemma',
)

s.r(
    'ex-singular-values-shift',
    'Singular values reveal a coefficient absent from the eigenvalues',
    r'''On $\F^4$ with its standard inner product, define
\[
T(z_1,z_2,z_3,z_4)=(0,3z_1,2z_2,-3z_4).
\]
Its singular values are $3,3,2,0$, whereas its only eigenvalues are $-3$ and $0$.''',
    r'''The coordinate formula defines a linear map. If $z,w\in\F^4$, then
\[
\ip{Tz}{w}
=3z_1\overline{w_2}+2z_2\overline{w_3}-3z_4\overline{w_4}
=\ip{z}{(3w_2,2w_3,0,-3w_4)}.
\]
The defining uniqueness of the adjoint therefore gives
\[
T^*w=(3w_2,2w_3,0,-3w_4),
\qquad
T^*Tz=(9z_1,4z_2,0,9z_4).
\]
Writing $u_1,\ldots,u_4$ for the standard basis, the eigenspaces of $T^*T$ are
\[
E(9,T^*T)=\Span(u_1,u_4),\quad
E(4,T^*T)=\Span(u_2),\quad
E(0,T^*T)=\Span(u_3).
\]
Indeed, the equation $T^*Tz=\lambda z$ requires
$(9-\lambda)z_1=(4-\lambda)z_2=-\lambda z_3=(9-\lambda)z_4=0$.
This both verifies the displayed eigenspaces and excludes every other eigenvalue. Their dimensions are $2,1,1$, giving singular values $3,3,2,0$.

For the eigenvalues of $T$ itself, the equations are
\[
0=\lambda z_1,\qquad 3z_1=\lambda z_2,\qquad
2z_2=\lambda z_3,\qquad -3z_4=\lambda z_4.
\]
If $\lambda$ is neither $0$ nor $-3$, the first three equations successively give $z_1=z_2=z_3=0$, and the last gives $z_4=0$. Such a scalar is not an eigenvalue. The nonzero vectors $u_3$ and $u_4$ satisfy $Tu_3=0$ and $Tu_4=-3u_4$, so both $0$ and $-3$ are eigenvalues.''',
    2,
    20,
    [
        r'''First compute the adjoint from the standard inner product.''',
        r'''Compute the eigenvalues of $T^*T$ and $T$ separately.''',
    ],
    [
        'def-singular-values',
        'def-adjoint',
        'lem-adjoint-existence',
        'c6-thm-standard-inner-product',
        'c3-thm-coordinate-linear-maps',
        'c5-def-eigenvalue',
        'c5-def-eigenspace',
        'c2-def-dimension',
    ],
    '7.66',
    271,
    'example',
)

s.r(
    'ex-singular-values-rectangular',
    'Four singular values for a map into three-dimensional space',
    r'''Give $\F^4$ and $\F^3$ their standard inner products. For
\[
T(x_1,x_2,x_3,x_4)=(-5x_4,0,x_1+x_2),
\]
the singular values are $5,\sqrt2,0,0$.''',
    r'''For $x\in\F^4$ and $y\in\F^3$,
\[
\ip{Tx}{y}
=-5x_4\overline{y_1}+(x_1+x_2)\overline{y_3}
=\ip{x}{(y_3,y_3,0,-5y_1)}.
\]
Hence
\[
T^*y=(y_3,y_3,0,-5y_1),\qquad
T^*Tx=(x_1+x_2,x_1+x_2,0,25x_4).
\]
Let $u_1,\ldots,u_4$ be the standard basis of $\F^4$. The vectors
\[
b_1=u_4,\qquad
b_2=\frac{u_1+u_2}{\sqrt2},\qquad
b_3=\frac{u_1-u_2}{\sqrt2},\qquad
b_4=u_3
\]
are orthonormal by direct inner-product computation. They span because
\[
u_1=\frac{b_2+b_3}{\sqrt2},\qquad
u_2=\frac{b_2-b_3}{\sqrt2},\qquad
u_3=b_4,\qquad u_4=b_1.
\]
Their eigenvalues for $T^*T$ are respectively $25,2,0,0$, as substitution into its formula verifies. In this basis, the eigenvector equation forces coordinates to vanish unless their displayed eigenvalue matches the proposed eigenvalue. Thus the eigenspace dimensions are $1,1,2$ for $25,2,0$, respectively, and there are no other eigenvalues. Taking nonnegative square roots with these multiplicities gives the claimed list.''',
    2,
    20,
    [
        r'''Separate the fourth coordinate from the first two coordinates.''',
        r'''Use the sum and difference of the first two standard basis vectors.''',
    ],
    [
        'def-singular-values',
        'def-adjoint',
        'lem-adjoint-existence',
        'c6-thm-standard-inner-product',
        'c6-thm-orthonormal-independent',
        'c3-thm-coordinate-linear-maps',
        'c2-thm-basis-coordinates',
        'c5-def-eigenspace',
    ],
    '7.67',
    271,
    'example',
)

s.r(
    'thm-singular-rank',
    'Positive singular values count the range dimension',
    r'''For $T\in\Lin(V,W)$, let $r$ be the number of positive entries in its singular-value list, counting repetitions. Then
\[
r=\dim\Range T,
\qquad
\#\{\text{zero entries}\}=\dim\Null T.
\]
Consequently, $T$ is injective exactly when its list contains no zero, and $T$ is surjective exactly when $r=\dim W$.''',
    r'''Choose the orthonormal eigenbasis from the singular-value eigenbasis lemma and write $v=\sum_j a_je_j$. Then
\[
T^*Tv=\sum_j s_j^2a_je_j.
\]
Basis independence shows that this vector is zero exactly when $a_j=0$ at every index with $s_j>0$. Therefore the basis vectors associated with zero singular values form a basis of $\Null(T^*T)$. Since $\Null(T^*T)=\Null T$, the number of zero entries is $\dim\Null T$.

The whole list has $\dim V$ entries, so rank-nullity gives
\[
r=\dim V-\dim\Null T=\dim\Range T.
\]
Injectivity is equivalent to $\Null T=\{0\}$, which is equivalent to its dimension being zero and hence to having no zero entries. Finally, $\Range T$ is a subspace of $W$. It equals $W$ exactly when its dimension equals $\dim W$, by the full-dimension subspace theorem. This proves the surjectivity criterion. Empty lists and zero-dimensional spaces satisfy the same dimension identities.''',
    2,
    20,
    [
        r'''Identify the kernel of $T^*T$ in an orthonormal eigenbasis.''',
        r'''Count its basis vectors and apply rank-nullity.''',
    ],
    [
        'lem-singular-eigenbasis',
        'thm-adjoint-product-positive',
        'c2-thm-basis-coordinates',
        'c2-def-dimension',
        'c2-lem-zero-dimension',
        'c2-thm-full-dimension-equality',
        'c3-thm-rank-nullity',
        'c3-thm-injective-null',
        'c3-thm-range-subspace',
        'c3-def-surjective',
    ],
    '7.68',
    272,
)

s.r(
    'thm-isometry-singular-values',
    'Isometries have precisely unit singular values',
    r'''A map $T\in\Lin(V,W)$ is an isometry if and only if every singular value of $T$ equals $1$. The statement includes an empty singular-value list when $V=\{0\}$.''',
    r'''The isometry equivalences say that $T$ is an isometry exactly when $T^*T=I_V$. If this identity holds, every vector in an orthonormal basis of $V$ is an eigenvector with eigenvalue $1$. Thus every singular value is $1$.

Conversely, suppose every singular value is $1$. In the orthonormal eigenbasis indexed by the singular-value list, $T^*Te_j=e_j$ at every index. The two linear maps $T^*T$ and $I_V$ therefore agree on a basis, so they agree on all of $V$. The isometry criterion now applies. If $V=\{0\}$, both maps on $V$ are the unique zero map, the basis is empty, and the same argument proves the vacuous-list case.''',
    1,
    10,
    [
        r'''Use the criterion $T^*T=I_V$.''',
    ],
    [
        'thm-isometry-equivalences',
        'lem-singular-eigenbasis',
        'def-singular-values',
        'c3-thm-linear-map-basis',
    ],
    '7.69',
    272,
)

s.r(
    'thm-singular-value-decomposition',
    'Singular value decomposition',
    r'''Let $T\in\Lin(V,W)$, and let
\[
s_1\ge\cdots\ge s_r>0
\]
be its positive singular values, including repetitions. There are orthonormal lists $e_1,\ldots,e_r$ in $V$ and $f_1,\ldots,f_r$ in $W$ such that
\[
Tv=\sum_{j=1}^r s_j\ip{v}{e_j}f_j
\qquad\text{for every }v\in V.
\]
When $r=0$, both lists and the sum are empty, and $T=0$.''',
    r'''Put $n=\dim V$. Choose the orthonormal eigenbasis $e_1,\ldots,e_n$ with
\[
T^*Te_j=s_j^2e_j,
\]
where $s_1,\ldots,s_n$ is the full singular-value list. Its positive entries occupy the first $r$ indices. For $1\le j\le r$, define
\[
f_j=\frac{Te_j}{s_j}.
\]
The denominators are positive real numbers. For $j,k\le r$, the adjoint identity and the scalar rules for the inner product give
\[
\ip{f_j}{f_k}
=\frac{\ip{Te_j}{Te_k}}{s_js_k}
=\frac{\ip{e_j}{T^*Te_k}}{s_js_k}
=\frac{s_k}{s_j}\ip{e_j}{e_k}.
\]
This equals $0$ for $j\ne k$ and $1$ for $j=k$, proving that the $f_j$ form an orthonormal list.

If $j>r$, then $T^*Te_j=0$. Equality of the null spaces of $T^*T$ and $T$ gives $Te_j=0$. For any $v$, its orthonormal expansion is
\[
v=\sum_{j=1}^n\ip{v}{e_j}e_j.
\]
Applying $T$, using the vanishing images for $j>r$, and substituting $Te_j=s_jf_j$ at the remaining indices gives the asserted formula. If $r=0$, all basis vectors are killed, so this formula states $Tv=0$ for every $v$. If $n=0$, the same conclusion follows from the empty expansion.''',
    3,
    45,
    [
        r'''Start with an orthonormal eigenbasis of $T^*T$.''',
        r'''Normalize $Te_j$ using the corresponding positive singular value.''',
        r'''Treat the zero singular values through the equality of null spaces.''',
    ],
    [
        'lem-singular-eigenbasis',
        'thm-adjoint-product-positive',
        'def-adjoint',
        'c6-def-orthonormal',
        'c6-thm-inner-product-properties',
        'c6-thm-orthonormal-coordinates',
        'c3-def-linear-map',
    ],
    '7.70',
    273,
)

s.r(
    'lem-svd-subspaces',
    'The subspaces represented by singular vectors',
    r'''Suppose a singular value decomposition is written
\[
Tv=\sum_{j=1}^r s_j\ip{v}{e_j}f_j,
\qquad s_j>0.
\]
Then $e_1,\ldots,e_r$ is an orthonormal basis of $(\Null T)^\perp$, and $f_1,\ldots,f_r$ is an orthonormal basis of $\Range T$. Moreover,
\[
Te_j=s_jf_j,\qquad
\Null T=\bigl(\Span(e_1,\ldots,e_r)\bigr)^\perp.
\]''',
    r'''Substituting $v=e_k$ into the decomposition and using orthonormality gives $Te_k=s_kf_k$. The decomposition puts every $Tv$ in $\Span(f_1,\ldots,f_r)$, and $f_k=T(e_k/s_k)$ puts every $f_k$ in $\Range T$. Thus this span equals $\Range T$. The list is orthonormal and therefore independent, so it is a basis of that range.

Let $E=\Span(e_1,\ldots,e_r)$. Independence of the $f_j$, together with $s_j>0$, shows that $Tv=0$ exactly when $\ip{v}{e_j}=0$ for all $j$. These equalities hold exactly when $v$ is orthogonal to every vector of $E$: one direction tests the generators, and the other follows by conjugate linearity in the second slot for any linear combination of them. Hence $\Null T=E^\perp$. Taking orthogonal complements and applying the double-complement theorem gives $(\Null T)^\perp=E$. The orthonormal list $e_1,\ldots,e_r$ is therefore a basis of that subspace.

When $r=0$, the decomposition says $T=0$, the two spans are $\{0\}$, and $\Null T=V$. The same complement identities prove all the assertions in this case.''',
    2,
    20,
    [
        r'''Evaluate the decomposition on its right singular vectors.''',
        r'''Use independence of the left singular vectors to characterize the kernel.''',
    ],
    [
        'thm-singular-value-decomposition',
        'c6-thm-orthonormal-independent',
        'c6-thm-inner-product-properties',
        'c6-def-orthogonal-complement',
        'c6-thm-double-orthogonal',
        'c2-thm-span-smallest',
        'c3-def-range',
        'c3-def-null-space',
    ],
    page=274,
    kind='lemma',
)

s.d(
    'def-rectangular-diagonal',
    'Diagonal rectangular matrices',
    r'''A matrix $A\in\F^{p,n}$ is diagonal if $A_{j,k}=0$ whenever $j\ne k$. Thus its only possibly nonzero entries are $A_{k,k}$ for $1\le k\le\min(p,n)$. Matrices with zero rows or zero columns satisfy this condition vacuously.''',
    '7.74',
    274,
)

s.r(
    'thm-svd-orthonormal-bases',
    'A rectangular diagonal matrix in orthonormal bases',
    r'''Let $T\in\Lin(V,W)$, with $n=\dim V$, $p=\dim W$, and positive singular values $s_1,\ldots,s_r$. There are orthonormal bases $\mathcal E=(e_1,\ldots,e_n)$ of $V$ and $\mathcal F=(f_1,\ldots,f_p)$ of $W$ for which
\[
\Mat(T,\mathcal E,\mathcal F)_{j,k}
=
\begin{cases}
s_k,&j=k\le r,\\
0,&\text{otherwise}.
\end{cases}
\]
In particular, this matrix is diagonal, even when it is rectangular.''',
    r'''Take the two orthonormal lists from a singular value decomposition. Extend each to an orthonormal basis of its ambient space. For $k\le r$, evaluating the decomposition at $e_k$ gives $Te_k=s_kf_k$. For $k>r$, orthonormality of the extended basis gives $\ip{e_k}{e_j}=0$ for all $j\le r$, so the decomposition gives $Te_k=0$.

The $k$th column of a representing matrix records the coordinates of $Te_k$ in the codomain basis. The two cases for $Te_k$ give exactly the displayed entry formula. Its nonzero entries can occur only at matching row and column indices. If either basis is empty, there are no entries requiring verification, and the same construction produces the corresponding empty matrix.''',
    2,
    15,
    [
        r'''Extend both singular-vector lists to orthonormal bases.''',
        r'''Compute the image of every vector in the extended domain basis.''',
    ],
    [
        'thm-singular-value-decomposition',
        'def-rectangular-diagonal',
        'c6-thm-orthonormal-extension',
        'c3-def-map-matrix',
    ],
    page=274,
    kind='corollary',
)

s.note(
    'note-svd-two-bases',
    'The two bases need not agree',
    r'''Even when $V=W$, the domain basis and codomain basis in this construction may be different. Thus obtaining this diagonal representing matrix does not assert that $T$ has a diagonal matrix using one common basis.''',
    274,
)

s.r(
    'thm-svd-adjoint-pseudoinverse',
    'Adjoint and pseudoinverse from a singular value decomposition',
    r'''Suppose
\[
Tv=\sum_{j=1}^r s_j\ip{v}{e_j}f_j
\]
is a singular value decomposition of $T\in\Lin(V,W)$ using its positive singular values. Then, for every $w\in W$,
\[
T^*w=\sum_{j=1}^r s_j\ip{w}{f_j}e_j,
\qquad
T^\dagger w=\sum_{j=1}^r \frac{\ip{w}{f_j}}{s_j}e_j.
\]
Both maps have domain $W$ and codomain $V$.''',
    r'''For $v\in V$ and $w\in W$, expansion of the decomposition gives
\[
\ip{Tv}{w}
=\sum_{j=1}^r s_j\ip{v}{e_j}\ip{f_j}{w}.
\]
Because $s_j$ is real and the inner product is conjugate linear in its second slot, conjugate symmetry gives
\[
\ip{v}{\sum_{j=1}^r s_j\ip{w}{f_j}e_j}
=\sum_{j=1}^r s_j\overline{\ip{w}{f_j}}\ip{v}{e_j}
=\sum_{j=1}^r s_j\ip{f_j}{w}\ip{v}{e_j}.
\]
The two expressions agree for every $v$. Uniqueness in the definition of the adjoint proves its formula.

Set
\[
x=\sum_{j=1}^r \frac{\ip{w}{f_j}}{s_j}e_j.
\]
The singular-vector subspace lemma puts $x$ in $(\Null T)^\perp$. That lemma also gives $Te_j=s_jf_j$, so
\[
Tx=\sum_{j=1}^r\ip{w}{f_j}f_j.
\]
The vectors $f_1,\ldots,f_r$ form an orthonormal basis of $\Range T$. The orthogonal-projection formula therefore identifies the last expression with $P_{\Range T}w$. By the definition of the pseudoinverse, $T^\dagger w$ is the unique vector in $(\Null T)^\perp$ whose image is $P_{\Range T}w$. Thus $x=T^\dagger w$.

For $r=0$, all displayed sums are zero; the same arguments show that both the adjoint and pseudoinverse are zero.''',
    3,
    30,
    [
        r'''Check the adjoint identity, keeping track of conjugation in the second slot.''',
        r'''For the pseudoinverse, identify the proposed vector's subspace and its image under $T$.''',
    ],
    [
        'thm-singular-value-decomposition',
        'lem-svd-subspaces',
        'def-adjoint',
        'lem-adjoint-existence',
        'c6-thm-inner-product-properties',
        'c6-thm-projection-properties',
        'c6-def-pseudoinverse',
        'c6-thm-kernel-complement-restriction',
    ],
    '7.75',
    275,
)

s.r(
    'thm-adjoint-pseudoinverse-singular-values',
    'Singular values of the adjoint and pseudoinverse',
    r'''Let $T:V\to W$ have positive singular values $s_1\ge\cdots\ge s_r>0$, and put $p=\dim W$. The singular-value list of $T^*$ consists of
\[
s_1,\ldots,s_r
\]
followed by $p-r$ zeros. The list for $T^\dagger$ consists of
\[
\frac1{s_r},\ldots,\frac1{s_1}
\]
followed by $p-r$ zeros. These descriptions include repetitions and the case $r=0$.''',
    r'''Choose a singular value decomposition of $T$, and extend $f_1,\ldots,f_r$ to an orthonormal basis $f_1,\ldots,f_p$ of $W$. The adjoint formula gives
\[
T^*f_j=s_je_j\quad(j\le r),\qquad
T^*f_j=0\quad(j>r).
\]
Since $Te_j=s_jf_j$ and $(T^*)^*=T$, it follows that
\[
(T^*)^*T^*f_j=TT^*f_j
=
\begin{cases}
s_j^2f_j,&j\le r,\\
0,&j>r.
\end{cases}
\]
This is an orthonormal eigenbasis for the operator defining the singular values of $T^*$.

Put $Q=T^\dagger$. Its established formula is
\[
Qw=\sum_{j=1}^r s_j^{-1}\ip{w}{f_j}e_j.
\]
For $w\in W$ and $v\in V$, the inner-product scalar rules give
\[
\ip{Qw}{v}
=\sum_{j=1}^r s_j^{-1}\ip{w}{f_j}\ip{e_j}{v}
=\ip{w}{\sum_{j=1}^r s_j^{-1}\ip{v}{e_j}f_j}.
\]
Thus
\[
Q^*v=\sum_{j=1}^r s_j^{-1}\ip{v}{e_j}f_j.
\]
Consequently $Q^*Qf_j=s_j^{-2}f_j$ for $j\le r$ and $Q^*Qf_j=0$ for $j>r$.

For each of the two diagonal operators just obtained, the coordinate eigenvector equation shows that the eigenspace for a diagonal value is spanned exactly by the basis vectors with that value. Hence the multiplicities are those of the displayed lists, including $p-r$ zero entries. Taking square roots gives the claimed positive values. Reciprocals reverse the nonincreasing ordering because every $s_j$ is positive. If $r=0$, both diagonal operators are zero on $W$, giving $p$ zero singular values.''',
    2,
    20,
    [
        r'''Extend the left singular vectors to an orthonormal basis of $W$.''',
        r'''Diagonalize $TT^*$ and $(T^\dagger)^*T^\dagger$ in that basis.''',
    ],
    [
        'thm-svd-adjoint-pseudoinverse',
        'lem-svd-subspaces',
        'def-singular-values',
        'thm-adjoint-properties',
        'def-adjoint',
        'lem-adjoint-existence',
        'c6-thm-orthonormal-extension',
        'c6-thm-inner-product-properties',
        'c2-thm-basis-coordinates',
    ],
    page=275,
    kind='corollary',
)

s.r(
    'ex-explicit-rectangular-svd',
    'A singular value decomposition and pseudoinverse in coordinates',
    r'''For
\[
T(x_1,x_2,x_3,x_4)=(-5x_4,0,x_1+x_2),
\]
set
\[
e_1=(0,0,0,1),\qquad
e_2=\frac1{\sqrt2}(1,1,0,0),\qquad
f_1=(-1,0,0),\qquad f_2=(0,0,1).
\]
Then
\[
Tx=5\ip{x}{e_1}f_1+\sqrt2\ip{x}{e_2}f_2
\]
is a singular value decomposition. For $y=(y_1,y_2,y_3)$,
\[
T^*y=(y_3,y_3,0,-5y_1),\qquad
T^\dagger y=\left(\frac{y_3}{2},\frac{y_3}{2},0,-\frac{y_1}{5}\right).
\]''',
    r'''The earlier rectangular example gives positive singular values $5,\sqrt2$. For the proposed right vectors, each squared norm is $1$ and their inner product is $0$, because their nonzero coordinates occur in disjoint positions. The same statements hold for the proposed left vectors. Thus both lists are orthonormal.

In the standard inner products,
\[
\ip{x}{e_1}=x_4,\qquad
\ip{x}{e_2}=\frac{x_1+x_2}{\sqrt2}.
\]
Substitution gives
\[
5\ip{x}{e_1}f_1+\sqrt2\ip{x}{e_2}f_2
=(-5x_4,0,x_1+x_2)=Tx,
\]
proving the asserted decomposition. Also
\[
\ip{y}{f_1}=-y_1,\qquad \ip{y}{f_2}=y_3.
\]
The adjoint formula therefore gives
\[
5(-y_1)e_1+\sqrt2y_3e_2=(y_3,y_3,0,-5y_1).
\]
The pseudoinverse formula gives
\[
-\frac{y_1}{5}e_1+\frac{y_3}{\sqrt2}e_2
=\left(\frac{y_3}{2},\frac{y_3}{2},0,-\frac{y_1}{5}\right),
\]
as required.''',
    2,
    20,
    [
        r'''Use the positive-eigenvalue eigenvectors from the earlier rectangular example.''',
        r'''Normalize their images under $T$, then apply the adjoint and pseudoinverse formulas.''',
    ],
    [
        'ex-singular-values-rectangular',
        'thm-singular-value-decomposition',
        'thm-svd-adjoint-pseudoinverse',
        'c6-thm-standard-inner-product',
        'c6-def-orthonormal',
    ],
    '7.79',
    276,
    'example',
)

s.r(
    'thm-svd-matrix',
    'Reduced and full matrix singular value decompositions',
    r'''Let $A\in\F^{p,n}$ have rank $r\ge0$, and let $s_1\ge\cdots\ge s_r>0$ be the positive singular values of the map $x\mapsto Ax$ between standard inner product spaces.
\begin{enumerate}
\item There are matrices $B\in\F^{p,r}$ and $C\in\F^{n,r}$ with orthonormal columns and a matrix
\[
D=\operatorname{diag}(s_1,\ldots,s_r)\in\F^{r,r}
\]
such that
\[
A=BDC^*.
\]
\item There are unitary matrices $U\in\F^{p,p}$ and $Z\in\F^{n,n}$ such that
\[
A=U\Sigma Z^*,
\]
where $\Sigma\in\F^{p,n}$ has entries
\[
\Sigma_{j,k}=
\begin{cases}
s_k,&j=k\le r,\\
0,&\text{otherwise}.
\end{cases}
\]
\end{enumerate}
For $r=0$, the reduced factors have zero columns, $D$ is the empty square matrix, and the reduced product is the zero $p$-by-$n$ matrix. The full factorization also permits $p=0$ or $n=0$.''',
    r'''Let $T:\F^n\to\F^p$ be the linear map whose standard matrix is $A$. Its range dimension is the rank of $A$, namely $r$. The singular-rank theorem therefore gives exactly $r$ positive singular values. Choose a singular value decomposition
\[
Tx=\sum_{\ell=1}^r s_\ell\ip{x}{e_\ell}f_\ell.
\]
Define $B$ to have columns $f_1,\ldots,f_r$ and $C$ to have columns $e_1,\ldots,e_r$, and define $D$ as in the statement. Their column lists are orthonormal by construction.

For a row index $j$ and column index $k$, matrix multiplication and the definition of conjugate transpose give
\[
(BDC^*)_{j,k}
=\sum_{\ell=1}^r (f_\ell)_j s_\ell\overline{(e_\ell)_k}.
\]
Let $u_k$ be the $k$th standard basis vector in $\F^n$. Then $\ip{u_k}{e_\ell}=\overline{(e_\ell)_k}$. Applying the decomposition to $u_k$ shows that the preceding sum is the $j$th coordinate of $Tu_k$, which is $A_{j,k}$. Thus $A=BDC^*$.

For the full version, extend $f_1,\ldots,f_r$ to an orthonormal basis $f_1,\ldots,f_p$ of $\F^p$, and extend $e_1,\ldots,e_r$ to an orthonormal basis $e_1,\ldots,e_n$ of $\F^n$. Let $U$ and $Z$ have these respective full lists as columns. A square matrix with orthonormal columns is unitary, so both matrices are unitary. Define $\Sigma$ by the stated entry formula. Its zero entries reduce the product to
\[
(U\Sigma Z^*)_{j,k}
=\sum_{\ell=1}^r (f_\ell)_j s_\ell\overline{(e_\ell)_k}
=A_{j,k}.
\]
This proves the full factorization.

If $r=0$, the range of $T$ has dimension zero, so it equals $\{0\}$ and $T=0$. Hence $A=0$, and every entry of the reduced product is an empty sum, also zero. The full construction then uses arbitrary orthonormal bases and $\Sigma=0$. If $p=0$ or $n=0$, the appropriate bases and square matrices are empty; orthonormality and the entry equalities remain valid. Thus these cases are included.''',
    3,
    35,
    [
        r'''Apply the operator decomposition to the map with standard matrix $A$.''',
        r'''Put the left and right singular vectors into columns and compare matrix entries.''',
        r'''Extend both column lists to obtain the full factorization.''',
    ],
    [
        'thm-singular-rank',
        'thm-singular-value-decomposition',
        'def-rectangular-diagonal',
        'def-conjugate-transpose',
        'def-unitary-matrix',
        'thm-unitary-matrix-equivalences',
        'c3-thm-coordinate-linear-maps',
        'c3-def-map-matrix',
        'c3-thm-range-matrix-rank',
        'c3-def-matrix-product',
        'c6-thm-standard-inner-product',
        'c6-thm-orthonormal-extension',
        'c2-lem-zero-dimension',
    ],
    '7.80',
    277,
)

s.card(
    'singular-values-definition',
    'def-singular-values',
    r'''How are the singular values of $T:V\to W$ defined, including their ordering and repetitions?''',
    r'''They are the nonnegative square roots of the eigenvalues of $T^*T$, listed in nonincreasing order, with each repeated according to the dimension of the corresponding eigenspace.''',
)

s.card(
    'singular-list-length',
    'lem-singular-eigenbasis',
    r'''How many singular values does $T:V\to W$ have when zeros are included?''',
    r'''Exactly $\dim V$. A positive operator $T^*T$ has an orthonormal eigenbasis, and its eigenspace dimensions account for every basis vector.''',
)

s.card(
    'singular-rank',
    'thm-singular-rank',
    r'''What do the positive and zero singular-value counts measure?''',
    r'''The positive count is $\dim\Range T$, and the zero count is $\dim\Null T$. Repetitions count in both statements.''',
)

s.card(
    'singular-isometry',
    'thm-isometry-singular-values',
    r'''What singular-value condition characterizes an isometry?''',
    r'''Every singular value equals $1$. This includes the empty list when the domain is $\{0\}$.''',
)

s.card(
    'svd-construction',
    'thm-singular-value-decomposition',
    r'''Starting with $T^*Te_j=s_j^2e_j$ and $s_j>0$, how is the corresponding left singular vector constructed?''',
    r'''Set $f_j=Te_j/s_j$. The adjoint identity proves that these normalized images form an orthonormal list.''',
)

s.card(
    'svd-subspaces',
    'lem-svd-subspaces',
    r'''Which subspaces have the positive right and left singular vectors as orthonormal bases?''',
    r'''The right vectors form an orthonormal basis of $(\Null T)^\perp$; the left vectors form an orthonormal basis of $\Range T$.''',
)

s.card(
    'svd-adjoint',
    'thm-svd-adjoint-pseudoinverse',
    r'''If $Tv=\sum_{j=1}^r s_j\ip{v}{e_j}f_j$, what is $T^*w$?''',
    r'''$\displaystyle T^*w=\sum_{j=1}^r s_j\ip{w}{f_j}e_j$.''',
)

s.card(
    'svd-pseudoinverse',
    'thm-svd-adjoint-pseudoinverse',
    r'''How does a singular value decomposition give the pseudoinverse?''',
    r'''Exchange the right and left singular vectors and reciprocate the positive coefficients:
$\displaystyle T^\dagger w=\sum_{j=1}^r s_j^{-1}\ip{w}{f_j}e_j$.''',
)

s.card(
    'adjoint-singular-zero-count',
    'thm-adjoint-pseudoinverse-singular-values',
    r'''If $T:V\to W$ has $r$ positive singular values, how many zero singular values does $T^*$ have?''',
    r'''It has $\dim W-r$ zero singular values. Its positive singular values agree with those of $T$, including repetitions.''',
)

s.card(
    'matrix-svd',
    'thm-svd-matrix',
    r'''State the reduced matrix SVD for a $p$-by-$n$ matrix of rank $r$.''',
    r'''$\displaystyle A=BDC^*$, where $B$ is $p$-by-$r$ and $C$ is $n$-by-$r$, both have orthonormal columns, and $D$ is $r$-by-$r$ diagonal with the positive singular values on its diagonal.''',
)

s.write()