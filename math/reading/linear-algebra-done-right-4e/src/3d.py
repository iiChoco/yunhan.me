from common import Section

s = Section('3d')

s.p('intro-invertibility', 'Recovering inputs and changing coordinates', r'''An inverse recovers an input from its image. In finite dimensions, the dimension formula often proves that an inverse exists without constructing it explicitly. We then use invertible maps to compare vector spaces and to understand how matrices change when bases change.''', 82)

s.d('def-invertible-map', 'Invertible linear maps', r'''A map $T\in\Lin(V,W)$ is invertible if there is a linear map $S\in\Lin(W,V)$ with
\[ST=I_V,\qquad TS=I_W.\]
Such a map $S$ is called an inverse of $T$. The two identity maps act on different spaces when $V$ and $W$ differ.''', '3.59', 82)

s.r('thm-inverse-unique', 'Uniqueness of a linear inverse', r'''An invertible linear map has exactly one inverse.''',
r'''Existence is part of invertibility. Suppose $S,R:W\to V$ are both inverses of $T:V\to W$. Since $TR=I_W$ and $ST=I_V$, associativity and the identity laws give
\[S=S I_W=S(TR)=(ST)R=I_VR=R.\]
Thus any two inverses agree.''',
1, 10, [r'Compose one proposed inverse with the identity written using the other inverse.'],
['def-invertible-map', 'thm-composition-laws'], '3.60', 82)

s.d('def-map-inverse', 'Notation for the inverse map', r'''The unique inverse of an invertible map $T$ is written $T^{-1}$. For $T:V\to W$, it belongs to $\Lin(W,V)$ and satisfies $T^{-1}T=I_V$ and $TT^{-1}=I_W$.''', '3.61', 82)

s.r('ex-coordinate-inverse', 'Undoing a coordinate transformation', r'''The map $T:\R^3\to\R^3$ given by $T(x,y,z)=(-y,x,4z)$ is invertible, with
\[T^{-1}(x,y,z)=(y,-x,z/4).\]''',
r'''Each coordinate of $T$ is a fixed scalar combination of the input coordinates, so the coordinate characterization of linear maps makes $T$ linear. The same characterization makes $S(x,y,z)=(y,-x,z/4)$ linear. Direct substitution gives
\[S(T(x,y,z))=S(-y,x,4z)=(x,y,z)\]
and
\[T(S(x,y,z))=T(y,-x,z/4)=(x,y,z).\]
Thus $ST=TS=I_{\R^3}$, so $S$ is the inverse of $T$.''',
1, 10, [r'Check both compositions, not only one.'],
['thm-coordinate-linear-maps', 'def-invertible-map', 'def-map-inverse'], '3.62', 82, 'example')

s.r('thm-invertible-bijective', 'Invertibility is equivalent to bijectivity', r'''A linear map is invertible if and only if it is both injective and surjective.''',
r'''Suppose $T:V\to W$ has an inverse $S$. If $Tu=Tv$, applying $S$ gives $u=v$, so $T$ is injective. For every $w\in W$, the equality $w=T(Sw)$ gives a preimage, so $T$ is surjective.
Conversely, suppose $T$ is injective and surjective. For each $w\in W$, surjectivity supplies a preimage and injectivity makes that preimage unique. Define $Sw$ to be this unique vector. Then $TS=I_W$. Also $S(Tv)=v$, since $v$ is the unique preimage of $Tv$, giving $ST=I_V$.
It remains to check that $S$ is linear. For $w_1,w_2\in W$,
\[T(Sw_1+Sw_2)=w_1+w_2=T(S(w_1+w_2)).\]
Injectivity of $T$ gives $S(w_1+w_2)=Sw_1+Sw_2$. For $a\in\F$ and $w\in W$,
\[T(aSw)=aw=T(S(aw)),\]
so injectivity also gives $S(aw)=aSw$. Thus $S$ is a linear inverse, as required.''',
2, 20, [r'For the reverse direction, define the inverse by unique preimages.', r'Then use injectivity of the original map to prove that this inverse function is linear.'],
['def-invertible-map', 'def-injective', 'def-surjective', 'def-linear-map'], '3.63', 83)

s.r('ex-injective-not-invertible', 'Injectivity can fail to provide an inverse', r'''On $\Poly(\R)$, the linear map $Mp=x^2p$ is injective but not invertible.''',
r'''Linearity was proved for multiplication by a fixed polynomial. Suppose $Mp=0$, and write $p(x)=\sum_{j=0}^m a_jx^j$. Then $\sum_{j=0}^m a_jx^{j+2}$ is the zero polynomial. Uniqueness of polynomial coefficients gives all $a_j=0$, so $p=0$. The null-space criterion proves injectivity. Every polynomial of the form $x^2p$ has value zero at $x=0$, while the constant polynomial $1$ has value one there. Hence $1$ is not in the range, and $M$ is not surjective. The invertibility criterion therefore rules out an inverse.''',
2, 15, [r'Use coefficient uniqueness for injectivity and evaluation at zero for failure of surjectivity.'],
['ex-polynomial-multiplication', 'c2-lem-polynomial-coefficients', 'thm-injective-null', 'thm-invertible-bijective'], '3.64', 84, 'example')

s.r('ex-surjective-not-invertible', 'Surjectivity can fail to provide an inverse', r'''The backward shift $B:\F^\infty\to\F^\infty$, defined by
\[B(x_1,x_2,\ldots)=(x_2,x_3,\ldots),\]
is surjective but not invertible.''',
r'''The backward shift is linear by the earlier example. Given $y=(y_1,y_2,\ldots)$, the sequence $(0,y_1,y_2,\ldots)$ is a preimage of $y$, proving surjectivity. The nonzero sequence $(1,0,0,\ldots)$ and the zero sequence both have image zero. Thus $B$ is not injective and cannot be invertible.''',
1, 10, [r'Construct a preimage by inserting one new first entry.'],
['ex-backward-shift', 'def-injective', 'def-surjective', 'thm-invertible-bijective'], '3.64', 84, 'example')

s.r('thm-equal-dimension-invertibility', 'Equal dimensions make either condition sufficient', r'''Suppose $V,W$ are finite-dimensional, $\dim V=\dim W$, and $T\in\Lin(V,W)$. Then the following conditions are equivalent: $T$ is invertible; $T$ is injective; $T$ is surjective.''',
r'''Write $n=\dim V=\dim W$. Rank-nullity gives
\[n=\dim\Null T+\dim\Range T.\]
If $T$ is injective, its null space is $\{0\}$, so $\dim\Range T=n$. The range is a subspace of $W$ of the same dimension as $W$, hence equals $W$. Thus $T$ is surjective. Conversely, if $T$ is surjective, then $\dim\Range T=n$ and rank-nullity gives $\dim\Null T=0$. A zero-dimensional space is $\{0\}$, so $T$ is injective. The invertibility-bijectivity theorem now gives all three equivalences. These calculations include $n=0$.''',
2, 20, [r'Apply rank-nullity and compare the range dimension with the target dimension.'],
['thm-rank-nullity', 'thm-injective-null', 'thm-range-subspace', 'def-surjective', 'c2-thm-full-dimension-equality', 'c2-lem-zero-dimension', 'thm-invertible-bijective'], '3.65', 84)

s.r('ex-polynomial-second-derivative', 'Solving a polynomial second-derivative equation', r'''For every $q\in\Poly(\R)$, there is exactly one $p\in\Poly(\R)$ satisfying
\[\big((x^2+5x+7)p\big)''=q.\]''',
r'''Multiplication by $x^2+5x+7$ and polynomial differentiation are linear, so their composition
\[Tp=\big((x^2+5x+7)p\big)''\]
is linear on $\Poly(\R)$. If $p$ is nonzero of degree $k$ with leading coefficient $a_k\ne0$, the product $(x^2+5x+7)p$ has leading term $a_kx^{k+2}$: every other product term has smaller exponent. Applying the coefficient formula for differentiation twice gives leading term $(k+2)(k+1)a_kx^k$ in $Tp$. Its coefficient is nonzero because $(k+2)(k+1)$ is a positive real number. Thus $Tp$ has degree $k$, in particular $Tp\ne0$. Hence $T$ is injective on the entire polynomial space.
Choose a nonnegative integer $m$ with $q\in\Poly_m(\R)$. The same degree calculation, together with $T0=0$, shows that $T$ restricts to a linear map from $\Poly_m(\R)$ to itself. This restriction is injective, and its domain is finite-dimensional. Equal-dimension invertibility makes the restriction surjective, so there is a $p\in\Poly_m(\R)$ with $Tp=q$. Finally, injectivity of $T$ on the entire polynomial space proves uniqueness even among polynomials with no prescribed degree bound. If $q=0$, the same reasoning gives $p=0$.''',
3, 35, [r'Compute the highest-degree term of the image of a nonzero polynomial.', r'Work on a sufficiently large bounded-degree polynomial space before invoking finite-dimensional results.'],
['ex-polynomial-multiplication', 'ex-polynomial-differentiation', 'lem-composition-linear', 'c2-thm-polynomial-differentiation', 'c2-lem-polynomial-coefficients', 'c2-def-degree', 'c2-thm-bounded-polynomials', 'thm-injective-null', 'thm-linear-zero', 'thm-equal-dimension-invertibility'], '3.67', 85, 'example')

s.r('thm-one-sided-inverse', 'A one-sided inverse suffices in equal finite dimensions', r'''Suppose $V,W$ are finite-dimensional spaces of equal dimension, $T\in\Lin(V,W)$, and $S\in\Lin(W,V)$. Then
\[ST=I_V\quad\Longleftrightarrow\quad TS=I_W.\]''',
r'''Suppose $ST=I_V$. If $Tu=Tv$, applying $S$ gives $u=v$, so $T$ is injective. The equal-dimension theorem makes $T$ invertible. Composing $ST=I_V$ on the right with $T^{-1}$ gives
\[S=S(TT^{-1})=(ST)T^{-1}=T^{-1}.\]
Consequently $TS=I_W$. For the reverse implication, suppose $TS=I_W$. If $Sw_1=Sw_2$, applying $T$ gives $w_1=w_2$, so $S$ is injective. The same equal-dimension theorem makes $S$ invertible. Composing $TS=I_W$ on the right with $S^{-1}$ gives $T=S^{-1}$, hence $ST=I_V$.''',
2, 20, [r'A left inverse forces injectivity of the map to its right.'],
['def-injective', 'thm-equal-dimension-invertibility', 'def-map-inverse', 'thm-composition-laws'], '3.68', 85)

s.d('def-isomorphism', 'Isomorphisms of vector spaces', r'''An isomorphism is an invertible linear map. Two vector spaces over the same scalar field are isomorphic if an isomorphism exists from one to the other.''', '3.69', 86)

s.r('lem-isomorphism-basis', 'An isomorphism transports a basis', r'''Suppose $T:V\to W$ is an isomorphism and $v_1,\ldots,v_n$ is a basis of $V$. Then $Tv_1,\ldots,Tv_n$ is a basis of $W$. In particular, being isomorphic to a finite-dimensional space makes a vector space finite-dimensional.''',
r'''Given $w\in W$, surjectivity gives $v\in V$ with $Tv=w$. Expand $v=\sum a_jv_j$ and apply linearity to obtain $w=\sum a_jTv_j$, proving that the image list spans $W$. If $\sum b_jTv_j=0$, then $T(\sum b_jv_j)=0$. Injectivity and $T0=0$ give $\sum b_jv_j=0$, and independence of the original basis gives every $b_j=0$. Thus the image list is a basis. If $n=0$, then $V=\{0\}$ and surjectivity together with $T0=0$ gives $W=\{0\}$, so the empty image list is a basis. If instead the known finite-dimensional space is the target, apply the same result to the inverse isomorphism.''',
2, 20, [r'Use surjectivity for spanning and injectivity for independence.'],
['def-isomorphism', 'thm-invertible-bijective', 'def-map-inverse', 'def-linear-map', 'thm-linear-zero', 'c2-def-basis', 'c2-def-finite-dimensional'], page=86, kind='lemma')

s.r('thm-isomorphism-dimension', 'Dimension classifies finite-dimensional vector spaces', r'''Two finite-dimensional vector spaces over $\F$ are isomorphic if and only if they have the same dimension.''',
r'''If an isomorphism exists, it transports any basis of the first space to a basis of the second. The two bases have the same length, so the dimensions agree. Conversely, suppose both dimensions equal $n$, and choose bases $v_1,\ldots,v_n$ and $w_1,\ldots,w_n$. The basis-prescription theorem supplies a linear map $T$ with $Tv_j=w_j$. Every vector in the target is a combination of the $w_j$, so linearity shows it is the image of the same combination of the $v_j$; hence $T$ is surjective. If $T(\sum a_jv_j)=0$, then $\sum a_jw_j=0$, so all $a_j=0$. Thus its null space is $\{0\}$, making it injective. The invertibility criterion makes $T$ an isomorphism. When $n=0$, the prescribed map is the unique map between the two zero spaces, and the same empty-list argument applies.''',
2, 20, [r'Match one basis with the other.'],
['lem-isomorphism-basis', 'c2-thm-basis-existence', 'c2-def-dimension', 'thm-linear-map-basis', 'thm-injective-null', 'thm-invertible-bijective', 'def-isomorphism'], '3.70', 86)

s.r('ex-coordinate-isomorphism', 'Finite-dimensional spaces and coordinate models', r'''If $\dim V=n$, then $V$ is isomorphic to $\F^n$. In particular, $\Poly_m(\F)$ is isomorphic to $\F^{m+1}$ for every nonnegative integer $m$.''',
r'''The coordinate space $\F^n$ has dimension $n$, so the dimension classification supplies an isomorphism with $V$. The polynomial space $\Poly_m(\F)$ has dimension $m+1$, so applying the same result gives its isomorphism with $\F^{m+1}$. The first assertion includes $n=0$.''',
1, 10, [r'Compare dimensions with the standard coordinate and monomial bases.'],
['thm-isomorphism-dimension', 'c2-ex-coordinate-dimension', 'c2-ex-polynomial-dimension'], page=87, kind='example')

s.r('thm-map-matrix-isomorphism', 'The matrix representation is an isomorphism', r'''Fix a basis $\mathcal B=(v_1,\ldots,v_n)$ of $V$ and a basis $\mathcal C=(w_1,\ldots,w_m)$ of $W$. Then
\[\Mat:\Lin(V,W)\longrightarrow\F^{m,n},\qquad
T\longmapsto\Mat(T,\mathcal B,\mathcal C)\]
is an isomorphism.''',
r'''The matrix rules for sums and scalar multiples make this function linear. Suppose two maps $S,T$ have the same matrix. Their corresponding columns give the same $\mathcal C$ coefficients for $Sv_k$ and $Tv_k$, so these vectors agree for every $k$. A linear map is determined by its values on a basis, hence $S=T$. Thus the matrix representation is injective.
Given an arbitrary $A\in\F^{m,n}$, prescribe
\[Tv_k=\sum_{j=1}^m A_{jk}w_j\quad(1\le k\le n).\]
The basis-prescription theorem gives a linear map with exactly these values, and its matrix is $A$. Thus the representation is surjective and therefore invertible. If $n=0$, the prescribed list is empty and there is only the zero map from $V=\{0\}$; there is also only one $m$-by-$0$ matrix. If $m=0$, every prescribed image is the empty sum zero and there is only one $0$-by-$n$ matrix. The argument includes both cases.''',
2, 20, [r'For surjectivity, use the columns of an arbitrary matrix to prescribe the images of a basis.'],
['thm-linear-map-space', 'def-map-matrix', 'thm-matrix-addition', 'thm-matrix-scaling', 'thm-linear-map-basis', 'thm-invertible-bijective', 'def-isomorphism'], '3.71', 87)

s.r('thm-linear-map-dimension', 'The dimension of a space of linear maps', r'''If $V,W$ are finite-dimensional, then $\Lin(V,W)$ is finite-dimensional and
\[\dim\Lin(V,W)=(\dim V)(\dim W).\]''',
r'''Put $n=\dim V$ and $m=\dim W$, and choose bases. The matrix representation is an isomorphism from $\Lin(V,W)$ to $\F^{m,n}$. The matrix space has a basis of length $mn$. Applying the basis-transport lemma to the inverse isomorphism transports this finite basis to a basis of $\Lin(V,W)$. Thus that space is finite-dimensional, and its basis has length $mn$, proving the formula. When either $m$ or $n$ is zero, the matrix-space basis and its transported basis are empty, giving dimension zero.''',
2, 15, [r'Transport a basis of the matrix space back to the linear-map space.'],
['thm-map-matrix-isomorphism', 'thm-matrix-space-dimension', 'lem-isomorphism-basis', 'def-map-inverse', 'c2-def-dimension'], '3.72', 87)

s.d('def-vector-matrix', 'The coordinate column of a vector', r'''For a basis $\mathcal B=(v_1,\ldots,v_n)$ of $V$ and a vector $v=\sum_{j=1}^n b_jv_j$, define
\[\Mat(v,\mathcal B)=
\begin{pmatrix}b_1\\ \vdots\\ b_n\end{pmatrix}\in\F^{n,1}.\]
Uniqueness of basis coefficients makes this well-defined. When the basis is fixed, write simply $\Mat(v)$. If $n=0$, this is the unique $0$-by-$1$ column.''', '3.73', 88)

s.r('ex-vector-matrix', 'Reading coordinate columns', r'''With respect to the basis $1,x,x^2,x^3,x^4$ of $\Poly_4(\R)$, the coordinate column of $2-7x+5x^3+x^4$ is
\[\begin{pmatrix}2\\-7\\0\\5\\1\end{pmatrix}.\]
With respect to the standard basis of $\F^n$, the coordinate column of $(x_1,\ldots,x_n)$ has entries $x_1,\ldots,x_n$ in that order.''',
r'''The polynomial is $2\cdot1-7x+0x^2+5x^3+x^4$, so uniqueness of its basis expansion gives the first column. For the second assertion, the standard expansion is $(x_1,\ldots,x_n)=\sum_{j=1}^n x_je_j$. The definition of the coordinate column records these coefficients. For $n=0$, both the expansion and column have no entries.''',
1, 10, [r'Insert a zero coefficient for any omitted basis vector.'],
['def-vector-matrix', 'c2-thm-basis-coordinates', 'c2-ex-monomial-independent', 'c2-thm-bounded-polynomials', 'c2-ex-standard-spanning'], '3.74', 88, 'example')

s.r('thm-vector-matrix-isomorphism', 'Coordinates give an isomorphism', r'''For a fixed basis $\mathcal B$ of length $n$, the function
\[v\longmapsto\Mat(v,\mathcal B)\]
is an isomorphism from $V$ onto $\F^{n,1}$.''',
r'''If $u$ and $v$ have coefficient lists $(a_j)$ and $(b_j)$, then $u+v$ has coefficients $a_j+b_j$, and $cu$ has coefficients $ca_j$. These follow by expanding and using uniqueness of basis coefficients. Thus coordinate columns preserve addition and scalar multiplication. If two columns agree, the corresponding basis expansions agree, so the function is injective. Every column $(b_j)$ is the coordinate column of $\sum b_jv_j$, so it is surjective. The invertibility criterion makes it an isomorphism. Empty columns give the same bijection when $n=0$.''',
2, 15, [r'Build the preimage of an arbitrary column by taking its entries as basis coefficients.'],
['def-vector-matrix', 'c2-thm-basis-coordinates', 'thm-invertible-bijective', 'def-isomorphism'], page=88)

s.r('thm-matrix-columns', 'Columns are coordinate columns of basis images', r'''Fix bases $\mathcal B=(v_1,\ldots,v_n)$ of $V$ and $\mathcal C$ of $W$. For $T\in\Lin(V,W)$ and $1\le k\le n$, the $k$th column of $\Mat(T,\mathcal B,\mathcal C)$ is $\Mat(Tv_k,\mathcal C)$.''',
r'''By definition, the entries in column $k$ of the matrix of $T$ are the coefficients expressing $Tv_k$ in the basis $\mathcal C$. By the definition of a vector's coordinate column, these same coefficients, in the same order, form $\Mat(Tv_k,\mathcal C)$. Hence the columns agree.''',
1, 10, [r'Compare the two definitions of the entries.'],
['def-map-matrix', 'def-vector-matrix'], '3.75', 89)

s.r('thm-matrix-action', 'Applying a map is matrix multiplication in coordinates', r'''For fixed bases $\mathcal B$ of $V$ and $\mathcal C$ of $W$, every $T\in\Lin(V,W)$ and $v\in V$ satisfy
\[\Mat(Tv,\mathcal C)=\Mat(T,\mathcal B,\mathcal C)\Mat(v,\mathcal B).\]''',
r'''Write $v=\sum_{k=1}^n b_kv_k$ and put $A=\Mat(T,\mathcal B,\mathcal C)$. Linearity of $T$ gives $Tv=\sum b_kTv_k$. The coordinate map is linear, so
\[\Mat(Tv,\mathcal C)=\sum_{k=1}^n b_k\Mat(Tv_k,\mathcal C)
=\sum_{k=1}^n b_k A_{\cdot,k}.\]
The column-combination formula for matrix multiplication identifies the last sum with $A\Mat(v,\mathcal B)$. If $n=0$, then $v=0$ and $Tv=0$; both sides are the zero column, with the matrix product given by empty sums. If the target dimension is zero, both sides are the unique empty column.''',
2, 15, [r'Expand the input in its basis and compare the resulting linear combination of columns.'],
['def-vector-matrix', 'thm-vector-matrix-isomorphism', 'thm-matrix-columns', 'thm-column-combination', 'def-linear-map', 'thm-linear-zero'], '3.76', 89)

s.r('thm-range-matrix-rank', 'Range dimension equals matrix rank', r'''For finite-dimensional $V,W$ and $T\in\Lin(V,W)$, the dimension of $\Range T$ equals the column rank, and hence the rank, of any matrix representing $T$.''',
r'''Choose bases $\mathcal B$ of $V$ and $\mathcal C$ of $W$, and put $A=\Mat(T,\mathcal B,\mathcal C)$. By the matrix-action theorem, the coordinate column of every vector in $\Range T$ is a linear combination of the columns of $A$. Conversely, for any scalars $b_1,\ldots,b_n$, that column combination is the coordinate column of $T(\sum b_kv_k)$. Therefore the coordinate isomorphism maps $\Range T$ onto the column span of $A$. Its restriction is linear and injective and has precisely that span as its target range, so the invertibility criterion makes the restriction an isomorphism. Both spaces are finite-dimensional subspaces, and isomorphic finite-dimensional spaces have equal dimensions. The dimension of the column span is the column rank by definition; equality of row and column rank identifies it with the rank. The argument also includes empty column lists and zero-dimensional ranges.''',
2, 20, [r'Restrict the coordinate isomorphism to the range of the map.'],
['thm-matrix-action', 'thm-vector-matrix-isomorphism', 'thm-range-subspace', 'thm-invertible-bijective', 'thm-isomorphism-dimension', 'def-row-column-rank', 'thm-row-column-rank', 'def-rank', 'c2-thm-span-smallest', 'c2-thm-subspaces-finite'], '3.78', 90)

s.note('remark-basis-labels', 'Displaying the bases explicitly', r'''We write $\Mat(T,\mathcal B,\mathcal C)$ with the domain basis first and the target basis second. For an operator on one space, $\Mat(T,\mathcal B)$ abbreviates $\Mat(T,\mathcal B,\mathcal B)$. Keeping both labels visible is useful when an identity map converts one coordinate system to another.''', 90)

s.d('def-identity-matrix', 'Identity matrices', r'''For $n\ge0$, the identity matrix $I_n\in\F^{n,n}$ has entry $1$ when its row and column indices agree and entry $0$ otherwise. For $n=0$, this is the unique empty square matrix. We may write $I$ when its size is determined by context.''', '3.79', 90)

s.r('lem-identity-matrix-laws', 'Identity matrices act as identities', r'''For every $A\in\F^{m,n}$,
\[I_mA=A,\qquad AI_n=A.\]
If $\mathcal B$ is a basis of length $n$ of $V$, then $\Mat(I_V,\mathcal B)=I_n$.''',
r'''For an entry with indices $j,k$, the matrix product formula gives
\[(I_mA)_{jk}=\sum_{\ell=1}^m(I_m)_{j\ell}A_{\ell k}=A_{jk},\]
because the only nonzero coefficient from the identity row has $\ell=j$. Similarly,
\[(AI_n)_{jk}=\sum_{\ell=1}^n A_{j\ell}(I_n)_{\ell k}=A_{jk},\]
because only $\ell=k$ contributes. If either dimension is zero, the matrices in the relevant equality have no entries, so equality still holds. Finally, $I_Vv_k=v_k$ has coefficient $1$ at position $k$ and zero at all other basis positions. These coefficient columns form $I_n$, proving the last assertion, including the empty-basis case.''',
1, 10, [r'In each entry formula, at most one summand can be nonzero.'],
['def-identity-matrix', 'def-matrix-product', 'def-map-matrix', 'def-zero-identity-maps'], page=91, kind='lemma')

s.d('def-invertible-matrix', 'Invertible square matrices', r'''A square matrix $A\in\F^{n,n}$ is invertible if some $B\in\F^{n,n}$ satisfies
\[AB=BA=I_n.\]
Such a matrix $B$ is an inverse of $A$. The next result proves uniqueness, after which we denote it by $A^{-1}$.''', '3.80', 91)

s.r('lem-matrix-inverse-laws', 'Uniqueness and product rules for matrix inverses', r'''A square matrix has at most one inverse. For invertible square matrices of compatible equal size,
\[(A^{-1})^{-1}=A,\qquad (AC)^{-1}=C^{-1}A^{-1}.\]
The identity matrix is invertible, including $I_0$.''',
r'''If $B,D$ are inverses of $A$, associativity and the identity laws give
\[B=B(AD)=(BA)D=D.\]
Thus the inverse is unique. The two equalities $AA^{-1}=A^{-1}A=I$ show that $A$ is an inverse of $A^{-1}$, proving the first formula. For the second,
\[(AC)(C^{-1}A^{-1})=A(CC^{-1})A^{-1}=AA^{-1}=I,\]
and
\[(C^{-1}A^{-1})(AC)=C^{-1}(A^{-1}A)C=C^{-1}C=I.\]
Thus $C^{-1}A^{-1}$ is the inverse of $AC$. Finally, $II=I$, so $I$ is its own inverse. For size zero, the unique empty matrix is $I_0$ and all these products are the unique empty matrix, so the same conclusions hold.''',
2, 20, [r'Keep the order of the factors when undoing a product.'],
['def-invertible-matrix', 'lem-identity-matrix-laws', 'lem-matrix-product-laws'], page=91, kind='lemma')

s.r('thm-matrix-composition-bases', 'Composition with all basis choices displayed', r'''Let $T:U\to V$ and $S:V\to W$ be linear maps, and fix bases $\mathcal A,\mathcal B,\mathcal C$ of the respective finite-dimensional spaces. Then
\[\Mat(ST,\mathcal A,\mathcal C)
=\Mat(S,\mathcal B,\mathcal C)\Mat(T,\mathcal A,\mathcal B).\]''',
r'''Write $P=\Mat(T,\mathcal A,\mathcal B)$ and $Q=\Mat(S,\mathcal B,\mathcal C)$. If $\mathcal A=(u_1,\ldots,u_m)$, $\mathcal B=(v_1,\ldots,v_n)$, and $\mathcal C=(w_1,\ldots,w_p)$, then
\[Tu_k=\sum_{j=1}^n P_{jk}v_j,\qquad Sv_j=\sum_{\ell=1}^p Q_{\ell j}w_\ell.\]
Linearity gives
\[STu_k=\sum_{\ell=1}^p\left(\sum_{j=1}^n Q_{\ell j}P_{jk}\right)w_\ell.\]
Hence entry $(\ell,k)$ of the matrix of $ST$ is $\sum_jQ_{\ell j}P_{jk}$, which is entry $(\ell,k)$ of $QP$. This proves the formula. If the middle basis is empty, both inner sums are empty sums zero; if either outer basis is empty, there are no corresponding matrix entries to check. Thus zero-dimensional cases are included.''',
2, 15, [r'Expand the image of a domain basis vector twice, using the intermediate basis.'],
['def-map-matrix', 'def-matrix-product', 'def-linear-map', 'def-map-composition', 'thm-linear-zero'], '3.81', 91)

s.r('thm-basis-transition-inverse', 'Opposite coordinate changes are inverse matrices', r'''For two bases $\mathcal B,\mathcal C$ of a finite-dimensional space $V$, the matrices
\[P=\Mat(I_V,\mathcal B,\mathcal C),\qquad
Q=\Mat(I_V,\mathcal C,\mathcal B)\]
are invertible and satisfy $P^{-1}=Q$.''',
r'''Apply the composition formula to $I_VI_V=I_V$, starting in basis $\mathcal B$, using $\mathcal C$ as the intermediate basis, and ending in $\mathcal B$. It gives
\[QP=\Mat(I_V,\mathcal B)=I_n.\]
Starting and ending in $\mathcal C$ instead gives $PQ=I_n$. By the definition of a matrix inverse, $P$ and $Q$ are inverses of one another. For $n=0$, both matrices are $I_0$ and the same equations hold.''',
1, 10, [r'Compose the two identity maps while keeping their coordinate systems distinct.'],
['thm-matrix-composition-bases', 'lem-identity-matrix-laws', 'def-invertible-matrix', 'lem-matrix-inverse-laws'], '3.82', 92)

s.r('ex-basis-transition', 'A concrete transition matrix and its inverse', r'''Let $\mathcal B=((4,2),(5,3))$ and let $\mathcal E=((1,0),(0,1))$. Prove that $\mathcal B$ is a basis of $\F^2$ and that
\[
\Mat(I,\mathcal B,\mathcal E)=
\begin{pmatrix}4&5\\2&3\end{pmatrix},\qquad
\Mat(I,\mathcal E,\mathcal B)=
\begin{pmatrix}3/2&-5/2\\-1&2\end{pmatrix}.
\]''',
r'''A relation $a(4,2)+b(5,3)=0$ gives $4a+5b=0$ and $2a+3b=0$. Twice the second equation minus the first gives $b=0$, and then $a=0$. Thus the two-vector list is independent and is a basis of the two-dimensional space $\F^2$. Its vectors already have standard coordinates $(4,2)$ and $(5,3)$, giving the first matrix, call it $P$. Let $Q$ be the second displayed matrix. Direct multiplication gives
\[
PQ=\begin{pmatrix}6-5&-10+10\\3-3&-5+6\end{pmatrix}=I_2,
\qquad
QP=\begin{pmatrix}6-5&15/2-15/2\\-4+4&-5+6\end{pmatrix}=I_2.
\]
Thus $Q=P^{-1}$. Opposite transition matrices are inverses, so uniqueness of the inverse identifies $Q$ with $\Mat(I,\mathcal E,\mathcal B)$.''',
2, 20, [r'The columns of the first matrix are the new basis vectors written in standard coordinates.'],
['def-map-matrix', 'thm-basis-transition-inverse', 'lem-matrix-inverse-laws', 'c2-ex-coordinate-dimension', 'c2-thm-full-length-independent', 'def-matrix-product'], '3.83', 92, 'example')

s.r('thm-change-basis', 'Changing the basis of an operator', r'''Suppose $T\in\Lin(V)$ and $\mathcal B,\mathcal C$ are bases of the finite-dimensional space $V$. Set
\[A=\Mat(T,\mathcal B),\qquad B=\Mat(T,\mathcal C),\qquad
P=\Mat(I_V,\mathcal B,\mathcal C).\]
Then
\[A=P^{-1}BP.\]''',
r'''Let $D=\Mat(T,\mathcal B,\mathcal C)$. The composition $TI_V$, with the identity converting $\mathcal B$ coordinates into $\mathcal C$ coordinates before $T$ is applied, gives
\[D=\Mat(T,\mathcal C,\mathcal C)\Mat(I_V,\mathcal B,\mathcal C)=BP.\]
The composition $I_VT$, now ending in basis $\mathcal B$, gives
\[A=\Mat(I_V,\mathcal C,\mathcal B)\Mat(T,\mathcal B,\mathcal C)=P^{-1}D,\]
where the transition-inverse theorem supplies the inverse matrix. Substituting $D=BP$ yields $A=P^{-1}BP$. The composition and transition theorems include zero-dimensional spaces, so no separate nonzero-dimension assumption is needed.''',
3, 30, [r'Introduce the matrix of $T$ whose domain and target use different bases.', r'Factor that mixed-basis matrix through an identity map.'],
['thm-matrix-composition-bases', 'thm-basis-transition-inverse'], '3.84', 93)

s.r('thm-matrix-inverse', 'The matrix of an inverse is the inverse matrix', r'''Suppose $T\in\Lin(V)$ is invertible and $\mathcal B$ is a basis of the finite-dimensional space $V$. Then
\[\Mat(T^{-1},\mathcal B)=\big(\Mat(T,\mathcal B)\big)^{-1}.\]''',
r'''Write $A=\Mat(T,\mathcal B)$ and $B=\Mat(T^{-1},\mathcal B)$. The equalities $T^{-1}T=I_V$ and $TT^{-1}=I_V$, together with the matrix composition formula, give
\[BA=\Mat(I_V,\mathcal B)=I_n,\qquad
AB=\Mat(I_V,\mathcal B)=I_n.\]
Thus $A$ is invertible and $B$ is its inverse. Uniqueness of a matrix inverse yields the claimed formula, including $n=0$.''',
1, 10, [r'Take matrices of both inverse identities.'],
['def-map-inverse', 'thm-matrix-composition-bases', 'lem-identity-matrix-laws', 'def-invertible-matrix', 'lem-matrix-inverse-laws'], '3.86', 93)

s.card('inverse-definition', 'def-invertible-map',
r'What two identities define an inverse of $T:V\to W$?',
r'$T^{-1}T=I_V$ and $TT^{-1}=I_W$.')

s.card('inverse-linearity', 'thm-invertible-bijective',
r'How do you prove that the inverse function of a bijective linear map is linear?',
r'Apply the original map to the desired additivity and homogeneity identities, then use its injectivity.')

s.card('equal-dimension-inverse', 'thm-equal-dimension-invertibility',
r'When does injectivity alone imply invertibility of a linear map $V\to W$?',
r'When $V,W$ are finite-dimensional and have equal dimension.')

s.card('infinite-dimensional-inverse', 'ex-injective-not-invertible',
r'Give an injective operator that is not invertible.',
r'On $\Poly(\R)$, multiplication by $x^2$ is injective but cannot produce the constant polynomial $1$.')

s.card('isomorphism-dimension', 'thm-isomorphism-dimension',
r'When are two finite-dimensional vector spaces over the same field isomorphic?',
r'Exactly when they have the same dimension.')

s.card('linear-map-dimension', 'thm-linear-map-dimension',
r'What is $\dim\Lin(V,W)$ for finite-dimensional $V,W$?',
r'$(\dim V)(\dim W)$.')

s.card('matrix-action', 'thm-matrix-action',
r'How are the coordinate columns of $v$ and $Tv$ related?',
r'$\Mat(Tv,\mathcal C)=\Mat(T,\mathcal B,\mathcal C)\Mat(v,\mathcal B)$.')

s.card('rank-range', 'thm-range-matrix-rank',
r'Why is the rank of a representing matrix independent of the chosen bases?',
r'It equals $\dim\Range T$, which does not involve a basis choice.')

s.card('change-basis-direction', 'thm-change-basis',
r'If $P=\Mat(I,\mathcal B,\mathcal C)$, how are $A=\Mat(T,\mathcal B)$ and $B=\Mat(T,\mathcal C)$ related?',
r'$A=P^{-1}BP$; the matrix $P$ converts $\mathcal B$ coordinates to $\mathcal C$ coordinates.')

s.card('matrix-inverse-order', 'lem-matrix-inverse-laws',
r'What is the inverse of a product of two invertible matrices?',
r'$(AC)^{-1}=C^{-1}A^{-1}$.')

s.write()
