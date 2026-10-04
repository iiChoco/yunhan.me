from common import Section

s = Section('7a')

s.p('intro-adjoints-normal', 'Adjoints and operator geometry', r'''Throughout this section, all inner product spaces are finite-dimensional over the same field $\F$, and inner products are linear in their first variable. The adjoint moves a linear map from one side of an inner product to the other. We use it to distinguish self-adjoint and normal operators and to study their eigenvectors.''', 228)

s.d('def-adjoint', 'The adjoint of a linear map', r'''For $T\in\Lin(V,W)$, its adjoint is the function $T^*:W\to V$ characterized by
\[\ip{Tv}{w}=\ip{v}{T^*w}\quad(v\in V,\ w\in W).\]
The inner product on the left is taken in $W$, and the one on the right in $V$. Existence and uniqueness of this function are established next.''', '7.1', 228)

s.r('lem-adjoint-existence', 'The adjoint exists and is uniquely determined', r'''For every $T\in\Lin(V,W)$ and every $w\in W$, there is exactly one vector $T^*w\in V$ satisfying the adjoint identity for all $v\in V$. Thus the adjoint is a well-defined function from $W$ to $V$.''',
r'''Fix $w\in W$ and define $\varphi_w(v)=\ip{Tv}{w}$. Linearity of $T$ and linearity in the first inner-product variable give
\[\varphi_w(u+v)=\varphi_w(u)+\varphi_w(v),\qquad
\varphi_w(av)=a\varphi_w(v).\]
Thus $\varphi_w$ is a linear functional on $V$. The finite-dimensional Riesz representation theorem supplies exactly one vector $x\in V$ such that $\varphi_w(v)=\ip v x$ for every $v$. Defining $T^*w=x$ gives the required value. Since this construction works uniquely for every $w$, it defines exactly one function satisfying the identity. Riesz representation includes the zero space, so no positive-dimension assumption is needed.''',
2, 15, [r'For fixed $w$, regard the left side of the adjoint identity as a functional of $v$.'],
['def-adjoint', 'c3-def-linear-map', 'c6-thm-inner-product-properties', 'c6-thm-riesz'], page=228, kind='lemma')

s.r('ex-coordinate-adjoint', 'Computing an adjoint between coordinate spaces', r'''Give $\R^3$ and $\R^2$ their standard inner products and define
\[T(x_1,x_2,x_3)=(x_2+3x_3,2x_1).\]
Then
\[T^*(y_1,y_2)=(2y_2,y_1,3y_1).\]''',
r'''The coordinate formula defines a linear map. For arbitrary $x\in\R^3$ and $y\in\R^2$,
\[
\begin{aligned}
\ip{Tx}{y}
&=(x_2+3x_3)y_1+2x_1y_2\\
&=x_1(2y_2)+x_2y_1+x_3(3y_1)\\
&=\ip{x}{(2y_2,y_1,3y_1)}.
\end{aligned}
\]
Uniqueness in the adjoint identity identifies the second-slot vector with $T^*y$.''',
1, 10, [r'Regroup the scalar expression by the coordinates of the input $x$.'],
['lem-adjoint-existence', 'def-adjoint', 'c3-thm-coordinate-linear-maps', 'c6-thm-standard-inner-product'], '7.2', 228, 'example')

s.r('ex-rank-one-adjoint', 'The adjoint of a one-dimensional-image formula', r'''Fix $u\in V$ and $x\in W$. The formula
\[Tv=\ip v u\,x\]
defines a linear map $V\to W$, and its adjoint satisfies
\[T^*w=\ip w x\,u.\]''',
r'''The functional $v\mapsto\ip v u$ is linear in $v$, so multiplying its values by the fixed vector $x$ gives a linear map. For all $v,w$,
\[
\ip{Tv}{w}=\ip v u\,\ip x w
=\ip v u\,\overline{\ip w x}
=\ip v{\ip w x\,u}.
\]
The last equality uses conjugate linearity in the second variable. Uniqueness of the representing vector gives the displayed adjoint. If $u=0$ or $x=0$, the same calculation gives the zero map and its zero adjoint.''',
1, 10, [r'When moving a scalar into the second inner-product slot, conjugate it.'],
['def-adjoint', 'lem-adjoint-existence', 'c6-thm-inner-product-properties', 'c3-def-linear-map'], '7.3', 229, 'example')

s.r('thm-adjoint-linear', 'The adjoint is a linear map', r'''For $T\in\Lin(V,W)$, its adjoint belongs to $\Lin(W,V)$.''',
r'''Let $w_1,w_2\in W$. For every $v\in V$, additivity in the second inner-product variable gives
\[
\ip{Tv}{w_1+w_2}
=\ip{Tv}{w_1}+\ip{Tv}{w_2}
=\ip v{T^*w_1+T^*w_2}.
\]
Uniqueness in the definition of the adjoint yields $T^*(w_1+w_2)=T^*w_1+T^*w_2$. For $a\in\F$ and $w\in W$,
\[
\ip{Tv}{aw}
=\overline a\,\ip{Tv}{w}
=\overline a\,\ip v{T^*w}
=\ip v{aT^*w}.
\]
The same uniqueness yields $T^*(aw)=aT^*w$. Thus the adjoint satisfies both linearity identities.''',
2, 15, [r'Test the proposed value against every $v$ and use uniqueness of the adjoint value.'],
['def-adjoint', 'lem-adjoint-existence', 'c6-thm-inner-product-properties', 'c3-def-linear-map'], '7.4', 229)

s.r('thm-adjoint-properties', 'Algebraic rules for adjoints', r'''For $T\in\Lin(V,W)$, the following identities hold:
\begin{enumerate}
\item $(R+T)^*=R^*+T^*$ for $R\in\Lin(V,W)$.
\item $(aT)^*=\overline a\,T^*$ for $a\in\F$.
\item $(T^*)^*=T$.
\item $(ST)^*=T^*S^*$ for $S\in\Lin(W,U)$.
\item $I_V^*=I_V$.
\item If $T$ is invertible, then $T^*$ is invertible and $(T^*)^{-1}=(T^{-1})^*$.
\end{enumerate}''',
r'''For the first identity, evaluate at arbitrary $v\in V,w\in W$:
\[
\ip{(R+T)v}{w}
=\ip v{R^*w}+\ip v{T^*w}
=\ip v{(R^*+T^*)w}.
\]
Adjoint uniqueness gives the result. For the scalar identity,
\[
\ip{aTv}{w}
=a\ip v{T^*w}
=\ip v{\overline a\,T^*w},
\]
where taking the conjugate twice justifies the second-slot scalar. Uniqueness again applies.

Conjugate symmetry and the defining identity give
\[
\ip{T^*w}{v}
=\overline{\ip v{T^*w}}
=\overline{\ip{Tv}{w}}
=\ip w{Tv}.
\]
Thus $T$ satisfies the identity defining the adjoint of $T^*$, proving the third assertion. For composition, take $u\in U$ and compute
\[
\ip{STv}{u}=\ip{Tv}{S^*u}=\ip v{T^*S^*u}.
\]
This proves the fourth assertion, with the reversed order and the stated domains. The equation $\ip{I_Vv}{w}=\ip v w$ proves $I_V^*=I_V$.

Finally, if $T:V\to W$ is invertible, take adjoints of $T^{-1}T=I_V$ and $TT^{-1}=I_W$. The product and identity rules just proved give
\[T^*(T^{-1})^*=I_V,\qquad (T^{-1})^*T^*=I_W.\]
Here $T^*:W\to V$ and $(T^{-1})^*:V\to W$, so these are both inverse identities. They prove the final assertion.''',
2, 20, [r'Prove each proposed adjoint formula by checking its inner-product identity.', r'The scalar rule and composition rule change conjugation and order respectively.'],
['def-adjoint', 'lem-adjoint-existence', 'thm-adjoint-linear', 'c6-thm-inner-product-properties', 'c4-thm-complex-properties', 'c3-def-map-inverse', 'c3-def-invertible-map'], '7.5', 230)

s.r('thm-adjoint-range-null', 'Orthogonal complements connect adjoint ranges and null spaces', r'''For $T\in\Lin(V,W)$,
\[
\begin{aligned}
\Null T^*&=(\Range T)^\perp \quad\text{in }W,\\
\Range T^*&=(\Null T)^\perp \quad\text{in }V,\\
\Null T&=(\Range T^*)^\perp \quad\text{in }V,\\
\Range T&=(\Null T^*)^\perp \quad\text{in }W.
\end{aligned}
\]''',
r'''For $w\in W$, the condition $T^*w=0$ implies $\ip v{T^*w}=0$ for every $v$. Conversely, if all these inner products vanish, choosing $v=T^*w$ gives $\|T^*w\|^2=0$, hence $T^*w=0$. By the adjoint identity, these equivalent conditions are the same as $\ip{Tv}{w}=0$ for every $v\in V$. Conjugate symmetry makes this exactly orthogonality of $w$ to $\Range T$. Thus $\Null T^*=(\Range T)^\perp$.
The range is a subspace of a finite-dimensional inner product space. Taking orthogonal complements and using the double-complement theorem gives $(\Null T^*)^\perp=\Range T$, proving the fourth formula.
Apply the first formula to $T^*$ and use $(T^*)^*=T$ to obtain $\Null T=(\Range T^*)^\perp$, the third formula. Taking complements of this equality gives $(\Null T)^\perp=\Range T^*$, the second formula. All ambient spaces are specified in the statement, and the double-complement theorem includes zero subspaces.''',
2, 20, [r'Prove the first identity directly, then take orthogonal complements and replace $T$ by $T^*$.'],
['def-adjoint', 'thm-adjoint-properties', 'c3-def-null-space', 'c3-def-range', 'c3-thm-range-subspace', 'c6-def-orthogonal-complement', 'c6-thm-double-orthogonal', 'c6-thm-inner-product-properties', 'c6-thm-norm-properties'], '7.6', 231)

s.d('def-conjugate-transpose', 'The conjugate transpose of a matrix', r'''For $A\in\F^{m,n}$, its conjugate transpose $A^*\in\F^{n,m}$ is defined by
\[(A^*)_{jk}=\overline{A_{kj}}.\]
For real matrices this is the ordinary transpose. The definition also applies when a dimension is zero.''', '7.7', 231)

s.r('ex-conjugate-transpose', 'Conjugating after exchanging rows and columns', r'''For
\[A=\begin{pmatrix}2&3+4i&7\\6&5&8i\end{pmatrix},\]
its conjugate transpose is
\[A^*=\begin{pmatrix}2&6\\3-4i&5\\7&-8i\end{pmatrix}.\]''',
r'''The first row of $A$ becomes the first column after conjugating its entries, giving $(2,3-4i,7)$. The second row becomes the second column after conjugation, giving $(6,5,-8i)$. These two columns form the displayed $3$-by-$2$ matrix.''',
1, 10, [r'The $j$th row becomes the $j$th column, and each entry is conjugated.'],
['def-conjugate-transpose', 'c4-def-conjugate-modulus'], '7.8', 231, 'example')

s.r('thm-adjoint-matrix', 'Adjoint matrices in orthonormal bases', r'''Let $\mathcal E=(e_1,\ldots,e_n)$ and $\mathcal F=(f_1,\ldots,f_m)$ be orthonormal bases of $V,W$, respectively. For $T\in\Lin(V,W)$,
\[\Mat(T^*,\mathcal F,\mathcal E)=\Mat(T,\mathcal E,\mathcal F)^*.\]''',
r'''Set $A=\Mat(T,\mathcal E,\mathcal F)$ and $B=\Mat(T^*,\mathcal F,\mathcal E)$. Orthonormal coordinate extraction gives
\[A_{kj}=\ip{Te_j}{f_k},\qquad B_{jk}=\ip{T^*f_k}{e_j}.\]
Conjugate symmetry and the adjoint identity imply
\[
B_{jk}=\overline{\ip{e_j}{T^*f_k}}
=\overline{\ip{Te_j}{f_k}}
=\overline{A_{kj}}.
\]
Thus every entry of $B$ equals the corresponding entry of $A^*$, proving the identity. If either basis is empty, the two matrices have the same empty shape and the equality remains valid.''',
2, 15, [r'Express each matrix entry as an inner product with the corresponding orthonormal basis vector.'],
['def-conjugate-transpose', 'def-adjoint', 'c3-def-map-matrix', 'c6-thm-orthonormal-coordinates', 'c6-thm-inner-product-properties'], '7.9', 232)

s.r('ex-nonorthonormal-adjoint', 'Why the matrix formula needs orthonormal bases', r'''On $\R^2$ with its standard inner product, let $T(x,y)=(y,0)$ and use the basis $\mathcal B=((1,0),(0,2))$. Prove that
\[\Mat(T,\mathcal B)=\begin{pmatrix}0&2\\0&0\end{pmatrix},
\qquad
\Mat(T^*,\mathcal B)=\begin{pmatrix}0&0\\1/2&0\end{pmatrix}.
\]
Thus the matrix of the adjoint need not be the transpose in a nonorthonormal basis.''',
r'''For $v=(x,y)$ and $w=(a,b)$,
\[\ip{Tv}{w}=ya=\ip{(x,y)}{(0,a)},\]
so adjoint uniqueness gives $T^*(a,b)=(0,a)$. If the basis vectors are $b_1=(1,0)$ and $b_2=(0,2)$, then $Tb_1=0$ and $Tb_2=2b_1$, giving the first matrix. Also $T^*b_1=(0,1)=b_2/2$ and $T^*b_2=0$, giving the second matrix. The transpose of the first matrix has entry $2$ in row two, column one, whereas the second matrix has entry $1/2$ there. They differ. The basis fails to be orthonormal because $b_2$ has norm $2$.''',
2, 15, [r'Compute the adjoint using the inner product before changing coordinates.'],
['def-adjoint', 'lem-adjoint-existence', 'c3-def-map-matrix', 'c6-thm-standard-inner-product', 'c6-def-norm'], page=232, kind='example')

s.d('def-self-adjoint', 'Self-adjoint operators', r'''An operator $T\in\Lin(V)$ is self-adjoint if $T=T^*$.''', '7.10', 233)

s.r('thm-self-adjoint-tests', 'Equivalent tests for self-adjointness', r'''For $T\in\Lin(V)$, self-adjointness is equivalent to
\[\ip{Tv}{w}=\ip v{Tw}\quad(v,w\in V).\]
For any orthonormal basis $\mathcal E$, it is also equivalent to
\[\Mat(T,\mathcal E)=\Mat(T,\mathcal E)^*.\]''',
r'''If $T=T^*$, the adjoint identity gives the displayed inner-product equation. Conversely, if that equation holds for all $v,w$, then for each fixed $w$ the vector $Tw$ satisfies the identity uniquely defining $T^*w$. Thus $Tw=T^*w$ for every $w$, so $T=T^*$.
In an orthonormal basis, the adjoint-matrix theorem identifies $\Mat(T^*,\mathcal E)$ with $\Mat(T,\mathcal E)^*$. Two linear maps have the same matrix in fixed bases exactly when their values agree on every basis vector, which is equivalent to equality of the maps. Thus equality with the conjugate transpose is equivalent to $T=T^*$.''',
1, 10, [r'Use uniqueness of the adjoint in the inner-product test and uniqueness of basis coordinates in the matrix test.'],
['def-self-adjoint', 'def-adjoint', 'lem-adjoint-existence', 'thm-adjoint-matrix', 'c3-def-map-matrix', 'c3-thm-linear-map-basis'], page=233)

s.r('ex-self-adjoint-parameter', 'A matrix parameter determined by self-adjointness', r'''For the standard inner product on $\F^2$, an operator with standard matrix
\[\begin{pmatrix}2&c\\3&7\end{pmatrix}\]
is self-adjoint exactly when $c=3$.''',
r'''The standard basis is orthonormal. The conjugate transpose of the displayed matrix is
\[\begin{pmatrix}2&3\\\overline c&7\end{pmatrix}.\]
Equality of these matrices requires $c=3$ from their top-right entries. This value also gives $\overline c=3$, so it makes the bottom-left entries agree as well. The diagonal entries already agree. The matrix criterion therefore gives precisely $c=3$.''',
1, 10, [r'Compare the two off-diagonal entries after conjugate transposition.'],
['thm-self-adjoint-tests', 'def-conjugate-transpose', 'c6-thm-standard-inner-product'], '7.11', 233, 'example')

s.r('thm-self-adjoint-eigenvalues', 'Eigenvalues of a self-adjoint operator are real', r'''Every eigenvalue of a self-adjoint operator is real.''',
r'''Let $Tv=\lambda v$ with $v\ne0$. Self-adjointness and the inner-product scalar rules give
\[
\lambda\|v\|^2
=\ip{\lambda v}{v}
=\ip{Tv}{v}
=\ip v{Tv}
=\ip v{\lambda v}
=\overline\lambda\|v\|^2.
\]
Since $v\ne0$, positive definiteness gives $\|v\|^2>0$. Cancelling this real scalar yields $\lambda=\overline\lambda$, which is equivalent to $\lambda$ being real. If the space has no eigenvalues, the assertion has no instances to check.''',
1, 10, [r'Compute $\ip{Tv}{v}$ using the eigenvector equation and then self-adjointness.'],
['def-self-adjoint', 'thm-self-adjoint-tests', 'c5-def-eigenvalue', 'c6-thm-inner-product-properties', 'c6-thm-norm-properties', 'c4-thm-complex-properties'], '7.12', 233)

s.r('ex-real-quadratic-counterexample', 'A nonzero real operator with zero quadratic values', r'''On $\R^2$ with its standard inner product, the operator $J(x,y)=(-y,x)$ is nonzero and satisfies $\ip{Jv}{v}=0$ for every $v$. It is not self-adjoint.''',
r'''For $v=(x,y)$,
\[\ip{Jv}{v}=(-y)x+xy=0.\]
But $J(1,0)=(0,1)\ne0$, so $J$ is nonzero. Its standard matrix is
\[\begin{pmatrix}0&-1\\1&0\end{pmatrix},\]
whose transpose is its negative and is different from it. The standard basis is orthonormal, so the self-adjoint matrix criterion proves that $J$ is not self-adjoint. In particular, real quadratic values alone do not characterize self-adjointness on a real space: all such inner-product values are real, including this example.''',
1, 10, [r'Compute the quadratic expression directly and compare the standard matrix with its transpose.'],
['c6-thm-standard-inner-product', 'thm-self-adjoint-tests', 'def-conjugate-transpose', 'c3-def-map-matrix'], page=234, kind='example')

s.r('thm-zero-quadratic-complex', 'Vanishing complex quadratic values force the operator to vanish', r'''For an operator on a complex inner product space,
\[\ip{Tv}{v}=0\text{ for every }v\quad\Longleftrightarrow\quad T=0.\]''',
r'''The zero operator has zero quadratic values. Conversely, suppose all those values vanish. For arbitrary $u,w$, expand the value at $u+w$. The two diagonal terms vanish, leaving
\[\ip{Tu}{w}+\ip{Tw}{u}=0.\]
Expand instead at $u+iw$. Linearity of $T$, linearity in the first slot, and conjugate linearity in the second give
\[
0=\ip{T(u+iw)}{u+iw}
=-i\ip{Tu}{w}+i\ip{Tw}{u}.
\]
Writing $a=\ip{Tu}{w}$ and $b=\ip{Tw}{u}$, the first equation says $a+b=0$ and the second says $b-a=0$. Hence $2a=0$, so $a=0$. Thus $\ip{Tu}{w}=0$ for all $u,w$. Choosing $w=Tu$ gives $\|Tu\|^2=0$, so $Tu=0$ for every $u$. Therefore $T=0$.''',
3, 30, [r'Compare the assumed identity at $u+w$ and at $u+iw$.', r'These two choices separate the two mixed inner-product terms.'],
['c3-def-linear-map', 'c6-thm-inner-product-properties', 'c6-thm-norm-properties', 'c1-def-complex'], '7.13', 234)

s.r('thm-self-adjoint-quadratic', 'Real quadratic values characterize complex self-adjointness', r'''For an operator on a complex inner product space,
\[T=T^*\quad\Longleftrightarrow\quad
\ip{Tv}{v}\in\R\text{ for every }v.\]''',
r'''For every $v$, the adjoint identity and conjugate symmetry give
\[\ip{T^*v}{v}
=\overline{\ip v{T^*v}}
=\overline{\ip{Tv}{v}}.\]
If $T=T^*$, the number $\ip{Tv}{v}$ therefore equals its conjugate, so it is real. Conversely, suppose all the quadratic values are real. The displayed identity gives
\[\ip{(T-T^*)v}{v}
=\ip{Tv}{v}-\overline{\ip{Tv}{v}}=0\]
for every $v$. The complex zero-quadratic theorem applied to the linear operator $T-T^*$ implies $T-T^*=0$. Thus $T$ is self-adjoint.''',
2, 20, [r'Apply the previous result to $T-T^*$.'],
['def-self-adjoint', 'def-adjoint', 'thm-adjoint-linear', 'thm-zero-quadratic-complex', 'c6-thm-inner-product-properties', 'c4-thm-complex-properties', 'c3-thm-linear-map-space'], '7.14', 234)

s.r('thm-zero-self-adjoint-quadratic', 'Vanishing quadratic values for a self-adjoint operator', r'''Over either $\R$ or $\C$, a self-adjoint operator satisfies
\[\ip{Tv}{v}=0\text{ for every }v\quad\Longleftrightarrow\quad T=0.\]''',
r'''The zero operator has the stated values. If the field is complex, the converse follows from the complex zero-quadratic theorem without any further assumption. Suppose the field is real and every quadratic value vanishes. Expanding at $u+w$ gives
\[0=\ip{Tu}{w}+\ip{Tw}{u},\]
because the diagonal terms vanish. Self-adjointness gives $\ip{Tw}{u}=\ip w{Tu}$, and symmetry of a real inner product gives $\ip w{Tu}=\ip{Tu}{w}$. Therefore $2\ip{Tu}{w}=0$ for every $u,w$. Taking $w=Tu$ yields $\|Tu\|^2=0$, hence $Tu=0$. Thus $T=0$ in the real case as well.''',
2, 20, [r'Over $\R$, use self-adjointness to make the two mixed terms in the expansion at $u+w$ equal.'],
['def-self-adjoint', 'thm-self-adjoint-tests', 'thm-zero-quadratic-complex', 'c6-thm-inner-product-properties', 'c6-thm-norm-properties'], '7.16', 235)

s.d('def-normal', 'Normal operators', r'''An operator $T\in\Lin(V)$ is normal if it commutes with its adjoint:
\[TT^*=T^*T.\]''', '7.18', 235)

s.r('thm-self-adjoint-normal', 'Self-adjoint operators are normal', r'''Every self-adjoint operator is normal.''',
r'''For a self-adjoint operator, $T^*=T$. Hence both $TT^*$ and $T^*T$ equal $T^2$, which is the defining equality for normality.''',
1, 10, [r'Substitute $T^*=T$.'],
['def-self-adjoint', 'def-normal'], page=235)

s.r('ex-normal-not-self-adjoint', 'Normality does not require self-adjointness', r'''On $\F^2$ with the standard inner product, the operator with matrix
\[A=\begin{pmatrix}2&-3\\3&2\end{pmatrix}\]
is normal but is not self-adjoint.''',
r'''The adjoint matrix in the standard orthonormal basis is
\[A^*=\begin{pmatrix}2&3\\-3&2\end{pmatrix},\]
which differs from $A$, so the operator is not self-adjoint. Multiplication gives
\[
AA^*=\begin{pmatrix}4+9&6-6\\6-6&9+4\end{pmatrix}
=\begin{pmatrix}13&0\\0&13\end{pmatrix}
\]
and
\[
A^*A=\begin{pmatrix}4+9&-6+6\\-6+6&9+4\end{pmatrix}
=\begin{pmatrix}13&0\\0&13\end{pmatrix}.
\]
Matrices of compositions are products, and fixed-basis matrices determine their maps. Thus $TT^*=T^*T$, proving normality over either scalar field.''',
2, 15, [r'Compare the two products with the conjugate transpose.'],
['def-normal', 'thm-self-adjoint-tests', 'thm-adjoint-matrix', 'def-conjugate-transpose', 'c3-thm-matrix-composition', 'c3-thm-linear-map-basis', 'c6-thm-standard-inner-product'], '7.19', 235, 'example')

s.r('thm-normal-norm', 'Normality is equality of two output norms', r'''For $T\in\Lin(V)$,
\[T\text{ is normal}\quad\Longleftrightarrow\quad
\|Tv\|=\|T^*v\|\text{ for every }v\in V.\]''',
r'''Set $D=T^*T-TT^*$. The adjoint rules give
\[(T^*T)^*=T^*(T^*)^*=T^*T,\qquad
(TT^*)^*=(T^*)^*T^*=TT^*.\]
Since the scalar $-1$ is real, the sum and scalar rules therefore give $D^*=D$. Thus $D$ is self-adjoint. Using the adjoint identity for $T^*$ and for $T$,
\[
\ip{Dv}{v}
=\ip{T^*Tv}{v}-\ip{TT^*v}{v}
=\ip{Tv}{Tv}-\ip{T^*v}{T^*v}
=\|Tv\|^2-\|T^*v\|^2.
\]
Normality means $D=0$, which implies equality of these squared norms and hence of the nonnegative norms. Conversely, equality of norms makes $\ip{Dv}{v}=0$ for every $v$. The zero-quadratic theorem for self-adjoint operators gives $D=0$, which is normality. This argument works over both fields.''',
2, 20, [r'Consider the self-adjoint operator $T^*T-TT^*$.'],
['def-normal', 'thm-adjoint-properties', 'def-adjoint', 'thm-zero-self-adjoint-quadratic', 'c6-def-norm', 'c6-thm-norm-properties'], '7.20', 236)

s.r('thm-normal-properties', 'Null spaces, ranges, shifts, and eigenvectors of normal operators', r'''If $T\in\Lin(V)$ is normal, then:
\begin{enumerate}
\item $\Null T=\Null T^*$.
\item $\Range T=\Range T^*$.
\item $V=\Null T\oplus\Range T$, and the two summands are orthogonal.
\item $T-\lambda I$ is normal for every $\lambda\in\F$.
\item For every $v\in V$ and $\lambda\in\F$,
\[Tv=\lambda v\quad\Longleftrightarrow\quad T^*v=\overline\lambda v.\]
\end{enumerate}''',
r'''By equality of the two output norms, $Tv=0$ exactly when $T^*v=0$. This proves the first assertion. The adjoint range identities then give
\[\Range T=(\Null T^*)^\perp=(\Null T)^\perp=\Range T^*.\]
They also identify the orthogonal decomposition
\[V=\Null T\oplus(\Null T)^\perp\]
with the asserted null-space and range decomposition.

For a scalar $\lambda$, the adjoint rules give
\[(T-\lambda I)^*=T^*-\overline\lambda I.\]
Expanding both possible products gives
\[
\begin{aligned}
(T-\lambda I)(T^*-\overline\lambda I)
&=TT^*-\overline\lambda T-\lambda T^*+|\lambda|^2I,\\
(T^*-\overline\lambda I)(T-\lambda I)
&=T^*T-\lambda T^*-\overline\lambda T+|\lambda|^2I.
\end{aligned}
\]
These agree because $T$ is normal. Thus $T-\lambda I$ is normal.
Finally, the first assertion applied to this shifted operator yields
\[\Null(T-\lambda I)=\Null(T^*-\overline\lambda I).\]
Membership in these two kernels is precisely the two equations in the last assertion, proving their equivalence even when $v=0$.''',
3, 35, [r'First use equality of norms to identify the kernels.', r'Apply the adjoint range identities and then repeat the kernel argument for $T-\lambda I$.'],
['def-normal', 'thm-normal-norm', 'thm-adjoint-range-null', 'thm-adjoint-properties', 'c6-thm-orthogonal-direct-sum', 'c6-thm-norm-properties', 'c3-thm-null-subspace', 'c3-def-null-space', 'c3-thm-composition-laws', 'c4-thm-complex-properties'], '7.21', 237)

s.r('thm-normal-orthogonal-eigenvectors', 'Different eigenvalues of a normal operator give orthogonal eigenvectors', r'''If $T$ is normal and $u,v$ are eigenvectors corresponding to distinct eigenvalues $\alpha,\beta$, then $\ip u v=0$.''',
r'''The eigenvector equations are $Tu=\alpha u$ and $Tv=\beta v$. The normal-operator property gives $T^*v=\overline\beta v$. Consequently,
\[
\alpha\ip u v
=\ip{Tu}{v}
=\ip u{T^*v}
=\ip u{\overline\beta v}
=\beta\ip u v.
\]
The final scalar is $\beta$, because the second inner-product slot conjugates $\overline\beta$. Thus $(\alpha-\beta)\ip u v=0$. Since the eigenvalues are distinct, scalar cancellation gives $\ip u v=0$, which is orthogonality.''',
1, 10, [r'Use the adjoint eigenvector equation for the vector in the second slot.'],
['thm-normal-properties', 'def-adjoint', 'c5-def-eigenvector', 'c6-thm-inner-product-properties', 'c1-lem-scalar-cancellation'], '7.22', 238)

s.r('thm-normal-real-imaginary', 'Normality and commuting self-adjoint parts', r'''On a complex inner product space, every operator has a unique expression
\[T=A+iB\]
with $A,B$ self-adjoint, namely
\[A=\frac{T+T^*}{2},\qquad B=\frac{T-T^*}{2i}.\]
The operator $T$ is normal if and only if these two parts commute. Equivalently, $T$ is normal if and only if it can be written as $A+iB$ for commuting self-adjoint operators $A,B$.''',
r'''The adjoint rules give
\[A^*=\frac{T^*+T}{2}=A.\]
Since $\overline{1/(2i)}=-1/(2i)$, they also give
\[B^*=-\frac{T^*-T}{2i}=B.\]
Direct substitution yields $A+iB=T$. If $T=C+iD$ with $C,D$ self-adjoint, then taking adjoints gives $T^*=C-iD$. Adding and subtracting these two equations forces $C=(T+T^*)/2=A$ and $D=(T-T^*)/(2i)=B$. This proves uniqueness.

For these specific parts, distributivity gives
\[
\begin{aligned}
AB-BA
&=\frac{(T+T^*)(T-T^*)-(T-T^*)(T+T^*)}{4i}\\
&=\frac{-2TT^*+2T^*T}{4i}
=\frac{T^*T-TT^*}{2i}.
\end{aligned}
\]
The numerator vanishes exactly when $T$ is normal. Since $2i\ne0$, the displayed equality shows that $AB=BA$ exactly in that case. Together with existence and uniqueness of the self-adjoint decomposition, this proves both formulations of the criterion.''',
3, 30, [r'Add and subtract $T$ and $T^*$ to define the two parts.', r'Expand their commutator without assuming its factors commute.'],
['def-self-adjoint', 'def-normal', 'thm-adjoint-properties', 'c3-thm-composition-laws', 'c3-thm-linear-map-space', 'c4-thm-complex-properties'], '7.23', 238)

s.card('adjoint-identity', 'def-adjoint',
r'What identity defines the adjoint of $T:V\to W$?',
r'$T^*:W\to V$ satisfies $\ip{Tv}{w}=\ip v{T^*w}$ for every $v\in V,w\in W$.')

s.card('adjoint-scalars-order', 'thm-adjoint-properties',
r'How do adjoints treat scalar multiples and products?',
r'$(aT)^*=\overline a\,T^*$ and $(ST)^*=T^*S^*$.')

s.card('adjoint-range-kernel', 'thm-adjoint-range-null',
r'How are the range of a map and the kernel of its adjoint related?',
r'$\Null T^*=(\Range T)^\perp$ and $\Range T=(\Null T^*)^\perp$.')

s.card('adjoint-matrix-bases', 'thm-adjoint-matrix',
r'Under what basis hypothesis is the matrix of the adjoint the conjugate transpose?',
r'The chosen bases of both domain and target must be orthonormal.')

s.card('self-adjoint-eigenvalues', 'thm-self-adjoint-eigenvalues',
r'What restriction does self-adjointness place on eigenvalues?',
r'Every eigenvalue is real.')

s.card('complex-quadratic-zero', 'thm-zero-quadratic-complex',
r'Why does the complex zero-quadratic theorem use both $u+w$ and $u+iw$?',
r'The two expansions give independent equations for the two mixed inner-product terms.')

s.card('normal-norm', 'thm-normal-norm',
r'What norm identity characterizes a normal operator?',
r'$\|Tv\|=\|T^*v\|$ for every $v$.')

s.card('normal-adjoint-eigenvectors', 'thm-normal-properties',
r'If $T$ is normal and $Tv=\lambda v$, what is $T^*v$?',
r'$T^*v=\overline\lambda v$.')

s.card('normal-orthogonality', 'thm-normal-orthogonal-eigenvectors',
r'How are eigenvectors for distinct eigenvalues of a normal operator related?',
r'They are orthogonal.')

s.card('normal-real-imaginary', 'thm-normal-real-imaginary',
r'What are the self-adjoint parts of a complex operator, and when do they commute?',
r'$A=(T+T^*)/2$ and $B=(T-T^*)/(2i)$; they commute exactly when $T$ is normal.')

s.write()
