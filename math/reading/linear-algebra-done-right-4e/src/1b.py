from common import Section
s=Section('1b')
s.p('intro-vector-spaces','From coordinates to vector spaces',r'''The identities proved for coordinate lists can be imposed on other kinds of objects. A vector space packages these identities into axioms, so one argument can apply to lists, sequences, and functions. We first check these examples and then derive consequences of the axioms.''',12)
s.d('def-vector-operations','Addition and scalar multiplication on a set',r'''An addition on a set $V$ is a function from $V\times V$ to $V$, written $(u,v)\mapsto u+v$. A scalar multiplication is a function from $\F\times V$ to $V$, written $(a,v)\mapsto av$. Both operations must be defined for every indicated input and return an element of $V$.''','1.19',12)
s.d('def-vector-space','Vector space axioms',r'''A vector space over $\F$ is a set $V$ equipped with addition and scalar multiplication satisfying these axioms:
\begin{itemize}
\item $u+v=v+u$ for $u,v\in V$.
\item $(u+v)+w=u+(v+w)$ for $u,v,w\in V$.
\item There is $0_V\in V$ such that $v+0_V=v$ for every $v\in V$.
\item For every $v\in V$ there is $w\in V$ such that $v+w=0_V$.
\item $(ab)v=a(bv)$ for $a,b\in\F$ and $v\in V$.
\item $1v=v$ for every $v\in V$.
\item $a(u+v)=au+av$ for $a\in\F$ and $u,v\in V$.
\item $(a+b)v=av+bv$ for $a,b\in\F$ and $v\in V$.
\end{itemize}
We usually write $0$ for $0_V$ when the context determines its meaning. A vector space is nonempty because it contains an additive identity.''','1.20',12)
s.d('def-vector-terminology','Vectors and points',r'''An element of a vector space is called a vector, or a point. These terms do not require the element to be a coordinate list.''','1.21',12)
s.d('def-real-complex-space','Real and complex vector spaces',r'''A vector space with scalar field $\R$ is real; one with scalar field $\C$ is complex. The scalar field is part of the specification of the vector space.''','1.22',13)
s.r('ex-coordinate-space','Coordinate spaces satisfy the axioms',r'''For every nonnegative integer $n$, coordinate addition and scalar multiplication make $\F^n$ a vector space over $\F$. The zero list is an additive identity, and the coordinate negative is an additive inverse.''',r'''Each operation returns a length-$n$ list with scalar entries, so the operations have the required domains and codomains. Coordinate commutativity gives commutative addition. The remaining coordinate identities give associative addition, $(ab)x=a(bx)$, $1x=x$, and both distributive laws. The zero-list identity and the coordinate-inverse result supply an identity and inverses. Thus all eight axioms hold. Those earlier results include $n=0$, when there is only the empty list and both operations return that list.''',1,10,[r'Match each axiom with an established coordinate identity.'],['def-vector-space','def-coordinate-space','def-coordinate-addition','def-coordinate-scaling','thm-coordinate-commutativity','ex-coordinate-identity','lem-coordinate-inverse','lem-coordinate-laws'],page=13,kind='example')
s.r('ex-zero-space','The one-element vector space',r'''Let $V=\{z\}$, define $z+z=z$, and define $az=z$ for every $a\in\F$. Then $V$ is a vector space.''',r'''Both operations are defined on their required domains and return $z$. Every side of every equality in the axioms equals $z$, so all the associative, commutative, and distributive identities hold, as does $1z=z$. The element $z$ is an additive identity and its own additive inverse because $z+z=z$.''',1,10,[r'Every expression taking values in this set has the same value.'],['def-vector-space'],page=13,kind='example')
s.d('def-sequences','Scalar sequences',r'''Let $\F^\infty$ consist of sequences $x=(x_1,x_2,\ldots)$ indexed by $\N$. Equality means agreement at every index. Define $(x+y)_k=x_k+y_k$ and $(ax)_k=ax_k$ for every $k\in\N$.''','1.23',13)
s.r('ex-sequence-space','Sequences form a vector space',r'''The specified operations make $\F^\infty$ a vector space over $\F$. The all-zero sequence is an additive identity, and the sequence with entries $-x_k$ is an additive inverse of $x$.''',r'''Both operations produce scalar entries at every index, so they produce sequences. For $x,y,z\in\F^\infty$ and $a,b\in\F$, at each index $k$ scalar arithmetic gives
\[\begin{aligned}
x_k+y_k&=y_k+x_k, & (x_k+y_k)+z_k&=x_k+(y_k+z_k),\\
(ab)x_k&=a(bx_k), & 1x_k&=x_k,\\
a(x_k+y_k)&=ax_k+ay_k, & (a+b)x_k&=ax_k+bx_k.
\end{aligned}\]
These coordinate equalities give commutativity and associativity of addition, compatibility with scalar products, the scalar identity axiom, and both distributive axioms. The all-zero sequence belongs to the set and satisfies $x_k+0=x_k$ at every index. The sequence with entries $-x_k$ also belongs to the set and satisfies $x_k+(-x_k)=0$ at every index. This verifies the remaining axioms.''',2,20,[r'Check equality one index at a time.',r'Specify every entry of the identity and inverse sequences.'],['foundations','thm-complex-laws','thm-complex-inverses','def-scalars','def-sequences','def-vector-space'],'1.23',13,'example')
s.d('def-function-space','Scalar-valued functions on a set',r'''For a set $S$, let $\F^S$ be the set of functions from $S$ to $\F$. For $x\in S$, define
\[(f+g)(x)=f(x)+g(x),\qquad (af)(x)=af(x).\]
For example, $\R^{[0,1]}$ contains all real-valued functions on $[0,1]$, without any continuity requirement.''','1.24',13)
s.r('thm-function-space','Function spaces satisfy the axioms',r'''For any set $S$, including the empty set, $\F^S$ is a vector space with these operations. The function $z(x)=0$ is an additive identity; the function $h(x)=-f(x)$ is an additive inverse of $f$.''',r'''Each rule specifies one scalar for each $x\in S$, so sums, scalar multiples, $z$, and $h$ are functions with the required domain and target. For $f,g,q\in\F^S$ and $a,b\in\F$, evaluation at any $x\in S$ gives
\[\begin{aligned}
(f+g)(x)&=f(x)+g(x)=g(x)+f(x)=(g+f)(x),\\
((f+g)+q)(x)&=(f(x)+g(x))+q(x)\\
&=f(x)+(g(x)+q(x))=(f+(g+q))(x),\\
((ab)f)(x)&=(ab)f(x)=a(bf(x))=(a(bf))(x),\\
(1f)(x)&=f(x),\\
(a(f+g))(x)&=a(f(x)+g(x))=af(x)+ag(x)=(af+ag)(x),\\
((a+b)f)(x)&=(a+b)f(x)=af(x)+bf(x)=(af+bf)(x).
\end{aligned}\]
Scalar distributivity and commutativity justify the last identity. Agreement at every argument proves these six axioms. Also $(f+z)(x)=f(x)$ and $(f+h)(x)=0=z(x)$ for each $x$, proving the identity and inverse axioms. For $S=\varnothing$, there is exactly one function, the empty function; all constructed functions equal it and all these equalities hold. This includes the empty-domain case.''',2,20,[r'Evaluate each vector space identity at an arbitrary argument.',r'Two functions with the same domain are equal when their values agree everywhere.'],['foundations','thm-complex-laws','thm-complex-inverses','def-scalars','def-vector-space','def-function-space'],'1.25',14,'example')
s.note('remark-functions-as-vectors','Coordinates are function values',r'''A list in $\F^n$ can be viewed as a function on $\{1,\ldots,n\}$ by sending $k$ to its $k$th entry. A sequence is a function on $\N$. These viewpoints explain why the preceding examples have the same arithmetic rules.''',14)
s.r('thm-unique-zero','Uniqueness of the additive identity',r'''A vector space has exactly one additive identity.''',r'''Existence is an axiom. If $e$ and $z$ are both identities, the identity property of $z$ gives $e+z=e$, whereas the identity property of $e$ gives $z+e=z$. The left sides are equal by commutativity, so $e=z$.''',1,10,[r'Add the two proposed identities.'],['def-vector-space'],'1.26',14)
s.r('thm-unique-negative','Uniqueness of additive inverses',r'''For each $v\in V$, exactly one $w\in V$ satisfies $v+w=0$.''',r'''An inverse exists by the vector space axioms, and the additive identity is unique. Suppose $v+w=0$ and $v+t=0$. Adding $w$ on the left of the latter equation gives $w+(v+t)=w$. By associativity and commutativity the left side equals $(v+w)+t=0+t=t$. Thus $w=t$.''',1,10,[r'Use one proposed inverse to simplify the equation for the other.'],['def-vector-space','thm-unique-zero'],'1.27',15)
s.d('def-vector-subtraction','Vector negatives and subtraction',r'''Write $-v$ for the unique additive inverse of $v$. Define $w-v=w+(-v)$ for vectors in the same space.''','1.28',15)
s.d('def-ambient-space','Standing vector space notation',r'''Unless specified otherwise, $V$ denotes a vector space over $\F$, where $\F$ is $\R$ or $\C$. Operations in a statement are those of the specified vector space.''','1.29',15)
s.r('lem-vector-cancellation','Cancellation for vector addition',r'''If $u+v=u+w$ in $V$, then $v=w$.''',r'''Add $-u$ on the left and use associativity to obtain $((-u)+u)+v=((-u)+u)+w$. Commutativity and the inverse property give $(-u)+u=0$, so the identity axiom gives $v=w$.''',1,10,[r'Add the inverse of the shared summand.'],['def-vector-space','def-vector-subtraction'],page=15,kind='lemma')
s.r('thm-zero-scalar','The zero scalar annihilates vectors',r'''For every $v\in V$, $0v=0_V$. The zero on the left is a scalar; the right side is a vector.''',r'''Put $x=0v$. Distributivity applied to $0+0=0$ gives $x=(0+0)v=0v+0v=x+x$. Since $x+0_V=x$, we have $x+0_V=x+x$. Vector cancellation gives $0_V=x$.''',1,10,[r'Apply distributivity to $0+0=0$.'],['foundations','thm-complex-laws','def-vector-space','lem-vector-cancellation'],'1.30',15)
s.r('thm-scalar-zero','Scalars preserve the zero vector',r'''For every $a\in\F$, $a0_V=0_V$.''',r'''From $0_V+0_V=0_V$ and distributivity, $a0_V=a0_V+a0_V$. Also $a0_V+0_V=a0_V$. Cancellation in $a0_V+0_V=a0_V+a0_V$ therefore gives $0_V=a0_V$.''',1,10,[r'Expand $a(0_V+0_V)$.'],['def-vector-space','lem-vector-cancellation'],'1.31',16)
s.r('thm-negative-one','Multiplication by minus one gives the negative',r'''For $v\in V$, $(-1)v=-v$.''',r'''Since $(-1)+1=0$, distributivity and $1v=v$ give $(-1)v+v=((-1)+1)v=0v=0_V$. Commutativity shows $v+(-1)v=0_V$, so $(-1)v$ is an additive inverse of $v$. Its uniqueness gives $(-1)v=-v$.''',1,10,[r'Show that the proposed expression is an additive inverse.'],['foundations','thm-complex-inverses','def-vector-space','thm-unique-negative','def-vector-subtraction','thm-zero-scalar'],'1.32',16)
s.card('vector-axioms','def-vector-space',r'State both distributive axioms.',r'$a(u+v)=au+av$ and $(a+b)v=av+bv$.')
s.card('vector-nonempty','def-vector-space',r'Why is the empty set not a vector space?',r'It contains no additive identity.')
s.card('scalar-field','def-real-complex-space',r'What distinguishes a real vector space from a complex one?',r'The scalar field is $\R$ in the first case and $\C$ in the second.')
s.card('function-space-operations','def-function-space',r'How are operations defined in $\F^S$?',r'$(f+g)(x)=f(x)+g(x)$ and $(af)(x)=af(x)$ for every $x\in S$.')
s.card('empty-domain','thm-function-space',r'What is $\F^\varnothing$?',r'The one-element vector space consisting of the empty function.')
s.card('zero-uniqueness','thm-unique-zero',r'What proves uniqueness of the additive identity?',r'Adding two proposed identities gives a sum equal to each of them.')
s.card('vector-zero-identities','thm-zero-scalar',r'How do $0v=0_V$ and $a0_V=0_V$ differ?',r'One multiplies any vector by zero; the other multiplies the zero vector by any scalar.')
s.card('negative-one','thm-negative-one',r'Why is $(-1)v=-v$?',r'Distributivity shows it is an additive inverse, and that inverse is unique.')
s.write()
