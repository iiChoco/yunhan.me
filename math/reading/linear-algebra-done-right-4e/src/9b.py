from common import Section

s = Section('9b')

s.p(
    'intro-alternating-multilinear',
    'Multilinearity, alternation, and permutations',
    r'''Throughout this section, $V$ is a finite-dimensional vector space over $\F$. Multilinear forms are linear in each argument separately, and alternating forms vanish when two arguments agree. We extend the definitions to zero arguments so that the top-degree statements also apply to the zero-dimensional space.''',
    346,
)

s.d(
    'def-cartesian-power',
    'Ordered tuples of vectors',
    r'''For an integer $m\ge1$, let
\[
V^m=\underbrace{V\times\cdots\times V}_{m\text{ factors}},
\]
whose elements are ordered lists $(v_1,\ldots,v_m)$. Define $V^0=\{()\}$ to be the singleton containing the empty tuple.''',
    '9.24',
    346,
)

s.d(
    'def-multilinear-form',
    'Multilinear forms',
    r'''For an integer $m\ge1$, an $m$-linear form on $V$ is a function $\beta:V^m\to\F$ that is linear in each slot with all other slots fixed. Explicitly, for each slot $k$, scalars $a,b$, and vectors $x,y$,
\[
\beta(v_1,\ldots,ax+by,\ldots,v_m)
=a\beta(v_1,\ldots,x,\ldots,v_m)
+b\beta(v_1,\ldots,y,\ldots,v_m).
\]
Write $V^{(m)}$ for the set of these forms. A multilinear form means an $m$-linear form for some specified $m$.

A $0$-linear form is a function $V^0\to\F$. It has a single value $\beta(())$ and has no linearity conditions to check. We sometimes abbreviate its value to $\beta()$.''',
    '9.25',
    346,
)

s.r(
    'thm-multilinear-space',
    'Multilinear forms form a vector space',
    r'''For every integer $m\ge0$, $V^{(m)}$ is a vector space with pointwise addition and scalar multiplication. For $m=0$, evaluation at the empty tuple is a linear isomorphism
\[
V^{(0)}\longrightarrow\F,\qquad \beta\longmapsto\beta().
\]
For $m\ge1$, an $m$-linear form vanishes whenever one of its arguments is zero. Also, $V^{(1)}$ is exactly the dual space of $V$.''',
    r'''All functions $V^m\to\F$ form a vector space with pointwise operations. The zero function is multilinear. Suppose $\alpha,\beta$ are multilinear, and fix a slot and all other arguments. For scalars $a,b$, expanding in that slot gives
\[
\begin{aligned}
(\alpha+\beta)(\ldots,ax+by,\ldots)
&=a\alpha(\ldots,x,\ldots)+b\alpha(\ldots,y,\ldots)\\
&\quad+a\beta(\ldots,x,\ldots)+b\beta(\ldots,y,\ldots)\\
&=a(\alpha+\beta)(\ldots,x,\ldots)
+b(\alpha+\beta)(\ldots,y,\ldots).
\end{aligned}
\]
For a scalar $c$, the same expansion multiplied by $c$ gives the required identity for $c\alpha$. Thus the set is closed under addition and scalar multiplication. The subspace criterion proves that it is a vector space.

When $m=0$, the slot conditions are vacuous, so every function on the singleton $V^0$ is allowed. Evaluation at its one element preserves addition and scalar multiplication. It is injective because two functions on a singleton agree if their values there agree. It is surjective because any $c\in\F$ is the value of the function sending $()$ to $c$. Hence it is a linear isomorphism.

For $m\ge1$, fixing all arguments except a slot containing zero gives a linear functional in that slot. Linear maps send zero to zero, so the value of the form is zero. Finally, a $1$-linear form is precisely a linear map $V\to\F$, which is the definition of a member of the dual space.''',
    2,
    15,
    [
        r'''Use the function space as an ambient vector space and check closure slot by slot.''',
        r'''A function on a singleton is completely determined by its one value.''',
    ],
    [
        'def-cartesian-power',
        'def-multilinear-form',
        'c1-thm-function-space',
        'c1-thm-subspace-test',
        'c3-thm-linear-zero',
        'c3-def-dual-space',
        'c3-def-linear-functional',
        'c3-thm-invertible-bijective',
        'c3-def-isomorphism',
    ],
    page=346,
)

s.r(
    'ex-product-multilinear',
    'Multiplying two bilinear forms',
    r'''Let $\alpha,\rho\in V^{(2)}$. Then the formula
\[
\beta(v_1,v_2,v_3,v_4)
=\alpha(v_1,v_2)\rho(v_3,v_4)
\]
defines a $4$-linear form on $V$.''',
    r'''For fixed $v_2,v_3,v_4$, the map in the first slot is the linear functional $v_1\mapsto\alpha(v_1,v_2)$ multiplied by the fixed scalar $\rho(v_3,v_4)$, so it is linear. With $v_1,v_3,v_4$ fixed, the same argument uses linearity of $\alpha$ in its second slot.

For fixed $v_1,v_2,v_4$, the map in the third slot is $v_3\mapsto\rho(v_3,v_4)$ multiplied by the fixed scalar $\alpha(v_1,v_2)$, hence is linear. With $v_1,v_2,v_3$ fixed, linearity of $\rho$ in its second slot proves linearity in the fourth slot. All four slot conditions therefore hold.''',
    1,
    10,
    [
        r'''When one argument varies, the other factor is a fixed scalar.''',
    ],
    [
        'def-multilinear-form',
        'c3-thm-linear-map-space',
    ],
    '9.26(a)',
    346,
    'example',
)

s.r(
    'ex-trace-multilinear',
    'The trace of a product is multilinear',
    r'''For each integer $m\ge1$, the function on $\Lin(V)^m$ defined by
\[
\beta(T_1,\ldots,T_m)=\tr(T_1\cdots T_m)
\]
is an $m$-linear form. With the empty operator product interpreted as $I_V$, the same prescription for $m=0$ is the $0$-linear form with value $\tr I_V=\dim V$.''',
    r'''Fix a slot $k$ and all operators outside that slot. Let
\[
A=T_1\cdots T_{k-1},\qquad B=T_{k+1}\cdots T_m,
\]
using $I_V$ for either empty product. Distributivity and compatibility with scalar multiplication for composition give
\[
A(aS+bR)B=aASB+bARB.
\]
Linearity of trace therefore gives
\[
\tr(A(aS+bR)B)=a\tr(ASB)+b\tr(ARB).
\]
This proves linearity in slot $k$, and the choice of $k$ was arbitrary.

For $m=0$, there are no slots, so the prescription is a function on a singleton and is a $0$-linear form. In any basis, the identity matrix has $\dim V$ diagonal entries, all equal to $1$, so its trace is $\dim V$. On the zero space that diagonal is empty, and the trace is $0$, giving the same formula.''',
    1,
    10,
    [
        r'''Fix all factors except one, then use distributivity of composition and linearity of trace.''',
    ],
    [
        'def-multilinear-form',
        'c3-thm-composition-laws',
        'c8-thm-trace-linear-cyclic',
        'c8-def-matrix-trace',
        'c8-def-operator-trace',
        'c3-def-identity-matrix',
    ],
    '9.26(b)',
    346,
    'example',
)

s.d(
    'def-alternating-form',
    'Alternating multilinear forms',
    r'''An $m$-linear form $\alpha$ is alternating if
\[
\alpha(v_1,\ldots,v_m)=0
\]
whenever two arguments in distinct slots are equal. Denote the set of alternating $m$-linear forms by $V_{\mathrm{alt}}^{(m)}$.

For $m=0$ or $m=1$, there are no two distinct slots whose arguments could coincide, so the alternating condition is vacuous. In particular,
\[
V_{\mathrm{alt}}^{(0)}=V^{(0)},\qquad
V_{\mathrm{alt}}^{(1)}=V^{(1)}.
\]''',
    '9.27',
    347,
)

s.r(
    'thm-alternating-subspace',
    'Alternating forms form a subspace',
    r'''For every integer $m\ge0$, the set $V_{\mathrm{alt}}^{(m)}$ is a subspace of $V^{(m)}$.''',
    r'''The zero multilinear form vanishes on every tuple and is alternating. Let $\alpha,\beta$ be alternating and let $c\in\F$. Their sum and scalar multiple are multilinear because $V^{(m)}$ is a vector space. For any tuple with two equal arguments,
\[
(\alpha+\beta)(v_1,\ldots,v_m)=0+0=0,
\qquad
(c\alpha)(v_1,\ldots,v_m)=c\cdot0=0.
\]
Thus both forms are alternating. The subspace criterion applies. If $m=0$ or $m=1$, there are no repeated-slot tests; the alternating forms are the entire multilinear-form space, which gives the same conclusion.''',
    1,
    10,
    [
        r'''Check the subspace conditions on a tuple with two equal entries.''',
    ],
    [
        'def-alternating-form',
        'thm-multilinear-space',
        'c1-thm-subspace-test',
    ],
    page=347,
)

s.r(
    'thm-alternating-dependent',
    'Alternating forms vanish on dependent lists',
    r'''Let $m\ge1$ and $\alpha\in V_{\mathrm{alt}}^{(m)}$. If $v_1,\ldots,v_m$ is linearly dependent, then
\[
\alpha(v_1,\ldots,v_m)=0.
\]''',
    r'''Choose a relation
\[
\sum_{j=1}^m c_jv_j=0
\]
with at least one coefficient nonzero, and choose $k$ such that $c_k\ne0$. Solving for $v_k$ gives
\[
v_k=-\sum_{j\ne k}\frac{c_j}{c_k}v_j.
\]
If $m=1$, this says $v_k=0$, and a multilinear form vanishes when an argument is zero.

If $m\ge2$, substitute the displayed expression into slot $k$ and expand by linearity in that slot:
\[
\alpha(v_1,\ldots,v_m)
=-\sum_{j\ne k}\frac{c_j}{c_k}
\alpha(v_1,\ldots,v_{k-1},v_j,v_{k+1},\ldots,v_m).
\]
In the term indexed by $j$, slots $j$ and $k$ both contain $v_j$. Alternation makes each term zero. Their sum is therefore zero as well.''',
    2,
    15,
    [
        r'''Solve a nontrivial dependence relation for one vector.''',
        r'''Expand in that vector's slot and look for repeated arguments.''',
    ],
    [
        'def-alternating-form',
        'def-multilinear-form',
        'thm-multilinear-space',
        'c2-def-linear-dependence',
        'c1-lem-scalar-cancellation',
    ],
    '9.28',
    347,
)

s.r(
    'thm-alternating-excess-degree',
    'More arguments than dimensions force the zero form',
    r'''If $m>\dim V$, then $V_{\mathrm{alt}}^{(m)}=\{0\}$.''',
    r'''Put $n=\dim V$. The hypothesis $m>n\ge0$ implies $m\ge1$. Every list of $m$ vectors in $V$ is dependent: an independent list could have length at most the length $n$ of a basis. The preceding theorem therefore makes every alternating $m$-linear form vanish on every tuple in $V^m$. Hence it is the zero function. Conversely, the zero function is alternating, so the space is exactly $\{0\}$.

The strict inequality is essential to the scope of this conclusion: when $m=n=0$, it does not apply.''',
    1,
    10,
    [
        r'''Compare the length of an input list with a basis length.''',
    ],
    [
        'thm-alternating-dependent',
        'thm-alternating-subspace',
        'c2-thm-independent-length',
        'c2-thm-basis-existence',
        'c2-def-dimension',
    ],
    '9.29',
    347,
)

s.r(
    'thm-alternating-swap',
    'Exchanging any two arguments reverses the sign',
    r'''If $\alpha$ is alternating, exchanging the arguments in any two distinct slots multiplies its value by $-1$. Conversely, an $m$-linear form over $\F$ with this sign-change property is alternating. For $m=0$ or $m=1$, both conditions are vacuous.''',
    r'''Suppose $m\ge2$ and choose any two distinct slots $p,q$. Fix the arguments in all other slots, and let $F(x,y)$ denote the resulting function with $x$ in slot $p$ and $y$ in slot $q$. Multilinearity makes $F$ bilinear, regardless of whether the chosen slots are adjacent.

If $\alpha$ is alternating, then $F(x,x)=F(y,y)=F(x+y,x+y)=0$. Expanding the last equality gives
\[
0=F(x,x)+F(x,y)+F(y,x)+F(y,y)=F(x,y)+F(y,x).
\]
Thus $F(y,x)=-F(x,y)$, which proves the sign change for the chosen slots.

Conversely, suppose exchanging any two slots changes the sign. On a tuple with equal arguments in slots $p,q$, that exchange leaves the tuple unchanged. Its value $a$ therefore satisfies $a=-a$, so $2a=0$. Because $\F$ is $\R$ or $\C$, the scalar $2$ is nonzero and has an inverse; hence $a=0$. This proves alternation. When fewer than two slots are present, there is neither an exchange to test nor a pair of equal slots, so both properties hold vacuously.''',
    2,
    15,
    [
        r'''Put $x+y$ in both chosen slots and expand.''',
        r'''For the converse, exchange two equal arguments.''',
    ],
    [
        'def-alternating-form',
        'def-multilinear-form',
        'c1-lem-scalar-cancellation',
        'c1-def-field',
    ],
    '9.30',
    348,
)

s.r(
    'ex-alternating-three-cycle',
    'A cyclic rearrangement of three arguments',
    r'''If $\alpha$ is an alternating $3$-linear form, then
\[
\alpha(v_3,v_1,v_2)=\alpha(v_1,v_2,v_3)
\]
for all $v_1,v_2,v_3$.''',
    r'''Exchange the first two slots and then the last two slots. The sign-change theorem gives
\[
\alpha(v_3,v_1,v_2)
=-\alpha(v_1,v_3,v_2)
=\alpha(v_1,v_2,v_3).
\]
The two factors of $-1$ multiply to $1$, proving the equality, including tuples whose values are zero.''',
    1,
    10,
    [
        r'''Restore the original order using two swaps.''',
    ],
    [
        'thm-alternating-swap',
    ],
    page=348,
    kind='example',
)

s.d(
    'def-permutation',
    'Permutations and their inverses',
    r'''For an integer $m\ge0$, a permutation of $(1,\ldots,m)$ is a list containing each of $1,\ldots,m$ exactly once. Write $S_m$, also denoted $\operatorname{perm}m$, for the set of these lists.

A permutation $\sigma=(j_1,\ldots,j_m)$ can also be regarded as the bijection $\sigma(k)=j_k$. Its inverse permutation $\sigma^{-1}$ sends each value to the position where that value occurs; thus $\sigma^{-1}(\sigma(k))=k$.

There is exactly one element of $S_0$, the empty permutation. It is its own inverse.''',
    '9.31',
    348,
)

s.d(
    'def-permutation-sign',
    'Inversions and permutation signs',
    r'''An inversion of a permutation $\sigma\in S_m$ is a pair of positions $(a,b)$ with
\[
a<b,\qquad \sigma(a)>\sigma(b).
\]
Equivalently, it is a pair of values whose larger member occurs before its smaller member. Let $N(\sigma)$ be the number of inversions and define
\[
\operatorname{sgn}(\sigma)=(-1)^{N(\sigma)}.
\]
The empty permutation has zero inversions and sign $1$.''',
    '9.32',
    349,
)

s.r(
    'ex-permutation-signs',
    'Signs of some basic permutations',
    r'''The following signs hold:
\begin{enumerate}
\item The identity permutation $(1,\ldots,m)$ has sign $1$, including $m=0$.
\item The permutation $(2,1,3,4)$ has sign $-1$.
\item For $m\ge1$, the permutation $(2,3,\ldots,m,1)$ has sign $(-1)^{m-1}$; for $m=1$, this list means $(1)$.
\end{enumerate}
In particular, $(2,3,4,5,1)$ has sign $1$.''',
    r'''The identity list is increasing, so it has no inversions and has sign $(-1)^0=1$.

In $(2,1,3,4)$, the first two entries form an inversion. Every other pair is increasing, so there is exactly one inversion and the sign is $-1$.

In $(2,3,\ldots,m,1)$, the entries preceding $1$ are in increasing order. Each of those $m-1$ entries is larger than the final $1$, and these are all the inversions. The sign is therefore $(-1)^{m-1}$. For $m=1$, there are zero such entries and zero inversions. Taking $m=5$ yields $(-1)^4=1$.''',
    1,
    10,
    [
        r'''List exactly which pairs are reversed from increasing order.''',
    ],
    [
        'def-permutation',
        'def-permutation-sign',
    ],
    '9.33',
    349,
    'example',
)

s.r(
    'thm-permutation-sign',
    'Every transposition reverses permutation sign',
    r'''Exchanging the entries in any two distinct positions of a permutation multiplies its sign by $-1$. Moreover, a permutation can be rearranged into the identity by finitely many such exchanges. If a sequence of $q$ exchanges does so, then
\[
\operatorname{sgn}(\sigma)=(-1)^q.
\]''',
    r'''First exchange entries $x,y$ in adjacent positions $r,r+1$. Their own pair changes from an inversion to a non-inversion or from a non-inversion to an inversion. Its contribution therefore changes by $1$ or $-1$.

An entry before both positions contributes two comparisons, one with $x$ and one with $y$; their total number of inversions is unchanged by exchanging the positions of $x,y$. The same is true for an entry after both positions. Pairs not involving either position are unchanged. Because there are no positions between adjacent positions, these cases exhaust all pairs. Thus the total inversion count changes by an odd number, in fact by $1$ or $-1$, and the sign is reversed.

Now take positions $p<q$, and put $d=q-p$. Write the segment between these positions as
\[
(x,b_1,\ldots,b_{d-1},y).
\]
Move $x$ successively to the right across all $d$ following entries. The segment becomes
\[
(b_1,\ldots,b_{d-1},y,x).
\]
Then move $y$ left across the $d-1$ entries $b_{d-1},\ldots,b_1$. The segment becomes
\[
(y,b_1,\ldots,b_{d-1},x).
\]
Thus the desired exchange, with intermediate entries restored, is accomplished by $d+(d-1)=2d-1$ adjacent exchanges. Each reverses the sign, and their number is odd. Hence an exchange in arbitrary positions also reverses the sign.

To sort any permutation, process positions $k=1,\ldots,m$. If position $k$ already contains $k$, do nothing. Otherwise locate the unique occurrence of $k$ and exchange it with the entry in position $k$. The located position must exceed $k$, because the earlier positions already contain their correct distinct values. Each step therefore preserves the positions previously fixed. After finitely many exchanges the identity is obtained.

If a sequence of $q$ exchanges changes $\sigma$ into the identity, repeated sign reversal gives
\[
1=\operatorname{sgn}(\mathrm{id})=(-1)^q\operatorname{sgn}(\sigma).
\]
Multiplying by $(-1)^q$ gives the desired parity formula. For $m=0$ or $m=1$, the identity is the only permutation, no exchanges are possible, and the formula holds with $q=0$.''',
    3,
    30,
    [
        r'''First analyze adjacent positions, where no intermediate entries need to be considered.''',
        r'''Express an exchange at distance $d$ using $2d-1$ adjacent exchanges.''',
        r'''Sort a permutation by fixing its positions from left to right.''',
    ],
    [
        'def-permutation',
        'def-permutation-sign',
        'ex-permutation-signs',
        'c1-foundations',
    ],
    '9.34',
    349,
)

s.r(
    'lem-permutation-inverse-sign',
    'A permutation and its inverse have the same sign',
    r'''For every permutation $\sigma$,
\[
N(\sigma^{-1})=N(\sigma),
\qquad
\operatorname{sgn}(\sigma^{-1})=\operatorname{sgn}(\sigma).
\]''',
    r'''If $(a,b)$ is an inversion of $\sigma$, then $a<b$ and $\sigma(a)>\sigma(b)$. Put
\[
p=\sigma(b),\qquad q=\sigma(a).
\]
Then $p<q$, while
\[
\sigma^{-1}(p)=b>a=\sigma^{-1}(q).
\]
Thus $(p,q)$ is an inversion of $\sigma^{-1}$.

Conversely, from an inversion $(p,q)$ of $\sigma^{-1}$, define
\[
a=\sigma^{-1}(q),\qquad b=\sigma^{-1}(p).
\]
Its inversion inequalities give $a<b$, and $\sigma(a)=q>p=\sigma(b)$, so $(a,b)$ is an inversion of $\sigma$. These two constructions undo one another. They give a bijection between the finite inversion sets, proving equality of their cardinalities. Applying the definition $(-1)^N$ proves equality of signs. For the empty permutation, both inversion sets are empty and the same conclusion holds.''',
    2,
    15,
    [
        r'''Turn an inverted pair of positions into the corresponding pair of values in increasing order.''',
    ],
    [
        'def-permutation',
        'def-permutation-sign',
    ],
    page=349,
    kind='lemma',
)

s.r(
    'thm-alternating-permutation',
    'Permuting arguments of an alternating form',
    r'''Let $m\ge0$, $\alpha\in V_{\mathrm{alt}}^{(m)}$, and $\sigma=(j_1,\ldots,j_m)\in S_m$. Then
\[
\alpha(v_{j_1},\ldots,v_{j_m})
=\operatorname{sgn}(\sigma)\alpha(v_1,\ldots,v_m).
\]''',
    r'''Choose a sequence of $q$ exchanges that turns the list $(j_1,\ldots,j_m)$ into $(1,\ldots,m)$. Apply the same position exchanges to the argument list $(v_{j_1},\ldots,v_{j_m})$. Each exchange reverses the value of the alternating form, so
\[
\alpha(v_1,\ldots,v_m)
=(-1)^q\alpha(v_{j_1},\ldots,v_{j_m}).
\]
Multiplying by $(-1)^q$, whose square is $1$, gives
\[
\alpha(v_{j_1},\ldots,v_{j_m})
=(-1)^q\alpha(v_1,\ldots,v_m).
\]
The permutation-sign theorem identifies $(-1)^q$ with $\operatorname{sgn}(\sigma)$.

The argument depends on exchanges of positions, so it remains valid if some input vectors happen to agree. For $m=0$, both sides are $\alpha()$, because the empty permutation has sign $1$; for $m=1$, the only permutation is also the identity.''',
    2,
    15,
    [
        r'''Use the same sequence of exchanges to track the permutation sign and the form value.''',
    ],
    [
        'thm-alternating-swap',
        'thm-permutation-sign',
        'def-permutation',
        'def-permutation-sign',
    ],
    '9.35',
    350,
)

s.r(
    'thm-top-alternating-formula',
    'A top-degree alternating form is determined by one basis value',
    r'''Let $n=\dim V$, let $\mathcal E=(e_1,\ldots,e_n)$ be a basis, and write
\[
v_k=\sum_{j=1}^n b_{j,k}e_j
\qquad(1\le k\le n).
\]
For every $\alpha\in V_{\mathrm{alt}}^{(n)}$,
\[
\alpha(v_1,\ldots,v_n)
=\alpha(e_1,\ldots,e_n)
\sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)
\prod_{k=1}^n b_{\sigma(k),k}.
\]
For $n=0$, the sum has one term, its product is empty and equals $1$, and this identity reads $\alpha()=\alpha()$.''',
    r'''Suppose first $n\ge1$. Substitute the basis expansion into every slot. Repeated use of linearity, once in each slot, gives the finite expansion
\[
\alpha(v_1,\ldots,v_n)
=\sum_{j_1=1}^n\cdots\sum_{j_n=1}^n
\left(\prod_{k=1}^n b_{j_k,k}\right)
\alpha(e_{j_1},\ldots,e_{j_n}).
\]
Whenever two indices agree, the corresponding arguments agree and alternation makes the term zero. A list of $n$ distinct indices drawn from $\{1,\ldots,n\}$ contains every index exactly once, so the remaining lists are precisely the permutations.

For a surviving list associated with $\sigma\in S_n$, the alternating-permutation theorem gives
\[
\alpha(e_{\sigma(1)},\ldots,e_{\sigma(n)})
=\operatorname{sgn}(\sigma)\alpha(e_1,\ldots,e_n).
\]
Substitution into the finite sum and factoring out the common basis value yield the stated formula.

If $n=0$, the basis and input tuple are both empty. The unique empty permutation has sign $1$, and the stipulated empty product is $1$. Thus the formula reduces to equality of $\alpha()$ with itself, as asserted.''',
    3,
    30,
    [
        r'''Expand all arguments in the basis and use multilinearity in every slot.''',
        r'''Repeated basis indices make terms vanish; the remaining index lists are permutations.''',
    ],
    [
        'def-multilinear-form',
        'def-alternating-form',
        'thm-alternating-permutation',
        'def-permutation-sign',
        'c2-thm-basis-coordinates',
        'c1-foundations',
    ],
    '9.36',
    350,
)

s.d(
    'def-coordinate-alternating-form',
    'The normalized coordinate alternating form',
    r'''Let $\mathcal E=(e_1,\ldots,e_n)$ be a basis of $V$, and let $\varphi_1,\ldots,\varphi_n$ be its dual basis. Define a function $\omega_{\mathcal E}:V^n\to\F$ by
\[
\omega_{\mathcal E}(v_1,\ldots,v_n)
=\sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)
\prod_{k=1}^n\varphi_{\sigma(k)}(v_k).
\]
When $n=0$, this prescription gives $\omega_{\mathcal E}()=1$, using the unique empty permutation and an empty product. The next result proves that this function is alternating and multilinear.''',
    page=351,
)

s.r(
    'thm-coordinate-alternating-form',
    'The coordinate formula produces a nonzero alternating form',
    r'''For every basis $\mathcal E=(e_1,\ldots,e_n)$ of $V$, the function $\omega_{\mathcal E}$ belongs to $V_{\mathrm{alt}}^{(n)}$ and satisfies
\[
\omega_{\mathcal E}(e_1,\ldots,e_n)=1.
\]
In particular, it is nonzero, including when $n=0$.''',
    r'''Assume first $n\ge1$. Fix a slot $k$ and all the other arguments. For each permutation $\sigma$, the corresponding summand, as a function of the argument in slot $k$, is the linear functional $\varphi_{\sigma(k)}$ multiplied by the fixed scalar
\[
\operatorname{sgn}(\sigma)\prod_{\ell\ne k}
\varphi_{\sigma(\ell)}(v_\ell).
\]
It is therefore linear in that argument. A finite sum of linear functionals is linear, so $\omega_{\mathcal E}$ is linear in slot $k$. Since $k$ was arbitrary, it is multilinear.

To prove alternation, suppose arguments in two distinct slots $p,q$ agree. For each $\sigma\in S_n$, let $\tau$ be the permutation obtained by exchanging the entries $\sigma(p)$ and $\sigma(q)$ in those two positions. This pairing has no fixed points, because a permutation has distinct entries in distinct positions, and applying the exchange twice recovers $\sigma$. Hence it partitions $S_n$ into disjoint pairs.

The sign theorem gives $\operatorname{sgn}(\tau)=-\operatorname{sgn}(\sigma)$. All factors in the two summands agree outside positions $p,q$. At those positions, writing $v_p=v_q=w$, the factors in the first product are
\[
\varphi_{\sigma(p)}(w)\varphi_{\sigma(q)}(w),
\]
and the factors in the second product occur in the opposite order. Scalar commutativity makes these products equal. The signs are opposite, so each pair of summands cancels. The whole sum is zero. This proves alternation for every possible pair of equal slots. For $n=1$, there are no such pairs and alternation is vacuous.

Finally evaluate the function at $(e_1,\ldots,e_n)$. The dual-basis identities say
\[
\varphi_j(e_k)=
\begin{cases}
1,&j=k,\\
0,&j\ne k.
\end{cases}
\]
For any permutation other than the identity, there is some $k$ with $\sigma(k)\ne k$, making that product zero. The identity permutation contributes a product of ones and has sign $1$. The total is therefore $1$.

If $n=0$, the function on the singleton $V^0$ has value $1$ by its definition. It is multilinear and alternating because both requirements have no slots to test. Its value on the empty basis is $1$, so it is nonzero in this case as well.''',
    3,
    35,
    [
        r'''For multilinearity, fix a slot and regard the formula as a finite linear combination of coordinate functionals.''',
        r'''When two arguments agree, pair permutations by exchanging the indices in those two positions.''',
        r'''On the defining basis, determine which permutation can contribute a nonzero term.''',
    ],
    [
        'def-coordinate-alternating-form',
        'def-multilinear-form',
        'def-alternating-form',
        'thm-permutation-sign',
        'ex-permutation-signs',
        'c3-def-dual-basis',
        'c3-thm-linear-map-space',
        'c1-def-field',
    ],
    page=351,
    kind='lemma',
)

s.r(
    'thm-top-alternating-dimension',
    'The space of top-degree alternating forms has dimension one',
    r'''For $n=\dim V$,
\[
\dim V_{\mathrm{alt}}^{(n)}=1.
\]
More precisely, for any basis $\mathcal E=(e_1,\ldots,e_n)$, its normalized coordinate form is a basis of this one-dimensional space, and every $\alpha\in V_{\mathrm{alt}}^{(n)}$ satisfies
\[
\alpha=\alpha(e_1,\ldots,e_n)\omega_{\mathcal E}.
\]
Thus specifying an arbitrary scalar as the value on $\mathcal E$ specifies exactly one alternating $n$-linear form.''',
    r'''Fix a basis $\mathcal E$, and take any alternating $n$-linear form $\alpha$. For input vectors $v_1,\ldots,v_n$, their basis coefficients are
\[
b_{j,k}=\varphi_j(v_k)
\]
by the dual-coordinate theorem. The top-degree expansion formula therefore gives
\[
\begin{aligned}
\alpha(v_1,\ldots,v_n)
&=\alpha(e_1,\ldots,e_n)
\sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)
\prod_{k=1}^n\varphi_{\sigma(k)}(v_k)\\
&=\alpha(e_1,\ldots,e_n)\omega_{\mathcal E}(v_1,\ldots,v_n).
\end{aligned}
\]
Agreement on every tuple proves the stated equality of functions.

The coordinate form is alternating and has value $1$ on $\mathcal E$, so it is a nonzero member of the space. The equality just proved shows that it spans the space. A single nonzero vector is independent, so the one-element list consisting of $\omega_{\mathcal E}$ is a basis, and the dimension is one.

Given a scalar $c$, the form $c\omega_{\mathcal E}$ has value $c$ on the basis. Conversely, any form with that value must equal $c\omega_{\mathcal E}$ by the displayed equality, proving uniqueness.

For $n=0$, the same computation uses the unique empty tuple and gives $\alpha=\alpha()\omega_{\mathcal E}$ with $\omega_{\mathcal E}()=1$. Thus it proves the dimension and uniqueness assertions for the zero-dimensional space as well.''',
    2,
    20,
    [
        r'''Compare an arbitrary form with the normalized coordinate form using the basis expansion formula.''',
        r'''Exhibit one nonzero spanning vector in the space of forms.''',
    ],
    [
        'thm-alternating-subspace',
        'thm-top-alternating-formula',
        'def-coordinate-alternating-form',
        'thm-coordinate-alternating-form',
        'c3-thm-dual-coordinates',
        'c2-ex-single-independent',
        'c2-def-basis',
        'c2-def-dimension',
        'c2-thm-basis-existence',
    ],
    '9.37',
    351,
)

s.r(
    'thm-top-alternating-independence',
    'A nonzero top-degree form detects linear independence',
    r'''Let $n=\dim V$ and let $\alpha\in V_{\mathrm{alt}}^{(n)}$ be nonzero. For a list $v_1,\ldots,v_n$ in $V$,
\[
\alpha(v_1,\ldots,v_n)\ne0
\quad\Longleftrightarrow\quad
v_1,\ldots,v_n\text{ is linearly independent}.
\]''',
    r'''Suppose first $n\ge1$. If the form has a nonzero value on the list, the theorem that alternating forms vanish on dependent lists shows that this list cannot be dependent. It is therefore independent.

Conversely, suppose the list is independent. Its length is $\dim V$, so it is a basis. Apply the top-degree form formula using this basis. If $\alpha(v_1,\ldots,v_n)$ were zero, that formula would make $\alpha$ vanish on every input tuple. This would make it the zero form, contrary to the hypothesis. Hence its value on the list is nonzero.

If $n=0$, the only input is the empty tuple. Since $\alpha$ is a nonzero function on a singleton, its one value $\alpha()$ is nonzero. The empty list is independent by definition. Thus both sides of the equivalence hold in this case as well.''',
    2,
    15,
    [
        r'''Use vanishing on dependent inputs for one direction.''',
        r'''For the other direction, the input list is a basis; a zero basis value would force the entire form to vanish.''',
    ],
    [
        'thm-alternating-dependent',
        'thm-top-alternating-formula',
        'def-cartesian-power',
        'def-multilinear-form',
        'c2-thm-full-length-independent',
        'c2-def-linear-independence',
    ],
    '9.39',
    352,
)

s.card(
    'multilinear-definition',
    'def-multilinear-form',
    r'''What does it mean for a form to be $m$-linear?''',
    r'''It is a scalar-valued function of $m$ vector arguments that is linear in each slot when all the other arguments are held fixed.''',
)

s.card(
    'zero-arity-form',
    'thm-multilinear-space',
    r'''What is a $0$-linear form, and how is its space identified with $\F$?''',
    r'''It is a function on the singleton containing the empty tuple. Evaluation at that tuple is a linear isomorphism from the space of such forms to $\F$.''',
)

s.card(
    'alternating-definition',
    'def-alternating-form',
    r'''What additional condition makes a multilinear form alternating?''',
    r'''Its value is zero whenever two arguments in distinct slots are equal. For zero or one slot, this condition is vacuous.''',
)

s.card(
    'dependent-inputs',
    'thm-alternating-dependent',
    r'''Why does an alternating form vanish on a dependent input list?''',
    r'''Express one input as a combination of the others and expand in its slot. Every resulting term has a repeated argument; a zero argument also gives zero.''',
)

s.card(
    'excess-alternating-degree',
    'thm-alternating-excess-degree',
    r'''When must every alternating $m$-linear form on $V$ be zero because of dimension alone?''',
    r'''When $m>\dim V$, because every input list of that length is dependent.''',
)

s.card(
    'permutation-sign-definition',
    'def-permutation-sign',
    r'''How is a permutation's sign defined without choosing a sequence of swaps?''',
    r'''It is $(-1)^N$, where $N$ counts pairs of positions $a<b$ with $\sigma(a)>\sigma(b)$.''',
)

s.card(
    'arbitrary-transposition-sign',
    'thm-permutation-sign',
    r'''Why does exchanging entries at distance $d$ reverse permutation sign?''',
    r'''That exchange can be made using $2d-1$ adjacent exchanges, an odd number, and each adjacent exchange reverses the sign.''',
)

s.card(
    'alternating-permutation-rule',
    'thm-alternating-permutation',
    r'''How does a permutation of the arguments affect an alternating form?''',
    r'''$\displaystyle \alpha(v_{\sigma(1)},\ldots,v_{\sigma(m)})
=\operatorname{sgn}(\sigma)\alpha(v_1,\ldots,v_m)$.''',
)

s.card(
    'top-form-dimension',
    'thm-top-alternating-dimension',
    r'''What is the dimension of the space of alternating $(\dim V)$-linear forms on $V$?''',
    r'''It is $1$, including when $\dim V=0$. A form is determined by its value on any chosen basis.''',
)

s.card(
    'top-form-independence',
    'thm-top-alternating-independence',
    r'''What does a nonzero alternating $n$-linear form detect when $n=\dim V$?''',
    r'''It is nonzero on an input list exactly when that list is linearly independent, equivalently when it is a basis.''',
)

s.write()
