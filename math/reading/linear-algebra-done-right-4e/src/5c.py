from common import Section

s = Section('5c')

s.p('intro-upper-triangular', 'Invariant subspaces and triangular matrices', r'''A matrix representation becomes more useful when its entries have a predictable pattern. Upper-triangular matrices encode a sequence of invariant subspaces, and their diagonal entries reveal the eigenvalues. We will characterize exactly when an operator admits such a representation.''', 154)

s.d('def-operator-matrix', 'The matrix of an operator in one basis', r'''For an operator $T\in\Lin(V)$ and a basis $\mathcal B=(v_1,\ldots,v_n)$, write $\Mat(T,\mathcal B)$ for the matrix using $\mathcal B$ in both the domain and target. Its entries satisfy
\[Tv_k=\sum_{j=1}^n A_{jk}v_j.\]
Thus it is square, and its $k$th column records the coefficients of $Tv_k$. On $\F^n$, an unspecified basis means the standard coordinate basis. The zero-dimensional space has the empty $0$-by-$0$ operator matrix.''', '5.35', 154)

s.r('ex-triangular-coordinate-matrix', 'A coordinate operator with a triangular matrix', r'''For
\[T(x,y,z)=(2x+y,5y+3z,8z)\quad\text{on }\F^3,\]
prove that $T$ is linear and its standard matrix is
\[\begin{pmatrix}2&1&0\\0&5&3\\0&0&8\end{pmatrix}.\]''',
r'''Each output coordinate is a fixed scalar combination of the input coordinates, so the coordinate characterization of linear maps proves linearity. The standard basis vectors have images
\[Te_1=(2,0,0),\qquad Te_2=(1,5,0),\qquad Te_3=(0,3,8).\]
Placing their coordinate lists in successive columns gives the displayed matrix.''',
1, 10, [r'Apply the operator to each standard basis vector.'],
['def-operator-matrix', 'c3-thm-coordinate-linear-maps', 'c3-def-map-matrix'], '5.36', 154, 'example')

s.r('ex-eigenvector-first-column', 'Starting a basis with an eigenvector', r'''If $V$ is a nonzero finite-dimensional complex vector space and $T\in\Lin(V)$, there is a basis in which the first column of the matrix of $T$ has the form $(\lambda,0,\ldots,0)$ for some $\lambda\in\C$.''',
r'''The complex eigenvalue theorem supplies an eigenvalue $\lambda$ and a nonzero vector $v_1$ with $Tv_1=\lambda v_1$. The one-vector list $v_1$ is independent, so it extends to a basis $v_1,\ldots,v_n$ of $V$. In this basis, the coefficients of $Tv_1$ are $\lambda$ in position one and zero in all other positions. These coefficients form the first matrix column.''',
1, 10, [r'Extend an eigenvector to a basis.'],
['thm-complex-eigenvalue', 'def-eigenvector', 'c2-ex-single-independent', 'c2-thm-extend-independent', 'def-operator-matrix'], page=155, kind='example')

s.d('def-matrix-diagonal', 'The diagonal of a square matrix', r'''The diagonal entries of $A\in\F^{n,n}$ are $A_{11},A_{22},\ldots,A_{nn}$, in that order. The diagonal list is empty when $n=0$.''', '5.37', 155)

s.d('def-upper-triangular', 'Upper-triangular matrices', r'''A square matrix $A$ is upper triangular if $A_{jk}=0$ whenever $j>k$. Thus every entry strictly below its diagonal vanishes. The empty square matrix is upper triangular.''', '5.38', 155)

s.r('thm-triangular-invariant', 'Triangularity and invariant initial spans', r'''Suppose $T\in\Lin(V)$ and $v_1,\ldots,v_n$ is a basis. For $0\le k\le n$, put $V_k=\Span(v_1,\ldots,v_k)$, so $V_0=\{0\}$. The following are equivalent:
\begin{enumerate}
\item The matrix of $T$ in this basis is upper triangular.
\item Each $V_k$ is invariant under $T$.
\item $Tv_k\in V_k$ for every $1\le k\le n$.
\end{enumerate}''',
r'''If the matrix is upper triangular, the coefficients of $Tv_j$ at positions larger than $j$ vanish, so $Tv_j\in V_j$. For $j\le k$, this implies $Tv_j\in V_k$. If $u=\sum_{j=1}^k a_jv_j\in V_k$, linearity gives $Tu=\sum_{j=1}^k a_jTv_j\in V_k$. Also $T0=0$, so $V_0$ is invariant. Thus the first condition implies the second.
If each $V_k$ is invariant, then $v_k\in V_k$ gives $Tv_k\in V_k$, proving the third condition.
Finally, if $Tv_k\in V_k$, it has an expansion using only $v_1,\ldots,v_k$. Uniqueness of its expansion in the full basis forces every coefficient at a position $j>k$ to vanish. These coefficients are exactly the entries below the diagonal in column $k$. Hence the matrix is upper triangular. When $n=0$, all indexed conditions are vacuous, $V=V_0=\{0\}$ is invariant, and the empty matrix satisfies the definition.''',
2, 20, [r'Translate a zero matrix entry into the absence of a basis vector from an image expansion.'],
['def-operator-matrix', 'def-upper-triangular', 'def-invariant', 'c2-def-span', 'c2-thm-basis-coordinates', 'c3-def-linear-map', 'c3-thm-linear-zero'], '5.39', 156)

s.r('thm-triangular-diagonal-product', 'A triangular operator satisfies its diagonal product', r'''Suppose $T$ has an upper-triangular matrix in a basis of length $n$, with diagonal entries $\lambda_1,\ldots,\lambda_n$. Then
\[(T-\lambda_1I)(T-\lambda_2I)\cdots(T-\lambda_nI)=0.\]
For $n=0$, the empty operator product means $I$; on the zero space, $I=0$.''',
r'''Let $v_1,\ldots,v_n$ be the basis and put $V_k=\Span(v_1,\ldots,v_k)$. For $k\ge1$, the triangular matrix gives
\[(T-\lambda_kI)v_k\in V_{k-1},\]
because subtracting $\lambda_kv_k$ removes the diagonal coefficient. For $j<k$, both $Tv_j$ and $\lambda_kv_j$ belong to $V_{k-1}$. Thus linearity gives
\[(T-\lambda_kI)V_k\subseteq V_{k-1}.\]
Apply the product in the stated order, remembering that the rightmost factor acts first. It sends $V_n$ first into $V_{n-1}$, then into $V_{n-2}$, and so on, finally into $V_0=\{0\}$. Therefore it is the zero operator on $V=V_n$. If $n=0$, every vector of $V$ is zero, so the identity and zero operators agree, proving the empty-product case.''',
2, 20, [r'Show that the factor associated with the $k$th diagonal entry sends the $k$th initial span into the preceding one.'],
['thm-triangular-invariant', 'def-operator-matrix', 'c3-def-map-composition', 'c3-def-map-operations', 'c3-def-zero-identity-maps'], '5.40', 156)

s.r('thm-triangular-invertible', 'Invertibility of a triangular operator', r'''An operator with an upper-triangular matrix is invertible if and only if every diagonal entry is nonzero. In dimension zero this condition is vacuous, and the unique operator is invertible.''',
r'''Write the diagonal entries as $\lambda_1,\ldots,\lambda_n$. Suppose they are all nonzero, and let $v=\sum_{j=1}^n b_jv_j$ be a nonzero vector. Choose the largest index $k$ with $b_k\ne0$. In the expansion of $Tv$, terms with index $j<k$ have no $v_k$ coefficient by triangularity, and terms with index $j>k$ have coefficient $b_j=0$. Thus the coefficient of $v_k$ in $Tv$ is $\lambda_kb_k\ne0$. Hence $Tv\ne0$, proving that the null space is $\{0\}$. The injectivity criterion and finite-dimensional equivalence make $T$ invertible.
Conversely, suppose $\lambda_k=0$ for some $k$. The triangular matrix sends $V_k=\Span(v_1,\ldots,v_k)$ into $V_{k-1}$: earlier basis images lie in $V_{k-1}$, and the zero diagonal coefficient puts $Tv_k$ there too. Consider this restriction as a map from $V_k$ to $V_{k-1}$. These spaces have dimensions $k$ and $k-1$. Its range has dimension at most $k-1$, so rank-nullity gives a null space of dimension at least one. It therefore has a nonzero vector killed by $T$, and $T$ is not injective or invertible. In dimension zero the unique operator is both identity and zero and is its own inverse.''',
2, 20, [r'For a nonzero input, inspect its last nonzero basis coefficient.', r'If a diagonal entry vanishes, compare two consecutive initial spans.'],
['thm-triangular-invariant', 'def-operator-matrix', 'c3-thm-injective-null', 'c3-thm-equal-dimension-invertibility', 'c3-thm-rank-nullity', 'c2-thm-subspace-dimension', 'c2-lem-independent-sublist', 'c2-def-basis', 'c2-def-dimension', 'c2-lem-zero-dimension', 'c1-lem-scalar-cancellation'], page=157)

s.r('thm-triangular-eigenvalues', 'The diagonal lists all eigenvalues', r'''If an operator has an upper-triangular matrix, its eigenvalues are exactly the scalar values appearing on that matrix's diagonal. The diagonal may contain repetitions, whereas the assertion about eigenvalues concerns their distinct values.''',
r'''Let the diagonal entries be $\lambda_1,\ldots,\lambda_n$. For any scalar $\mu$, the matrix of $T-\mu I$ is upper triangular with diagonal entries $\lambda_1-\mu,\ldots,\lambda_n-\mu$, by the matrix rules for linear combinations and the matrix of the identity. The triangular invertibility criterion says that $T-\mu I$ fails to be invertible exactly when one of these entries is zero, or equivalently when $\mu=\lambda_k$ for some $k$. The eigenvalue test says this failure of invertibility is exactly the condition that $\mu$ be an eigenvalue. When $n=0$, the diagonal is empty, every $T-\mu I$ is the invertible operator on the zero space, and there are no eigenvalues.''',
1, 10, [r'Apply the triangular invertibility test to $T-\mu I$.'],
['thm-triangular-invertible', 'thm-eigenvalue-tests', 'c3-thm-matrix-addition', 'c3-thm-matrix-scaling', 'c3-lem-identity-matrix-laws'], '5.41', 157)

s.r('ex-triangular-eigenvalues', 'Reading eigenvalues from a coordinate example', r'''For $T(x,y,z)=(2x+y,5y+3z,8z)$ on $\F^3$, the eigenvalues are exactly $2,5,8$.''',
r'''The earlier coordinate computation gives the upper-triangular standard matrix with diagonal entries $2,5,8$. The diagonal-eigenvalue theorem therefore gives precisely those three scalars as the eigenvalues, with no others.''',
1, 10, [r'Use the previously computed matrix.'],
['ex-triangular-coordinate-matrix', 'thm-triangular-eigenvalues'], '5.42', 158, 'example')

s.r('ex-field-dependent-triangularization', 'The scalar field can determine whether triangularization is possible', r'''Define $T$ on $\F^4$ by
\[T(z_1,z_2,z_3,z_4)=(-z_2,z_1,2z_1+3z_3,z_3+3z_4).\]
Its minimal polynomial is
\[p(z)=(z^2+1)(z-3)^2=z^4-6z^3+10z^2-6z+9.\]
Over $\R$, no basis gives an upper-triangular matrix for $T$. Over $\C$, the ordered list
\[
\begin{aligned}
u_1&=(4-3i,-3-4i,-3+i,1),\\
u_2&=(4+3i,-3+4i,-3-i,1),\\
u_3&=(0,0,0,1),\\
u_4&=(0,0,1,0)
\end{aligned}
\]
is a basis and gives the matrix
\[\begin{pmatrix}i&0&0&0\\0&-i&0&0\\0&0&3&1\\0&0&0&3\end{pmatrix}.\]''',
r'''The coordinate characterization proves that $T$ is linear. Let $E=\Span(e_3,e_4)$. On the first two coordinates, $T$ sends $(z_1,z_2)$ to $(-z_2,z_1)$, so $T^2+I$ sends every vector into $E$. On $E$, the map $T-3I$ sends $e_3$ to $e_4$ and $e_4$ to zero, hence $(T-3I)^2$ vanishes on $E$. Therefore $(T-3I)^2(T^2+I)=0$. Polynomial evaluation respects products, so $p(T)=0$.

To rule out an annihilating polynomial of degree below four, compute
\[
e_1=(1,0,0,0),\quad
Te_1=(0,1,2,0),\quad
T^2e_1=(-1,0,6,2),\quad
T^3e_1=(0,-1,16,12).
\]
In a zero relation with coefficients $a_0,a_1,a_2,a_3$, the first two coordinates give $a_0=a_2$ and $a_1=a_3$. The last two coordinates then give $6a_2+18a_3=0$ and $2a_2+12a_3=0$. The first yields $a_2=-3a_3$, and the second then yields $6a_3=0$. Thus all four coefficients vanish. If a nonzero polynomial of degree at most three annihilated $T$, applying it to $e_1$ would contradict this independence. Since $p$ is monic of degree four and annihilates $T$, uniqueness of the minimal polynomial identifies it with $p$.

Suppose now that $\F=\R$ and an upper-triangular representation existed, with real diagonal entries $\alpha_1,\ldots,\alpha_4$. Its diagonal-product polynomial $q(z)=\prod_{j=1}^4(z-\alpha_j)$ would annihilate $T$. Hence $q=pr$ for a real polynomial $r$. This coefficient identity also holds for complex arguments. At $z=i$ it would give $q(i)=0$, because $p(i)=0$. But every $i-\alpha_j$ is nonzero, so their product is nonzero. This contradiction rules out real triangularization.

Over $\C$, direct substitution gives $Tu_1=iu_1$, $Tu_2=-iu_2$, $Tu_3=3u_3$, and $Tu_4=u_3+3u_4$. To prove independence, suppose $\sum_{j=1}^4b_ju_j=0$. Put $a=4-3i$ and $\overline a=4+3i$. The first two coordinates are
\[b_1a+b_2\overline a=0,\qquad -ib_1a+ib_2\overline a=0.\]
Adding $i$ times the first equation to the second gives $2ib_2\overline a=0$, so $b_2=0$ and then $b_1=0$. The last two coordinates now give $b_3=b_4=0$. The four-vector independent list is a basis of $\C^4$. Its four image formulas give the displayed upper-triangular matrix.''',
4, 60, [
    r'To verify the annihilating polynomial, first observe where $T^2+I$ sends the space.',
    r'Test the independence of $e_1,Te_1,T^2e_1,T^3e_1$ to prove minimality.',
    r'For the real obstruction, compare a hypothetical diagonal-product polynomial with its value at $i$.',
],
['c3-thm-coordinate-linear-maps', 'def-operator-powers', 'def-polynomial-operator', 'thm-polynomial-evaluation-product', 'thm-minimal-polynomial-existence', 'def-minimal-polynomial', 'thm-annihilating-divisibility', 'thm-triangular-diagonal-product', 'c4-lem-conjugate-polynomial', 'c1-lem-scalar-cancellation', 'c2-thm-full-length-independent', 'c2-ex-coordinate-dimension', 'def-operator-matrix'], '5.43', 158, 'example')

s.r('lem-divisor-split-polynomial', 'A monic divisor of a split polynomial also splits', r'''Suppose
\[q(z)=\prod_{j=1}^{m}(z-\lambda_j),\qquad \lambda_j\in\F,\]
and $q=pr$, where $p,r\in\Poly(\F)$ and $p$ has leading coefficient $1$. Then $p$ is a product of factors $z-\mu$ with $\mu\in\F$. Empty products are allowed.''',
r'''We use induction on $m$. For $m=0$, $q=1$. The product-degree formula forces $p$ and $r$ to be nonzero constants; since $p$ has leading coefficient $1$, it is $1$, the empty product.
Suppose $m\ge1$. Both $p$ and $r$ are nonzero because their product is nonzero. Evaluation at $\lambda_1$ gives $p(\lambda_1)r(\lambda_1)=0$. If $p(\lambda_1)=0$, the factor-root theorem gives $p=(z-\lambda_1)p_1$, with $p_1$ again having leading coefficient $1$. Cancel the nonzero polynomial $z-\lambda_1$ from $q=pr$ to obtain
\[\prod_{j=2}^{m}(z-\lambda_j)=p_1r.\]
The induction hypothesis factors $p_1$, and restoring $z-\lambda_1$ factors $p$.
If $p(\lambda_1)\ne0$, then $r(\lambda_1)=0$. Write $r=(z-\lambda_1)r_1$ and cancel the same factor to obtain $\prod_{j=2}^{m}(z-\lambda_j)=pr_1$. The induction hypothesis directly factors $p$. These two cases complete the induction.''',
3, 30, [r'Evaluate the divisor equation at one of the listed roots, then cancel a linear factor from whichever factor vanishes there.'],
['c4-thm-factor-root', 'c4-lem-polynomial-cancellation', 'c4-lem-polynomial-product-degree', 'c1-lem-scalar-cancellation', 'c1-foundations'], page=159, kind='lemma')

s.r('lem-split-annihilator-triangular', 'A split annihilating polynomial produces a triangular basis', r'''Suppose $V$ is finite-dimensional, $T\in\Lin(V)$, and
\[\prod_{j=1}^{m}(T-\lambda_jI)=0,\qquad \lambda_j\in\F.\]
Then $T$ has an upper-triangular matrix in some basis. The empty product means $I$.''',
r'''Induct on $m$, allowing all finite-dimensional spaces at each induction stage. If $m=0$, the hypothesis is $I=0$. Every vector $v$ then satisfies $v=Iv=0$, so $V=\{0\}$ and its empty basis gives an upper-triangular matrix.
Suppose $m\ge1$ and let $U=\Range(T-\lambda_mI)$. This is an invariant subspace by the theorem on ranges of polynomial operators, and it is finite-dimensional because it is a subspace of $V$. Put $S=T|_U$ and $q(z)=\prod_{j=1}^{m-1}(z-\lambda_j)$. For $u\in U$, choose $v\in V$ with $u=(T-\lambda_mI)v$. The product hypothesis gives $q(T)u=0$.

For every nonnegative integer $k$, $S^ku=T^ku$ on $U$: this holds for $k=0$, and if it holds for $k$, invariance keeps $T^ku$ in $U$, so applying the restriction gives $S^{k+1}u=T^{k+1}u$. Thus $q(S)u=q(T)u=0$ for every $u\in U$. The induction hypothesis gives a basis $u_1,\ldots,u_r$ of $U$ in which $S$ is upper triangular. Extend it to a basis
\[u_1,\ldots,u_r,v_1,\ldots,v_s\]
of $V$. For each $j\le r$, triangularity of the restriction gives $Tu_j\in\Span(u_1,\ldots,u_j)$. For an added vector,
\[Tv_k=(T-\lambda_mI)v_k+\lambda_mv_k
\in U+\Span(v_k)
\subseteq\Span(u_1,\ldots,u_r,v_1,\ldots,v_k).\]
The initial-span criterion therefore makes the matrix of $T$ in this extended basis upper triangular. If $U=\{0\}$ or if no extension vectors are needed, the corresponding lists are empty and the same reasoning applies.''',
4, 60, [
    r'Induct on the number of linear factors, not on the dimension.',
    r'Use the range of the last factor as an invariant subspace.',
    r'Triangularize the restriction, then extend its basis to the whole space.',
],
['thm-polynomial-invariant', 'def-invariant', 'def-operator-powers', 'def-polynomial-operator', 'thm-polynomial-evaluation-product', 'thm-triangular-invariant', 'c2-thm-subspaces-finite', 'c2-thm-extend-independent', 'c3-def-range', 'c3-def-zero-identity-maps'], page=159, kind='lemma')

s.r('thm-triangularizable-splitting', 'Triangularization is equivalent to splitting of the minimal polynomial', r'''For an operator $T$ on a finite-dimensional vector space over $\F$, the following are equivalent:
\begin{enumerate}
\item Some basis gives an upper-triangular matrix for $T$.
\item The minimal polynomial of $T$ is a product of factors $z-\lambda$ with $\lambda\in\F$.
\end{enumerate}
For the zero space, the minimal polynomial is $1$, represented by an empty product.''',
r'''Suppose a triangular basis exists and its diagonal entries are $\alpha_1,\ldots,\alpha_n$. The diagonal-product theorem shows that $q(z)=\prod_{j=1}^n(z-\alpha_j)$ annihilates $T$. The annihilating-divisibility theorem says that $q$ is a polynomial multiple of the minimal polynomial $p$. The polynomial $p$ has leading coefficient $1$, so the split-divisor lemma proves that $p$ itself splits into linear factors over $\F$.
Conversely, suppose $p(z)=\prod_{j=1}^m(z-\lambda_j)$ with every $\lambda_j\in\F$. By definition $p(T)=0$, and polynomial evaluation respects products. Hence $\prod_{j=1}^m(T-\lambda_jI)=0$. The split-annihilator lemma supplies a triangular basis. On the zero space the empty basis is triangular and the minimal polynomial is $1$, so both implications include that case.''',
2, 20, [r'In one direction use the diagonal-product polynomial; in the other use the minimal polynomial itself as an annihilator.'],
['thm-triangular-diagonal-product', 'thm-annihilating-divisibility', 'def-minimal-polynomial', 'lem-divisor-split-polynomial', 'lem-split-annihilator-triangular', 'thm-polynomial-evaluation-product'], '5.44', 159)

s.r('thm-complex-triangularization', 'Every finite-dimensional complex operator can be triangularized', r'''For every operator on a finite-dimensional complex vector space, there is a basis in which its matrix is upper triangular.''',
r'''The minimal polynomial is nonzero and has leading coefficient $1$. Complex polynomial factorization writes it as a product of complex linear factors, with the empty product allowed for the constant polynomial $1$. The splitting criterion therefore gives an upper-triangular basis. In particular, the zero space is covered by its empty basis.''',
1, 10, [r'Apply complex factorization to the minimal polynomial.'],
['def-minimal-polynomial', 'c4-thm-complex-factorization', 'thm-triangularizable-splitting'], '5.47', 160)

s.r('thm-basis-vector-eigenvector', 'Which vectors of a triangular basis are eigenvectors?', r'''For any operator matrix in a basis $v_1,\ldots,v_n$, the basis vector $v_k$ is an eigenvector exactly when every entry in column $k$ except possibly the diagonal entry is zero. Consequently, in a nonempty upper-triangular basis, $v_1$ is an eigenvector, but later basis vectors need not be.''',
r'''The vector $v_k$ is nonzero because it belongs to a basis. Its image has expansion $Tv_k=\sum_jA_{jk}v_j$. By uniqueness of basis coefficients, this image is a scalar multiple of $v_k$ exactly when $A_{jk}=0$ for all $j\ne k$. In that case the scalar is $A_{kk}$, giving the eigenvector equation. For an upper-triangular matrix, column one already has zero entries in every row below the first, so $v_1$ is an eigenvector. Later columns may have nonzero entries above the diagonal. For example, the earlier operator $T(x,y,z)=(2x+y,5y+3z,8z)$ sends $e_2$ to $e_1+5e_2$, which is not a multiple of $e_2$ because its first coordinate is nonzero. Thus $e_2$ is not an eigenvector despite the triangular standard matrix.''',
1, 10, [r'Compare the image column with the coefficient list of a scalar multiple of $v_k$.'],
['def-operator-matrix', 'def-upper-triangular', 'def-eigenvector', 'c2-thm-basis-coordinates', 'ex-triangular-coordinate-matrix'], page=160)

s.card('upper-triangular', 'def-upper-triangular',
r'Which entries of an upper-triangular matrix must vanish?',
r'Every entry $A_{jk}$ with row index $j$ larger than column index $k$.')

s.card('triangular-invariant', 'thm-triangular-invariant',
r'Which invariant subspaces correspond to an upper-triangular matrix in a given basis?',
r'Every initial span $\Span(v_1,\ldots,v_k)$ must be invariant.')

s.card('triangular-product', 'thm-triangular-diagonal-product',
r'What polynomial identity follows from diagonal entries $\lambda_1,\ldots,\lambda_n$ of a triangular operator matrix?',
r'$(T-\lambda_1I)\cdots(T-\lambda_nI)=0$.')

s.card('triangular-invertible', 'thm-triangular-invertible',
r'When is an operator with an upper-triangular matrix invertible?',
r'Exactly when all its diagonal entries are nonzero.')

s.card('triangular-eigenvalues', 'thm-triangular-eigenvalues',
r'Where are the eigenvalues visible in an upper-triangular matrix?',
r'The eigenvalues are exactly the scalar values on the diagonal.')

s.card('triangular-splitting', 'thm-triangularizable-splitting',
r'What condition on the minimal polynomial characterizes triangularizability over $\F$?',
r'It must split into factors $z-\lambda$ with all $\lambda\in\F$.')

s.card('complex-triangularization', 'thm-complex-triangularization',
r'Why does every operator on a finite-dimensional complex space admit an upper-triangular basis?',
r'Its minimal polynomial splits over $\C$, so the splitting criterion applies.')

s.card('triangular-basis-eigenvectors', 'thm-basis-vector-eigenvector',
r'Does every vector of a triangular basis have to be an eigenvector?',
r'No. A basis vector is an eigenvector only if its column has no nonzero off-diagonal entry; triangularity guarantees this for the first column, but not for later ones.')

s.write()
