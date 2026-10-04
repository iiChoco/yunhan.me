from common import Section

s = Section('2a')

s.p('intro-span-independence', 'Building a space from a finite list', r'''We now ask which vectors can be assembled from a given finite list by addition and scalar multiplication. Spanning measures whether the list reaches every vector, while linear independence measures whether its coefficients are determined uniquely. Comparing these two properties will give a bound on the size of an independent list.''', 28)

s.d('def-vector-list', 'Notation for lists of vectors', r'''We usually write a list of vectors as $v_1,\ldots,v_m$, without outer parentheses. Parentheses inside such a list may still describe individual coordinate vectors. A list may be empty, in which case its length is zero.''', '2.1', 28)

s.d('def-linear-combination', 'Linear combinations', r'''A linear combination of vectors $v_1,\ldots,v_m\in V$ is an expression
\[\sum_{j=1}^m a_jv_j\qquad(a_1,\ldots,a_m\in\F).\]
Its value is an element of $V$. An empty sum of vectors means the zero vector, so the empty list has exactly one linear combination, namely $0$.''', '2.2', 28)

s.r('ex-linear-combinations', 'Solving for a linear combination', r'''In $\R^3$, put $u=(2,1,-3)$ and $v=(1,-2,4)$. Prove that $(17,-4,2)$ is a linear combination of $u,v$, whereas $(17,-4,5)$ is not.''',
r'''Coordinate arithmetic gives $6u+5v=(12,6,-18)+(5,-10,20)=(17,-4,2)$. Suppose $au+bv=(17,-4,5)$. The first two coordinates require $2a+b=17$ and $a-2b=-4$. Substituting $b=17-2a$ into the second equation gives $5a=30$, hence $a=6$ and $b=5$. These coefficients give third coordinate $-3a+4b=2$, which is not $5$. Thus the second vector has no such representation.''',
2, 15, [r'Use the first two coordinates to determine the only possible coefficients.'],
['def-linear-combination', 'c1-def-coordinate-addition', 'c1-def-coordinate-scaling'], '2.3', 28, 'example')

s.d('def-span', 'Span of a list', r'''The span $\Span(v_1,\ldots,v_m)$ is the set of values of all linear combinations of $v_1,\ldots,v_m$. In particular, $\Span()=\{0\}$ for the empty list.''', '2.4', 29)

s.r('ex-span-membership', 'Membership and nonmembership in a span', r'''For $u=(2,1,-3)$ and $v=(1,-2,4)$ in $\R^3$,
\[(17,-4,2)\in\Span(u,v),\qquad (17,-4,5)\notin\Span(u,v).\]''',
r'''By definition, belonging to $\Span(u,v)$ means being a linear combination of $u,v$. The preceding example supplies such a combination for $(17,-4,2)$ and rules out every such combination for $(17,-4,5)$.''',
1, 10, [r'Translate each membership assertion using the definition of span.'],
['def-span', 'ex-linear-combinations'], '2.5', 29, 'example')

s.r('thm-span-smallest', 'Span is the smallest containing subspace', r'''For a list $v_1,\ldots,v_m$ in $V$, its span is a subspace containing every vector in the list. Moreover, every subspace of $V$ containing those vectors contains their span.''',
r'''First suppose $m>0$. Taking every coefficient to be zero gives $0$ in the span. If $x=\sum a_jv_j$ and $y=\sum b_jv_j$, the vector space axioms, applied finitely many times, give
\[x+y=\sum_{j=1}^m(a_j+b_j)v_j,\qquad
cx=\sum_{j=1}^m(ca_j)v_j\quad(c\in\F).\]
Thus the span is closed under addition and scalar multiplication, and the subspace test makes it a subspace. To obtain $v_k$, choose coefficient $1$ at position $k$ and $0$ at every other position. Hence every listed vector is in the span. If a subspace $U$ contains every $v_j$, closure under scalar multiplication puts each $a_jv_j$ in $U$, and induction using closure under addition puts their sum in $U$. Therefore $U$ contains the span. When $m=0$, the span is $\{0\}$. It is a subspace because $0+0=0$ and $c0=0$; every subspace contains $0$, and there are no listed vectors to check.''',
2, 20, [r'Check the subspace test, then use closure of any competing subspace.'],
['def-span', 'c1-def-vector-space', 'c1-thm-zero-scalar', 'c1-thm-scalar-zero', 'c1-thm-subspace-test'], '2.6', 29)

s.d('def-spanning-list', 'Spanning a vector space', r'''A list $v_1,\ldots,v_m$ spans $V$ if $\Span(v_1,\ldots,v_m)=V$. Thus every vector in $V$ must be a linear combination of the list.''', '2.7', 29)

s.r('ex-standard-spanning', 'The standard coordinate list spans', r'''For $n\ge1$, let $e_j\in\F^n$ have coordinate $1$ in position $j$ and coordinate $0$ in every other position. Then $e_1,\ldots,e_n$ spans $\F^n$. For $n=0$, the empty list spans $\F^0$.''',
r'''If $x=(x_1,\ldots,x_n)$, the $k$th coordinate of $\sum_{j=1}^n x_je_j$ is $x_k$, because all its other summands have $k$th coordinate zero. Equality of all coordinates gives $x=\sum x_je_j$. Thus every $x\in\F^n$ is in the span. Conversely, each linear combination is an element of $\F^n$, so the span equals $\F^n$. If $n=0$, $\F^0$ consists of its zero vector, the empty list; it therefore equals the span of the empty list.''',
1, 10, [r'Use the coordinates of the target vector as coefficients.'],
['def-spanning-list', 'def-span', 'c1-def-coordinate-space', 'c1-def-coordinate-addition', 'c1-def-coordinate-scaling'], '2.8', 30, 'example')

s.d('def-finite-dimensional', 'Finite-dimensional spaces', r'''A vector space is finite-dimensional if it has a finite spanning list. The empty list is allowed, so the zero space is finite-dimensional.''', '2.9', 30)

s.d('def-polynomial', 'Polynomial functions', r'''A polynomial over $\F$ is a function $p:\F\to\F$ for which there are a nonnegative integer $m$ and coefficients $a_0,\ldots,a_m\in\F$ such that
\[p(z)=\sum_{j=0}^m a_jz^j\quad\text{for every }z\in\F.\]
The set of these functions is denoted by $\Poly(\F)$. Addition and scalar multiplication are the operations inherited from the function space $\F^\F$.''', '2.10', 30)

s.r('thm-polynomial-subspace', 'Polynomial functions form a subspace', r'''The set $\Poly(\F)$ is a subspace of $\F^\F$, and hence is a vector space over $\F$.''',
r'''The zero function has the polynomial representation $p(z)=0$. If $p$ and $q$ have polynomial representations, append zero coefficients to the shorter representation so that both are indexed from $0$ to the same integer $m$. Writing their coefficients as $a_j$ and $b_j$, pointwise addition gives $(p+q)(z)=\sum_{j=0}^m(a_j+b_j)z^j$. For $c\in\F$, scalar multiplication gives $(cp)(z)=\sum_{j=0}^m(ca_j)z^j$. Thus addition and scalar multiplication preserve $\Poly(\F)$. The function-space theorem gives the ambient vector space, and the subspace test proves the claim.''',
1, 10, [r'Append zero coefficients so that two representations have the same length.'],
['def-polynomial', 'c1-thm-function-space', 'c1-thm-subspace-test'], page=30)

s.r('lem-power-difference', 'Leading coefficient of a power difference', r'''For every integer $j\ge1$, the function $(z+1)^j-z^j$ has a representation
\[(z+1)^j-z^j=jz^{j-1}+\sum_{k=0}^{j-2}b_kz^k\]
with scalars $b_k$. When $j=1$, the sum on the right is empty and means zero.''',
r'''For $j=1$, the difference is $1$, as required. Suppose the assertion holds for some $j\ge1$, and write $D_j(z)=(z+1)^j-z^j$. Scalar distributivity and the laws of powers give
\[
\begin{aligned}
(z+1)^{j+1}-z^{j+1}
&=(z+1)\big((z+1)^j-z^j\big)+z^j\\
&=(z+1)D_j(z)+z^j.
\end{aligned}
\]
By the induction hypothesis, multiplying $D_j$ by $z$ contributes $jz^j$, while its remaining terms have exponents at most $j-1$. Multiplying $D_j$ by $1$ contributes only terms with exponents at most $j-1$. The final $z^j$ therefore changes the coefficient of $z^j$ to $j+1$. Collecting the finitely many lower powers produces the required representation for $j+1$. Induction proves the assertion.''',
2, 20, [r'Find a recurrence relating the difference for exponent $j+1$ to the difference for exponent $j$.'],
['def-polynomial', 'c1-foundations', 'c1-thm-complex-laws', 'c1-lem-scalar-powers'], page=30, kind='lemma')

s.r('lem-polynomial-coefficients', 'Uniqueness of polynomial coefficients', r'''If
\[\sum_{j=0}^m a_jz^j=0\quad\text{for every }z\in\F,\]
then $a_0=\cdots=a_m=0$. Consequently, two representations of the same polynomial have identical coefficients after trailing zero coefficients are appended to make their lengths equal.''',
r'''We prove the first assertion by induction on the nonnegative integer $m$. For $m=0$, the identity directly gives $a_0=0$. Suppose $m\ge1$ and the assertion holds for representations indexed from $0$ to $m-1$. Subtract the assumed identity at $z$ from the same identity at $z+1$. The constant term cancels, and the power-difference lemma shows that
\[\sum_{j=1}^m a_j\big((z+1)^j-z^j\big)=0\]
has a representation using powers from $0$ through $m-1$, whose coefficient of $z^{m-1}$ is $ma_m$. By the induction hypothesis every coefficient in this representation is zero, in particular $ma_m=0$. The positive integer $m$, regarded as a real or complex scalar, is nonzero, so scalar cancellation gives $a_m=0$. The original identity now has exponents at most $m-1$, and the induction hypothesis gives all the remaining $a_j=0$. This completes the induction. For two representations of one function, append zero coefficients as needed and subtract their values at each $z$. The first assertion makes each coefficient difference zero, proving uniqueness.''',
3, 35, [r'Apply induction to a representation of an identically zero function.', r'Compare its values at $z+1$ and $z$ to lower the largest exponent.'],
['def-polynomial', 'lem-power-difference', 'c1-foundations', 'c1-lem-scalar-cancellation'], page=30, kind='lemma')

s.d('def-degree', 'Degree of a polynomial', r'''For a nonzero polynomial $p$, its degree, denoted by $\deg p$, is the largest index with a nonzero coefficient in a polynomial representation. Coefficient uniqueness makes this independent of the representation. Set $\deg 0=-\infty$, and use the convention that $-\infty$ is smaller than every integer.''', '2.11', 31)

s.d('def-polynomial-space', 'Polynomials of bounded degree', r'''For a nonnegative integer $m$, define
\[\Poly_m(\F)=\{p\in\Poly(\F):\deg p\le m\}.\]
In lists of polynomial functions, the symbol $z^j$ denotes the function sending a scalar $z$ to its $j$th power. In particular, $1$ denotes the constant function with value $1$.''', '2.12', 31)

s.r('thm-bounded-polynomials', 'Bounded-degree polynomials are finitely spanned', r'''For every nonnegative integer $m$,
\[\Poly_m(\F)=\Span(1,z,\ldots,z^m).\]
In particular, $\Poly_m(\F)$ is a finite-dimensional vector space.''',
r'''A linear combination of $1,z,\ldots,z^m$ has a representation using only exponents at most $m$. Coefficient uniqueness and the definition of degree imply that its degree is at most $m$, including the zero polynomial. Conversely, every nonzero member of $\Poly_m(\F)$ has such a representation after appending zero coefficients, and the zero polynomial is obtained by taking every coefficient zero. This proves the equality. The span is a subspace of the polynomial vector space by the smallest-containing-subspace theorem. Its displayed finite spanning list then makes it finite-dimensional.''',
1, 10, [r'Translate the degree bound into a bound on the exponents in a representation.'],
['def-polynomial-space', 'lem-polynomial-coefficients', 'def-degree', 'thm-polynomial-subspace', 'thm-span-smallest', 'def-finite-dimensional'], page=31)

s.d('def-infinite-dimensional', 'Infinite-dimensional spaces', r'''A vector space is infinite-dimensional if no finite list spans it.''', '2.13', 31)

s.r('thm-polynomials-infinite', 'The polynomial space is infinite-dimensional', r'''The vector space $\Poly(\F)$ is infinite-dimensional.''',
r'''Consider an arbitrary finite list $p_1,\ldots,p_r$ of polynomials. If the list is empty or every listed polynomial is zero, its span is $\{0\}$, which does not contain the constant function $1$. Otherwise, let $m$ be the largest degree among the nonzero polynomials in the list. Every $p_j$ belongs to $\Poly_m(\F)$, including any zero entries. Because $\Poly_m(\F)$ is a subspace, the span of the list is contained in $\Poly_m(\F)$. The polynomial $z^{m+1}$ has degree $m+1$ by coefficient uniqueness, so it is outside this subspace and outside the span. Every finite list therefore fails to span $\Poly(\F)$.''',
2, 20, [r'Look for a degree bound shared by all linear combinations of a fixed finite list.'],
['def-infinite-dimensional', 'thm-polynomial-subspace', 'thm-bounded-polynomials', 'lem-polynomial-coefficients', 'def-degree', 'thm-span-smallest'], '2.14', 31, 'example')

s.d('def-linear-independence', 'Linear independence', r'''A list $v_1,\ldots,v_m$ is linearly independent if
\[\sum_{j=1}^m a_jv_j=0\quad\Longrightarrow\quad a_1=\cdots=a_m=0.\]
The empty list is linearly independent: it has no coefficients that could be nonzero.''', '2.15', 32)

s.r('thm-independent-coordinates', 'Independence and uniqueness of coefficients', r'''A list is linearly independent if and only if each vector in its span has exactly one representation as a linear combination of that list.''',
r'''Suppose the list is independent and $\sum a_jv_j=\sum b_jv_j$. Distributing and regrouping gives
\[\sum_{j=1}^m(a_j-b_j)v_j=0.\]
Indeed, adding $\sum(-b_j)v_j$ to either side cancels the sum on the right, because regrouping pairs each $b_jv_j$ with its additive inverse $(-b_j)v_j$. Independence gives $a_j-b_j=0$ for every $j$, hence $a_j=b_j$. A representation exists by the definition of span, so it is unique. Conversely, the zero vector has a representation with all coefficients zero. If representations are unique, every relation $\sum a_jv_j=0$ must use these same coefficients, proving independence. For an empty list, its span is $\{0\}$ and its only coefficient list is empty, so both assertions hold.''',
2, 15, [r'Compare two representations by subtracting them.', r'For the reverse implication, consider representations of the zero vector.'],
['def-linear-independence', 'def-span', 'c1-def-vector-space', 'c1-def-vector-subtraction', 'c1-thm-negative-one', 'c1-thm-zero-scalar'], page=32)

s.r('ex-standard-independent', 'Standard coordinate vectors are independent', r'''For $0\le r\le n$, the list $e_1,\ldots,e_r$ of standard coordinate vectors in $\F^n$ is linearly independent. This includes the first three standard vectors in $\F^4$.''',
r'''When $r=0$, this is the convention for the empty list. Otherwise, suppose $\sum_{j=1}^r a_je_j=0$. For each $k$ with $1\le k\le r$, the $k$th coordinate of the left side is $a_k$, while that of the right side is zero. Thus every coefficient is zero, establishing independence.''',
1, 10, [r'Read a coefficient from the corresponding coordinate.'],
['def-linear-independence', 'ex-standard-spanning', 'c1-def-coordinate-addition', 'c1-def-coordinate-scaling'], '2.16(a)', 32, 'example')

s.r('ex-monomial-independent', 'Distinct consecutive monomials are independent', r'''For every nonnegative integer $m$, the list $1,z,\ldots,z^m$ is linearly independent in $\Poly(\F)$.''',
r'''A relation $a_0+a_1z+\cdots+a_mz^m=0$ in this function space means that its left side equals zero at every scalar argument. Coefficient uniqueness therefore gives $a_0=\cdots=a_m=0$. This is exactly linear independence.''',
1, 10, [r'A zero polynomial relation is an identity holding at every argument.'],
['def-linear-independence', 'def-polynomial-space', 'lem-polynomial-coefficients'], '2.16(b)', 32, 'example')

s.r('ex-single-independent', 'Independence of a one-vector list', r'''A list consisting of one vector $v$ is linearly independent if and only if $v\ne0$.''',
r'''If $v=0$, then $1v=0$ is a relation with nonzero coefficient, so the list is not independent. Suppose $v\ne0$ and $av=0$. If $a\ne0$, multiplication by $a^{-1}$ gives $v=a^{-1}(av)=a^{-1}0=0$, a contradiction. Thus $a=0$, which proves independence.''',
1, 10, [r'If the coefficient in a zero relation is nonzero, multiply by its reciprocal.'],
['def-linear-independence', 'c1-def-vector-space', 'c1-def-field', 'c1-thm-scalar-zero'], '2.16(c)', 32, 'example')

s.r('ex-pair-independent', 'Independence of two vectors', r'''A list $u,v$ is linearly independent if and only if neither vector is a scalar multiple of the other.''',
r'''If $u=cv$, the relation $u-cv=0$ has coefficient $1$ on $u$, so the pair is not independent. If $v=cu$, the relation $v-cu=0$ gives the same conclusion. Conversely, suppose $au+bv=0$ with at least one coefficient nonzero. If $a\ne0$, rearranging and multiplying by $a^{-1}$ yields $u=(-b/a)v$. If $a=0$, then $b\ne0$, and multiplication by $b^{-1}$ yields $v=0=0u$. Thus every nontrivial relation makes at least one vector a scalar multiple of the other. If neither vector is such a multiple, no nontrivial relation exists, so the pair is independent.''',
2, 15, [r'Distinguish whether the first coefficient in a nontrivial relation vanishes.'],
['def-linear-independence', 'c1-def-vector-space', 'c1-def-field', 'c1-def-vector-subtraction', 'c1-thm-zero-scalar', 'c1-thm-scalar-zero', 'c1-thm-negative-one'], '2.16(d)', 32, 'example')

s.r('lem-independent-sublist', 'Deleting vectors preserves independence', r'''Every list obtained by deleting some entries of a linearly independent list is linearly independent.''',
r'''Take a relation equal to zero among the retained entries. Give coefficient zero to every deleted position. This extends the relation to the original list, because zero scalar multiples contribute zero. Independence of the original list makes every coefficient zero, including the coefficients of the retained entries. If none remain, the conclusion also follows from the empty-list convention.''',
1, 10, [r'Extend a relation on the shorter list by inserting zero coefficients.'],
['def-linear-independence', 'c1-thm-zero-scalar'], page=33, kind='lemma')

s.d('def-linear-dependence', 'Linear dependence', r'''A list is linearly dependent when it is not linearly independent. Equivalently, it admits scalars, not all zero, whose linear combination of the listed vectors equals zero. In particular, the empty list is not linearly dependent.''', '2.17', 33)

s.r('ex-dependent-parameter', 'A parameter controlling dependence', r'''The list
\[(2,3,1),\quad(1,-1,2),\quad(7,3,c)\]
in $\F^3$ is linearly dependent exactly when $c=8$. In that case the first vector multiplied by $2$, plus the second multiplied by $3$, equals the third.''',
r'''For a zero relation with coefficients $a,b,d$, the first two coordinates give $2a+b+7d=0$ and $3a-b+3d=0$. Adding gives $5a+10d=0$, hence $a=-2d$; substitution into the first equation gives $b=-3d$. The third coordinate is then
\[a+2b+cd=(c-8)d.\]
If $c\ne8$, scalar cancellation forces $d=0$, and consequently $a=b=0$. Thus the list is independent in this case. If $c=8$, coefficients $2,3,-1$ give a zero relation and are not all zero. Their relation is the stated expression for the third vector, and proves dependence.''',
2, 20, [r'Use the first two coordinates to express two coefficients in terms of the third.'],
['def-linear-dependence', 'c1-def-coordinate-addition', 'c1-def-coordinate-scaling', 'c1-lem-scalar-cancellation'], '2.18', 33, 'example')

s.r('thm-redundant-list', 'A redundant entry forces dependence', r'''If one entry of a nonempty list is in the span of the remaining entries, the list is linearly dependent. In particular, a list containing the zero vector is linearly dependent.''',
r'''Suppose $v_k=\sum_{j\ne k}b_jv_j$, where the empty sum is allowed. Subtract the right side to get a zero relation with coefficient $1$ in position $k$ and coefficient $-b_j$ in every other position. This is a nontrivial relation because $1\ne0$. If $v_k=0$, take every $b_j=0$, obtaining the required representation even if there are no other entries. The first assertion then gives dependence.''',
1, 10, [r'Move a representation of one entry to one side of an equation.'],
['def-linear-dependence', 'def-span', 'c1-def-vector-space', 'c1-thm-zero-scalar', 'c1-thm-negative-one'], '2.18', 33)

s.r('lem-linear-dependence', 'The linear dependence lemma', r'''If $v_1,\ldots,v_m$ is linearly dependent, there exists an index $k$ such that
\[v_k\in\Span(v_1,\ldots,v_{k-1}).\]
For every index $k$ satisfying this inclusion, deleting the $k$th entry leaves the span unchanged.''',
r'''Choose a nontrivial relation $\sum_{j=1}^m a_jv_j=0$. There is a largest index $k$ for which $a_k\ne0$. All terms beyond $k$ vanish, so scalar multiplication by $a_k^{-1}$ and rearrangement give
\[v_k=\sum_{j=1}^{k-1}(-a_j/a_k)v_j.\]
If $k=1$, the original relation is $a_1v_1=0$, so multiplying by $a_1^{-1}$ gives $v_1=0$; this is membership in the span of the empty list.
For the second assertion, let $k$ be any index with the stated inclusion, and let $W$ be the span after its deletion. The space $W$ contains every retained entry. It also contains $v_k$, because it contains all earlier entries and is a subspace. Thus the smallest-containing-subspace property puts the original span inside $W$. Conversely, the original span is a subspace containing every retained entry, so it contains $W$. The two spans are equal. This argument includes $k=1$, when the deleted vector is zero, and includes a one-entry list, when the retained span is $\{0\}$.''',
3, 30, [r'In a nontrivial zero relation, use the last nonzero coefficient.', r'For the deletion statement, compare the two spans by inclusion.'],
['def-linear-dependence', 'def-span', 'thm-span-smallest', 'c1-def-vector-space', 'c1-def-field', 'c1-thm-scalar-zero', 'c1-thm-negative-one'], '2.19', 33, 'lemma')

s.r('ex-first-redundancy', 'Finding the first removable entry', r'''For the ordered list
\[(1,2,3),\quad(6,5,4),\quad(15,16,17),\quad(8,9,7)\]
in $\R^3$, the smallest index $k$ for which the $k$th vector is in the span of its predecessors is $k=3$. The list is dependent, and deleting its third entry preserves its span.''',
r'''The first vector is nonzero, so it is not in the span of the empty list. If the second were a scalar multiple of the first, its first coordinate would force the scalar to be $6$, but its second coordinate would then be $12$, not $5$. Thus $k=2$ also fails. Coordinate calculation gives
\[3(1,2,3)+2(6,5,4)=(15,16,17),\]
so $k=3$ works and is the smallest such index. This representation makes the third entry redundant, hence the list dependent. The deletion conclusion of the linear dependence lemma shows that its third entry can be removed without changing the span.''',
2, 15, [r'Rule out the first two indices, then solve for a combination of the first two vectors.'],
['def-span', 'thm-redundant-list', 'lem-linear-dependence', 'c1-def-coordinate-addition', 'c1-def-coordinate-scaling'], '2.21', 34, 'example')

s.r('thm-independent-length', 'An independent list is no longer than a spanning list', r'''If $u_1,\ldots,u_m$ is linearly independent in $V$ and $w_1,\ldots,w_n$ spans $V$, then $m\le n$.''',
r'''Suppose, for a contradiction, that $m>n$. Starting with the spanning list $w_1,\ldots,w_n$, we construct for each $k$ with $0\le k\le n$ a spanning list of length $n$ consisting of $u_1,\ldots,u_k$ followed by $n-k$ retained entries from the original $w$ list. The case $k=0$ is the given list.
Suppose $k<n$ and such a list has been constructed. Insert $u_{k+1}$ immediately after $u_k$, or at the beginning if $k=0$. Because the old list spans $V$, the inserted vector is a combination of its entries, so the enlarged list is dependent. The linear dependence lemma supplies an entry in the span of its predecessors that can be deleted without changing the span. That entry cannot be among $u_1,\ldots,u_{k+1}$: otherwise the corresponding initial portion of the independent $u$ list would have a redundant entry, making it dependent, contrary to independence of sublists. Hence an entry retained from the $w$ list is deleted. This gives the required spanning list for $k+1$.
After $n$ steps, $u_1,\ldots,u_n$ spans $V$. Since $m>n$, the vector $u_{n+1}$ exists and is in this span. The list $u_1,\ldots,u_{n+1}$ therefore has a redundant entry and is dependent, contradicting independence of a sublist of the original $u$ list. If $n=0$, the same final argument applies immediately: the empty list spans $V=\{0\}$ and $u_1=0$ is redundant. The contradiction proves $m\le n$.''',
3, 45, [r'Try replacing entries of a spanning list by entries of the independent list.', r'Order the independent entries first so that the dependence lemma can only remove an old spanning entry.'],
['def-spanning-list', 'def-linear-independence', 'lem-independent-sublist', 'thm-redundant-list', 'lem-linear-dependence'], '2.22', 35)

s.r('ex-four-vectors-three-space', 'Four vectors in three coordinates are dependent', r'''Every list of four vectors in $\R^3$ is linearly dependent. In particular, this holds for
\[(1,2,3),\quad(4,5,8),\quad(9,6,7),\quad(-3,2,8).\]''',
r'''The three standard coordinate vectors span $\R^3$. The independent-length theorem therefore bounds every independent list in $\R^3$ by length three. A list of length four cannot be independent and hence is dependent. The displayed list has length four, so it is covered by this conclusion.''',
1, 10, [r'Compare the length with the standard spanning list.'],
['ex-standard-spanning', 'thm-independent-length', 'def-linear-dependence'], '2.23', 36, 'example')

s.r('ex-three-vectors-four-space', 'Three vectors cannot span four coordinates', r'''No list of three vectors spans $\R^4$. In particular,
\[(1,2,3,-5),\quad(4,5,8,3),\quad(9,6,7,-1)\]
does not span $\R^4$.''',
r'''The four standard coordinate vectors in $\R^4$ are independent. If a three-entry list spanned $\R^4$, the independent-length theorem would give $4\le3$, a contradiction. Therefore no such list spans, including the displayed one.''',
1, 10, [r'Find an independent list longer than the proposed spanning list.'],
['ex-standard-independent', 'thm-independent-length'], '2.24', 36, 'example')

s.r('thm-subspaces-finite', 'Subspaces of finite-dimensional spaces are finite-dimensional', r'''If $V$ is finite-dimensional and $U$ is a subspace of $V$, then $U$ is finite-dimensional.''',
r'''Choose a spanning list of $V$ of length $n$. Begin with the empty list in $U$, whose span is $\{0\}$. If the current list spans $U$, stop. If not, its span is a subspace contained in $U$, so there is a vector of $U$ outside that span; append one such vector. In every list obtained this way, no entry belongs to the span of its predecessors. The linear dependence lemma implies that each such list is independent, for a dependent list would have an entry with precisely that forbidden property.
If this construction did not stop by length $n$, it would produce an independent list of length $n+1$ in $V$, contradicting the independent-length theorem. Hence it stops with a list of length at most $n$ spanning $U$. This proves that $U$ is finite-dimensional. If $U=\{0\}$, it stops at the empty list. In particular, when $n=0$, $V=\{0\}$ and every subspace is $\{0\}$, so the same conclusion holds.''',
3, 30, [r'Keep choosing vectors outside the span of those already chosen.', r'Use the length bound to show this process must stop.'],
['def-finite-dimensional', 'def-span', 'thm-span-smallest', 'lem-linear-dependence', 'thm-independent-length', 'c1-def-subspace'], '2.25', 36)

s.card('span', 'def-span',
r'What is the span of a list, and what is the span of the empty list?',
r'The span is the set of all linear combinations of the list. The span of the empty list is $\{0\}$.')

s.card('span-minimal', 'thm-span-smallest',
r'What does it mean that a span is the smallest subspace containing a list?',
r'The span is itself a subspace containing the listed vectors, and it is contained in every subspace that contains them.')

s.card('finite-dimensional', 'def-finite-dimensional',
r'What does finite-dimensional mean before dimension has been defined?',
r'The vector space has a finite spanning list.')

s.card('polynomial-coefficients', 'lem-polynomial-coefficients',
r'How can coefficient uniqueness be proved without a theorem about polynomial roots?',
r'Subtract the identity at $z$ from the identity at $z+1$ and use induction on the largest exponent.')

s.card('polynomial-infinite', 'thm-polynomials-infinite',
r'Why can no finite list span all polynomial functions?',
r'Its linear combinations have a common degree bound unless the list contains only zero polynomials; a sufficiently high power lies outside its span.')

s.card('independence', 'def-linear-independence',
r'What does linear independence require?',
r'Every linear combination equal to zero must have all coefficients zero. The empty list is independent.')

s.card('dependence-lemma', 'lem-linear-dependence',
r'State the linear dependence lemma.',
r'A dependent list has an entry in the span of its predecessors. Deleting any entry with that property preserves the span.')

s.card('length-bound', 'thm-independent-length',
r'How do the lengths of an independent list and a spanning list compare?',
r'In the same vector space, the independent list has length at most the spanning list.')

s.card('subspaces-finite', 'thm-subspaces-finite',
r'Why must repeatedly choosing vectors outside the current span eventually span a subspace of a finite-dimensional space?',
r'The chosen list stays independent, and its length is bounded by the length of a fixed spanning list of the ambient space.')

s.write()
