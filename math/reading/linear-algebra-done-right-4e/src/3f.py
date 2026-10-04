from common import Section

s = Section('3f')

s.p(
    'intro-duality',
    'Scalar-valued observations of vectors',
    r'''A linear functional assigns a scalar to each vector while respecting vector arithmetic. Collecting these functionals into a vector space gives another way to study a linear map, with the direction of the map reversed.''',
    105
)

s.d(
    'def-linear-functional',
    'Linear functionals',
    r'''A \emph{linear functional} on a vector space $V$ over $\F$ is a linear map from $V$ to $\F$. Thus it is an element of $\Lin(V,\F)$.''',
    '3.108', 105
)

s.r(
    'ex-functional-three-coordinates',
    'A scalar output from three coordinates',
    r'''The function $\varphi:\R^3\to\R$ given by
\[
\varphi(x,y,z)=4x-5y+2z
\]
is a linear functional.''',
    r'''For $u=(x,y,z)$ and $v=(a,b,c)$, distributivity gives
\[
\varphi(u+v)
=4(x+a)-5(y+b)+2(z+c)
=(4x-5y+2z)+(4a-5b+2c)
=\varphi(u)+\varphi(v).
\]
For $r\in\R$, factoring $r$ from the three terms gives
$\varphi(ru)=r(4x-5y+2z)=r\varphi(u)$.
The output is real, so these identities establish that $\varphi$ is a linear functional on $\R^3$.''',
    1, 10,
    [r'''Expand the output on a sum and on a scalar multiple.'''],
    ['def-linear-functional', 'def-linear-map',
     'c1-def-coordinate-addition', 'c1-def-coordinate-scaling'],
    number='3.109', page=105, kind='example'
)

s.r(
    'ex-functional-coordinate-combination',
    'Coordinate linear functionals',
    r'''For fixed $c_1,\ldots,c_n\in\F$, the function
\[
\varphi:\F^n\to\F,\qquad
\varphi(x)=\sum_{k=1}^{n}c_kx_k
\]
is a linear functional. This includes $n=0$, when the formula defines the zero functional on the zero coordinate space.''',
    r'''The finite sum is a scalar. For $x,y\in\F^n$ and $a\in\F$,
\[
\varphi(x+y)=\sum_kc_k(x_k+y_k)
=\sum_kc_kx_k+\sum_kc_ky_k
=\varphi(x)+\varphi(y),
\]
and
\[
\varphi(ax)=\sum_kc_k(ax_k)
=a\sum_kc_kx_k=a\varphi(x).
\]
Thus the function is linear. When $n=0$, all sums in these equalities are zero, so the same calculation verifies the asserted zero functional.''',
    1, 10,
    [r'''Distribute inside each finite sum.'''],
    ['def-linear-functional', 'def-linear-map',
     'c1-def-coordinate-addition', 'c1-def-coordinate-scaling',
     'c1-thm-complex-laws'],
    number='3.109', page=105, kind='example'
)

s.r(
    'ex-functional-polynomial-values',
    'A functional using values and derivatives',
    r'''The function $\varphi:\Poly(\R)\to\R$ defined by
\[
\varphi(p)=3p''(5)+7p(4),
\]
where $p''=(p')'$, is a linear functional.''',
    r'''Polynomial differentiation is linear. Applying that fact twice gives
\[
(p+q)''=p''+q'',\qquad (ap)''=ap''
\]
for polynomials $p,q$ and real $a$. Evaluation of a pointwise sum or scalar multiple gives the corresponding sum or scalar multiple of its values. Therefore
\[
\begin{aligned}
\varphi(p+q)
&=3\bigl(p''(5)+q''(5)\bigr)+7\bigl(p(4)+q(4)\bigr)\\
&=\varphi(p)+\varphi(q),
\end{aligned}
\]
and
\[
\varphi(ap)=3ap''(5)+7ap(4)=a\varphi(p).
\]
The displayed values are real scalars, so this proves the claim.''',
    1, 10,
    [r'''Use linearity of differentiation twice and the pointwise rules for functions.'''],
    ['def-linear-functional', 'def-linear-map',
     'ex-polynomial-differentiation', 'c1-def-function-space'],
    number='3.109', page=105, kind='example'
)

s.r(
    'ex-functional-polynomial-integral',
    'A polynomial integral functional',
    r'''The function $J:\Poly(\R)\to\R$ defined by
\[
Jp=\int_0^1p(x)\,dx
\]
is a linear functional, with the integral understood by its earlier coefficient definition.''',
    r'''Write $p(x)=\sum_j a_jx^j$ and $q(x)=\sum_j b_jx^j$, adding trailing zero coefficients so that the finite sums have the same index range. The integral definition gives
\[
J(p+q)=\sum_j\frac{a_j+b_j}{j+1}
=\sum_j\frac{a_j}{j+1}+\sum_j\frac{b_j}{j+1}
=Jp+Jq.
\]
For $c\in\R$, it likewise gives
$J(cp)=\sum_j ca_j/(j+1)=cJp$.
Thus $J$ is linear with scalar outputs, which is precisely the functional condition.''',
    1, 10,
    [r'''Use the finite sum defining the integral of a polynomial.'''],
    ['def-linear-functional', 'def-polynomial-integral',
     'c2-def-polynomial', 'c2-lem-polynomial-coefficients'],
    number='3.109', page=105, kind='example'
)

s.d(
    'def-dual-space',
    'Dual space',
    r'''The \emph{dual space} of $V$ is
\[
\dual{V}=\Lin(V,\F).
\]
Its vectors are linear functionals. Addition and scalar multiplication are the pointwise operations already defined for linear maps, so the earlier vector-space theorem for $\Lin(V,\F)$ makes this a vector space, whether or not $V$ is finite-dimensional.''',
    '3.110', 105
)

s.r(
    'thm-dual-dimension',
    'A finite-dimensional space and its dual have equal dimensions',
    r'''If $V$ is finite-dimensional, then $\dual{V}$ is finite-dimensional and
\[
\dim\dual{V}=\dim V.
\]''',
    r'''The scalar space $\F$ has the one-element basis consisting of $1$: every scalar $a$ equals $a\cdot1$, and $a\cdot1=0$ forces $a=0$. Hence $\dim\F=1$. Applying the dimension theorem for spaces of linear maps to the finite-dimensional spaces $V$ and $\F$ gives
\[
\dim\dual{V}
=\dim\Lin(V,\F)
=(\dim V)(\dim\F)
=\dim V.
\]
That theorem also supplies finite-dimensionality of the space of maps. The calculation includes $V=\{0\}$, in which case both dimensions are zero.''',
    1, 10,
    [r'''Regard the dual as a space of linear maps with a one-dimensional target.'''],
    ['def-dual-space', 'thm-linear-map-dimension',
     'c2-def-basis', 'c2-def-dimension'],
    number='3.111', page=105
)

s.d(
    'def-dual-basis',
    'Dual basis',
    r'''Let $v_1,\ldots,v_n$ be a basis of $V$. For each $j$, let $\varphi_j\in\dual{V}$ be the unique linear functional with
\[
\varphi_j(v_k)=
\begin{cases}
1,&k=j,\\
0,&k\ne j.
\end{cases}
\]
Existence and uniqueness follow from the theorem on prescribing a linear map on a basis. The list $\varphi_1,\ldots,\varphi_n$ is called the \emph{dual basis} of the chosen basis; when $n=0$, it is the empty list.''',
    '3.112', 106
)

s.r(
    'ex-standard-dual-basis',
    'The dual of the standard coordinate basis',
    r'''For the standard basis $e_1,\ldots,e_n$ of $\F^n$, its dual basis consists of the coordinate selectors
\[
\varphi_j(x_1,\ldots,x_n)=x_j
\qquad(1\le j\le n).
\]
For $n=0$, both lists are empty.''',
    r'''Each coordinate selector is linear: it is the coordinate functional with coefficient $1$ in position $j$ and zero coefficients elsewhere. Its value at $e_k$ is $1$ when $k=j$ and $0$ otherwise. These are exactly the prescribed values in the definition of the dual basis. Uniqueness of a functional with specified basis values identifies it with $\varphi_j$.

When $n=0$, there are no selectors or basis vectors to specify, and the definition gives the empty dual list.''',
    1, 10,
    [r'''Evaluate the $j$th coordinate selector on every standard basis vector.'''],
    ['def-dual-basis', 'ex-functional-coordinate-combination',
     'thm-linear-map-basis', 'c2-ex-standard-basis'],
    number='3.113', page=106, kind='example'
)

s.r(
    'thm-dual-coordinates',
    'Dual functionals recover basis coefficients',
    r'''If $v_1,\ldots,v_n$ is a basis of $V$ and $\varphi_1,\ldots,\varphi_n$ is its dual basis, then every $v\in V$ satisfies
\[
v=\sum_{j=1}^{n}\varphi_j(v)v_j.
\]''',
    r'''Expand $v$ in the chosen basis as $v=\sum_{k=1}^{n}a_kv_k$. Applying $\varphi_j$ and using its linearity gives
\[
\varphi_j(v)=\sum_{k=1}^{n}a_k\varphi_j(v_k)=a_j,
\]
because its prescribed value is zero at every basis vector except $v_j$, where it is one. Substituting these values for all coefficients proves the formula.

If $n=0$, the basis condition implies $V=\{0\}$. The only vector $v$ is zero, and the asserted empty sum also equals zero.''',
    1, 10,
    [r'''Apply one dual functional to a basis expansion of the vector.'''],
    ['def-dual-basis', 'def-linear-functional',
     'c2-thm-basis-coordinates', 'def-linear-map'],
    number='3.114', page=106
)

s.r(
    'thm-dual-basis',
    'The dual basis spans the dual space independently',
    r'''If $v_1,\ldots,v_n$ is a basis of a finite-dimensional space $V$, then its dual basis $\varphi_1,\ldots,\varphi_n$ is a basis of $\dual{V}$.''',
    r'''Suppose $\sum_{j=1}^{n}a_j\varphi_j=0$, where zero denotes the zero functional. Evaluating this identity at $v_k$ gives
\[
0=\sum_{j=1}^{n}a_j\varphi_j(v_k)=a_k.
\]
Thus all coefficients vanish, proving independence.

To show spanning, let $\psi\in\dual{V}$. For every $v\in V$, the dual-coordinate formula and linearity of $\psi$ give
\[
\psi(v)=\psi\left(\sum_{j=1}^{n}\varphi_j(v)v_j\right)
=\sum_{j=1}^{n}\varphi_j(v)\psi(v_j)
=\left(\sum_{j=1}^{n}\psi(v_j)\varphi_j\right)(v).
\]
The two functionals agree at every input, so
$\psi=\sum_j\psi(v_j)\varphi_j$.
Hence the dual list spans $\dual{V}$ and is a basis.

For $n=0$, the domain is the zero space. Every linear functional sends its only vector to zero, so the dual space consists only of the zero functional. The empty list is then independent and spans this dual space, in agreement with the proof.''',
    2, 20,
    [
        r'''For independence, evaluate a zero relation on each original basis vector.''',
        r'''For spanning, apply an arbitrary functional to the dual-coordinate expansion of an arbitrary vector.'''
    ],
    ['def-dual-space', 'def-dual-basis', 'thm-dual-coordinates',
     'def-map-operations', 'def-linear-map', 'thm-linear-zero',
     'c2-def-basis', 'c2-def-linear-independence'],
    number='3.116', page=107
)

s.d(
    'def-dual-map',
    'Dual map',
    r'''For $T\in\Lin(V,W)$, prescribe the \emph{dual map}
\[
T':\dual{W}\to\dual{V},
\qquad
T'(\psi)=\psi\circ T.
\]
Thus $(T'\psi)(v)=\psi(Tv)$. The following result verifies that this prescription takes values in $\dual{V}$ and is linear.''',
    '3.118', 107
)

s.r(
    'thm-dual-map-linear',
    'The dual map is well-defined and linear',
    r'''For every $T\in\Lin(V,W)$, the prescribed dual map belongs to $\Lin(\dual{W},\dual{V})$. No finite-dimensionality assumption is needed.''',
    r'''For $\psi\in\dual{W}$, both $T:V\to W$ and $\psi:W\to\F$ are linear. Their composition is therefore a linear map $V\to\F$, so $T'\psi\in\dual{V}$. This proves that the prescription has the stated domain and target.

For $\psi,\theta\in\dual{W}$ and $v\in V$,
\[
(T'(\psi+\theta))(v)
=(\psi+\theta)(Tv)
=\psi(Tv)+\theta(Tv)
=(T'\psi+T'\theta)(v).
\]
For $a\in\F$,
\[
(T'(a\psi))(v)=(a\psi)(Tv)
=a\psi(Tv)=(aT'\psi)(v).
\]
Agreement at every $v$ proves the additivity and homogeneity identities for $T'$.''',
    1, 10,
    [
        r'''First check that composing the two maps gives a scalar-valued linear map.''',
        r'''Then evaluate the proposed linearity identities at an arbitrary vector of $V$.'''
    ],
    ['def-dual-map', 'def-dual-space', 'def-linear-functional',
     'lem-composition-linear', 'def-map-operations', 'def-linear-map'],
    page=107
)

s.r(
    'ex-dual-differentiation-evaluation',
    'Dual differentiation applied to evaluation',
    r'''Let $D:\Poly(\R)\to\Poly(\R)$ be differentiation, and let $E_3(p)=p(3)$. Prove that $E_3$ is a linear functional and that
\[
(D'E_3)(p)=p'(3)
\]
for every polynomial $p$.''',
    r'''Pointwise function operations give
$E_3(p+q)=p(3)+q(3)=E_3p+E_3q$ and
$E_3(ap)=ap(3)=aE_3p$.
Thus $E_3$ is a linear functional. The definition of the dual map now gives
\[
(D'E_3)(p)=E_3(Dp)=E_3(p')=p'(3).
\]
The prime in $D'$ denotes the dual map; the prime in $p'$ denotes the derivative.''',
    1, 10,
    [r'''Apply differentiation first and evaluation second.'''],
    ['def-dual-map', 'def-linear-functional',
     'ex-polynomial-differentiation', 'c1-def-function-space'],
    number='3.119', page=108, kind='example'
)

s.r(
    'ex-dual-differentiation-integral',
    'Dual differentiation applied to integration',
    r'''Let $D$ be differentiation on $\Poly(\R)$ and let $Jp=\int_0^1p(x)\,dx$. Prove directly from polynomial coefficients that
\[
(D'J)(p)=p(1)-p(0)
\]
for every $p\in\Poly(\R)$.''',
    r'''The integral map $J$ is a linear functional by the earlier example. If
$p(x)=\sum_{j=0}^{m}a_jx^j$, then
$p'(x)=\sum_{j=1}^{m}ja_jx^{j-1}$.
The definition of the dual map and the coefficient definition of the integral therefore give
\[
(D'J)(p)=J(p')
=\sum_{j=1}^{m}\frac{ja_j}{j}
=\sum_{j=1}^{m}a_j.
\]
Meanwhile $p(1)=\sum_{j=0}^{m}a_j$ and $p(0)=a_0$, so their difference is the same sum. For a constant polynomial, both sums over $j=1,\ldots,m$ are empty and the difference is zero, so the identity also holds in that case.''',
    2, 15,
    [
        r'''Compute $J(p')$ from the coefficient formula for $p$.''',
        r'''Compare the resulting coefficient sum with $p(1)-p(0)$.'''
    ],
    ['def-dual-map', 'ex-functional-polynomial-integral',
     'def-polynomial-integral', 'ex-polynomial-differentiation',
     'c2-thm-polynomial-differentiation', 'c2-def-polynomial'],
    number='3.119', page=108, kind='example'
)

s.r(
    'thm-dual-map-laws',
    'Addition, scaling, and reversed composition for dual maps',
    r'''Dual maps satisfy the following identities:
\[
(S+T)'=S'+T',\qquad (aT)'=aT'
\]
for $S,T\in\Lin(V,W)$ and $a\in\F$, and
\[
(RT)'=T'R'
\]
for $T\in\Lin(V,W)$ and $R\in\Lin(W,U)$. Consequently $T\mapsto T'$ is a linear map from $\Lin(V,W)$ to $\Lin(\dual{W},\dual{V})$.''',
    r'''Let $\psi\in\dual{W}$ and $v\in V$. Linearity of $\psi$ gives
\[
\begin{aligned}
((S+T)'\psi)(v)
&=\psi(Sv+Tv)\\
&=\psi(Sv)+\psi(Tv)
=((S'+T')\psi)(v).
\end{aligned}
\]
For a scalar $a$, it also gives
\[
((aT)'\psi)(v)=\psi(aTv)
=a\psi(Tv)=((aT')\psi)(v).
\]
Thus, for every input functional, the resulting functionals agree at every vector. This proves the first two identities.

For $\eta\in\dual{U}$ and $v\in V$,
\[
((RT)'\eta)(v)=\eta(R(Tv))
=(R'\eta)(Tv)
=(T'(R'\eta))(v)
=((T'R')\eta)(v).
\]
This establishes the composition identity, with the reversed order and matching domain $\dual{U}$ and target $\dual{V}$.

Every $T'$ is in the asserted target map space by the linearity theorem for dual maps. The first two identities are exactly the additivity and homogeneity conditions for the assignment $T\mapsto T'$, proving the last assertion.''',
    2, 20,
    [
        r'''Evaluate each map identity first on a functional and then on a vector.''',
        r'''For composition, follow the input vector through $T$, then $R$, then the functional.'''
    ],
    ['def-dual-map', 'thm-dual-map-linear', 'def-dual-space',
     'def-map-operations', 'def-map-composition',
     'def-linear-map', 'thm-linear-map-space'],
    number='3.120', page=108
)

s.p(
    'intro-annihilators',
    'Functionals that vanish on a chosen set',
    r'''To describe the kernel and range of a dual map, we need to collect functionals that vanish on specified vectors. The ambient space matters because it determines which functionals are available.''',
    109
)

s.d(
    'def-annihilator',
    'Annihilator',
    r'''For any subset $U\subseteq V$, its \emph{annihilator} in $\dual{V}$ is
\[
U^0=\{\varphi\in\dual{V}:\varphi(u)=0\text{ for every }u\in U\}.
\]
The subset $U$ need not be a subspace. The notation always refers to functionals on the stated ambient space $V$.''',
    '3.121', 109
)

s.r(
    'ex-annihilator-polynomial-multiples',
    'A functional vanishing on polynomial multiples',
    r'''Let
\[
U=\{x^2q(x):q\in\Poly(\R)\}\subseteq\Poly(\R).
\]
Prove that $U$ is a subspace and that the functional $\varphi(p)=p'(0)$ belongs to $U^0$.''',
    r'''Multiplication by $x^2$ is a linear map on polynomial space, and its range is exactly $U$. The range-subspace theorem makes $U$ a subspace.

For polynomials $p,r$ and real $a$, linearity of differentiation gives
\[
\varphi(p+r)=(p'+r')(0)=\varphi(p)+\varphi(r),
\qquad
\varphi(ap)=(ap')(0)=a\varphi(p).
\]
Thus $\varphi$ is a linear functional.

If $u=x^2q$ and $q(x)=\sum_{j=0}^{m}a_jx^j$, then
\[
u'(x)=\sum_{j=0}^{m}(j+2)a_jx^{j+1}.
\]
Every exponent in this sum is positive, so evaluation at zero gives $u'(0)=0$. Hence $\varphi$ vanishes on every element of $U$, proving $\varphi\in U^0$.''',
    2, 15,
    [
        r'''View $U$ as the range of multiplication by $x^2$.''',
        r'''Check the lowest exponent that can occur in the derivative of $x^2q$.'''
    ],
    ['def-annihilator', 'def-linear-functional',
     'ex-polynomial-multiplication', 'thm-range-subspace',
     'ex-polynomial-differentiation', 'c2-thm-polynomial-differentiation'],
    number='3.122', page=109, kind='example'
)

s.r(
    'ex-annihilator-coordinate-plane',
    'The annihilator of a coordinate plane',
    r'''Let $e_1,\ldots,e_5$ be the standard basis of $\R^5$, and let $\varphi_1,\ldots,\varphi_5$ be its dual basis. For $U=\Span(e_1,e_2)$, prove
\[
U^0=\Span(\varphi_3,\varphi_4,\varphi_5).
\]''',
    r'''The dual functionals are coordinate selectors. If
$\psi=a_3\varphi_3+a_4\varphi_4+a_5\varphi_5$ and $u=be_1+ce_2\in U$, each of $\varphi_3,\varphi_4,\varphi_5$ vanishes at $u$. Hence $\psi(u)=0$. This proves
$\Span(\varphi_3,\varphi_4,\varphi_5)\subseteq U^0$.

Conversely, let $\psi\in U^0$. Because the dual list is a basis of $(\R^5)'$, write
$\psi=\sum_{j=1}^{5}a_j\varphi_j$.
Both $e_1$ and $e_2$ belong to $U$, so
\[
0=\psi(e_1)=a_1,\qquad 0=\psi(e_2)=a_2.
\]
Thus $\psi=a_3\varphi_3+a_4\varphi_4+a_5\varphi_5$, proving the other inclusion.''',
    2, 20,
    [
        r'''Expand an arbitrary functional in the dual basis.''',
        r'''Its values at $e_1$ and $e_2$ determine which two coefficients must vanish.'''
    ],
    ['def-annihilator', 'ex-standard-dual-basis',
     'thm-dual-basis', 'def-dual-basis', 'c2-def-span'],
    number='3.123', page=109, kind='example'
)

s.r(
    'thm-annihilator-subspace',
    'An annihilator is a subspace',
    r'''For every subset $U\subseteq V$, the annihilator $U^0$ is a subspace of $\dual{V}$. If $U=\varnothing$, then $U^0=\dual{V}$.''',
    r'''The zero functional vanishes at every vector, so it belongs to $U^0$. If $\varphi,\psi\in U^0$ and $u\in U$, then
\[
(\varphi+\psi)(u)=\varphi(u)+\psi(u)=0+0=0.
\]
Thus $\varphi+\psi\in U^0$. For $a\in\F$ and $\varphi\in U^0$, one has
$(a\varphi)(u)=a\varphi(u)=a0=0$ for every $u\in U$, so $a\varphi\in U^0$. The subspace test in $\dual{V}$ proves the assertion.

When $U$ is empty, every linear functional satisfies the requirement of vanishing at every member of $U$, because there is no member at which it could fail. Thus the annihilator is the whole dual space in that case.''',
    1, 10,
    [r'''Use the pointwise operations on functionals and the subspace test.'''],
    ['def-annihilator', 'def-dual-space', 'def-map-operations',
     'thm-linear-map-space', 'c1-thm-subspace-test'],
    number='3.124', page=110
)

s.r(
    'thm-annihilator-dimension',
    'A basis and dimension formula for an annihilator',
    r'''Let $V$ be finite-dimensional and let $U$ be a subspace. Choose a basis $u_1,\ldots,u_m$ of $U$ and extend it to a basis $u_1,\ldots,u_n$ of $V$. If $\varphi_1,\ldots,\varphi_n$ is the corresponding dual basis, then
\[
\varphi_{m+1},\ldots,\varphi_n
\]
is a basis of $U^0$. Consequently
\[
\dim U^0=\dim V-\dim U.
\]''',
    r'''The required choices exist: a subspace of a finite-dimensional space is finite-dimensional, has a basis, and that basis extends to one of $V$.

For $j>m$, the functional $\varphi_j$ vanishes at every $u_k$ with $k\le m$. By linearity it vanishes on their span $U$. Thus each listed tail functional belongs to $U^0$.

For an arbitrary $\psi\in U^0$, expand in the full dual basis:
\[
\psi=\sum_{j=1}^{n}a_j\varphi_j.
\]
For each $k\le m$, evaluation at $u_k\in U$ gives $0=\psi(u_k)=a_k$. Hence
$\psi=\sum_{j=m+1}^{n}a_j\varphi_j$.
This proves that the tail list spans $U^0$.

A zero relation on the tail list becomes a zero relation on the full dual basis by inserting zero coefficients in the first $m$ positions. Independence of that full basis makes every tail coefficient zero. Thus the tail list is independent and is a basis of $U^0$.

Its length is $n-m$, whereas the chosen bases give $\dim V=n$ and $\dim U=m$. This proves the formula. If $m=0$, the tail is the whole dual basis. If $m=n$, it is empty and its span is $\{0\}$. The proof also covers $n=0$.''',
    3, 35,
    [
        r'''Adapt a basis of $V$ so that its first vectors form a basis of $U$.''',
        r'''An annihilating functional must have zero dual-basis coefficients in those first positions.'''
    ],
    ['def-annihilator', 'thm-annihilator-subspace',
     'def-dual-basis', 'thm-dual-basis',
     'c2-thm-subspaces-finite', 'c2-thm-basis-existence',
     'c2-thm-extend-independent', 'c2-def-basis',
     'c2-def-dimension', 'c2-def-linear-independence'],
    number='3.125', page=110
)

s.r(
    'thm-annihilator-extremes',
    'When an annihilator is zero or the whole dual',
    r'''For a subspace $U$ of a finite-dimensional vector space $V$,
\[
U^0=\{0\}\quad\Longleftrightarrow\quad U=V,
\]
and
\[
U^0=\dual{V}\quad\Longleftrightarrow\quad U=\{0\}.
\]''',
    r'''If $U^0=\{0\}$, its dimension is zero. The annihilator dimension formula gives $\dim U=\dim V$. Since $U$ is a subspace of the finite-dimensional space $V$, equality of dimensions implies $U=V$. Conversely, if $U=V$, a functional in $U^0$ vanishes on every vector of its domain and hence is the zero functional. The zero functional belongs to $U^0$, so $U^0=\{0\}$.

If $U^0=\dual{V}$, equality of the dimensions of $V$ and its dual, together with the annihilator formula, gives
\[
\dim V=\dim U^0=\dim V-\dim U.
\]
Thus $\dim U=0$, which implies $U=\{0\}$. Conversely, if $U=\{0\}$, every linear functional on $V$ vanishes on $U$ because linear maps preserve zero. Therefore every element of $\dual{V}$ belongs to $U^0$, proving $U^0=\dual{V}$. These arguments also apply when $V$ is the zero space.''',
    2, 20,
    [
        r'''Use the annihilator dimension formula for the implications from small or large annihilators.''',
        r'''For the reverse implications, inspect directly what the functionals must vanish on.'''
    ],
    ['def-annihilator', 'thm-annihilator-dimension',
     'thm-dual-dimension', 'thm-linear-zero',
     'c2-lem-zero-dimension', 'c2-thm-full-dimension-equality'],
    number='3.127', page=111
)

s.r(
    'thm-dual-null',
    'The null space of the dual map',
    r'''For arbitrary vector spaces $V,W$ and $T\in\Lin(V,W)$,
\[
\Null T'=(\Range T)^0,
\]
where the annihilator on the right is formed in $\dual{W}$. This equality does not require finite-dimensionality.''',
    r'''Take $\psi\in\dual{W}$. The condition $\psi\in\Null T'$ means that $T'\psi$ is the zero functional on $V$. By the dual-map definition, this is equivalent to
\[
\psi(Tv)=0\qquad\text{for every }v\in V.
\]
The vectors $Tv$, as $v$ varies, are exactly the members of $\Range T$. Thus the displayed condition is equivalent to $\psi$ vanishing on every member of $\Range T$, which is the condition
$\psi\in(\Range T)^0$.
This equivalence proves equality of the two subsets of $\dual{W}$.''',
    1, 10,
    [r'''Unwind what it means for $T'\psi$ to be the zero functional.'''],
    ['def-dual-map', 'thm-dual-map-linear',
     'def-null-space', 'def-range', 'def-annihilator'],
    number='3.128(a)', page=111
)

s.r(
    'thm-dual-null-dimension',
    'Dimension of the dual null space',
    r'''If $V,W$ are finite-dimensional and $T\in\Lin(V,W)$, then
\[
\dim\Null T'=\dim\Null T+\dim W-\dim V.
\]''',
    r'''The range of $T$ is a subspace of $W$. The dual null-space identity and the annihilator dimension formula in the ambient space $W$ give
\[
\dim\Null T'
=\dim(\Range T)^0
=\dim W-\dim\Range T.
\]
The fundamental theorem of linear maps gives
$\dim\Range T=\dim V-\dim\Null T$.
Substituting and regrouping the integers proves
\[
\dim\Null T'
=\dim W-(\dim V-\dim\Null T)
=\dim\Null T+\dim W-\dim V.
\]
All spaces whose dimensions occur are finite-dimensional under the hypotheses and the earlier dual-space and subspace theorems.''',
    2, 15,
    [
        r'''Apply the annihilator dimension formula in $W$, then use rank-nullity for $T$.'''
    ],
    ['thm-dual-null', 'thm-annihilator-dimension',
     'thm-range-subspace', 'thm-rank-nullity', 'thm-dual-dimension'],
    number='3.128(b)', page=112
)

s.r(
    'thm-surjective-dual-injective',
    'Surjectivity becomes injectivity under duality',
    r'''Let $V,W$ be finite-dimensional and $T\in\Lin(V,W)$. Then
\[
T\text{ is surjective}\quad\Longleftrightarrow\quad
T'\text{ is injective}.
\]''',
    r'''By the definition of surjectivity, $T$ is surjective exactly when $\Range T=W$. This range is a subspace of the finite-dimensional space $W$, so the annihilator criterion says that the equality is equivalent to
$(\Range T)^0=\{0\}$.
The dual null-space identity turns this into $\Null T'=\{0\}$. Because $T'$ is linear, the null-space criterion for injectivity says that this last condition is equivalent to injectivity of $T'$. Every step is an equivalence, proving both implications.''',
    2, 15,
    [
        r'''Translate surjectivity into a statement about the annihilator of the range.'''
    ],
    ['def-surjective', 'thm-range-subspace', 'thm-annihilator-extremes',
     'thm-dual-null', 'thm-dual-map-linear', 'thm-injective-null'],
    number='3.129', page=112
)

s.r(
    'thm-dual-range-dimension',
    'A map and its dual have ranges of equal dimension',
    r'''If $V,W$ are finite-dimensional and $T\in\Lin(V,W)$, then
\[
\dim\Range T'=\dim\Range T.
\]''',
    r'''The domain of $T'$ is $\dual{W}$, which is finite-dimensional. Rank-nullity applied to $T'$ gives
\[
\dim\Range T'=\dim\dual{W}-\dim\Null T'.
\]
The dual dimension theorem replaces the first dimension on the right by $\dim W$. The dual null-space identity and the annihilator dimension formula give
$\dim\Null T'=\dim W-\dim\Range T$.
Therefore
\[
\dim\Range T'
=\dim W-(\dim W-\dim\Range T)
=\dim\Range T.
\]
The same calculation permits any of these dimensions to be zero.''',
    2, 15,
    [
        r'''Apply rank-nullity to $T'$ and then compute its null-space dimension.'''
    ],
    ['thm-dual-map-linear', 'thm-dual-dimension',
     'thm-rank-nullity', 'thm-dual-null',
     'thm-annihilator-dimension', 'thm-range-subspace'],
    number='3.130(a)', page=112
)

s.r(
    'thm-dual-range',
    'The range of the dual map',
    r'''If $V,W$ are finite-dimensional and $T\in\Lin(V,W)$, then
\[
\Range T'=(\Null T)^0,
\]
where the annihilator is formed in $\dual{V}$.''',
    r'''Let $\varphi\in\Range T'$. Choose $\psi\in\dual{W}$ with
$\varphi=T'\psi=\psi\circ T$.
For any $v\in\Null T$, one has
\[
\varphi(v)=\psi(Tv)=\psi(0_W)=0,
\]
using preservation of zero by the linear functional $\psi$. Thus
$\varphi\in(\Null T)^0$, proving
$\Range T'\subseteq(\Null T)^0$.

Both sets are subspaces of $\dual{V}$: one is the range of a linear map, and the other is an annihilator. They are finite-dimensional because $\dual{V}$ is finite-dimensional. Their dimensions agree, since
\[
\begin{aligned}
\dim\Range T'
&=\dim\Range T\\
&=\dim V-\dim\Null T\\
&=\dim(\Null T)^0.
\end{aligned}
\]
The first equality is the preceding dual-range dimension theorem, the second is rank-nullity for $T$, and the third is the annihilator formula for the subspace $\Null T$ of $V$. A subspace of a finite-dimensional space with the same dimension as that space must equal it. Applying this to the established inclusion proves the desired equality.''',
    3, 30,
    [
        r'''First show that every functional of the form $\psi\circ T$ vanishes on $\Null T$.''',
        r'''After obtaining one inclusion, compare dimensions.'''
    ],
    ['def-range', 'def-dual-map', 'def-annihilator',
     'def-null-space', 'thm-linear-zero', 'thm-dual-range-dimension',
     'thm-rank-nullity', 'thm-annihilator-dimension',
     'thm-null-subspace', 'thm-range-subspace',
     'thm-annihilator-subspace', 'thm-dual-dimension',
     'c2-thm-subspaces-finite', 'c2-thm-full-dimension-equality'],
    number='3.130(b)', page=113
)

s.r(
    'thm-injective-dual-surjective',
    'Injectivity becomes surjectivity under duality',
    r'''Let $V,W$ be finite-dimensional and $T\in\Lin(V,W)$. Then
\[
T\text{ is injective}\quad\Longleftrightarrow\quad
T'\text{ is surjective}.
\]''',
    r'''The injectivity criterion gives
$T$ injective if and only if $\Null T=\{0\}$.
Because $\Null T$ is a subspace of the finite-dimensional space $V$, the annihilator criterion makes this equivalent to
$(\Null T)^0=\dual{V}$.
The dual-range theorem identifies $(\Null T)^0$ with $\Range T'$. Consequently the condition is equivalent to
$\Range T'=\dual{V}$.
The target of $T'$ is $\dual{V}$, so the last equality is exactly surjectivity of $T'$. These equivalences prove both directions.''',
    2, 15,
    [
        r'''Translate injectivity into a null-space statement, and then take its annihilator.'''
    ],
    ['thm-injective-null', 'thm-null-subspace',
     'thm-annihilator-extremes', 'thm-dual-range',
     'def-dual-map', 'def-surjective'],
    number='3.131', page=113
)

s.p(
    'intro-dual-matrices',
    'Representing dual maps in dual bases',
    r'''Fix bases in the original spaces and use their corresponding dual bases in the dual spaces. With these coordinated choices, reversing a linear map by duality exchanges the rows and columns of its representing matrix.''',
    113
)

s.r(
    'thm-dual-matrix',
    'The matrix of a dual map is the transpose',
    r'''Let $v_1,\ldots,v_n$ and $w_1,\ldots,w_m$ be bases of finite-dimensional spaces $V,W$, with corresponding dual bases $\varphi_1,\ldots,\varphi_n$ and $\psi_1,\ldots,\psi_m$. For $T\in\Lin(V,W)$, form $\Mat(T)$ using the original bases, and form $\Mat(T')$ using the domain basis $\psi_1,\ldots,\psi_m$ and target basis $\varphi_1,\ldots,\varphi_n$. Then
\[
\Mat(T')=\bigl(\Mat(T)\bigr)^{\mathsf t},
\]
where ${}^{\mathsf t}$ denotes transpose.''',
    r'''Put $A=\Mat(T)$ and $C=\Mat(T')$. The shapes are respectively $m$ by $n$ and $n$ by $m$. By the definition of a representing matrix,
\[
Tv_k=\sum_{r=1}^{m}A_{rk}w_r,
\qquad
T'\psi_j=\sum_{\ell=1}^{n}C_{\ell j}\varphi_\ell.
\]
For $1\le j\le m$ and $1\le k\le n$, evaluate the second equality at $v_k$. The defining values of the dual basis give
\[
(T'\psi_j)(v_k)
=\sum_{\ell=1}^{n}C_{\ell j}\varphi_\ell(v_k)
=C_{kj}.
\]
On the other hand, the dual-map definition and the first matrix expansion give
\[
(T'\psi_j)(v_k)
=\psi_j(Tv_k)
=\sum_{r=1}^{m}A_{rk}\psi_j(w_r)
=A_{jk}.
\]
Thus $C_{kj}=A_{jk}$ for every pair of indices, which is precisely the transpose rule.

If $m=0$ or $n=0$, both $C$ and $A^{\mathsf t}$ have the same shape and no entries. Equality then follows from equality of their shapes and the vacuous entry comparison. The argument is valid over both $\R$ and $\C$; the scalar coefficients are not conjugated.''',
    3, 30,
    [
        r'''The coefficient of $\varphi_k$ in $T'\psi_j$ can be recovered by evaluating at $v_k$.''',
        r'''Compute that same value as $\psi_j(Tv_k)$.'''
    ],
    ['def-map-matrix', 'def-transpose', 'def-dual-map',
     'def-dual-basis', 'thm-dual-basis', 'def-linear-map',
     'def-map-operations'],
    number='3.132', page=113
)

s.r(
    'thm-row-column-rank-duality',
    'Row rank equals column rank by duality',
    r'''For every $m$ by $n$ matrix $A$ over $\F$, its column rank equals its row rank. Give a proof using dual maps and the transpose formula, without using the earlier equality of row and column rank.''',
    r'''We first justify the connection between column spans and ranges without using row rank. Let $S:P\to Q$ be a linear map between finite-dimensional spaces with bases $p_1,\ldots,p_r$ and $q_1,\ldots,q_s$, and let $B$ be its representing matrix. Define the coordinate function
\[
\Gamma:Q\to\F^s,\qquad
\Gamma\left(\sum_{j=1}^{s}a_jq_j\right)=(a_1,\ldots,a_s).
\]
Unique basis coefficients make this well-defined. Adding two basis expansions adds their coefficient lists, and scaling an expansion scales that list, so $\Gamma$ is linear. Every coefficient list is the image of its displayed combination, and unique coefficients make $\Gamma$ injective. Hence it is an isomorphism.

Linearity of $S$ shows that $\Range S=\Span(Sp_1,\ldots,Sp_r)$: apply $S$ to a basis expansion of any input for one inclusion, and use closure of the range for the other. The vectors $\Gamma(Sp_k)$ are exactly the columns of $B$, viewed as lists of entries. It follows that
\[
\Gamma(\Range S)=\Span(\text{columns of }B).
\]
The restriction of $\Gamma$ is a linear bijection from $\Range S$ to this column span, so these spaces have equal dimensions. Thus the column rank of $B$ equals $\dim\Range S$. If columns are written as one-column matrices instead of lists, the correspondence that preserves all entries is a linear bijection, so the same dimension statement holds with that convention.

Now define $T:\F^n\to\F^m$ by
$(Tx)_j=\sum_{k=1}^{n}A_{jk}x_k$.
The coordinate-map theorem proves linearity. Evaluating $T$ at the standard basis vectors shows that its representing matrix is $A$. In the corresponding dual bases the matrix of $T'$ is $A^{\mathsf t}$. Applying the column-span conclusion to both maps and then using equality of their range dimensions yields
\[
\begin{aligned}
\text{column rank of }A
&=\dim\Range T\\
&=\dim\Range T'\\
&=\text{column rank of }A^{\mathsf t}\\
&=\text{row rank of }A.
\end{aligned}
\]
The last equality follows from the definition of transpose: its columns are the rows of $A$ with the same entries, so their spans have the same dimension after the entry-preserving row-to-column identification. Empty bases and empty column lists have zero span, so the proof includes $m=0$ or $n=0$.''',
    3, 35,
    [
        r'''First identify the dimension of a map range with the dimension of the span of its matrix columns.''',
        r'''Use a map with representing matrix $A$, and compare it with its dual map.''',
        r'''Transposition turns the original rows into columns.'''
    ],
    ['thm-coordinate-linear-maps', 'def-map-matrix',
     'def-row-column-rank', 'def-transpose',
     'thm-dual-matrix', 'thm-dual-range-dimension',
     'def-range', 'thm-range-subspace', 'def-linear-map',
     'thm-invertible-bijective', 'def-isomorphism',
     'thm-isomorphism-dimension', 'c2-thm-basis-coordinates',
     'c2-def-span'],
    number='3.133', page=114
)

s.card(
    'linear-functional',
    'def-linear-functional',
    r'''What is a linear functional on a vector space over $\F$?''',
    r'''A linear map from the space to the scalar field $\F$.'''
)

s.card(
    'dual-dimension',
    'thm-dual-dimension',
    r'''What is the dimension of the dual of a finite-dimensional space?''',
    r'''$\dim\dual{V}=\dim V$.'''
)

s.card(
    'dual-basis-values',
    'def-dual-basis',
    r'''Which values define the dual basis of $v_1,\ldots,v_n$?''',
    r'''The functional $\varphi_j$ takes value $1$ at $v_j$ and value $0$ at every other listed basis vector.'''
)

s.card(
    'dual-map-direction',
    'def-dual-map',
    r'''If $T:V\to W$ is linear, what are the domain, target, and formula of its dual map?''',
    r'''$T':\dual{W}\to\dual{V}$ is given by $T'\psi=\psi\circ T$.'''
)

s.card(
    'dual-composition-order',
    'thm-dual-map-laws',
    r'''How does duality affect the order of composition?''',
    r'''It reverses the order: $(RT)'=T'R'$.'''
)

s.card(
    'annihilator-definition',
    'def-annihilator',
    r'''What is the annihilator of $U\subseteq V$?''',
    r'''$U^0$ consists of all linear functionals on $V$ that vanish at every vector of $U$.'''
)

s.card(
    'annihilator-dimension',
    'thm-annihilator-dimension',
    r'''What is the dimension of $U^0$ when $U$ is a subspace of a finite-dimensional space $V$?''',
    r'''$\dim U^0=\dim V-\dim U$.'''
)

s.card(
    'dual-kernel-and-range',
    'thm-dual-range',
    r'''For a linear map between finite-dimensional spaces, how are the null space and range of its dual described by annihilators?''',
    r'''$\Null T'=(\Range T)^0$ in $\dual{W}$, and $\Range T'=(\Null T)^0$ in $\dual{V}$.'''
)

s.card(
    'dual-matrix-transpose',
    'thm-dual-matrix',
    r'''Which basis choices make the matrix of the dual map the transpose of the original matrix?''',
    r'''Use the corresponding dual bases, with the dual of the original target basis as domain basis and the dual of the original domain basis as target basis. No complex conjugation is involved.'''
)

s.write()
