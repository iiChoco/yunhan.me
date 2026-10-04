from common import Section

s = Section('2b')

s.p(
    'intro-bases',
    'Spanning without redundant vectors',
    r'''A spanning list supplies representations, while linear independence controls their uniqueness. A basis combines these two properties and provides a coordinate description of every vector.''',
    39
)

s.d(
    'def-basis',
    'Basis',
    r'''A finite list $v_1,\ldots,v_n$ in a vector space $V$ is a \emph{basis} of $V$ when it is linearly independent and its span is $V$. Lists of length zero are allowed, with their earlier conventions for independence and span.''',
    '2.26', 39
)

s.r(
    'ex-standard-basis',
    'The standard coordinate basis',
    r'''For $n\ge1$, let $e_j\in\F^n$ have coordinate $1$ in position $j$ and coordinate $0$ in every other position. Prove that $e_1,\ldots,e_n$ is a basis of $\F^n$, called its \emph{standard basis}. For $n=0$, prove that the empty list is a basis of $\F^0=\{()\}$.''',
    r'''For $n\ge1$, every $x=(x_1,\ldots,x_n)$ satisfies $x=x_1e_1+\cdots+x_ne_n$, so the list spans $\F^n$. If $a_1e_1+\cdots+a_ne_n=0$, comparison of coordinate $j$ gives $a_j=0$ for each $j$. Thus the list is independent and is a basis.

For $n=0$, the space consists of its single zero vector, the empty coordinate list. The empty list of vectors is independent by convention, and its span is the zero space. It is therefore a basis of $\F^0$.''',
    1, 10,
    [r'In a combination of the standard coordinate vectors, what is the $j$th coordinate?'],
    ['def-basis', 'def-span', 'def-linear-independence',
     'c1-def-coordinate-space', 'c1-def-coordinate-addition',
     'c1-def-coordinate-scaling'],
    number='2.27(a)', page=39, kind='example'
)

s.r(
    'ex-nonstandard-basis',
    'A basis with no coordinate-axis vectors',
    r'''Prove that $(1,2),(3,5)$ is a basis of $\F^2$.''',
    r'''For any $(x,y)\in\F^2$, direct coordinate calculation gives
\[
(x,y)=(3y-5x)(1,2)+(2x-y)(3,5).
\]
Indeed, the first coordinate on the right is $3y-5x+6x-3y=x$, and the second is $6y-10x+10x-5y=y$. Hence the list spans.

Suppose $a(1,2)+b(3,5)=0$. The coordinate equations are $a+3b=0$ and $2a+5b=0$. Subtracting twice the first equation from the second gives $-b=0$, so $b=0$ and then $a=0$. Thus the list is independent, proving it is a basis.''',
    2, 15,
    [
        r'Treat the coefficients in $a(1,2)+b(3,5)=(x,y)$ as unknowns.',
        r'Subtract twice the first coordinate equation from the second.'
    ],
    ['def-basis', 'def-spanning-list', 'def-linear-independence',
     'c1-def-coordinate-addition', 'c1-def-coordinate-scaling'],
    number='2.27(b)', page=39, kind='example'
)

s.r(
    'ex-independent-not-basis',
    'Independence without spanning',
    r'''Prove that $(1,2,-4),(7,-5,6)$ is linearly independent in $\F^3$ but is not a basis of $\F^3$.''',
    r'''Suppose
\[
a(1,2,-4)+b(7,-5,6)=0.
\]
The first two coordinates give $a+7b=0$ and $2a-5b=0$. Subtracting twice the first equation from the second gives $-19b=0$. Since $19\ne0$ in $\F$, this implies $b=0$, and the first equation then gives $a=0$. Thus the two-vector list is independent.

The three standard coordinate vectors are independent in $\F^3$. If the given two-vector list spanned $\F^3$, the inequality between the length of an independent list and the length of a spanning list would give $3\le2$, a contradiction. Therefore the given list does not span and is not a basis.''',
    2, 20,
    [
        r'Use the first two coordinates to check independence.',
        r'Compare the length of this list with the independent standard coordinate list.'
    ],
    ['def-basis', 'def-linear-independence', 'thm-independent-length',
     'ex-standard-basis', 'c1-lem-scalar-cancellation'],
    number='2.27(c)', page=39, kind='example'
)

s.r(
    'ex-spanning-not-basis',
    'Spanning with a redundant vector',
    r'''Prove that $(1,2),(3,5),(4,13)$ spans $\F^2$ but is not a basis of $\F^2$.''',
    r'''The first two vectors already form a basis by the preceding two-coordinate example. Every vector of $\F^2$ is therefore a combination of the first two, and becomes a combination of all three by assigning coefficient zero to the third. Thus the three-vector list spans.

However,
\[
19(1,2)-5(3,5)-(4,13)=(19-15-4,38-25-13)=(0,0).
\]
The coefficient of the third vector is $-1\ne0$, so this is a nontrivial relation. The list is dependent and hence is not a basis.''',
    2, 15,
    [
        r'The first two vectors have already been studied.',
        r'Express the third vector as a combination of the first two.'
    ],
    ['def-basis', 'ex-nonstandard-basis', 'def-spanning-list',
     'def-linear-dependence'],
    number='2.27(d)', page=39, kind='example'
)

s.r(
    'ex-equal-coordinate-basis',
    'A basis for a coordinate-equality subspace',
    r'''Prove that
\[
U=\{(x,x,y):x,y\in\F\}
\]
is a subspace of $\F^3$ and that $(1,1,0),(0,0,1)$ is a basis of $U$.''',
    r'''Every combination of the displayed vectors has the form
\[
a(1,1,0)+b(0,0,1)=(a,a,b),
\]
which lies in $U$. Conversely, every $(x,x,y)\in U$ is the combination with $a=x$ and $b=y$. Hence $U$ equals their span, so it is a subspace by the span theorem and the list spans $U$.

If $(a,a,b)=0$, the first and third coordinate equations give $a=0$ and $b=0$. The list is therefore independent and is a basis of $U$.''',
    1, 10,
    [r'Write a general combination of the two proposed basis vectors.'],
    ['def-basis', 'def-span', 'thm-span-smallest',
     'def-linear-independence', 'c1-def-coordinate-addition',
     'c1-def-coordinate-scaling'],
    number='2.27(e)', page=39, kind='example'
)

s.r(
    'ex-zero-coordinate-sum-basis',
    'A basis for a coordinate-sum subspace',
    r'''Prove that
\[
H=\{(x,y,z)\in\F^3:x+y+z=0\}
\]
is a subspace and that $(1,-1,0),(1,0,-1)$ is a basis of $H$.''',
    r'''A general combination of the proposed vectors is
\[
a(1,-1,0)+b(1,0,-1)=(a+b,-a,-b).
\]
Its coordinates sum to zero, so their span is contained in $H$. Conversely, if $(x,y,z)\in H$, then $x=-y-z$, and taking $a=-y$, $b=-z$ in the displayed formula produces $(x,y,z)$. Thus $H$ is exactly the span of the two vectors and is a subspace.

If $(a+b,-a,-b)=0$, its second coordinate gives $a=0$ and its third gives $b=0$. This proves independence, so the list is a basis of $H$.''',
    2, 15,
    [
        r'Use the second and third coordinates to determine the two coefficients.'
    ],
    ['def-basis', 'def-span', 'thm-span-smallest',
     'def-linear-independence', 'c1-def-coordinate-addition',
     'c1-def-coordinate-scaling'],
    number='2.27(f)', page=39, kind='example'
)

s.r(
    'ex-polynomial-standard-basis',
    'The standard polynomial basis',
    r'''For every nonnegative integer $m$, prove that $1,z,\ldots,z^m$ is a basis of $\Poly_m(\F)$. This list is called the \emph{standard basis} of $\Poly_m(\F)$.''',
    r'''Every polynomial in $\Poly_m(\F)$ has an expression
\[
p(z)=a_0+a_1z+\cdots+a_mz^m
\]
by the definition of degree and the bounded-degree polynomial space; missing higher coefficients are taken to be zero. Thus the monomial list spans.

If $a_0+a_1z+\cdots+a_mz^m$ is the zero polynomial, uniqueness of polynomial coefficients gives $a_0=\cdots=a_m=0$. Hence the list is independent and is a basis. When $m=0$, this argument says that the one-element list containing the constant polynomial $1$ is a basis of the constant polynomials.''',
    1, 10,
    [
        r'Use the polynomial coefficient result for the independence part.'
    ],
    ['def-basis', 'def-polynomial-space', 'def-degree',
     'lem-polynomial-coefficients', 'def-linear-independence'],
    number='2.27(g)', page=39, kind='example'
)

s.r(
    'ex-another-plane-basis',
    'Another choice of coordinates in the plane',
    r'''Prove that $(7,5),(-4,9)$ is also a basis of $\F^2$.''',
    r'''For arbitrary $(x,y)\in\F^2$, set
\[
a=\frac{9x+4y}{83},\qquad b=\frac{-5x+7y}{83}.
\]
The denominator is nonzero in $\F$. Calculation gives
\[
7a-4b=\frac{63x+28y+20x-28y}{83}=x,\qquad
5a+9b=\frac{45x+20y-45x+63y}{83}=y.
\]
Thus $a(7,5)+b(-4,9)=(x,y)$, proving that the list spans.

For independence, suppose $a(7,5)+b(-4,9)=0$. Then $7a-4b=0$ and $5a+9b=0$. Nine times the first equation plus four times the second gives $83a=0$, and negative five times the first plus seven times the second gives $83b=0$. Since $83\ne0$, both coefficients vanish. The list is a basis.''',
    2, 15,
    [
        r'Eliminate one coefficient from the two coordinate equations.',
        r'The combinations $9(7a-4b)+4(5a+9b)$ and $-5(7a-4b)+7(5a+9b)$ isolate the coefficients.'
    ],
    ['def-basis', 'def-spanning-list', 'def-linear-independence',
     'c1-lem-scalar-cancellation', 'c1-def-coordinate-addition',
     'c1-def-coordinate-scaling'],
    page=39, kind='example'
)

s.r(
    'thm-basis-coordinates',
    'Bases are exactly lists with unique coordinates',
    r'''A list $v_1,\ldots,v_n$ in $V$ is a basis of $V$ if and only if every $v\in V$ has exactly one coefficient list $(a_1,\ldots,a_n)\in\F^n$ for which
\[
v=\sum_{j=1}^{n}a_jv_j.
\]
For $n=0$, the sum and coefficient list are empty.''',
    r'''Suppose the list is a basis. Spanning gives at least one coefficient list for each $v$. If
\[
v=\sum_{j=1}^{n}a_jv_j=\sum_{j=1}^{n}b_jv_j,
\]
subtracting the two expressions using distributivity gives
\[
0=\sum_{j=1}^{n}(a_j-b_j)v_j.
\]
Independence forces $a_j-b_j=0$ for every $j$, so the two coefficient lists are equal. Hence the coefficients are unique.

Conversely, suppose every vector has exactly one coefficient list. Existence of these lists means that the given vectors span $V$. If $\sum_{j=1}^{n}a_jv_j=0$, compare this with the representation of zero having every coefficient zero. Uniqueness gives $a_j=0$ for every $j$, proving independence. Thus the list is a basis.

If $n=0$, the empty sum has value zero and there is precisely one empty coefficient list. The unique-coordinate condition therefore holds exactly when $V=\{0\}$. This agrees with the definition: the empty list is independent and spans precisely the zero space.''',
    2, 20,
    [
        r'Spanning supplies existence; which property controls two different coefficient lists?',
        r'Subtract two representations. For the reverse implication, apply uniqueness to the zero vector.'
    ],
    ['def-basis', 'def-span', 'def-spanning-list',
     'def-linear-independence', 'c1-def-vector-space',
     'c1-def-vector-subtraction', 'c1-thm-zero-scalar'],
    number='2.28', page=39
)

s.p(
    'intro-basis-constructions',
    'Removing and adding vectors',
    r'''A spanning list can contain unnecessary vectors, while an independent list can leave some vectors unrepresented. We next give finite procedures that remove the first problem or repair the second.''',
    40
)

s.r(
    'ex-delete-redundant-vectors',
    'Removing two redundant entries',
    r'''For the list
\[
(1,2),\ (3,6),\ (4,7),\ (5,9)
\]
in $\F^2$, prove that deleting its second and fourth entries preserves its span and leaves a basis of $\F^2$.''',
    r'''Write $u=(1,2)$ and $w=(4,7)$. The deleted vectors satisfy $(3,6)=3u$ and $(5,9)=u+w$. Thus every combination of the original four vectors can be rewritten as a combination of $u,w$. Conversely, each of $u,w$ is among the original vectors, so every combination of $u,w$ is a combination of that original list. The two spans are equal.

For arbitrary $(x,y)\in\F^2$,
\[
(x,y)=(4y-7x)u+(2x-y)w.
\]
The first coordinate on the right is $4y-7x+8x-4y=x$, and the second is $8y-14x+14x-7y=y$. Thus the remaining list spans $\F^2$.

If $au+bw=0$, the equations $a+4b=0$ and $2a+7b=0$ give $-b=0$ on subtracting twice the first from the second. Hence $b=0$ and $a=0$. The remaining list is independent and therefore is a basis.''',
    2, 20,
    [
        r'Express each deleted vector using the retained ones.',
        r'For the retained pair, solve the two coordinate equations.'
    ],
    ['def-basis', 'def-span', 'def-linear-independence',
     'c1-def-coordinate-addition', 'c1-def-coordinate-scaling'],
    page=40, kind='example'
)

s.r(
    'thm-reduce-spanning',
    'Reducing a spanning list to a basis',
    r'''Every finite list that spans a vector space contains a sublist, in the original order, that is a basis of the space. One may construct it by scanning the list from left to right and retaining a vector exactly when it is outside the span of the vectors already retained.''',
    r'''Let $v_1,\ldots,v_n$ span $V$. Begin with the empty retained list $B_0$. For $k=1,\ldots,n$, leave the retained list unchanged if $v_k\in\Span(B_{k-1})$; otherwise append $v_k$, producing $B_k$.

We prove by induction on $k$ that $B_k$ is independent and
\[
\Span(B_k)=\Span(v_1,\ldots,v_k).
\]
At $k=0$, both spans are $\{0\}$ and the empty list is independent.

Assume the assertions at $k-1$. If $v_k$ is omitted, then it already belongs to $\Span(B_{k-1})$. Every combination of the first $k$ original vectors consequently belongs to that subspace. The reverse inclusion holds because all entries of $B_{k-1}$ occur among the first $k$ original vectors. This proves span equality, and independence is unchanged.

If $v_k$ is appended, the previous span equality shows that combinations of the retained vectors together with $v_k$ give exactly the combinations of the first $k$ original vectors: rewrite any combination of the first $k-1$ vectors using $B_{k-1}$, and conversely use the fact that the retained entries are original entries. Thus span equality again holds. To check independence, write the previous retained list as $b_1,\ldots,b_r$ and suppose
\[
a_1b_1+\cdots+a_rb_r+cv_k=0.
\]
If $c\ne0$, multiplication by $c^{-1}$ and rearrangement give
\[
v_k=-c^{-1}(a_1b_1+\cdots+a_rb_r)\in\Span(B_{k-1}),
\]
contrary to the rule for appending $v_k$. Hence $c=0$, and independence of $B_{k-1}$ forces every $a_j=0$. This completes the induction.

At $k=n$, the retained list is independent and spans $V$, so it is a basis. The procedure takes only $n$ steps and keeps the original order. If $n=0$, the original list spans only the zero space, and the unchanged empty list is already its basis.''',
    3, 35,
    [
        r'Keep a vector only if the previously retained vectors cannot represent it.',
        r'Prove after each step that the retained list is independent and has the same span as the part already scanned.',
        r'In a dependence relation involving an appended vector, a nonzero coefficient for that vector would express it using the previous ones.'
    ],
    ['def-basis', 'def-span', 'thm-span-smallest',
     'def-linear-independence', 'c1-def-vector-space',
     'c1-thm-negative-one', 'c1-thm-complex-inverses'],
    number='2.30', page=40
)

s.r(
    'thm-basis-existence',
    'Existence of a basis in finite-dimensional spaces',
    r'''Every finite-dimensional vector space has a basis.''',
    r'''By the definition of finite-dimensionality, the space has a finite spanning list. The spanning-list reduction theorem provides a sublist that is a basis. For the zero space, the spanning list may be empty, and the reduction theorem includes that case.''',
    1, 10,
    [
        r'Use the definition of finite-dimensionality, then apply the preceding construction.'
    ],
    ['def-finite-dimensional', 'thm-reduce-spanning'],
    number='2.31', page=41, kind='corollary'
)

s.r(
    'thm-extend-independent',
    'Extending an independent list to a basis',
    r'''Every linearly independent finite list in a finite-dimensional vector space can be extended to a basis, preserving the original list as the initial part of the resulting basis.''',
    r'''Let $u_1,\ldots,u_m$ be independent in $V$. Choose a finite spanning list $w_1,\ldots,w_n$ for $V$. The concatenated list
\[
u_1,\ldots,u_m,w_1,\ldots,w_n
\]
spans $V$, since it contains the spanning list $w_1,\ldots,w_n$.

Apply the left-to-right retention procedure from the spanning-list reduction theorem to this concatenated list. None of the $u$ entries is omitted. Indeed, suppose the procedure reaches $u_k$ with $u_1,\ldots,u_{k-1}$ retained. If $u_k$ belonged to their span, a representation
$u_k=\sum_{j<k}a_ju_j$ would give a relation on the original independent list with coefficient $1$ at $u_k$, coefficients $-a_j$ at earlier entries, and coefficients zero at later entries. This is impossible. The argument also covers $k=1$, because the preceding span is then $\{0\}$.

The reduction theorem guarantees that the final retained list is a basis. It begins with all the $u$ entries, in order, followed by some of the $w$ entries, as required. If the original independent list is empty, there are no initial entries to protect, and the same procedure supplies a basis. If it already spans $V$, every $w$ entry is omitted and no extension is needed.''',
    2, 20,
    [
        r'Append a spanning list to the independent list.',
        r'Use the preceding deletion procedure, and explain why it cannot discard any entry of the independent initial list.'
    ],
    ['def-finite-dimensional', 'def-span', 'def-linear-independence',
     'thm-reduce-spanning'],
    number='2.32', page=41
)

s.r(
    'ex-explicit-basis-extension',
    'An explicit extension in three-coordinate space',
    r'''Prove that
\[
(2,3,4),\ (9,6,8),\ (0,1,0)
\]
is a basis of $\F^3$, extending the first two vectors. Also show that the extension procedure which scans the standard coordinate vectors after those first two vectors skips $(1,0,0)$ and retains $(0,1,0)$.''',
    r'''Write $u=(2,3,4)$, $v=(9,6,8)$, and $e_2=(0,1,0)$. Suppose
\[
au+bv+ce_2=0.
\]
The third coordinate gives $4a+8b=0$, hence $a=-2b$. The first coordinate then gives $2(-2b)+9b=5b=0$, so $b=0$ and $a=0$. The second coordinate now gives $c=0$. Thus the three-vector list is independent; taking $c=0$ also proves independence of its first two vectors.

For any $(x,y,z)\in\F^3$, put
\[
a=\frac{9z-8x}{20},\qquad
b=\frac{2x-z}{10},\qquad
c=y-\frac{3z}{4}.
\]
The nonzero denominators are invertible in $\F$. These choices satisfy
\[
2a+9b=x,\qquad 4a+8b=z,
\]
as is seen by combining the respective numerators:
$9z-8x+18x-9z=10x$ over denominator $10$, and
$9z-8x+8x-4z=5z$ over denominator $5$.
Also $a+2b=z/4$, so
$3a+6b+c=3z/4+y-3z/4=y$.
Thus $au+bv+ce_2=(x,y,z)$. The list spans and is a basis.

For the specified procedure, the initial two vectors are retained because they are independent. The first standard vector satisfies
\[
(1,0,0)=-\frac25u+\frac15v,
\]
so it is skipped. If $e_2=au+bv$, then $au+bv-e_2=0$ would contradict the independence just proved, because the coefficient of $e_2$ would be $-1$. Thus $e_2$ is retained. The resulting list already spans $\F^3$, so the final standard vector is skipped.''',
    3, 30,
    [
        r'Use the first and third coordinate equations to solve for the coefficients of the first two vectors.',
        r'The new vector changes only the second coordinate.',
        r'To understand the scanning procedure, express $(1,0,0)$ using the first two vectors.'
    ],
    ['def-basis', 'def-linear-independence', 'def-span',
     'thm-reduce-spanning', 'thm-extend-independent',
     'c1-def-coordinate-addition', 'c1-def-coordinate-scaling',
     'c1-lem-scalar-cancellation'],
    page=41, kind='example'
)

s.p(
    'intro-subspace-complements',
    'Completing a subspace to the whole space',
    r'''A basis extension can be divided into the original basis and the newly added vectors. Their two spans give a decomposition in which each vector has exactly one component in each subspace.''',
    41
)

s.r(
    'thm-subspace-complement',
    'Every subspace has a complement in finite dimensions',
    r'''If $V$ is finite-dimensional and $U$ is a subspace of $V$, then there is a subspace $W$ of $V$ such that $V=U\oplus W$.''',
    r'''The theorem on subspaces of finite-dimensional spaces implies that $U$ is finite-dimensional. Choose a basis $u_1,\ldots,u_m$ of $U$ using basis existence. The list is also independent when regarded as a list in $V$, because a relation among its entries uses the same operations and the same zero vector in the subspace and ambient space. Extend it to a basis
\[
u_1,\ldots,u_m,w_1,\ldots,w_n
\]
of $V$. Define $W=\Span(w_1,\ldots,w_n)$, which is a subspace by the span theorem.

Every $v\in V$ is a combination of this extended basis. Grouping its coefficients gives
\[
v=\left(\sum_{j=1}^{m}a_ju_j\right)
  +\left(\sum_{k=1}^{n}b_kw_k\right).
\]
The first parenthesis is in $U$, and the second is in $W$, so $V\subseteq U+W$. Conversely, the sum of a vector in $U$ and a vector in $W$ belongs to $V$, because both subspaces are contained in $V$ and $V$ is closed under addition. Hence $V=U+W$.

If $x\in U\cap W$, write
\[
x=\sum_{j=1}^{m}a_ju_j=\sum_{k=1}^{n}b_kw_k.
\]
Subtraction yields a relation on the extended basis with coefficients $a_j$ and $-b_k$. Independence forces all these coefficients to be zero, and thus $x=0$. Both subspaces contain zero, so $U\cap W=\{0\}$. The two-subspace direct-sum criterion gives $V=U\oplus W$.

All steps allow empty lists: their sums are zero and their spans are $\{0\}$. In particular the argument covers $U=\{0\}$, $U=V$, and $V=\{0\}$.''',
    3, 35,
    [
        r'Choose a basis of $U$ and extend it to a basis of $V$.',
        r'Take the span of the newly added vectors.',
        r'A vector lying in both spans would produce a relation on the extended basis.'
    ],
    ['thm-subspaces-finite', 'thm-basis-existence', 'def-basis',
     'thm-extend-independent', 'def-span', 'thm-span-smallest',
     'def-linear-independence', 'c1-def-subspace',
     'c1-def-subspace-sum', 'c1-thm-direct-intersection',
     'c1-def-vector-subtraction'],
    number='2.33', page=42
)

s.card(
    'basis-definition',
    'def-basis',
    r'What two conditions define a basis of a vector space?',
    r'The list must be linearly independent and span the entire space.'
)

s.card(
    'basis-empty',
    'thm-basis-coordinates',
    r'For which vector space is the empty list a basis?',
    r'Exactly the zero space: the empty list is independent and its span is $\{0\}$.'
)

s.card(
    'basis-unique-coordinates',
    'thm-basis-coordinates',
    r'How can the basis property be stated using coefficients of vectors?',
    r'Every vector must have exactly one coefficient list expressing it as a combination of the proposed basis vectors.'
)

s.card(
    'basis-polynomials',
    'ex-polynomial-standard-basis',
    r'What is the standard basis of $\Poly_m(\F)$ for $m\ge0$?',
    r'The list $1,z,\ldots,z^m$.'
)

s.card(
    'basis-reduction-rule',
    'thm-reduce-spanning',
    r'In the left-to-right basis-reduction procedure, when is an entry retained?',
    r'Exactly when it is outside the span of the entries already retained.'
)

s.card(
    'basis-existence',
    'thm-basis-existence',
    r'Why does every finite-dimensional vector space have a basis?',
    r'It has a finite spanning list, and such a list can be reduced to a basis.'
)

s.card(
    'basis-extension',
    'thm-extend-independent',
    r'Why does the basis-extension construction preserve a prescribed independent initial list?',
    r'No vector in that initial list is in the span of its predecessors; otherwise it would yield a nontrivial relation on the independent list.'
)

s.card(
    'basis-complement',
    'thm-subspace-complement',
    r'How does extending a basis of a subspace produce a direct-sum complement?',
    r'Take the span of the newly added basis vectors. The full basis supplies the sum, and its independence forces the two spans to intersect only at zero.'
)

s.write()
