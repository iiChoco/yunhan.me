from common import Section

s = Section('7b')

s.p(
    'intro-spectral-theorem',
    'Diagonal matrices in orthonormal coordinates',
    r'''Diagonalization becomes especially useful when the diagonalizing basis is orthonormal. Over the real field this property characterizes self-adjoint operators; over the complex field it characterizes normal operators. All spaces in this section are finite-dimensional inner product spaces.''',
    243
)

s.r(
    'thm-spectral-equivalence',
    'Orthonormal diagonalization and eigenvector bases',
    r'''Let $T\in\Lin(V)$, and fix an orthonormal basis $e_1,\ldots,e_n$ of $V$. The matrix of $T$ in this basis is diagonal if and only if every $e_j$ is an eigenvector of $T$. Consequently, existence of an orthonormal diagonalizing basis is equivalent to existence of an orthonormal eigenvector basis.''',
    r'''Let $A$ be the matrix of $T$ in the chosen basis. By the matrix definition,
\[
Te_k=\sum_{j=1}^{n}A_{jk}e_j.
\]
If $A$ is diagonal, this becomes $Te_k=A_{kk}e_k$. Each $e_k$ has norm one and is therefore nonzero, so it is an eigenvector.

Conversely, suppose $Te_k=\lambda_ke_k$ for each $k$. Uniqueness of basis coefficients gives $A_{kk}=\lambda_k$ and $A_{jk}=0$ for $j\ne k$. Thus $A$ is diagonal. Applying this equivalence to each possible orthonormal basis proves the existence statement.

If $n=0$, the space is zero and its orthonormal basis is empty. Its representing matrix has no entries and is diagonal, while the assertion that every member of the empty basis is an eigenvector is vacuous. Hence the equivalence includes that case.''',
    1, 10,
    [r'''Read the image of each basis vector from its column.'''],
    ['c3-def-map-matrix', 'c5-def-eigenvector',
     'c6-def-orthonormal-basis', 'c6-def-orthonormal',
     'c6-thm-norm-properties', 'c2-thm-basis-coordinates'],
    page=243, kind='lemma'
)

s.r(
    'thm-self-adjoint-quadratic-invertible',
    'Irreducible real quadratics give invertible self-adjoint expressions',
    r'''Let $T\in\Lin(V)$ be self-adjoint, where $V$ is a finite-dimensional real or complex inner product space. If $b,c\in\R$ and $b^2<4c$, then
\[
Q=T^2+bT+cI
\]
is invertible. More precisely, with $S=T+(b/2)I$ and $d=c-b^2/4>0$,
\[
\ip{Qv}{v}=\norm{Sv}^2+d\norm{v}^2
\]
for every $v\in V$, and this scalar is strictly positive when $v\ne0$.''',
    r'''The adjoint rules give $I^*=I$. Because $b/2$ is real and $T^*=T$, they also give
\[
S^*=\bigl(T+(b/2)I\bigr)^*
=T^*+(b/2)I^*
=T+(b/2)I=S.
\]
Thus $S$ is self-adjoint. Distributivity of composition and the identity laws yield
\[
S^2=T^2+bT+(b^2/4)I,
\]
so $Q=S^2+dI$. For any $v$,
\[
\begin{aligned}
\ip{Qv}{v}
&=\ip{S^2v}{v}+d\ip{v}{v}\\
&=\ip{Sv}{S^*v}+d\norm{v}^2\\
&=\norm{Sv}^2+d\norm{v}^2.
\end{aligned}
\]
The first summand is nonnegative. If $v\ne0$, norm definiteness and $d>0$ make the second summand positive. Hence $\ip{Qv}{v}>0$, which rules out $Qv=0$, since the inner product of zero with $v$ is zero.

Therefore $\Null Q=\{0\}$, so $Q$ is injective. Its domain and target are the same finite-dimensional space, and the equal-dimension invertibility theorem makes $Q$ invertible. If $V=\{0\}$, the strict-positivity assertion has no nonzero input to test, the null space is still $\{0\}$, and the same invertibility argument applies.''',
    2, 20,
    [
        r'''Complete the square at the operator level.''',
        r'''The operator $T+(b/2)I$ is self-adjoint, so its squared quadratic expression is a squared norm.'''
    ],
    ['def-self-adjoint', 'def-adjoint', 'thm-adjoint-properties',
     'c3-thm-composition-laws', 'c3-thm-injective-null',
     'c3-thm-equal-dimension-invertibility',
     'c5-def-polynomial-operator',
     'c6-thm-inner-product-properties', 'c6-def-norm',
     'c6-thm-norm-properties', 'c1-foundations'],
    number='7.26', page=243
)

s.r(
    'thm-self-adjoint-splitting',
    'A self-adjoint minimal polynomial splits over the reals',
    r'''If $T$ is self-adjoint on a finite-dimensional real or complex inner product space, its minimal polynomial has the form
\[
p(z)=\prod_{j=1}^{m}(z-\lambda_j)
\qquad\text{with }\lambda_j\in\R.
\]
Repetitions are permitted in this statement. On the zero space, $m=0$ and the empty product is $1$.''',
    r'''If $V=\{0\}$, the minimal polynomial is $1$, giving the stated empty product. We now consider the two scalar fields.

Over $\C$, complex polynomial factorization writes the monic polynomial $p$ as a product of monic linear factors. Each root is an eigenvalue of $T$ by the minimal-root theorem. Every eigenvalue of a self-adjoint operator is real, so all the factors have the required real roots.

Over $\R$, real polynomial factorization writes $p$ as a product of monic real linear factors and monic quadratics of the form $z^2+bz+c$ with $b^2<4c$. The leading scalar in that factorization is one because $p$ is monic. Suppose at least one quadratic factor occurs. Isolate one of them and write
\[
p(z)=q(z)(z^2+bz+c),
\]
where $q$ is monic and $\deg q=\deg p-2$. Evaluation at $T$ gives
\[
q(T)(T^2+bT+cI)=p(T)=0.
\]
The quadratic operator is invertible by the preceding theorem. Composing on the right with its inverse yields $q(T)=0$. This contradicts the least degree defining the minimal polynomial, because $q$ is monic and has smaller degree. Therefore no quadratic factor occurs, leaving only real linear factors.''',
    3, 30,
    [
        r'''Over $\C$, combine polynomial factorization with reality of self-adjoint eigenvalues.''',
        r'''Over $\R$, suppose an irreducible quadratic factor occurs and cancel its invertible operator value.'''
    ],
    ['def-self-adjoint', 'thm-self-adjoint-eigenvalues',
     'thm-self-adjoint-quadratic-invertible',
     'c5-def-minimal-polynomial', 'c5-thm-minimal-roots',
     'c5-thm-polynomial-evaluation-product',
     'c5-thm-minimal-polynomial-existence',
     'c4-thm-complex-factorization', 'c4-thm-real-factorization',
     'c4-lem-polynomial-product-degree',
     'c3-def-map-inverse', 'c3-thm-composition-laws'],
    number='7.27', page=244
)

s.r(
    'cor-self-adjoint-eigenvalue',
    'A nonzero self-adjoint space has an eigenvector',
    r'''Every self-adjoint operator on a nonzero finite-dimensional real or complex inner product space has an eigenvalue, and that eigenvalue is real.''',
    r'''The minimal polynomial cannot be the constant polynomial $1$, because evaluating $1$ gives the identity operator, which is nonzero on a nonzero space. Thus its degree is positive. The preceding splitting theorem expresses it as a nonempty product of linear factors with real roots. Choose one of those roots. The minimal-root theorem makes it an eigenvalue of the operator, proving the assertion.''',
    1, 10,
    [r'''A positive-degree product of real linear factors has a real root.'''],
    ['thm-self-adjoint-splitting',
     'c5-def-minimal-polynomial', 'c5-def-polynomial-operator',
     'c5-thm-minimal-roots', 'c3-def-zero-identity-maps'],
    page=244, kind='corollary'
)

s.r(
    'thm-real-spectral',
    'Real spectral theorem',
    r'''Let $V$ be a finite-dimensional real inner product space and let $T\in\Lin(V)$. The following conditions are equivalent:
\begin{enumerate}
\item $T$ is self-adjoint.
\item In some orthonormal basis, the matrix of $T$ is diagonal.
\item $V$ has an orthonormal basis consisting of eigenvectors of $T$.
\end{enumerate}''',
    r'''Suppose $T$ is self-adjoint. Its minimal polynomial splits into real linear factors by the self-adjoint splitting theorem. The orthonormal triangularization criterion therefore gives an orthonormal basis in which its matrix $A$ is upper triangular.

In an orthonormal basis, the adjoint matrix is the conjugate transpose. The entries here are real, so conjugate transpose is ordinary transpose. Since $T=T^*$, their representing matrices agree, giving $A_{jk}=A_{kj}$ for every pair of indices. If $j>k$, upper triangularity gives $A_{jk}=0$. If $j<k$, it gives $A_{kj}=0$, and the symmetry then gives $A_{jk}=0$. Thus all off-diagonal entries vanish, proving condition 2.

Conversely, suppose $T$ has a diagonal matrix $A$ in an orthonormal basis. Because its diagonal entries are real, its conjugate transpose equals $A$. The adjoint matrix formula therefore gives $\Mat(T^*)=\Mat(T)$ in that same basis. Matrix representation in fixed bases is injective, so $T^*=T$, proving condition 1.

The equivalence of conditions 2 and 3 is the earlier orthonormal diagonalization and eigenvector-basis equivalence. This completes all implications.

On the zero space the empty orthonormal basis gives the empty diagonal matrix, and the sole operator equals its adjoint. Hence all three conditions hold there as well.''',
    3, 30,
    [
        r'''First obtain an upper-triangular matrix in an orthonormal basis.''',
        r'''A real matrix that is both upper triangular and equal to its transpose must be diagonal.'''
    ],
    ['def-self-adjoint', 'thm-self-adjoint-splitting',
     'thm-adjoint-matrix', 'thm-spectral-equivalence',
     'c6-thm-orthonormal-triangular', 'c6-def-orthonormal-basis',
     'c3-thm-map-matrix-isomorphism', 'c4-thm-complex-properties'],
    number='7.29', page=245
)

s.r(
    'ex-real-spectral-basis',
    'An explicit real orthonormal eigenvector basis',
    r'''Let $T\in\Lin(\R^3)$ have the standard-basis matrix
\[
A=
\begin{pmatrix}
14&-13&8\\
-13&14&8\\
8&8&-7
\end{pmatrix}.
\]
Prove that $T$ is self-adjoint and that
\[
e_1=\frac{(1,-1,0)}{\sqrt2},\qquad
e_2=\frac{(1,1,1)}{\sqrt3},\qquad
e_3=\frac{(1,1,-2)}{\sqrt6}
\]
is an orthonormal eigenvector basis. Show that the matrix in this basis is
\[
\begin{pmatrix}
27&0&0\\
0&9&0\\
0&0&-15
\end{pmatrix}.
\]''',
    r'''The standard basis is orthonormal. The real matrix $A$ equals its transpose, so the adjoint matrix formula gives the same matrix for $T^*$ and $T$. Injectivity of matrix representation yields $T^*=T$.

The unnormalized displayed vectors have squared norms $2,3,6$, respectively, so their stated normalizations have norm one. Their three distinct inner products before normalization are
\[
(1,-1,0)\cdot(1,1,1)=1-1=0,
\]
\[
(1,-1,0)\cdot(1,1,-2)=1-1=0,
\qquad
(1,1,1)\cdot(1,1,-2)=1+1-2=0.
\]
Dividing by the positive normalization factors preserves these zero values. Thus the list is orthonormal. Its length is $\dim\R^3=3$, so it is an orthonormal basis.

Direct multiplication gives
\[
\begin{aligned}
A(1,-1,0)^{\mathsf t}&=(27,-27,0)^{\mathsf t}
=27(1,-1,0)^{\mathsf t},\\
A(1,1,1)^{\mathsf t}&=(9,9,9)^{\mathsf t}
=9(1,1,1)^{\mathsf t},\\
A(1,1,-2)^{\mathsf t}&=(-15,-15,30)^{\mathsf t}
=-15(1,1,-2)^{\mathsf t}.
\end{aligned}
\]
By the matrix-action formula and linearity, the normalized vectors satisfy
$Te_1=27e_1$, $Te_2=9e_2$, and $Te_3=-15e_3$. They are nonzero, so they are eigenvectors. Their images supply the three columns of the displayed diagonal matrix in this basis.''',
    2, 20,
    [
        r'''Check orthogonality before checking the three eigenvalue equations.''',
        r'''The matrix columns in an eigenvector basis contain the corresponding eigenvalues.'''
    ],
    ['def-self-adjoint', 'thm-adjoint-matrix',
     'c3-thm-map-matrix-isomorphism', 'c3-thm-matrix-action',
     'c3-def-map-matrix', 'c6-thm-standard-inner-product',
     'c6-def-orthonormal', 'c6-thm-full-orthonormal',
     'c6-thm-norm-properties', 'c2-ex-coordinate-dimension',
     'c5-def-eigenvector'],
    number='7.30', page=245, kind='example'
)

s.r(
    'thm-complex-spectral',
    'Complex spectral theorem',
    r'''Let $V$ be a finite-dimensional complex inner product space and let $T\in\Lin(V)$. The following conditions are equivalent:
\begin{enumerate}
\item $T$ is normal.
\item In some orthonormal basis, the matrix of $T$ is diagonal.
\item $V$ has an orthonormal basis consisting of eigenvectors of $T$.
\end{enumerate}''',
    r'''Assume $T$ is normal. Schur's theorem supplies an orthonormal basis $e_1,\ldots,e_n$ in which $A=\Mat(T)$ is upper triangular. We prove by induction on the row index $k$ that every off-diagonal entry in row $k$ is zero.

Suppose that every off-diagonal entry in rows $1,\ldots,k-1$ has already been shown to vanish; for $k=1$ there are no preceding rows. In column $k$, entries below the diagonal vanish by upper triangularity. Entries above the diagonal lie in the preceding rows and vanish by the induction hypothesis. Consequently
\[
Te_k=A_{kk}e_k,\qquad \norm{Te_k}^2=|A_{kk}|^2.
\]
The adjoint matrix is the conjugate transpose, so the coefficients of $T^*e_k$ are $\overline{A_{kj}}$ as $j$ varies. For $j<k$, the entry $A_{kj}$ is below the diagonal and is zero. The norm formula for orthonormal coordinates therefore gives
\[
\norm{T^*e_k}^2=\sum_{j=k}^{n}|A_{kj}|^2.
\]
Normality implies $\norm{Te_k}=\norm{T^*e_k}$. Comparing the squared norms and subtracting the common diagonal term yields
\[
\sum_{j=k+1}^{n}|A_{kj}|^2=0.
\]
Every summand is a nonnegative real number, so every one is zero. A scalar has modulus zero only when it is zero, hence $A_{kj}=0$ for all $j>k$. The entries with $j<k$ were already zero by triangularity, proving the induction step. After all rows have been considered, $A$ is diagonal. This proves condition 2.

Conversely, suppose condition 2 holds. In the given orthonormal basis write $Te_j=\lambda_je_j$. The adjoint matrix formula gives $T^*e_j=\overline{\lambda_j}e_j$. Linearity then gives
\[
T^*Te_j=\lambda_j\overline{\lambda_j}e_j,
\qquad
TT^*e_j=\overline{\lambda_j}\lambda_je_j.
\]
The scalar products are equal, so the two compositions agree on every basis vector. Applying them to arbitrary basis expansions shows that they agree on every vector. Thus $T^*T=TT^*$, which is normality.

Conditions 2 and 3 are equivalent by the earlier orthonormal diagonalization and eigenvector-basis result. For the zero space, the empty matrix is diagonal, the empty basis satisfies condition 3, and the sole operator commutes with its adjoint. The row induction has no steps in that case, so all conclusions remain valid.''',
    3, 40,
    [
        r'''Use Schur's theorem to obtain an upper-triangular matrix in an orthonormal basis.''',
        r'''Compare the norms of $Te_k$ and $T^*e_k$, beginning with $k=1$.''',
        r'''After clearing the preceding rows, the norm comparison forces the remaining off-diagonal entries of row $k$ to vanish.'''
    ],
    ['def-normal', 'thm-normal-norm', 'thm-adjoint-matrix',
     'thm-spectral-equivalence',
     'c6-thm-schur', 'c6-thm-orthonormal-coordinates',
     'c6-thm-norm-properties', 'c6-def-orthonormal-basis',
     'c3-def-map-matrix', 'c3-def-map-composition',
     'c3-def-linear-map', 'c2-thm-basis-coordinates',
     'c4-thm-complex-properties', 'c1-foundations'],
    number='7.31', page=246
)

s.r(
    'ex-complex-spectral-basis',
    'A complex orthonormal eigenvector basis',
    r'''Define $T:\C^2\to\C^2$ by
\[
T(w,z)=(2w-3z,3w+2z).
\]
Prove that $T$ is normal and that
\[
e_1=\frac{(i,1)}{\sqrt2},\qquad
e_2=\frac{(-i,1)}{\sqrt2}
\]
is an orthonormal eigenvector basis. Compute its representing matrix in this basis.''',
    r'''The coordinate-map theorem proves linearity, since both output coordinates are scalar linear combinations of the inputs. Its standard-basis matrix is
\[
\begin{pmatrix}2&-3\\3&2\end{pmatrix}.
\]

The squared norm of each proposed basis vector is $(|i|^2+1)/2=1$. Using conjugation in the second inner-product variable gives
\[
\ip{e_1}{e_2}
=\frac{i\,\overline{-i}+1}{2}
=\frac{i^2+1}{2}=0.
\]
The reverse pairing is its conjugate and is also zero. Thus the two vectors are orthonormal, and their length equals $\dim\C^2$, so they form an orthonormal basis.

Direct computation yields
\[
T(i,1)=(2i-3,3i+2)=(2+3i)(i,1)
\]
and
\[
T(-i,1)=(-2i-3,-3i+2)=(2-3i)(-i,1).
\]
Dividing these equations by $\sqrt2$ shows
$Te_1=(2+3i)e_1$ and $Te_2=(2-3i)e_2$.
The matrix in this ordered basis is therefore
\[
\begin{pmatrix}
2+3i&0\\
0&2-3i
\end{pmatrix}.
\]
This orthonormal eigenvector basis satisfies the third condition of the complex spectral theorem, so that theorem proves that $T$ is normal.''',
    2, 20,
    [
        r'''Conjugate the second vector when checking the off-diagonal inner product.''',
        r'''Compute the images before dividing by the normalization factor.'''
    ],
    ['thm-complex-spectral', 'c3-thm-coordinate-linear-maps',
     'c3-def-map-matrix', 'c6-thm-standard-inner-product',
     'c6-thm-inner-product-properties', 'c6-def-orthonormal',
     'c6-thm-full-orthonormal', 'c2-ex-coordinate-dimension',
     'c5-def-eigenvector', 'c4-thm-complex-properties'],
    number='7.33', page=247, kind='example'
)

s.card(
    'orthonormal-diagonal-equivalence',
    'thm-spectral-equivalence',
    r'''What does a diagonal representing matrix say about the chosen orthonormal basis vectors?''',
    r'''Each is an eigenvector, and its eigenvalue is the corresponding diagonal entry.'''
)

s.card(
    'self-adjoint-quadratic',
    'thm-self-adjoint-quadratic-invertible',
    r'''Why is $T^2+bT+cI$ invertible for self-adjoint $T$ when $b^2<4c$?''',
    r'''Writing $S=T+(b/2)I$ gives $\ip{(T^2+bT+cI)v}{v}=\norm{Sv}^2+(c-b^2/4)\norm{v}^2>0$ for $v\ne0$. Its kernel is zero, so finite-dimensional invertibility follows.'''
)

s.card(
    'self-adjoint-minimal-splitting',
    'thm-self-adjoint-splitting',
    r'''What factorization is guaranteed for the minimal polynomial of a finite-dimensional self-adjoint operator?''',
    r'''It is a product of linear factors with real roots. The empty product $1$ occurs on the zero space.'''
)

s.card(
    'real-spectral',
    'thm-real-spectral',
    r'''Which operators on finite-dimensional real inner product spaces have orthonormal eigenvector bases?''',
    r'''Exactly the self-adjoint operators.'''
)

s.card(
    'complex-spectral',
    'thm-complex-spectral',
    r'''Which operators on finite-dimensional complex inner product spaces have orthonormal eigenvector bases?''',
    r'''Exactly the normal operators.'''
)

s.card(
    'normal-triangular-proof',
    'thm-complex-spectral',
    r'''What turns Schur's upper-triangular matrix into a diagonal matrix for a normal operator?''',
    r'''The identities $\norm{Te_k}=\norm{T^*e_k}$ force the off-diagonal entries in successive rows to vanish, using sums of their squared moduli.'''
)

s.card(
    'complex-example-diagonal',
    'ex-complex-spectral-basis',
    r'''For $T(w,z)=(2w-3z,3w+2z)$, which eigenvalues correspond to the orthonormal vectors $(i,1)/\sqrt2$ and $(-i,1)/\sqrt2$?''',
    r'''They correspond respectively to $2+3i$ and $2-3i$.'''
)

s.write()
