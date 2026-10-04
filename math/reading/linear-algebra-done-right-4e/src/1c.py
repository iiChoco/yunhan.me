from common import Section

s = Section('1c')

s.p(
    'intro-subspaces',
    'Vector spaces inside vector spaces',
    r'''A subset can inherit the vector-space operations of a larger space.
    We develop a short test for this situation, then study how several such
    subsets combine and when their contributions can be recovered uniquely.''',
    18,
)

s.d(
    'def-subspace',
    'Subspaces',
    r'''Let $V$ be a vector space over $\F$. A subset $U\subseteq V$ is a
    \emph{subspace} of $V$ if, with the addition and scalar multiplication
    inherited from $V$ and with the same zero vector, $U$ is a vector space
    over $\F$.''',
    '1.33',
    18,
)

s.r(
    'thm-subspace-test',
    'The three-part subspace test',
    r'''A subset $U$ of a vector space $V$ is a subspace if and only if
    \begin{enumerate}
    \item $0\in U$;
    \item $u+w\in U$ whenever $u,w\in U$;
    \item $au\in U$ whenever $a\in\F$ and $u\in U$.
    \end{enumerate}''',
    r'''If $U$ is a subspace, its zero vector is the zero vector of $V$,
    and its addition and scalar multiplication are operations with values
    in $U$. These facts give the three conditions.

    Conversely, suppose the conditions hold. The closure conditions make
    the inherited operations well-defined on $U$. For $u\in U$,
    the vector $-u=(-1)u$ also belongs to $U$, so $u$ has an additive
    inverse in $U$. The vector $0\in U$ satisfies $u+0=u$.
    The equations expressing commutativity and associativity of addition,
    associativity of scalar multiplication, the scalar identity law, and
    both distributive laws hold for elements of $U$ because these elements
    lie in $V$ and the operations are unchanged. Thus every vector-space
    axiom holds on $U$, with the prescribed zero vector.''',
    2,
    20,
    [
        r'Which vector-space axioms can be inherited without further work?',
        r'Obtain the additive inverse of $u$ by multiplying $u$ by a scalar.',
    ],
    ['def-subspace', 'def-vector-space', 'thm-negative-one'],
    '1.34',
    18,
)

s.r(
    'cor-nonempty-subspace-test',
    'Replacing the zero condition by nonemptiness',
    r'''A nonempty subset of $V$ that is closed under addition and scalar
    multiplication is a subspace of $V$.''',
    r'''Choose $u$ in the subset. Closure under scalar multiplication
    places $0u$ in the subset, and $0u=0$. The three-part subspace test
    now applies.''',
    1,
    10,
    [r'Apply the scalar zero to one element of the subset.'],
    ['thm-zero-scalar', 'thm-subspace-test'],
    page=18,
    kind='corollary',
)

s.r(
    'ex-affine-coordinate-condition',
    'When a coordinate constraint is homogeneous',
    r'''Fix $b\in\F$, and let
    \[
    U_b=\{(x_1,x_2,x_3,x_4)\in\F^4:x_3=5x_4+b\}.
    \]
    Then $U_b$ is a subspace of $\F^4$ exactly when $b=0$.''',
    r'''If $U_b$ is a subspace, it contains $(0,0,0,0)$.
    Substitution in the defining equation gives $0=b$.

    Suppose now that $b=0$. The zero vector satisfies the defining equation.
    For $x,y\in U_0$,
    \[
    (x+y)_3=x_3+y_3=5x_4+5y_4=5(x_4+y_4)=5(x+y)_4.
    \]
    Thus $x+y\in U_0$. For $a\in\F$ and $x\in U_0$,
    \[
    (ax)_3=ax_3=a(5x_4)=5(ax_4)=5(ax)_4,
    \]
    so $ax\in U_0$. The subspace test proves the assertion.''',
    2,
    15,
    [
        r'First determine whether the zero vector satisfies the constraint.',
        r'When the constant term vanishes, check the equation on a sum and a scalar multiple.',
    ],
    [
        'thm-subspace-test',
        'def-coordinate-addition',
        'def-coordinate-scaling',
        'thm-complex-laws',
    ],
    '1.35(a)',
    19,
    'example',
)

s.d(
    'def-analysis-notation',
    'Continuity, derivatives, and convergence for the examples',
    r'''For a real number $x$, $|x|$ means $x$ when $x\ge0$ and $-x$
    when $x<0$. A function $f:I\to\R$, where $I$ is an interval, is
    \emph{continuous at} $t\in I$ if for every $\varepsilon>0$ there is
    a $\delta>0$ such that $x\in I$ and $|x-t|<\delta$ imply
    $|f(x)-f(t)|<\varepsilon$; it is continuous on $I$ if this holds
    at every $t\in I$.

    A real number $t$ is an accumulation point of a set $D\subseteq\R$ if every $\delta>0$ admits $x\in D$ with $0<|x-t|<\delta$.
    For a real-valued function $q$ defined near $t$, the notation
    $\lim_{x\to t}q(x)=L$ means that for every $\varepsilon>0$ there is
    a $\delta>0$ such that $0<|x-t|<\delta$ implies
    $|q(x)-L|<\varepsilon$, for $x$ in the domain of $q$.
    On an open interval $I$, $f$ is \emph{differentiable at} $t$ if the
    real limit
    \[
    f'(t)=\lim_{x\to t}\frac{f(x)-f(t)}{x-t}
    \]
    exists; it is differentiable on $I$ if this holds at every point.

    For a real sequence $(a_n)$, the notation $a_n\to0$ means that for
    every $\varepsilon>0$ there is an integer $N$ such that
    $|a_n|<\varepsilon$ whenever $n\ge N$. For a complex sequence
    $z_n=a_n+b_ni$, define $z_n\to0$ to mean that both $a_n\to0$ and
    $b_n\to0$.''',
    page=19,
)

s.add(
    'theorem',
    'thm-analysis-closure',
    'Elementary analysis facts used in the subspace examples',
    r'''Real function limits, when they exist at an accumulation point
    of the domain, are unique. The following closure facts hold.
    \begin{enumerate}
    \item The zero function on an interval is continuous. If $f,g$ are
    continuous on the same interval and $a,b\in\R$, then $af+bg$ is
    continuous there.
    \item The zero function on an open interval is differentiable with
    derivative zero. If $f,g$ are differentiable on an open interval
    and $a,b\in\R$, then $af+bg$ is differentiable there and
    \[
    (af+bg)'(t)=af'(t)+bg'(t)
    \]
    at every point of the interval.
    \item If complex sequences $(z_n)$ and $(w_n)$ converge to zero
    and $a\in\C$, then $(z_n+w_n)$ and $(az_n)$ converge to zero.
    The sequence whose terms are all zero converges to zero.
    \end{enumerate}''',
    page=19,
)

s.note(
    'remark-analysis-on-faith',
    'Analysis prerequisites accepted here',
    r'''The preceding elementary analysis theorem is taken on faith in
    this module. It supplies precisely the continuity, differentiation,
    and convergence facts needed for the next four examples; their
    subspace arguments remain proof tasks.''',
    19,
)

s.r(
    'ex-continuous-subspace',
    'Continuous functions form a subspace',
    r'''The set of continuous functions from $[0,1]$ to $\R$ is a
    subspace of the real vector space $\R^{[0,1]}$.''',
    r'''The ambient space consists of all real-valued functions on
    $[0,1]$, with pointwise operations. Its zero vector is the zero
    function, which is continuous by the elementary analysis theorem.
    If $f$ and $g$ are continuous, that theorem with coefficients
    $1,1$ shows that $f+g$ is continuous. If $a\in\R$ and $f$ is
    continuous, apply it to $f$ and the zero function with coefficients
    $a,0$ to see that $af$ is continuous. These are the three
    subspace conditions.''',
    1,
    10,
    [r'Use the accepted continuity facts to check the three subspace conditions.'],
    [
        'def-function-space',
        'thm-function-space',
        'thm-subspace-test',
        'thm-analysis-closure',
    ],
    '1.35(b)',
    19,
    'example',
)

s.r(
    'ex-differentiable-subspace',
    'Differentiable functions form a subspace',
    r'''The differentiable functions from $\R$ to $\R$ form a subspace
    of the real vector space $\R^\R$.''',
    r'''The zero function is differentiable. For differentiable $f,g$,
    the elementary analysis theorem with coefficients $1,1$ makes
    $f+g$ differentiable. For $a\in\R$, the same theorem applied to
    $f$ and the zero function with coefficients $a,0$ makes $af$
    differentiable. All operations agree with the pointwise
    operations in $\R^\R$, so the subspace test applies.''',
    1,
    10,
    [r'Check that the differentiability condition survives the inherited operations.'],
    [
        'def-function-space',
        'thm-function-space',
        'thm-subspace-test',
        'thm-analysis-closure',
    ],
    '1.35(c)',
    19,
    'example',
)

s.r(
    'ex-prescribed-derivative',
    'A prescribed derivative at one point',
    r'''For $b\in\R$, let
    \[
    D_b=\{f\in\R^{(0,3)}:f\text{ is differentiable on }(0,3)
    \text{ and }f'(2)=b\}.
    \]
    Then $D_b$ is a subspace of $\R^{(0,3)}$ if and only if $b=0$.''',
    r'''If $D_b$ is a subspace, its zero function belongs to $D_b$.
    The derivative of that function at $2$ is zero, so membership
    forces $b=0$.

    For $b=0$, the zero function belongs to $D_0$. If $f,g\in D_0$,
    their sum is differentiable and
    \[
    (f+g)'(2)=f'(2)+g'(2)=0.
    \]
    If $a\in\R$ and $f\in D_0$, then $af$ is differentiable and
    $(af)'(2)=af'(2)=a0=0$. Thus addition and scalar multiplication
    preserve $D_0$, and the subspace test completes the proof.''',
    2,
    15,
    [
        r'What derivative does the zero function have at $2$?',
        r'Use linearity of differentiation for the converse.',
    ],
    [
        'def-function-space',
        'thm-function-space',
        'thm-subspace-test',
        'thm-analysis-closure',
        'lem-scalar-cancellation',
    ],
    '1.35(d)',
    19,
    'example',
)

s.r(
    'ex-null-sequence-subspace',
    'Sequences tending to zero form a subspace',
    r'''The complex sequences that converge to zero form a subspace of
    the complex sequence space $\C^\infty$.''',
    r'''The zero sequence converges to zero. If $z=(z_n)$ and $w=(w_n)$
    converge to zero, their vector-space sum is $(z_n+w_n)$, which
    converges to zero by the elementary analysis theorem. If
    $a\in\C$ and $z_n\to0$, the scalar multiple of $z$ is $(az_n)$,
    which also converges to zero by that theorem. The subspace test
    therefore applies in $\C^\infty$.''',
    1,
    10,
    [r'Identify addition and scalar multiplication of sequences before applying the limit facts.'],
    [
        'def-sequences',
        'ex-sequence-space',
        'thm-subspace-test',
        'thm-analysis-closure',
    ],
    '1.35(e)',
    19,
    'example',
)

s.r(
    'ex-extreme-subspaces',
    'The smallest and largest subspaces',
    r'''For every vector space $V$, both $\{0\}$ and $V$ are subspaces
    of $V$, whereas $\varnothing$ is not. Every subspace $U$ satisfies
    $\{0\}\subseteq U\subseteq V$.''',
    r'''The set $\{0\}$ contains zero, and $0+0=0$ and $a0=0$
    for every scalar $a$ show closure under both operations.
    The whole set $V$ contains its zero vector and is closed under
    its defining operations. The subspace test proves that both
    sets are subspaces. The empty set fails the zero condition
    and hence is not a subspace. For any subspace $U$, the
    definition gives $U\subseteq V$, and the zero condition gives
    $\{0\}\subseteq U$.''',
    1,
    10,
    [r'Apply the zero condition as well as the two closure conditions.'],
    ['def-vector-space', 'thm-scalar-zero', 'thm-subspace-test'],
    page=19,
    kind='example',
)

s.d(
    'def-coordinate-lines-planes', 'Lines and planes through zero',
    r"""In $\R^n$, a line through zero is a set $\{tu:t\in\R\}$ with $u\ne0$. A plane through zero is a set $\{su+tv:s,t\in\R\}$ where neither $u$ nor $v$ is a scalar multiple of the other.""", page=19,
)
s.add(
    'theorem', 'thm-geometric-subspaces-accepted', 'Subspaces in two and three real coordinates',
    r"""Every subspace of $\R^2$ is $\{0\}$, a line through zero, or $\R^2$. Every subspace of $\R^3$ is $\{0\}$, a line through zero, a plane through zero, or $\R^3$. Conversely, every set in these lists is a subspace of its ambient space.""", page=19,
)
s.note(
    'remark-geometric-subspaces', 'Classification accepted at this point',
    r"""This classification is taken on faith here, as in the source's discussion. After developing bases and dimension, we will give a proof that does not rely on this accepted statement.""",19,
)

s.d(
    'def-subspace-sum',
    'Sums of subspaces',
    r'''Let $V_1,\ldots,V_m$ be subspaces of $V$, where $m\ge1$.
    Their \emph{sum} is the subset
    \[
    V_1+\cdots+V_m
    =\{v_1+\cdots+v_m:v_j\in V_j\text{ for every }j\}.
    \]
    Thus a vector belongs to this set when it can be formed by choosing
    one vector from each listed subspace and adding the choices.''',
    '1.36',
    19,
)

s.r(
    'ex-coordinate-axes-sum',
    'Two coordinate axes add to a coordinate plane',
    r'''Set
    \[
    U=\{(a,0,0):a\in\F\},\qquad
    W=\{(0,b,0):b\in\F\}.
    \]
    These are subspaces of $\F^3$, and
    \[
    U+W=\{(a,b,0):a,b\in\F\}.
    \]''',
    r'''Both sets contain zero. The formulas
    \[
    (a,0,0)+(c,0,0)=(a+c,0,0),\qquad
    t(a,0,0)=(ta,0,0)
    \]
    show that $U$ is closed under both operations. For $W$, the
    corresponding formulas are
    \[
    (0,b,0)+(0,d,0)=(0,b+d,0),\qquad
    t(0,b,0)=(0,tb,0).
    \]
    The subspace test proves the first assertion.

    Every element of $U+W$ has the form
    $(a,0,0)+(0,b,0)=(a,b,0)$, which proves one inclusion in the
    asserted equality. Conversely, this same decomposition places
    every vector $(a,b,0)$ in $U+W$.''',
    1,
    10,
    [r'For the set equality, prove both inclusions using coordinate addition.'],
    [
        'thm-subspace-test',
        'def-subspace-sum',
        'def-coordinate-addition',
        'def-coordinate-scaling',
    ],
    '1.37',
    20,
    'example',
)

s.r(
    'ex-repeated-coordinates-sum',
    'Adding two spaces with repeated coordinates',
    r'''Let
    \[
    U=\{(a,a,b,b):a,b\in\F\},\qquad
    W=\{(c,c,c,d):c,d\in\F\}.
    \]
    Then $U$ and $W$ are subspaces of $\F^4$, and
    \[
    U+W=\{(x,x,y,z):x,y,z\in\F\}.
    \]''',
    r'''Each set contains the zero vector. Adding two vectors
    $(a,a,b,b)$ and $(a',a',b',b')$ gives
    $(a+a',a+a',b+b',b+b')$, and multiplying the first by a scalar
    $t$ gives $(ta,ta,tb,tb)$. Both outputs belong to $U$.
    For $W$, the sum of $(c,c,c,d)$ and $(c',c',c',d')$ is
    $(c+c',c+c',c+c',d+d')$, and a scalar multiple is
    $(tc,tc,tc,td)$. Both outputs belong to $W$.
    Hence both sets are subspaces.

    A sum of one vector from each set has the form
    \[
    (a,a,b,b)+(c,c,c,d)=(a+c,a+c,b+c,b+d),
    \]
    so its first two coordinates agree. For the reverse inclusion,
    given $(x,x,y,z)$, use
    \[
    (x,x,y,z)=(x,x,y,y)+(0,0,0,z-y).
    \]
    The first summand belongs to $U$, and the second belongs to
    $W$ by taking $c=0$ and $d=z-y$. Thus every vector in the
    displayed target set belongs to $U+W$.''',
    2,
    20,
    [
        r'Find a coordinate relation obeyed by every sum.',
        r'Then construct summands for an arbitrary vector obeying that relation.',
    ],
    [
        'thm-subspace-test',
        'def-subspace-sum',
        'def-coordinate-addition',
        'def-coordinate-scaling',
        'def-scalar-inverses',
    ],
    '1.38',
    20,
    'example',
)

s.r(
    'thm-smallest-sum',
    'The smallest subspace containing the summands',
    r'''For subspaces $V_1,\ldots,V_m$ of $V$, with $m\ge1$, their sum
    is a subspace containing every $V_j$. If $U$ is any subspace of
    $V$ containing each $V_j$, then $V_1+\cdots+V_m\subseteq U$.''',
    r'''Write $S=V_1+\cdots+V_m$. Choosing zero from each summand
    gives $0\in S$. If $x,y\in S$, choose representations
    $x=\sum_{j=1}^m x_j$ and $y=\sum_{j=1}^m y_j$ with
    $x_j,y_j\in V_j$. Repeated associativity and commutativity give
    \[
    x+y=\sum_{j=1}^m(x_j+y_j).
    \]
    Each $x_j+y_j$ belongs to $V_j$, so $x+y\in S$.
    Repeated distributivity gives
    \[
    ax=\sum_{j=1}^m ax_j,
    \]
    and $ax_j\in V_j$, so $ax\in S$ for every scalar $a$.
    The subspace test proves that $S$ is a subspace.

    If $v\in V_k$, choose $v$ in position $k$ and zero in every other
    position. The resulting sum equals $v$, so $V_k\subseteq S$.

    Finally, let a subspace $U$ contain each $V_j$. If
    $x=\sum_{j=1}^m x_j\in S$ with $x_j\in V_j$, then each $x_j$
    belongs to $U$. To verify that their sum belongs to $U$, start
    with $x_1\in U$ and use closure under addition successively:
    whenever $\sum_{j=1}^k x_j\in U$ and $k<m$, adding
    $x_{k+1}\in U$ gives $\sum_{j=1}^{k+1}x_j\in U$.
    Thus $x\in U$, proving the final inclusion.''',
    2,
    20,
    [
        r'Check closure by combining the two vectors from each matching summand.',
        r'For minimality, use closure under finite sums in any containing subspace.',
    ],
    ['def-vector-space', 'thm-subspace-test', 'def-subspace-sum'],
    '1.40',
    21,
)

s.d(
    'def-direct-sum',
    'Direct sums',
    r'''For subspaces $V_1,\ldots,V_m$ of $V$, with $m\ge1$, the sum
    $V_1+\cdots+V_m$ is \emph{direct} when each vector in that sum
    has exactly one representation
    \[
    v_1+\cdots+v_m,\qquad v_j\in V_j.
    \]
    Uniqueness concerns the ordered list of chosen summands.
    For a direct sum we write $V_1\oplus\cdots\oplus V_m$ for the
    same subset of $V$, recording this additional uniqueness property.''',
    '1.41',
    21,
)

s.r(
    'ex-plane-axis-direct',
    'Splitting off the last coordinate',
    r'''For
    \[
    U=\{(a,b,0):a,b\in\F\},\qquad
    W=\{(0,0,c):c\in\F\},
    \]
    one has $\F^3=U\oplus W$.''',
    r'''Both sets contain zero. Adding vectors in $U$ adds their
    first two coordinates and leaves the third zero; a scalar
    multiple also has third coordinate zero. Adding vectors in $W$
    or taking scalar multiples leaves the first two coordinates zero.
    The subspace test therefore makes $U,W$ subspaces.

    Every $(x,y,z)\in\F^3$ is the sum
    $(x,y,0)+(0,0,z)$ with the indicated memberships, so
    $\F^3=U+W$. If
    \[
    (x,y,z)=(a,b,0)+(0,0,c),
    \]
    coordinate equality forces $a=x$, $b=y$, and $c=z$.
    Hence its representation has unique summands, and the sum is direct.''',
    1,
    10,
    [r'Equality of coordinates determines the two candidate summands.'],
    [
        'thm-subspace-test',
        'def-subspace-sum',
        'def-direct-sum',
        'def-coordinate-addition',
        'def-coordinate-scaling',
    ],
    '1.42',
    21,
    'example',
)

s.r(
    'ex-coordinate-direct-sum',
    'The coordinate axes give a direct sum',
    r'''Let $n\ge1$. For $1\le j\le n$, let $V_j\subseteq\F^n$
    consist of vectors whose coordinates other than coordinate $j$
    are zero. Then each $V_j$ is a subspace and
    \[
    \F^n=V_1\oplus\cdots\oplus V_n.
    \]''',
    r'''For each $j$, zero belongs to $V_j$. A sum of two vectors
    in $V_j$ has every coordinate other than $j$ equal to $0+0=0$,
    and a scalar multiple has each such coordinate equal to
    a scalar times zero, again zero. Thus $V_j$ is a subspace.

    For $x=(x_1,\ldots,x_n)$, let $v_j$ have coordinate $j$ equal to
    $x_j$ and all other coordinates zero. Then $v_j\in V_j$ and
    $\sum_{j=1}^n v_j=x$, since the only possibly nonzero contribution
    to coordinate $k$ is the $k$th coordinate of $v_k$.
    This proves that the sum equals $\F^n$.

    In any representation $x=\sum_{j=1}^n w_j$ with $w_j\in V_j$,
    coordinate $k$ forces the $k$th coordinate of $w_k$ to equal
    $x_k$. Its other coordinates are zero by membership in $V_k$,
    so $w_k=v_k$ for every $k$. This proves uniqueness, including
    the case $n=1$.''',
    2,
    15,
    [r'At any fixed coordinate, only one summand can contribute.'],
    [
        'thm-subspace-test',
        'def-direct-sum',
        'def-subspace-sum',
        'def-coordinate-addition',
        'def-coordinate-scaling',
        'lem-scalar-cancellation',
    ],
    '1.43',
    22,
    'example',
)

s.r(
    'ex-three-nondirect',
    'Three summands with nonunique decompositions',
    r'''In $\F^3$, let
    \[
    V_1=\{(a,b,0):a,b\in\F\},\quad
    V_2=\{(0,0,c):c\in\F\},\quad
    V_3=\{(0,d,d):d\in\F\}.
    \]
    These are subspaces whose sum is $\F^3$, but the sum is not direct.''',
    r'''The first two sets are the subspaces from the plane-and-axis
    example. The set $V_3$ contains zero, and
    \[
    (0,d,d)+(0,e,e)=(0,d+e,d+e),\qquad
    a(0,d,d)=(0,ad,ad)
    \]
    prove its closure under addition and scalar multiplication.
    Thus $V_3$ is also a subspace.

    Every $(x,y,z)$ has the representation
    $(x,y,0)+(0,0,z)+(0,0,0)$, so the sum is $\F^3$.
    The zero vector has both the all-zero representation and the
    representation
    \[
    0=(0,-1,0)+(0,0,-1)+(0,1,1).
    \]
    The displayed summands belong respectively to $V_1,V_2,V_3$.
    The two ordered lists of summands differ, since $1\ne0$ in $\F$.
    Thus uniqueness fails and the sum is not direct.''',
    2,
    15,
    [
        r'The first two summands already cover the ambient space.',
        r'Look for a nonzero vector in the third summand that can be cancelled by vectors from the first two.',
    ],
    [
        'ex-plane-axis-direct',
        'thm-subspace-test',
        'def-subspace-sum',
        'def-direct-sum',
        'def-coordinate-addition',
        'def-coordinate-scaling',
    ],
    '1.44',
    22,
    'example',
)

s.r(
    'thm-direct-zero',
    'Testing uniqueness only at zero',
    r'''Let $V_1,\ldots,V_m$ be subspaces of $V$, with $m\ge1$.
    Their sum is direct if and only if
    \[
    v_1+\cdots+v_m=0,\qquad v_j\in V_j,
    \]
    forces $v_j=0$ for every $j$.''',
    r'''Suppose first that the sum is direct. Each $V_j$ contains
    zero, so the ordered list of zero vectors is a representation
    of zero. Uniqueness in the definition of a direct sum forces
    every other representation of zero to have these same entries.

    Conversely, assume the stated property of zero, and suppose
    a vector $x$ has two representations
    \[
    x=\sum_{j=1}^m u_j=\sum_{j=1}^m v_j,\qquad u_j,v_j\in V_j.
    \]
    Put $d_j=u_j-v_j$. Since $-v_j=(-1)v_j\in V_j$ and
    $V_j$ is closed under addition, $d_j\in V_j$.
    If $d=\sum_{j=1}^m d_j$, repeated associativity and
    commutativity give
    \[
    d+x
    =\sum_{j=1}^m(u_j-v_j)+\sum_{j=1}^m v_j
    =\sum_{j=1}^m\bigl(u_j+(-v_j+v_j)\bigr)
    =\sum_{j=1}^m u_j=x.
    \]
    Comparing $d+x=x$ with $0+x=x$ and cancelling $x$ gives $d=0$.
    The hypothesis now gives $d_j=0$ for every $j$.
    Adding $v_j$ to $u_j-v_j=0$ yields $u_j=v_j$.
    Thus any two representations agree in every position.
    Existence of a representation for a vector in the sum follows
    from the definition of that sum, so the sum is direct.''',
    2,
    20,
    [
        r'To compare two representations, form the differences of matching summands.',
        r'Those differences lie in the same subspaces and their sum is zero.',
    ],
    [
        'def-vector-space',
        'def-vector-subtraction',
        'thm-negative-one',
        'lem-vector-cancellation',
        'thm-subspace-test',
        'def-subspace-sum',
        'def-direct-sum',
    ],
    '1.45',
    23,
)

s.r(
    'thm-direct-intersection',
    'The intersection criterion for two summands',
    r'''For subspaces $U,W$ of $V$, the sum $U+W$ is direct if and
    only if $U\cap W=\{0\}$.''',
    r'''Assume first that $U+W$ is direct and take $v\in U\cap W$.
    Because $W$ is closed under scalar multiplication,
    $-v=(-1)v\in W$. The equation $v+(-v)=0$ is a representation
    of zero with the first summand in $U$ and the second in $W$.
    The zero criterion for direct sums gives $v=0$. Thus
    $U\cap W\subseteq\{0\}$; the opposite inclusion holds because
    both subspaces contain zero.

    Conversely, suppose $U\cap W=\{0\}$ and take $u\in U$, $w\in W$
    with $u+w=0$. Adding $-w$ gives $u=-w$. Closure of $W$ under
    scalar multiplication places $-w$ in $W$, so $u\in U\cap W$.
    Hence $u=0$, and $u+w=0$ then gives $w=0$. Every representation
    of zero in the sum has zero summands, so the zero criterion
    proves that $U+W$ is direct.''',
    2,
    15,
    [
        r'A vector in the intersection can be used once in each summand with opposite signs.',
        r'For the converse, start from a representation of zero.',
    ],
    [
        'def-vector-space',
        'thm-negative-one',
        'thm-subspace-test',
        'thm-direct-zero',
    ],
    '1.46',
    23,
)

s.r(
    'ex-pairwise-zero-insufficient',
    'Pairwise zero intersections do not suffice for three summands',
    r'''For the three subspaces $V_1,V_2,V_3$ in the earlier
    non-direct-sum example,
    \[
    V_1\cap V_2=V_1\cap V_3=V_2\cap V_3=\{0\}.
    \]
    Consequently, the two-subspace intersection criterion cannot be
    extended to three subspaces by checking their pairwise intersections.''',
    r'''A vector in $V_1\cap V_2$ has first and second coordinates
    zero by membership in $V_2$, and third coordinate zero by
    membership in $V_1$. Hence it is zero.

    A vector in $V_1\cap V_3$ has the form $(0,d,d)$, and its
    third coordinate is zero by membership in $V_1$. Therefore
    $d=0$ and the vector is zero.

    A vector in $V_2\cap V_3$ also has the form $(0,d,d)$, and its
    second coordinate is zero by membership in $V_2$. Again
    $d=0$ and the vector is zero.

    Each intersection contains zero because the sets are subspaces,
    proving all three equalities. Their sum was already proved not
    to be direct, so these equalities are insufficient to guarantee
    directness for three summands.''',
    1,
    10,
    [r'For each pair, combine the coordinate restrictions defining the two sets.'],
    ['ex-three-nondirect', 'thm-subspace-test'],
    page=24,
    kind='example',
)

s.card(
    'subspace-definition',
    'def-subspace',
    r'What operations does a subspace use?',
    r'''It uses the ambient vector space addition and scalar multiplication,
    over the same scalar field, and has the same zero vector.''',
)

s.card(
    'subspace-test',
    'thm-subspace-test',
    r'State the three-part test for a subset $U\subseteq V$ to be a subspace.',
    r'''$0\in U$; $u+w\in U$ for $u,w\in U$; and $au\in U$
    for $a\in\F$ and $u\in U$.''',
)

s.card(
    'affine-obstruction',
    'ex-affine-coordinate-condition',
    r'''What is the quickest obstruction to the subspace property for
    $\{x\in\F^4:x_3=5x_4+b\}$ when $b\ne0$?''',
    r'The zero vector does not satisfy the equation.',
)

s.card(
    'subspace-sum',
    'def-subspace-sum',
    r'What does it mean for $x$ to belong to $V_1+\cdots+V_m$?',
    r'There must be $v_j\in V_j$ such that $x=v_1+\cdots+v_m$.',
)

s.card(
    'smallest-sum',
    'thm-smallest-sum',
    r'How is $V_1+\cdots+V_m$ characterized by containment?',
    r'''It is a subspace containing every $V_j$, and it is contained in
    every subspace containing all the $V_j$.''',
)

s.card(
    'direct-sum-definition',
    'def-direct-sum',
    r'''What additional property does the notation
    $V_1\oplus\cdots\oplus V_m$ assert?''',
    r'''Every vector in the sum has a unique ordered list of summands,
    with the $j$th summand in $V_j$.''',
)

s.card(
    'direct-zero',
    'thm-direct-zero',
    r'Why is it enough to check representations of zero when testing directness?',
    r'''The differences of matching terms in two representations belong
    to the same summand subspaces and add to zero.''',
)

s.card(
    'direct-intersection',
    'thm-direct-intersection',
    r'When is the sum of two subspaces $U,W$ direct?',
    r'Exactly when $U\cap W=\{0\}$.',
)

s.card(
    'pairwise-intersections',
    'ex-pairwise-zero-insufficient',
    r'Give three subspaces with pairwise intersection $\{0\}$ whose sum is not direct.',
    r'''In $\F^3$, take $V_1=\{(a,b,0)\}$,
    $V_2=\{(0,0,c)\}$, and $V_3=\{(0,d,d)\}$, with all displayed
    parameters in $\F$. Their pairwise intersections are $\{0\}$,
    but $0=(0,-1,0)+(0,0,-1)+(0,1,1)$ is a nonzero-summand
    representation of zero.''',
)

s.write()
