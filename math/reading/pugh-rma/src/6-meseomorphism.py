from __future__ import annotations

import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from c6common import prose, note, result, card, write

B = []

B.append(prose("c6-mes-intro", r"""
Topology studies homeomorphisms, the bijections that preserve open sets in both directions, and isometries, which also preserve distance. Measure theory has the analogous notions: a \emph{meseomorphism} preserves measurability in both directions, and a \emph{meseometry} preserves measure as well. This section finds out how the basic maps of $\R^n$ behave: translations and rigid motions preserve measure, a linear map multiplies it by the absolute value of its determinant, and a Lipschitz map cannot inflate a zero set. Throughout, $TA = \set{Tx : x \in A}$ denotes the image of a set.
"""))

B.append(note("definition", "c6-def-meseomorphism", "Meseomorphism and meseometry", r"""
A bijection $T : \R^n \to \R^n$ is a \emph{meseomorphism} if $TE$ and $T^{-1}E$ are measurable whenever $E \subseteq \R^n$ is measurable. It is a \emph{meseometry} if, in addition, $m(TE) = mE$ for every measurable $E$ (and then also $m(T^{-1}E) = mE$).
"""))

B.append(prose("c6-mes-principle-prose", r"""
Two general principles do most of the work. The first says that to bound the outer measure of images it is enough to look at images of boxes. The second says that a bijection that rescales \emph{outer} measure by a constant factor automatically respects Carathéodory's condition.
"""))

B.append(result("lemma", "c6-lem-box-principle", "It is enough to test boxes", r"""
Let $T : \R^n \to \R^n$ be any map and let $c > 0$. Suppose $m^*(TB) \le c\,\abs{B}$ for every open box $B \subseteq \R^n$. Then $m^*(TA) \le c\, m^*A$ for every $A \subseteq \R^n$.
""", r"""
If $m^*A = \infty$ there is nothing to prove. Otherwise let $\eps > 0$ and choose open boxes $B_1, B_2, \dots$ covering $A$ with $\sum_k \abs{B_k} \le m^*A + \eps$. Then $TA \subseteq \bigcup_k TB_k$, so by monotonicity and countable subadditivity
\[ m^*(TA) \le \sum_k m^*(TB_k) \le c \sum_k \abs{B_k} \le c\,(m^*A + \eps). \]
Since $\eps > 0$ is arbitrary, $m^*(TA) \le c\, m^*A$.
""", 2, 15, [
    r"Push an almost optimal covering of $A$ forward by $T$.",
], ["c6-def-outer-measure", "c6-prop-outer-basic", "c6-thm-countable-subadditivity"]))

B.append(result("lemma", "c6-lem-outer-scaling", "Scaling outer measure forces measurability", r"""
Let $T : \R^n \to \R^n$ be a bijection and let $c > 0$. Suppose $m^*(TA) = c\, m^*A$ for every $A \subseteq \R^n$. Then $T$ is a meseomorphism, and $m(TE) = c\, mE$ for every measurable $E$. If $c = 1$, $T$ is a meseometry.
""", r"""
Let $E$ be measurable and let $X \subseteq \R^n$ be a test set. Because $T$ is a bijection, $T(E^c) = (TE)^c$, and
\[ X \cap TE = T\bigl( T^{-1}X \cap E \bigr), \qquad X \cap (TE)^c = T\bigl( T^{-1}X \cap E^c \bigr). \]
By the hypothesis (used three times) and the measurability of $E$ with the test set $T^{-1}X$,
\[ m^*(X \cap TE) + m^*(X \cap (TE)^c) = c\,\bigl[ m^*(T^{-1}X \cap E) + m^*(T^{-1}X \cap E^c) \bigr] = c\, m^*(T^{-1}X) = m^*(T\,T^{-1}X) = m^*X. \]
So $TE$ is measurable, and $m(TE) = m^*(TE) = c\,m^*E = c\,mE$.

The inverse satisfies the same kind of hypothesis: for any $A$, applying the assumption to $T^{-1}A$ gives $m^*A = c\,m^*(T^{-1}A)$, that is, $m^*(T^{-1}A) = c^{-1} m^*A$. By what was just proved (with $T^{-1}$ and $c^{-1}$), $T^{-1}E$ is measurable whenever $E$ is. Hence $T$ is a meseomorphism, and a meseometry when $c = 1$.
""", 3, 25, [
    r"To test $TE$ against a set $X$, pull $X$ back: use $T^{-1}X$ as a test set for $E$.",
    r"$X \cap TE = T(T^{-1}X \cap E)$ and $X \cap (TE)^c = T(T^{-1}X \cap E^c)$ because $T$ is a bijection. Then check that $T^{-1}$ satisfies the same hypothesis with $1/c$.",
], ["c6-def-meseomorphism", "c6-def-measurable"]))

B.append(result("theorem", "c6-thm-translation", "Translations are meseometries", r"""
For $v \in \R^n$ let $\tau_v(x) = x + v$. Then $m^*(A + v) = m^*A$ for every $A \subseteq \R^n$, where $A + v = \tau_v A$, and $\tau_v$ is a meseometry.
""", r"""
If $B = \prod_i (a_i, b_i)$ is an open box, then $\tau_v B = \prod_i (a_i + v_i, b_i + v_i)$ is an open box with the same side lengths, so $m^*(\tau_v B) = \abs{\tau_v B} = \abs{B}$. Since it is enough to test boxes (with $c = 1$), $m^*(\tau_v A) \le m^*A$ for every $A$ and every $v$. Applying this to the set $\tau_v A$ and the vector $-v$,
\[ m^*A = m^*(\tau_{-v} \tau_v A) \le m^*(\tau_v A) \le m^*A. \]
So $m^*(\tau_v A) = m^*A$ for all $A$. As $\tau_v$ is a bijection, the lemma that scaling outer measure forces measurability (with $c = 1$) shows it is a meseometry.
""", 2, 15, [
    r"A translate of a box is a box of the same volume. That gives one inequality for all sets.",
    r"Get the reverse inequality by translating back with $-v$.",
], ["c6-lem-box-principle", "c6-lem-outer-scaling", "c6-thm-box-measure"]))

B.append(result("theorem", "c6-thm-diagonal", "Diagonal maps and coordinate permutations", r"""
(a) Let $\lambda_1, \dots, \lambda_n$ be nonzero real numbers and $D(x_1, \dots, x_n) = (\lambda_1 x_1, \dots, \lambda_n x_n)$. Then $m^*(DA) = \abs{\lambda_1 \cdots \lambda_n}\, m^*A$ for every $A \subseteq \R^n$, and $D$ is a meseomorphism. In particular the dilation $x \mapsto \lambda x$ ($\lambda \neq 0$) multiplies outer measure by $\abs{\lambda}^n$.

(b) Let $\pi$ be a permutation of $\set{1, \dots, n}$ and $P(x_1, \dots, x_n) = (x_{\pi(1)}, \dots, x_{\pi(n)})$. Then $m^*(PA) = m^*A$ for every $A$, and $P$ is a meseometry.
""", r"""
(a) Put $\Lambda = \abs{\lambda_1 \cdots \lambda_n} > 0$. If $B = \prod_i (a_i, b_i)$ is an open box, then $DB = \prod_i J_i$ where $J_i = (\lambda_i a_i, \lambda_i b_i)$ if $\lambda_i > 0$ and $J_i = (\lambda_i b_i, \lambda_i a_i)$ if $\lambda_i < 0$. In either case $\abs{J_i} = \abs{\lambda_i}(b_i - a_i)$, so $DB$ is an open box with $m^*(DB) = \abs{DB} = \Lambda \abs{B}$. Since it is enough to test boxes, $m^*(DA) \le \Lambda\, m^*A$ for all $A$. The inverse $D^{-1}$ is the diagonal map with factors $1/\lambda_i$, so likewise $m^*(D^{-1}A') \le \Lambda^{-1} m^*A'$ for all $A'$; with $A' = DA$ this reads $m^*A \le \Lambda^{-1} m^*(DA)$. Hence $m^*(DA) = \Lambda\, m^*A$. Since $D$ is a bijection, scaling outer measure forces measurability, and $D$ is a meseomorphism.

(b) $P$ carries the open box $I_1 \times \dots \times I_n$ onto the open box $I_{\pi(1)} \times \dots \times I_{\pi(n)}$, which has the same volume. As in the proof for translations, testing boxes gives $m^*(PA) \le m^*A$ for all $A$; $P^{-1}$ is again a coordinate permutation, so $m^*A = m^*(P^{-1}PA) \le m^*(PA)$. Thus $m^*(PA) = m^*A$, and $P$ is a meseometry by the lemma on scaling outer measure.
""", 2, 20, [
    r"What does the map do to an open box, and to its volume?",
    r"Get $\le$ from boxes, and $\ge$ by applying the same reasoning to the inverse map, which is of the same type.",
], ["c6-lem-box-principle", "c6-lem-outer-scaling", "c6-thm-box-measure"]))

B.append(prose("c6-mes-shear-prose", r"""
The remaining building block of linear algebra is the shear, which slides each horizontal slice of a box sideways by an amount proportional to its height. A sheared box is a parallelepiped, not a box, but thin slices of it are nearly boxes.
"""))

B.append(result("lemma", "c6-lem-shear", "Shears preserve outer measure", r"""
Let $n \ge 2$, let $i \ne j$ be indices in $\set{1, \dots, n}$, and let $\sigma \in \R$. Define the \emph{shear} $S : \R^n \to \R^n$ by $(Sx)_i = x_i + \sigma x_j$ and $(Sx)_k = x_k$ for $k \ne i$. Then $m^*(SA) = m^*A$ for every $A \subseteq \R^n$, and $S$ is a meseometry.
""", r"""
\emph{Step 1: $m^*(SB) \le \abs{B}$ for every open box $B$.} Let $B = \prod_k (a_k, b_k)$. If $B$ is empty the claim is trivial, so assume $a_k < b_k$ for all $k$. Put $\ell = b_j - a_j$ and let $N \in \N$. For $r = 1, \dots, N$ let $t_r = a_j + (r-1)\ell/N$ and
\[ J_r = (a_j, b_j) \cap [t_r, t_r + \ell/N], \]
an interval of length $\ell/N$; these intervals cover $(a_j, b_j)$. Let $B_r = \set{x \in B : x_j \in J_r}$, so $B = B_1 \cup \dots \cup B_N$.

Fix $r$ and $x \in B_r$. Then $\abs{x_j - t_r} \le \ell/N$, so $\abs{\sigma x_j - \sigma t_r} \le \abs{\sigma}\ell/N$, and since $a_i < x_i < b_i$,
\[ (Sx)_i = x_i + \sigma x_j \in I_r' := \bigl( a_i + \sigma t_r - \abs{\sigma}\ell/N,\; b_i + \sigma t_r + \abs{\sigma}\ell/N \bigr). \]
The other coordinates of $Sx$ are those of $x$. Hence $SB_r$ is contained in the box $B_r'$ whose $i$-th interval is $I_r'$, whose $j$-th interval is $J_r$, and whose $k$-th interval is $(a_k, b_k)$ for $k \ne i, j$. With $V = \prod_{k \ne i,j} (b_k - a_k)$ (an empty product is $1$),
\[ \abs{B_r'} = \Bigl( b_i - a_i + \frac{2\abs{\sigma}\ell}{N} \Bigr) \cdot \frac{\ell}{N} \cdot V. \]
Since $SB \subseteq B_1' \cup \dots \cup B_N'$ and any boxes may be used in coverings,
\[ m^*(SB) \le \sum_{r=1}^N \abs{B_r'} = \Bigl( b_i - a_i + \frac{2\abs{\sigma}\ell}{N} \Bigr) \ell\, V = \abs{B} + \frac{2\abs{\sigma}\ell^2 V}{N}. \]
Letting $N \to \infty$ gives $m^*(SB) \le \abs{B}$.

\emph{Step 2.} Since it is enough to test boxes, $m^*(SA) \le m^*A$ for every $A$. The inverse of $S$ is the shear with $-\sigma$ in place of $\sigma$, so the same holds for $S^{-1}$: $m^*A = m^*(S^{-1}SA) \le m^*(SA)$. Hence $m^*(SA) = m^*A$, and as $S$ is a bijection, the lemma on scaling outer measure shows $S$ is a meseometry.
""", 4, 60, [
    r"By the box principle it suffices to show $m^*(SB) \le \abs{B}$ for an open box $B$; the reverse inequality comes from the inverse shear.",
    r"Slice $B$ into $N$ thin slabs according to the value of $x_j$. On one slab $\sigma x_j$ varies by at most $\abs{\sigma}\ell/N$, so the sheared slab fits in a box only slightly longer in the $i$-th direction.",
    r"Add up the volumes of the $N$ enclosing boxes: you get $\abs{B}$ plus an error of order $1/N$.",
], ["c6-lem-box-principle", "c6-lem-outer-scaling", "c6-cor-any-boxes"]))

B.append(prose("c6-mes-linear-prose", r"""
From linear algebra we borrow two standard facts: every invertible $n \times n$ matrix is a product of \emph{elementary matrices} (those that swap two coordinates, multiply one coordinate by a nonzero scalar, or add a multiple of one coordinate to another), and $\det(ST) = \det S \cdot \det T$. In the next theorem the convention $0 \cdot \infty = 0$ is in force.
"""))

B.append(result("theorem", "c6-thm-linear", "Linear maps scale measure by the determinant", r"""
Let $T : \R^n \to \R^n$ be linear. Then for every $A \subseteq \R^n$,
\[ m^*(TA) = \abs{\det T}\; m^*A . \]
If $E$ is measurable then $TE$ is measurable and $m(TE) = \abs{\det T}\, mE$. If $T$ is invertible, it is a meseomorphism.

Here $0 \cdot \infty = 0$ (this matters only when $\det T = 0$). You may assume the standard facts of linear algebra: every invertible matrix is a product of elementary matrices (coordinate swaps, multiplication of one coordinate by a nonzero scalar, addition of a multiple of one coordinate to another); $\det(ST) = \det S \cdot \det T$; a linear map with $\det T = 0$ has range of dimension less than $n$; and a linearly independent set extends to a basis.
""", r"""
\emph{Invertible $T$.} Write $T = E_1 E_2 \cdots E_r$ as a product of elementary matrices. Each $E_s$ is of one of three kinds. A swap of two coordinates is a coordinate permutation, has $\abs{\det} = 1$, and preserves outer measure. Multiplication of one coordinate by $\lambda \ne 0$ is a diagonal map with $\abs{\det} = \abs{\lambda}$, and multiplies outer measure by $\abs{\lambda}$. Adding $\sigma$ times the $j$-th coordinate to the $i$-th is a shear with $\det = 1$, and preserves outer measure. So in every case $m^*(E_s A) = \abs{\det E_s}\, m^*A$ for all $A$. Applying this $r$ times and using multiplicativity of the determinant,
\[ m^*(TA) = \abs{\det E_1} \cdots \abs{\det E_r}\; m^*A = \abs{\det T}\; m^*A. \]
Since $T$ is a bijection and $\abs{\det T} > 0$, the lemma that scaling outer measure forces measurability shows that $T$ is a meseomorphism and $m(TE) = \abs{\det T}\, mE$ for measurable $E$.

\emph{Singular $T$.} Now $\det T = 0$, and we must show $m^*(TA) = 0$ for all $A$; it suffices to show that the range $T\R^n$ is a zero set. The range is a linear subspace of dimension at most $n-1$. If $n = 1$ it is $\set{0}$, a zero set. If $n \ge 2$, the range is contained in a subspace $W$ of dimension $n - 1$; choose a basis $w_1, \dots, w_{n-1}$ of $W$ and extend it by a vector $w_n$ to a basis of $\R^n$. The linear map $L$ with $L e_k = w_k$ for all $k$ is invertible and maps the coordinate hyperplane $H = \set{x : x_n = 0}$ onto $W$. By the invertible case and the fact that coordinate hyperplanes are zero sets, $m^*W = \abs{\det L}\, m^*H = 0$. Hence $m^*(TA) \le m^*W = 0 = \abs{\det T}\, m^*A$. Finally, $TE$ is then a zero set, so it is measurable with $m(TE) = 0 = \abs{\det T}\, mE$.
""", 3, 40, [
    r"Factor an invertible matrix into elementary matrices; each elementary matrix is a map whose effect on outer measure you already know.",
    r"Once $m^*(TA) = \abs{\det T}\,m^*A$ for all $A$ with $T$ invertible, measurability comes from the lemma on scaling outer measure.",
    r"If $T$ is singular, its range lies in a proper subspace, which is the image of a coordinate hyperplane under an invertible linear map.",
], ["c6-thm-diagonal", "c6-lem-shear", "c6-lem-outer-scaling", "c6-prop-hyperplane-zero", "c6-prop-measurable-basic"]))

B.append(result("corollary", "c6-cor-rigid-motion", "Rigid motions are meseometries", r"""
Let $O$ be an orthogonal $n \times n$ matrix (that is, $O^{T}O = I$) and $v \in \R^n$. Then the rigid motion $x \mapsto Ox + v$ is a meseometry of $\R^n$. In particular rotations and reflections preserve Lebesgue measure.
""", r"""
From $O^{T}O = I$ and $\det O^{T} = \det O$ we get $(\det O)^2 = 1$, so $\abs{\det O} = 1$ and $O$ is invertible. By the theorem on linear maps, $m^*(OA) = m^*A$ for every $A$, and by the theorem on translations $m^*(OA + v) = m^*(OA) = m^*A$. So the bijection $x \mapsto Ox + v$ preserves the outer measure of every set, and by the lemma that scaling outer measure forces measurability (with $c = 1$) it is a meseometry.
""", 1, 10, [
    r"What is the determinant of an orthogonal matrix?",
], ["c6-thm-linear", "c6-thm-translation", "c6-lem-outer-scaling"]))

B.append(prose("c6-mes-lipschitz-prose", r"""
Nonlinear maps can distort measure in complicated ways, but a map that stretches distances by at most a fixed factor stretches outer measure by at most a fixed factor. The enclosing argument needs coverings by cubes rather than by boxes of arbitrary shape, since a long thin box has small volume but large diameter.
"""))

B.append(note("definition", "c6-def-lipschitz", "Lipschitz map", r"""
Let $A \subseteq \R^n$. A map $T : A \to \R^n$ is \emph{Lipschitz} with constant $L \ge 0$ if $\abs{Tx - Ty} \le L \abs{x - y}$ for all $x, y \in A$, where $\abs{\cdot}$ is the Euclidean length. A Lipschitz map is continuous.
"""))

B.append(result("lemma", "c6-lem-cube-coverings", "Coverings by cubes", r"""
Let $A \subseteq \R^n$ with $m^*A < \infty$ and let $\eps > 0$. Then there are countably many closed cubes $Q_1, Q_2, \dots$ with $A \subseteq \bigcup_k Q_k$ and $\sum_k \abs{Q_k} \le m^*A + \eps$.
""", r"""
\emph{Step 1: one box.} Let $B = \prod_i (a_i, b_i)$ be a nonempty open box and $\eta > 0$. For $N \in \N$ and $j = (j_1, \dots, j_n) \in \Z^n$ let $Q_j = \prod_i [j_i/N, (j_i+1)/N]$, a closed cube of side $1/N$ and volume $N^{-n}$. Each $x \in \R^n$ lies in the cube with $j_i$ the greatest integer $\le N x_i$, so the cubes that meet $B$ cover $B$. If $Q_j$ meets $B$, then for each $i$ the interval $[j_i/N, (j_i+1)/N]$ meets $(a_i, b_i)$, which forces $N a_i - 1 < j_i < N b_i$. By the lemma on counting lattice points (applied with $N = 1$ to the interval $(Na_i - 1, Nb_i)$), there are at most $N(b_i - a_i) + 2$ such integers $j_i$. Hence at most $\prod_i (N(b_i - a_i) + 2)$ cubes $Q_j$ meet $B$, and their total volume is at most
\[ N^{-n} \prod_{i=1}^n \bigl( N(b_i - a_i) + 2 \bigr) = \prod_{i=1}^n \Bigl( b_i - a_i + \frac{2}{N} \Bigr) \longrightarrow \abs{B} \quad (N \to \infty). \]
So for $N$ large, $B$ is covered by finitely many closed cubes of total volume at most $\abs{B} + \eta$.

\emph{Step 2.} Choose open boxes $B_1, B_2, \dots$ covering $A$ with $\sum_k \abs{B_k} \le m^*A + \eps/2$; empty boxes may be discarded. By Step 1 cover each $B_k$ by finitely many closed cubes of total volume at most $\abs{B_k} + \eps/2^{k+1}$. All these cubes together form a countable family covering $A$ with total volume at most $m^*A + \eps/2 + \sum_k \eps/2^{k+1} = m^*A + \eps$.
""", 3, 30, [
    r"First cover a single open box by small cubes from the grid of mesh $1/N$, wasting little volume.",
    r"Count, in each coordinate, how many grid intervals $[j/N, (j+1)/N]$ can meet $(a_i, b_i)$: at most $N(b_i - a_i) + 2$.",
], ["c6-def-outer-measure", "c6-lem-integer-count"]))

B.append(result("theorem", "c6-thm-lipschitz-zero", "Lipschitz maps do not inflate zero sets", r"""
Let $A \subseteq \R^n$ and let $T : A \to \R^n$ be Lipschitz with constant $L$. Then
\[ m^*(TA) \le (2L\sqrt n)^n\, m^*A. \]
In particular, if $Z \subseteq A$ is a zero set then $TZ$ is a zero set.
""", r"""
If $m^*A = \infty$ there is nothing to prove (when $L = 0$ the map is constant and $TA$ is at most one point, a zero set). Assume $m^*A < \infty$, let $\eps > 0$, and by the lemma on coverings by cubes choose closed cubes $Q_k$ with sides $s_k$, covering $A$, with $\sum_k s_k^n \le m^*A + \eps$.

Fix $k$ with $Q_k \cap A \ne \emptyset$ and pick $p \in Q_k \cap A$. For $x \in Q_k \cap A$, each coordinate of $x - p$ has absolute value at most $s_k$, so $\abs{x - p} \le s_k \sqrt n$ and therefore $\abs{Tx - Tp} \le L s_k \sqrt n$. In particular each coordinate of $Tx$ is within $L s_k \sqrt n$ of the corresponding coordinate of $Tp$. Thus $T(Q_k \cap A)$ lies in the closed cube $Q_k'$ centered at $Tp$ with side $2 L s_k \sqrt n$, and $\abs{Q_k'} = (2L\sqrt n)^n s_k^n$.

Since $TA = \bigcup_k T(Q_k \cap A)$ and any boxes may be used in coverings,
\[ m^*(TA) \le \sum_k \abs{Q_k'} = (2L\sqrt n)^n \sum_k s_k^n \le (2L\sqrt n)^n (m^*A + \eps). \]
Let $\eps \to 0$. For the last statement apply the inequality to the restriction of $T$ to $Z$, which is Lipschitz with the same constant.
""", 3, 30, [
    r"Cover $A$ by cubes rather than general boxes. How big can the image of (the part of $A$ in) a cube of side $s$ be?",
    r"A cube of side $s$ has diameter $s\sqrt n$, so its image has diameter at most $Ls\sqrt n$ and fits in a cube of side $2Ls\sqrt n$.",
], ["c6-def-lipschitz", "c6-lem-cube-coverings", "c6-cor-any-boxes"]))

B.append(note("remark", "c6-rem-diffeomorphisms", "Smooth maps, taken on faith", r"""
A continuously differentiable map is Lipschitz on each compact convex set (by the mean value inequality of multivariable calculus), so it sends zero sets to zero sets. It will be shown in the section on regularity that a Lipschitz map of $\R^n$ sends measurable sets to measurable sets. Two further facts are stated here without proof, since they belong to multivariable calculus: a diffeomorphism between open subsets of $\R^n$ preserves measurability in both directions, and it changes measure according to the change of variables formula $m(TE) = \int_E \abs{\det DT}$.

A homeomorphism, by contrast, need not be a meseomorphism: there is a homeomorphism of $[0,1]$ that carries the Cantor set, a zero set, onto a set of positive measure, and then some measurable subset of the Cantor set has a nonmeasurable image.
"""))

C = [
    card("c6-card-meseomorphism", "c6-def-meseomorphism", r"Define meseomorphism and meseometry.", r"A bijection $T$ of $\R^n$ such that $T$ and $T^{-1}$ send measurable sets to measurable sets; a meseometry also satisfies $m(TE) = mE$."),
    card("c6-card-box-principle", "c6-lem-box-principle", r"State the box principle for bounding $m^*(TA)$.", r"If $m^*(TB) \le c\abs{B}$ for every open box $B$, then $m^*(TA) \le c\,m^*A$ for every set $A$."),
    card("c6-card-outer-scaling", "c6-lem-outer-scaling", r"Why is a bijection with $m^*(TA) = c\,m^*A$ for all $A$ a meseomorphism?", r"Test $TE$ against $X$ by testing $E$ against $T^{-1}X$: $X \cap TE = T(T^{-1}X \cap E)$ and $X \cap (TE)^c = T(T^{-1}X \cap E^c)$."),
    card("c6-card-linear", "c6-thm-linear", r"How does a linear map $T$ of $\R^n$ change Lebesgue measure?", r"$m(TE) = \abs{\det T}\,mE$ (and $m^*(TA) = \abs{\det T}\,m^*A$ for all $A$)."),
    card("c6-card-linear-idea", "c6-thm-linear", r"Outline the proof that $m^*(TA) = \abs{\det T}\,m^*A$.", r"Factor $T$ into elementary matrices: swaps and diagonal maps send boxes to boxes; a shear is handled by slicing a box into thin slabs. A singular $T$ has range in a hyperplane, a zero set."),
    card("c6-card-shear-idea", "c6-lem-shear", r"Why does a shear $x_i \mapsto x_i + \sigma x_j$ not increase the outer measure of a box?", r"Cut the box into $N$ slabs of thickness $\ell/N$ in the $x_j$ direction; each sheared slab lies in a box longer by $2\abs{\sigma}\ell/N$; the total excess volume is $O(1/N)$."),
    card("c6-card-lipschitz", "c6-thm-lipschitz-zero", r"What does a Lipschitz map with constant $L$ do to outer measure in $\R^n$?", r"$m^*(TA) \le (2L\sqrt n)^n m^*A$; in particular zero sets go to zero sets. Proof: cover by cubes; the image of a cube of side $s$ lies in a cube of side $2Ls\sqrt n$."),
    card("c6-card-rigid", "c6-cor-rigid-motion", r"Which maps of $\R^n$ are shown to be meseometries?", r"Translations, coordinate permutations, shears, and all rigid motions $x \mapsto Ox + v$ with $O$ orthogonal (linear maps with $\abs{\det} = 1$)."),
]

write("6-meseomorphism", B, C)
