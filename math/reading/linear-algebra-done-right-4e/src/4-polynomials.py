from common import Section

s = Section('4-polynomials')

s.p('intro-polynomials', 'Roots, division, and factorization', r'''We develop the polynomial facts needed for the study of linear operators. After establishing some scalar identities, we relate roots to factors and prove division with remainder. The final results describe how the permitted factors differ over $\C$ and $\R$.''', 120)

s.d('def-real-imaginary', 'Real and imaginary parts', r'''For $z=a+bi$ with $a,b\in\R$, define $\operatorname{Re}z=a$ and $\operatorname{Im}z=b$. Thus
\[z=\operatorname{Re}z+i\operatorname{Im}z.\]
Both parts are real numbers.''', '4.1', 120)

s.d('def-conjugate-modulus', 'Complex conjugation and absolute value', r'''For $z=a+bi\in\C$, define
\[\overline z=a-bi,\qquad |z|=\sqrt{a^2+b^2},\]
where the square root is the nonnegative real square root. These are the complex conjugate and the absolute value, or modulus, of $z$.''', '4.2', 120)

s.r('ex-complex-parts', 'Computing scalar parts and modulus', r'''For $z=3+2i$, compute its real part, imaginary part, conjugate, and modulus.''',
r'''The coefficients in the expression $3+2i$ give $\operatorname{Re}z=3$ and $\operatorname{Im}z=2$. Reversing the sign of the imaginary coefficient gives $\overline z=3-2i$. Finally, $|z|=\sqrt{3^2+2^2}=\sqrt{13}$.''',
1, 10, [r'Apply each definition to the two real coordinates.'],
['def-real-imaginary', 'def-conjugate-modulus'], '4.3', 120, 'example')

s.r('thm-complex-properties', 'Conjugation, modulus, and the triangle inequality', r'''For $w,z\in\C$,
\[
\begin{aligned}
z+\overline z&=2\operatorname{Re}z,&
z-\overline z&=2i\operatorname{Im}z,&
z\overline z&=|z|^2,\\
\overline{w+z}&=\overline w+\overline z,&
\overline{wz}&=\overline w\,\overline z,&
\overline{\overline z}&=z,\\
|\operatorname{Re}z|&\le |z|,&
|\operatorname{Im}z|&\le |z|,&
|\overline z|&=|z|,\\
|wz|&=|w|\,|z|,&
|w+z|&\le |w|+|z|.
\end{aligned}
\]
Moreover, $|z|=0$ exactly when $z=0$, and $\overline z=z$ exactly when $z$ is real.''',
r'''Write $z=a+bi$ and $w=c+di$, with real coordinates. Adding and subtracting $a-bi$ gives $z+\overline z=2a$ and $z-\overline z=2bi$. Multiplication gives $z\overline z=a^2+b^2=|z|^2$. Conjugating the coordinate sum gives
\[\overline{w+z}=(c+a)-(d+b)i=(c-di)+(a-bi).\]
The product $wz$ has coordinates $(ca-db,cb+da)$, so its conjugate is $(ca-db)-(cb+da)i$. Multiplication of $c-di$ and $a-bi$ gives this same expression, proving multiplicativity of conjugation. Applying conjugation twice restores $a+bi$.

For nonnegative real numbers $u,v$, the implication $u^2\le v^2\Longrightarrow u\le v$ follows because $u>v$ would give $(u-v)(u+v)>0$, hence $u^2>v^2$. The real modulus of $a$ has square $a^2$ and is nonnegative, so $a^2\le a^2+b^2$ gives $|a|\le|z|$. The same reasoning gives $|b|\le|z|$. Replacing $b$ by $-b$ in the modulus formula proves $|\overline z|=|z|$. The sum $a^2+b^2$ vanishes exactly when both real squares vanish, hence exactly when $a=b=0$; this proves the zero-modulus assertion. Equality $a-bi=a+bi$ is equivalent to $2b=0$, hence to $b=0$, proving the assertion about real numbers.

Using conjugation of products,
\[|wz|^2=wz\,\overline{wz}
=wz\,\overline w\,\overline z
=|w|^2|z|^2.\]
Both $|wz|$ and $|w||z|$ are nonnegative, so their equal squares make them equal. Finally, expansion gives
\[
\begin{aligned}
|w+z|^2
&=|w|^2+|z|^2+w\overline z+\overline w z\\
&=|w|^2+|z|^2+2\operatorname{Re}(w\overline z)\\
&\le |w|^2+|z|^2+2|w\overline z|\\
&=|w|^2+|z|^2+2|w||z|\\
&=(|w|+|z|)^2.
\end{aligned}
\]
Here $\operatorname{Re}(w\overline z)\le|\operatorname{Re}(w\overline z)|\le|w\overline z|$ by the real order and the already established part bound. Comparing nonnegative square roots proves the triangle inequality.''',
3, 35, [r'Begin with coordinate calculations for conjugation.', r'Prove the product rule for moduli by squaring.', r'Expand $|w+z|^2$ and bound the real part of its mixed term.'],
['def-real-imaginary', 'def-conjugate-modulus', 'c1-def-complex', 'c1-thm-complex-laws', 'c1-foundations'], '4.4', 121)

s.r('lem-polynomial-product-degree', 'Products and leading terms of polynomials', r'''The pointwise product of two polynomials over $\F$ is a polynomial. If $p,q$ are nonzero, then
\[\deg(pq)=\deg p+\deg q,\]
and the leading coefficient of $pq$ is the product of their leading coefficients. For arbitrary polynomials,
\[\deg(p+q)\le\max(\deg p,\deg q).\]
In particular, the product of two nonzero polynomials is nonzero.''',
r'''Write $p(z)=\sum_{j=0}^m a_jz^j$ and $q(z)=\sum_{k=0}^n b_kz^k$. Scalar distributivity and the laws of powers give
\[(pq)(z)=\sum_{j=0}^m\sum_{k=0}^n a_jb_kz^{j+k}.\]
Collecting terms with equal exponents yields a polynomial. If $p,q$ are nonzero and $m,n$ are their degrees, the only summand with exponent $m+n$ is $a_mb_nz^{m+n}$. The coefficient $a_mb_n$ is nonzero because the scalar field has no zero divisors. All other exponents are smaller, so coefficient uniqueness gives the degree and leading-coefficient assertions. If either polynomial is zero, its product is the zero polynomial by pointwise multiplication.

For the sum, if both polynomials are zero, the asserted inequality reads $-\infty\le-\infty$. Otherwise choose polynomial representations whose exponents are bounded by the larger of the two degrees, padding the shorter list with zeros. Adding the representations introduces no higher power, so the degree of the sum is at most that bound, including when the sum vanishes.''',
2, 20, [r'In the expanded product, identify the unique contribution to the largest possible exponent.'],
['c2-def-polynomial', 'c2-def-degree', 'c2-lem-polynomial-coefficients', 'c1-thm-complex-laws', 'c1-lem-scalar-powers', 'c1-lem-scalar-cancellation'], page=122, kind='lemma')

s.r('lem-polynomial-cancellation', 'Cancellation of a nonzero polynomial factor', r'''If $s,p,q\in\Poly(\F)$, $s\ne0$, and $sp=sq$, then $p=q$.''',
r'''Pointwise distributivity gives $s(p-q)=0$. If $p-q$ were nonzero, the product-degree lemma would make $s(p-q)$ nonzero, a contradiction. Therefore $p-q=0$, which means $p=q$.''',
1, 10, [r'Reduce cancellation to the impossibility of a zero product of two nonzero polynomials.'],
['lem-polynomial-product-degree', 'c2-thm-polynomial-subspace'], page=122, kind='lemma')

s.d('def-polynomial-zero', 'Zeros of a polynomial', r'''A scalar $\lambda\in\F$ is a zero, or root, of $p\in\Poly(\F)$ if $p(\lambda)=0$. Unless multiplicities are explicitly mentioned, a count of zeros means a count of distinct scalar values.''', '4.5', 122)

s.r('thm-factor-root', 'A root gives a linear factor', r'''Suppose $p\in\Poly(\F)$ has degree $m\ge1$ and $\lambda\in\F$. Then $p(\lambda)=0$ if and only if there is a polynomial $q$ of degree $m-1$ with
\[p(z)=(z-\lambda)q(z)\quad(z\in\F).\]''',
r'''Write $p(z)=\sum_{k=0}^m a_kz^k$, where $a_m\ne0$. For every positive integer $k$,
\[(z-\lambda)\sum_{j=0}^{k-1}z^{k-1-j}\lambda^j=z^k-\lambda^k.\]
Indeed, multiplication by $z$ gives the terms $z^{k-j}\lambda^j$ for $0\le j\le k-1$, while multiplication by $-\lambda$ gives their negatives with indices $1\le j\le k$; every intermediate term cancels, leaving $z^k-\lambda^k$.

If $p(\lambda)=0$, then
\[
p(z)=p(z)-p(\lambda)
=(z-\lambda)\sum_{k=1}^m a_k\sum_{j=0}^{k-1}z^{k-1-j}\lambda^j.
\]
Define $q$ by the double sum. Its coefficient of $z^{m-1}$ is $a_m$, and every other term has smaller exponent. Thus $q$ has degree $m-1$. Conversely, a factorization of the displayed form gives $p(\lambda)=(\lambda-\lambda)q(\lambda)=0$ by evaluation.''',
2, 20, [r'First factor $z^k-\lambda^k$ by a telescoping sum.', r'Apply that identity to $p(z)-p(\lambda)$.'],
['def-polynomial-zero', 'c2-def-polynomial', 'c2-lem-polynomial-coefficients', 'c2-def-degree', 'c1-lem-scalar-powers', 'c1-thm-complex-laws'], '4.6', 122)

s.r('thm-root-bound', 'A nonzero polynomial has at most its degree many roots', r'''A nonzero polynomial of degree $m\ge0$ has at most $m$ distinct roots in $\F$.''',
r'''We use induction on $m$. A nonzero constant has no root, giving the case $m=0$. Suppose $m\ge1$ and the claim holds for degree $m-1$. If $p$ has no root, the required bound holds. Otherwise choose a root $\lambda$. The factor-root theorem gives $p(z)=(z-\lambda)q(z)$ with $\deg q=m-1$. Every root $\mu$ of $p$ different from $\lambda$ satisfies $(\mu-\lambda)q(\mu)=0$. Since $\mu-\lambda\ne0$, scalar cancellation gives $q(\mu)=0$. There are at most $m-1$ such values by the induction hypothesis. Including $\lambda$ gives at most $m$ distinct roots of $p$.''',
2, 20, [r'Remove one linear factor and apply induction to the remaining polynomial.'],
['def-polynomial-zero', 'thm-factor-root', 'c1-lem-scalar-cancellation', 'c1-foundations'], '4.8', 123)

s.r('thm-polynomial-agreement', 'Agreement at infinitely many scalars determines a polynomial', r'''If two polynomials over $\F$ agree at infinitely many scalar values, they are equal as polynomials and have identical coefficient lists after trailing zeros are appended.''',
r'''Their difference is a polynomial vanishing at every scalar where they agree. If it were nonzero, the root bound would give only finitely many zeros, contrary to the hypothesis. Thus their difference is the zero function. Coefficient uniqueness then shows that corresponding coefficients agree after padding the representations with zeros.''',
1, 10, [r'Apply the root bound to the difference.'],
['thm-root-bound', 'c2-thm-polynomial-subspace', 'c2-lem-polynomial-coefficients'], page=123)

s.r('lem-distinct-degrees-independent', 'Distinct degrees give independent polynomials', r'''A finite list of nonzero polynomials having pairwise distinct degrees is linearly independent.''',
r'''Suppose a zero linear combination has at least one nonzero coefficient. Among the polynomials with nonzero coefficients in that combination, choose the one of largest degree. No other term contributes to that power, so the coefficient of this largest power in the sum is the nonzero scalar coefficient of the chosen polynomial times its nonzero leading coefficient. This product is nonzero. Coefficient uniqueness therefore prevents the sum from being zero, a contradiction. Thus every coefficient in a zero relation must vanish. An empty list is independent by definition.''',
2, 15, [r'Choose the highest-degree polynomial whose scalar coefficient in the relation is nonzero.'],
['c2-def-linear-independence', 'c2-def-degree', 'c2-lem-polynomial-coefficients', 'c1-lem-scalar-cancellation'], page=124, kind='lemma')

s.r('thm-polynomial-division', 'Division with a unique remainder', r'''For $p,s\in\Poly(\F)$ with $s\ne0$, there exist unique polynomials $q,r$ such that
\[p=sq+r,\qquad \deg r<\deg s.\]''',
r'''Put $m=\deg s$. If $p=0$, the choices $q=r=0$ give existence. If $p\ne0$ and $\deg p<m$, take $q=0$ and $r=p$. In the remaining case put $n=\deg p\ge m$. Consider the list
\[1,z,\ldots,z^{m-1},\ s,zs,\ldots,z^{n-m}s,\]
where the first portion is empty if $m=0$. The product-degree lemma shows that the degrees of these polynomials are exactly $0,1,\ldots,n$, each occurring once. Thus the list is independent. It has $n+1$ entries in the $(n+1)$-dimensional space $\Poly_n(\F)$, so it is a basis. Expanding $p$ in this basis gives scalars $a_0,\ldots,a_{m-1}$ and $b_0,\ldots,b_{n-m}$ such that
\[p=\sum_{j=0}^{m-1}a_jz^j+s\sum_{k=0}^{n-m}b_kz^k.\]
Take $r$ to be the first sum and $q$ the second. Then $\deg r<m$, including $m=0$, when $r=0$ and $\deg r=-\infty$.

For uniqueness in every case, suppose $p=sq_1+r_1=sq_2+r_2$ with both remainder degrees below $m$. Then
\[s(q_1-q_2)=r_2-r_1.\]
If $q_1-q_2$ were nonzero, the left side would have degree $m+\deg(q_1-q_2)\ge m$. The right side has degree below $m$ by the bound on the degree of a sum, also when one or both remainders vanish. This is impossible. Thus $q_1=q_2$, and the displayed equality then gives $r_1=r_2$.''',
3, 35, [r'For existence, build a basis combining low powers with multiples of the divisor.', r'For uniqueness, compare the degrees in the difference of two proposed divisions.'],
['lem-polynomial-product-degree', 'lem-distinct-degrees-independent', 'c2-ex-polynomial-dimension', 'c2-thm-full-length-independent', 'c2-thm-basis-coordinates', 'c2-def-degree'], '4.9', 124)

s.add('theorem', 'thm-fundamental-algebra', 'Fundamental theorem of algebra', r'''Every nonconstant polynomial with complex coefficients has at least one root in $\C$.''', '4.12', 125)

s.note('remark-fundamental-algebra-faith', 'An analytic theorem accepted here', r'''We take the fundamental theorem of algebra on faith in this module. The book proves it using analytic facts about minima of continuous functions and complex roots in polar form; those prerequisites have not been developed here. All subsequent factorization arguments will explicitly use this accepted theorem.''', 125)

s.r('thm-complex-factorization', 'Unique factorization into complex linear factors', r'''Every nonzero polynomial $p\in\Poly(\C)$ of degree $m$ can be written
\[p(z)=c\prod_{j=1}^m(z-\lambda_j),\]
where $c\in\C\setminus\{0\}$ and $\lambda_j\in\C$. The scalar $c$ is the leading coefficient, and the list of roots, including repetitions, is unique up to rearrangement. For $m=0$, the product is empty and equals $1$.''',
r'''For existence, use induction on $m$. A nonzero constant is already the required scalar times an empty product. If $m\ge1$, the fundamental theorem of algebra gives a root $\lambda$. The factor-root theorem writes $p(z)=(z-\lambda)q(z)$ with $\deg q=m-1$. The induction hypothesis factors $q$, and adjoining $z-\lambda$ factors $p$. Since every displayed linear factor has leading coefficient $1$, the product-degree lemma shows that the scalar $c$ equals the leading coefficient of $p$.

For uniqueness, every such factorization has exactly $m$ factors by the product-degree lemma, and its scalar must equal this same leading coefficient. Cancel that nonzero scalar. If $m=0$, nothing remains to compare. For $m\ge1$, suppose
\[\prod_{j=1}^m(z-\lambda_j)=\prod_{j=1}^m(z-\mu_j).\]
At $z=\lambda_1$, the left side is zero. A finite product of nonzero complex scalars is nonzero, so some factor on the right must vanish; hence some $\mu_j=\lambda_1$. Rearrange the right factors to put this root first. Polynomial cancellation then removes the common nonzero factor $z-\lambda_1$. Induction applied to the remaining degree-$m-1$ factorizations identifies the remaining root lists up to rearrangement. Repeated roots are retained at each cancellation step, so the uniqueness includes their repetitions.''',
3, 35, [r'Repeatedly remove one root supplied by the fundamental theorem.', r'For uniqueness, evaluate one factorization at a root from the other and cancel the matching factor.'],
['thm-fundamental-algebra', 'thm-factor-root', 'lem-polynomial-product-degree', 'lem-polynomial-cancellation', 'c1-lem-scalar-cancellation', 'c1-foundations'], '4.13', 126)

s.d('def-root-multiplicity', 'Multiplicity of a complex root', r'''For a nonzero complex polynomial, the multiplicity of $\lambda\in\C$ is the number of occurrences of $\lambda$ in its unique linear-factor list. It is zero if $\lambda$ is absent. The zero polynomial is excluded from this definition.''', page=127)

s.d('def-conjugate-polynomial', 'Conjugating coefficients and extending real polynomials', r'''For $p(z)=\sum_{j=0}^m a_jz^j\in\Poly(\C)$, define
\[p^\#(z)=\sum_{j=0}^m\overline{a_j}z^j.\]
A polynomial originally defined on $\R$ is viewed on $\C$ by using the same real coefficients and allowing complex arguments. Coefficient uniqueness ensures that this extension does not depend on the chosen representation.''', page=127)

s.r('lem-conjugate-polynomial', 'Conjugation of polynomial coefficients', r'''For complex polynomials $p,q$,
\[p^\#(z)=\overline{p(\overline z)},\qquad
(pq)^\#=p^\#q^\#.\]
Moreover, $p^\#=p$ if and only if every coefficient of $p$ is real. An equality between real polynomial functions extends to the same equality between their complex extensions.''',
r'''Conjugation preserves finite sums and products, and repeated multiplication gives $\overline{(\overline z)^j}=z^j$ for every nonnegative integer $j$, including $j=0$. Thus
\[\overline{p(\overline z)}
=\sum_j\overline{a_j}\,\overline{(\overline z)^j}
=\sum_j\overline{a_j}z^j=p^\#(z).\]
Applying this identity to a product gives
\[(pq)^\#(z)=\overline{p(\overline z)q(\overline z)}
=p^\#(z)q^\#(z).\]
By coefficient uniqueness, $p^\#=p$ is equivalent to $\overline{a_j}=a_j$ for every $j$. The scalar conjugation criterion says this is equivalent to every $a_j$ being real. Finally, two equal real polynomial functions have equal coefficient lists by coefficient uniqueness over $\R$. Their complex extensions use those same lists, so they agree at every complex argument as well.''',
2, 20, [r'Conjugate the polynomial value at a conjugated argument.'],
['def-conjugate-polynomial', 'thm-complex-properties', 'c2-lem-polynomial-coefficients', 'lem-polynomial-product-degree'], page=127, kind='lemma')

s.r('thm-conjugate-roots', 'Real coefficients give conjugate roots with equal multiplicities', r'''If $p\in\Poly(\C)$ has real coefficients, then
\[p(\overline z)=\overline{p(z)}\quad(z\in\C).\]
Thus the conjugate of any root is a root. If $p\ne0$, a root and its conjugate have equal multiplicities.''',
r'''Real coefficients give $p^\#=p$. The conjugate-polynomial identity therefore gives $p(z)=\overline{p(\overline z)}$, and conjugating once more gives the stated formula. If $p(\lambda)=0$, the formula yields $p(\overline\lambda)=0$.

For multiplicities, let $p\ne0$ and write its complex factorization as
\[p(z)=c\prod_{j=1}^m(z-\lambda_j).\]
The leading coefficient $c$ is real. Conjugating coefficients, using the product rule for this operation, gives
\[p(z)=p^\#(z)=c\prod_{j=1}^m(z-\overline{\lambda_j}).\]
Uniqueness of complex factorization says that the original root list and its conjugated list have the same entries with the same repetition counts. The number of occurrences of any $\lambda$ in one list therefore equals the number of occurrences of $\overline\lambda$ in the original list. This proves equal multiplicities. The constant case has empty lists and no roots.''',
2, 20, [r'Conjugate the entire polynomial factorization, including its coefficients.'],
['def-conjugate-polynomial', 'lem-conjugate-polynomial', 'thm-complex-properties', 'thm-complex-factorization', 'def-root-multiplicity'], '4.14', 127)

s.r('lem-real-quotient', 'A quotient of real polynomial factors has real coefficients', r'''Suppose $p,s\in\Poly(\C)$ have real coefficients, $s\ne0$, and $p=sq$ for some $q\in\Poly(\C)$. Then $q$ has real coefficients.''',
r'''The real-coefficient criterion gives $p^\#=p$ and $s^\#=s$. Conjugating the equality $p=sq$ therefore gives $p=sq^\#$. Comparing with $p=sq$ and cancelling the nonzero polynomial $s$ yields $q^\#=q$. The same coefficient criterion now says that every coefficient of $q$ is real. This proof also covers $p=0$, in which case cancellation forces $q=0$.''',
2, 15, [r'Conjugate coefficients in the factorization and cancel the divisor.'],
['lem-conjugate-polynomial', 'lem-polynomial-cancellation'], page=128, kind='lemma')

s.r('thm-real-quadratic', 'When a real quadratic splits into real linear factors', r'''For $b,c\in\R$, the polynomial $x^2+bx+c$ is a product $(x-\lambda_1)(x-\lambda_2)$ with $\lambda_1,\lambda_2\in\R$ if and only if $b^2\ge4c$. If $b^2<4c$, it has no real root and cannot be a product of two real polynomials of positive degree.''',
r'''Completing the square gives
\[x^2+bx+c=(x+b/2)^2+c-b^2/4.\]
If $b^2<4c$, the second term is positive and the square is nonnegative, so the polynomial is positive for every real $x$. It has no real root and therefore cannot have a real linear factor. If it were the product of two positive-degree real polynomials, the product-degree formula would force both factors to have degree one. Each real degree-one polynomial has a real root, obtained by dividing the negative constant coefficient by its nonzero leading coefficient. Such a root would be a root of the quadratic, a contradiction.
If $b^2\ge4c$, let $d=\sqrt{b^2/4-c}$. This is real, and
\[x^2+bx+c=(x+b/2-d)(x+b/2+d).\]
These are the required real linear factors, including $d=0$, when they coincide. The two alternatives cover all possible discriminants and establish the equivalence.''',
2, 20, [r'Complete the square and distinguish the sign of its remaining constant term.'],
['c1-foundations', 'lem-polynomial-product-degree', 'def-polynomial-zero'], '4.15', 127)

s.r('thm-real-factorization', 'Unique real factorization into linear and quadratic factors', r'''Every nonzero real polynomial $p$ has a factorization
\[p(x)=c\prod_{j=1}^{m}(x-\lambda_j)
          \prod_{k=1}^{M}(x^2+b_kx+d_k),\]
where $c\in\R\setminus\{0\}$, all $\lambda_j,b_k,d_k$ are real, and $b_k^2<4d_k$ for every $k$. Here either product may be empty, $m+2M=\deg p$, and $c$ is the leading coefficient. The scalar and the factors, including their repetition counts, are unique except for the order of the factors.''',
r'''We first prove existence by induction on the degree $n$ of $p$. A nonzero constant gives the case $n=0$ with both products empty. For $n\ge1$, extend $p$ to complex arguments and choose a complex root $\lambda$ by the fundamental theorem of algebra.

If $\lambda$ is real, the factor-root theorem gives $p(z)=(z-\lambda)q(z)$ with $\deg q=n-1$. The divisor $z-\lambda$ has real coefficients, so the real-quotient lemma makes every coefficient of $q$ real. Apply the induction hypothesis to $q$ and append the factor $x-\lambda$.

If $\lambda$ is nonreal, its conjugate is a distinct root of $p$. First write $p(z)=(z-\lambda)q(z)$. Evaluation at $\overline\lambda$ gives
\[0=(\overline\lambda-\lambda)q(\overline\lambda).\]
The first factor is nonzero, so $q(\overline\lambda)=0$. The polynomial $q$ is nonzero and has a root, hence is not constant. Thus the factor-root theorem applies again and gives
\[p(z)=(z-\lambda)(z-\overline\lambda)r(z).\]
Writing $\lambda=a+bi$ with $b\ne0$, the paired factor is
\[(z-\lambda)(z-\overline\lambda)
=z^2-2az+(a^2+b^2).\]
It has real coefficients and discriminant $(-2a)^2-4(a^2+b^2)=-4b^2<0$. The real-quotient lemma makes the coefficients of $r$ real, and its degree is $n-2$. Apply induction to $r$ and append this quadratic factor. This completes existence. The product-degree formula shows $m+2M=n$ and identifies $c$ as the leading coefficient.

For uniqueness, take any factorization of the stated form and extend its equality to complex arguments. Each quadratic factor $x^2+bx+d$ with $b^2<4d$ can be written
\[(z-\zeta)(z-\overline\zeta),\qquad
\zeta=-b/2+\frac{i}{2}\sqrt{4d-b^2}.
\]
Indeed, $\zeta+\overline\zeta=-b$ and $\zeta\overline\zeta=b^2/4+(4d-b^2)/4=d$, which verifies the expansion. The imaginary part of $\zeta$ is strictly positive, while that of $\overline\zeta$ is strictly negative. Expanding every quadratic this way produces a complex linear factorization of $p$. Its scalar is forced to be the leading coefficient, and the multiset of its roots is forced by complex factorization uniqueness.

The real roots in that multiset can only come from the real linear factors, so these factors and their repetition counts are uniquely determined. For a nonreal root $\zeta$ with positive imaginary part, the only quadratic factor of the permitted form that can contain it is
\[z^2-2(\operatorname{Re}\zeta)z+|\zeta|^2,\]
because its other root must be $\overline\zeta$ by the displayed quadratic formula. Each occurrence of that quadratic contributes one occurrence of $\zeta$, and no different permitted quadratic contributes that root. Hence its repetition count is exactly the multiplicity of $\zeta$ in the complex factorization. This uniquely determines every quadratic factor and its count. Equal conjugate multiplicities ensure the positive- and negative-imaginary roots pair with the same counts, as also follows from the conjugate-root theorem. Thus no ambiguity remains except the order of factors.''',
4, 75, [r'For existence, remove a real root or a pair of conjugate nonreal roots.', r'Prove that the remaining quotient still has real coefficients.', r'For uniqueness, split each quadratic over $\C$ and distinguish its root with positive imaginary part.'],
['thm-fundamental-algebra', 'thm-factor-root', 'thm-conjugate-roots', 'lem-real-quotient', 'lem-conjugate-polynomial', 'thm-complex-factorization', 'thm-complex-properties', 'thm-real-quadratic', 'lem-polynomial-product-degree', 'def-root-multiplicity', 'c1-foundations', 'c1-lem-scalar-cancellation'], '4.16', 128)

s.card('conjugate-modulus', 'def-conjugate-modulus',
r'For $z=a+bi$, what are $\overline z$ and $|z|$?',
r'$\overline z=a-bi$ and $|z|=\sqrt{a^2+b^2}$.')

s.card('complex-triangle', 'thm-complex-properties',
r'What is the key estimate in the proof of the complex triangle inequality?',
r'After expanding $|w+z|^2$, bound $\operatorname{Re}(w\overline z)$ by $|w\overline z|=|w||z|$.')

s.card('factor-root', 'thm-factor-root',
r'How does a root of a positive-degree polynomial correspond to a factor?',
r'$p(\lambda)=0$ exactly when $p(z)=(z-\lambda)q(z)$ for a polynomial $q$ of degree $\deg p-1$.')

s.card('root-bound', 'thm-root-bound',
r'How many distinct roots can a nonzero degree-$m$ polynomial have?',
r'At most $m$.')

s.card('division-remainder', 'thm-polynomial-division',
r'State polynomial division with remainder.',
r'For $s\ne0$, there are unique $q,r$ with $p=sq+r$ and $\deg r<\deg s$.')

s.card('fundamental-algebra', 'thm-fundamental-algebra',
r'What does the fundamental theorem of algebra guarantee?',
r'Every nonconstant polynomial with complex coefficients has a complex root.')

s.card('complex-factorization', 'thm-complex-factorization',
r'What is uniquely determined in a complex linear factorization?',
r'The leading scalar and the list of roots with their repetition counts, up to rearrangement.')

s.card('conjugate-multiplicity', 'thm-conjugate-roots',
r'For a nonzero polynomial with real coefficients, how do the multiplicities of $\lambda$ and $\overline\lambda$ compare?',
r'They are equal.')

s.card('real-quadratic', 'thm-real-quadratic',
r'When does $x^2+bx+c$ split into real linear factors?',
r'Exactly when $b^2\ge4c$; if $b^2<4c$, it has no real root.')

s.card('real-factorization', 'thm-real-factorization',
r'Which factors occur in the unique real factorization of a nonzero polynomial?',
r'A nonzero real scalar, real linear factors, and real quadratic factors $x^2+bx+d$ with $b^2<4d$, with repetitions allowed.')

s.write()
