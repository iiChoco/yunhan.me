from common import Section

s = Section('9c')

s.p(
    'intro-determinants',
    'The scalar action on top alternating forms',
    r'''Throughout this section, $V$ is finite-dimensional over $\F$, where $\F$ is $\R$ or $\C$. An operator acts on alternating forms by applying itself to every argument. Because the space of alternating forms of degree $\dim V$ is one-dimensional, this action is multiplication by a scalar: the determinant.''',
    '354',
)

s.d(
    'def-form-pullback',
    'Applying an operator to every argument',
    r'''Let $m\ge0$, let $T\in\Lin(V)$, and let $\alpha$ be an alternating $m$-linear form on $V$. Define
    \[
    \alpha_T(v_1,\ldots,v_m)=\alpha(Tv_1,\ldots,Tv_m).
    \]
    When $m=0$, this definition means $\alpha_T(())=\alpha(())$.''',
    '9.40', '354',
)

s.r(
    'thm-form-pullback',
    'Operators induce linear maps on alternating forms',
    r'''The form $\alpha_T$ is alternating and multilinear. For fixed $T$, the map $\alpha\mapsto\alpha_T$ is linear. Moreover,
    \[
    \alpha_I=\alpha,\qquad \alpha_{ST}=(\alpha_S)_T
    \]
    for $S,T\in\Lin(V)$.''',
    r'''For $m>0$, fix all arguments except the $j$th. Linearity of $T$ and of $\alpha$ in that argument gives
    \[
    \alpha_T(\ldots,au+bw,\ldots)
    =a\alpha_T(\ldots,u,\ldots)+b\alpha_T(\ldots,w,\ldots).
    \]
    If two arguments agree, their images under $T$ agree, so alternation of $\alpha$ makes the value zero. Thus $\alpha_T$ is an alternating multilinear form.
    Pointwise evaluation gives
    \[
    (a\alpha+b\beta)_T=a\alpha_T+b\beta_T.
    \]
    Applying the identity changes no argument, and applying $ST$ to each argument is the same as first using $T$ and then $S$. This proves the two composition identities.
    For $m=0$, every pullback is the original function on the singleton $\{()\}$, and all the assertions follow from that equality.''',
    1, 15,
    [r'''Check linearity in one argument, then check what happens to two equal arguments.'''],
    ['def-form-pullback', 'def-multilinear-form', 'def-alternating-form', 'c3-def-linear-map'],
    '', '354',
)

s.r(
    'lem-determinant-existence',
    'The top-degree action has one scalar multiplier',
    r'''Write $n=\dim V$. For every $T\in\Lin(V)$ there is a unique scalar $d\in\F$ such that
    \[
    \alpha_T=d\alpha
    \]
    for every alternating $n$-linear form $\alpha$ on $V$.''',
    r'''The space of alternating $n$-linear forms has dimension one. Choose a nonzero form $\omega$ in this space. Since $\omega_T$ belongs to the same one-dimensional space, there is a scalar $d$ with $\omega_T=d\omega$.
    Every alternating $n$-linear form is $c\omega$ for a scalar $c$. Linearity of pullback gives
    \[
    (c\omega)_T=c\omega_T=cd\omega=d(c\omega).
    \]
    Thus the same scalar works for every form. If another scalar $d'$ also worked, then $(d-d')\omega=0$. Since $\omega$ is nonzero, this forces $d=d'$.
    The argument also applies to $n=0$, because the space of alternating zero-forms is one-dimensional.''',
    2, 15,
    [r'''Choose one nonzero top-degree form and express every other one as its scalar multiple.'''],
    ['thm-form-pullback', 'thm-top-alternating-dimension'],
    '', '354', kind='lemma',
)

s.d(
    'def-determinant',
    'Determinant of an operator',
    r'''For $T\in\Lin(V)$, the \emph{determinant} $\det T$ is the unique scalar satisfying
    \[
    \alpha_T=(\det T)\alpha
    \]
    for every alternating form $\alpha$ of degree $\dim V$.
    In dimension zero, pullback fixes every zero-form, so the determinant of the only operator is $1$.''',
    '9.41', '354',
)

s.r(
    'thm-determinant-scaling',
    'Identity, scalar multiplication, and an eigenvector basis',
    r'''Let $n=\dim V$.
    \begin{enumerate}
    \item $\det I=1$.
    \item For $\lambda\in\F$, $\det(\lambda I)=\lambda^n$.
    \item For $\lambda\in\F$ and $T\in\Lin(V)$,
    \[
    \det(\lambda T)=\lambda^n\det T.
    \]
    \item If $e_1,\ldots,e_n$ is a basis with $Te_j=\lambda_j e_j$, then
    \[
    \det T=\prod_{j=1}^n\lambda_j.
    \]
    \end{enumerate}
    In dimension zero, each empty product and each factor $\lambda^0$ in these formulas is interpreted as $1$.''',
    r'''Pullback by $I$ fixes every form, so the defining scalar is $1$.
    Multilinearity gives
    \[
    \alpha(\lambda Tv_1,\ldots,\lambda Tv_n)
    =\lambda^n\alpha(Tv_1,\ldots,Tv_n)
    =\lambda^n(\det T)\alpha(v_1,\ldots,v_n).
    \]
    Uniqueness of the determinant proves the third assertion. Taking $T=I$ proves the second.
    For the last assertion, choose an alternating top-degree form $\omega$ normalized by $\omega(e_1,\ldots,e_n)=1$. Then
    \[
    \det T
    =\omega(Te_1,\ldots,Te_n)
    =\omega(\lambda_1e_1,\ldots,\lambda_ne_n)
    =\prod_{j=1}^n\lambda_j.
    \]
    For $n=0$, the normalized form has value $1$ on the empty tuple, so these calculations give $1$ with the stated conventions.''',
    2, 20,
    [r'''Pull a scalar out of each argument of a top-degree alternating form.'''],
    ['def-determinant', 'thm-form-pullback', 'thm-coordinate-alternating-form'],
    '9.42', '354', kind='example',
)

s.d(
    'def-matrix-determinant',
    'Determinant of a square matrix',
    r'''For an $n$-by-$n$ matrix $A$ over $\F$, let $T_A:\F^n\to\F^n$ be the operator whose standard matrix is $A$. Define
    \[
    \det A=\det T_A.
    \]
    This includes $n=0$, so the determinant of the empty matrix is $1$.''',
    '9.43', '355',
)

s.r(
    'ex-identity-diagonal-determinants',
    'Determinants of identity and diagonal matrices',
    r'''The identity matrix has determinant $1$. A diagonal matrix with diagonal entries $\lambda_1,\ldots,\lambda_n$ has determinant $\lambda_1\cdots\lambda_n$.''',
    r'''The operator associated with the identity matrix is the identity operator, whose determinant is $1$.
    For a diagonal matrix, the $j$th standard basis vector is sent to $\lambda_j$ times itself. Thus the standard basis is an eigenvector basis, and the preceding eigenbasis product formula gives the determinant. For the empty matrix, the product is $1$, agreeing with its definition.''',
    1, 10,
    [r'''Describe how the associated operator acts on the standard basis.'''],
    ['def-matrix-determinant', 'thm-determinant-scaling'],
    '9.44', '355', kind='example',
)

s.r(
    'thm-determinant-columns',
    'Determinant is the normalized alternating form of the columns',
    r'''On $\F^n$, the function
    \[
    (v_1,\ldots,v_n)\longmapsto\det(v_1\ \cdots\ v_n)
    \]
    is the unique alternating $n$-linear form whose value on the standard basis is $1$.''',
    r'''Let $\omega$ be the alternating form normalized by
    $\omega(e_1,\ldots,e_n)=1$ on the standard basis. Given columns $v_1,\ldots,v_n$, define $T$ by $Te_j=v_j$. Its standard matrix has exactly these columns. Hence
    \[
    \det(v_1\ \cdots\ v_n)
    =\det T
    =(\det T)\omega(e_1,\ldots,e_n)
    =\omega(Te_1,\ldots,Te_n)
    =\omega(v_1,\ldots,v_n).
    \]
    Thus the determinant function is $\omega$ and is alternating and multilinear. Uniqueness of a normalized top-degree form gives the asserted uniqueness. The same calculation on the empty tuple applies when $n=0$.''',
    2, 20,
    [r'''Choose the normalized alternating form and evaluate its pullback on the standard basis.'''],
    [
        'def-determinant', 'def-matrix-determinant',
        'thm-coordinate-alternating-form', 'thm-top-alternating-formula',
        'c3-thm-linear-map-basis',
    ],
    '9.45', '355',
)

s.r(
    'thm-determinant-formula',
    'The permutation formula for a determinant',
    r'''For an $n$-by-$n$ matrix $A$,
    \[
    \det A=\sum_{\sigma}\sgn(\sigma)
    \prod_{j=1}^n A_{\sigma(j),j},
    \]
    where the sum is over all permutations of $\{1,\ldots,n\}$ and $\sigma(j)$ denotes the $j$th entry of the permutation. For $n=0$, there is one empty permutation, with sign and product both equal to $1$.''',
    r'''The $j$th column of $A$ has standard coordinates
    \[
    v_j=\sum_{i=1}^n A_{i,j}e_i.
    \]
    Apply the coordinate expansion formula for an alternating top-degree form to the determinant form of the columns. Its value at the standard basis is $1$, so the expansion gives
    \[
    \det(v_1\ \cdots\ v_n)
    =\sum_{\sigma}\sgn(\sigma)
      A_{\sigma(1),1}\cdots A_{\sigma(n),n}.
    \]
    This is the asserted formula. In dimension zero, the coordinate expansion consists of its one empty term and gives $1$.''',
    2, 15,
    [r'''Use the coordinate expansion of an alternating form, normalized to be $1$ on the standard basis.'''],
    ['thm-determinant-columns', 'thm-top-alternating-formula'],
    '9.46', '356',
)

s.r(
    'ex-small-determinant-formulas',
    'Explicit formulas in dimensions two and three',
    r'''\[
    \det\begin{pmatrix}a&b\\c&d\end{pmatrix}=ad-bc,
    \]
    and
    \[
    \det\begin{pmatrix}
    a&b&c\\d&e&f\\g&h&i
    \end{pmatrix}
    =aei+bfg+cdh-ceg-bdi-afh.
    \]''',
    r'''For a two-element set, the permutations $(1,2)$ and $(2,1)$ have signs $1$ and $-1$. Their terms in the permutation formula are $ad$ and $-cb$.
    For a three-element set, the permutations
    \[
    (1,2,3),\ (2,1,3),\ (3,2,1),\
    (1,3,2),\ (3,1,2),\ (2,3,1)
    \]
    have signs $1,-1,-1,-1,1,1$, respectively, as obtained by counting inversions. Their terms are
    \[
    aei,\ -dbi,\ -gec,\ -ahf,\ gbf,\ dhc.
    \]
    Summing and commuting scalar factors gives the displayed formula.''',
    1, 15,
    [r'''List the permutations and determine each sign by its number of inversions.'''],
    ['thm-determinant-formula', 'def-permutation-sign'],
    '9.47', '356', kind='example',
)

s.r(
    'thm-triangular-determinant',
    'The determinant of an upper-triangular matrix',
    r'''If $A$ is upper triangular with diagonal entries $\lambda_1,\ldots,\lambda_n$, then
    \[
    \det A=\lambda_1\cdots\lambda_n.
    \]''',
    r'''Suppose a permutation $\sigma$ satisfies $\sigma(j)\le j$ for every $j$. Since
    \[
    \sum_{j=1}^n\sigma(j)=\sum_{j=1}^n j,
    \]
    none of these inequalities can be strict. Thus $\sigma$ is the identity. Consequently every nonidentity permutation has an index $j$ with $\sigma(j)>j$. Upper triangularity then gives $A_{\sigma(j),j}=0$, making that permutation's entire product zero.
    Only the identity permutation can contribute to the determinant formula. Its sign is $1$ and its product is $\prod_jA_{j,j}=\prod_j\lambda_j$. This also gives the empty product when $n=0$.''',
    2, 20,
    [r'''Show that any nonidentity permutation selects at least one entry below the diagonal.'''],
    ['thm-determinant-formula', 'c5-def-upper-triangular'],
    '9.48', '356',
)

s.r(
    'thm-determinant-multiplicative',
    'Determinants multiply under composition',
    r'''For $S,T\in\Lin(V)$,
    \[
    \det(ST)=(\det S)(\det T).
    \]
    For square matrices $A,B$ of the same size,
    \[
    \det(AB)=(\det A)(\det B).
    \]''',
    r'''For every alternating top-degree form $\alpha$, the pullback identities and linearity give
    \[
    \alpha_{ST}=(\alpha_S)_T
    =((\det S)\alpha)_T
    =(\det S)\alpha_T
    =(\det S)(\det T)\alpha.
    \]
    Uniqueness of the determinant proves the operator formula.
    Let $S$ and $T$ be the standard-coordinate operators associated with $A$ and $B$. Matrix multiplication represents composition, so the standard matrix of $ST$ is $AB$. The definition of matrix determinant and the operator formula yield
    \[
    \det(AB)=\det(ST)=(\det S)(\det T)=(\det A)(\det B).
    \]
    The same reasoning applies in dimension zero.''',
    2, 20,
    [r'''Apply the defining scalar action first for $S$, then for $T$.'''],
    ['def-determinant', 'thm-form-pullback', 'def-matrix-determinant', 'c3-thm-matrix-composition'],
    '9.49', '357',
)

s.r(
    'thm-determinant-invertible',
    'A nonzero determinant detects invertibility',
    r'''An operator $T\in\Lin(V)$ is invertible if and only if $\det T\ne0$. If $T$ is invertible, then
    \[
    \det(T^{-1})=\frac1{\det T}.
    \]''',
    r'''If $T$ is invertible, multiplicativity gives
    \[
    1=\det I=\det(TT^{-1})=(\det T)\det(T^{-1}).
    \]
    Thus $\det T$ is nonzero and the inverse formula follows.
    Conversely, suppose $\det T\ne0$. If a nonzero vector $v$ satisfied $Tv=0$, extend $v$ to a basis $v,e_2,\ldots,e_n$. Choose an alternating top-degree form $\omega$ with value $1$ on this basis. Then
    \[
    \det T
    =\omega(Tv,Te_2,\ldots,Te_n)
    =\omega(0,Te_2,\ldots,Te_n)=0,
    \]
    a contradiction. The last equality follows from linearity in the first argument. Hence $\Null T=\{0\}$, so $T$ is injective and therefore invertible on a finite-dimensional space.
    In dimension zero there is no nonzero $v$, the only operator is the identity, and the same invertibility conclusion holds.''',
    2, 25,
    [
        r'''For one direction, take determinants in $TT^{-1}=I$.''',
        r'''For the other, extend a proposed nonzero kernel vector to a basis.''',
    ],
    [
        'thm-determinant-multiplicative', 'thm-determinant-scaling',
        'thm-coordinate-alternating-form', 'c2-thm-extend-independent',
        'c3-thm-injective-null', 'c3-thm-equal-dimension-invertibility',
    ],
    '9.50', '357',
)

s.r(
    'cor-matrix-determinant-invertible',
    'The matrix invertibility test',
    r'''A square matrix $A$ is invertible if and only if $\det A\ne0$. If it is invertible, then
    \[
    \det(A^{-1})=(\det A)^{-1}.
    \]''',
    r'''A square matrix is invertible exactly when its standard-coordinate operator is invertible, and the matrix of the inverse operator is the inverse matrix. Apply the operator determinant test and inverse formula to that operator, then use the definition of matrix determinant.''',
    1, 10,
    [r'''Translate the statement to the associated operator on $\F^n$.'''],
    ['thm-determinant-invertible', 'def-matrix-determinant', 'c3-thm-matrix-inverse'],
    '', '358', kind='corollary',
)

s.r(
    'thm-determinant-eigenvalue',
    'Eigenvalues are detected by a determinant equation',
    r'''For $\lambda\in\F$,
    \[
    \lambda\text{ is an eigenvalue of }T
    \quad\Longleftrightarrow\quad
    \det(\lambda I-T)=0.
    \]''',
    r'''A scalar $\lambda$ is an eigenvalue exactly when $T-\lambda I$ is not invertible. Multiplication by $-1$ preserves invertibility: if an operator $A$ has inverse $B$, then $-A$ has inverse $-B$, and the converse follows by applying the same observation again. Thus $T-\lambda I$ is not invertible exactly when $\lambda I-T$ is not invertible. The determinant invertibility test gives the claimed equivalence.
    In dimension zero, every $\lambda I-T$ is the only operator and has determinant $1$, agreeing with the absence of eigenvalues.''',
    1, 15,
    [r'''Combine the invertibility test for eigenvalues with the invertibility test for determinants.'''],
    ['thm-determinant-invertible', 'c5-thm-eigenvalue-tests'],
    '9.51', '358',
)

s.r(
    'thm-determinant-similarity',
    'Determinant is preserved by an isomorphism of spaces',
    r'''Suppose $S:W\to V$ is an invertible linear map and $T\in\Lin(V)$. Then
    \[
    \det(S^{-1}TS)=\det T.
    \]''',
    r'''The isomorphic spaces have the same dimension $n$. Choose a nonzero alternating $n$-linear form $\tau$ on $W$, and define a form on $V$ by
    \[
    \alpha(v_1,\ldots,v_n)=\tau(S^{-1}v_1,\ldots,S^{-1}v_n).
    \]
    Linearity of $S^{-1}$ makes this multilinear, and equal arguments have equal images, making it alternating. For $w_1,\ldots,w_n\in W$,
    \[
    \begin{aligned}
    \tau(S^{-1}TSw_1,\ldots,S^{-1}TSw_n)
    &=\alpha(TSw_1,\ldots,TSw_n)\\
    &=(\det T)\alpha(Sw_1,\ldots,Sw_n)\\
    &=(\det T)\tau(w_1,\ldots,w_n).
    \end{aligned}
    \]
    The left side is also $\det(S^{-1}TS)\tau(w_1,\ldots,w_n)$. Since $\tau$ is a nonzero function, comparison of these scalar multiples gives the desired equality. For $n=0$, the calculation uses the empty tuple and remains valid.''',
    3, 30,
    [r'''Transport an alternating form from $W$ to $V$ using $S^{-1}$.'''],
    [
        'def-determinant', 'thm-top-alternating-dimension',
        'c3-thm-isomorphism-dimension', 'c3-thm-invertible-bijective',
    ],
    '9.52', '358',
)

s.r(
    'thm-operator-matrix-determinant',
    'An operator and its matrix have the same determinant',
    r'''If $\mathcal E=(e_1,\ldots,e_n)$ is any basis of $V$, then
    \[
    \det T=\det\mathcal M(T,\mathcal E).
    \]''',
    r'''Let $S:\F^n\to V$ send a coordinate list $(a_1,\ldots,a_n)$ to $\sum_ja_je_j$. The basis coordinate theorem makes $S$ a linear bijection. If $A=\mathcal M(T,\mathcal E)$, then the standard-coordinate operator $S^{-1}TS$ has matrix $A$: applying it to the $j$th standard vector gives exactly the coordinates of $Te_j$.
    Similarity invariance and the definition of matrix determinant therefore give
    \[
    \det T=\det(S^{-1}TS)=\det A.
    \]
    This includes the coordinate isomorphism between zero spaces.''',
    2, 20,
    [r'''Use the isomorphism that sends standard coordinate vectors to the chosen basis vectors.'''],
    [
        'thm-determinant-similarity', 'def-matrix-determinant',
        'c2-thm-basis-coordinates', 'c3-def-map-matrix',
    ],
    '9.53', '359',
)

s.r(
    'thm-determinant-eigenvalue-product',
    'Over the complex field, determinant is the eigenvalue product',
    r'''For a complex operator $T$, its determinant is the product of its eigenvalues, each repeated according to its multiplicity. The product is $1$ on the zero space.''',
    r'''Choose a triangular matrix of $T$. The diagonal entries list the eigenvalues with their multiplicities. The determinant of this matrix is the product of its diagonal entries, and the operator determinant equals the matrix determinant. These facts give the asserted product, including the empty product in dimension zero.''',
    2, 15,
    [r'''Use a triangular matrix and the theorem identifying its diagonal multiplicities.'''],
    [
        'thm-operator-matrix-determinant', 'thm-triangular-determinant',
        'c8-thm-triangular-multiplicities', 'c8-thm-generalized-block-diagonal',
    ],
    '9.55', '359',
)

s.r(
    'thm-determinant-transpose-dual-adjoint',
    'Transpose, conjugation, duals, and adjoints',
    r'''\begin{enumerate}
    \item For a square matrix $A$,
    \[
    \det(A^{\mathsf t})=\det A,\qquad
    \det(\overline A)=\overline{\det A},\qquad
    \det(A^*)=\overline{\det A},
    \]
    where $A^*=\overline A^{\mathsf t}$.
    \item For the dual operator $T'$, $\det T'=\det T$.
    \item On a finite-dimensional inner product space,
    \[
    \det(T^*)=\overline{\det T}.
    \]
    \end{enumerate}''',
    r'''The permutation formula gives
    \[
    \det(A^{\mathsf t})
    =\sum_\sigma\sgn(\sigma)
      \prod_{j=1}^n A_{j,\sigma(j)}.
    \]
    Set $\tau=\sigma^{-1}$. Reindexing the product by $k=\sigma(j)$ turns it into
    $\prod_kA_{\tau(k),k}$. A permutation and its inverse have the same sign, and inversion permutes the set of permutations. Thus the sum equals $\det A$.
    All permutation signs are real. Conjugating the determinant formula therefore gives
    $\det(\overline A)=\overline{\det A}$. Combining this with the transpose identity proves the conjugate-transpose identity. The empty-matrix formulas also hold because its determinant is $1$.
    Choose a basis of $V$ and its dual basis. The matrices of $T$ and $T'$ in these bases are transposes, so equality of operator and matrix determinants proves $\det T'=\det T$.
    Finally choose an orthonormal basis of an inner product space. The matrix of $T^*$ is the conjugate transpose of the matrix of $T$. The matrix identity and equality of operator and matrix determinants give $\det(T^*)=\overline{\det T}$.''',
    3, 35,
    [
        r'''In the permutation formula for the transpose, replace each permutation by its inverse.''',
        r'''Represent the dual in a dual basis and the adjoint in an orthonormal basis.''',
    ],
    [
        'thm-determinant-formula', 'lem-permutation-inverse-sign',
        'thm-operator-matrix-determinant', 'c3-thm-dual-matrix',
        'c6-thm-orthonormal-basis-existence', 'c7-thm-adjoint-matrix',
    ],
    '9.56', '360',
)

s.r(
    'thm-determinant-row-column-operations',
    'How elementary row and column operations affect a determinant',
    r'''\begin{enumerate}
    \item A matrix with two equal columns or two equal rows has determinant zero.
    \item Swapping two distinct columns or two distinct rows multiplies the determinant by $-1$.
    \item Multiplying one column or one row by a scalar multiplies the determinant by that scalar.
    \item Adding a scalar multiple of one column to a different column leaves the determinant unchanged.
    \item Adding a scalar multiple of one row to a different row leaves the determinant unchanged.
    \end{enumerate}''',
    r'''The determinant is alternating in its columns, so equal columns give zero, and swapping two columns changes its sign. Multilinearity shows that multiplying one column by a scalar multiplies the determinant by that scalar.
    For distinct indices $j,k$, replace column $j$, originally $v_j$, by $v_j+cv_k$. Linearity in that column expands the new determinant as the old determinant plus $c$ times a determinant whose columns in positions $j$ and $k$ are both $v_k$. The latter determinant is zero, proving invariance under the addition.
    Transposition turns each row operation into the corresponding column operation and leaves the determinant unchanged. Applying each established column rule to the transposed matrices therefore gives its row version. Statements requiring two distinct rows or columns have no instances when the size is less than two.''',
    2, 25,
    [r'''Prove the column rules using alternation and multilinearity, then transpose to obtain the row rules.'''],
    [
        'thm-determinant-columns', 'thm-alternating-swap',
        'thm-determinant-transpose-dual-adjoint',
    ],
    '9.57', '360–361',
)

s.r(
    'thm-unitary-determinant',
    'A unitary determinant has absolute value one',
    r'''A unitary operator $S$ satisfies $|\det S|=1$. The same holds for a unitary square matrix.''',
    r'''Unitarity gives $S^*S=I$. Hence
    \[
    1=\det I=\det(S^*S)
    =\det(S^*)\det S
    =\overline{\det S}\det S
    =|\det S|^2.
    \]
    Since absolute value is nonnegative, this implies $|\det S|=1$.
    A unitary matrix satisfies the same identity $A^*A=I$, so the matrix determinant formulas give the same calculation. In size zero it reads $1=1$.''',
    2, 15,
    [r'''Take determinants in the identity $S^*S=I$.'''],
    [
        'thm-determinant-multiplicative', 'thm-determinant-transpose-dual-adjoint',
        'thm-determinant-scaling', 'c7-thm-unitary-equivalences',
        'c7-def-unitary-matrix', 'c4-thm-complex-properties',
    ],
    '9.58', '362',
)

s.r(
    'thm-positive-determinant',
    'Positive operators have nonnegative determinants',
    r'''If $T$ is a positive operator on a finite-dimensional inner product space, then $\det T$ is a nonnegative real number.''',
    r'''A positive operator has an orthonormal eigenvector basis with nonnegative eigenvalues. Its determinant is the product of the eigenvalues associated with that basis, by the eigenbasis determinant formula. A finite product of nonnegative real numbers is nonnegative. For the zero space the empty product is $1$, which is also nonnegative.''',
    1, 15,
    [r'''Use an orthonormal eigenvector basis for the positive operator.'''],
    ['thm-determinant-scaling', 'c7-thm-positive-characterizations'],
    '9.59', '362',
)

s.r(
    'thm-determinant-singular-values',
    'The absolute determinant is the product of singular values',
    r'''Let $T$ be an operator on a finite-dimensional inner product space, with singular values $s_1,\ldots,s_n$. Then
    \[
    |\det T|=\sqrt{\det(T^*T)}=\prod_{j=1}^n s_j.
    \]''',
    r'''Multiplicativity and the adjoint identity give
    \[
    \det(T^*T)=\det(T^*)\det T
    =\overline{\det T}\det T=|\det T|^2.
    \]
    The singular-eigenbasis theorem supplies an orthonormal basis in which $T^*T$ has eigenvalues $s_1^2,\ldots,s_n^2$. The eigenbasis determinant formula therefore gives
    \[
    \det(T^*T)=\prod_{j=1}^n s_j^2
    =\left(\prod_{j=1}^n s_j\right)^2.
    \]
    Both $|\det T|$ and $\prod_js_j$ are nonnegative, so they are the same nonnegative square root of $\det(T^*T)$. Empty products give the same conclusion when $n=0$.''',
    2, 20,
    [
        r'''First compute $\det(T^*T)$ using multiplicativity.''',
        r'''Compute it again in a singular eigenbasis.''',
    ],
    [
        'thm-determinant-multiplicative', 'thm-determinant-transpose-dual-adjoint',
        'thm-determinant-scaling', 'c7-lem-singular-eigenbasis',
        'c4-thm-complex-properties',
    ],
    '9.60', '362',
)

s.r(
    'lem-proper-subspace-volume-zero',
    'Every subset of a proper real subspace has volume zero',
    r'''If $U$ is a proper subspace of $\R^n$ and $A\subseteq U$, then $A$ is Lebesgue measurable and has $n$-dimensional volume zero.''',
    r'''A proper subspace can occur only for $n\ge1$. First consider
    \[
    H=\{x\in\R^n:x_n=0\}.
    \]
    For $\varepsilon>0$ and each integer $k\ge1$, set
    \[
    \delta_k=\frac{\varepsilon\,2^{-k-1}}{(2k)^{n-1}},
    \qquad B_k=(-k,k)^{n-1}\times(-\delta_k,\delta_k).
    \]
    For $n=1$, the first factor is the empty Cartesian product. These boxes cover $H$: every point of $H$ has its first $n-1$ coordinates inside $(-k,k)$ for a sufficiently large $k$. Their total volume is
    \[
    \sum_{k=1}^{\infty}(2k)^{n-1}2\delta_k
    =\varepsilon\sum_{k=1}^{\infty}2^{-k}
    \le\varepsilon.
    \]
    The last bound follows because every finite partial sum is at most $1$. Thus every subset of $H$ has outer measure zero.

    We verify from the definition that any set $A$ of outer measure zero is measurable. Outer measure is monotone because every cover of a set also covers each subset. Therefore $m_n^*(E\cap A)=0$ and $m_n^*(E\setminus A)\le m_n^*(E)$.
    If $m_n^*(E\setminus A)$ is finite, combine a box cover of $E\setminus A$ with total volume within $\varepsilon/2$ of its outer measure and a cover of $A$ of total volume less than $\varepsilon/2$. Their union covers $E$, giving
    \[
    m_n^*(E)\le m_n^*(E\setminus A)+\varepsilon.
    \]
    Letting $\varepsilon$ decrease to zero yields equality with $m_n^*(E\setminus A)$. If that outer measure is infinite, monotonicity gives $m_n^*(E)=+\infty$ as well. In both cases
    \[
    m_n^*(E)=m_n^*(E\cap A)+m_n^*(E\setminus A),
    \]
    proving measurability and volume zero.

    For a general proper subspace $U$, choose an orthonormal basis of $U$ and extend it to an orthonormal basis of $\R^n$. The corresponding orthonormal coordinate map $Q$ preserves the inner product and the norm and sends $U$ into $H$, because $\dim U<n$. Thus $Q(A)$ is measurable and has volume zero by the preceding argument. The accepted invariance of measurability and measure under orthogonal coordinate changes now gives the same conclusions for $A$.''',
    3, 45,
    [
        r'''Cover a coordinate hyperplane by boxes that are arbitrarily thin in the last coordinate.''',
        r'''Use the outer-measure definition to prove that every set of outer measure zero is measurable.''',
        r'''Put a general proper subspace inside a coordinate hyperplane using an orthonormal basis.''',
    ],
    [
        'c7-def-volume', 'c7-thm-lebesgue-prerequisites',
        'c6-thm-orthonormal-basis-existence', 'c6-thm-orthonormal-extension',
        'c6-thm-orthonormal-coordinates', 'c2-thm-proper-subspace-dimension',
    ],
    '', '363', kind='lemma',
)

s.r(
    'thm-determinant-volume',
    'Absolute determinant is the volume multiplier',
    r'''Let $T\in\Lin(\R^n)$.
    \begin{enumerate}
    \item If $T$ is invertible and $\Omega$ is Lebesgue measurable, then $T(\Omega)$ is measurable and
    \[
    \Vol(T(\Omega))=|\det T|\Vol(\Omega).
    \]
    This includes infinite volume.
    \item If $T$ is not invertible, the image of every subset of $\R^n$ is measurable and has volume zero.
    \end{enumerate}
    Consequently the displayed scaling formula holds for every measurable $\Omega$ of finite volume, whether or not $T$ is invertible.''',
    r'''For invertible $T$, the earlier volume-scaling theorem gives the multiplier $\prod_js_j$, where the $s_j$ are its singular values. The determinant singular-value formula identifies this product with $|\det T|$, proving the first assertion. This multiplier is positive, so it also applies to infinite volume.
    If $T$ is not invertible, finite-dimensional equivalence of surjectivity and invertibility makes $\Range T$ a proper subspace of $\R^n$. Every image $T(\Omega)$ is a subset of that subspace, so the preceding lemma gives measurability and volume zero. Also $\det T=0$ by the determinant invertibility test. If $\Vol(\Omega)$ is finite, the right side of the displayed formula is therefore zero as well. The separate statement for singular maps avoids assigning a value to the product $0\cdot+\infty$.''',
    2, 20,
    [r'''Use singular values for invertible maps and the proper-subspace lemma for singular maps.'''],
    [
        'thm-determinant-singular-values', 'thm-determinant-invertible',
        'lem-proper-subspace-volume-zero', 'c7-thm-volume-scaling',
        'c3-thm-equal-dimension-invertibility',
    ],
    '9.61', '363',
)

s.r(
    'thm-complex-characteristic-determinant',
    'The complex characteristic polynomial is a determinant',
    r'''Suppose $V$ is complex and the distinct eigenvalues of $T$ are $\lambda_1,\ldots,\lambda_p$, with multiplicities $d_1,\ldots,d_p$. Then
    \[
    \det(zI-T)=\prod_{j=1}^p(z-\lambda_j)^{d_j}.
    \]
    Thus $z\mapsto\det(zI-T)$ is the characteristic polynomial already defined using multiplicities.''',
    r'''Choose a triangular matrix of $T$ whose diagonal lists each eigenvalue $\lambda_j$ exactly $d_j$ times. For any $z\in\C$, the matrix of $zI-T$ in the same basis is upper triangular and has $z-\lambda_j$ in those same $d_j$ diagonal positions. Its determinant is the product of its diagonal entries. Equality of operator and matrix determinants gives the displayed identity for every $z$.
    On the zero space, both sides are $1$: the determinant is that of the only operator and the product is empty.''',
    2, 20,
    [r'''Use the same triangular basis for $T$ and $zI-T$.'''],
    [
        'thm-operator-matrix-determinant', 'thm-triangular-determinant',
        'c8-thm-triangular-multiplicities', 'c8-thm-generalized-block-diagonal', 'c8-def-characteristic-polynomial',
        'c3-thm-matrix-addition', 'c3-thm-matrix-scaling',
    ],
    '9.62', '363',
)

s.d(
    'def-characteristic-polynomial-real-complex',
    'The characteristic polynomial over either field',
    r'''For an operator $T$ on a finite-dimensional real or complex space, define its \emph{characteristic polynomial} by
    \[
    q_T(z)=\det(zI-T).
    \]
    The next result verifies that this function is a polynomial over the underlying field. Over $\C$, it agrees with the earlier definition by eigenvalue multiplicities.''',
    '9.63', '363',
)

s.r(
    'thm-characteristic-degree-roots',
    'Degree and roots of the characteristic polynomial',
    r'''If $n=\dim V$, then $q_T$ is a monic polynomial over $\F$ of degree $n$. Its roots in $\F$ are exactly the eigenvalues of $T$. In particular, $q_T=1$ when $n=0$.''',
    r'''Choose a basis and let $A$ be the matrix of $T$. Then
    \[
    q_T(z)=\det(zI-A).
    \]
    The permutation formula expresses this as a finite sum of products of polynomials with coefficients in $\F$, so it is a polynomial over $\F$.
    The identity permutation contributes
    \[
    \prod_{j=1}^n(z-A_{j,j}),
    \]
    a monic polynomial of degree $n$. Every nonidentity permutation moves at least two indices: if it moved only one index, bijectivity would fail at the image of that index. At each moved index, the selected matrix entry is an off-diagonal entry of $zI-A$ and is independent of $z$. Thus any nonidentity term has degree at most $n-2$, unless it is zero. For $n=1$ there are no nonidentity permutations. The leading term is therefore $z^n$, with coefficient $1$. For $n=0$, the determinant formula gives the constant polynomial $1$ directly.
    Finally, the determinant eigenvalue criterion says that $q_T(\lambda)=0$ exactly when $\lambda$ is an eigenvalue.''',
    2, 25,
    [
        r'''In the permutation formula, only the identity permutation can contribute a term of degree $n$.''',
        r'''A nonidentity permutation cannot move exactly one index.''',
    ],
    [
        'def-characteristic-polynomial-real-complex', 'thm-determinant-formula',
        'thm-operator-matrix-determinant', 'thm-determinant-eigenvalue',
    ],
    '', '363',
)

s.r(
    'thm-cayley-hamilton-real-complex',
    'Cayley–Hamilton over the real or complex field',
    r'''Every operator satisfies its characteristic polynomial:
    \[
    q_T(T)=0.
    \]''',
    r'''Over $\C$, the determinant definition agrees with the earlier characteristic polynomial, so the previously proved complex Cayley–Hamilton theorem gives the result.
    Now let $\F=\R$, choose a basis of $V$, and let $A$ be the resulting real matrix. Let $S$ be the complex-linear operator on $\C^n$ whose standard matrix is the same array $A$.
    The permutation formula for $\det(zI-A)$ uses the same finite polynomial expression whether the entries are regarded as real or complex. Consequently the real coefficients of $q_T$ also define the complex characteristic polynomial of $S$. Complex Cayley–Hamilton gives $q_T(S)=0$.
    Write $q_T(z)=\sum_{j=0}^n a_jz^j$. Matrix addition, scaling, and composition show that the standard matrix of $q_T(S)$ is
    \[
    \sum_{j=0}^n a_jA^j.
    \]
    Hence this matrix is zero. The same expression is the matrix of $q_T(T)$ in the chosen real basis. A linear map with zero matrix sends every basis vector, and therefore every vector, to zero. Thus $q_T(T)=0$.
    For $n=0$, the characteristic polynomial is $1$ and $1(T)=I=0$ on the zero space, agreeing with the argument.''',
    3, 35,
    [
        r'''For a real operator, use its real matrix to define an operator on $\C^n$.''',
        r'''The permutation formula gives exactly the same characteristic-polynomial coefficients over either field.''',
    ],
    [
        'thm-complex-characteristic-determinant', 'thm-determinant-formula',
        'c8-thm-cayley-hamilton', 'c3-thm-matrix-composition',
        'c3-thm-matrix-addition', 'c3-thm-matrix-scaling',
        'c5-def-polynomial-operator',
    ],
    '9.64', '364',
)

s.r(
    'thm-characteristic-minimal-divisibility',
    'The minimal polynomial divides the characteristic polynomial',
    r'''Over $\R$ or $\C$, the minimal polynomial of $T$ divides its characteristic polynomial. If the minimal polynomial has degree $\dim V$, these two monic polynomials are equal.''',
    r'''Cayley–Hamilton says that the characteristic polynomial annihilates $T$. Every annihilating polynomial is divisible by the minimal polynomial, so write $q_T=pr$, where $p$ is minimal.
    If $\deg p=\dim V$, then $\deg p=\deg q_T$. The product-degree formula forces $r$ to be constant. Both $p$ and $q_T$ are monic, so that constant is $1$. Thus $p=q_T$. This also covers dimension zero, where both are $1$.''',
    1, 15,
    [r'''Apply the characterization of all annihilating polynomials to Cayley–Hamilton.'''],
    [
        'thm-cayley-hamilton-real-complex', 'thm-characteristic-degree-roots',
        'c5-thm-annihilating-divisibility', 'c4-lem-polynomial-product-degree',
    ],
    '', '364',
)

s.r(
    'thm-characteristic-coefficients',
    'Trace and determinant are characteristic-polynomial coefficients',
    r'''Let $n=\dim V$. The constant coefficient of $q_T$ is
    \[
    (-1)^n\det T.
    \]
    If $n\ge1$, the coefficient of $z^{n-1}$ is $-\tr T$. For $n=1$, this says $q_T(z)=z-\tr T=z-\det T$. For $n\ge2$, the coefficients occur in the expansion
    \[
    q_T(z)=z^n-(\tr T)z^{n-1}+\cdots+(-1)^n\det T.
    \]
    When $n=0$, the polynomial is $1$.''',
    r'''Evaluation at zero gives the constant coefficient:
    \[
    q_T(0)=\det(-T)=(-1)^n\det T.
    \]
    To identify the other coefficient, assume $n\ge1$, choose a basis, and write $A$ for the matrix of $T$. The identity-permutation term in $\det(zI-A)$ is
    \[
    \prod_{j=1}^n(z-A_{j,j}).
    \]
    A term of degree $n-1$ in this product is obtained by choosing $-A_{j,j}$ from one factor and $z$ from all others. Its total coefficient is therefore $-\sum_jA_{j,j}=-\tr T$.
    As established in the degree proof, every nonidentity permutation term has degree at most $n-2$, and there are no such terms for $n=1$. They contribute nothing to the coefficient of $z^{n-1}$. This proves the claim. For $n=0$, the separate formula $q_T=1$ applies.''',
    2, 25,
    [
        r'''The constant coefficient is the value at $z=0$.''',
        r'''For the next-to-leading coefficient, only the identity-permutation term contributes.''',
    ],
    [
        'thm-characteristic-degree-roots', 'thm-determinant-scaling',
        'thm-determinant-formula', 'c8-def-operator-trace',
        'c8-def-matrix-trace',
    ],
    '9.65', '364',
)

s.r(
    'thm-hadamard',
    'Hadamard’s inequality',
    r'''If the columns of an $n$-by-$n$ real or complex matrix $A$ are $v_1,\ldots,v_n$, then
    \[
    |\det A|\le\prod_{j=1}^n\norm{v_j},
    \]
    where the norms come from the standard inner product.''',
    r'''For $n=0$, both sides are $1$. If $A$ is not invertible, its determinant is zero, whereas the product of column norms is nonnegative, so the inequality holds.
    Suppose $A$ is invertible. Its QR factorization is $A=QR$, where $Q$ is unitary and $R$ is upper triangular with positive diagonal entries $r_{j,j}$. Multiplicativity, the unitary determinant formula, and the triangular determinant formula give
    \[
    |\det A|=\prod_{j=1}^n r_{j,j}.
    \]
    Let $r_j$ denote the $j$th column of $R$. In the standard norm,
    \[
    \norm{r_j}^2=\sum_{i=1}^n|r_{i,j}|^2\ge r_{j,j}^2,
    \]
    so $r_{j,j}\le\norm{r_j}$. Also $v_j=Qr_j$, and unitarity gives $\norm{v_j}=\norm{r_j}$. Multiplying the nonnegative inequalities yields
    \[
    |\det A|=\prod_jr_{j,j}\le\prod_j\norm{r_j}
    =\prod_j\norm{v_j}.
    \]''',
    3, 35,
    [
        r'''Separate the singular case, then use QR factorization.''',
        r'''Bound each positive diagonal entry of the triangular factor by the norm of its column.''',
    ],
    [
        'cor-matrix-determinant-invertible', 'thm-determinant-multiplicative',
        'thm-unitary-determinant', 'thm-triangular-determinant',
        'c7-thm-qr', 'c7-thm-unitary-matrix-equivalences',
    ],
    '9.66', '365',
)

s.r(
    'cor-parallelepiped-determinant',
    'Determinants measure the volume generated by edges',
    r'''For $v_1,\ldots,v_n\in\R^n$, set
    \[
    P=\left\{\sum_{j=1}^n t_jv_j:0<t_j<1\text{ for every }j\right\},
    \qquad A=(v_1\ \cdots\ v_n).
    \]
    Then $P$ is measurable and
    \[
    \Vol(P)=|\det A|\le\prod_{j=1}^n\norm{v_j}.
    \]
    When the edges are pairwise orthogonal, equality holds. For prescribed nonnegative edge lengths, orthogonal choices therefore attain the largest possible volume.''',
    r'''Let $T$ have standard matrix $A$. The set $P$ is the image under $T$ of the open unit cube, which is measurable and has volume $1$. The determinant volume theorem gives
    $\Vol(P)=|\det T|=|\det A|$, including a singular $T$. Hadamard's inequality gives the bound.
    If the edges are pairwise orthogonal and all nonzero, divide each edge by its positive norm. The resulting list is orthonormal and hence independent. Its length is $n$, so it is an orthonormal basis. The original set is therefore a box with the stated edge lengths, whose product is its volume. If one edge is zero, the determinant has a zero column, so both the volume and the product of lengths are zero. In dimension zero, the set is the singleton zero space and both quantities are $1$.
    Finally, for any prescribed lengths $\ell_1,\ldots,\ell_n\ge0$, the vectors $\ell_1e_1,\ldots,\ell_ne_n$ are pairwise orthogonal and attain the product $\prod_j\ell_j$. The bound shows that no choice with those lengths has larger volume.''',
    2, 20,
    [r'''View the generated set as the image of the unit cube under the matrix with the given columns.'''],
    [
        'thm-determinant-volume', 'thm-hadamard',
        'thm-determinant-columns', 'c7-thm-lebesgue-prerequisites',
        'c7-def-box-volume', 'c6-thm-orthonormal-independent', 'c2-thm-full-length-independent',
    ],
    '', '365', kind='corollary',
)

s.r(
    'thm-vandermonde',
    'The Vandermonde determinant',
    r'''For $\beta_1,\ldots,\beta_n\in\F$, let $A$ be the matrix
    \[
    A_{i,j}=\beta_i^{\,j-1}\qquad(1\le i,j\le n).
    \]
    Then
    \[
    \det A=\prod_{1\le j<k\le n}(\beta_k-\beta_j).
    \]
    The formula includes repeated scalars and the cases $n=0$ and $n=1$, with empty products equal to $1$.''',
    r'''For $n=0$, both sides are $1$. Suppose $n\ge1$, and define
    \[
    q_0(z)=1,\qquad q_j(z)=\prod_{\ell=1}^j(z-\beta_\ell)
    \quad(1\le j<n).
    \]
    Let the $j$th column of $B$ be the coefficient vector of $q_{j-1}$ in the ordered monomial basis $1,z,\ldots,z^{n-1}$. The polynomial $q_{j-1}$ is monic of degree $j-1$. Hence the entries below position $j$ in column $j$ are zero and its diagonal entry is $1$. Thus $B$ is upper triangular with $\det B=1$.
    For $C=AB$, the matrix product formula gives
    \[
    C_{i,j}=q_{j-1}(\beta_i).
    \]
    Indeed, row $i$ of $A$ evaluates a coefficient vector at $\beta_i$. If $i<j$, the product defining $q_{j-1}$ contains the factor $z-\beta_i$, so $C_{i,j}=0$. Thus $C$ is lower triangular, with diagonal entries
    \[
    C_{i,i}=\prod_{\ell=1}^{i-1}(\beta_i-\beta_\ell).
    \]
    Its transpose is upper triangular. Transpose invariance and the triangular determinant formula yield
    \[
    \det C
    =\prod_{i=1}^n\prod_{\ell=1}^{i-1}(\beta_i-\beta_\ell).
    \]
    Finally, multiplicativity gives $\det C=(\det A)(\det B)=\det A$. The double product is the desired product over all pairs $j<k$. No division by any difference was used, so the argument also covers repeated values of the $\beta_i$.''',
    4, 60,
    [
        r'''Replace the monomials by $1,(z-\beta_1),(z-\beta_1)(z-\beta_2),\ldots$.''',
        r'''The coefficient-change matrix is upper triangular with diagonal entries $1$.''',
        r'''Evaluating the new polynomials at the $\beta_i$ produces a lower-triangular matrix.''',
    ],
    [
        'thm-triangular-determinant', 'thm-determinant-multiplicative',
        'thm-determinant-transpose-dual-adjoint', 'c3-def-matrix-product',
        'c2-ex-polynomial-dimension', 'c4-lem-polynomial-product-degree',
    ],
    '9.67', '366',
)

s.card(
    'determinant-definition',
    'def-determinant',
    r'''How is the determinant of an operator defined without choosing a basis?''',
    r'''It is the scalar by which applying the operator to every argument multiplies every alternating form of degree $\dim V$.''',
)

s.card(
    'determinant-columns',
    'thm-determinant-columns',
    r'''Which properties characterize determinant as a function of the columns?''',
    r'''It is alternating and multilinear, and its value on the standard basis columns is $1$.''',
)

s.card(
    'determinant-multiplication',
    'thm-determinant-multiplicative',
    r'''State the product rule for determinants.''',
    r'''For operators on one space, $\det(ST)=(\det S)(\det T)$; for same-sized square matrices, $\det(AB)=(\det A)(\det B)$.''',
)

s.card(
    'determinant-invertibility',
    'thm-determinant-invertible',
    r'''How does determinant detect invertibility, and what is the determinant of an inverse?''',
    r'''An operator is invertible exactly when its determinant is nonzero. In that case, $\det(T^{-1})=1/\det T$.''',
)

s.card(
    'determinant-row-rules',
    'thm-determinant-row-column-operations',
    r'''How do a row swap, row scaling, and adding a multiple of another row affect determinant?''',
    r'''A swap changes the sign; scaling multiplies the determinant by the same scalar; adding a multiple of a different row leaves it unchanged. The same rules hold for columns.''',
)

s.card(
    'determinant-adjoint',
    'thm-determinant-transpose-dual-adjoint',
    r'''What happens to a determinant under transpose or adjoint?''',
    r'''Transpose leaves a determinant unchanged. Taking an adjoint conjugates it: $\det(T^*)=\overline{\det T}$.''',
)

s.card(
    'determinant-volume',
    'thm-determinant-volume',
    r'''What is the volume multiplier of a real invertible linear map?''',
    r'''It is $|\det T|$. A singular map sends every set into a proper subspace, so its image has ambient volume zero.''',
)

s.card(
    'characteristic-trace-determinant',
    'thm-characteristic-coefficients',
    r'''Where do trace and determinant appear in the characteristic polynomial?''',
    r'''For positive dimension $n$, the coefficient of $z^{n-1}$ is $-\tr T$. The constant coefficient is $(-1)^n\det T$.''',
)

s.card(
    'hadamard',
    'thm-hadamard',
    r'''State Hadamard's inequality for a square matrix with columns $v_1,\ldots,v_n$.''',
    r'''It states $|\det A|\le\prod_{j=1}^n\norm{v_j}$.''',
)

s.card(
    'vandermonde',
    'thm-vandermonde',
    r'''What is the determinant of the matrix with entries $A_{i,j}=\beta_i^{j-1}$?''',
    r'''It is $\prod_{1\le j<k\le n}(\beta_k-\beta_j)$.''',
)

s.write()