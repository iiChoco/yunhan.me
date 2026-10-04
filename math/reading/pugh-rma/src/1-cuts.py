from __future__ import annotations
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from c1_common import Section

s = Section("1-cuts")

# ---------------------------------------------------------------- the gap in Q
s.prose("cuts-intro", r"""
The rational numbers are closed under arithmetic and densely ordered, and still they are not enough for analysis: a length as simple as the diagonal of the unit square is not rational. This section builds the real numbers out of $\Q$ by Dedekind's method of cuts, proves that the result has no gaps (the least upper bound property), and then derives the working tools of analysis from that one property: the Archimedean property, density of $\Q$, square roots, the $\eps$-principle, the convergence of Cauchy sequences and of bounded monotone sequences, and the limit laws.
""")

s.result("thm-sqrt2-irrational", "theorem", "No rational number has square 2", r"""
There is no $r \in \Q$ with $r^2 = 2$.
""", r"""
Suppose there is a rational $r$ with $r^2 = 2$. Then $r \ne 0$, and since $(-r)^2 = r^2$ we may assume $r > 0$. So $r = p/q$ with $p, q \in \N$. The set of natural numbers $q$ for which $r = p/q$ for some $p \in \N$ is nonempty, so by the least element principle it has a smallest member; fix that $q$ and the corresponding $p$.

From $r^2 = 2$ we get $p^2 = 2q^2$, so $p^2$ is even, and therefore $p$ is even: $p = 2k$ with $k \in \N$. Substituting, $4k^2 = 2q^2$, so $q^2 = 2k^2$ is even and therefore $q$ is even: $q = 2j$ with $j \in \N$. But then
\[ r = \frac{p}{q} = \frac{2k}{2j} = \frac{k}{j}, \qquad j < q, \]
which expresses $r$ as a fraction with a smaller natural denominator, contradicting the choice of $q$. Hence no rational number has square $2$.
""", 2, 20, [
    r"Argue by contradiction, writing $r = p/q$. You need some way to say the fraction cannot be reduced forever.",
    r"Choose $q \in \N$ as small as possible. Show that $p$ is even, then that $q$ is even, and produce a smaller denominator.",
], ["ex-even-square"])

s.prose("cuts-gap", r"""
So the rationals whose square is less than $2$ and the positive rationals whose square is more than $2$ are separated by nothing at all: there is a gap in $\Q$ where $\sqrt{2}$ ought to be. Dedekind's idea is to let the separation itself be the number.
""")

# ---------------------------------------------------------------- cuts
s.definition("def-cut", "Cut", r"""
A \emph{cut} in $\Q$ is a pair of subsets $A, B$ of $\Q$ such that
\begin{enumerate}
\item $A \cup B = \Q$, $A \ne \varnothing$, $B \ne \varnothing$, and $A \cap B = \varnothing$;
\item if $a \in A$ and $b \in B$ then $a < b$;
\item $A$ contains no largest element.
\end{enumerate}
The cut is written $A|B$; $A$ is its left-hand part and $B$ its right-hand part. Two cuts $A|B$ and $C|D$ are equal when $A = C$ and $B = D$.
""")

s.result("lem-cut-basic", "lemma", "Shape of a cut", r"""
Let $A|B$ be a cut in $\Q$. Then:
\begin{enumerate}
\item $B = \Q \setminus A$, so a cut is determined by its left-hand part;
\item if $a \in A$ and $r \in \Q$ with $r < a$, then $r \in A$;
\item if $b \in B$ and $r \in \Q$ with $r > b$, then $r \in B$.
\end{enumerate}
""", r"""
(1) Since $A \cap B = \varnothing$, no element of $B$ is in $A$, so $B \subset \Q \setminus A$. Since $A \cup B = \Q$, every rational not in $A$ is in $B$, so $\Q \setminus A \subset B$.

(2) Let $a \in A$ and $r < a$. If $r$ were not in $A$ it would be in $B$ by (1), and then property (2) of a cut, applied to $a \in A$ and $r \in B$, would give $a < r$, contradicting $r < a$. So $r \in A$.

(3) Let $b \in B$ and $r > b$. If $r$ were in $A$, then property (2) of a cut applied to $r \in A$ and $b \in B$ would give $r < b$, contradicting $r > b$. So $r \notin A$, and $r \in B$ by (1).
""", 1, 10, [
    r"Each part is a short argument by contradiction from the three defining properties of a cut.",
    r"For (2): a rational that is not in $A$ is in $B$, and every element of $B$ exceeds every element of $A$.",
], ["def-cut"])

s.result("lem-rational-cut", "lemma", "Each rational number gives a cut", r"""
Let $c \in \Q$, and put $A = \set{r \in \Q : r < c}$ and $B = \set{r \in \Q : r \ge c}$. Then $A|B$ is a cut.
""", r"""
Every rational $r$ satisfies exactly one of $r < c$ and $r \ge c$, so $A \cup B = \Q$ and $A \cap B = \varnothing$. We have $c - 1 \in A$ and $c \in B$, so neither part is empty. If $a \in A$ and $b \in B$ then $a < c \le b$, so $a < b$. Finally, let $a \in A$. The number $a' = (a + c)/2$ is rational, and $a < c$ gives $a < a' < c$; so $a' \in A$ and $a' > a$. Thus no element of $A$ is the largest, and $A|B$ is a cut.
""", 1, 10, [
    r"Check the three conditions in the definition of a cut one at a time.",
    r"For the absence of a largest element, the midpoint of $a$ and $c$ is rational.",
], ["def-cut"])

s.definition("def-real-number", "Real number, rational cut", r"""
A \emph{real number} is a cut in $\Q$. The set of all real numbers is denoted $\R$. For $c \in \Q$, the cut
\[ c^* = \set{r \in \Q : r < c} \,\big|\, \set{r \in \Q : r \ge c} \]
is the \emph{rational cut} at $c$. A cut that is not of this form is an \emph{irrational} number.
""")

s.result("ex-sqrt2-cut", "exercise", "A cut that is not rational", r"""
Let
\[ A = \set{r \in \Q : r \le 0 \text{ or } r^2 < 2}, \qquad B = \set{r \in \Q : r > 0 \text{ and } r^2 \ge 2}. \]
Prove that $A|B$ is a cut, and that it is not $c^*$ for any $c \in \Q$.
""", r"""
We use the following computation. For a rational $t > 0$ put $t' = \dfrac{2t + 2}{t + 2}$. Then $t'$ is a positive rational, and
\[ t' - t = \frac{2 - t^2}{t + 2}, \qquad (t')^2 - 2 = \frac{(2t + 2)^2 - 2(t + 2)^2}{(t + 2)^2} = \frac{2(t^2 - 2)}{(t + 2)^2}. \]
So if $t^2 < 2$ then $t' > t$ and $(t')^2 < 2$, while if $t^2 > 2$ then $t' < t$ and $(t')^2 > 2$.

\emph{$A|B$ is a cut.} A rational $r$ fails to be in $A$ exactly when $r > 0$ and $r^2 \ge 2$, that is, exactly when $r \in B$; so $A \cup B = \Q$ and $A \cap B = \varnothing$. Also $0 \in A$ and $2 \in B$. Let $a \in A$ and $b \in B$. If $a \le 0$ then $a < b$ because $b > 0$. If $a > 0$ then $a^2 < 2 \le b^2$; were $a \ge b$, multiplying positive numbers would give $a^2 \ge b^2$, so $a < b$. Finally let $a \in A$. If $a \le 0$ then $1 \in A$ and $1 > a$. If $a > 0$ then $a^2 < 2$, and by the computation $a' = (2a + 2)/(a + 2)$ satisfies $a' > a$ and $(a')^2 < 2$, so $a' \in A$. Thus $A$ has no largest element.

\emph{$A|B$ is not a rational cut.} Suppose $A = \set{r \in \Q : r < c}$ for some $c \in \Q$. Then $c \notin A$, so $c > 0$ and $c^2 \ge 2$. Since no rational has square $2$, $c^2 > 2$. By the computation, $c' = (2c + 2)/(c + 2)$ is a positive rational with $c' < c$ and $(c')^2 > 2$. Then $c' \in B$, so $c' \notin A$; but $c' < c$ says $c' \in A$. This contradiction shows that $A|B$ is not $c^*$ for any rational $c$.
""", 3, 35, [
    r"Verifying that every element of $A$ and $B$ compare correctly is routine. The real work is in showing $A$ has no largest element: given a positive rational $a$ with $a^2 < 2$, you must produce a larger rational whose square is still less than $2$.",
    r"Try $a' = \dfrac{2a + 2}{a + 2}$ and compute $a' - a$ and $(a')^2 - 2$.",
    r"If $A|B = c^*$ then $c \in B$ and $c^2 > 2$. Use the same formula to find a rational below $c$ that is still in $B$.",
], ["def-cut", "def-real-number", "thm-sqrt2-irrational"])

# ---------------------------------------------------------------- order
s.definition("def-cut-order", "Order on cuts", r"""
Let $x = A|B$ and $y = C|D$ be cuts. We say that $x$ is \emph{less than or equal to} $y$, written $x \le y$, if $A \subset C$. We write $x < y$ if $x \le y$ and $x \ne y$. As usual $y \ge x$ and $y > x$ mean $x \le y$ and $x < y$.
""")

s.result("prop-order-total", "proposition", "The order on cuts is a total order", r"""
Let $x = A|B$, $y = C|D$, $z = E|F$ be cuts. Then:
\begin{enumerate}
\item if $x \le y$ and $y \le x$ then $x = y$;
\item if $x \le y$ and $y \le z$ then $x \le z$;
\item $x \le y$ or $y \le x$.
\end{enumerate}
Consequently exactly one of $x < y$, $x = y$, $y < x$ holds (trichotomy).
""", r"""
(1) $A \subset C$ and $C \subset A$ give $A = C$. By the lemma on the shape of a cut, $B = \Q \setminus A = \Q \setminus C = D$. So $x = y$.

(2) $A \subset C$ and $C \subset E$ give $A \subset E$.

(3) Suppose $x \le y$ fails, so $A \not\subset C$: there is an $a \in A$ with $a \notin C$, and then $a \in D$. Let $c \in C$. Since $c \in C$ and $a \in D$, we have $c < a$. Since $a \in A$ and $c < a$, the lemma on the shape of a cut gives $c \in A$. Hence $C \subset A$, that is, $y \le x$.

\emph{Trichotomy.} By (3), $x \le y$ or $y \le x$. If both hold then $x = y$ by (1), and then neither $x < y$ nor $y < x$ holds, since each requires $x \ne y$. If $x \le y$ holds and $y \le x$ does not, then $x \ne y$ (equal cuts satisfy $y \le x$), so $x < y$; and $y < x$ fails because it requires $y \le x$. Symmetrically, if $y \le x$ holds and $x \le y$ does not, then $y < x$ and neither of the other two holds. In every case exactly one of the three holds.
""", 2, 20, [
    r"Parts (1) and (2) are facts about inclusion of sets. Part (3) needs the structure of cuts.",
    r"For (3): if $A \not\subset C$, pick $a \in A \setminus C$. Then $a \in D$, so $a$ is above everything in $C$. Why does that force $C \subset A$?",
], ["def-cut", "def-cut-order", "lem-cut-basic"])

s.result("lem-rational-order", "lemma", "The order on rational cuts is the order on Q", r"""
For $c, d \in \Q$: $c < d$ if and only if $c^* < d^*$. In particular $c \mapsto c^*$ is an injection of $\Q$ into $\R$.
""", r"""
Suppose $c < d$. If $r < c$ then $r < d$, so $\set{r \in \Q : r < c} \subset \set{r \in \Q : r < d}$, that is, $c^* \le d^*$. The rational $c$ belongs to the second set and not to the first, so the left-hand parts differ and $c^* \ne d^*$. Hence $c^* < d^*$.

Conversely suppose $c^* < d^*$. If $c = d$ then $c^* = d^*$, and if $d < c$ then $d^* < c^*$ by the first paragraph; by trichotomy for cuts, each of these is incompatible with $c^* < d^*$. Since exactly one of $c < d$, $c = d$, $d < c$ holds in $\Q$, we conclude $c < d$.

Injectivity: if $c \ne d$ then $c < d$ or $d < c$, so $c^* < d^*$ or $d^* < c^*$, and in either case $c^* \ne d^*$.
""", 1, 10, [
    r"For the forward direction, compare the two left-hand parts and find a rational in one but not the other.",
    r"For the converse, rule out $c = d$ and $d < c$ using the forward direction and trichotomy for cuts.",
], ["def-real-number", "def-cut-order", "prop-order-total"])

# ---------------------------------------------------------------- lub
s.definition("def-upper-bound", "Upper bound, least upper bound", r"""
Let $S \subset \R$. A number $M \in \R$ is an \emph{upper bound} for $S$ if $s \le M$ for every $s \in S$; if $S$ has an upper bound it is \emph{bounded above}. An upper bound $M$ for $S$ is the \emph{least upper bound} of $S$ if $M \le M'$ for every upper bound $M'$ of $S$. It is denoted $\lub S$ (also called the \emph{supremum}, $\sup S$). Two least upper bounds of the same set are each $\le$ the other, hence equal; so the least upper bound is unique when it exists.

Symmetrically, $m$ is a \emph{lower bound} for $S$ if $m \le s$ for every $s \in S$, $S$ is \emph{bounded below} if it has one, and the \emph{greatest lower bound} $\glb S$ (the \emph{infimum}, $\inf S$) is a lower bound that is $\ge$ every lower bound. A set is \emph{bounded} if it is bounded above and below.
""")

s.result("thm-lub", "theorem", "Least upper bound property", r"""
Every nonempty subset of $\R$ that is bounded above has a least upper bound in $\R$. (Here $\R$ is the set of cuts in $\Q$ with the order defined above.)
""", r"""
Let $S \subset \R$ be nonempty and bounded above, with upper bound $M = C_0|D_0$. Define
\[ E = \set{r \in \Q : r \in A \text{ for some cut } A|B \in S}, \qquad F = \Q \setminus E. \]
So $E$ is the union of the left-hand parts of the members of $S$.

\emph{$E|F$ is a cut.} By construction $E \cup F = \Q$ and $E \cap F = \varnothing$. Since $S$ is nonempty, it has a member $A|B$, and $A \ne \varnothing$, so $E \ne \varnothing$. Each $A|B \in S$ satisfies $A|B \le M$, that is, $A \subset C_0$; hence $E \subset C_0$, and so $D_0 = \Q \setminus C_0 \subset F$. As $D_0 \ne \varnothing$, $F \ne \varnothing$. Let $e \in E$ and $f \in F$. Then $e \in A$ for some $A|B \in S$, and $f \notin E$ gives $f \notin A$, so $f \in B$; therefore $e < f$. Finally let $e \in E$, say $e \in A$ with $A|B \in S$. Since $A$ has no largest element there is $a' \in A$ with $a' > e$, and $a' \in E$. So $E$ has no largest element.

\emph{$E|F$ is an upper bound for $S$.} If $A|B \in S$ then $A \subset E$, which says $A|B \le E|F$.

\emph{$E|F$ is the least upper bound.} Let $z = G|H$ be any upper bound for $S$. Then $A \subset G$ for every $A|B \in S$, so the union $E$ of these sets satisfies $E \subset G$. That is, $E|F \le z$.
""", 3, 30, [
    r"You have to build one cut out of a whole set of cuts. With the order defined by inclusion of left-hand parts, what is the smallest set containing every left-hand part?",
    r"Let $E$ be the union of the left-hand parts of the members of $S$ and $F = \Q \setminus E$. Show $E|F$ is a cut; the upper bound is needed exactly to see that $F \ne \varnothing$.",
    r"Being an upper bound and being least are then both statements about inclusions of sets.",
], ["def-cut", "def-cut-order", "def-upper-bound", "lem-cut-basic"])

s.remark("rem-q-not-complete", r"""
The rational numbers do not have this property. In $\Q$ the set $\set{r \in \Q : r \le 0 \text{ or } r^2 < 2}$ is nonempty and bounded above by $2$, and it has no least upper bound \emph{in} $\Q$. In $\R$ its least upper bound is the irrational cut of the earlier exercise. Filling such gaps is the whole point of the construction.
""")

# ---------------------------------------------------------------- arithmetic
s.prose("cuts-arithmetic-intro", r"""
Cuts are to be numbers, so they must be added and multiplied. The definitions are natural; checking that they obey the laws of arithmetic is long and unenlightening. We do the first steps and then record the outcome.
""")

s.definition("def-cut-sum", "Sum of cuts", r"""
Let $x = A|B$ and $y = C|D$ be cuts. Their \emph{sum} is $x + y = E|F$, where
\[ E = \set{a + c : a \in A,\ c \in C}, \qquad F = \Q \setminus E. \]
""")

s.result("lem-sum-is-cut", "lemma", "The sum of two cuts is a cut", r"""
Let $A|B$ and $C|D$ be cuts, $E = \set{a + c : a \in A,\ c \in C}$ and $F = \Q \setminus E$. Then $E|F$ is a cut.
""", r"""
By construction $E \cup F = \Q$ and $E \cap F = \varnothing$. Since $A$ and $C$ are nonempty, so is $E$.

\emph{$F$ is nonempty.} Pick $b \in B$ and $d \in D$. If $b + d$ were in $E$, we would have $b + d = a + c$ with $a \in A$, $c \in C$. But $a < b$ and $c < d$, so $a + c < b + d$, a contradiction. Hence $b + d \in F$.

\emph{$E$ is closed downward.} Let $e = a + c \in E$ with $a \in A$, $c \in C$, and let $r \in \Q$ with $r < e$. Then $r - c < a$, so $r - c \in A$ by the lemma on the shape of a cut, and $r = (r - c) + c \in E$.

\emph{Elements of $E$ are less than elements of $F$.} Let $e \in E$ and $f \in F$. Then $f \ne e$ because $f \notin E$. If $f < e$, then $f \in E$ because $E$ is closed downward, which is false. Hence $e < f$.

\emph{$E$ has no largest element.} Let $e = a + c \in E$. Since $A$ has no largest element there is $a' \in A$ with $a' > a$, and then $a' + c \in E$ and $a' + c > e$.
""", 2, 20, [
    r"The conditions on $E \cup F$ and $E \cap F$ are free. The three things to check are: $F \ne \varnothing$, every element of $E$ is below every element of $F$, and $E$ has no largest element.",
    r"For $F \ne \varnothing$, add an element of $B$ to an element of $D$. For the comparison, first show $E$ is closed downward: if $r < a + c$ then $r = (r - c) + c$.",
], ["def-cut", "lem-cut-basic", "def-cut-sum"])

s.result("ex-zero-identity", "exercise", "The rational cut at zero is the additive identity", r"""
Prove that $x + 0^* = x$ for every cut $x$.
""", r"""
Let $x = A|B$. The left-hand part of $0^*$ is $Z = \set{r \in \Q : r < 0}$, so the left-hand part of $x + 0^*$ is $E = \set{a + z : a \in A,\ z \in Z}$. Since a cut is determined by its left-hand part, it suffices to show $E = A$.

$E \subset A$: if $a \in A$ and $z < 0$ then $a + z < a$, so $a + z \in A$ by the lemma on the shape of a cut.

$A \subset E$: let $a \in A$. Since $A$ has no largest element there is $a' \in A$ with $a' > a$. Then $z = a - a'$ is a negative rational and $a = a' + z \in E$.
""", 2, 15, [
    r"A cut is determined by its left-hand part, so compare the left-hand part of $x + 0^*$ with $A$ by two inclusions.",
    r"One inclusion uses that $A$ is closed downward; the other uses that $A$ has no largest element.",
], ["def-cut-sum", "lem-cut-basic", "def-real-number"])

s.definition("def-cut-negative-product", "Negatives and products of cuts", r"""
Let $x = A|B$ and $y = C|D$ be cuts.
\begin{itemize}
\item The \emph{negative} of $x$ is $-x = A'|B'$, where $A'$ consists of the rationals $r$ such that $-r \in B$ and $-r$ is not the smallest element of $B$, and $B' = \Q \setminus A'$. The \emph{difference} is $x - y = x + (-y)$.
\item If $x > 0^*$ and $y > 0^*$, the \emph{product} is $x \cdot y = E|F$, where
\[ E = \set{r \in \Q : r \le 0, \text{ or } r = ac \text{ for some } a \in A,\ c \in C \text{ with } a > 0,\ c > 0} \]
and $F = \Q \setminus E$.
\item In the remaining cases the product is defined by the rule of signs: $x \cdot 0^* = 0^* \cdot x = 0^*$; $x \cdot y = -\big(x \cdot (-y)\big)$ if $x > 0^*$, $y < 0^*$; $x \cdot y = -\big((-x) \cdot y\big)$ if $x < 0^*$, $y > 0^*$; and $x \cdot y = (-x) \cdot (-y)$ if $x < 0^*$, $y < 0^*$.
\end{itemize}
""")

s.text("thm-complete-ordered-field", "theorem", r"""
With the order, sum, negative, and product defined above, the set $\R$ of cuts in $\Q$ has the following properties.
\begin{enumerate}
\item \emph{$\R$ is a field.} Addition and multiplication are well defined, commutative, and associative, and multiplication distributes over addition. The cuts $0^*$ and $1^*$ are different; $x + 0^* = x$ and $x \cdot 1^* = x$ for all $x$; $x + (-x) = 0^*$ for all $x$; and every $x \ne 0^*$ has a reciprocal $x^{-1}$ with $x \cdot x^{-1} = 1^*$.
\item \emph{$\R$ is an ordered field.} For all $x, y, z \in \R$: exactly one of $x < y$, $x = y$, $y < x$ holds; if $x < y$ and $y < z$ then $x < z$; if $x < y$ then $x + z < y + z$; and if $x < y$ and $0^* < z$ then $x z < y z$.
\item \emph{$\R$ contains $\Q$.} The map $c \mapsto c^*$ is injective and satisfies $(c + d)^* = c^* + d^*$, $(cd)^* = c^* \cdot d^*$, and $c < d$ if and only if $c^* < d^*$.
\item \emph{$\R$ is complete.} Every nonempty subset of $\R$ that is bounded above has a least upper bound.
\end{enumerate}
In short: $\R$ is a complete ordered field containing $\Q$ as an ordered subfield.
""", "The real numbers form a complete ordered field")

s.remark("rem-field-on-faith", r"""
Parts of this theorem have been proved above: trichotomy and transitivity of the order, the order statement in (3), that sums are cuts, that $0^*$ is the additive identity, and all of (4). The remaining verifications (associativity, distributivity, negatives, reciprocals, compatibility of the order with the operations) are of the same kind, long and without surprises, and they are taken on faith here.

\textbf{From now on} we identify each rational $c$ with the cut $c^*$, so that $\N \subset \Z \subset \Q \subset \R$, and we forget how real numbers were built. Every later proof uses only the four properties in the theorem. The consequences of properties (1) and (2) are the ordinary rules of algebra and of inequalities (for example: $x^2 \ge 0$; $0 < 1$; a product of positive numbers is positive; if $0 \le u < v$ then $u^2 < v^2$; inequalities in the same direction may be added) and they are used freely without comment. What is new, and what must always be cited, is the least upper bound property.
""")

# ---------------------------------------------------------------- consequences of lub
s.definition("def-interval", "Intervals", r"""
For real numbers $a \le b$,
\[ (a, b) = \set{x \in \R : a < x < b}, \qquad [a, b] = \set{x \in \R : a \le x \le b}, \]
and $[a, b)$, $(a, b]$ are defined in the same way. The first is an \emph{open} interval and the second a \emph{closed} interval. Unbounded intervals are written with the symbols $\pm\infty$, which are not real numbers: $(a, \infty) = \set{x \in \R : x > a}$, $(-\infty, b] = \set{x \in \R : x \le b}$, and so on.
""")

s.result("cor-glb", "corollary", "Greatest lower bound property", r"""
Every nonempty subset of $\R$ that is bounded below has a greatest lower bound.
""", r"""
Let $S \subset \R$ be nonempty and bounded below, and let $L$ be the set of all lower bounds of $S$. Then $L \ne \varnothing$. Fix some $s_0 \in S$; every $\ell \in L$ satisfies $\ell \le s_0$, so $L$ is bounded above. By the least upper bound property, $m = \lub L$ exists.

\emph{$m$ is a lower bound for $S$.} Let $s \in S$. Every $\ell \in L$ satisfies $\ell \le s$, so $s$ is an upper bound for $L$, and therefore $m \le s$ because $m$ is the least upper bound.

\emph{$m$ is the greatest lower bound.} If $\ell$ is any lower bound for $S$, then $\ell \in L$, so $\ell \le m$ because $m$ is an upper bound for $L$.
""", 2, 15, [
    r"Apply the least upper bound property to a different set, built from $S$.",
    r"Let $L$ be the set of all lower bounds of $S$. It is nonempty and bounded above by any element of $S$. Show $\lub L$ is a lower bound of $S$.",
], ["thm-lub", "def-upper-bound"])

s.result("thm-archimedean", "theorem", "Archimedean property", r"""
For every $x \in \R$ there is an $n \in \N$ with $n > x$. Consequently, for every real $\eps > 0$ there is an $n \in \N$ with $1/n < \eps$.
""", r"""
Suppose the first statement fails for some $x \in \R$: then $n \le x$ for all $n \in \N$, so $\N$ is a nonempty subset of $\R$ that is bounded above. By the least upper bound property $b = \lub \N$ exists. Since $b - 1 < b$, the number $b - 1$ is not an upper bound for $\N$, so there is an $n \in \N$ with $n > b - 1$. Then $n + 1 \in \N$ and $n + 1 > b$, contradicting the fact that $b$ is an upper bound for $\N$. Hence for every $x$ there is an $n \in \N$ with $n > x$.

For the consequence, let $\eps > 0$ and choose $n \in \N$ with $n > 1/\eps$. Multiplying by the positive number $\eps/n$ gives $\eps > 1/n$.
""", 3, 25, [
    r"Argue by contradiction: if no natural number exceeds $x$, then $\N$ is bounded above in $\R$.",
    r"Let $b = \lub \N$. The number $b - 1$ is not an upper bound, so some $n$ exceeds it. Now look at $n + 1$.",
], ["thm-lub", "thm-complete-ordered-field"])

s.result("thm-density-rationals", "theorem", "The rationals are dense in the reals", r"""
If $a, b \in \R$ and $a < b$, then there is a rational number $r$ with $a < r < b$.
""", r"""
Since $b - a > 0$, the Archimedean property gives $n \in \N$ with $1/n < b - a$, that is, $na + 1 < nb$.

We find an integer $m$ with $na < m \le na + 1$. Let $M = \set{m \in \Z : m > na}$. By the Archimedean property there is a natural number greater than $na$, so $M \ne \varnothing$; and there is $K \in \N$ with $K > -na$, that is, $-K < na$. Every $m \in M$ satisfies $m > na > -K$, so $m + K$ is a positive integer. Thus $\set{m + K : m \in M}$ is a nonempty subset of $\N$, and by the least element principle it has a smallest element. Correspondingly $M$ has a smallest element $m$. Then $m > na$, and $m - 1 \notin M$ (it is an integer smaller than the least element of $M$), so $m - 1 \le na$. Hence
\[ na < m \le na + 1 < nb. \]
Dividing by $n > 0$ gives $a < m/n < b$, and $r = m/n$ is rational.
""", 3, 30, [
    r"Rationals with denominator $n$ are spaced $1/n$ apart. If the spacing is smaller than $b - a$, one of them should land in $(a, b)$.",
    r"Choose $n$ with $1/n < b - a$ by the Archimedean property, and let $m$ be the \emph{least} integer greater than $na$. You must justify that a least such integer exists.",
    r"Then $m - 1 \le na < m$, so $na < m \le na + 1 < nb$.",
], ["thm-archimedean"])

s.result("thm-square-roots", "theorem", "Existence of square roots", r"""
For every real number $c > 0$ there is exactly one real number $y > 0$ with $y^2 = c$. It is denoted $\sqrt{c}$. (We also set $\sqrt{0} = 0$.)
""", r"""
\emph{Uniqueness.} If $0 < y_1 < y_2$ then $y_1^2 < y_2^2$, so two different positive numbers cannot have the same square.

\emph{Existence.} Let $S = \set{t \in \R : t \ge 0 \text{ and } t^2 \le c}$. Then $0 \in S$. If $t > c + 1$ then $t^2 > (c + 1)^2 = c^2 + 2c + 1 > c$, so $t \notin S$; hence $c + 1$ is an upper bound for $S$. By the least upper bound property, $y = \lub S$ exists.

\emph{$y > 0$.} Let $t = \min(1, c) > 0$. Since $0 < t \le 1$ we have $t^2 \le t \le c$, so $t \in S$ and $y \ge t > 0$.

\emph{$y^2 < c$ is impossible.} Suppose $y^2 < c$, and let $h = \min\left(1, \dfrac{c - y^2}{2y + 1}\right) > 0$. Since $0 < h \le 1$ we have $h^2 \le h$, so
\[ (y + h)^2 = y^2 + 2yh + h^2 \le y^2 + (2y + 1)h \le y^2 + (c - y^2) = c. \]
Thus $y + h \in S$ and $y + h > y$, contradicting that $y$ is an upper bound for $S$.

\emph{$y^2 > c$ is impossible.} Suppose $y^2 > c$, and let $h = \dfrac{y^2 - c}{2y} > 0$. Since $c > 0$, $h < \dfrac{y^2}{2y} = \dfrac{y}{2}$, so $y - h > 0$. Also
\[ (y - h)^2 = y^2 - 2yh + h^2 > y^2 - 2yh = c. \]
If $t \in S$ then $t^2 \le c < (y - h)^2$; were $t \ge y - h > 0$ we would have $t^2 \ge (y - h)^2$, so $t < y - h$. Thus $y - h$ is an upper bound for $S$ smaller than $y$, contradicting that $y$ is the least upper bound.

By trichotomy, $y^2 = c$.
""", 4, 60, [
    r"The square root should be the least upper bound of the numbers whose square is at most $c$. Check that this set is nonempty and bounded above.",
    r"With $y = \lub S$, rule out $y^2 < c$ and $y^2 > c$ separately. In the first case show that a slightly larger number is still in $S$; in the second, that a slightly smaller number is still an upper bound.",
    r"For small $h \in (0, 1]$: $(y + h)^2 \le y^2 + (2y + 1)h$ and $(y - h)^2 > y^2 - 2yh$. Choose $h$ to make the right-hand sides equal to $c$.",
], ["thm-lub", "thm-complete-ordered-field"])

s.result("cor-density-irrationals", "corollary", "Every interval contains irrational numbers", r"""
If $a, b \in \R$ and $a < b$, then there is an irrational number $z$ with $a < z < b$. Hence every interval $(a, b)$ with $a < b$ contains both rational and irrational numbers.
""", r"""
By the existence of square roots there is a real number $\sqrt{2} > 0$ with square $2$, and it is irrational because no rational number has square $2$. Since $a - \sqrt{2} < b - \sqrt{2}$, density of the rationals gives $r \in \Q$ with $a - \sqrt{2} < r < b - \sqrt{2}$. Put $z = r + \sqrt{2}$; then $a < z < b$. If $z$ were rational, then $\sqrt{2} = z - r$ would be a difference of rational numbers, hence rational, which it is not. So $z$ is irrational. The last sentence combines this with density of the rationals.
""", 2, 15, [
    r"You know one irrational number. Translate a rational number by it.",
    r"Find a rational $r$ in $(a - \sqrt{2}, b - \sqrt{2})$ and consider $r + \sqrt{2}$.",
], ["thm-density-rationals", "thm-square-roots", "thm-sqrt2-irrational"])

# ---------------------------------------------------------------- magnitude
s.definition("def-abs", "Absolute value", r"""
The \emph{absolute value} (or \emph{magnitude}) of $x \in \R$ is
\[ \abs{x} = \begin{cases} x & \text{if } x \ge 0, \\ -x & \text{if } x < 0. \end{cases} \]
Thus $\abs{x} \ge 0$, with $\abs{x} = 0$ only for $x = 0$, and $\abs{-x} = \abs{x}$. The number $\abs{x - y}$ is the \emph{distance} between $x$ and $y$.
""")

s.result("prop-triangle-inequality", "proposition", "Triangle inequality", r"""
Let $x, y, M \in \R$. Then:
\begin{enumerate}
\item $\abs{x} \le M$ if and only if $-M \le x \le M$;
\item $\abs{xy} = \abs{x}\abs{y}$;
\item $\abs{x + y} \le \abs{x} + \abs{y}$ (the triangle inequality);
\item $\big|\abs{x} - \abs{y}\big| \le \abs{x - y}$.
\end{enumerate}
""", r"""
(1) Suppose $\abs{x} \le M$; then $M \ge 0$. If $x \ge 0$ then $x = \abs{x} \le M$ and $-M \le 0 \le x$. If $x < 0$ then $-x = \abs{x} \le M$, so $x \ge -M$, and $x < 0 \le M$. Conversely, suppose $-M \le x \le M$. Then $x \le M$ and $-x \le M$; since $\abs{x}$ is one of $x$ and $-x$, $\abs{x} \le M$.

(2) If $x \ge 0$ and $y \ge 0$ then $xy \ge 0$ and $\abs{xy} = xy = \abs{x}\abs{y}$. If $x \ge 0$ and $y < 0$ then $xy \le 0$, so $\abs{xy} = -xy = x(-y) = \abs{x}\abs{y}$ (when $xy = 0$ both $\abs{xy}$ and $-xy$ are $0$). The case $x < 0$, $y \ge 0$ is the same with the roles exchanged. If $x < 0$ and $y < 0$ then $xy > 0$ and $\abs{xy} = xy = (-x)(-y) = \abs{x}\abs{y}$.

(3) By (1) applied with $M = \abs{x}$ and with $M = \abs{y}$, we have $-\abs{x} \le x \le \abs{x}$ and $-\abs{y} \le y \le \abs{y}$. Adding,
\[ -(\abs{x} + \abs{y}) \le x + y \le \abs{x} + \abs{y}, \]
and (1) with $M = \abs{x} + \abs{y}$ gives $\abs{x + y} \le \abs{x} + \abs{y}$.

(4) By (3), $\abs{x} = \abs{(x - y) + y} \le \abs{x - y} + \abs{y}$, so $\abs{x} - \abs{y} \le \abs{x - y}$. Exchanging $x$ and $y$, $\abs{y} - \abs{x} \le \abs{y - x} = \abs{x - y}$. Thus $-\abs{x - y} \le \abs{x} - \abs{y} \le \abs{x - y}$, and (1) gives the claim.
""", 2, 20, [
    r"Prove (1) by cases on the sign of $x$; it turns every later statement about absolute values into a pair of inequalities.",
    r"For (3), add $-\abs{x} \le x \le \abs{x}$ to the same statement for $y$ and apply (1). For (4), write $x = (x - y) + y$.",
], ["def-abs"])

s.result("prop-eps-principle", "proposition", "The epsilon principle", r"""
Let $a, b, x, y \in \R$.
\begin{enumerate}
\item If $a \le b + \eps$ for every $\eps > 0$, then $a \le b$.
\item If $\abs{x - y} \le \eps$ for every $\eps > 0$, then $x = y$.
\end{enumerate}
""", r"""
(1) Suppose $a > b$. Then $\eps = (a - b)/2 > 0$, and $b + \eps = (a + b)/2 < a$, so $a \le b + \eps$ fails for this $\eps$. Hence if the hypothesis holds for every $\eps > 0$, then $a \le b$.

(2) Suppose $x \ne y$. Then $\abs{x - y} > 0$, and $\eps = \abs{x - y}/2$ is positive with $\eps < \abs{x - y}$, so $\abs{x - y} \le \eps$ fails for this $\eps$. Hence if the hypothesis holds for every $\eps > 0$, then $x = y$.
""", 1, 10, [
    r"Prove the contrapositive: if $a > b$, exhibit one $\eps > 0$ for which the inequality fails.",
    r"Half the gap works: $\eps = (a - b)/2$.",
], ["def-abs"])

# ---------------------------------------------------------------- sequences
s.prose("cuts-sequences-intro", r"""
The least upper bound property is one way to say that $\R$ has no gaps. A second way speaks of sequences: terms that crowd together must be crowding around something. The rest of the section shows that the first kind of completeness implies the second.
""")

s.definition("def-convergence", "Sequence, convergence", r"""
A \emph{sequence} of real numbers is a function $\N \to \R$, written $(a_n)$ or $a_1, a_2, a_3, \dots$. The sequence $(a_n)$ \emph{converges} to the \emph{limit} $b \in \R$ if for every $\eps > 0$ there is an $N \in \N$ such that
\[ \abs{a_n - b} < \eps \quad\text{for all } n \ge N. \]
We then write $a_n \to b$ or $\lim_{n \to \infty} a_n = b$. A sequence that converges to some real number is \emph{convergent}.
""")

s.result("prop-limit-unique", "proposition", "Limits are unique", r"""
If $a_n \to b$ and $a_n \to b'$, then $b = b'$.
""", r"""
Let $\eps > 0$. There are $N_1, N_2 \in \N$ with $\abs{a_n - b} < \eps/2$ for $n \ge N_1$ and $\abs{a_n - b'} < \eps/2$ for $n \ge N_2$. For $n = \max(N_1, N_2)$ the triangle inequality gives
\[ \abs{b - b'} \le \abs{b - a_n} + \abs{a_n - b'} < \eps. \]
Since $\eps > 0$ was arbitrary, the $\eps$-principle gives $b = b'$.
""", 1, 10, [
    r"Estimate $\abs{b - b'}$ by passing through a single term $a_n$ with $n$ large, and use the $\eps$-principle.",
], ["def-convergence", "prop-triangle-inequality", "prop-eps-principle"])

s.definition("def-cauchy", "Cauchy sequence", r"""
A sequence $(a_n)$ of real numbers is a \emph{Cauchy sequence} (or satisfies the \emph{Cauchy condition}) if for every $\eps > 0$ there is an $N \in \N$ such that
\[ \abs{a_n - a_m} < \eps \quad\text{for all } n, m \ge N. \]
""")

s.result("lem-convergent-cauchy", "lemma", "Convergent sequences are Cauchy", r"""
Every convergent sequence of real numbers is a Cauchy sequence.
""", r"""
Let $a_n \to b$ and let $\eps > 0$. Choose $N$ with $\abs{a_n - b} < \eps/2$ for all $n \ge N$. If $n, m \ge N$, then by the triangle inequality
\[ \abs{a_n - a_m} \le \abs{a_n - b} + \abs{b - a_m} < \frac{\eps}{2} + \frac{\eps}{2} = \eps. \]
""", 1, 10, [
    r"Two terms that are both within $\eps/2$ of the limit are within $\eps$ of each other.",
], ["def-convergence", "def-cauchy", "prop-triangle-inequality"])

s.result("lem-cauchy-bounded", "lemma", "Cauchy sequences are bounded", r"""
If $(a_n)$ is a Cauchy sequence, then there is an $M \in \R$ with $\abs{a_n} \le M$ for all $n \in \N$.
""", r"""
Apply the Cauchy condition with $\eps = 1$: there is an $N$ with $\abs{a_n - a_m} < 1$ for all $n, m \ge N$. In particular, for $n \ge N$,
\[ \abs{a_n} \le \abs{a_n - a_N} + \abs{a_N} < 1 + \abs{a_N}. \]
Let $M = \max\set{\abs{a_1}, \dots, \abs{a_{N-1}}, \abs{a_N} + 1}$. Then $\abs{a_n} \le M$ for $n < N$ and for $n \ge N$.
""", 1, 10, [
    r"Use the Cauchy condition with $\eps = 1$ to control all terms past some index $N$ in terms of $a_N$; finitely many terms remain.",
], ["def-cauchy", "prop-triangle-inequality"])

s.result("thm-cauchy-complete", "theorem", "Cauchy sequences converge", r"""
Every Cauchy sequence of real numbers converges to a limit in $\R$. Together with the lemma that convergent sequences are Cauchy: a sequence in $\R$ converges if and only if it is a Cauchy sequence (the \emph{Cauchy convergence criterion}).
""", r"""
Let $(a_n)$ be a Cauchy sequence. Since Cauchy sequences are bounded, there is an $M$ with $-M \le a_n \le M$ for all $n$. Let
\[ X = \set{x \in \R : a_n \ge x \text{ for infinitely many } n \in \N}. \]
Then $-M \in X$, since $a_n \ge -M$ for every $n$. If $x \in X$ then $x \le a_n \le M$ for some $n$; so $M$ is an upper bound for $X$. By the least upper bound property, $b = \lub X$ exists. We show $a_n \to b$.

Let $\eps > 0$. By the Cauchy condition there is an $N$ with $\abs{a_n - a_m} < \eps/2$ for all $n, m \ge N$.

Since $b + \eps/2 > b$ and $b$ is an upper bound for $X$, $b + \eps/2 \notin X$: only finitely many $n$ satisfy $a_n \ge b + \eps/2$. Hence there is an $N_1 \ge N$ such that $a_n < b + \eps/2$ for all $n \ge N_1$.

Since $b - \eps/2 < b$, the number $b - \eps/2$ is not an upper bound for $X$, so there is an $x \in X$ with $x > b - \eps/2$. Infinitely many $n$ satisfy $a_n \ge x$, so there is an $m \ge N_1$ with $a_m \ge x > b - \eps/2$. For this $m$ we have $b - \eps/2 < a_m < b + \eps/2$, that is, $\abs{a_m - b} < \eps/2$.

Now let $n \ge N_1$. Since $n, m \ge N$,
\[ \abs{a_n - b} \le \abs{a_n - a_m} + \abs{a_m - b} < \frac{\eps}{2} + \frac{\eps}{2} = \eps. \]
Hence $a_n \to b$. The final assertion follows from this and the lemma that convergent sequences are Cauchy.
""", 4, 60, [
    r"The limit has to be produced from the least upper bound property, so you need a set whose least upper bound it is. The set of terms itself will not do (think of $a_n = 1/n$). The sequence is bounded; use that.",
    r"Let $X$ be the set of real $x$ such that $a_n \ge x$ for infinitely many $n$, and $b = \lub X$.",
    r"For $\eps > 0$: only finitely many terms are $\ge b + \eps/2$, and infinitely many are $> b - \eps/2$. So some far-out term $a_m$ is within $\eps/2$ of $b$; the Cauchy condition brings all later terms along.",
], ["thm-lub", "def-cauchy", "def-convergence", "lem-cauchy-bounded", "lem-convergent-cauchy", "prop-triangle-inequality"])

s.definition("def-monotone", "Monotone sequence", r"""
A sequence $(a_n)$ is \emph{nondecreasing} if $a_m \le a_n$ whenever $m \le n$, and \emph{nonincreasing} if $a_m \ge a_n$ whenever $m \le n$. It is \emph{monotone} if it is one or the other. It is \emph{bounded above} (\emph{below}) if the set $\set{a_n : n \in \N}$ is.
""")

s.result("prop-monotone-convergence", "proposition", "Bounded monotone sequences converge", r"""
A nondecreasing sequence $(a_n)$ that is bounded above converges, and its limit is $\lub \set{a_n : n \in \N}$. Likewise a nonincreasing sequence that is bounded below converges to $\glb \set{a_n : n \in \N}$.
""", r"""
Let $(a_n)$ be nondecreasing and bounded above. The set $\set{a_n : n \in \N}$ is nonempty and bounded above, so $b = \lub \set{a_n : n \in \N}$ exists. Let $\eps > 0$. Since $b - \eps$ is not an upper bound, there is an $N$ with $a_N > b - \eps$. For $n \ge N$ we have $a_n \ge a_N$ because the sequence is nondecreasing, and $a_n \le b$ because $b$ is an upper bound. So
\[ b - \eps < a_N \le a_n \le b, \]
and therefore $\abs{a_n - b} < \eps$ for all $n \ge N$. Hence $a_n \to b$.

If $(a_n)$ is nonincreasing and bounded below, then $(-a_n)$ is nondecreasing and bounded above, so $-a_n \to c$ where $c = \lub \set{-a_n}$. Then $\abs{a_n - (-c)} = \abs{-a_n - c}$ shows $a_n \to -c$. Moreover $-c$ is the greatest lower bound of $\set{a_n}$: $-a_n \le c$ gives $a_n \ge -c$ for all $n$, and if $\ell$ is a lower bound for $\set{a_n}$ then $-\ell$ is an upper bound for $\set{-a_n}$, so $c \le -\ell$, that is, $\ell \le -c$.
""", 2, 20, [
    r"The candidate for the limit is the least upper bound $b$ of the set of terms.",
    r"Given $\eps > 0$, $b - \eps$ is not an upper bound, so some term $a_N$ exceeds it. Where are the later terms?",
], ["thm-lub", "def-convergence", "def-monotone", "cor-glb"])

s.prose("cuts-limit-laws-intro", r"""
Limits of sequences are computed and compared by a handful of rules. They are used constantly in the later chapters, usually without comment, so they are proved here once: limits respect sums, products and quotients, and they respect weak inequalities.
""")

s.result("prop-limit-laws", "proposition", "Limit laws for sequences: sums and products", r"""
Let $(a_n)$ and $(b_n)$ be sequences of real numbers with $a_n \to a$ and $b_n \to b$, and let $k \in \R$. Then:
\begin{enumerate}
\item $(a_n)$ is bounded: there is an $M \in \R$ with $\abs{a_n} \le M$ for all $n$;
\item $a_n + b_n \to a + b$;
\item $a_n b_n \to ab$;
\item $k a_n \to ka$, and $a_n - b_n \to a - b$.
\end{enumerate}
""", r"""
(1) A convergent sequence is a Cauchy sequence, and Cauchy sequences are bounded.

(2) Let $\eps > 0$. Choose $N_1$ with $\abs{a_n - a} < \eps/2$ for $n \ge N_1$ and $N_2$ with $\abs{b_n - b} < \eps/2$ for $n \ge N_2$. For $n \ge \max(N_1, N_2)$ the triangle inequality gives
\[ \abs{(a_n + b_n) - (a + b)} \le \abs{a_n - a} + \abs{b_n - b} < \eps. \]

(3) By (1) there is an $M$ with $\abs{a_n} \le M$ for all $n$; then $M \ge 0$. For every $n$,
\[ a_n b_n - ab = a_n(b_n - b) + b(a_n - a). \]
Let $\eps > 0$. Choose $N_1$ with $\abs{b_n - b} < \dfrac{\eps}{2(M + 1)}$ for $n \ge N_1$ and $N_2$ with $\abs{a_n - a} < \dfrac{\eps}{2(\abs{b} + 1)}$ for $n \ge N_2$. For $n \ge \max(N_1, N_2)$,
\[ \abs{a_n b_n - ab} \le \abs{a_n}\abs{b_n - b} + \abs{b}\abs{a_n - a} \le \frac{M}{M + 1} \cdot \frac{\eps}{2} + \frac{\abs{b}}{\abs{b} + 1} \cdot \frac{\eps}{2} < \eps, \]
because $M/(M + 1) < 1$ and $\abs{b}/(\abs{b} + 1) < 1$.

(4) The constant sequence $k, k, k, \dots$ converges to $k$ (any $N$ serves every $\eps$), so $k a_n \to ka$ by (3). In particular $-b_n = (-1)b_n \to -b$, and then $a_n - b_n = a_n + (-b_n) \to a - b$ by (2).
""", 3, 30, [
    r"The sum is an $\eps/2$ argument. For the product, the difference $a_n b_n - ab$ must be written in terms of $a_n - a$ and $b_n - b$.",
    r"$a_n b_n - ab = a_n(b_n - b) + b(a_n - a)$. The factor $a_n$ changes with $n$, so you need a bound on $\abs{a_n}$ that holds for all $n$: convergent sequences are Cauchy, and Cauchy sequences are bounded.",
], ["def-convergence", "prop-triangle-inequality", "lem-convergent-cauchy", "lem-cauchy-bounded"])

s.result("prop-limit-quotient", "proposition", "Limit laws for sequences: quotients", r"""
Let $a_n \to a$ and $b_n \to b$, where $b \ne 0$ and $b_n \ne 0$ for every $n$. Then
\[ \frac{1}{b_n} \to \frac{1}{b} \qquad\text{and}\qquad \frac{a_n}{b_n} \to \frac{a}{b}. \]
""", r"""
Since $\abs{b}/2 > 0$ there is an $N_1$ with $\abs{b_n - b} < \abs{b}/2$ for $n \ge N_1$. For such $n$, the inequality $\abs{b} - \abs{b_n} \le \abs{b - b_n}$ gives
\[ \abs{b_n} \ge \abs{b} - \abs{b_n - b} > \frac{\abs{b}}{2}, \qquad\text{so}\qquad \frac{1}{\abs{b_n}} < \frac{2}{\abs{b}}. \]
Let $\eps > 0$, and choose $N_2$ with $\abs{b_n - b} < \eps\abs{b}^2/2$ for $n \ge N_2$. For $n \ge \max(N_1, N_2)$,
\[ \abs{\frac{1}{b_n} - \frac{1}{b}} = \frac{\abs{b - b_n}}{\abs{b_n}\abs{b}} < \frac{\eps\abs{b}^2}{2} \cdot \frac{2}{\abs{b}} \cdot \frac{1}{\abs{b}} = \eps. \]
Hence $1/b_n \to 1/b$. Finally $a_n/b_n = a_n \cdot (1/b_n) \to a \cdot (1/b) = a/b$ by the limit law for products.
""", 3, 25, [
    r"$\dfrac{1}{b_n} - \dfrac{1}{b} = \dfrac{b - b_n}{b_n b}$. The numerator is small; the danger is a small denominator.",
    r"First find $N_1$ beyond which $\abs{b_n} > \abs{b}/2$, using $\abs{b_n} \ge \abs{b} - \abs{b_n - b}$. Then make $\abs{b_n - b} < \eps\abs{b}^2/2$.",
], ["def-convergence", "prop-triangle-inequality", "prop-limit-laws"])

s.result("prop-limit-order", "proposition", "Limits respect weak inequalities; the squeeze", r"""
Let $(a_n)$, $(b_n)$, $(x_n)$ be sequences of real numbers and $n_0 \in \N$.
\begin{enumerate}
\item If $a_n \to a$, $b_n \to b$, and $a_n \le b_n$ for all $n \ge n_0$, then $a \le b$. In particular, if $a_n \le K$ (respectively $a_n \ge K$) for all $n \ge n_0$, then $a \le K$ (respectively $a \ge K$).
\item (\emph{Squeeze.}) If $a_n \le x_n \le b_n$ for all $n \ge n_0$, and $a_n \to L$ and $b_n \to L$, then $(x_n)$ converges and $x_n \to L$.
\end{enumerate}
Strict inequalities are not preserved: $0 < 1/n$ for all $n$, and $1/n \to 0$.
""", r"""
(1) Suppose $a > b$ and let $\eps = (a - b)/2 > 0$. There are $N_1, N_2$ with $\abs{a_n - a} < \eps$ for $n \ge N_1$ and $\abs{b_n - b} < \eps$ for $n \ge N_2$. Take $n = \max(n_0, N_1, N_2)$. Then
\[ b_n < b + \eps = \frac{a + b}{2} = a - \eps < a_n, \]
contradicting $a_n \le b_n$. Hence $a \le b$. For the particular cases, compare $(a_n)$ with the constant sequence $K, K, \dots$, which converges to $K$.

(2) Let $\eps > 0$. There are $N_1, N_2$ with $\abs{a_n - L} < \eps$ for $n \ge N_1$ and $\abs{b_n - L} < \eps$ for $n \ge N_2$. For $n \ge \max(n_0, N_1, N_2)$,
\[ L - \eps < a_n \le x_n \le b_n < L + \eps, \]
so $\abs{x_n - L} < \eps$. Hence $x_n \to L$.

For the last sentence: $1/n \to 0$ because, given $\eps > 0$, the Archimedean property gives $N$ with $1/N < \eps$, and then $\abs{1/n - 0} = 1/n \le 1/N < \eps$ for $n \ge N$.
""", 2, 20, [
    r"For (1) argue by contradiction: if $a > b$, the terms $a_n$ are eventually close to $a$ and the terms $b_n$ close to $b$, with a gap between.",
    r"Use $\eps = (a - b)/2$ in (1). In (2), for large $n$ both $a_n$ and $b_n$ lie in $(L - \eps, L + \eps)$, and $x_n$ is between them.",
], ["def-convergence", "prop-triangle-inequality", "thm-archimedean"])

s.result("ex-e-irrational", "exercise", "The number e is irrational", r"""
For $n \ge 0$ let $s_n = \displaystyle\sum_{k=0}^{n} \frac{1}{k!} = 1 + 1 + \frac{1}{2!} + \dots + \frac{1}{n!}$.
\begin{enumerate}
\item Prove that $s_n < 3$ for all $n$, so that $e = \lub \set{s_n : n \ge 0}$ exists (and $s_n \to e$).
\item Prove that $e$ is irrational.
\end{enumerate}
You may use the finite geometric sum $\sum_{j=0}^{J-1} r^j = \dfrac{1 - r^J}{1 - r}$ for $r \ne 1$.
""", r"""
(1) First, $k! \ge 2^{k-1}$ for all $k \ge 1$, by induction: $1! = 1 = 2^0$, and if $k! \ge 2^{k-1}$ then $(k+1)! = (k+1)\,k! \ge 2 \cdot 2^{k-1} = 2^k$. Hence for $n \ge 1$
\[ s_n = 1 + \sum_{k=1}^{n} \frac{1}{k!} \le 1 + \sum_{k=1}^{n} \frac{1}{2^{k-1}} = 1 + \frac{1 - 2^{-n}}{1 - \frac12} = 3 - 2^{1-n} < 3, \]
and $s_0 = 1 < 3$. So $\set{s_n}$ is nonempty and bounded above, and $e = \lub \set{s_n}$ exists. Since $s_{n+1} - s_n = 1/(n+1)! > 0$, the sequence is nondecreasing, and it converges to $e$ because bounded monotone sequences converge to their least upper bound.

(2) Suppose $e$ is rational. Since $e \ge s_0 = 1 > 0$, we can write $e = p/q$ with $p, q \in \N$, and replacing $p, q$ by $2p, 2q$ if necessary we may assume $q \ge 2$.

Let $m > q$. For $q < k \le m$, the integer $k!/q! = (q+1)(q+2)\cdots k$ is a product of $k - q$ factors each at least $q + 1$, so $q!/k! \le r^{k-q}$ where $r = 1/(q+1)$. Therefore
\[ q!\,(s_m - s_q) = \sum_{k=q+1}^{m} \frac{q!}{k!} \le \sum_{j=1}^{m-q} r^j = r\,\frac{1 - r^{m-q}}{1 - r} < \frac{r}{1 - r} = \frac{1}{q}. \]
So $s_m < s_q + \dfrac{1}{q \cdot q!}$ for all $m > q$; and $s_m \le s_q$ for $m \le q$. Thus $s_q + \dfrac{1}{q \cdot q!}$ is an upper bound for $\set{s_n}$, and so $e \le s_q + \dfrac{1}{q \cdot q!}$. On the other hand $e \ge s_{q+1} > s_q$. Multiplying by $q!$,
\[ 0 < q!\,(e - s_q) \le \frac{1}{q} \le \frac{1}{2}. \]
But $q!\,e = (q-1)!\,p$ is an integer, and $q!\,s_q = \sum_{k=0}^{q} q!/k!$ is a sum of integers, since $k!$ divides $q!$ for $k \le q$. So $q!\,(e - s_q)$ is an integer strictly between $0$ and $1$, which is impossible. Hence $e$ is irrational.
""", 4, 60, [
    r"For (1), compare $1/k!$ with a geometric sequence: $k! \ge 2^{k-1}$.",
    r"For (2), suppose $e = p/q$ and look at the number $q!\,(e - s_q)$. Why is it an integer? Why is it positive?",
    r"Bound the tail: for $k > q$, $q!/k! \le (q+1)^{-(k-q)}$, and a geometric sum shows $q!\,(s_m - s_q) < 1/q$ for every $m > q$. An integer cannot lie strictly between $0$ and $1$.",
], ["thm-lub", "def-upper-bound", "prop-monotone-convergence"])

s.remark("cuts-outro", r"""
One can show that any two complete ordered fields are isomorphic, so the construction by cuts could be replaced by any other that yields the four properties, and nothing later would change. This is why, from here on, real numbers are handled by their properties and never as pairs of sets of rationals.
""")

# ---------------------------------------------------------------- cards
s.card("cut", r"Define a cut in $\Q$.",
       r"A pair $A|B$ of subsets of $\Q$ with: $A \cup B = \Q$, $A \cap B = \varnothing$, both nonempty; $a < b$ whenever $a \in A$, $b \in B$; and $A$ has no largest element.", "def-cut")
s.card("cut-order", r"How is $x \le y$ defined for cuts $x = A|B$ and $y = C|D$? Why is it a total order?",
       r"$x \le y$ means $A \subset C$. If $A \not\subset C$, some $a \in A$ lies in $D$, so it is above all of $C$, and downward closure of $A$ forces $C \subset A$.", "prop-order-total")
s.card("lub-def", r"Define the least upper bound of a set $S \subset \R$.",
       r"An upper bound $M$ of $S$ (so $s \le M$ for all $s \in S$) such that $M \le M'$ for every upper bound $M'$ of $S$.", "def-upper-bound")
s.card("lub-property", r"State the least upper bound property of $\R$, and give the idea of its proof for cuts.",
       r"Every nonempty subset of $\R$ that is bounded above has a least upper bound. Proof idea: take the union of the left-hand parts of the cuts in $S$; the upper bound guarantees the complement is nonempty.", "thm-lub")
s.card("archimedean", r"State the Archimedean property and the idea of its proof.",
       r"For every $x \in \R$ there is $n \in \N$ with $n > x$ (so $1/n < \eps$ for some $n$). If not, $b = \lub \N$ exists; some $n > b - 1$, and then $n + 1 > b$.", "thm-archimedean")
s.card("density", r"Why is there a rational number between any two reals $a < b$?",
       r"Pick $n$ with $1/n < b - a$ (Archimedean) and let $m$ be the least integer greater than $na$. Then $na < m \le na + 1 < nb$, so $a < m/n < b$.", "thm-density-rationals")
s.card("sqrt", r"How is $\sqrt{c}$ produced for $c > 0$?",
       r"As $y = \lub\set{t \ge 0 : t^2 \le c}$. If $y^2 < c$, a slightly larger number is still in the set; if $y^2 > c$, a slightly smaller number is still an upper bound.", "thm-square-roots")
s.card("eps-principle", r"State the $\eps$-principle.",
       r"If $a \le b + \eps$ for every $\eps > 0$ then $a \le b$. If $\abs{x - y} \le \eps$ for every $\eps > 0$ then $x = y$.", "prop-eps-principle")
s.card("cauchy-def", r"Define a Cauchy sequence.",
       r"For every $\eps > 0$ there is an $N$ such that $\abs{a_n - a_m} < \eps$ for all $n, m \ge N$.", "def-cauchy")
s.card("limit-laws", r"State the limit laws for sequences $a_n \to a$, $b_n \to b$.",
       r"$a_n + b_n \to a + b$; $a_n b_n \to ab$; $k a_n \to ka$; if $b \ne 0$ and all $b_n \ne 0$, $a_n/b_n \to a/b$. Weak inequalities pass to the limit ($a_n \le b_n$ eventually gives $a \le b$), and a sequence squeezed between two sequences with the same limit $L$ converges to $L$.", "prop-limit-order")
s.card("monotone-convergence", r"What does a bounded monotone sequence do?",
       r"It converges: a nondecreasing sequence bounded above converges to the least upper bound of its terms, a nonincreasing one bounded below to the greatest lower bound.", "prop-monotone-convergence")
s.card("cauchy-complete", r"State the Cauchy convergence criterion and name the set whose least upper bound is the limit.",
       r"A sequence in $\R$ converges if and only if it is Cauchy. The limit is $\lub X$ where $X = \set{x : a_n \ge x \text{ for infinitely many } n}$.", "thm-cauchy-complete")

s.write()
