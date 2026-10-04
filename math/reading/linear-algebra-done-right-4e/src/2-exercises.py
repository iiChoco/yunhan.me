from common import Section

s = Section('2-exercises')

s.p(
    'intro-exercises',
    'Exercises on spanning, bases, and dimension',
    r'''These optional exercises develop the chapter's methods through explicit constructions and dimension arguments. They range from finding a basis to arranging complements for two subspaces at once. Each exercise can be solved using the required material of Chapters 1 and 2, without relying on another exercise.''',
)

s.r(
    'ex-coordinate-constraints',
    'A basis from two coordinate constraints',
    r'''Let
\[U=\{(x_1,x_2,x_3,x_4)\in\F^4:x_1+2x_2-x_4=0,\ x_3=x_2\}.\]
Prove that $U$ is a subspace, find a basis, and compute its dimension.''',
    r'''The zero vector satisfies both equations. Adding two solutions preserves each equation, and multiplying a solution by any scalar preserves each equation. Thus the subspace test applies. Put $a=x_2$ and $b=x_4$. The equations then give $x_1=-2a+b$ and $x_3=a$, so every vector of $U$ has the form
\[a(-2,1,1,0)+b(1,0,0,1).\]
Both displayed vectors satisfy the equations, so they span $U$. If their linear combination with coefficients $a,b$ is zero, its second coordinate gives $a=0$ and its fourth gives $b=0$. The list is therefore independent and is a basis. Consequently $\dim U=2$.''',
    2,
    20,
    [r'Choose two coordinates freely and express the remaining coordinates in terms of them.'],
    ['c1-thm-subspace-test', 'def-basis', 'def-dimension', 'def-linear-independence'],
    kind='exercise',
    optional=True,
)

s.r(
    'ex-neighbor-basis',
    'Changing each vector by its predecessor',
    r'''Suppose $v_1,\ldots,v_n$ is a basis of $V$, where $n\ge1$. Define $w_1=v_1$ and $w_j=v_j+2v_{j-1}$ for $2\le j\le n$. Prove that $w_1,\ldots,w_n$ is also a basis.''',
    r'''Suppose $\sum_{j=1}^n a_jw_j=0$. If any coefficient is nonzero, let $k$ be its largest nonzero index. On expanding this relation in the $v$ basis, the coefficient of $v_k$ is $a_k$: only $w_k$ and possibly $w_{k+1}$ can contribute to that position, and the coefficient of $w_{k+1}$ is zero if it exists. Independence of the $v$ basis would give $a_k=0$, a contradiction. Thus every $a_j=0$, proving independence of the $w$ list. Its length is $n=\dim V$, so the full-length independence theorem makes it a basis. The argument includes $n=1$, when the two lists agree.''',
    2,
    20,
    [r'In a proposed dependence relation, consider the largest index with a nonzero coefficient.'],
    ['def-basis', 'def-linear-independence', 'def-dimension', 'thm-full-length-independent'],
    kind='exercise',
    optional=True,
)

s.r(
    'ex-exact-deletions',
    'Exactly how many spanning entries can be deleted?',
    r'''Let $\dim V=d$, and suppose a list of length $m$ spans $V$. Prove that one can delete exactly $m-d$ entries and leave a basis. Prove also that deleting more than $m-d$ entries cannot leave a spanning list.''',
    r'''The spanning-list reduction theorem permits deleting entries until the retained list is a basis. Every basis of $V$ has length $d$, so this deletes exactly $m-d$ entries; in particular $m\ge d$. If more entries were deleted, the retained list would have length less than $d$. A basis of $V$ is an independent list of length $d$, and the independent-length theorem rules out any spanning list shorter than it. Thus such a shorter retained list cannot span. For $d=0$, reduction leaves the empty basis and deletes all $m$ entries, while deleting more than $m$ entries is impossible.''',
    2,
    15,
    [r'Combine reduction of a spanning list with the common length of all bases.'],
    ['thm-reduce-spanning', 'thm-basis-length', 'def-dimension', 'thm-independent-length'],
    kind='exercise',
    optional=True,
)

s.r(
    'ex-real-complex-dimension',
    'Changing the permitted scalars changes dimension',
    r'''Using the usual operations, prove that $1+i,\ 2-i$ is a basis of $\C$ considered as a real vector space. Prove that this same list is dependent when complex scalars are permitted, and compute the dimension of $\C$ over each scalar field.''',
    r'''The complex vector space axioms remain valid when the permitted scalars are restricted to $\R$, because real sums and products are the same operations inside $\C$. For real $a,b$,
\[a(1+i)+b(2-i)=(a+2b)+(a-b)i.\]
Given $x+yi\in\C$, take $b=(x-y)/3$ and $a=(x+2y)/3$ to obtain this number. Thus the list spans over $\R$. If its combination is zero, the equations $a+2b=0$ and $a-b=0$ give $a=b=0$, so the list is independent over $\R$. It is a real basis, and the real dimension is $2$. With complex coefficients,
\[(2-i)(1+i)-(1+i)(2-i)=0\]
is a relation with nonzero coefficients, so the two-vector list is dependent. The one-vector list consisting of $1$ spans $\C$ over $\C$ and is independent because $a1=0$ implies $a=0$. Hence the complex dimension is $1$.''',
    2,
    20,
    [r'For real coefficients, compare real and imaginary parts.', r'For complex coefficients, use commutativity of multiplication to obtain a relation.'],
    ['c1-def-complex', 'c1-thm-complex-laws', 'c1-def-real-complex-space', 'def-basis', 'def-dimension', 'def-linear-dependence'],
    kind='exercise',
    optional=True,
)

s.r(
    'ex-finite-support',
    'Sequences with only finitely many nonzero entries',
    r'''Let $E$ be the subset of $\F^\infty$ consisting of sequences with only finitely many nonzero entries. Prove that $E$ is an infinite-dimensional subspace of $\F^\infty$.''',
    r'''The zero sequence belongs to $E$. The nonzero entries of the sum of two members can occur only among the indices where at least one summand has a nonzero entry. This is a finite set of indices. Scalar multiplication introduces no new nonzero entries. Thus the subspace test makes $E$ a subspace.
For each positive integer $j$, let $e_j$ be the sequence with entry $1$ in position $j$ and entry $0$ elsewhere. Each $e_j$ belongs to $E$. For every positive integer $r$, a relation $\sum_{j=1}^r a_je_j=0$ gives $a_k=0$ by inspecting position $k$, for each $1\le k\le r$. Thus $e_1,\ldots,e_r$ is independent. If a list of length $m$ spanned $E$, the independent list $e_1,\ldots,e_{m+1}$ would violate the independent-length theorem. No finite list spans $E$, so it is infinite-dimensional.''',
    2,
    20,
    [r'Use sequences supported at a single index to build arbitrarily long independent lists.'],
    ['c1-def-sequences', 'c1-ex-sequence-space', 'c1-thm-subspace-test', 'def-linear-independence', 'thm-independent-length', 'def-infinite-dimensional'],
    kind='exercise',
    optional=True,
)

s.r(
    'ex-polynomial-equal-values',
    'A polynomial subspace defined by equal values',
    r'''Let
\[U=\{p\in\Poly_5(\F):p(1)=p(-1)\}.\]
Prove that $1,z^2,z^4,z^3-z,z^5-z$ is a basis of $U$ and determine $\dim U$.''',
    r'''The zero polynomial satisfies the condition, and pointwise addition and scalar multiplication preserve it. Hence $U$ is a subspace of $\Poly_5(\F)$. Write $p(z)=\sum_{j=0}^5a_jz^j$. Evaluation gives
\[p(1)-p(-1)=2(a_1+a_3+a_5).\]
Because $2\ne0$ in $\F$, membership in $U$ is equivalent to $a_1=-a_3-a_5$. Therefore every member of $U$ has the representation
\[p=a_0+a_2z^2+a_4z^4+a_3(z^3-z)+a_5(z^5-z).\]
Every displayed generator satisfies the required equality of values, so the list spans $U$. In a zero relation on this list, coefficient uniqueness applied to powers $z^5,z^4,z^3,z^2,z^0$ makes the respective coefficients of the five generators zero. The list is independent, hence a basis, and $\dim U=5$.''',
    2,
    20,
    [r'Express the condition using the odd-power coefficients.'],
    ['def-polynomial-space', 'lem-polynomial-coefficients', 'thm-bounded-polynomials', 'c1-thm-subspace-test', 'def-basis', 'def-dimension'],
    kind='exercise',
    optional=True,
)

s.r(
    'ex-dimension-does-not-imply-inclusion',
    'What dimension alone does not imply',
    r'''Give subspaces $U,W$ of $\F^3$ such that $\dim U=\dim W$, but neither contains the other. Require also that $U+W=\F^3$ and that this sum is not direct. Justify every assertion.''',
    r'''Let $e_1,e_2,e_3$ be the standard coordinate vectors and set
\[U=\Span(e_1,e_2),\qquad W=\Span(e_1,e_3).\]
Spans are subspaces. Each displayed spanning list is independent by inspection of coordinates, so both subspaces have dimension $2$. The vector $e_2$ is in $U$ but not in $W$, because vectors in $W$ have second coordinate zero. Similarly, $e_3$ is in $W$ but not in $U$. The sum contains all three standard coordinate vectors and therefore equals $\F^3$. Finally, $e_1\ne0$ belongs to $U\cap W$, so the criterion for a direct sum of two subspaces shows that the sum is not direct.''',
    2,
    20,
    [r'Use two distinct coordinate planes sharing one coordinate axis.'],
    ['thm-span-smallest', 'ex-standard-spanning', 'ex-standard-independent', 'def-basis', 'def-dimension', 'c1-thm-direct-intersection'],
    kind='exercise',
    optional=True,
)

s.r(
    'ex-basis-replacement',
    'Replacing one basis vector',
    r'''Let $v_1,\ldots,v_n$ be a basis of $V$, let $1\le k\le n$, and write $w=\sum_{j=1}^n a_jv_j$. Prove that replacing $v_k$ by $w$ gives a basis exactly when $a_k\ne0$.''',
    r'''Suppose first that $a_k\ne0$. A relation on the replacement list can be written
\[bw+\sum_{j\ne k}b_jv_j=0.\]
After substituting the representation of $w$, the coefficient of $v_k$ is $ba_k$. Independence of the original basis and scalar cancellation give $b=0$. The remaining relation on the $v_j$ then gives all $b_j=0$. Thus the replacement list is independent and has length $n=\dim V$, so it is a basis.
If $a_k=0$, every entry of the replacement list lies in the span of the original basis vectors other than $v_k$. This span does not contain $v_k$, because a representation of $v_k$ by those vectors would produce a nontrivial relation on the original basis. The replacement list consequently cannot span $V$, so it is not a basis.''',
    2,
    20,
    [r'Inspect the coefficient of the basis vector that was removed.'],
    ['def-basis', 'thm-basis-coordinates', 'thm-full-length-independent', 'thm-span-smallest', 'c1-lem-scalar-cancellation'],
    kind='exercise',
    optional=True,
)

s.r(
    'ex-extension-from-specified-list',
    'Extending an independent list using prescribed vectors',
    r'''Suppose $u_1,\ldots,u_r$ is independent in $V$ and $w_1,\ldots,w_m$ spans $V$. Prove that a basis of $V$ can be obtained by appending some entries of the given $w$ list to the entire $u$ list, without deleting any $u_j$.''',
    r'''Begin with the independent $u$ list, and inspect $w_1,\ldots,w_m$ in their given order. If the current $w_j$ belongs to the span of the retained list, do not append it. Otherwise append it. Appending a vector outside the existing span preserves independence: in a zero relation involving it, a nonzero coefficient on the new vector would express that vector using the earlier ones; hence that coefficient is zero, after which independence of the old list makes all other coefficients zero.
At the end, every $w_j$ belongs to the span of the retained list. An appended entry belongs to it directly. An entry not appended belonged to the span at its inspection time, and that earlier span is contained in the final span. Since the $w$ list spans $V$, the final retained list spans $V$. It remains independent by the construction, so it is a basis. Empty lists cause no exception: if the original spanning list is empty, $V=\{0\}$ and the independent $u$ list must also be empty.''',
    3,
    35,
    [r'Inspect the prescribed spanning vectors one at a time and retain only those that enlarge the span.'],
    ['def-linear-independence', 'def-spanning-list', 'thm-span-smallest', 'thm-independent-length', 'def-basis', 'c1-def-field'],
    kind='exercise',
    optional=True,
)

s.r(
    'ex-interpolation-basis',
    'A basis adapted to prescribed values',
    r'''Let $n\ge1$ and let $t_1,\ldots,t_n$ be distinct elements of $\F$. For $1\le j\le n$, define
\[L_j(z)=\prod_{\substack{1\le k\le n\\k\ne j}}\frac{z-t_k}{t_j-t_k},\]
with an empty product equal to $1$. Prove that $L_1,\ldots,L_n$ is a basis of $\Poly_{n-1}(\F)$. Deduce that, for arbitrary scalars $b_1,\ldots,b_n$, exactly one polynomial $p\in\Poly_{n-1}(\F)$ satisfies $p(t_j)=b_j$ for all $j$, and give its formula.''',
    r'''Distinctness of the $t_j$ makes every denominator nonzero. Expanding the product by scalar distributivity gives a polynomial representation involving powers at most $n-1$, because there are $n-1$ linear factors. Hence every $L_j$ belongs to $\Poly_{n-1}(\F)$. At $z=t_j$, each factor equals $1$, so $L_j(t_j)=1$. If $i\ne j$, the factor indexed by $k=i$ gives $L_j(t_i)=0$.
Suppose $\sum_{j=1}^n a_jL_j=0$. Evaluating at $t_i$ gives $a_i=0$ for every $i$, proving independence. The space $\Poly_{n-1}(\F)$ has dimension $n$, so these $n$ independent polynomials form a basis. The polynomial
\[p=\sum_{j=1}^n b_jL_j\]
has the requested values. For uniqueness, expand any other candidate $q$ in the same basis, say $q=\sum c_jL_j$. Evaluating at $t_i$ forces $c_i=b_i$ for every $i$, so $q=p$. When $n=1$, the sole polynomial $L_1=1$ gives the same argument with empty products.''',
    3,
    45,
    [r'Evaluate each proposed basis function at each specified scalar.', r'Use the dimension of the bounded-degree polynomial space after proving independence.'],
    ['def-polynomial-space', 'lem-polynomial-coefficients', 'ex-polynomial-dimension', 'thm-full-length-independent', 'thm-basis-coordinates', 'c1-def-field'],
    kind='exercise',
    optional=True,
)

s.r(
    'ex-intersection-bound-sharp',
    'The smallest possible intersection dimension',
    r'''Suppose $\dim V=n$ and $U,W$ are subspaces with dimensions $r,s$. Prove
\[\dim(U\cap W)\ge\max(0,r+s-n).\]
For every pair of integers $0\le r,s\le n$, construct subspaces of $\F^n$ of those dimensions for which equality holds.''',
    r'''The dimension formula gives
\[\dim(U\cap W)=r+s-\dim(U+W)\ge r+s-n,\]
because $U+W$ is a subspace of $V$. Dimensions are nonnegative, giving the other lower bound.
For sharpness, let $e_1,\ldots,e_n$ be the standard basis and set
\[U=\Span(e_1,\ldots,e_r),\qquad
W=\Span(e_{n-s+1},\ldots,e_n),\]
interpreting a list as empty when its intended length is zero. Each generating list is independent, so these spaces have dimensions $r,s$. A vector in $U$ can have nonzero coordinates only in positions $1,\ldots,r$, and one in $W$ can have nonzero coordinates only in positions $n-s+1,\ldots,n$. Thus the intersection consists exactly of the vectors supported in both index sets. If $r+s\le n$, there are no such indices, and the intersection is $\{0\}$. If $r+s>n$, the common indices are $n-s+1,\ldots,r$, numbering $r+s-n$; their standard coordinate vectors form a basis of the intersection. This also covers $n=0$ with empty lists.''',
    3,
    30,
    [r'Use the dimension formula for the lower bound.', r'To attain it, place one coordinate subspace at the start and the other at the end of the coordinate list.'],
    ['thm-dimension-sum', 'thm-subspace-dimension', 'ex-standard-independent', 'def-basis', 'def-dimension', 'lem-zero-dimension'],
    kind='exercise',
    optional=True,
)

s.r(
    'ex-nested-adapted-basis',
    'A basis adapted to a chain of subspaces',
    r'''Suppose $U\subseteq W\subseteq V$ are subspaces and $V$ is finite-dimensional. Put $\dim U=r$, $\dim W=s$, and $\dim V=n$. Prove that $V$ has a basis $v_1,\ldots,v_n$ whose first $r$ entries form a basis of $U$ and whose first $s$ entries form a basis of $W$. Deduce decompositions
\[W=U\oplus A,\qquad V=U\oplus A\oplus B\]
with $\dim A=s-r$ and $\dim B=n-s$.''',
    r'''Subspaces of $V$ are finite-dimensional. Choose a basis $v_1,\ldots,v_r$ of $U$. Its independence is the same when its vectors are viewed in $W$, because all vector operations are inherited. Extend it to a basis $v_1,\ldots,v_s$ of $W$, and then extend that list to a basis $v_1,\ldots,v_n$ of $V$.
Set $A=\Span(v_{r+1},\ldots,v_s)$ and $B=\Span(v_{s+1},\ldots,v_n)$. The respective generating lists are independent sublists of a basis, so they are bases of $A$ and $B$, giving the asserted dimensions. Grouping a basis expansion shows that $W=U+A$ and $V=U+A+B$. If $u+a+b=0$ with $u\in U$, $a\in A$, and $b\in B$, expand these three vectors in their disjoint portions of the chosen basis. Independence makes all coefficients zero, so $u=a=b=0$. The direct-sum criterion proves the second decomposition, and the same argument with $b=0$ proves the first. If two dimensions coincide, the corresponding portion of the list is empty and its span is $\{0\}$, so the argument still applies.''',
    3,
    35,
    [r'Extend bases in two stages, following the inclusions.'],
    ['thm-subspaces-finite', 'thm-basis-existence', 'thm-extend-independent', 'lem-independent-sublist', 'def-basis', 'def-dimension', 'c1-thm-direct-zero'],
    kind='exercise',
    optional=True,
)

s.r(
    'ex-many-complements',
    'A family of different complements',
    r'''Suppose $V$ is finite-dimensional and $U$ is a nonzero proper subspace. Prove that there are infinitely many distinct subspaces $C$ such that $V=U\oplus C$. Give an explicit family indexed by scalars.''',
    r'''Choose a complement $W$ with $V=U\oplus W$. Because $U\ne\{0\}$, choose $u\in U$ with $u\ne0$. Because $U\ne V$, the complement $W$ is nonzero; choose a basis $w_1,\ldots,w_m$ of $W$, with $m\ge1$. For $t\in\F$, define
\[C_t=\Span(w_1+tu,w_2,\ldots,w_m).\]
For a vector $v=u_0+\sum_{j=1}^m b_jw_j$ in $V$, rewrite it as
\[v=(u_0-b_1tu)+\left(b_1(w_1+tu)+\sum_{j=2}^m b_jw_j\right).\]
This proves $V=U+C_t$. If $c=b_1(w_1+tu)+\sum_{j=2}^m b_jw_j$ lies in $U$, then $\sum b_jw_j=c-b_1tu$ lies in $U\cap W=\{0\}$. Independence of the $w$ basis gives every $b_j=0$, hence $c=0$. Therefore $V=U\oplus C_t$.
If $C_t=C_q$, subtracting the two vectors $w_1+tu$ and $w_1+qu$ in this common subspace gives $(t-q)u\in C_t\cap U=\{0\}$. Since $u\ne0$, a nonzero scalar cannot annihilate it, so $t=q$. Thus the subspaces are pairwise distinct. The scalar field contains infinitely many real integers, giving infinitely many complements.''',
    3,
    45,
    [r'Fix one complement and alter one of its basis vectors by a scalar multiple of a nonzero vector of $U$.'],
    ['thm-subspace-complement', 'thm-basis-existence', 'thm-subspaces-finite', 'c1-thm-direct-intersection', 'ex-single-independent', 'c1-foundations'],
    kind='exercise',
    optional=True,
)

s.r(
    'ex-basis-outside-subspace',
    'A basis with every vector outside a prescribed subspace',
    r'''If $U$ is a proper subspace of a finite-dimensional vector space $V$, prove that $V$ has a basis none of whose vectors belongs to $U$.''',
    r'''Choose a complement $W$ so that $V=U\oplus W$. The space $W$ is nonzero because $U\ne V$. Let $u_1,\ldots,u_r$ be a basis of $U$ and $w_1,\ldots,w_m$ a basis of $W$, where $m\ge1$. Consider
\[u_1+w_1,\ldots,u_r+w_1,\ w_1,\ldots,w_m.\]
Every $w_j$ is outside $U$, since it is nonzero and $U\cap W=\{0\}$. Each $u_i+w_1$ is also outside $U$: otherwise subtracting $u_i$ would put $w_1$ in $U$.
The list spans $V$ because it contains every $w_j$ in its span and also contains $u_i=(u_i+w_1)-w_1$ in its span. To check independence, suppose
\[\sum_{i=1}^r a_i(u_i+w_1)+\sum_{j=1}^m b_jw_j=0.\]
Its $U$ part is $\sum a_iu_i$, while its $W$ part is $(\sum a_i+b_1)w_1+\sum_{j=2}^m b_jw_j$. Directness makes both parts zero. The basis of $U$ gives all $a_i=0$, and the basis of $W$ then gives all $b_j=0$. Thus the displayed list is a basis. When $U=\{0\}$, the $u$ list is empty and the construction reduces to a basis of $V$.''',
    3,
    35,
    [r'Choose a complement and add one fixed nonzero complementary vector to each vector of a basis of $U$.'],
    ['thm-subspace-complement', 'thm-subspaces-finite', 'thm-basis-existence', 'def-basis', 'c1-thm-direct-zero', 'c1-thm-direct-intersection'],
    kind='exercise',
    optional=True,
)

s.r(
    'ex-common-complement',
    'A common complement for two subspaces',
    r'''Let $V$ be finite-dimensional, and let $U,W$ be subspaces with $\dim U=\dim W$. Prove that there exists a subspace $C$ such that
\[V=U\oplus C=W\oplus C.\]''',
    r'''Put $A=U\cap W$ and choose a basis $a_1,\ldots,a_k$ of $A$. Extend it to bases
\[a_1,\ldots,a_k,u_1,\ldots,u_r\quad\text{of }U,\]
\[a_1,\ldots,a_k,w_1,\ldots,w_r\quad\text{of }W.\]
The two extensions have the same length $r$ because $\dim U=\dim W$. Let
\[D=\Span(u_1+w_1,\ldots,u_r+w_r),\qquad S=U+W.\]
We first prove $D\cap U=\{0\}$. If $d=\sum b_j(u_j+w_j)$ belongs to $U$, then $\sum b_jw_j=d-\sum b_ju_j$ belongs to $U\cap W=A$. Expanding that vector in the $a$ basis gives a relation on the displayed basis of $W$. Independence forces every $b_j=0$, hence $d=0$. Interchanging the roles of $U$ and $W$ in this argument proves $D\cap W=\{0\}$.
Moreover, $U+D=S$: each $w_j=(u_j+w_j)-u_j$ belongs to $U+D$, and the $a_j$ already belong to $U$, so $W\subseteq U+D$; the reverse inclusion follows from $U,D\subseteq S$. The same computation with $u_j=(u_j+w_j)-w_j$ proves $W+D=S$.
Choose a complement $E$ of $S$ in $V$ and define $C=D+E$. Then $U+C=S+E=V$, and also $W+C=V$. If $c=d+e\in C\cap U$, with $d\in D$ and $e\in E$, then $e=c-d\in S\cap E=\{0\}$. Therefore $c=d\in D\cap U=\{0\}$. The same reasoning gives $C\cap W=\{0\}$. The two-subspace directness criterion proves both required decompositions. All lists may be empty where their lengths are zero; in particular $r=0$ gives $D=\{0\}$ and the argument remains valid.''',
    4,
    75,
    [
        r'Start with one basis of $U\cap W$ and extend it separately to bases of $U$ and $W$.',
        r'Pair the extra vectors from the two extensions and consider their sums.',
        r'First build a common complement inside $U+W$, then account for the rest of $V$.',
    ],
    ['lem-intersection-subspace', 'thm-subspaces-finite', 'thm-basis-existence', 'thm-extend-independent', 'def-dimension', 'thm-subspace-complement', 'c1-thm-smallest-sum', 'c1-thm-direct-intersection'],
    kind='exercise',
    optional=True,
)

s.r(
    'ex-three-subspace-inequality',
    'An inclusion-exclusion bound for three subspaces',
    r'''For subspaces $U,W,Z$ of a finite-dimensional vector space, prove
\[
\begin{aligned}
\dim(U+W+Z)\le{}&\dim U+\dim W+\dim Z\\
&-\dim(U\cap W)-\dim(U\cap Z)-\dim(W\cap Z)\\
&+\dim(U\cap W\cap Z).
\end{aligned}
\]
Prove that equality holds exactly when
\[(U+W)\cap Z=(U\cap Z)+(W\cap Z).\]
Give an example where the inequality is strict.''',
    r'''Set $A=(U+W)\cap Z$ and $B=(U\cap Z)+(W\cap Z)$. These are subspaces. Every vector of $B$ is a sum of a vector in $U$ and a vector in $W$, and both summands lie in $Z$. Hence $B\subseteq A$, so $\dim B\le\dim A$. Applying the two-subspace dimension formula gives
\[
\begin{aligned}
\dim(U+W+Z)
&=\dim(U+W)+\dim Z-\dim A\\
&=\dim U+\dim W-\dim(U\cap W)+\dim Z-\dim A.
\end{aligned}
\]
Also,
\[\dim B=\dim(U\cap Z)+\dim(W\cap Z)-\dim(U\cap W\cap Z),\]
because $(U\cap Z)\cap(W\cap Z)=U\cap W\cap Z$. Substituting $\dim A\ge\dim B$ into the preceding expression proves the claimed upper bound. The only inequality used is $\dim A\ge\dim B$, so equality holds precisely when these dimensions agree. Since $B\subseteq A$ and both are finite-dimensional, equality of dimensions is equivalent to $A=B$.
For strictness, work in $\F^2$ and take $U=\Span((1,0))$, $W=\Span((0,1))$, and $Z=\Span((1,1))$. Each space has dimension one. Every pairwise intersection is $\{0\}$: equality of scalar multiples in either pair forces both coordinates, and hence both scalars, to vanish. The triple intersection is therefore also $\{0\}$. The sum is $\F^2$, since $U+W=\F^2$. Its dimension is $2$, whereas the right side of the proposed bound is $3$.''',
    4,
    60,
    [
        r'Apply the two-subspace formula first to $U+W$ and $Z$.',
        r'Compare $(U\cap Z)+(W\cap Z)$ with $(U+W)\cap Z$.',
        r'Three distinct lines in a plane can test whether equality is automatic.',
    ],
    ['thm-dimension-sum', 'thm-subspace-dimension', 'thm-full-dimension-equality', 'lem-intersection-subspace', 'c1-thm-smallest-sum', 'ex-coordinate-dimension', 'lem-zero-dimension', 'ex-single-independent'],
    kind='exercise',
    optional=True,
)

s.card(
    'ex-replacement-coefficient',
    'ex-basis-replacement',
    r'When can a vector replace the $k$th member of a basis?',
    r'Exactly when its coefficient at the $k$th basis vector is nonzero.',
)

s.card(
    'ex-prescribed-extension',
    'ex-extension-from-specified-list',
    r'How can an independent list be extended using only entries of a given spanning list?',
    r'Inspect the spanning entries in order and append an entry precisely when it lies outside the current span.',
)

s.card(
    'ex-interpolation',
    'ex-interpolation-basis',
    r'How do the interpolation basis polynomials behave at the prescribed points?',
    r'$L_j(t_j)=1$, and $L_j(t_i)=0$ when $i\ne j$.',
)

s.card(
    'ex-intersection-bound',
    'ex-intersection-bound-sharp',
    r'What lower bound follows for the intersection of subspaces of dimensions $r,s$ in an $n$-dimensional space?',
    r'$\dim(U\cap W)\ge\max(0,r+s-n)$.',
)

s.card(
    'ex-dimension-counterexample',
    'ex-dimension-does-not-imply-inclusion',
    r'Give equal-dimensional subspaces neither of which contains the other.',
    r'In $\F^3$, $\Span(e_1,e_2)$ and $\Span(e_1,e_3)$ are distinct two-dimensional subspaces, and neither contains the other.',
)

s.card(
    'ex-common-complement',
    'ex-common-complement',
    r'What construction produces a common complement for two equal-dimensional subspaces inside their sum?',
    r'Extend a shared basis of their intersection separately, then span the pairwise sums of the additional basis vectors.',
)

s.card(
    'ex-three-space-equality',
    'ex-three-subspace-inequality',
    r'When does the three-subspace inclusion-exclusion bound become an equality?',
    r'Exactly when $(U+W)\cap Z=(U\cap Z)+(W\cap Z)$.',
)

s.write()
