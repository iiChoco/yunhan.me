from __future__ import annotations

import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from c6common import prose, note, result, card, write

B = []

B.append(prose("c6-om-intro", r"""
How large is a subset of $\R^n$? For an interval the answer is its length, for a rectangle its area, for a box its volume. Lebesgue's idea is to measure an arbitrary set $A$ from the outside: cover $A$ by countably many boxes, add up their volumes, and take the most economical covering. The number so obtained, the \emph{outer measure} of $A$, is defined for every set whatsoever. This section sets it up and proves the one fact that is not a formality: a box is as large as it should be.

Throughout the chapter $n \ge 1$ is fixed, sums of nonnegative terms take values in $[0,\infty]$, and such sums may be reordered and regrouped freely.
"""))

B.append(note("definition", "c6-def-box", "Boxes and their volume", r"""
The \emph{length} of a bounded interval $I \subseteq \R$ is $\abs{I} = b - a$ if $I$ is nonempty with $a = \inf I$ and $b = \sup I$, and $\abs{\emptyset} = 0$. (So $(a,b)$, $[a,b]$, $[a,b)$, $(a,b]$ all have length $b-a$, and a single point has length $0$.)

A \emph{box} in $\R^n$ is a product $B = I_1 \times \dots \times I_n$ of bounded intervals. Its \emph{volume} is
\[ \abs{B} = \abs{I_1}\,\abs{I_2}\cdots\abs{I_n}. \]
The box is \emph{open} if each $I_i$ is an open interval $(a_i,b_i)$ with $a_i \le b_i$ (so the empty set is an open box), and \emph{closed} if each $I_i$ is a closed interval $[a_i,b_i]$ or empty. For $n=1$ boxes are intervals and for $n=2$ they are rectangles. A \emph{cube} is a box whose intervals all have the same length, its \emph{side}.
"""))

B.append(prose("c6-om-count-prose", r"""
To compare volumes of boxes that overlap in complicated ways we count lattice points. The points of the fine lattice $\tfrac1N\Z^n$ inside a box number about $N^n$ times its volume, and counting respects inclusions and disjointness for free.
"""))

B.append(result("lemma", "c6-lem-integer-count", "Counting lattice points in an interval", r"""
Let $I \subseteq \R$ be a bounded interval and $N \in \N$. Let $c$ be the number of points of $\tfrac1N\Z = \set{j/N : j \in \Z}$ that lie in $I$. Then
\[ N\abs{I} - 1 \;\le\; c \;\le\; N\abs{I} + 1. \]
""", r"""
If $I = \emptyset$ then $c = 0$ and $\abs{I} = 0$, and the inequalities hold. Otherwise let $a = \inf I \le b = \sup I$, so that $(a,b) \subseteq I \subseteq [a,b]$. A point $j/N$ lies in $[a,b]$ exactly when $Na \le j \le Nb$, and in $(a,b)$ exactly when $Na < j < Nb$.

\emph{Upper bound.} Suppose the integers in $[Na, Nb]$ are $j_1 < j_2 < \dots < j_r$ with $r \ge 1$. Consecutive integers differ by at least $1$, so $j_r - j_1 \ge r - 1$, while $j_r - j_1 \le Nb - Na$. Hence $r \le N(b-a) + 1$, and this also holds when $r = 0$. Since $c \le r$, we get $c \le N\abs{I} + 1$.

\emph{Lower bound.} Let $j_0$ be the greatest integer with $j_0 \le Na$. The integers greater than $Na$ are exactly $j_0 + 1, j_0 + 2, \dots$. Let $s \ge 0$ be the number of integers in $(Na, Nb)$; they are $j_0+1, \dots, j_0+s$, and $j_0 + s + 1$ is not among them, so $j_0 + s + 1 \ge Nb$. Therefore
\[ s \ge Nb - j_0 - 1 \ge Nb - Na - 1 . \]
Since $c \ge s$, we get $c \ge N\abs{I} - 1$.
""", 2, 15, [
    r"Translate the question: $j/N \in [a,b]$ means $Na \le j \le Nb$. How many integers can a closed interval of length $\ell$ hold, and how few can an open one hold?",
    r"For the upper bound, the largest and smallest integers in $[Na,Nb]$ are at least (their number minus one) apart. For the lower bound, start from the greatest integer $\le Na$ and step up by ones until you pass $Nb$.",
], ["c6-def-box"]))

B.append(result("lemma", "c6-lem-lattice-volume", "Lattice points measure volume", r"""
For a box $B \subseteq \R^n$ and $N \in \N$ let $c_N(B)$ be the number of points of $\tfrac1N\Z^n$ that lie in $B$. Then
\[ \lim_{N \to \infty} \frac{c_N(B)}{N^n} = \abs{B}. \]
""", r"""
Write $B = I_1 \times \dots \times I_n$. A point $(j_1/N, \dots, j_n/N)$ lies in $B$ exactly when $j_i/N \in I_i$ for every $i$, so the lattice points in $B$ are obtained by choosing a point of $\tfrac1N\Z \cap I_i$ independently for each $i$. Hence $c_N(B) = c_N(I_1)\cdots c_N(I_n)$, where $c_N(I_i)$ is the number of points of $\tfrac1N\Z$ in $I_i$, and
\[ \frac{c_N(B)}{N^n} = \prod_{i=1}^n \frac{c_N(I_i)}{N}. \]
By the lemma on counting lattice points in an interval, $\abs{I_i} - \tfrac1N \le c_N(I_i)/N \le \abs{I_i} + \tfrac1N$, so $c_N(I_i)/N \to \abs{I_i}$ as $N \to \infty$. A product of $n$ convergent sequences converges to the product of the limits, which is $\abs{B}$.
""", 2, 15, [
    r"The lattice points in a product are the products of the lattice points in the factors.",
    r"$c_N(B) = \prod_i c_N(I_i)$, and the previous lemma traps $c_N(I_i)/N$ within $1/N$ of $\abs{I_i}$.",
], ["c6-def-box", "c6-lem-integer-count"]))

B.append(result("lemma", "c6-lem-finite-box-cover", "Finite coverings and packings of a box", r"""
Let $B, B_1, \dots, B_m$ be boxes in $\R^n$.

(a) If $B \subseteq B_1 \cup \dots \cup B_m$, then $\abs{B} \le \abs{B_1} + \dots + \abs{B_m}$.

(b) If $B_1, \dots, B_m$ are pairwise disjoint and each is contained in $B$, then $\abs{B_1} + \dots + \abs{B_m} \le \abs{B}$.
""", r"""
Let $c_N(\cdot)$ count the points of $\tfrac1N\Z^n$ in a box.

(a) Every lattice point in $B$ lies in at least one $B_k$, so $c_N(B) \le c_N(B_1) + \dots + c_N(B_m)$. Divide by $N^n$ and let $N \to \infty$. By the lemma that lattice points measure volume, the left side tends to $\abs{B}$ and the right side to $\sum_k \abs{B_k}$; limits preserve weak inequalities, so $\abs{B} \le \sum_k \abs{B_k}$.

(b) Every lattice point lies in at most one $B_k$, and those that lie in some $B_k$ lie in $B$, so $c_N(B_1) + \dots + c_N(B_m) \le c_N(B)$. Dividing by $N^n$ and letting $N \to \infty$ gives $\sum_k \abs{B_k} \le \abs{B}$.
""", 2, 15, [
    r"Compare the numbers of points of $\tfrac1N\Z^n$ in the boxes, where inclusion and disjointness give inequalities at once.",
    r"Divide the counting inequality by $N^n$ and let $N \to \infty$.",
], ["c6-lem-lattice-volume"]))

B.append(note("definition", "c6-def-outer-measure", "Outer measure", r"""
The \emph{(Lebesgue) outer measure} of a set $A \subseteq \R^n$ is
\[ m^*A = \inf \set{ \sum_{k=1}^\infty \abs{B_k} \;:\; B_1, B_2, \dots \text{ are open boxes with } A \subseteq \bigcup_{k=1}^\infty B_k } \in [0, \infty]. \]
Such coverings always exist, for instance $B_k = (-k,k)^n$. Because the empty set is an open box of volume $0$, coverings by finitely many open boxes are included. When the dimension needs emphasis we speak of the outer measure \emph{in} $\R^n$; for $n = 1$ it is defined with open intervals and for $n = 2$ with open rectangles.
"""))

B.append(result("proposition", "c6-prop-outer-basic", "First properties of outer measure", r"""
(a) $m^*\emptyset = 0$.

(b) (Monotonicity) If $A \subseteq A' \subseteq \R^n$, then $m^*A \le m^*A'$.

(c) $m^*\set{p} = 0$ for every point $p \in \R^n$.
""", r"""
(a) The empty open box covers $\emptyset$ and has volume $0$, so $m^*\emptyset \le 0$.

(b) Every covering of $A'$ by open boxes is also a covering of $A$. So the set of totals over which the infimum for $m^*A$ is taken contains the corresponding set for $m^*A'$, and the infimum over a larger set is no larger: $m^*A \le m^*A'$.

(c) Let $\eps > 0$ and put $\delta = \min(\eps, 1)/2$. The open cube $\prod_{i=1}^n (p_i - \delta/2, p_i + \delta/2)$ contains $p$ and has volume $\delta^n \le \delta < \eps$, since $0 < \delta < 1$. Hence $m^*\set{p} < \eps$ for every $\eps > 0$, so $m^*\set{p} = 0$.
""", 1, 10, [
    r"Each part is a direct look at which coverings are available.",
], ["c6-def-outer-measure"]))

B.append(result("theorem", "c6-thm-countable-subadditivity", "Countable subadditivity", r"""
For any sets $A_1, A_2, \dots \subseteq \R^n$,
\[ m^*\Bigl( \bigcup_{j=1}^\infty A_j \Bigr) \le \sum_{j=1}^\infty m^*A_j. \]
The same holds for finitely many sets.
""", r"""
If $\sum_j m^*A_j = \infty$ there is nothing to prove, so assume the sum is finite; in particular each $m^*A_j$ is finite. Let $\eps > 0$. For each $j$, the definition of the infimum gives open boxes $B_{j,1}, B_{j,2}, \dots$ covering $A_j$ with
\[ \sum_{k=1}^\infty \abs{B_{j,k}} \le m^*A_j + \frac{\eps}{2^j}. \]
The family $\set{B_{j,k} : j, k \in \N}$ is countable, since $\N \times \N$ is countable, and it covers $\bigcup_j A_j$. Listing it as a single sequence and using that a sum of nonnegative terms does not depend on the order or grouping of its terms,
\[ m^*\Bigl( \bigcup_j A_j \Bigr) \le \sum_{j=1}^\infty \sum_{k=1}^\infty \abs{B_{j,k}} \le \sum_{j=1}^\infty \Bigl( m^*A_j + \frac{\eps}{2^j} \Bigr) = \sum_{j=1}^\infty m^*A_j + \eps. \]
As $\eps > 0$ was arbitrary, the inequality follows. For finitely many sets $A_1, \dots, A_r$, apply the result with $A_j = \emptyset$ for $j > r$, using $m^*\emptyset = 0$.
""", 2, 20, [
    r"Cover each $A_j$ almost optimally and put all the coverings together.",
    r"Allow the $j$-th covering an excess of $\eps/2^j$, so the total excess is $\eps$.",
], ["c6-def-outer-measure", "c6-prop-outer-basic"]))

B.append(prose("c6-om-box-prose", r"""
Nothing so far rules out the absurd possibility that every set has outer measure zero. The next theorem does: clever countable coverings cannot make a box smaller than its volume. Compactness reduces a countable covering to a finite one, and the lattice count handles finite coverings.
"""))

B.append(result("lemma", "c6-lem-box-approx", "Boxes are nearly open and nearly closed", r"""
Let $B \subseteq \R^n$ be a box and $\eps > 0$. Then there are an open box $B^+ \supseteq B$ with $\abs{B^+} \le \abs{B} + \eps$ and a closed box $B^- \subseteq B$ with $\abs{B^-} \ge \abs{B} - \eps$.
""", r"""
If $B = \emptyset$, take $B^+ = B^- = \emptyset$. Otherwise write $B = I_1 \times \dots \times I_n$ with $a_i = \inf I_i \le b_i = \sup I_i$.

\emph{The open box.} For $\delta > 0$ the open box $B_\delta = \prod_i (a_i - \delta, b_i + \delta)$ contains $\prod_i [a_i, b_i] \supseteq B$, and its volume is $p(\delta) = \prod_i (b_i - a_i + 2\delta)$. This is a polynomial in $\delta$, hence continuous, with $p(0) = \abs{B}$. So there is a $\delta > 0$ with $p(\delta) \le \abs{B} + \eps$; take $B^+ = B_\delta$.

\emph{The closed box.} If $\abs{B} = 0$, take $B^- = \emptyset$. Otherwise $a_i < b_i$ for every $i$. For $0 < \delta < \tfrac12 \min_i (b_i - a_i)$ the closed box $\prod_i [a_i + \delta, b_i - \delta]$ is contained in $\prod_i (a_i, b_i) \subseteq B$, and its volume $q(\delta) = \prod_i (b_i - a_i - 2\delta)$ is continuous in $\delta$ with $q(0) = \abs{B}$. Choose $\delta$ so small that $q(\delta) \ge \abs{B} - \eps$ and take $B^-$ to be that closed box.
""", 1, 10, [
    r"Fatten or shrink every side by the same small $\delta$; the volume is a polynomial in $\delta$.",
], ["c6-def-box"]))

B.append(result("theorem", "c6-thm-box-measure", "The outer measure of a box is its volume", r"""
For every box $B \subseteq \R^n$, $m^*B = \abs{B}$. In particular $m^*[a,b] = m^*(a,b) = b - a$ in $\R$ whenever $a \le b$.
""", r"""
\emph{$m^*B \le \abs{B}$.} Let $\eps > 0$. By the lemma that boxes are nearly open, there is an open box $B^+ \supseteq B$ with $\abs{B^+} \le \abs{B} + \eps$. The single box $B^+$ is a covering of $B$, so $m^*B \le \abs{B} + \eps$. As $\eps$ is arbitrary, $m^*B \le \abs{B}$.

\emph{$m^*B \ge \abs{B}$.} Let $B_1, B_2, \dots$ be open boxes covering $B$, and let $\eps > 0$. Choose a closed box $B^- \subseteq B$ with $\abs{B^-} \ge \abs{B} - \eps$. The set $B^-$ is closed and bounded in $\R^n$, hence compact by the Heine–Borel theorem, and the open sets $B_k$ cover it. So finitely many of them cover it: $B^- \subseteq B_1 \cup \dots \cup B_m$ for some $m$. By part (a) of the lemma on finite coverings of a box,
\[ \abs{B} - \eps \le \abs{B^-} \le \sum_{k=1}^m \abs{B_k} \le \sum_{k=1}^\infty \abs{B_k}. \]
Since $\eps$ is arbitrary, $\abs{B} \le \sum_k \abs{B_k}$ for every covering of $B$ by open boxes. Taking the infimum over coverings, $\abs{B} \le m^*B$.
""", 3, 35, [
    r"One inequality needs a single slightly larger open box. For the other, you must show that \emph{every} countable covering by open boxes has total volume at least $\abs{B}$.",
    r"Shrink $B$ to a closed box of almost the same volume. Closed boxes are compact, so a countable open covering has a finite subcovering.",
    r"For a finite covering of a box by boxes, the volume inequality was proved by counting lattice points.",
], ["c6-def-outer-measure", "c6-lem-box-approx", "c6-lem-finite-box-cover"]))

B.append(result("corollary", "c6-cor-any-boxes", "Any boxes may be used", r"""
If $A \subseteq \bigcup_{k=1}^\infty B_k$ where the $B_k$ are boxes of any kind (open, closed, or neither), then
\[ m^*A \le \sum_{k=1}^\infty \abs{B_k}. \]
Consequently $m^*A$ is also the infimum of $\sum_k \abs{B_k}$ over all countable coverings of $A$ by arbitrary boxes.
""", r"""
By monotonicity, countable subadditivity, and the theorem that the outer measure of a box is its volume,
\[ m^*A \le m^*\Bigl( \bigcup_k B_k \Bigr) \le \sum_k m^*B_k = \sum_k \abs{B_k}. \]
For the last statement, let $\mu$ be the infimum of $\sum_k \abs{B_k}$ over countable coverings of $A$ by arbitrary boxes. What was just shown gives $m^*A \le \mu$. Conversely, coverings by open boxes are among the coverings by arbitrary boxes, so the infimum over the larger family satisfies $\mu \le m^*A$.
""", 1, 10, [
    r"Combine monotonicity, subadditivity, and $m^*B = \abs{B}$.",
], ["c6-prop-outer-basic", "c6-thm-countable-subadditivity", "c6-thm-box-measure"]))

B.append(note("definition", "c6-def-zero-set", "Zero set", r"""
A set $Z \subseteq \R^n$ is a \emph{zero set} (or \emph{null set}) if $m^*Z = 0$; that is, if for every $\eps > 0$ there are countably many open boxes that cover $Z$ and have total volume less than $\eps$.
"""))

B.append(result("proposition", "c6-prop-zero-sets", "Zero sets", r"""
(a) Every subset of a zero set is a zero set.

(b) A countable union of zero sets is a zero set.

(c) Every countable subset of $\R^n$ is a zero set. In particular $\Q$ is a zero set in $\R$.
""", r"""
(a) If $A \subseteq Z$ and $m^*Z = 0$, monotonicity gives $0 \le m^*A \le m^*Z = 0$.

(b) If $m^*Z_j = 0$ for all $j$, countable subadditivity gives $m^*\bigl(\bigcup_j Z_j\bigr) \le \sum_j 0 = 0$.

(c) A countable set is a countable union of one-point sets, each of which has outer measure $0$ by the first properties of outer measure; apply (b). The set $\Q$ is countable.
""", 1, 10, [
    r"Use monotonicity for (a), countable subadditivity for (b), and points for (c).",
], ["c6-def-zero-set", "c6-prop-outer-basic", "c6-thm-countable-subadditivity"]))

B.append(result("proposition", "c6-prop-hyperplane-zero", "Coordinate hyperplanes are zero sets", r"""
For $1 \le i \le n$ and $c \in \R$, the set $H = \set{x \in \R^n : x_i = c}$ is a zero set in $\R^n$.
""", r"""
For $k \in \N$ let $B_k$ be the box $I_1 \times \dots \times I_n$ with $I_i = \set{c} = [c,c]$ and $I_j = [-k, k]$ for $j \ne i$. Since $\abs{I_i} = 0$, $\abs{B_k} = 0$, so $m^*B_k = 0$ by the theorem that the outer measure of a box is its volume. Every $x \in H$ lies in $B_k$ as soon as $k \ge \abs{x_j}$ for all $j$, so $H = \bigcup_k B_k$ is a countable union of zero sets, hence a zero set.
""", 1, 10, [
    r"Exhaust the hyperplane by countably many boxes that have one side of length $0$.",
], ["c6-thm-box-measure", "c6-prop-zero-sets"]))

B.append(result("exercise", "c6-ex-interval-uncountable", "Boxes with interior are not zero sets", r"""
Show that a box $B \subseteq \R^n$ with $\abs{B} > 0$ is not a zero set, and deduce that the interval $[0,1]$ is uncountable.
""", r"""
By the theorem on the outer measure of a box, $m^*B = \abs{B} > 0$, so $B$ is not a zero set. In particular $m^*[0,1] = 1 \ne 0$. Every countable set is a zero set, so $[0,1]$ is not countable.
""", 1, 5, [
    r"What is $m^*[0,1]$, and what is the outer measure of a countable set?",
], ["c6-thm-box-measure", "c6-prop-zero-sets"]))

B.append(result("exercise", "c6-ex-cantor-zero", "The Cantor set is a zero set", r"""
Let $C = \bigcap_{k \ge 0} C^k$ be the standard middle-thirds Cantor set, where $C^0 = [0,1]$ and $C^k$ is the union of $2^k$ closed intervals of length $3^{-k}$ obtained by removing the open middle third of each interval of $C^{k-1}$. Show that $C$ is a zero set in $\R$. (So a zero set can be uncountable.)
""", r"""
For each $k$, $C \subseteq C^k$, and $C^k$ is a union of $2^k$ intervals each of length $3^{-k}$. Since arbitrary boxes may be used in coverings,
\[ m^*C \le 2^k \cdot 3^{-k} = \Bigl(\tfrac23\Bigr)^k \quad \text{for every } k. \]
As $(2/3)^k \to 0$, $m^*C = 0$.
""", 1, 10, [
    r"The $k$-th stage of the construction is already a covering by finitely many intervals. What is its total length?",
], ["c6-cor-any-boxes", "c6-def-zero-set"]))

B.append(note("remark", "c6-rem-outer-not-additive", "What outer measure lacks", r"""
Outer measure is defined for every set, is monotone and countably subadditive, and gives boxes their volume. What one wants in addition is \emph{additivity}: $m^*(A \sqcup A') = m^*A + m^*A'$ for disjoint sets. This fails for some pairs of sets (an example is built in the section on regularity). The remedy, in the next section, is to restrict attention to the sets that split every other set additively.
"""))

C = [
    card("c6-card-outer-measure", "c6-def-outer-measure", r"Define the outer measure $m^*A$ of $A \subseteq \R^n$.", r"$m^*A = \inf \sum_k \abs{B_k}$ over all countable coverings of $A$ by open boxes $B_k$."),
    card("c6-card-outer-axioms", "c6-thm-countable-subadditivity", r"State the three basic properties of outer measure.", r"$m^*\emptyset = 0$; monotone: $A \subseteq A' \Rightarrow m^*A \le m^*A'$; countably subadditive: $m^*(\bigcup_j A_j) \le \sum_j m^*A_j$."),
    card("c6-card-subadditivity-idea", "c6-thm-countable-subadditivity", r"What is the idea of the proof of countable subadditivity?", r"Cover $A_j$ by open boxes with total volume at most $m^*A_j + \eps/2^j$; all these boxes together cover the union with excess at most $\eps$."),
    card("c6-card-box-measure", "c6-thm-box-measure", r"What is $m^*B$ for a box $B$, and what are the two ideas behind the hard inequality?", r"$m^*B = \abs{B}$. Shrink to a closed box and use compactness to get a finite subcovering; then compare volumes of finitely many boxes by counting points of $\tfrac1N\Z^n$."),
    card("c6-card-lattice", "c6-lem-lattice-volume", r"How does the lattice $\tfrac1N\Z^n$ detect the volume of a box $B$?", r"The number of lattice points in $B$, divided by $N^n$, tends to $\abs{B}$ as $N \to \infty$."),
    card("c6-card-zero-set", "c6-def-zero-set", r"Define a zero set and give three examples.", r"$m^*Z = 0$: for each $\eps > 0$, $Z$ is covered by countably many open boxes of total volume $< \eps$. Examples: any countable set (such as $\Q$), the Cantor set, a hyperplane $\set{x_i = c}$ in $\R^n$."),
    card("c6-card-zero-union", "c6-prop-zero-sets", r"Which operations preserve zero sets?", r"Passing to subsets and taking countable unions."),
    card("c6-card-cantor-zero", "c6-ex-cantor-zero", r"Why is the middle-thirds Cantor set a zero set?", r"It lies in $C^k$, a union of $2^k$ intervals of length $3^{-k}$, and $(2/3)^k \to 0$."),
]

write("6-outer-measure", B, C)
