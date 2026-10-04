from common import Section

s = Section('9d')

s.p(
    'intro-tensor-products',
    'Products of vectors and linearization',
    r'''All vector spaces used as tensor factors in this section are finite-dimensional over $\F$. Tensor products will provide a bilinear multiplication of vectors whose products span a new vector space. The construction uses bilinear functionals on the dual spaces, and includes zero-dimensional factors.''',
    370,
)

s.d(
    'def-bilinear-functional',
    'Bilinear functionals on two spaces',
    r'''A bilinear functional on $V\times W$ is a function $\beta:V\times W\to\F$ that is linear in each argument when the other argument is fixed. Write $\Bil(V,W)$ for the set of these functions, with pointwise addition and scalar multiplication. When $W=V$, this is the space of bilinear forms from Section 9A.''',
    '9.68', 370,
)

s.r(
    'thm-bilinear-functional-space',
    'The vector space of bilinear functionals',
    r'''The set $\Bil(V,W)$ is a vector subspace of the space of all functions $V\times W\to\F$. Every $\beta\in\Bil(V,W)$ satisfies
    \[
    \beta(0,w)=\beta(v,0)=0
    \]
    and
    \[
    \beta\left(\sum_j a_jv_j,\sum_k b_kw_k\right)
    =\sum_{j,k}a_jb_k\beta(v_j,w_k).
    \]
    If either $V$ or $W$ is the zero space, then $\Bil(V,W)=\{0\}$.''',
    r'''The zero function is separately linear. If $\alpha,\beta$ are separately linear, then for scalars $a,b$ each fixed-argument function of $a\alpha+b\beta$ is a linear combination of two linear functionals. Distributing a further scalar linear combination in that argument shows it is linear. This applies to both arguments, so the subspace test proves that $\Bil(V,W)$ is a subspace of the function space.

    Each fixed-argument linear functional takes zero to zero, giving the zero identities. Repeated linearity in the first argument expands the first finite sum, and repeated linearity in the second expands each resulting term into the displayed double sum. For empty sums the zero identities give the same formula.

    If $V=\{0\}$, every possible input is $(0,w)$ and every value is zero. If $W=\{0\}$, every input is $(v,0)$ and again every value is zero. Thus only the zero functional exists in either case.''',
    1, 10,
    [r'''Use the subspace test and expand one argument at a time.'''],
    ['def-bilinear-functional', 'c1-thm-function-space',
     'c1-thm-subspace-test', 'c3-thm-linear-zero'],
    page=370,
)

s.r(
    'ex-bilinear-functional-product',
    'Multiplying two functional values',
    r'''For $\varphi\in\dual V$ and $\tau\in\dual W$, the function
    \[
    \beta(v,w)=\varphi(v)\tau(w)
    \]
    belongs to $\Bil(V,W)$.''',
    r'''For scalars $a,b$,
    \[
    \beta(av+bv',w)
    =(a\varphi(v)+b\varphi(v'))\tau(w)
    =a\beta(v,w)+b\beta(v',w).
    \]
    In the other argument,
    \[
    \beta(v,aw+bw')
    =\varphi(v)(a\tau(w)+b\tau(w'))
    =a\beta(v,w)+b\beta(v,w').
    \]
    These identities prove separate linearity.''',
    1, 10,
    [r'''Hold one functional value fixed while using linearity of the other.'''],
    ['def-bilinear-functional', 'c3-def-dual-space'],
    '9.69(a)', 371, 'example',
)

s.r(
    'ex-dual-evaluation-bilinear',
    'A bilinear functional on the dual spaces',
    r'''For fixed $v\in V$ and $w\in W$, the function
    \[
    (\varphi,\tau)\longmapsto\varphi(v)\tau(w)
    \]
    belongs to $\Bil(\dual V,\dual W)$.''',
    r'''Operations on dual spaces are pointwise. Thus, for scalars $a,b$,
    \[
    (a\varphi+b\psi)(v)\tau(w)
    =a\varphi(v)\tau(w)+b\psi(v)\tau(w).
    \]
    Similarly,
    \[
    \varphi(v)(a\tau+b\sigma)(w)
    =a\varphi(v)\tau(w)+b\varphi(v)\sigma(w).
    \]
    These are linearity in the two dual-space arguments, proving the assertion.''',
    1, 10,
    [r'''Evaluation at a fixed vector is linear in the functional being evaluated.'''],
    ['def-bilinear-functional', 'c3-def-dual-space',
     'c3-def-map-operations'],
    '9.69(b)', 371, 'example',
)

s.r(
    'ex-vector-functional-evaluation',
    'Evaluation is bilinear',
    r'''The function $V\times\dual V\to\F$ given by
    \[
    \beta(v,\varphi)=\varphi(v)
    \]
    is a bilinear functional.''',
    r'''For fixed $\varphi$, the function of $v$ is linear because $\varphi$ is a linear functional. For fixed $v$, pointwise operations give
    \[
    \beta(v,a\varphi+b\psi)
    =(a\varphi+b\psi)(v)
    =a\beta(v,\varphi)+b\beta(v,\psi).
    \]
    Hence it is linear in the second argument as well.''',
    1, 10,
    [r'''Use the definition of a functional in one argument and pointwise operations in the other.'''],
    ['def-bilinear-functional', 'c3-def-dual-space'],
    '9.69(c)', 371, 'example',
)

s.r(
    'ex-vector-operator-functional',
    'Applying a functional after an operator',
    r'''For a fixed $\varphi\in\dual V$, the function
    \[
    \beta:V\times\Lin(V)\to\F,\qquad
    \beta(v,T)=\varphi(Tv)
    \]
    is bilinear.''',
    r'''For fixed $T$, the composition $\varphi\circ T$ is linear, so the first argument is linear. For fixed $v$, the pointwise operator operations and linearity of $\varphi$ give
    \[
    \beta(v,aS+bT)
    =\varphi(aSv+bTv)
    =a\beta(v,S)+b\beta(v,T).
    \]
    This proves linearity in the second argument.''',
    1, 10,
    [r'''Use composition for the first argument and pointwise operator operations for the second.'''],
    ['def-bilinear-functional', 'c3-lem-composition-linear',
     'c3-def-map-operations', 'c3-def-linear-functional'],
    '9.69(d)', 371, 'example',
)

s.r(
    'ex-rectangular-trace-bilinear',
    'Trace of a rectangular matrix product',
    r'''For nonnegative integers $m,n$, the function
    \[
    \beta:\F^{m,n}\times\F^{n,m}\to\F,\qquad
    \beta(A,B)=\tr(AB)
    \]
    is bilinear.''',
    r'''The matrix-product and trace definitions give
    \[
    \beta(A,B)=\sum_{j=1}^m\sum_{k=1}^n A_{jk}B_{kj}.
    \]
    Replacing $A$ by $aA+bC$ replaces each entry $A_{jk}$ by $aA_{jk}+bC_{jk}$, so distributing the finite sum proves
    $\beta(aA+bC,B)=a\beta(A,B)+b\beta(C,B)$.
    Replacing $B$ by $aB+bD$ and distributing proves
    $\beta(A,aB+bD)=a\beta(A,B)+b\beta(A,D)$.
    Thus the function is bilinear. If $m=0$ or $n=0$, all terms vanish and the same assertions hold for the zero function.''',
    1, 10,
    [r'''Write the trace of the product as a double sum of entry products.'''],
    ['def-bilinear-functional', 'c8-def-matrix-trace',
     'c3-def-matrix-product', 'c3-def-matrix-space'],
    '9.69(e)', 371, 'example',
)

s.r(
    'thm-bilinear-functional-dimension',
    'Dimension of the space of bilinear functionals',
    r'''For finite-dimensional spaces $V,W$,
    \[
    \dim\Bil(V,W)=(\dim V)(\dim W).
    \]
    More precisely, if $e_1,\ldots,e_m$ and $f_1,\ldots,f_n$ are bases, then
    \[
    \beta\longmapsto\bigl(\beta(e_j,f_k)\bigr)_{j,k}
    \]
    is an isomorphism from $\Bil(V,W)$ to $\F^{m,n}$.''',
    r'''Denote the displayed map by $M$. Pointwise operations give
    $M(a\alpha+b\beta)_{jk}=a\alpha(e_j,f_k)+b\beta(e_j,f_k)$,
    so $M$ is linear. If $v=\sum_jx_je_j$ and $w=\sum_ky_kf_k$, bilinear expansion gives
    \[
    \beta(v,w)=\sum_{j,k}x_jy_kM(\beta)_{jk}.
    \]
    Therefore $M(\beta)=0$ implies $\beta=0$, proving injectivity.

    Conversely, for $A\in\F^{m,n}$ define
    \[
    \beta_A\left(\sum_jx_je_j,\sum_ky_kf_k\right)
    =\sum_{j,k}A_{jk}x_jy_k.
    \]
    Unique basis coordinates make this a well-defined function. Coordinates of vector linear combinations are the same linear combinations of coordinates. Distributing the sum therefore proves separate linearity of $\beta_A$. Substitution of a basis pair gives $\beta_A(e_j,f_k)=A_{jk}$, proving surjectivity.

    Thus $M$ is an isomorphism. The inverse images of a basis of $\F^{m,n}$ span $\Bil(V,W)$ because their images span, and are independent because their images are independent. This transports a basis and proves equality of dimensions. The matrix-space dimension is $mn$. If either factor is zero, the functional space is zero by the preceding result, and the formula gives zero as required.''',
    2, 25,
    [r'''Record the values of a functional on all pairs of basis vectors.''',
     r'''Recover the functional from those entries by expanding both inputs.'''],
    ['def-bilinear-functional', 'thm-bilinear-functional-space',
     'c2-thm-basis-coordinates', 'c3-def-isomorphism',
     'c3-thm-matrix-space-dimension'],
    '9.70', 371,
)

s.d(
    'def-tensor-product',
    'Tensor products of two spaces and of two vectors',
    r'''Define
    \[
    V\otimes W=\Bil(\dual V,\dual W).
    \]
    For $v\in V$ and $w\in W$, define the pure tensor $v\otimes w$ by
    \[
    (v\otimes w)(\varphi,\tau)=\varphi(v)\tau(w)
    \qquad(\varphi\in\dual V,\ \tau\in\dual W).
    \]
    The preceding dual-evaluation example proves that this function belongs to the stated tensor product. Thus a tensor is, in this construction, a bilinear functional on the two dual spaces.''',
    '9.71', 372,
)

s.r(
    'thm-tensor-dimension',
    'Dimension of a tensor product',
    r'''The tensor product satisfies
    \[
    \dim(V\otimes W)=(\dim V)(\dim W).
    \]
    In particular, a zero factor makes the tensor product the zero space.''',
    r'''The definition and the bilinear-functional dimension formula give
    \[
    \dim(V\otimes W)
    =\dim\Bil(\dual V,\dual W)
    =(\dim\dual V)(\dim\dual W).
    \]
    Finite-dimensional dual spaces have the same dimensions as their original spaces, yielding the required product. If one factor has dimension zero, the tensor product has dimension zero and hence consists only of its zero vector.''',
    1, 10,
    [r'''Apply the dimension formula for bilinear functionals to the dual spaces.'''],
    ['def-tensor-product', 'thm-bilinear-functional-dimension',
     'c3-thm-dual-dimension', 'c2-lem-zero-dimension'],
    '9.72', 372,
)

s.r(
    'thm-tensor-bilinearity',
    'Bilinearity of the pure-tensor operation',
    r'''For vectors in the indicated factors and a scalar $a$,
    \[
    (v_1+v_2)\otimes w=v_1\otimes w+v_2\otimes w,
    \]
    \[
    v\otimes(w_1+w_2)=v\otimes w_1+v\otimes w_2,
    \]
    and
    \[
    (av)\otimes w=a(v\otimes w)=v\otimes(aw).
    \]
    Also $0\otimes w=v\otimes0=0$.''',
    r'''To prove identities between tensors in this construction, it suffices to compare their values at every pair $(\varphi,\tau)\in\dual V\times\dual W$. Linearity of $\varphi$ gives
    \[
    \begin{aligned}
    ((v_1+v_2)\otimes w)(\varphi,\tau)
    &=(\varphi(v_1)+\varphi(v_2))\tau(w)\\
    &=(v_1\otimes w+v_2\otimes w)(\varphi,\tau).
    \end{aligned}
    \]
    Linearity of $\tau$ gives
    \[
    (v\otimes(w_1+w_2))(\varphi,\tau)
    =\varphi(v)(\tau(w_1)+\tau(w_2))
    =(v\otimes w_1+v\otimes w_2)(\varphi,\tau).
    \]
    Finally,
    \[
    ((av)\otimes w)(\varphi,\tau)
    =a\varphi(v)\tau(w)
    =(a(v\otimes w))(\varphi,\tau)
    =(v\otimes(aw))(\varphi,\tau).
    \]
    Thus all asserted functions are equal. Since every linear functional takes zero to zero, the defining formula gives zero at every pair for $0\otimes w$ and $v\otimes0$.''',
    1, 10,
    [r'''Evaluate each proposed identity at an arbitrary pair of functionals.'''],
    ['def-tensor-product', 'c3-def-dual-space',
     'c3-thm-linear-zero', 'c1-def-function-space'],
    '9.73', 372,
)

s.r(
    'thm-tensor-basis',
    'Independent tensor lists and tensor bases',
    r'''Let $e_1,\ldots,e_m$ be a list in $V$ and $f_1,\ldots,f_n$ a list in $W$.
    \begin{enumerate}
    \item If both lists are independent, then the list
    \[
    (e_j\otimes f_k)_{1\le j\le m,\ 1\le k\le n}
    \]
    is independent.
    \item If both lists are bases, then that tensor list is a basis of $V\otimes W$.
    \end{enumerate}
    Choose any fixed order for the pairs of indices. Consequently every tensor is a finite sum of pure tensors.''',
    r'''For the first assertion, extend each independent list to a basis of its space. The dual bases supply functionals $\varphi_1,\ldots,\varphi_m$ and $\tau_1,\ldots,\tau_n$ with
    \[
    \varphi_r(e_j)=
    \begin{cases}1,&r=j,\\0,&r\ne j,\end{cases}
    \qquad
    \tau_s(f_k)=
    \begin{cases}1,&s=k,\\0,&s\ne k.\end{cases}
    \]
    Suppose $\sum_{j,k}a_{jk}(e_j\otimes f_k)=0$.
    Evaluation at $(\varphi_r,\tau_s)$ gives
    \[
    0=\sum_{j,k}a_{jk}\varphi_r(e_j)\tau_s(f_k)=a_{rs}.
    \]
    Every coefficient is therefore zero, proving independence. If either list is empty, the tensor list is empty and independence holds by definition.

    If the original lists are bases, the tensor list is independent and has $mn$ elements. The tensor-dimension formula says that $mn=\dim(V\otimes W)$, so the full-length independence theorem makes it a basis.

    Every tensor consequently has an expansion $\sum_{j,k}a_{jk}(e_j\otimes f_k)$. Tensor homogeneity rewrites each term as $(a_{jk}e_j)\otimes f_k$, which proves the finite-sum assertion. If a factor is zero, the tensor basis and sum are empty and represent the unique tensor zero.''',
    3, 35,
    [r'''Use functionals that select one vector from each independent list.''',
     r'''Evaluate a proposed dependence at each pair of these functionals.''',
     r'''For bases, compare the number of independent tensors with the dimension.'''],
    ['def-tensor-product', 'thm-tensor-dimension',
     'thm-tensor-bilinearity', 'c2-thm-extend-independent',
     'c3-def-dual-basis', 'c3-thm-dual-basis',
     'c2-thm-full-length-independent'],
    '9.74', 373,
)

s.r(
    'ex-nonpure-tensor',
    'A tensor that is not a single pure tensor',
    r'''If $\dim V\ge2$ and $\dim W\ge2$, choose independent vectors $e_1,e_2$ and $f_1,f_2$. Then
    \[
    z=e_1\otimes f_1+e_2\otimes f_2
    \]
    cannot equal $v\otimes w$ for any $v\in V,w\in W$. Thus pure tensors need not exhaust a tensor product.''',
    r'''Extend the two independent lists to bases and choose their coordinate functionals $\varphi_1,\varphi_2$ and $\tau_1,\tau_2$. These select the displayed vectors as in the tensor-basis proof. Suppose $z=v\otimes w$, and put $a_j=\varphi_j(v)$ and $b_k=\tau_k(w)$ for $j,k\in\{1,2\}$. Evaluating at the four pairs gives
    \[
    a_1b_1=1,\qquad a_1b_2=0,\qquad
    a_2b_1=0,\qquad a_2b_2=1.
    \]
    The first equation implies $a_1\ne0$. The second then forces $b_2=0$, whereas the fourth requires $a_2b_2=1$. This contradiction proves the assertion.''',
    2, 20,
    [r'''Evaluate a hypothetical pure-tensor representation using two coordinate functionals from each factor.'''],
    ['def-tensor-product', 'thm-tensor-basis',
     'c2-thm-extend-independent', 'c3-def-dual-basis',
     'c1-lem-scalar-cancellation'],
    page=373, kind='example',
)

s.r(
    'thm-tensor-coordinate-array',
    'Tensor coordinates and outer products',
    r'''Let $e_1,\ldots,e_m$ and $f_1,\ldots,f_n$ be the standard bases of $\F^m$ and $\F^n$. Sending
    \[
    z=\sum_{j,k}A_{jk}(e_j\otimes f_k)
    \quad\text{to}\quad
    A=(A_{jk})
    \]
    gives an isomorphism $\F^m\otimes\F^n\to\F^{m,n}$. Under this identification,
    \[
    v\otimes w\longleftrightarrow
    (v_jw_k)_{j,k}.
    \]
    The same coefficient formula holds in any pair of chosen bases, with $v_j,w_k$ interpreted as their coordinates.''',
    r'''The tensor-basis theorem gives existence and uniqueness of the coefficients $A_{jk}$. Addition and scalar multiplication of tensors add and scale these coefficients, so the correspondence is linear. It is injective because zero coordinates give the zero tensor, and surjective because any matrix supplies the coefficients of a tensor. Thus it is an isomorphism.

    Expand $v=\sum_jv_je_j$ and $w=\sum_kw_kf_k$. Repeated tensor bilinearity gives
    \[
    v\otimes w
    =\sum_{j,k}v_jw_k(e_j\otimes f_k).
    \]
    Uniqueness of tensor-basis coordinates gives the asserted entries. This calculation uses only basis expansions and tensor bilinearity, so it is valid for arbitrary bases as well. With a zero factor, both coordinate arrays and tensor bases are empty and the unique tensor maps to the unique matrix of that size.''',
    2, 15,
    [r'''Expand each vector before taking its tensor product.'''],
    ['thm-tensor-basis', 'thm-tensor-bilinearity',
     'c2-thm-basis-coordinates', 'c3-def-isomorphism',
     'c3-def-matrix-space'],
    '9.76', 374, 'example',
)

s.d(
    'def-bilinear-map',
    'Bilinear maps with a vector-space target',
    r'''For a vector space $U$, a bilinear map $\Gamma:V\times W\to U$ is a function that is linear in each argument with the other held fixed. The target $U$ need not be finite-dimensional.''',
    '9.77', 374,
)

s.r(
    'ex-bilinear-maps',
    'Four bilinear maps',
    r'''The following functions are bilinear maps:
    \begin{enumerate}
    \item Every bilinear functional $\beta:V\times W\to\F$.
    \item $(v,w)\mapsto v\otimes w$, with target $V\otimes W$.
    \item $(S,T)\mapsto ST$, from $\Lin(V)\times\Lin(V)$ to $\Lin(V)$.
    \item $(v,T)\mapsto Tv$, from $V\times\Lin(V,W)$ to $W$.
    \end{enumerate}''',
    r'''For the first item, the definition of a bilinear functional is the bilinear-map definition with target $\F$. The tensor identities prove the second item.

    For composition, the operator algebra gives
    \[
    (aS+bR)T=aST+bRT,
    \qquad
    S(aT+bR)=aST+bSR.
    \]
    These identities prove linearity in each operator argument.

    Finally, for evaluation, linearity of each operator gives
    $T(av+bv')=aTv+bTv'$.
    Pointwise operator operations give
    $(aS+bT)v=aSv+bTv$.
    Thus evaluation is linear in each of its two arguments as well.''',
    1, 10,
    [r'''Check the two scalar linear-combination identities for each formula.'''],
    ['def-bilinear-map', 'def-bilinear-functional',
     'thm-tensor-bilinearity', 'c3-thm-composition-laws',
     'c3-def-map-operations'],
    '9.78', 374, 'example',
)

s.r(
    'thm-tensor-universal',
    'The universal property of the tensor product',
    r'''For any vector space $U$ and bilinear map $\Gamma:V\times W\to U$, there is exactly one linear map
    \[
    \widehat\Gamma:V\otimes W\to U
    \]
    such that
    \[
    \widehat\Gamma(v\otimes w)=\Gamma(v,w)
    \qquad(v\in V,w\in W).
    \]
    Conversely, every linear map $T:V\otimes W\to U$ determines exactly one bilinear map
    \[
    T^\#(v,w)=T(v\otimes w).
    \]
    These two constructions are inverse to one another.''',
    r'''Choose bases $e_1,\ldots,e_m$ and $f_1,\ldots,f_n$. Their pure tensors are a basis of $V\otimes W$. Prescribe
    \[
    \widehat\Gamma(e_j\otimes f_k)=\Gamma(e_j,f_k)
    \]
    on that basis. The basis prescription theorem gives a unique linear map with these values. If $v=\sum_ja_je_j$ and $w=\sum_kb_kf_k$, tensor bilinearity and linearity of this prescribed map give
    \[
    \widehat\Gamma(v\otimes w)
    =\sum_{j,k}a_jb_k\widehat\Gamma(e_j\otimes f_k)
    =\sum_{j,k}a_jb_k\Gamma(e_j,f_k).
    \]
    Expanding the two arguments of the bilinear map $\Gamma$ shows that the last sum equals $\Gamma(v,w)$. Thus the required identity holds for all vectors, not just basis vectors. Any other linear map satisfying it has the same values on the tensor basis and is therefore equal to $\widehat\Gamma$.

    Conversely, define $T^\#$ by the stated formula. For scalars $a,b$, tensor bilinearity and linearity of $T$ give
    \[
    T^\#(av+bv',w)
    =T\bigl(a(v\otimes w)+b(v'\otimes w)\bigr)
    =aT^\#(v,w)+bT^\#(v',w).
    \]
    The second argument has the corresponding identity
    \[
    T^\#(v,aw+bw')
    =aT^\#(v,w)+bT^\#(v,w').
    \]
    Hence $T^\#$ is bilinear. Its formula specifies its value at every input, proving uniqueness. Beginning with $\Gamma$, the construction followed by $\#$ returns $\Gamma$ by the defining identity. Beginning with $T$, the constructed linear map agrees with $T$ on every pure tensor, hence on the tensor basis, so it is $T$.

    If a factor is zero, every bilinear map on the product is zero because a linear map in the zero argument takes zero to zero. The tensor product is also zero, and its unique linear map to $U$ is the zero map. Thus all assertions remain valid in this case.''',
    3, 40,
    [r'''Prescribe the desired map on a tensor basis, where coordinates are unique.''',
     r'''Expand arbitrary pure tensors to verify the formula beyond the basis.''',
     r'''For the converse, compose a linear map with the bilinear pure-tensor operation.'''],
    ['def-bilinear-map', 'thm-tensor-basis',
     'thm-tensor-bilinearity', 'thm-tensor-dimension',
     'c3-thm-linear-map-basis', 'c3-thm-linear-zero',
     'c2-thm-basis-coordinates'],
    '9.79', 375,
)

s.note(
    'note-tensor-universal-well-defined',
    'Why the construction uses a basis',
    r'''A tensor can have many presentations as a sum of pure tensors. The proof constructs the linear map from unique tensor-basis coordinates, and only then proves its formula for all pure tensors. Uniqueness also shows that the resulting map is independent of the bases chosen during the construction.''',
    376,
)

s.r(
    'thm-tensor-inner-product',
    'The inner product on a tensor product',
    r'''If $V$ and $W$ are inner product spaces, there is exactly one inner product on $V\otimes W$ satisfying
    \[
    \ip{v\otimes w}{u\otimes x}
    =\ip{v}{u}\,\ip{w}{x}
    \qquad(v,u\in V,\ w,x\in W).
    \]
    As throughout the module, the inner product is linear in its first argument.''',
    r'''Choose orthonormal bases $e_1,\ldots,e_m$ of $V$ and $f_1,\ldots,f_n$ of $W$. Their tensors form a basis. For the unique coordinate expansions
    \[
    z=\sum_{j,k}a_{jk}(e_j\otimes f_k),
    \qquad
    t=\sum_{j,k}b_{jk}(e_j\otimes f_k),
    \]
    define
    \[
    H(z,t)=\sum_{j,k}a_{jk}\overline{b_{jk}}.
    \]
    Unique coordinates make this well-defined.

    Addition and scalar multiplication of the first coordinate array give
    $H(z+z',t)=H(z,t)+H(z',t)$ and
    $H(cz,t)=cH(z,t)$.
    Conjugating the finite sum gives
    $\overline{H(z,t)}=\sum_{j,k}\overline{a_{jk}}b_{jk}=H(t,z)$,
    proving conjugate symmetry. Moreover,
    \[
    H(z,z)=\sum_{j,k}|a_{jk}|^2
    \]
    is real and nonnegative. It vanishes only when each coefficient is zero, since a finite sum of nonnegative numbers can be zero only if every summand is zero. By basis uniqueness, that is equivalent to $z=0$. Thus all inner-product axioms hold.

    Write $v=\sum_jv_je_j$, $u=\sum_ju_je_j$,
    $w=\sum_kw_kf_k$, and $x=\sum_kx_kf_k$.
    The tensor-coordinate formula yields
    \[
    \begin{aligned}
    H(v\otimes w,u\otimes x)
    &=\sum_{j,k}v_jw_k\overline{u_jx_k}\\
    &=\left(\sum_jv_j\overline{u_j}\right)
      \left(\sum_kw_k\overline{x_k}\right)\\
    &=\ip{v}{u}\,\ip{w}{x}.
    \end{aligned}
    \]
    The last step uses orthonormal coordinates in each factor. Thus the constructed inner product has the required property.

    Any other inner product with that property has
    \[
    \ip{e_j\otimes f_k}{e_r\otimes f_\ell}
    =\ip{e_j}{e_r}\ip{f_k}{f_\ell},
    \]
    equal to one for identical index pairs and zero otherwise. Expanding arbitrary tensors in this basis, using linearity in the first argument and conjugate linearity in the second, forces its value to be $\sum_{j,k}a_{jk}\overline{b_{jk}}$. Hence it equals $H$, proving uniqueness.

    If a factor is zero, the tensor product is zero and its tensor basis is empty. The construction then gives the sole value $H(0,0)=0$, which satisfies the inner-product axioms on the zero space. The prescribed formula holds because a pure tensor with a zero factor is zero and the corresponding factor inner product is zero.''',
    3, 45,
    [r'''Choose orthonormal bases of the factors and use the resulting tensor basis.''',
     r'''Define the inner product from the unique coordinate arrays and check all axioms.''',
     r'''For uniqueness, the required rule already specifies all inner products between tensor-basis vectors.'''],
    ['thm-tensor-basis', 'thm-tensor-coordinate-array',
     'thm-tensor-bilinearity', 'thm-tensor-dimension',
     'c6-def-inner-product', 'c6-thm-inner-product-properties',
     'c6-thm-orthonormal-basis-existence',
     'c6-thm-orthonormal-coordinates',
     'c4-thm-complex-properties', 'c2-thm-basis-coordinates'],
    '9.80', 376,
)

s.d(
    'def-tensor-inner-product',
    'The designated tensor-product inner product',
    r'''For inner product spaces $V,W$, equip $V\otimes W$ with the unique inner product proved to exist above. Thus
    \[
    \ip{v\otimes w}{u\otimes x}
    =\ip{v}{u}\,\ip{w}{x}.
    \]
    Its definition is independent of any orthonormal bases used to construct it.''',
    '9.82', 377,
)

s.r(
    'thm-tensor-norm',
    'The norm of a pure tensor',
    r'''For the tensor-product inner product,
    \[
    \norm{v\otimes w}=\norm v\,\norm w.
    \]''',
    r'''Applying the defining inner-product rule with equal arguments gives
    \[
    \norm{v\otimes w}^2
    =\ip{v\otimes w}{v\otimes w}
    =\ip{v}{v}\,\ip{w}{w}
    =\norm v^2\norm w^2.
    \]
    Both $\norm{v\otimes w}$ and $\norm v\,\norm w$ are nonnegative, so equality of their squares implies equality. If either vector is zero, both sides are zero and the same argument applies.''',
    1, 10,
    [r'''Compute the squared norm using the product rule for inner products.'''],
    ['def-tensor-inner-product', 'c6-def-norm',
     'c6-thm-norm-properties'],
    page=377,
)

s.r(
    'thm-tensor-orthonormal-basis',
    'Orthonormal tensor bases',
    r'''If $e_1,\ldots,e_m$ and $f_1,\ldots,f_n$ are any orthonormal bases of the factors, then
    \[
    (e_j\otimes f_k)_{j,k}
    \]
    is an orthonormal basis of their tensor product with its designated inner product.''',
    r'''It is a basis by the tensor-basis theorem. For two index pairs,
    \[
    \ip{e_j\otimes f_k}{e_r\otimes f_\ell}
    =\ip{e_j}{e_r}\ip{f_k}{f_\ell}.
    \]
    The right side is one if $j=r$ and $k=\ell$, and zero otherwise, because each factor basis is orthonormal. Thus the tensor basis is orthonormal. This reasoning uses the basis-independent inner-product rule, so the factor bases can be any orthonormal bases. When a factor is zero, the tensor space is zero and the empty list is its orthonormal basis.''',
    1, 10,
    [r'''Compute the inner product of two tensor-basis vectors.'''],
    ['thm-tensor-basis', 'def-tensor-inner-product',
     'c6-def-orthonormal-basis'],
    '9.83', 377,
)

s.d(
    'def-multiple-factor-notation',
    'Notation for several tensor factors',
    r'''For the remaining results, let $m\ge2$ be an integer and let $V_1,\ldots,V_m$ be finite-dimensional vector spaces over the same field $\F$. Any of these spaces may be zero.''',
    '9.84', 378,
)

s.d(
    'def-multilinear-functional',
    'Multilinear functionals on different spaces',
    r'''An $m$-linear functional on $V_1\times\cdots\times V_m$ is a scalar-valued function that is linear in each argument when the other arguments are fixed. Denote the set of these functions by
    \[
    \Bil(V_1,\ldots,V_m),
    \]
    with pointwise addition and scalar multiplication.''',
    '9.85', 378,
)

s.r(
    'thm-multilinear-functional-space',
    'The space and expansion rule for multilinear functionals',
    r'''The set $\Bil(V_1,\ldots,V_m)$ is a vector space. Every member vanishes whenever one argument is zero. If
    $v_r=\sum_{j=1}^{n_r}a_{rj}e_j^{(r)}$, then
    \[
    \beta(v_1,\ldots,v_m)
    =
    \sum_{j_1=1}^{n_1}\cdots\sum_{j_m=1}^{n_m}
    \left(\prod_{r=1}^m a_{rj_r}\right)
    \beta(e_{j_1}^{(1)},\ldots,e_{j_m}^{(m)}).
    \]
    In particular, if a factor is zero then this functional space is zero.''',
    r'''The zero function is linear in each argument. For a linear combination $a\alpha+b\beta$, fixing all but one argument leaves a linear combination of linear functionals in that argument; distributing the scalar coefficients proves its linearity. Applying this to each argument gives closure, so the subspace test in the ambient function space proves the vector-space assertion.

    If one argument is zero, the corresponding fixed-argument linear functional takes zero to zero. For the expansion formula, first use linearity to expand $v_1$ in the first argument, obtaining one sum and its coefficients $a_{1j_1}$. In every summand, expand $v_2$ in the second argument, multiplying its coefficient by $a_{2j_2}$. Continue through the $m$ arguments. Induction on the number of expanded arguments gives the displayed product of coefficients and iterated finite sum. If one expansion is empty, its vector is zero; the functional value and the iterated sum are both zero. If an entire factor space is zero, every input has such a zero argument, so the only functional is zero.''',
    2, 20,
    [r'''Apply the fixed-argument linearity rule successively in the $m$ positions.'''],
    ['def-multilinear-functional', 'c1-thm-function-space',
     'c1-thm-subspace-test', 'c3-thm-linear-zero',
     'c1-foundations'],
    page=378,
)

s.r(
    'ex-multilinear-functional-product',
    'A product of one functional from each factor',
    r'''If $\varphi_r\in\dual{V_r}$ for $r=1,\ldots,m$, then
    \[
    \beta(v_1,\ldots,v_m)=\prod_{r=1}^m\varphi_r(v_r)
    \]
    is an $m$-linear functional.''',
    r'''Fix all arguments except the $k$th. The function of that remaining argument is
    \[
    v_k\longmapsto
    \left(\prod_{r\ne k}\varphi_r(v_r)\right)\varphi_k(v_k).
    \]
    The parenthesized quantity is a fixed scalar, so this is a scalar multiple of the linear functional $\varphi_k$ and is therefore linear. Since $k$ was arbitrary, the function is linear in every argument.''',
    1, 10,
    [r'''With all other inputs fixed, only one factor in the product varies.'''],
    ['def-multilinear-functional', 'c3-def-linear-functional'],
    '9.86', 378, 'example',
)

s.r(
    'thm-multilinear-functional-dimension',
    'Dimension of a multilinear-functional space',
    r'''For finite-dimensional factors,
    \[
    \dim\Bil(V_1,\ldots,V_m)
    =\prod_{r=1}^m\dim V_r.
    \]''',
    r'''If one factor is zero, the functional space is zero by the preceding result, and both sides of the formula are zero. Now assume each $n_r=\dim V_r$ is positive. Choose a basis
    $e_1^{(r)},\ldots,e_{n_r}^{(r)}$
    with dual basis
    $\varphi_1^{(r)},\ldots,\varphi_{n_r}^{(r)}$.
    For each index tuple $J=(j_1,\ldots,j_m)$, define
    \[
    b_J(v_1,\ldots,v_m)
    =\prod_{r=1}^m\varphi_{j_r}^{(r)}(v_r).
    \]
    The product-functional example makes each $b_J$ multilinear.

    On a basis tuple
    $(e_{k_1}^{(1)},\ldots,e_{k_m}^{(m)})$,
    the value of $b_J$ is one if $J=(k_1,\ldots,k_m)$ and zero otherwise. Consequently, evaluating a zero linear combination of the $b_J$ at each basis tuple forces every coefficient to vanish. Thus they are independent.

    Given any multilinear functional $\beta$, define
    \[
    \gamma=\sum_J
    \beta(e_{j_1}^{(1)},\ldots,e_{j_m}^{(m)})\,b_J.
    \]
    The evaluation rule just proved shows that $\gamma$ and $\beta$ have the same value on every basis tuple. Their multilinear expansion formulas therefore give the same value on every tuple of vectors. Hence $\gamma=\beta$, proving that the $b_J$ span. They are a basis, with exactly $\prod_r n_r$ members, proving the dimension formula.''',
    3, 35,
    [r'''Use products of coordinate functionals as candidate basis vectors.''',
     r'''Evaluation at a basis tuple singles out one coefficient.''',
     r'''Repeated multilinearity shows that basis-tuple values determine the functional.'''],
    ['thm-multilinear-functional-space',
     'ex-multilinear-functional-product',
     'c3-def-dual-basis', 'c3-thm-dual-basis',
     'c2-thm-basis-existence', 'c2-def-dimension',
     'c1-foundations'],
    '9.87', 378,
)

s.d(
    'def-multiple-tensor-product',
    'Tensor products of several spaces and vectors',
    r'''Define
    \[
    V_1\otimes\cdots\otimes V_m
    =\Bil(\dual{V_1},\ldots,\dual{V_m}).
    \]
    For vectors $v_r\in V_r$, the pure tensor is the function
    \[
    (v_1\otimes\cdots\otimes v_m)(\varphi_1,\ldots,\varphi_m)
    =\prod_{r=1}^m\varphi_r(v_r).
    \]
    The next result verifies membership and the multilinearity of this operation.''',
    '9.88', 379,
)

s.r(
    'thm-multiple-tensor-multilinearity',
    'The pure-tensor operation is multilinear',
    r'''Every function specified as $v_1\otimes\cdots\otimes v_m$ in the definition belongs to the tensor product. The map
    \[
    (v_1,\ldots,v_m)\longmapsto v_1\otimes\cdots\otimes v_m
    \]
    is linear in each argument when the others are fixed. A pure tensor is zero whenever one of its vector arguments is zero.''',
    r'''For fixed vectors $v_r$, evaluation
    $\varphi_r\mapsto\varphi_r(v_r)$
    is a linear functional on $\dual{V_r}$ by pointwise dual-space operations. The product-functional example, applied to these dual spaces, shows that their product is multilinear in the functionals. This proves membership in
    $\Bil(\dual{V_1},\ldots,\dual{V_m})$.

    Fix all vector arguments except position $k$, and evaluate at an arbitrary tuple of functionals. Replacing the $k$th vector by $au+bw$ changes the value to
    \[
    \left(\prod_{r\ne k}\varphi_r(v_r)\right)
    \varphi_k(au+bw)
    =
    a\left(\prod_{r\ne k}\varphi_r(v_r)\right)\varphi_k(u)
    +
    b\left(\prod_{r\ne k}\varphi_r(v_r)\right)\varphi_k(w).
    \]
    This is the value of the corresponding linear combination of the two tensors with $u$ and $w$ in position $k$. Equality at every functional tuple proves equality of the tensors, and hence linearity in that position. Since $k$ was arbitrary, the operation is multilinear. If the $k$th vector is zero, the factor $\varphi_k(0)$ vanishes at every input, so the tensor is the zero function.''',
    2, 15,
    [r'''Verify identities by evaluating at an arbitrary tuple of functionals.'''],
    ['def-multiple-tensor-product',
     'ex-multilinear-functional-product',
     'c3-def-dual-space', 'c3-thm-linear-zero'],
    page=379,
)

s.r(
    'thm-multiple-tensor-dimension',
    'Dimension of a tensor product with several factors',
    r'''For $m\ge2$,
    \[
    \dim(V_1\otimes\cdots\otimes V_m)
    =\prod_{r=1}^m\dim V_r.
    \]''',
    r'''The definition and the multilinear-functional dimension theorem give
    \[
    \dim(V_1\otimes\cdots\otimes V_m)
    =\prod_{r=1}^m\dim\dual{V_r}.
    \]
    Each finite-dimensional dual has the dimension of its original space, so the right side is the asserted product. If a factor is zero, the product is zero, and the tensor space is zero by the zero-dimension criterion.''',
    1, 10,
    [r'''Apply the preceding dimension theorem to the dual factors.'''],
    ['def-multiple-tensor-product',
     'thm-multilinear-functional-dimension',
     'c3-thm-dual-dimension', 'c2-lem-zero-dimension'],
    '9.89', 379,
)

s.r(
    'thm-multiple-tensor-basis',
    'Tensor bases and arrays with several indices',
    r'''For each $r=1,\ldots,m$, choose a basis
    $e_1^{(r)},\ldots,e_{n_r}^{(r)}$ of $V_r$.
    Then the tensors
    \[
    E_J=e_{j_1}^{(1)}\otimes\cdots\otimes e_{j_m}^{(m)},
    \qquad
    1\le j_r\le n_r,
    \]
    form a basis of $V_1\otimes\cdots\otimes V_m$, in any fixed ordering of the index tuples.

    If $\varphi_1^{(r)},\ldots,\varphi_{n_r}^{(r)}$ are the dual bases, the coefficient of $E_J$ in a tensor $z$ is
    \[
    z(\varphi_{j_1}^{(1)},\ldots,\varphi_{j_m}^{(m)}).
    \]
    If $v_r=\sum_ja_{rj}e_j^{(r)}$, the coefficient of $E_J$ in the pure tensor $v_1\otimes\cdots\otimes v_m$ is
    $\prod_{r=1}^m a_{rj_r}$.''',
    r'''First assume no factor is zero. At a tuple of dual-basis functionals indexed by $K=(k_1,\ldots,k_m)$, the tensor definition gives
    \[
    E_J(\varphi_{k_1}^{(1)},\ldots,\varphi_{k_m}^{(m)})
    =\prod_{r=1}^m
    \varphi_{k_r}^{(r)}(e_{j_r}^{(r)}).
    \]
    This product is one if $J=K$ and zero otherwise. Evaluating a zero combination $\sum_Jc_JE_J=0$ at the tuple indexed by $K$ therefore gives $c_K=0$. All coefficients vanish, proving independence.

    There are $\prod_rn_r$ tensors in the list, equal to the dimension of the tensor space. The full-length independence theorem makes them a basis. Evaluating the unique basis expansion of any tensor $z$ at the tuple indexed by $J$ then selects its coefficient, proving the second assertion.

    For a pure tensor, that evaluation is
    \[
    \prod_{r=1}^m\varphi_{j_r}^{(r)}(v_r)
    =\prod_{r=1}^m a_{rj_r},
    \]
    by the dual-coordinate property. This proves the final assertion.

    If a factor is zero, its basis is empty, so there are no index tuples $J$. The tensor space is zero by the dimension theorem, and the empty list is its basis. The coordinate assertions contain no indices, and the only pure tensor is zero, as required.''',
    3, 35,
    [r'''Evaluate candidate basis tensors on tuples of dual-basis functionals.''',
     r'''The number of resulting independent tensors equals the dimension.'''],
    ['def-multiple-tensor-product',
     'thm-multiple-tensor-dimension',
     'thm-multiple-tensor-multilinearity',
     'c3-def-dual-basis', 'c3-thm-dual-basis',
     'c3-thm-dual-coordinates',
     'c2-thm-full-length-independent'],
    '9.90', 379,
)

s.d(
    'def-multilinear-map',
    'Multilinear maps into an arbitrary vector space',
    r'''For a vector space $U$, an $m$-linear map
    \[
    \Gamma:V_1\times\cdots\times V_m\to U
    \]
    is a function that is linear in each argument when the other arguments are fixed. No finite-dimensional assumption is imposed on $U$.''',
    '9.91', 379,
)

s.r(
    'thm-multiple-tensor-universal',
    'The universal property for several factors',
    r'''For an $m$-linear map
    $\Gamma:V_1\times\cdots\times V_m\to U$,
    there exists exactly one linear map
    \[
    \widehat\Gamma:
    V_1\otimes\cdots\otimes V_m\to U
    \]
    satisfying
    \[
    \widehat\Gamma(v_1\otimes\cdots\otimes v_m)
    =\Gamma(v_1,\ldots,v_m).
    \]
    Conversely, each linear map $T$ on the tensor product with target $U$ determines exactly one $m$-linear map
    \[
    T^\#(v_1,\ldots,v_m)=T(v_1\otimes\cdots\otimes v_m).
    \]
    These correspondences are inverse to one another.''',
    r'''First suppose every factor is nonzero, and choose bases as in the tensor-basis theorem. Prescribe values on that basis by
    \[
    \widehat\Gamma(E_J)
    =\Gamma(e_{j_1}^{(1)},\ldots,e_{j_m}^{(m)}).
    \]
    The basis prescription theorem gives exactly one linear map with these values. Write $v_r=\sum_ja_{rj}e_j^{(r)}$. The pure-tensor coordinate formula gives
    \[
    v_1\otimes\cdots\otimes v_m
    =\sum_J\left(\prod_r a_{rj_r}\right)E_J.
    \]
    Applying the prescribed linear map yields
    \[
    \widehat\Gamma(v_1\otimes\cdots\otimes v_m)
    =
    \sum_J\left(\prod_r a_{rj_r}\right)
    \Gamma(e_{j_1}^{(1)},\ldots,e_{j_m}^{(m)}).
    \]
    Expand $\Gamma(v_1,\ldots,v_m)$ first in its first argument, then in its second argument, and continue through its $m$th argument. Linearity in each position gives exactly the same sum with the same product of coefficients. This proves the required identity for every tuple of vectors. Any other linear map satisfying that identity agrees on every $E_J$, and hence is equal to $\widehat\Gamma$.

    Conversely, define $T^\#$ by the displayed formula. Fix all arguments except position $k$. The pure-tensor operation is linear in that position, so replacing its vector by $au+bw$ replaces the tensor by $a$ times the tensor with $u$ plus $b$ times the tensor with $w$. Applying linearity of $T$ gives the same scalar linear-combination identity for $T^\#$. Since this works in each position, $T^\#$ is $m$-linear. Its formula specifies every value, so it is unique.

    Starting with $\Gamma$ and then applying $\#$ returns $\Gamma$ by the proven pure-tensor identity. Starting with $T$ gives a new linear map agreeing with $T$ on every pure tensor, in particular on the tensor basis, so it returns $T$.

    If some factor $V_k$ is zero, every input to an $m$-linear map has zero in position $k$, and linearity there forces every output to be zero. The tensor space also has dimension zero. Its only linear map to $U$ is zero, and every pure tensor is zero. Thus existence, uniqueness, the formulas, and the inverse-correspondence assertion all hold in this remaining case.''',
    3, 45,
    [r'''Prescribe the map on the tensor basis indexed by tuples of basis indices.''',
     r'''Expand every argument to check the prescribed map on arbitrary pure tensors.''',
     r'''For the converse, compose a linear map with the multilinear pure-tensor operation.'''],
    ['def-multilinear-map',
     'thm-multiple-tensor-basis',
     'thm-multiple-tensor-multilinearity',
     'thm-multiple-tensor-dimension',
     'c3-thm-linear-map-basis', 'c3-thm-linear-zero',
     'c2-thm-basis-coordinates'],
    '9.92', 380,
)

s.card(
    'tensor-definition',
    'def-tensor-product',
    r'''In this construction, what space is $V\otimes W$, and how does $v\otimes w$ act?''',
    r'''$V\otimes W=\Bil(\dual V,\dual W)$, and $(v\otimes w)(\varphi,\tau)=\varphi(v)\tau(w)$.''',
)

s.card(
    'tensor-dimension',
    'thm-tensor-dimension',
    r'''What is $\dim(V\otimes W)$? What happens when a factor is zero?''',
    r'''It equals $(\dim V)(\dim W)$. A zero factor makes the tensor product the zero space.''',
)

s.card(
    'tensor-bilinearity',
    'thm-tensor-bilinearity',
    r'''How do sums and scalars interact with a pure tensor?''',
    r'''The operation is linear in each factor: for example $(v+u)\otimes w=v\otimes w+u\otimes w$, and $(av)\otimes w=a(v\otimes w)=v\otimes(aw)$.''',
)

s.card(
    'tensor-basis',
    'thm-tensor-basis',
    r'''How do bases of the factors produce a tensor basis, and how is independence proved?''',
    r'''All pairwise tensors $e_j\otimes f_k$ form a basis. Evaluate a proposed dependence on pairs of dual coordinate functionals to isolate its coefficients.''',
)

s.card(
    'tensor-outer-product',
    'thm-tensor-coordinate-array',
    r'''What coordinate matrix represents the pure tensor $v\otimes w$?''',
    r'''Its $(j,k)$ entry is $v_jw_k$, with no complex conjugation.''',
)

s.card(
    'tensor-universal',
    'thm-tensor-universal',
    r'''State the universal property of $V\otimes W$.''',
    r'''Every bilinear map $\Gamma:V\times W\to U$ factors uniquely through a linear map $\widehat\Gamma:V\otimes W\to U$ satisfying $\widehat\Gamma(v\otimes w)=\Gamma(v,w)$.''',
)

s.card(
    'tensor-inner-product',
    'thm-tensor-inner-product',
    r'''What rule specifies the tensor-product inner product, and why does its construction use a basis?''',
    r'''$\ip{v\otimes w}{u\otimes x}=\ip{v}{u}\,\ip{w}{x}$. Unique tensor-basis coordinates define a well-defined inner product; arbitrary sums of pure tensors need not be unique.''',
)

s.card(
    'tensor-norm',
    'thm-tensor-norm',
    r'''What is the norm of a pure tensor in inner product spaces?''',
    r'''$\norm{v\otimes w}=\norm v\,\norm w$.''',
)

s.card(
    'multiple-tensor-basis',
    'thm-multiple-tensor-basis',
    r'''How are coordinates indexed for a tensor product of $m$ spaces?''',
    r'''By tuples $(j_1,\ldots,j_m)$ selecting one basis vector from each factor. The associated basis vector is $e_{j_1}^{(1)}\otimes\cdots\otimes e_{j_m}^{(m)}$.''',
)

s.card(
    'multiple-tensor-universal',
    'thm-multiple-tensor-universal',
    r'''What replaces bilinear maps in the universal property for $m$ tensor factors?''',
    r'''Maps that are linear separately in all $m$ arguments. Each has a unique linear extension to the tensor product taking a pure tensor to its value on the corresponding tuple.''',
)

s.write()