from common import Section

s = Section('5b')

s.p(
    'intro-minimal-polynomials',
    'Polynomial equations satisfied by operators',
    r'''Over the complex numbers, a polynomial relation among successive images of one vector produces an eigenvector. We then seek polynomial relations that hold on every vector, leading to a distinguished polynomial attached to a finite-dimensional operator.''',
    143
)

s.r(
    'thm-complex-eigenvalue',
    'Existence of an eigenvalue over the complex numbers',
    r'''Every operator on a nonzero finite-dimensional complex vector space has an eigenvalue.''',
    r'''Let $n=\dim V>0$, let $T\in\Lin(V)$, and choose $v\ne0$. The list
\[
v,Tv,\ldots,T^nv
\]
has length $n+1$ and is therefore dependent. Hence there is a nonzero polynomial $p$ with $p(T)v=0$. Among all nonzero polynomials with this property, choose one of smallest degree; such a degree exists because nonnegative integers have a least element in every nonempty subset.

This polynomial cannot be a nonzero constant. Indeed, if $p(z)=a\ne0$, then $p(T)v=av=0$ would imply $v=a^{-1}0=0$, contrary to the choice of $v$. Thus $p$ is nonconstant.

The fundamental theorem of algebra gives a scalar $\lambda\in\C$ with $p(\lambda)=0$. Divide $p$ by $z-\lambda$. The remainder is constant and, on evaluating the division identity at $\lambda$, equals $p(\lambda)=0$. Consequently
\[
p(z)=(z-\lambda)q(z)
\]
for a nonzero polynomial $q$ with $\deg q=\deg p-1$. Minimality of the degree of $p$ implies $q(T)v\ne0$. The product rule for operator evaluation gives
\[
0=p(T)v=(T-\lambda I)q(T)v.
\]
Thus the nonzero vector $q(T)v$ satisfies
$T(q(T)v)=\lambda q(T)v$, proving that $\lambda$ is an eigenvalue.''',
    3, 35,
    [
        r'Find a polynomial relation among $v,Tv,\ldots,T^nv$ for a nonzero vector $v$.',
        r'Choose such a nonzero polynomial of smallest degree and factor out one complex root.',
        r'The remaining polynomial applied to $v$ must give a nonzero vector.'
    ],
    ['def-eigenvalue', 'def-polynomial-operator',
     'thm-polynomial-evaluation-product',
     'c2-thm-independent-length', 'c2-thm-basis-existence',
     'c2-def-dimension', 'c2-def-linear-dependence',
     'c4-thm-fundamental-algebra', 'c4-thm-polynomial-division',
     'c4-lem-polynomial-product-degree', 'c1-foundations'],
    number='5.19', page=143
)

s.r(
    'ex-complex-infinite-no-eigenvalue',
    'A complex polynomial operator without eigenvalues',
    r'''On $\Poly(\C)$, define $(Tp)(z)=zp(z)$. Prove that $T$ is an operator with no eigenvalues. Explain why this does not contradict finite-dimensional complex eigenvalue existence.''',
    r'''Multiplication by a fixed polynomial is linear, so multiplication by $z$ is an operator on $\Poly(\C)$.

Suppose $p\ne0$, and write $d=\deg p$. The product-degree formula shows that $Tp=zp$ is nonzero of degree $d+1$. If $\lambda=0$, then $\lambda p=0$ cannot equal $Tp$. If $\lambda\ne0$, the polynomial $\lambda p$ has degree $d$, since its leading coefficient is the nonzero leading coefficient of $p$ multiplied by the nonzero scalar $\lambda$. It again cannot equal $Tp$, whose degree is $d+1$. Thus no nonzero polynomial satisfies $Tp=\lambda p$ for any scalar $\lambda$, so there are no eigenvalues.

The polynomial space $\Poly(\C)$ is infinite-dimensional by the earlier polynomial-space result. The finite-dimensional eigenvalue theorem therefore does not apply to this operator.''',
    2, 20,
    [
        r'Compare degrees, separating the scalar $\lambda=0$ from nonzero scalars.'
    ],
    ['def-eigenvalue', 'c3-ex-polynomial-multiplication',
     'c4-lem-polynomial-product-degree', 'c2-def-degree',
     'c2-thm-polynomials-infinite', 'thm-complex-eigenvalue'],
    number='5.20', page=143, kind='example'
)

s.d(
    'def-monic',
    'Monic polynomials',
    r'''A nonzero polynomial is \emph{monic} if the coefficient of its highest power is $1$. In particular, the constant polynomial $1$ is monic; the zero polynomial is not monic.''',
    '5.21', 144
)

s.r(
    'ex-monic-polynomial',
    'Reading the leading coefficient',
    r'''Prove that $2+9z^2+z^7$ is a monic polynomial of degree $7$.''',
    r'''Its coefficient at exponent $7$ is $1\ne0$, and every coefficient at a higher exponent is zero. The degree is therefore $7$. The highest-degree coefficient is $1$, so the polynomial is monic by definition.''',
    1, 10,
    [r'Inspect the highest exponent with a nonzero coefficient.'],
    ['def-monic', 'c2-def-degree'],
    page=144, kind='example'
)

s.r(
    'lem-restriction-polynomial',
    'Polynomial evaluation commutes with invariant restriction',
    r'''Let $U$ be a subspace invariant under $T\in\Lin(V)$, and write $S=T|_U$. For every polynomial $p$ and every $u\in U$,
\[
p(S)u=p(T)u.
\]
In particular, $U$ is invariant under $p(T)$, and $p(T)|_U=p(T|_U)$.''',
    r'''We first prove $S^ku=T^ku$ for every nonnegative integer $k$ and $u\in U$. At $k=0$, both sides equal $u$, because the identity of $U$ and the identity of $V$ act identically on $u$. Suppose the equality holds for $k$. The vector $S^ku$ belongs to $U$, and $S$ agrees with $T$ there. Hence
\[
S^{k+1}u=S(S^ku)=T(T^ku)=T^{k+1}u.
\]
This proves the power assertion by induction.

For $p(z)=\sum_{k=0}^{m}a_kz^k$, it follows that
\[
p(S)u=\sum_{k=0}^{m}a_kS^ku
=\sum_{k=0}^{m}a_kT^ku=p(T)u.
\]
The left side belongs to $U$, since $p(S)$ is an operator on $U$. Thus $p(T)$ preserves $U$, and the equality at every input in $U$ proves the restriction identity. The argument includes $U=\{0\}$ and the zero polynomial.''',
    2, 15,
    [
        r'First compare the powers of $T$ and its restriction on inputs from $U$.'
    ],
    ['def-invariant', 'def-operator-powers',
     'lem-operator-power-laws', 'def-polynomial-operator',
     'thm-polynomial-evaluation-linear'],
    page=144, kind='lemma'
)

s.r(
    'thm-minimal-polynomial-existence',
    'Existence, uniqueness, and the degree bound',
    r'''For an operator $T$ on a finite-dimensional vector space $V$, there is a unique monic polynomial of smallest degree among those satisfying $p(T)=0$. Its degree is at most $\dim V$. On the zero space this polynomial is $1$.''',
    r'''We first prove by induction on $n=\dim V$ that some monic polynomial of degree at most $n$ annihilates $T$.

If $n=0$, the identity operator and the zero operator are the same map: both send the only vector to zero. Thus the constant polynomial $1$ evaluates to zero and has degree $0$.

Now let $n>0$ and assume the asserted existence bound for operators on all spaces of smaller dimension. Choose $u\ne0$. The list $u,Tu,\ldots,T^nu$ is dependent, while the one-vector list $u$ is independent. Let $m$ be the smallest positive integer for which
$u,Tu,\ldots,T^mu$ is dependent. Then $1\le m\le n$, and
$u,Tu,\ldots,T^{m-1}u$ is independent. In a nontrivial relation on the longer list, the coefficient of $T^mu$ must be nonzero; otherwise the preceding independent list would have a nontrivial relation. Dividing by that coefficient produces scalars $c_0,\ldots,c_{m-1}$ such that
\[
c_0u+c_1Tu+\cdots+c_{m-1}T^{m-1}u+T^mu=0.
\]
Set $q(z)=c_0+c_1z+\cdots+c_{m-1}z^{m-1}+z^m$. This polynomial is monic of degree $m$ and satisfies $q(T)u=0$.

For every $k\ge0$, polynomial commutation gives
\[
q(T)T^ku=T^kq(T)u=T^k0=0.
\]
Thus the independent list $u,Tu,\ldots,T^{m-1}u$ lies in $\Null q(T)$. Comparing it with a basis of that null space gives $\dim\Null q(T)\ge m$. Rank-nullity consequently yields
\[
\dim\Range q(T)
=n-\dim\Null q(T)\le n-m<n.
\]
Put $R=\Range q(T)$. This subspace is invariant under $T$ by polynomial invariance. The induction hypothesis applied to $T|_R$ supplies a monic polynomial $s$ with
\[
\deg s\le\dim R\le n-m,\qquad s(T|_R)=0.
\]
For each $v\in V$, the vector $q(T)v$ belongs to $R$. The restriction-evaluation lemma therefore gives
\[
(sq)(T)v=s(T)q(T)v=s(T|_R)(q(T)v)=0.
\]
The product $sq$ is monic: its leading coefficient is the product $1\cdot1$. Its degree is $\deg s+m\le n$ by the product-degree formula. This completes the induction.

The set of degrees of monic annihilating polynomials is now nonempty. Choose its least member and a monic annihilating polynomial $p$ of that degree. The existence bound already proved implies $\deg p\le\dim V$.

For uniqueness, suppose $r$ is another monic annihilating polynomial of that same least degree. Their leading terms cancel, and linearity of evaluation gives $(p-r)(T)=0$. If $p-r\ne0$, its degree is smaller than $\deg p$. Dividing it by its nonzero leading coefficient would produce a monic annihilating polynomial of smaller degree, a contradiction. Hence $p=r$.

On the zero space, the degree-zero monic polynomial $1$ annihilates the operator. No nonzero polynomial has smaller degree, and $1$ is the only monic constant, proving the last assertion.''',
    4, 75,
    [
        r'Use induction on the dimension and first find a monic polynomial that annihilates one nonzero vector.',
        r'If its degree is $m$, its null space contains an independent list of length $m$. Apply induction on its invariant range.',
        r'For uniqueness, subtract two monic annihilating polynomials of the same least degree.'
    ],
    ['def-monic', 'def-polynomial-operator',
     'thm-polynomial-evaluation-linear', 'thm-polynomial-evaluation-product',
     'thm-polynomial-invariant', 'lem-restriction-polynomial',
     'c2-def-linear-dependence', 'c2-ex-single-independent',
     'c2-thm-independent-length', 'c2-thm-basis-existence',
     'c2-thm-subspaces-finite', 'c2-def-dimension',
     'c3-thm-null-subspace', 'c3-thm-range-subspace',
     'c3-thm-rank-nullity', 'c3-thm-linear-zero',
     'c4-lem-polynomial-product-degree', 'c1-foundations'],
    number='5.22', page=144
)

s.d(
    'def-minimal-polynomial',
    'Minimal polynomial',
    r'''For an operator $T$ on a finite-dimensional space, its \emph{minimal polynomial} is the unique monic polynomial of least degree that evaluates to the zero operator at $T$. The preceding theorem guarantees its existence and uniqueness; for the zero space it is the constant polynomial $1$.''',
    '5.24', 145
)

s.r(
    'thm-minimal-coefficient-system',
    'Computing the minimal polynomial from operator powers',
    r'''Suppose $n=\dim V>0$. The degree of the minimal polynomial of $T$ is the smallest positive integer $m$ for which there are scalars $c_0,\ldots,c_{m-1}$ satisfying
\[
c_0I+c_1T+\cdots+c_{m-1}T^{m-1}=-T^m.
\]
This smallest $m$ is at most $n$, and at that value the coefficient list is unique. For a fixed basis and $A=\Mat(T)$, the displayed equation is equivalent to
\[
c_0I_n+c_1A+\cdots+c_{m-1}A^{m-1}=-A^m,
\]
which is a system of $n^2$ scalar linear equations in the $m$ unknown coefficients.''',
    r'''A monic polynomial of degree $m$ has the form
$p(z)=c_0+c_1z+\cdots+c_{m-1}z^{m-1}+z^m$.
By the definition of evaluation, $p(T)=0$ is exactly the displayed operator equation. Since $V\ne\{0\}$, its identity operator is not zero: it fixes any chosen nonzero vector. Thus the monic constant polynomial $1$ does not annihilate $T$, and the least degree is positive. The minimal-polynomial existence theorem bounds that degree by $n$. At the least degree, two different coefficient lists would give distinct monic annihilating polynomials of the same least degree, contrary to uniqueness.

For the matrix assertion, representation in a fixed basis is an injective linear map on the operator space. It takes $I$ to $I_n$. The composition rule, applied inductively, gives $\Mat(T^j)=A^j$ for every $j\ge0$. Therefore applying the representation map gives the stated matrix equation, and injectivity proves the converse implication.

Equality of two $n$ by $n$ matrices is equality at their $n^2$ entries. At each entry the powers of $A$ are fixed, so the equation is linear in the unknown scalars $c_0,\ldots,c_{m-1}$.''',
    2, 20,
    [
        r'Rewrite a monic polynomial relation with its highest power on the other side.',
        r'Use linearity and injectivity of matrix representation in a fixed basis.'
    ],
    ['def-minimal-polynomial', 'def-monic', 'def-polynomial-operator',
     'thm-minimal-polynomial-existence', 'def-operator-powers',
     'c3-thm-map-matrix-isomorphism', 'c3-thm-matrix-composition',
     'c3-def-identity-matrix', 'c3-def-matrix'],
    page=145
)

s.r(
    'thm-cyclic-minimal-computation',
    'Computing from the successive images of one vector',
    r'''Let $n=\dim V>0$, let $T\in\Lin(V)$, and let $v\ne0$. If the equation
\[
\sum_{j=0}^{n-1}c_jT^jv=-T^nv
\]
has a unique scalar coefficient list $(c_0,\ldots,c_{n-1})$, then
\[
p(z)=z^n+\sum_{j=0}^{n-1}c_jz^j
\]
is the minimal polynomial of $T$. The coefficient equation has a unique solution whenever $v,Tv,\ldots,T^{n-1}v$ is a basis of $V$.''',
    r'''Suppose the coefficient equation has the unique solution $(c_j)$. If
$\sum_{j=0}^{n-1}a_jT^jv=0$, then the list $(c_j+a_j)$ is another solution of that equation. Uniqueness forces every $a_j=0$. Thus
$v,Tv,\ldots,T^{n-1}v$ is independent, and a length-$n$ independent list in an $n$-dimensional space is a basis.

The displayed polynomial satisfies $p(T)v=0$. Polynomial commutation gives
\[
p(T)T^kv=T^kp(T)v=0
\qquad(0\le k\le n-1).
\]
Hence $p(T)$ vanishes on every member of the basis just obtained. By linearity it vanishes on every vector, so $p(T)=0$.

No nonzero polynomial $q$ of degree less than $n$ can satisfy $q(T)=0$. Otherwise $q(T)v=0$, and writing its coefficients in the first $n$ positions, with trailing zero coefficients if necessary, would give a nontrivial relation on that basis. Thus $p$ is monic, annihilates $T$, and has the smallest possible degree; it is the minimal polynomial.

Finally, if the successive-image list is a basis at the outset, the vector $-T^nv$ has exactly one coefficient list in it by the basis-coordinate theorem. This gives existence and uniqueness of the stated scalar solution.''',
    3, 30,
    [
        r'Uniqueness of the coefficient list forces the successive-image list to be independent.',
        r'Use commutation to propagate $p(T)v=0$ to every vector in that list.',
        r'Test any proposed lower-degree annihilator on $v$.'
    ],
    ['def-minimal-polynomial', 'def-polynomial-operator',
     'thm-polynomial-evaluation-product',
     'c2-def-linear-independence', 'c2-thm-full-length-independent',
     'c2-thm-basis-coordinates', 'c3-def-linear-map',
     'c3-thm-linear-zero'],
    page=145
)

s.r(
    'ex-five-dimensional-minimal-polynomial',
    'A fifth-degree minimal polynomial',
    r'''Suppose $T\in\Lin(\F^5)$ has the matrix
\[
\Mat(T)=
\begin{pmatrix}
0&0&0&0&-3\\
1&0&0&0&6\\
0&1&0&0&0\\
0&0&1&0&0\\
0&0&0&1&0
\end{pmatrix}
\]
in the standard basis. Prove that its minimal polynomial is $z^5-6z+3$.''',
    r'''Reading the columns as images of standard basis vectors gives
\[
Te_1=e_2,\quad Te_2=e_3,\quad Te_3=e_4,\quad
Te_4=e_5,\quad Te_5=-3e_1+6e_2.
\]
Therefore $T^je_1=e_{j+1}$ for $0\le j\le4$, so the successive-image list starting at $e_1$ is the standard basis of $\F^5$. Also
\[
T^5e_1=-3e_1+6Te_1.
\]
Consequently the unique coefficients in
$\sum_{j=0}^{4}c_jT^je_1=-T^5e_1$
are $c_0=3$, $c_1=-6$, and $c_2=c_3=c_4=0$, by equality of standard coordinates. The preceding one-vector computation theorem now identifies the minimal polynomial as
$z^5+\sum_{j=0}^{4}c_jz^j=z^5-6z+3$.''',
    2, 20,
    [
        r'Follow the successive images of the first standard basis vector.',
        r'Read the final image from the last column.'
    ],
    ['thm-cyclic-minimal-computation', 'def-operator-powers',
     'c3-def-map-matrix', 'c2-ex-standard-basis',
     'c2-ex-coordinate-dimension'],
    number='5.26', page=146, kind='example'
)

s.r(
    'thm-minimal-roots',
    'The roots of the minimal polynomial are the eigenvalues',
    r'''Let $V$ be finite-dimensional, let $T\in\Lin(V)$, and let $p$ be its minimal polynomial. For $\lambda\in\F$,
\[
p(\lambda)=0
\quad\Longleftrightarrow\quad
\lambda\text{ is an eigenvalue of }T.
\]''',
    r'''Suppose first that $p(\lambda)=0$. Polynomial division by $z-\lambda$ gives
$p(z)=(z-\lambda)q(z)+r$ with constant remainder $r$. Evaluating at $\lambda$ yields $r=0$. Hence
$p=(z-\lambda)q$.
Because $p$ is monic and nonzero, $q$ is monic of degree $\deg p-1$ by comparison of leading coefficients and the product-degree formula.

The operator $q(T)$ is not zero; otherwise this monic polynomial would contradict the least degree of $p$. Thus choose $v\in V$ such that $q(T)v\ne0$. The product rule gives
\[
(T-\lambda I)q(T)v=p(T)v=0.
\]
The nonzero vector $q(T)v$ is therefore an eigenvector for $\lambda$.

Conversely, suppose $Tv=\lambda v$ for some $v\ne0$. Evaluation on an eigenvector gives
\[
0=p(T)v=p(\lambda)v.
\]
If $p(\lambda)\ne0$, multiplication by its inverse would force $v=0$. Hence $p(\lambda)=0$.

For the zero space, the minimal polynomial is $1$ and there are no eigenvectors. Both conditions are then false for every scalar, consistently with the equivalence.''',
    3, 30,
    [
        r'For a root, divide the minimal polynomial by $z-\lambda$.',
        r'The quotient cannot evaluate to the zero operator because its degree is smaller.',
        r'For an eigenvalue, use the formula for applying a polynomial to an eigenvector.'
    ],
    ['def-minimal-polynomial', 'def-monic', 'def-eigenvalue',
     'thm-polynomial-evaluation-product', 'lem-polynomial-eigenvector',
     'c4-thm-polynomial-division', 'c4-lem-polynomial-product-degree',
     'c3-def-zero-identity-maps'],
    number='5.27(a)', page=146
)

s.r(
    'thm-minimal-complex-factorization',
    'Factoring the complex minimal polynomial',
    r'''For an operator on a finite-dimensional complex vector space, the minimal polynomial can be written
\[
p(z)=\prod_{j=1}^{m}(z-\lambda_j),
\]
where the scalars $\lambda_j$ are eigenvalues. Every eigenvalue occurs in the list at least once, and repetitions are allowed. On the zero space, $m=0$ and the empty product is $1$.''',
    r'''If the space is zero, its minimal polynomial is $1$, so the empty product gives the claim and there are no eigenvalues to list.

Otherwise the identity operator is nonzero, because it fixes a nonzero vector. Thus the monic constant $1$ cannot be the minimal polynomial, and $p$ has positive degree. Complex polynomial factorization writes it as a nonzero scalar times a product of linear factors. The leading coefficient of that product is one, and $p$ is monic, so the scalar factor is one.

Each scalar appearing in a factor is a root of $p$, and hence an eigenvalue by the minimal-root theorem. Conversely, if $\lambda$ is an eigenvalue, then $p(\lambda)=0$. In the displayed product this means that at least one scalar factor $\lambda-\lambda_j$ is zero, since a finite product of nonzero scalars is nonzero. Thus $\lambda$ occurs among the $\lambda_j$.''',
    2, 15,
    [
        r'Combine complex polynomial factorization with the minimal-root theorem.',
        r'Use monicity to determine the leading scalar factor.'
    ],
    ['def-minimal-polynomial', 'def-monic', 'thm-minimal-roots',
     'c4-thm-complex-factorization', 'c1-lem-scalar-cancellation'],
    number='5.27(b)', page=147
)

s.r(
    'cor-minimal-eigenvalue-bound',
    'Counting eigenvalues through the minimal polynomial',
    r'''An operator on a finite-dimensional space has at most as many distinct eigenvalues as the degree of its minimal polynomial, and consequently at most $\dim V$ distinct eigenvalues.''',
    r'''Its distinct eigenvalues are exactly the distinct roots in $\F$ of its minimal polynomial. That polynomial is nonzero, so the polynomial root bound limits their number to its degree. The minimal-polynomial existence theorem bounds that degree by $\dim V$. On the zero space the polynomial has degree zero and there are no eigenvalues, so the same inequalities apply.''',
    1, 10,
    [r'Apply the polynomial root bound to the minimal polynomial.'],
    ['thm-minimal-roots', 'thm-minimal-polynomial-existence',
     'c4-thm-root-bound'],
    page=147, kind='corollary'
)

s.r(
    'thm-realize-monic-polynomial',
    'Every monic polynomial occurs as a minimal polynomial',
    r'''For every monic polynomial $p\in\Poly(\F)$ of degree $m\ge0$, there exists an operator on $\F^m$ whose minimal polynomial is $p$.''',
    r'''If $m=0$, monicity gives $p=1$. The only operator on $\F^0$ has minimal polynomial $1$, so it has the required property.

Suppose $m>0$, and write
\[
p(z)=z^m+\sum_{j=0}^{m-1}a_jz^j.
\]
Prescribe an operator on the standard basis of $\F^m$ by
\[
Te_k=e_{k+1}\quad(1\le k<m),\qquad
Te_m=-\sum_{j=0}^{m-1}a_je_{j+1}.
\]
The theorem on prescribing a map on a basis gives a unique linear operator with these values. They imply $T^je_1=e_{j+1}$ for $0\le j<m$, so the first $m$ successive images form a basis. The final prescribed value gives
\[
T^me_1=-\sum_{j=0}^{m-1}a_jT^je_1.
\]
The one-vector computation theorem therefore identifies the minimal polynomial as
$z^m+\sum_{j=0}^{m-1}a_jz^j=p(z)$.''',
    3, 30,
    [
        r'Use a standard basis and make the operator move each vector to the next one.',
        r'Choose the image of the final basis vector to encode the coefficients of $p$.'
    ],
    ['def-monic', 'def-minimal-polynomial',
     'thm-cyclic-minimal-computation', 'thm-minimal-polynomial-existence',
     'c3-thm-linear-map-basis', 'c2-ex-standard-basis',
     'c2-ex-coordinate-dimension'],
    page=147
)

s.r(
    'ex-quintic-eigenvalues',
    'Eigenvalues specified by a quintic',
    r'''For
\[
T:\C^5\to\C^5,\qquad
T(z_1,z_2,z_3,z_4,z_5)
=(-3z_5,z_1+6z_5,z_2,z_3,z_4),
\]
prove that the eigenvalues are exactly the complex roots of $z^5-6z+3$.''',
    r'''Each output coordinate is a fixed scalar linear combination of the inputs, so the coordinate-map theorem proves that $T$ is linear. Its images of the standard basis vectors are
$e_2,e_3,e_4,e_5,-3e_1+6e_2$, respectively. Hence its matrix is the one in the fifth-degree minimal-polynomial example. That example gives the minimal polynomial $z^5-6z+3$. The minimal-root theorem now identifies its eigenvalues with exactly the complex roots of that polynomial.''',
    1, 10,
    [
        r'Compare its standard basis images with the preceding five-dimensional example.'
    ],
    ['ex-five-dimensional-minimal-polynomial', 'thm-minimal-roots',
     'c3-thm-coordinate-linear-maps', 'c3-def-map-matrix'],
    number='5.28', page=147, kind='example'
)

s.add(
    'theorem',
    'thm-quintic-external-facts',
    'External facts about the quintic roots',
    r'''No root of $z^5-6z+3$ can be expressed using finitely many arithmetic operations and radicals starting from rational numbers. An approximate list of its complex roots is
\[
-1.67,\qquad 0.51,\qquad 1.40,\qquad
-0.12+1.59i,\qquad -0.12-1.59i.
\]''',
    number='', page=147
)

s.note(
    'remark-quintic-external-facts',
    'Facts taken on faith',
    r'''These statements are taken on faith here. The impossibility of radical expressions requires algebra beyond the results developed in this module, and the numerical approximations are supplied without a proof of their error bounds.''',
    147
)

s.r(
    'thm-annihilating-divisibility',
    'All annihilating polynomials are multiples of the minimal polynomial',
    r'''Let $V$ be finite-dimensional, let $T\in\Lin(V)$ have minimal polynomial $p$, and let $q\in\Poly(\F)$. Then
\[
q(T)=0
\quad\Longleftrightarrow\quad
q=ps\text{ for some }s\in\Poly(\F).
\]''',
    r'''Suppose $q(T)=0$. Polynomial division by the nonzero polynomial $p$ gives
\[
q=ps+r,
\]
where either $r=0$ or $\deg r<\deg p$. Linearity and multiplicativity of evaluation yield
\[
0=q(T)=p(T)s(T)+r(T)=r(T).
\]
If $r\ne0$, divide $r$ by its nonzero leading coefficient. The result is a monic polynomial of degree smaller than $\deg p$ that still evaluates to zero, contradicting the definition of $p$. Thus $r=0$, and $q=ps$.

Conversely, if $q=ps$, the product rule gives $q(T)=p(T)s(T)=0$: applied to any vector, the final expression sends the intermediate vector $s(T)v$ to zero. This proves both directions. The zero polynomial is covered by $q=p\cdot0$. On the zero space $p=1$, and every polynomial is a multiple of $1$ and evaluates to the unique zero operator, as the equivalence requires.''',
    2, 20,
    [
        r'Divide $q$ by the minimal polynomial and evaluate the remainder at $T$.',
        r'A nonzero remainder could be normalized to a smaller monic annihilator.'
    ],
    ['def-minimal-polynomial', 'def-monic',
     'thm-polynomial-evaluation-linear', 'thm-polynomial-evaluation-product',
     'c4-thm-polynomial-division'],
    number='5.29', page=148
)

s.r(
    'thm-restriction-minimal',
    'The minimal polynomial of an invariant restriction divides the original',
    r'''Let $V$ be finite-dimensional, let $T\in\Lin(V)$, and let $U$ be an invariant subspace. The minimal polynomial of $T|_U$ divides the minimal polynomial of $T$.''',
    r'''The subspace $U$ is finite-dimensional, and invariance makes $T|_U$ an operator, so its minimal polynomial is defined. Let $p$ be the minimal polynomial of $T$. For every $u\in U$, the restriction-evaluation lemma gives
\[
p(T|_U)u=p(T)u=0.
\]
Hence $p(T|_U)=0$. Applying the characterization of annihilating polynomials to the operator $T|_U$ shows that $p$ is a polynomial multiple of its minimal polynomial. If $U=\{0\}$, that divisor is $1$, which is included in the same argument.''',
    2, 15,
    [
        r'Restrict the identity $p(T)=0$ to $U$ and apply the divisibility theorem there.'
    ],
    ['def-invariant', 'def-minimal-polynomial',
     'lem-restriction-polynomial', 'thm-annihilating-divisibility',
     'c2-thm-subspaces-finite'],
    number='5.31', page=148
)

s.r(
    'thm-invertible-minimal',
    'The constant term detects invertibility',
    r'''For an operator $T$ on a finite-dimensional space with minimal polynomial $p$, the operator is not invertible if and only if $p(0)=0$. Equivalently, $T$ is invertible exactly when the constant term of its minimal polynomial is nonzero.''',
    r'''The eigenvalue tests with $\lambda=0$ say that $T$ is not invertible exactly when zero is an eigenvalue of $T$. By the minimal-root theorem, that is equivalent to $p(0)=0$. Evaluation of a polynomial at zero gives its constant coefficient, proving both formulations.

For the zero space, the minimal polynomial is $1$, whose constant term is nonzero. The only operator is the identity map on that space and is invertible, so this case also satisfies the conclusion.''',
    1, 10,
    [
        r'Apply the eigenvalue criterion to the scalar zero.'
    ],
    ['thm-eigenvalue-tests', 'thm-minimal-roots',
     'def-minimal-polynomial', 'c3-def-invertible-map'],
    number='5.32', page=149
)

s.p(
    'intro-real-odd-eigenvalues',
    'Real operators in odd dimension',
    r'''A real polynomial may have only irreducible quadratic factors, so the complex-root argument does not transfer directly to real scalars. We first show that the null space associated with such a quadratic has even dimension, then use that fact to reduce an odd-dimensional operator to a smaller odd-dimensional invariant subspace.''',
    149
)

s.r(
    'thm-quadratic-null-even',
    'An irreducible real quadratic gives an even-dimensional null space',
    r'''Let $V$ be a finite-dimensional real vector space, let $T\in\Lin(V)$, and suppose $b,c\in\R$ satisfy $b^2<4c$. Then
\[
\dim\Null(T^2+bT+cI)
\]
is even.''',
    r'''Set $q(z)=z^2+bz+c$ and $K=\Null q(T)$. This is a finite-dimensional subspace invariant under $T$. Let $S=T|_K$. The restriction-evaluation lemma gives
\[
S^2+bS+cI_K=0.
\]
We will prove that $\dim K$ is even.

There are no real eigenvectors for $S$. Indeed, if $Sv=\lambda v$ with $v\ne0$ and $\lambda\in\R$, then
\[
0=(S^2+bS+cI_K)v
=(\lambda^2+b\lambda+c)v
=\left((\lambda+b/2)^2+c-b^2/4\right)v.
\]
The scalar in parentheses is strictly positive because its squared term is nonnegative and $c-b^2/4>0$. It is therefore nonzero, and multiplication by its inverse would give $v=0$, a contradiction.

Among the subspaces of $K$ that are invariant under $S$ and have even dimension, choose one, denoted $U$, of largest dimension. Such a choice exists: the zero subspace is eligible, and all eligible dimensions are integers between zero and $\dim K$.

Suppose $U\ne K$, and choose $w\in K\setminus U$. Then $w\ne0$. The vectors $w,Sw$ are independent. To verify this, suppose $aw+dSw=0$. If $d\ne0$, then $Sw=-(a/d)w$, producing a forbidden eigenvector. Hence $d=0$, and $aw=0$ with $w\ne0$ forces $a=0$. Thus
\[
L=\Span(w,Sw)
\]
has dimension two. It is invariant under $S$: the image of $w$ is $Sw\in L$, while the quadratic identity gives
$S(Sw)=-bSw-cw\in L$, and linearity then handles every combination.

The intersection $U\cap L$ is also invariant under $S$, because the image of a vector in both subspaces remains in both. Its dimension is an integer between zero and two. It cannot have dimension two, since equality of dimensions with its containing space $L$ would give $U\cap L=L$, forcing $w\in U$. It cannot have dimension one: if a nonzero vector $v$ is a basis of that invariant intersection, then $Sv$ is a scalar multiple of $v$, again giving an eigenvector of $S$. Therefore the intersection has dimension zero and equals $\{0\}$.

The sum $U+L$ is invariant, because
$S(u+\ell)=Su+S\ell\in U+L$ for $u\in U$ and $\ell\in L$. The dimension formula for a sum gives
\[
\dim(U+L)=\dim U+\dim L-\dim(U\cap L)=\dim U+2.
\]
This is an even dimension larger than the chosen maximum, a contradiction. Hence $U=K$, and $\dim K$ is even. If $K=\{0\}$, the maximal subspace is already all of $K$ and the conclusion is dimension zero, so that case is included.''',
    4, 75,
    [
        r'Restrict $T$ to the indicated null space, where the quadratic operator becomes zero.',
        r'Complete the square to rule out real eigenvectors for the restriction.',
        r'If an even-dimensional invariant subspace is not the whole space, try enlarging it by the span of $w$ and its image.'
    ],
    ['thm-polynomial-invariant', 'lem-restriction-polynomial',
     'def-invariant', 'def-eigenvalue', 'def-polynomial-operator',
     'c3-thm-null-subspace', 'c2-thm-subspaces-finite',
     'c2-def-span', 'c2-def-basis', 'c2-def-dimension',
     'c2-thm-subspace-dimension', 'c2-thm-full-dimension-equality',
     'c2-lem-zero-dimension', 'c2-thm-dimension-sum',
     'c1-thm-smallest-sum', 'c1-foundations'],
    number='5.33', page=149
)

s.r(
    'thm-odd-real-eigenvalue',
    'Every odd-dimensional operator has an eigenvalue',
    r'''Every operator on a finite-dimensional vector space of odd dimension has an eigenvalue, over either $\R$ or $\C$.''',
    r'''Over $\C$, odd dimension is positive, so the complex eigenvalue-existence theorem applies. It remains to prove the assertion over $\R$.

We use induction over the positive odd values of $n=\dim V$. If $n=1$, choose a basis vector $v$. There is a real scalar $\lambda$ with $Tv=\lambda v$, since $v$ spans $V$. As $v\ne0$, this supplies an eigenvalue.

Now suppose $n\ge3$ is odd and the result holds for every operator on each smaller odd-dimensional real space. Let $p$ be the minimal polynomial of $T$. It is nonconstant: otherwise monicity would give $p=1$, but $p(T)=I$ is not zero on the nonzero space $V$.

If $p$ has a real linear factor $z-\lambda$, then $p(\lambda)=0$, so the minimal-root theorem gives the eigenvalue $\lambda$. Suppose instead that there is no such factor. Real polynomial factorization then provides a factor
\[
r(z)=z^2+bz+c,\qquad b^2<4c,
\]
and a monic polynomial $q$ such that $p=qr$. The remaining factors form $q$, so $\deg q=\deg p-2<\deg p$.

Put $R=\Range r(T)$. This subspace is invariant under $T$. The operator identity
\[
q(T)r(T)=p(T)=0
\]
means that $q(T)$ vanishes on $R$. The subspace $R$ is proper: if $R=V$, this would give $q(T)=0$ on all of $V$, contradicting minimality because $q$ is monic of smaller degree than $p$.

By rank-nullity,
\[
\dim R=n-\dim\Null r(T).
\]
The preceding quadratic-null-space theorem makes the subtracted dimension even. Thus $\dim R$ is odd. Since $R$ is a proper subspace of a finite-dimensional space, its dimension is less than $n$: equality would force $R=V$. An odd nonnegative dimension is positive, so the induction hypothesis applies to the operator $T|_R$.

Choose a nonzero $v\in R$ and a real scalar $\lambda$ with
$(T|_R)v=\lambda v$. The restriction has the same value as $T$ at $v$, so $Tv=\lambda v$. This gives an eigenvalue of $T$ and completes the induction.''',
    4, 60,
    [
        r'Induct on the odd dimension. A real linear factor of the minimal polynomial finishes the proof immediately.',
        r'Otherwise select an irreducible quadratic factor and consider the range of that quadratic evaluated at $T$.',
        r'Use minimality to make this range proper and the even-null-space theorem to make its dimension odd.'
    ],
    ['thm-complex-eigenvalue', 'def-minimal-polynomial',
     'def-monic', 'thm-minimal-roots',
     'thm-polynomial-evaluation-product', 'thm-polynomial-invariant',
     'thm-quadratic-null-even', 'def-invariant', 'def-eigenvalue',
     'c4-thm-real-factorization', 'c4-lem-polynomial-product-degree',
     'c3-thm-rank-nullity', 'c2-thm-subspace-dimension',
     'c2-thm-full-dimension-equality', 'c2-thm-basis-existence',
     'c2-def-dimension', 'c1-foundations'],
    number='5.34', page=150
)

s.card(
    'complex-eigenvalue-existence',
    'thm-complex-eigenvalue',
    r'''Which hypotheses guarantee that every complex operator has an eigenvalue?''',
    r'''The underlying complex vector space must be finite-dimensional and nonzero.'''
)

s.card(
    'minimal-polynomial-definition',
    'def-minimal-polynomial',
    r'''What is the minimal polynomial of a finite-dimensional operator?''',
    r'''The unique monic polynomial of smallest degree that evaluates to the zero operator.'''
)

s.card(
    'minimal-polynomial-bound',
    'thm-minimal-polynomial-existence',
    r'''What bound holds for the degree of the minimal polynomial, and what happens on the zero space?''',
    r'''Its degree is at most $\dim V$. On the zero space it is the constant polynomial $1$, of degree zero.'''
)

s.card(
    'one-vector-minimal-computation',
    'thm-cyclic-minimal-computation',
    r'''Why can one vector sometimes determine the entire minimal polynomial?''',
    r'''If its successive images form a basis, a polynomial that annihilates that vector annihilates all those basis vectors by commutation, while their independence rules out lower-degree annihilators.'''
)

s.card(
    'minimal-polynomial-roots',
    'thm-minimal-roots',
    r'''How do the roots of the minimal polynomial relate to eigenvalues?''',
    r'''Its roots in the scalar field are exactly the eigenvalues of the operator.'''
)

s.card(
    'annihilating-divisibility',
    'thm-annihilating-divisibility',
    r'''Which polynomials satisfy $q(T)=0$?''',
    r'''Exactly the polynomial multiples of the minimal polynomial of $T$.'''
)

s.card(
    'restriction-minimal-divisor',
    'thm-restriction-minimal',
    r'''How is the minimal polynomial of an invariant restriction related to the original one?''',
    r'''The minimal polynomial of the restriction divides the minimal polynomial of the original operator.'''
)

s.card(
    'minimal-constant-invertibility',
    'thm-invertible-minimal',
    r'''What does the constant term of the minimal polynomial tell you?''',
    r'''The operator is invertible exactly when that constant term is nonzero.'''
)

s.card(
    'quadratic-null-parity',
    'thm-quadratic-null-even',
    r'''For a real operator and $b^2<4c$, what parity must $\dim\Null(T^2+bT+cI)$ have?''',
    r'''It must be even, including the possibility of dimension zero.'''
)

s.card(
    'odd-dimensional-eigenvalue',
    'thm-odd-real-eigenvalue',
    r'''Does every operator on an odd-dimensional real vector space have an eigenvalue?''',
    r'''Yes. The proof reduces to a smaller odd-dimensional invariant range when the minimal polynomial has an irreducible quadratic factor.'''
)

s.write()
