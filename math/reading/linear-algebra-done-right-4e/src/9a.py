from common import Section

s = Section('9a')

s.p(
    'intro-bilinear-quadratic',
    'Forms that are linear in two arguments',
    r'''Throughout this section, $V$ is a finite-dimensional vector space over $\F$, where $\F$ is $\R$ or $\C$. A bilinear form is linear in each argument separately. In the complex case, this differs from an inner product, whose second argument is conjugate-linear.''',
    333,
)

s.d(
    'def-bilinear-form',
    'Bilinear forms',
    r'''A bilinear form on $V$ is a function $\beta:V\times V\to\F$ such that, for each fixed $w\in V$, both functions
    \[
    v\longmapsto\beta(v,w),
    \qquad
    v\longmapsto\beta(w,v)
    \]
    are linear functionals. Thus scalars leave either argument without complex conjugation.''',
    '9.1', 333,
)

s.r(
    'lem-bilinear-expansion',
    'Expanding a bilinear form',
    r'''Every bilinear form satisfies $\beta(0,v)=\beta(v,0)=0$. For finite lists of vectors and scalars,
    \[
    \beta\left(\sum_{j=1}^r a_ju_j,\sum_{k=1}^t b_kv_k\right)
    =
    \sum_{j=1}^r\sum_{k=1}^t a_jb_k\beta(u_j,v_k).
    \]
    This includes empty sums.''',
    r'''Fixing either argument gives a linear functional, and a linear map takes zero to zero. This proves the two zero identities. Repeated additivity and homogeneity in the first argument give
    \[
    \beta\left(\sum_j a_ju_j,\sum_k b_kv_k\right)
    =\sum_j a_j\beta\left(u_j,\sum_k b_kv_k\right).
    \]
    Applying additivity and homogeneity in the second argument to each term gives the double sum. Each finite expansion follows by induction on the number of terms from the two-term linearity rule. If either list is empty, the corresponding argument is zero, and both sides vanish by the zero identities.''',
    1, 10,
    [r'''Apply linearity to one argument at a time.'''],
    ['def-bilinear-form', 'c3-thm-linear-zero', 'c1-foundations'],
    page=333, kind='lemma',
)

s.r(
    'ex-inner-product-bilinearity',
    'When an inner product is bilinear',
    r'''An inner product on a real vector space is a bilinear form. On a nonzero complex inner product space, its inner-product function is not bilinear.''',
    r'''Over $\R$, conjugating a scalar leaves it unchanged. Thus the inner product is linear in the second argument as well as the first, proving bilinearity.

    Over $\C$, choose $v\ne0$. Conjugate homogeneity gives
    \[
    \ip{v}{iv}=-i\ip{v}{v}.
    \]
    If the function were bilinear, homogeneity in the second argument would instead give $\ip{v}{iv}=i\ip{v}{v}$. These equations imply $2i\ip{v}{v}=0$. Since $2i\ne0$, scalar cancellation would give $\ip{v}{v}=0$, contradicting positive definiteness. On the zero complex space the inner-product function is the zero bilinear form, explaining the nonzero hypothesis.''',
    1, 10,
    [r'''In the complex case, test multiplication by $i$ in the second argument.'''],
    ['def-bilinear-form', 'c6-def-inner-product',
     'c6-thm-inner-product-properties', 'c1-lem-scalar-cancellation'],
    page=333, kind='example',
)

s.r(
    'ex-coordinate-bilinear',
    'A coordinate formula with mixed indices',
    r'''The function on $\F^3\times\F^3$ given by
    \[
    \beta(x,y)=x_1y_2-5x_2y_3+2x_3y_1
    \]
    is a bilinear form.''',
    r'''For fixed $y$ and scalars $a,b$,
    \[
    \begin{aligned}
    \beta(ax+bx',y)
    &=(ax_1+bx'_1)y_2-5(ax_2+bx'_2)y_3
      +2(ax_3+bx'_3)y_1\\
    &=a\beta(x,y)+b\beta(x',y).
    \end{aligned}
    \]
    For fixed $x$, expansion in the other coordinates gives
    \[
    \begin{aligned}
    \beta(x,ay+by')
    &=x_1(ay_2+by'_2)-5x_2(ay_3+by'_3)
      +2x_3(ay_1+by'_1)\\
    &=a\beta(x,y)+b\beta(x,y').
    \end{aligned}
    \]
    These are the two required linearity conditions.''',
    1, 10,
    [r'''Check a linear combination in each argument separately.'''],
    ['def-bilinear-form', 'c1-def-coordinate-space'],
    '9.2(a)', 333, 'example',
)

s.r(
    'ex-matrix-bilinear',
    'A bilinear form from any square matrix',
    r'''For $A\in\F^{n,n}$, the formula
    \[
    \beta_A(x,y)=\sum_{j=1}^n\sum_{k=1}^n A_{jk}x_jy_k
    \]
    defines a bilinear form on $\F^n$. The preceding coordinate example corresponds to
    \[
    A=
    \begin{pmatrix}
    0&1&0\\
    0&0&-5\\
    2&0&0
    \end{pmatrix}.
    \]''',
    r'''For fixed $y$,
    \[
    \beta_A(ax+bx',y)
    =\sum_{j,k}A_{jk}(ax_j+bx'_j)y_k
    =a\beta_A(x,y)+b\beta_A(x',y).
    \]
    For fixed $x$,
    \[
    \beta_A(x,ay+by')
    =\sum_{j,k}A_{jk}x_j(ay_k+by'_k)
    =a\beta_A(x,y)+b\beta_A(x,y').
    \]
    Hence the form is bilinear. In the displayed matrix, only the entries with indices $(1,2),(2,3),(3,1)$ are nonzero, and substituting them gives exactly the preceding formula. For $n=0$, the formula is the empty sum zero and defines the unique bilinear form on the zero space.''',
    1, 10,
    [r'''Distribute a scalar linear combination inside the double sum.'''],
    ['def-bilinear-form', 'c3-def-matrix-space',
     'c1-def-coordinate-space'],
    '9.2(b)', 333, 'example',
)

s.r(
    'ex-operator-bilinear',
    'A real inner product composed with an operator',
    r'''If $V$ is a real inner product space and $T\in\Lin(V)$, then
    \[
    \beta(u,v)=\ip{u}{Tv}
    \]
    is a bilinear form.''',
    r'''For real scalars $a,b$,
    \[
    \beta(au+bu',v)
    =\ip{au+bu'}{Tv}
    =a\beta(u,v)+b\beta(u',v).
    \]
    Linearity of $T$ and real linearity in the second inner-product argument give
    \[
    \beta(u,av+bv')
    =\ip{u}{aTv+bTv'}
    =a\beta(u,v)+b\beta(u,v').
    \]
    Thus both arguments satisfy the required linearity.''',
    1, 10,
    [r'''Use linearity of $T$ for the second argument.'''],
    ['def-bilinear-form', 'ex-inner-product-bilinearity',
     'c3-def-linear-map'],
    '9.2(c)', 334, 'example',
)

s.r(
    'ex-polynomial-bilinear',
    'Evaluation multiplied by derivative evaluation',
    r'''For every integer $n\ge0$, the function
    \[
    \beta(p,q)=p(2)q'(3)
    \qquad(p,q\in\Poly_n(\R))
    \]
    is a bilinear form.''',
    r'''Evaluation is linear because
    $(ap+br)(2)=ap(2)+br(2)$. Polynomial differentiation is linear, so
    $(aq+br)'(3)=aq'(3)+br'(3)$. Therefore, for fixed $q$,
    \[
    \beta(ap+br,q)
    =(ap(2)+br(2))q'(3)
    =a\beta(p,q)+b\beta(r,q).
    \]
    For fixed $p$,
    \[
    \beta(p,aq+br)
    =p(2)(aq'(3)+br'(3))
    =a\beta(p,q)+b\beta(p,r).
    \]
    This proves bilinearity. For $n=0$, every derivative is zero, so the same formula is the zero bilinear form.''',
    1, 10,
    [r'''Evaluation and derivative evaluation are linear functionals.'''],
    ['def-bilinear-form', 'c3-ex-polynomial-differentiation',
     'c2-def-polynomial-space'],
    '9.2(d)', 334, 'example',
)

s.r(
    'ex-functional-products-bilinear',
    'Products and sums of linear functionals',
    r'''If $\varphi,\tau\in\dual V$, then
    \[
    \beta(u,v)=\varphi(u)\tau(v)
    \]
    is bilinear. More generally, if $\varphi_1,\ldots,\varphi_m,\tau_1,\ldots,\tau_m\in\dual V$, then
    \[
    \beta(u,v)=\sum_{j=1}^m\varphi_j(u)\tau_j(v)
    \]
    is bilinear, including the zero form when $m=0$.''',
    r'''For the sum formula and fixed $v$, linearity of every $\varphi_j$ gives
    \[
    \beta(au+bu',v)
    =\sum_j(a\varphi_j(u)+b\varphi_j(u'))\tau_j(v)
    =a\beta(u,v)+b\beta(u',v).
    \]
    For fixed $u$, linearity of every $\tau_j$ gives
    \[
    \beta(u,av+bv')
    =\sum_j\varphi_j(u)(a\tau_j(v)+b\tau_j(v'))
    =a\beta(u,v)+b\beta(u,v').
    \]
    Thus the sum is bilinear. Taking $m=1$ gives the first assertion. For $m=0$, both displayed linearity identities are identities between zeros.''',
    1, 10,
    [r'''Hold one argument fixed and distribute the linear functionals in the other argument.'''],
    ['def-bilinear-form', 'c3-def-linear-functional',
     'c3-def-dual-space'],
    '9.2(e,f)', 334, 'example',
)

s.r(
    'lem-bilinear-joint-linearity',
    'Separate linearity is different from linearity on the product',
    r'''A bilinear form $\beta$ is also a linear functional on the product vector space $V\times V$ if and only if $\beta=0$.''',
    r'''Suppose $\beta$ is linear on the product. Since
    $(u,v)=(u,0)+(0,v)$, joint additivity gives
    \[
    \beta(u,v)=\beta(u,0)+\beta(0,v)=0
    \]
    by the zero identities for a bilinear form. Thus $\beta$ is the zero function. Conversely, the zero function satisfies both separate linearity and linearity on the product, because every linearity equation has value zero on both sides.''',
    1, 10,
    [r'''Decompose $(u,v)$ as $(u,0)+(0,v)$.'''],
    ['lem-bilinear-expansion', 'c3-def-product-space',
     'c3-def-linear-functional'],
    page=334, kind='lemma',
)

s.d(
    'def-bilinear-space',
    'The collection of bilinear forms',
    r'''Write $V^{(2)}$, also denoted $\Bil(V)$, for the set of bilinear forms on $V$. Equip it with pointwise operations:
    \[
    (\alpha+\beta)(u,v)=\alpha(u,v)+\beta(u,v),
    \qquad
    (a\beta)(u,v)=a\beta(u,v).
    \]''',
    '9.3', 334,
)

s.r(
    'thm-bilinear-space',
    'Bilinear forms constitute a vector space',
    r'''The set $V^{(2)}$ is a vector subspace of the space of all functions from $V\times V$ to $\F$.''',
    r'''The zero function is bilinear. If $\alpha,\beta$ are bilinear and $a,b\in\F$, fix $v$. The function
    $u\mapsto a\alpha(u,v)+b\beta(u,v)$
    is a linear combination of linear functionals and hence is linear. Explicitly, its value at $cu+du'$ is the corresponding sum of $c$ times its value at $u$ and $d$ times its value at $u'$, by distributing $a,b$ through the linearity identities for $\alpha,\beta$. Fixing $u$ gives the same conclusion for the function of $v$, using linearity in the second argument. Thus $a\alpha+b\beta$ is bilinear. The subspace test applies inside the function space and proves the assertion.''',
    1, 10,
    [r'''Use the subspace test with pointwise operations.'''],
    ['def-bilinear-space', 'def-bilinear-form',
     'c1-thm-function-space', 'c1-thm-subspace-test'],
    page=334,
)

s.d(
    'def-bilinear-matrix',
    'The matrix of a bilinear form',
    r'''For a basis $\mathcal E=(e_1,\ldots,e_n)$, define
    \[
    \Mat(\beta,\mathcal E)_{jk}=\beta(e_j,e_k).
    \]
    When the basis is fixed, write simply $\Mat(\beta)$. This is an $n$-by-$n$ matrix; on the zero space it is the empty square matrix.''',
    '9.4', 334,
)

s.r(
    'thm-bilinear-matrix-isomorphism',
    'Matrices describe all bilinear forms',
    r'''For a fixed basis $\mathcal E=(e_1,\ldots,e_n)$, the map
    \[
    V^{(2)}\longrightarrow\F^{n,n},
    \qquad
    \beta\longmapsto\Mat(\beta,\mathcal E)
    \]
    is an isomorphism. In particular,
    \[
    \dim V^{(2)}=(\dim V)^2.
    \]
    If $A=\Mat(\beta,\mathcal E)$, then
    \[
    \beta\left(\sum_jx_je_j,\sum_ky_ke_k\right)
    =\sum_{j,k}A_{jk}x_jy_k.
    \]''',
    r'''The final formula follows from bilinear expansion. It shows that the matrix determines all values of $\beta$, because every vector has unique coordinates in the chosen basis.

    For forms $\alpha,\beta$ and scalars $a,b$, each matrix entry satisfies
    \[
    \Mat(a\alpha+b\beta)_{jk}
    =a\alpha(e_j,e_k)+b\beta(e_j,e_k),
    \]
    so the matrix correspondence is linear. If its value at $\beta$ is the zero matrix, the coordinate formula gives $\beta(u,v)=0$ for every pair. Therefore it is injective.

    Given any matrix $A$, use the coordinate formula to define a function $\beta_A$ on $V\times V$. Unique coordinates make this definition well-defined. Coordinates of a vector linear combination are the same linear combination of coordinate lists, by basis independence. Distributing those coordinates in the double sum proves linearity of $\beta_A$ in each argument, exactly as for the coordinate-space matrix example. Substituting $u=e_j,v=e_k$ gives $\beta_A(e_j,e_k)=A_{jk}$. Thus the correspondence is surjective and is an isomorphism.

    For completeness, transport any basis of $\F^{n,n}$ through its inverse. The transported list spans $V^{(2)}$, because the image of any form expands in the matrix basis. It is independent, because applying the isomorphism to a zero combination gives a zero combination in that matrix basis. Hence the two dimensions agree. The matrix-space dimension is $n^2$, proving the formula. If $n=0$, bilinearity forces the sole value $\beta(0,0)$ to be zero, so both spaces have dimension zero and the same argument uses empty bases.''',
    2, 25,
    [r'''Expand both arguments in the fixed basis.''',
     r'''Given a matrix, use its entries as coefficients of a bilinear coordinate formula.'''],
    ['def-bilinear-matrix', 'thm-bilinear-space',
     'lem-bilinear-expansion', 'ex-matrix-bilinear',
     'c2-thm-basis-coordinates', 'c3-def-isomorphism',
     'c3-thm-matrix-space-dimension'],
    '9.5', 335,
)

s.r(
    'thm-bilinear-composition',
    'Composing a bilinear form with an operator',
    r'''Let $\beta\in V^{(2)}$ and $T\in\Lin(V)$. Define
    \[
    \alpha(u,v)=\beta(u,Tv),
    \qquad
    \rho(u,v)=\beta(Tu,v).
    \]
    Both functions are bilinear. In any one fixed basis,
    \[
    \Mat(\alpha)=\Mat(\beta)\Mat(T),
    \qquad
    \Mat(\rho)=\Mat(T)^{\mathsf t}\Mat(\beta).
    \]
    The superscript $\mathsf t$ means ordinary transpose, without conjugation.''',
    r'''Fixing one argument of either function leaves a composition of linear maps, or a fixed-argument linear functional of $\beta$. More explicitly, linearity of $T$ and of $\beta$ gives
    \[
    \alpha(u,av+bw)=a\alpha(u,v)+b\alpha(u,w),
    \quad
    \rho(au+bw,v)=a\rho(u,v)+b\rho(w,v),
    \]
    while linearity in the other argument follows directly from $\beta$. Thus both are bilinear.

    Write $B=\Mat(\beta)$ and $M=\Mat(T)$ in a basis $e_1,\ldots,e_n$. Since $Te_k=\sum_\ell M_{\ell k}e_\ell$,
    \[
    \Mat(\alpha)_{jk}
    =\beta(e_j,Te_k)
    =\sum_\ell B_{j\ell}M_{\ell k}
    =(BM)_{jk}.
    \]
    Likewise,
    \[
    \Mat(\rho)_{jk}
    =\beta(Te_j,e_k)
    =\sum_\ell M_{\ell j}B_{\ell k}
    =(M^{\mathsf t}B)_{jk}.
    \]
    Equality of entries proves both matrix identities. In dimension zero all matrices are empty and both equalities hold.''',
    2, 20,
    [r'''Expand $Te_k$ using column $k$ of its matrix.''',
     r'''In the first argument, the indices of the operator matrix enter in transposed order.'''],
    ['def-bilinear-form', 'def-bilinear-matrix',
     'lem-bilinear-expansion', 'c3-def-map-matrix',
     'c3-def-matrix-product', 'c3-def-transpose'],
    '9.6', 335,
)

s.r(
    'thm-bilinear-basis-change',
    'The change-of-basis formula for a bilinear form',
    r'''Let $\mathcal E=(e_1,\ldots,e_n)$ and $\mathcal F=(f_1,\ldots,f_n)$ be bases. Put
    \[
    A=\Mat(\beta,\mathcal E),\qquad
    B=\Mat(\beta,\mathcal F),
    \]
    and let $C=\Mat(I,\mathcal E,\mathcal F)$, so column $k$ of $C$ is the $\mathcal F$-coordinate list of $e_k$. Then
    \[
    A=C^{\mathsf t}BC.
    \]''',
    r'''By the definition of $C$, one has $e_j=\sum_r C_{rj}f_r$ for every $j$. Bilinear expansion gives
    \[
    \begin{aligned}
    A_{jk}
    &=\beta(e_j,e_k)\\
    &=\sum_{r,\ell}C_{rj}C_{\ell k}\beta(f_r,f_\ell)\\
    &=\sum_{r,\ell}(C^{\mathsf t})_{jr}B_{r\ell}C_{\ell k}
    =(C^{\mathsf t}BC)_{jk}.
    \end{aligned}
    \]
    This proves equality of the matrices. The formula uses the transpose rather than a conjugate transpose because scalars leave both bilinear arguments unchanged. Empty matrices give the same identity in dimension zero.''',
    2, 20,
    [r'''Write each old basis vector in the new basis and expand both arguments.'''],
    ['def-bilinear-matrix', 'lem-bilinear-expansion',
     'c3-def-map-matrix', 'c3-def-matrix-product',
     'c3-def-transpose'],
    '9.7', 336,
)

s.r(
    'ex-polynomial-bilinear-matrices',
    'A polynomial form in two bases',
    r'''On $\Poly_2(\R)$ let $\beta(p,q)=p(2)q'(3)$, and consider
    \[
    \mathcal E=(1,x-2,(x-3)^2),
    \qquad
    \mathcal F=(1,x,x^2).
    \]
    These are bases, and
    \[
    A=\Mat(\beta,\mathcal E)=
    \begin{pmatrix}0&1&0\\0&0&0\\0&1&0\end{pmatrix},
    \quad
    B=\Mat(\beta,\mathcal F)=
    \begin{pmatrix}0&1&6\\0&2&12\\0&4&24\end{pmatrix}.
    \]
    Moreover,
    \[
    C=\Mat(I,\mathcal E,\mathcal F)=
    \begin{pmatrix}1&-2&9\\0&1&-6\\0&0&1\end{pmatrix},
    \qquad A=C^{\mathsf t}BC.
    \]''',
    r'''The standard monomial list $\mathcal F$ is a basis of $\Poly_2(\R)$. Expanding a combination from $\mathcal E$ gives
    \[
    a+b(x-2)+c(x-3)^2
    =(a-2b+9c)+(b-6c)x+cx^2.
    \]
    Given any three polynomial coefficients, the coefficient of $x^2$ determines $c$, the coefficient of $x$ then determines $b$, and the constant coefficient determines $a$. Thus the expansion in $\mathcal E$ exists uniquely, proving that $\mathcal E$ is a basis.

    Evaluation at $2$ on the $\mathcal E$ list gives $(1,0,1)$, while derivative evaluation at $3$ gives $(0,1,0)$. Each matrix entry is the product of the corresponding value from these two lists, yielding $A$. On $\mathcal F$, those lists are $(1,2,4)$ and $(0,1,6)$, yielding $B$.

    The monomial coordinates of the three $\mathcal E$ vectors are the three columns displayed in $C$, proving its formula. Direct multiplication gives
    \[
    BC=
    \begin{pmatrix}0&1&0\\0&2&0\\0&4&0\end{pmatrix},
    \qquad
    C^{\mathsf t}BC=
    \begin{pmatrix}0&1&0\\0&0&0\\0&1&0\end{pmatrix}=A.
    \]
    This also verifies the change-of-basis identity numerically.''',
    2, 20,
    [r'''Compute the evaluation list and derivative-evaluation list separately.''',
     r'''The change-of-basis columns are the monomial coefficients of the three shifted polynomials.'''],
    ['ex-polynomial-bilinear', 'def-bilinear-matrix',
     'thm-bilinear-basis-change', 'c2-def-polynomial-space',
     'c2-lem-polynomial-coefficients', 'c2-thm-basis-coordinates',
     'c3-def-map-matrix', 'c3-def-matrix-product',
     'c3-ex-polynomial-differentiation'],
    '9.8', 336, 'example',
)

s.d(
    'def-symmetric-bilinear',
    'Symmetric bilinear forms',
    r'''A bilinear form $\rho$ is symmetric if
    \[
    \rho(u,v)=\rho(v,u)\qquad(u,v\in V).
    \]
    Write $V_{\mathrm{sym}}^{(2)}$ for the set of symmetric bilinear forms.''',
    '9.9', 337,
)

s.r(
    'ex-symmetric-inner-product',
    'Symmetric forms arising from real inner products',
    r'''A real inner product is a symmetric bilinear form. More generally, for $T\in\Lin(V)$ on a real inner product space, the form
    \[
    \rho(u,v)=\ip{u}{Tv}
    \]
    is symmetric if and only if $T$ is self-adjoint.''',
    r'''A real inner product is bilinear by the earlier example and symmetric because conjugate symmetry becomes ordinary symmetry over $\R$.

    The more general formula is bilinear by the operator-composition example. Suppose $T$ is self-adjoint. Then
    \[
    \rho(u,v)=\ip{u}{Tv}=\ip{Tu}{v}=\ip{v}{Tu}=\rho(v,u),
    \]
    using self-adjointness and real symmetry of the inner product. Conversely, if $\rho$ is symmetric, then
    \[
    \ip{u}{Tv}=\rho(u,v)=\rho(v,u)=\ip{v}{Tu}=\ip{Tu}{v}
    \]
    for every $u,v$. The inner-product test for self-adjointness now gives $T=T^*$.''',
    2, 15,
    [r'''Translate symmetry of the form into the inner-product criterion for self-adjointness.'''],
    ['def-symmetric-bilinear', 'ex-inner-product-bilinearity',
     'ex-operator-bilinear', 'c7-thm-self-adjoint-tests',
     'c6-thm-inner-product-properties'],
    '9.10(a,b)', 337, 'example',
)

s.r(
    'ex-trace-bilinear',
    'Trace of a product is a symmetric bilinear form',
    r'''The function on $\Lin(V)\times\Lin(V)$ defined by
    \[
    \rho(S,T)=\tr(ST)
    \]
    is a symmetric bilinear form.''',
    r'''For scalars $a,b$, distributivity of composition and linearity of trace give
    \[
    \rho(aS+bR,T)
    =\tr(aST+bRT)
    =a\rho(S,T)+b\rho(R,T).
    \]
    In the second argument they give
    \[
    \rho(S,aT+bR)
    =\tr(aST+bSR)
    =a\rho(S,T)+b\rho(S,R).
    \]
    Thus $\rho$ is bilinear. Cyclicity of trace gives
    $\rho(S,T)=\tr(ST)=\tr(TS)=\rho(T,S)$, proving symmetry. The zero-dimensional case gives the zero form and is included in the trace identities.''',
    1, 10,
    [r'''Use linearity of trace and the equality $\tr(ST)=\tr(TS)$.'''],
    ['def-bilinear-form', 'def-symmetric-bilinear',
     'c8-thm-trace-linear-cyclic', 'c3-thm-composition-laws',
     'c3-thm-linear-map-space'],
    '9.10(c)', 337, 'example',
)

s.d(
    'def-symmetric-matrix',
    'Symmetric matrices',
    r'''A square matrix $A$ is symmetric if $A=A^{\mathsf t}$. Over $\C$, this still means ordinary transpose and does not mean equality with the conjugate transpose.''',
    '9.11', 337,
)

s.r(
    'lem-symmetric-diagonal-detection',
    'Diagonal values detect a symmetric bilinear form',
    r'''For a symmetric bilinear form $\rho$,
    \[
    2\rho(u,v)
    =\rho(u+v,u+v)-\rho(u,u)-\rho(v,v).
    \]
    Consequently, if $\rho\ne0$, there is a vector $w$ such that $\rho(w,w)\ne0$.''',
    r'''Expanding both arguments gives
    \[
    \rho(u+v,u+v)
    =\rho(u,u)+\rho(u,v)+\rho(v,u)+\rho(v,v).
    \]
    Symmetry identifies the middle two terms, giving the formula. If every diagonal value were zero, that formula would imply $2\rho(u,v)=0$ for every $u,v$. Since $2\ne0$ in $\R$ and $\C$, scalar cancellation would give $\rho=0$. Taking the contrapositive proves the final assertion.''',
    1, 10,
    [r'''Expand the diagonal value at $u+v$.'''],
    ['def-symmetric-bilinear', 'lem-bilinear-expansion',
     'c1-lem-scalar-cancellation'],
    page=338, kind='lemma',
)

s.r(
    'thm-symmetric-diagonalization',
    'Symmetric forms admit diagonal matrices',
    r'''For a bilinear form $\rho$ on $V$, the following conditions are equivalent:
    \begin{enumerate}
    \item $\rho$ is symmetric.
    \item Its matrix is symmetric in every basis.
    \item Its matrix is symmetric in some basis.
    \item Its matrix is diagonal in some basis.
    \end{enumerate}
    This holds over both $\R$ and $\C$, including the zero space.''',
    r'''If $\rho$ is symmetric, then in every basis
    $\Mat(\rho)_{jk}=\rho(e_j,e_k)=\rho(e_k,e_j)=\Mat(\rho)_{kj}$,
    proving the second condition. Because every finite-dimensional space has a basis, the second condition implies the third.

    Suppose its matrix $A$ is symmetric in a basis $\mathcal E$. For $u=\sum_jx_je_j$ and $v=\sum_ky_ke_k$,
    \[
    \rho(u,v)=\sum_{j,k}A_{jk}x_jy_k
    =\sum_{j,k}A_{kj}x_jy_k
    =\rho(v,u),
    \]
    where the final equality is the coordinate expansion with the indices interchanged. Thus the third condition implies the first. Every diagonal matrix is symmetric, so the fourth condition implies the third.

    It remains to obtain a diagonal matrix from symmetry. We use induction on $n=\dim V$. For $n=0$, the empty basis gives the empty diagonal matrix. Assume $n>0$ and that the assertion holds in all smaller dimensions. If $\rho=0$, any basis gives a zero, hence diagonal, matrix. Otherwise the diagonal-detection lemma supplies $w$ with $d=\rho(w,w)\ne0$.

    Define
    \[
    U=\{u\in V:\rho(u,w)=0\}.
    \]
    The function $u\mapsto\rho(u,w)$ is linear, so $U$ is a subspace. Every $v\in V$ has the decomposition
    \[
    v=
    \left(v-\frac{\rho(v,w)}d\,w\right)
    +\frac{\rho(v,w)}d\,w,
    \]
    whose first term belongs to $U$. Moreover, if $aw\in U$, then $0=\rho(aw,w)=ad$, so $a=0$. Thus $V=U\oplus\Span(w)$.

    Choose a basis $u_1,\ldots,u_k$ of $U$. The decomposition just proved shows that $u_1,\ldots,u_k,w$ spans $V$. If a linear combination of this list is zero, applying $\rho(\,\cdot\,,w)$ forces the coefficient of $w$ to be zero; independence of the $u_j$ then forces all the other coefficients to vanish. Hence this list is a basis, and $k+1=n$. In particular, $\dim U=n-1$.

    The restriction of $\rho$ to $U\times U$ is still symmetric and bilinear. By induction it has a diagonal matrix in some basis $e_1,\ldots,e_{n-1}$ of $U$. Adjoining $w$ gives a basis of $V$ by the preceding argument. Every cross term involving $w$ vanishes: $\rho(e_j,w)=0$ by the definition of $U$, and $\rho(w,e_j)=0$ by symmetry. The other off-diagonal entries vanish by the induction hypothesis. Thus this basis gives a diagonal matrix, completing the equivalence.''',
    4, 70,
    [r'''First relate symmetry of the form to symmetry of its matrix.''',
     r'''For a nonzero symmetric form, find $w$ with $\rho(w,w)\ne0$.''',
     r'''Split off the line through $w$ using the kernel of $u\mapsto\rho(u,w)$, then induct on that kernel.'''],
    ['def-symmetric-bilinear', 'def-symmetric-matrix',
     'def-bilinear-matrix', 'thm-bilinear-matrix-isomorphism',
     'lem-symmetric-diagonal-detection', 'c3-thm-null-subspace',
     'c2-thm-basis-existence', 'c2-thm-subspaces-finite',
     'c2-def-dimension', 'c1-def-direct-sum',
     'c1-lem-scalar-cancellation'],
    '9.12', 337,
)

s.r(
    'cor-symmetric-matrix-congruence',
    'Diagonalizing a symmetric matrix by congruence',
    r'''For every symmetric matrix $A\in\F^{n,n}$, there is an invertible matrix $C$ such that $C^{\mathsf t}AC$ is diagonal.''',
    r'''The coordinate matrix construction defines a bilinear form $\beta_A$ on $\F^n$ whose matrix in the standard basis is $A$. Because that matrix is symmetric, the symmetric-form theorem makes $\beta_A$ symmetric and supplies a basis $\mathcal E$ in which its matrix is diagonal. Let $C$ have as its columns the standard coordinates of the vectors in $\mathcal E$. This is the matrix of the identity map from $\mathcal E$ coordinates to standard coordinates, so it is invertible. The bilinear change-of-basis formula gives
    $\Mat(\beta_A,\mathcal E)=C^{\mathsf t}AC$,
    proving the assertion. Empty matrices satisfy the same statement when $n=0$.''',
    2, 15,
    [r'''View the symmetric matrix as the matrix of a bilinear form.'''],
    ['ex-matrix-bilinear', 'thm-symmetric-diagonalization',
     'thm-bilinear-basis-change', 'c3-thm-matrix-inverse'],
    page=338, kind='corollary',
)

s.r(
    'thm-real-symmetric-orthonormal',
    'Orthonormal diagonalization of a real symmetric form',
    r'''If $V$ is a real inner product space and $\rho$ is a symmetric bilinear form on $V$, then some orthonormal basis gives a diagonal matrix for $\rho$.''',
    r'''Choose an orthonormal basis $f_1,\ldots,f_n$, and set $A_{jk}=\rho(f_j,f_k)$. Symmetry of $\rho$ gives a real symmetric matrix $A$. Define a linear operator by
    \[
    Tf_k=\sum_j A_{jk}f_j.
    \]
    Its matrix in the orthonormal basis is $A$, which equals its conjugate transpose because its entries are real and it is symmetric. Thus the adjoint-matrix formula makes $T$ self-adjoint.

    For $u=\sum_jx_jf_j$ and $v=\sum_ky_kf_k$, real orthonormal coordinates give
    \[
    \ip{u}{Tv}
    =\sum_{j,k}x_jA_{jk}y_k
    =\rho(u,v).
    \]
    The real spectral theorem provides an orthonormal eigenbasis $e_1,\ldots,e_n$ of $T$, with $Te_k=\lambda_ke_k$. In this basis,
    \[
    \rho(e_j,e_k)=\ip{e_j}{Te_k}
    =\lambda_k\ip{e_j}{e_k},
    \]
    which is zero when $j\ne k$. Hence the matrix of $\rho$ is diagonal. On the zero space the empty orthonormal basis already has the required property.''',
    3, 35,
    [r'''Use an orthonormal basis to turn the matrix of the form into the matrix of a self-adjoint operator.''',
     r'''Apply the real spectral theorem to that operator.'''],
    ['def-bilinear-matrix', 'thm-symmetric-diagonalization',
     'thm-bilinear-matrix-isomorphism',
     'c6-thm-orthonormal-basis-existence',
     'c6-thm-orthonormal-coordinates',
     'c7-thm-adjoint-matrix', 'c7-thm-real-spectral',
     'c3-thm-linear-map-basis'],
    '9.13', 339,
)

s.d(
    'def-alternating-bilinear',
    'Alternating bilinear forms',
    r'''A bilinear form $\alpha$ is alternating if
    \[
    \alpha(v,v)=0\qquad(v\in V).
    \]
    Write $V_{\mathrm{alt}}^{(2)}$ for the set of alternating bilinear forms.''',
    '9.14', 339,
)

s.r(
    'ex-alternating-coordinate',
    'An alternating coordinate expression',
    r'''For $n\ge3$, the formula
    \[
    \alpha(x,y)=x_1y_2-x_2y_1+x_1y_3-x_3y_1
    \]
    defines an alternating bilinear form on $\F^n$.''',
    r'''This is the matrix-coordinate bilinear form with nonzero entries
    $A_{12}=1$, $A_{21}=-1$, $A_{13}=1$, and $A_{31}=-1$, so it is bilinear. On the diagonal,
    \[
    \alpha(x,x)=x_1x_2-x_2x_1+x_1x_3-x_3x_1=0
    \]
    by commutativity of scalar multiplication. Therefore it is alternating.''',
    1, 10,
    [r'''Set the two arguments equal and cancel the scalar products.'''],
    ['def-alternating-bilinear', 'ex-matrix-bilinear'],
    '9.15(a)', 339, 'example',
)

s.r(
    'ex-alternating-functionals',
    'Alternating a product of two functionals',
    r'''For $\varphi,\tau\in\dual V$, the formula
    \[
    \alpha(u,v)=\varphi(u)\tau(v)-\varphi(v)\tau(u)
    \]
    defines an alternating bilinear form.''',
    r'''Both $(u,v)\mapsto\varphi(u)\tau(v)$ and
    $(u,v)\mapsto\tau(u)\varphi(v)$ are bilinear by the functional-product example. Their difference is bilinear because bilinear forms form a vector space. At equal arguments,
    $\alpha(v,v)=\varphi(v)\tau(v)-\varphi(v)\tau(v)=0$.
    Hence the form is alternating.''',
    1, 10,
    [r'''Use closure of bilinear forms under subtraction, then test equal arguments.'''],
    ['def-alternating-bilinear', 'ex-functional-products-bilinear',
     'thm-bilinear-space'],
    '9.15(b)', 339, 'example',
)

s.r(
    'thm-alternating-bilinear-test',
    'Alternation is antisymmetry',
    r'''A bilinear form $\alpha$ is alternating if and only if
    \[
    \alpha(u,v)=-\alpha(v,u)\qquad(u,v\in V).
    \]''',
    r'''If $\alpha$ is alternating, bilinear expansion yields
    \[
    0=\alpha(u+v,u+v)
    =\alpha(u,u)+\alpha(u,v)+\alpha(v,u)+\alpha(v,v).
    \]
    The two diagonal values are zero, so
    $\alpha(u,v)+\alpha(v,u)=0$, proving antisymmetry.

    Conversely, suppose the stated antisymmetry holds. Setting $u=v$ gives $\alpha(v,v)=-\alpha(v,v)$, hence $2\alpha(v,v)=0$. Because $2\ne0$ in $\F$, scalar cancellation gives $\alpha(v,v)=0$ for every $v$. This is alternation.''',
    1, 10,
    [r'''For one direction, evaluate at $u+v$ in both arguments; for the other, use equal arguments.'''],
    ['def-alternating-bilinear', 'lem-bilinear-expansion',
     'c1-lem-scalar-cancellation'],
    '9.16', 340,
)

s.r(
    'thm-bilinear-decomposition',
    'The symmetric and alternating parts',
    r'''The sets $V_{\mathrm{sym}}^{(2)}$ and $V_{\mathrm{alt}}^{(2)}$ are subspaces of $V^{(2)}$, and
    \[
    V^{(2)}
    =V_{\mathrm{sym}}^{(2)}
    \oplus V_{\mathrm{alt}}^{(2)}.
    \]
    The unique decomposition $\beta=\rho+\alpha$ is
    \[
    \rho(u,v)=\frac{\beta(u,v)+\beta(v,u)}2,
    \qquad
    \alpha(u,v)=\frac{\beta(u,v)-\beta(v,u)}2.
    \]''',
    r'''The zero bilinear form is symmetric and alternating. If $\rho_1,\rho_2$ are symmetric, then for scalars $a,b$,
    \[
    (a\rho_1+b\rho_2)(u,v)
    =a\rho_1(v,u)+b\rho_2(v,u)
    =(a\rho_1+b\rho_2)(v,u).
    \]
    Thus their linear combination is symmetric. If $\alpha_1,\alpha_2$ are alternating, then
    $(a\alpha_1+b\alpha_2)(v,v)=a\cdot0+b\cdot0=0$,
    so their linear combination is alternating. Closure within $V^{(2)}$ follows from its vector-space property. The subspace test proves both subspace assertions.

    For an arbitrary $\beta$, the reversed-argument function
    $\beta^{\mathsf t}(u,v)=\beta(v,u)$ is bilinear: linearity in its first argument is linearity in the second argument of $\beta$, and conversely for its second argument. Therefore the two displayed averages are bilinear. Exchanging their arguments leaves $\rho$ unchanged and negates $\alpha$, so $\rho$ is symmetric and $\alpha$ is alternating by the antisymmetry test. Adding their formulas gives $\rho+\alpha=\beta$.

    Finally, if a form $\gamma$ is both symmetric and alternating, then
    \[
    \gamma(u,v)=\gamma(v,u)=-\gamma(u,v).
    \]
    Hence $2\gamma(u,v)=0$ for every pair, and scalar cancellation gives $\gamma=0$. The two subspaces have zero intersection and sum to the full space, so the direct-sum criterion proves the asserted direct sum and uniqueness of the displayed decomposition.''',
    2, 25,
    [r'''Average the form with its argument reversal, and take their half-difference.''',
     r'''A form that is both symmetric and antisymmetric must vanish.'''],
    ['def-symmetric-bilinear', 'def-alternating-bilinear',
     'thm-alternating-bilinear-test', 'thm-bilinear-space',
     'c1-thm-subspace-test', 'c1-thm-direct-intersection',
     'c1-lem-scalar-cancellation'],
    '9.17', 340,
)

s.d(
    'def-quadratic-form',
    'Quadratic forms associated with bilinear forms',
    r'''For a bilinear form $\beta$, define
    \[
    q_\beta(v)=\beta(v,v).
    \]
    A function $q:V\to\F$ is a quadratic form if $q=q_\beta$ for at least one bilinear form $\beta$.''',
    '9.18', 341,
)

s.r(
    'lem-zero-quadratic-form',
    'Which bilinear forms have zero diagonal function',
    r'''For a bilinear form $\beta$,
    \[
    q_\beta=0
    \quad\Longleftrightarrow\quad
    \beta\text{ is alternating}.
    \]''',
    r'''The identity $q_\beta=0$ means $\beta(v,v)=0$ for every $v$, which is precisely the definition of an alternating bilinear form. Thus each condition implies the other.''',
    1, 10,
    [r'''Compare the two definitions.'''],
    ['def-quadratic-form', 'def-alternating-bilinear'],
    page=341, kind='lemma',
)

s.r(
    'ex-quadratic-coordinate',
    'A quadratic form with cross terms',
    r'''On $\R^3$, the bilinear form
    \[
    \beta(x,y)=x_1y_1-4x_1y_2+8x_1y_3-3x_3y_3
    \]
    has associated quadratic form
    \[
    q_\beta(x)=x_1^2-4x_1x_2+8x_1x_3-3x_3^2.
    \]''',
    r'''The displayed bilinear expression is a matrix-coordinate form with nonzero entries $A_{11}=1$, $A_{12}=-4$, $A_{13}=8$, and $A_{33}=-3$. Hence it is bilinear. Substituting $y=x$ in its formula gives exactly the asserted expression for $q_\beta$, by the definition of the associated quadratic form.''',
    1, 10,
    [r'''Set the two inputs of the bilinear expression equal.'''],
    ['ex-matrix-bilinear', 'def-quadratic-form'],
    '9.19', 341, 'example',
)

s.r(
    'thm-coordinate-quadratic',
    'Quadratic forms in a coordinate space',
    r'''A function $q:\F^n\to\F$ is a quadratic form if and only if there are scalars $A_{jk}$ such that
    \[
    q(x)=\sum_{j=1}^n\sum_{k=1}^n A_{jk}x_jx_k
    \qquad(x\in\F^n).
    \]
    For $n=0$, this says that the only quadratic form is the function with value zero.''',
    r'''If $q=q_\beta$ for a bilinear form $\beta$, let $A$ be its matrix in the standard basis. The bilinear coordinate expansion with the same vector in both arguments gives
    \[
    q(x)=\beta(x,x)=\sum_{j,k}A_{jk}x_jx_k.
    \]
    Conversely, given such coefficients, the matrix-coordinate formula
    $\beta(x,y)=\sum_{j,k}A_{jk}x_jy_k$
    defines a bilinear form, and substituting $y=x$ gives $q=q_\beta$. When $n=0$, the double sum is zero and the unique vector is zero, so these arguments prove the stated special case as well.''',
    1, 10,
    [r'''Use the coordinate formula for a bilinear form with equal arguments.'''],
    ['def-quadratic-form', 'thm-bilinear-matrix-isomorphism',
     'ex-matrix-bilinear'],
    '9.20', 341,
)

s.r(
    'thm-quadratic-characterizations',
    'Recovering the symmetric form from a quadratic form',
    r'''For a function $q:V\to\F$, the following are equivalent:
    \begin{enumerate}
    \item $q$ is a quadratic form.
    \item There is exactly one symmetric bilinear form $\rho$ with $q(v)=\rho(v,v)$ for every $v$.
    \item $q(av)=a^2q(v)$ for every $a\in\F$ and $v\in V$, and
    \[
    b_q(u,v)=q(u+v)-q(u)-q(v)
    \]
    is a symmetric bilinear form.
    \item $q(2v)=4q(v)$ for every $v$, and the same function $b_q$ is a symmetric bilinear form.
    \end{enumerate}
    Whenever these conditions hold, the unique symmetric form is
    \[
    \rho(u,v)=\frac{q(u+v)-q(u)-q(v)}2.
    \]''',
    r'''Suppose first that $q=q_\beta$. Decompose $\beta=\rho+\alpha$ into its symmetric and alternating parts. Then
    \[
    q(v)=\rho(v,v)+\alpha(v,v)=\rho(v,v),
    \]
    proving existence in the second condition. If another symmetric form $\sigma$ has the same diagonal values, then $\sigma-\rho$ is symmetric and has zero quadratic form. It is therefore also alternating. The symmetric-alternating direct sum has zero intersection, so $\sigma-\rho=0$. This proves uniqueness.

    Now suppose $q(v)=\rho(v,v)$ for a symmetric bilinear form. Bilinearity gives
    \[
    q(av)=\rho(av,av)=a^2\rho(v,v)=a^2q(v).
    \]
    The diagonal-expansion identity gives
    \[
    b_q(u,v)=2\rho(u,v).
    \]
    Thus $b_q$ is symmetric and bilinear, proving the third condition and the stated recovery formula.

    The third condition implies the fourth by setting $a=2$. Finally, suppose the fourth condition holds and set $\rho=b_q/2$. This is a symmetric bilinear form by the assumed property of $b_q$. For every $v$,
    \[
    \rho(v,v)
    =\frac{q(2v)-2q(v)}2
    =\frac{4q(v)-2q(v)}2
    =q(v).
    \]
    Hence $q$ is a quadratic form, closing the cycle of implications. These equations also apply at zero and on the zero space.''',
    3, 35,
    [r'''The alternating part of a bilinear form disappears on the diagonal.''',
     r'''Expand the diagonal of a symmetric form at $u+v$.''',
     r'''For the weakest condition, take $\rho=b_q/2$ and evaluate it at $(v,v)$.'''],
    ['def-quadratic-form', 'thm-bilinear-decomposition',
     'lem-zero-quadratic-form', 'lem-symmetric-diagonal-detection',
     'lem-bilinear-expansion', 'thm-bilinear-space'],
    '9.21', 342,
)

s.r(
    'ex-symmetric-quadratic-associate',
    'The symmetric form behind the coordinate example',
    r'''For
    \[
    q(x)=x_1^2-4x_1x_2+8x_1x_3-3x_3^2,
    \]
    the unique symmetric bilinear form with diagonal $q$ is
    \[
    \rho(x,y)
    =x_1y_1-2x_1y_2-2x_2y_1
      +4x_1y_3+4x_3y_1-3x_3y_3.
    \]''',
    r'''The coordinate expression is bilinear by the matrix-coordinate construction. Exchanging $x$ and $y$ leaves the diagonal terms unchanged, interchanges the two terms with coefficient $-2$, and interchanges the two terms with coefficient $4$. Commutativity of scalar multiplication therefore gives $\rho(x,y)=\rho(y,x)$.

    Substituting $y=x$ combines the two $-2$ terms into $-4x_1x_2$ and the two $4$ terms into $8x_1x_3$, giving $\rho(x,x)=q(x)$. The quadratic-form characterization proves that this symmetric form is unique.''',
    1, 10,
    [r'''Split each cross-term coefficient equally between its two possible argument orders.'''],
    ['ex-matrix-bilinear', 'def-symmetric-bilinear',
     'thm-quadratic-characterizations', 'ex-quadratic-coordinate'],
    '9.22', 343, 'example',
)

s.r(
    'thm-quadratic-diagonalization',
    'Eliminating the cross terms of a quadratic form',
    r'''For every quadratic form $q$ on $V$, there are a basis $e_1,\ldots,e_n$ and scalars $\lambda_1,\ldots,\lambda_n$ such that
    \[
    q\left(\sum_{j=1}^n x_je_j\right)
    =\sum_{j=1}^n\lambda_jx_j^2
    \qquad(x_1,\ldots,x_n\in\F).
    \]
    If $V$ is a real inner product space, the basis can be chosen orthonormal. Over $\C$, the expression uses ordinary squares $x_j^2$, not squared moduli.''',
    r'''Let $\rho$ be the unique symmetric bilinear form whose diagonal is $q$. Symmetric-form diagonalization gives a basis $e_1,\ldots,e_n$ with $\rho(e_j,e_k)=0$ for $j\ne k$. Set $\lambda_j=\rho(e_j,e_j)$. Bilinear expansion gives
    \[
    \begin{aligned}
    q\left(\sum_jx_je_j\right)
    &=\rho\left(\sum_jx_je_j,\sum_kx_ke_k\right)\\
    &=\sum_{j,k}x_jx_k\rho(e_j,e_k)
    =\sum_j\lambda_jx_j^2.
    \end{aligned}
    \]
    If $V$ has a real inner product, use the orthonormal diagonalization theorem for $\rho$ to choose the basis, and the same calculation proves the orthonormal assertion. If $V=\{0\}$, the basis and sums are empty; every quadratic form then vanishes, so the formula remains valid.''',
    2, 20,
    [r'''Replace the quadratic form by its unique symmetric bilinear form.''',
     r'''Use a basis in which that bilinear form has zero off-diagonal entries.'''],
    ['thm-quadratic-characterizations',
     'thm-symmetric-diagonalization',
     'thm-real-symmetric-orthonormal', 'lem-bilinear-expansion',
     'def-quadratic-form'],
    '9.23', 343,
)

s.card(
    'bilinear-definition',
    'def-bilinear-form',
    r'''What does bilinearity require, and how does it differ from a complex inner product?''',
    r'''Each argument is linear when the other is fixed. Scalars leave either argument unchanged; in a complex inner product they leave the second argument conjugated.''',
)

s.card(
    'bilinear-matrix',
    'def-bilinear-matrix',
    r'''What is the $(j,k)$ entry of the matrix of a bilinear form in a basis $(e_1,\ldots,e_n)$?''',
    r'''It is $\beta(e_j,e_k)$.''',
)

s.card(
    'bilinear-dimension',
    'thm-bilinear-matrix-isomorphism',
    r'''What is the dimension of the space of bilinear forms on an $n$-dimensional space?''',
    r'''It is $n^2$, because taking the matrix in a fixed basis is an isomorphism onto $\F^{n,n}$.''',
)

s.card(
    'bilinear-change-basis',
    'thm-bilinear-basis-change',
    r'''If the columns of $C$ are the $\mathcal F$ coordinates of the $\mathcal E$ basis vectors, how are the form matrices related?''',
    r'''$\Mat(\beta,\mathcal E)=C^{\mathsf t}\Mat(\beta,\mathcal F)C$. The transpose is ordinary, even over $\C$.''',
)

s.card(
    'symmetric-diagonalization-idea',
    'thm-symmetric-diagonalization',
    r'''What is the inductive step for diagonalizing a nonzero symmetric bilinear form?''',
    r'''Find $w$ with $\rho(w,w)\ne0$, split off $\Span(w)$ using the kernel of $\rho(\,\cdot\,,w)$, and diagonalize the restriction to that smaller subspace.''',
)

s.card(
    'real-orthonormal-form',
    'thm-real-symmetric-orthonormal',
    r'''When does this section guarantee an orthonormal diagonalizing basis for a symmetric bilinear form?''',
    r'''When the ambient inner product space is real. The proof represents the form by a self-adjoint operator and applies the real spectral theorem.''',
)

s.card(
    'alternating-test',
    'thm-alternating-bilinear-test',
    r'''What identity is equivalent to alternation of a bilinear form over $\R$ or $\C$?''',
    r'''$\alpha(u,v)=-\alpha(v,u)$ for all inputs. Expand $\alpha(u+v,u+v)$ to obtain it from the diagonal condition.''',
)

s.card(
    'bilinear-parts',
    'thm-bilinear-decomposition',
    r'''What are the symmetric and alternating parts of $\beta$?''',
    r'''They are $\rho(u,v)=(\beta(u,v)+\beta(v,u))/2$ and $\alpha(u,v)=(\beta(u,v)-\beta(v,u))/2$. Their sum is $\beta$, uniquely.''',
)

s.card(
    'quadratic-polarization',
    'thm-quadratic-characterizations',
    r'''How does a quadratic form determine its unique symmetric bilinear form?''',
    r'''$\rho(u,v)=(q(u+v)-q(u)-q(v))/2$.''',
)

s.card(
    'quadratic-diagonalization',
    'thm-quadratic-diagonalization',
    r'''What does a quadratic form look like in a suitable basis?''',
    r'''It has the form $q(\sum_jx_je_j)=\sum_j\lambda_jx_j^2$. In a real inner product space the basis may be orthonormal.''',
)

s.write()