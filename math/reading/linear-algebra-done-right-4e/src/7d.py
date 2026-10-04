from common import Section

s = Section('7d')

s.p('intro-isometries-factorizations', 'Norm preservation and matrix factorizations', r'''Throughout this section the inner product spaces are finite-dimensional over $\F$, with inner products linear in the first variable. We first characterize linear maps that preserve lengths and then specialize to operators on one space. These ideas combine with Gram–Schmidt and positive square roots to produce QR and Cholesky factorizations.''', 258)

s.d('def-isometry', 'Linear isometries', r'''A linear map $S\in\Lin(V,W)$ is an isometry if
\[\|Sv\|=\|v\|\quad\text{for every }v\in V.\]
The domain and target need not be the same space.''', '7.44', 258)

s.r('lem-isometry-injective', 'Isometries are injective but need not be surjective', r'''Every linear isometry is injective. Consequently, an isometry $V\to W$ requires $\dim V\le\dim W$. An isometry need not map onto its target.''',
r'''If $Sv=0$, norm preservation gives $\|v\|=\|Sv\|=0$, hence $v=0$. The null-space criterion therefore makes $S$ injective. Rank-nullity gives $\dim V=\dim\Range S$, and the subspace dimension bound gives $\dim\Range S\le\dim W$. For an example without surjectivity, the map $S:\R\to\R^2$ given by $Sx=(x,0)$ is linear and preserves the standard norm, but $(0,1)$ is not in its range. The injectivity and dimension arguments include a zero-dimensional domain.''',
1, 10, [r'Apply norm preservation to a vector in the kernel.'],
['def-isometry', 'c6-thm-norm-properties', 'c6-thm-standard-inner-product', 'c3-thm-injective-null', 'c3-thm-rank-nullity', 'c2-thm-subspace-dimension'], page=258, kind='lemma')

s.r('ex-isometry-from-orthonormal-list', 'Sending an orthonormal basis to an orthonormal list', r'''Let $e_1,\ldots,e_n$ be an orthonormal basis of $V$ and let $g_1,\ldots,g_n$ be an orthonormal list in $W$. The unique linear map with $Se_j=g_j$ for every $j$ is an isometry.''',
r'''Prescribing the values on a basis gives a unique linear map. Write $v=\sum_j a_je_j$. The orthonormal norm formula gives $\|v\|^2=\sum_j|a_j|^2$. Linearity gives $Sv=\sum_j a_jg_j$, and the same norm formula for the orthonormal list gives $\|Sv\|^2=\sum_j|a_j|^2$. The two norms are nonnegative, so equality of their squares implies equality of the norms. For the empty basis, the domain is zero and both norms are zero.''',
1, 10, [r'Compare the squared norms of the two combinations with the same coefficients.'],
['def-isometry', 'c3-thm-linear-map-basis', 'c6-thm-orthonormal-norm', 'c6-def-orthonormal-basis', 'c2-thm-basis-coordinates'], '7.45', 258, 'example')

s.r('thm-isometry-equivalences', 'Equivalent descriptions of an isometry', r'''Fix orthonormal bases $\mathcal E=(e_1,\ldots,e_n)$ of $V$ and $\mathcal F=(f_1,\ldots,f_m)$ of $W$. For $S\in\Lin(V,W)$, the following are equivalent:
\begin{enumerate}
\item $S$ is an isometry.
\item $S^*S=I_V$.
\item $\ip{Su}{Sv}=\ip u v$ for all $u,v\in V$.
\item $Se_1,\ldots,Se_n$ is an orthonormal list.
\item The columns of $\Mat(S,\mathcal E,\mathcal F)$ form an orthonormal list in $\F^m$ with its standard inner product.
\end{enumerate}''',
r'''Assume norm preservation and put $D=I_V-S^*S$. The adjoint rules show that $D^*=D$. For every $v$,
\[\ip{Dv}{v}=\|v\|^2-\ip{S^*Sv}{v}
=\|v\|^2-\|Sv\|^2=0.\]
The zero-quadratic theorem for self-adjoint operators gives $D=0$, proving the second condition. If $S^*S=I_V$, the adjoint identity gives
\[\ip{Su}{Sv}=\ip u{S^*Sv}=\ip u v,\]
so the third condition holds. It makes the pairings of the vectors $Se_j$ equal those of the $e_j$, proving the fourth condition. Conversely, the fourth condition makes $S$ an isometry by the preceding orthonormal-list construction.

To connect the final condition, write $A=\Mat(S,\mathcal E,\mathcal F)$. Orthonormal expansion in the target gives
\[\ip{Se_k}{Se_r}=\sum_{j=1}^m A_{jk}\overline{A_{jr}}.\]
The right side is exactly the standard inner product of columns $k$ and $r$ of $A$. Thus the fourth and fifth conditions are equivalent. These implications prove equivalence of all five. Empty bases and columns cause no exception: the sums and orthonormality conditions have their usual empty-list meanings.''',
2, 20, [r'For norm preservation to imply the adjoint identity, use the self-adjoint operator $I-S^*S$.', r'Compare column inner products using orthonormal coordinates in the target.'],
['def-isometry', 'ex-isometry-from-orthonormal-list', 'thm-adjoint-properties', 'def-adjoint', 'thm-zero-self-adjoint-quadratic', 'c6-thm-orthonormal-coordinates', 'c6-def-orthonormal', 'c3-def-map-matrix'], '7.49', 259)

s.d('def-unitary', 'Unitary operators', r'''An operator $S\in\Lin(V)$ is unitary if it is both invertible and an isometry. Thus a unitary operator acts from a space onto that same space.''', '7.51', 260)

s.r('lem-finite-isometry-unitary', 'On one finite-dimensional space, every isometry is unitary', r'''An operator on a finite-dimensional inner product space is unitary if and only if it is an isometry.''',
r'''Every unitary operator is an isometry by definition. Conversely, an isometry is injective. An injective operator on a finite-dimensional space is invertible by the equal-dimension invertibility theorem. It therefore satisfies both requirements for unitarity. On the zero space the unique operator is the identity, is invertible, and preserves its sole norm value zero.''',
1, 10, [r'Use injectivity and equality of the domain and target dimensions.'],
['def-unitary', 'lem-isometry-injective', 'c3-thm-equal-dimension-invertibility'], page=260, kind='lemma')

s.r('ex-unitary-rotation', 'A rotation matrix is unitary', r'''For every real $\theta$, the operator on $\F^2$ with standard matrix
\[\begin{pmatrix}\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta\end{pmatrix}\]
is unitary.''',
r'''Put $a=\cos\theta$ and $b=\sin\theta$. The elementary trigonometric identity gives $a^2+b^2=1$. The two columns $(a,b)$ and $(-b,a)$ have squared norm $1$, and their inner product is $-ab+ba=0$. They therefore form an orthonormal list for the standard inner product over either field. The column characterization makes the associated operator an isometry, and the finite-dimensional operator criterion makes it unitary.''',
1, 10, [r'Check the norms and mutual inner product of the two columns.'],
['thm-isometry-equivalences', 'lem-finite-isometry-unitary', 'c6-thm-standard-inner-product', 'c6-thm-trigonometric-calculus-facts'], '7.52', 260, 'example')

s.r('thm-unitary-equivalences', 'Equivalent descriptions of a unitary operator', r'''Fix an orthonormal basis $\mathcal E=(e_1,\ldots,e_n)$ of $V$. For $S\in\Lin(V)$, the following are equivalent:
\begin{enumerate}
\item $S$ is unitary.
\item $S^*S=SS^*=I_V$.
\item $S$ is invertible and $S^{-1}=S^*$.
\item $Se_1,\ldots,Se_n$ is an orthonormal basis of $V$.
\item The rows of $\Mat(S,\mathcal E)$ form an orthonormal basis of $\F^n$.
\item $S^*$ is unitary.
\end{enumerate}''',
r'''If $S$ is unitary, the isometry criterion gives $S^*S=I$. Multiplication on the right by $S^{-1}$ gives $S^*=S^{-1}$, hence also $SS^*=I$. The second condition gives the third by the definition of an inverse, and the third gives $S^*S=I$, hence makes $S$ an isometry and therefore unitary. This proves equivalence of the first three conditions.

An isometry sends the fixed orthonormal basis to an orthonormal list of length $\dim V$, which is an orthonormal basis. Conversely, that image basis is an orthonormal list, so the isometry criterion and the finite-dimensional operator lemma give unitarity. This proves equivalence with the fourth condition.

Write $A=\Mat(S,\mathcal E)$. For rows $j,k$, their standard inner product is
\[\sum_{\ell=1}^n A_{j\ell}\overline{A_{k\ell}}=(AA^*)_{jk}.\]
Thus the rows form an orthonormal list exactly when $AA^*=I_n$. Such a list of length $n$ is a basis. By the adjoint-matrix and composition formulas, $AA^*=I_n$ is equivalent to $SS^*=I_V$. The finite-dimensional one-sided inverse theorem then gives $S^*S=I_V$ also, proving equivalence with the second condition.

Finally, applying the second condition to $S^*$ gives the same two identities in the opposite order, because $(S^*)^*=S$. Thus the second condition holds for $S$ exactly when it holds for $S^*$, proving equivalence with the sixth condition. The argument includes the empty basis, whose rows form the empty orthonormal basis of $\F^0$.''',
3, 30, [r'An inverse and the adjoint coincide once $S^*S=I$ and invertibility are known.', r'Row inner products are the entries of $AA^*$.'],
['def-unitary', 'thm-isometry-equivalences', 'lem-finite-isometry-unitary', 'thm-adjoint-properties', 'thm-adjoint-matrix', 'c6-thm-full-orthonormal', 'c3-thm-one-sided-inverse', 'c3-thm-matrix-composition', 'c3-lem-identity-matrix-laws', 'c3-def-matrix-product', 'c3-def-map-inverse'], '7.53', 261)

s.r('thm-unitary-eigenvalues', 'Unitary eigenvalues lie on the unit circle', r'''Every eigenvalue $\lambda$ of a unitary operator satisfies $|\lambda|=1$.''',
r'''Choose a corresponding nonzero eigenvector $v$. Norm homogeneity and norm preservation give
\[|\lambda|\|v\|=\|\lambda v\|=\|Sv\|=\|v\|.\]
Since $\|v\|>0$, division gives $|\lambda|=1$. If the operator has no eigenvalues, including on the zero space, the assertion is vacuous.''',
1, 10, [r'Take norms of the eigenvector equation.'],
['def-unitary', 'def-isometry', 'c5-def-eigenvalue', 'c6-thm-norm-properties'], '7.54', 262)

s.r('thm-unitary-complex-diagonalization', 'Unitary operators over the complex field', r'''On a finite-dimensional complex inner product space, an operator is unitary if and only if there is an orthonormal basis of eigenvectors whose corresponding eigenvalues all have modulus one.''',
r'''If $S$ is unitary, then $S^*S=SS^*=I$, so it is normal. The complex spectral theorem supplies an orthonormal eigenvector basis, and the unitary eigenvalue theorem makes every associated eigenvalue have modulus one.
Conversely, suppose $Se_j=\lambda_je_j$ in an orthonormal basis, with $|\lambda_j|=1$. For indices $j,k$,
\[\ip{Se_j}{Se_k}=\lambda_j\overline{\lambda_k}\ip{e_j}{e_k}.\]
This is zero for distinct indices and equals $|\lambda_j|^2=1$ when the indices agree. Thus the image list is orthonormal. The isometry criterion and finite-dimensional operator lemma imply that $S$ is unitary. For the zero space, the empty basis satisfies the stated condition and its unique operator is unitary.''',
2, 20, [r'Use the complex spectral theorem after proving normality.', r'For the converse, check the image of the proposed orthonormal basis.'],
['thm-unitary-equivalences', 'def-normal', 'thm-complex-spectral', 'thm-unitary-eigenvalues', 'thm-isometry-equivalences', 'lem-finite-isometry-unitary', 'c6-thm-inner-product-properties'], '7.55', 262)

s.d('def-unitary-matrix', 'Unitary matrices', r'''A square matrix $Q\in\F^{n,n}$ is unitary if its columns form an orthonormal list in $\F^n$ with the standard inner product. Such a list is also an orthonormal basis. The empty square matrix is unitary.''', '7.56', 263)

s.r('thm-unitary-matrix-equivalences', 'Equivalent tests for a unitary matrix', r'''For $Q\in\F^{n,n}$, the following conditions are equivalent:
\begin{enumerate}
\item $Q$ is unitary.
\item Its rows form an orthonormal list.
\item $\|Qx\|=\|x\|$ for every $x\in\F^n$.
\item $Q^*Q=QQ^*=I_n$.
\item $Q^*Q=I_n$.
\item $QQ^*=I_n$.
\end{enumerate}
They imply $Q^{-1}=Q^*$.''',
r'''Let $S$ be the linear operator on $\F^n$ whose standard matrix is $Q$. The standard basis is orthonormal. The isometry equivalences identify column orthonormality, preservation of norms, and $S^*S=I$. The finite-dimensional isometry lemma identifies these conditions with unitarity of $S$. The unitary equivalences identify that condition with row orthonormality and with both inverse identities. The adjoint-matrix theorem gives the standard matrix $Q^*$ for $S^*$, while matrices of products are products of matrices. Hence the operator identities translate exactly into the stated matrix identities.
Either single identity suffices: $Q^*Q=I$ corresponds to $S^*S=I$ and thus to an isometry, whereas $QQ^*=I$ corresponds to $SS^*=I$ and the finite-dimensional one-sided inverse theorem supplies the other identity. Finally, the two identities state that $Q^*$ is the inverse matrix of $Q$. All translations include size zero.''',
2, 20, [r'Apply the operator results to the map whose standard matrix is $Q$.'],
['def-unitary-matrix', 'thm-isometry-equivalences', 'lem-finite-isometry-unitary', 'thm-unitary-equivalences', 'thm-adjoint-matrix', 'c3-thm-coordinate-linear-maps', 'c3-thm-matrix-composition', 'c3-thm-one-sided-inverse', 'c3-def-invertible-matrix', 'c6-ex-standard-orthonormal'], '7.57', 263)

s.r('lem-conjugate-transpose-algebra', 'Products and inverses under conjugate transposition', r'''For matrices with compatible sizes,
\[(AB)^*=B^*A^*,\qquad (A^*)^*=A.\]
If $A$ is invertible, then $A^*$ is invertible and
\[(A^*)^{-1}=(A^{-1})^*.\]''',
r'''For an entry of the conjugate transpose of a product,
\[
((AB)^*)_{jk}
=\overline{\sum_\ell A_{k\ell}B_{\ell j}}
=\sum_\ell\overline{B_{\ell j}}\,\overline{A_{k\ell}}
=(B^*A^*)_{jk}.
\]
This uses conjugation of scalar sums and products. Applying the entry definition twice gives $((A^*)^*)_{jk}=\overline{\overline{A_{jk}}}=A_{jk}$.
If $AA^{-1}=A^{-1}A=I$, conjugate transposition gives
\[(A^{-1})^*A^*=I,\qquad A^*(A^{-1})^*=I.\]
Thus $(A^{-1})^*$ is the inverse of $A^*$. Empty dimensions give either empty entry assertions or empty sums, so the identities include them.''',
2, 15, [r'Use the entry formula for a product and reverse the scalar factors after conjugating.'],
['def-conjugate-transpose', 'c3-def-matrix-product', 'c3-def-invertible-matrix', 'c4-thm-complex-properties'], page=264, kind='lemma')

s.r('thm-qr', 'QR factorization with positive diagonal', r'''Let $A\in\F^{n,n}$ have linearly independent columns. There is a unique pair $Q,R\in\F^{n,n}$ such that
\[A=QR,\]
where $Q$ is unitary and $R$ is upper triangular with strictly positive real diagonal entries. For $n=0$, the unique empty pair is the required factorization.''',
r'''Assume first $n\ge1$, and denote the columns of $A$ by $v_1,\ldots,v_n$. Apply Gram–Schmidt to this independent list to obtain an orthonormal basis $e_1,\ldots,e_n$ with the same successive spans. At step $k$, its nonzero remainder is
\[h_k=v_k-\sum_{j<k}\ip{v_k}{e_j}e_j,\qquad e_k=h_k/\|h_k\|.\]
Let $Q$ have columns $e_1,\ldots,e_n$, and define $R_{jk}=\ip{v_k}{e_j}$. Since $v_k\in\Span(e_1,\ldots,e_k)$, its coefficient at $e_j$ is zero for $j>k$. Thus $R$ is upper triangular. The displayed remainder expression gives
\[v_k=\sum_{j<k}\ip{v_k}{e_j}e_j+\|h_k\|e_k,\]
so uniqueness of orthonormal coefficients gives $R_{kk}=\|h_k\|>0$. The $k$th column of $QR$ is $\sum_jR_{jk}e_j=v_k$, proving $A=QR$. The columns of $Q$ are orthonormal, so $Q$ is unitary.

For uniqueness, suppose also $A=\widehat Q\widehat R$, with columns $q_j$ of $\widehat Q$ orthonormal and diagonal entries of $\widehat R$ positive real numbers. The first column equation is $v_1=\widehat R_{11}q_1$. Taking norms forces $\widehat R_{11}=\|v_1\|$, and hence $q_1=v_1/\|v_1\|=e_1$. Suppose inductively that $q_j=e_j$ for $j<k$. The $k$th column equation is
\[v_k=\sum_{j<k}\widehat R_{jk}q_j+\widehat R_{kk}q_k.\]
Taking its inner product with $q_j$ for $j<k$ yields $\widehat R_{jk}=\ip{v_k}{q_j}=\ip{v_k}{e_j}$. Subtracting these earlier terms gives $h_k=\widehat R_{kk}q_k$. The unit norm of $q_k$ and positivity of $\widehat R_{kk}$ force $\widehat R_{kk}=\|h_k\|$ and $q_k=e_k$. Induction gives $\widehat Q=Q$. Taking inner products of every column equation with every $e_j$ now yields $\widehat R_{jk}=R_{jk}$, so $\widehat R=R$. When $n=0$, there is exactly one matrix of each required size and the conditions are vacuous.''',
3, 45, [r'Apply Gram–Schmidt to the columns and record the expansion coefficients.', r'For uniqueness, recover each next unit column from the residual after subtracting all earlier columns.'],
['c6-thm-gram-schmidt', 'c6-thm-orthonormal-coordinates', 'c6-thm-full-orthonormal', 'c6-thm-norm-properties', 'def-unitary-matrix', 'c5-def-upper-triangular', 'c3-thm-column-combination', 'c2-thm-basis-coordinates'], '7.58', 264)

s.r('ex-qr-factorization', 'An explicit QR factorization', r'''The QR factorization of
\[A=\begin{pmatrix}1&2&1\\0&1&-4\\0&3&2\end{pmatrix}\]
with positive diagonal in $R$ is
\[
Q=\begin{pmatrix}
1&0&0\\
0&1/\sqrt{10}&-3/\sqrt{10}\\
0&3/\sqrt{10}&1/\sqrt{10}
\end{pmatrix},
\qquad
R=\begin{pmatrix}
1&2&1\\
0&\sqrt{10}&\sqrt{10}/5\\
0&0&7\sqrt{10}/5
\end{pmatrix}.
\]''',
r'''First, the columns of $A$ are independent. In a zero combination with coefficients $a,b,c$, the second and third coordinates give $b-4c=0$ and $3b+2c=0$. Substitution yields $14c=0$, then $b=0$, and the first coordinate gives $a=0$.
The columns of $Q$ are
\[e_1=(1,0,0),\quad e_2=(0,1,3)/\sqrt{10},\quad
e_3=(0,-3,1)/\sqrt{10}.\]
Each has norm one. The first is orthogonal to the other two, and $\ip{e_2}{e_3}=(-3+3)/10=0$. Thus $Q$ is unitary. The matrix $R$ is upper triangular with positive real diagonal. Its columns give the following columns of $QR$:
\[
e_1=(1,0,0),\qquad
2e_1+\sqrt{10}e_2=(2,1,3),
\]
\[
e_1+\frac{\sqrt{10}}5e_2+\frac{7\sqrt{10}}5e_3
=(1,1/5-21/5,3/5+7/5)=(1,-4,2).
\]
These are exactly the columns of $A$. The QR uniqueness theorem therefore identifies the displayed matrices as its required factorization.''',
2, 20, [r'Check the three columns of $Q$ and compute the product one column at a time.'],
['thm-qr', 'def-unitary-matrix', 'c6-thm-standard-inner-product', 'c3-thm-column-combination', 'c1-lem-scalar-cancellation'], '7.60', 265, 'example')

s.r('thm-qr-solve', 'Solving a system by QR and backward substitution', r'''Suppose $A=QR$ is a QR factorization with positive diagonal in $R$, and let $b\in\F^n$. Set $c=Q^*b$. The unique solution of $Ax=b$ is obtained recursively, for $j=n,n-1,\ldots,1$, by
\[x_j=\frac{c_j-\sum_{k=j+1}^nR_{jk}x_k}{R_{jj}}.\]''',
r'''Because $Q^*Q=QQ^*=I$, multiplying $QRx=b$ by $Q^*$ gives the equivalent equation $Rx=c$. The last row is $R_{nn}x_n=c_n$, so the displayed formula determines $x_n$. Having determined $x_{j+1},\ldots,x_n$, the $j$th row is
\[R_{jj}x_j+\sum_{k=j+1}^nR_{jk}x_k=c_j.\]
The coefficient $R_{jj}$ is positive and hence nonzero, so there is exactly one value of $x_j$ satisfying that row, namely the stated value. Proceeding downward determines all coordinates, satisfies all rows, and proves uniqueness. For $n=0$, the system has the unique empty vector as its solution, and no recursion steps are required.''',
2, 15, [r'First remove the unitary factor, then solve the last remaining row at each step.'],
['thm-qr', 'thm-unitary-matrix-equivalences', 'c3-def-matrix-product', 'c5-def-upper-triangular', 'c1-def-field'], page=266)

s.r('thm-positive-invertible', 'Strict quadratic positivity characterizes positive invertibility', r'''For a self-adjoint operator $T$, the following are equivalent:
\begin{enumerate}
\item $T$ is positive and invertible.
\item $\ip{Tv}{v}>0$ for every nonzero $v$.
\end{enumerate}''',
r'''Suppose $T$ is positive and invertible. For $v\ne0$, injectivity gives $Tv\ne0$. The zero-quadratic criterion for a positive operator then gives $\ip{Tv}{v}\ne0$. Positivity makes this real number nonnegative, so it is strictly positive.
Conversely, suppose the second condition holds. The value at zero is zero, so all quadratic values are nonnegative. Together with the assumed self-adjointness, this makes $T$ positive. If $Tv=0$ with $v\ne0$, its quadratic value would be zero, contradicting strict positivity. Thus the kernel is $\{0\}$ and $T$ is injective, hence invertible in finite dimensions. On the zero space the strict condition is vacuous; its unique operator is positive and is the invertible identity, so the equivalence remains valid.''',
2, 15, [r'Use the characterization of zero quadratic values for positive operators.'],
['def-positive', 'thm-positive-zero', 'def-self-adjoint', 'c3-thm-injective-null', 'c3-thm-equal-dimension-invertibility', 'c3-thm-invertible-bijective', 'c6-thm-inner-product-properties'], '7.61', 266)

s.d('def-positive-definite', 'Positive definite matrices', r'''A square matrix $B\in\F^{n,n}$ is positive definite if $B^*=B$ and
\[\ip{Bx}{x}>0\quad\text{for every nonzero }x\in\F^n,\]
using the standard inner product. The empty square matrix satisfies this definition, because the nonzero-vector condition is vacuous.''', '7.62', 266)

s.r('thm-cholesky', 'Cholesky factorization', r'''For every positive definite matrix $B\in\F^{n,n}$, there is a unique upper-triangular matrix $R\in\F^{n,n}$ with strictly positive real diagonal entries such that
\[B=R^*R.\]
Conversely, every matrix of this form, with the stated conditions on $R$, is positive definite. The empty matrices give the size-zero case.''',
r'''Let $T$ be the operator on $\F^n$ with standard matrix $B$. The adjoint-matrix criterion makes $T$ self-adjoint, and positive definiteness gives its strict quadratic positivity. Thus $T$ is positive and invertible. Let $P$ be its positive square root, so $P^2=T$ and $P=P^*$. If $Px=0$, then $Tx=P^2x=0$, so $x=0$. Hence $P$ is injective and therefore invertible. Its standard matrix $A$ is invertible and satisfies
\[A^*A=\Mat(P^*P)=\Mat(P^2)=B.\]
In particular its columns are independent: a zero combination of them is an equation $Ax=0$, which forces $x=0$. Apply QR factorization to $A$, writing $A=QR$ with the required triangular and positivity conditions. The conjugate-transpose product rule and unitarity give
\[B=A^*A=R^*Q^*QR=R^*R.\]
This proves existence.

For uniqueness, suppose also $B=H^*H$, where $H$ is upper triangular with positive real diagonal. If $Hx=0$, then
\[\ip{Bx}{x}=\ip{H^*Hx}{x}=\|Hx\|^2=0.\]
Positive definiteness forces $x=0$, so $H$ is invertible by finite-dimensional injectivity. Put $U=AH^{-1}$. Then
\[
\begin{aligned}
U^*U
&=(H^{-1})^*A^*AH^{-1}\\
&=(H^{-1})^*H^*HH^{-1}\\
&=(HH^{-1})^*(HH^{-1})=I.
\end{aligned}
\]
The unitary matrix criterion makes $U$ unitary. Therefore $A=UH$ is another QR factorization with positive triangular diagonal. QR uniqueness implies $H=R$.

For the converse, suppose $R$ has the stated triangular form. Its nonzero diagonal makes its associated operator invertible by the triangular invertibility theorem. The matrix $B=R^*R$ is self-conjugate-transpose by the product and double-transpose rules. For $x\ne0$, invertibility gives $Rx\ne0$, and
\[\ip{Bx}{x}=\ip{R^*Rx}{x}=\|Rx\|^2>0.\]
Thus $B$ is positive definite. All arguments apply in dimension zero using the unique empty matrix, which is its own identity and inverse; the factorization there is unique.''',
4, 60, [r'Write $B=A^*A$ using a positive square root, then apply QR to $A$.', r'If another triangular factor $H$ exists, show that $AH^{-1}$ is unitary and use QR uniqueness.'],
['def-positive-definite', 'thm-self-adjoint-tests', 'thm-adjoint-matrix', 'thm-positive-invertible', 'thm-positive-square-root-unique', 'def-positive-square-root', 'def-positive', 'thm-qr', 'thm-unitary-matrix-equivalences', 'lem-conjugate-transpose-algebra', 'def-adjoint', 'c3-thm-equal-dimension-invertibility', 'c3-thm-matrix-inverse', 'c3-thm-matrix-composition', 'c5-thm-triangular-invertible', 'c6-thm-norm-properties'], '7.63', 267)

s.card('isometry', 'def-isometry',
r'What does a linear isometry preserve?',
r'Norms: $\|Sv\|=\|v\|$ for every vector in its domain.')

s.card('isometry-adjoint', 'thm-isometry-equivalences',
r'What adjoint equation characterizes an isometry $S:V\to W$?',
r'$S^*S=I_V$; there is no requirement that $SS^*=I_W$ for different-dimensional spaces.')

s.card('unitary-inverse', 'thm-unitary-equivalences',
r'What is the inverse of a unitary operator?',
r'Its adjoint: $S^{-1}=S^*$.')

s.card('unitary-eigenvalues', 'thm-unitary-eigenvalues',
r'What modulus must a unitary eigenvalue have?',
r'Every unitary eigenvalue has modulus one.')

s.card('complex-unitary-basis', 'thm-unitary-complex-diagonalization',
r'What orthonormal-basis description characterizes a complex unitary operator?',
r'An orthonormal eigenvector basis with all corresponding eigenvalues of modulus one.')

s.card('qr', 'thm-qr',
r'What conditions make the QR factorization unique?',
r'For a square matrix with independent columns, require $Q$ unitary and $R$ upper triangular with strictly positive real diagonal entries.')

s.card('qr-solve', 'thm-qr-solve',
r'How does $A=QR$ help solve $Ax=b$?',
r'Compute $c=Q^*b$, then solve $Rx=c$ from the last row upward.')

s.card('positive-definite', 'def-positive-definite',
r'What does positive definite mean for a matrix?',
r'$B^*=B$ and $\ip{Bx}{x}>0$ for every nonzero $x$.')

s.card('cholesky', 'thm-cholesky',
r'State the Cholesky factorization of a positive definite matrix.',
r'There is a unique upper-triangular $R$ with positive real diagonal such that $B=R^*R$.')

s.write()
