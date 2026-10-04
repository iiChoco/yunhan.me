"""Section 3.2, Riemann integration: the editable source of 3-riemann-integration.json."""
from __future__ import annotations

from c3_common import card, definition, example, gate, prose, remark, write

B: list[dict] = []

B.append(prose("c3-int-intro", r"""
The integral of $f$ over $[a,b]$ is meant to be the area under its graph. Riemann's definition approximates that area by sums of areas of thin rectangles and asks that the sums converge as the rectangles get thinner. Throughout this section $a < b$ and $f : [a,b] \to \R$ is an arbitrary function unless more is said. The main theorem characterises exactly which functions are integrable: the bounded ones whose discontinuities form a negligible set. After that the fundamental theorem of calculus ties integration back to differentiation.
"""))

B.append(definition("c3-def-riemann-integral", "Partition pairs, Riemann sums, the Riemann integral", r"""
A \emph{partition} of $[a,b]$ is a finite set $P = \set{x_0, x_1, \dots, x_n}$ with
\[ a = x_0 < x_1 < \dots < x_n = b . \]
Its \emph{intervals} are $[x_{i-1}, x_i]$, of lengths $\Delta x_i = x_i - x_{i-1}$, and its \emph{mesh} is $\operatorname{mesh} P = \max_i \Delta x_i$. A choice of \emph{tags} for $P$ is a set $T = \set{t_1, \dots, t_n}$ with $t_i \in [x_{i-1}, x_i]$ for each $i$; then $(P,T)$ is a \emph{partition pair}. The \emph{Riemann sum} of $f : [a,b] \to \R$ for $(P,T)$ is
\[ R(f,P,T) = \sum_{i=1}^{n} f(t_i)\, \Delta x_i . \]
The function $f$ is \emph{Riemann integrable} with \emph{integral} $I \in \R$ if for every $\eps > 0$ there is a $\delta > 0$ such that for every partition pair $(P,T)$ of $[a,b]$,
\[ \operatorname{mesh} P < \delta \quad\Longrightarrow\quad \abs{R(f,P,T) - I} < \eps . \]
We then write $I = \int_a^b f(x)\,dx = \int_a^b f$. Note that $\sum_i \Delta x_i = b - a$ for every partition.
"""))

B.append(gate("proposition", "c3-prop-integral-unique", "The integral is unique", r"""
If $f : [a,b] \to \R$ is Riemann integrable with integral $I$ and also with integral $I'$, then $I = I'$.
""", r"""
Let $\eps > 0$. Choose $\delta > 0$ and $\delta' > 0$ from the definition for $I$ and for $I'$ respectively. Choose $n \in \N$ with $(b-a)/n < \min\set{\delta, \delta'}$, let $P$ be the partition of $[a,b]$ into $n$ intervals of equal length, and let $T$ consist of the left endpoints. Then $\operatorname{mesh} P < \delta$ and $\operatorname{mesh} P < \delta'$, so
\[ \abs{I - I'} \le \abs{I - R(f,P,T)} + \abs{R(f,P,T) - I'} < 2\eps . \]
Since $\eps > 0$ was arbitrary, $I = I'$.
""", 1, 10, [
    r"Partitions of arbitrarily small mesh exist. Compare $I$ and $I'$ through one Riemann sum.",
], ["c3-def-riemann-integral"]))

B.append(gate("theorem", "c3-thm-integrable-bounded", "Integrable functions are bounded", r"""
If $f : [a,b] \to \R$ is Riemann integrable, then $f$ is bounded.
""", r"""
Suppose $f$ is Riemann integrable with integral $I$ but unbounded. With $\eps = 1$ choose $\delta > 0$ such that $\abs{R(f,P,T) - I} < 1$ whenever $\operatorname{mesh} P < \delta$. Fix a partition $P = \set{x_0, \dots, x_n}$ with $\operatorname{mesh} P < \delta$. If $f$ were bounded on each of the finitely many intervals $[x_{i-1}, x_i]$, it would be bounded on their union $[a,b]$; so there is an index $j$ such that $f$ is unbounded on $[x_{j-1}, x_j]$.

Fix tags $T = \set{t_1, \dots, t_n}$ for $P$. Since $f$ is unbounded on $[x_{j-1},x_j]$, there is a $t_j' \in [x_{j-1}, x_j]$ with
\[ \abs{f(t_j')} > \abs{f(t_j)} + \frac{2}{\Delta x_j}, \qquad\text{hence}\qquad \abs{f(t_j') - f(t_j)}\,\Delta x_j > 2 . \]
Let $T'$ be $T$ with $t_j$ replaced by $t_j'$. The two Riemann sums differ only in the $j$-th term, so
\[ \abs{R(f,P,T') - R(f,P,T)} = \abs{f(t_j') - f(t_j)}\, \Delta x_j > 2 . \]
But both sums are within $1$ of $I$, so they differ by less than $2$. This contradiction shows $f$ is bounded.
""", 3, 25, [
    r"Argue by contradiction. Fix one partition of small mesh; an unbounded $f$ is unbounded on one of its intervals.",
    r"Keep all the tags fixed except the one in the bad interval, and move that one to change the Riemann sum by more than $2$.",
], ["c3-def-riemann-integral"]))

B.append(gate("theorem", "c3-thm-integral-linear", "Linearity of the integral", r"""
If $f, g : [a,b] \to \R$ are Riemann integrable and $c \in \R$, then $f + cg$ is Riemann integrable and
\[ \int_a^b (f + cg) = \int_a^b f + c \int_a^b g . \]
""", r"""
For any partition pair $(P,T)$,
\[ R(f + cg, P, T) = \sum_i \bigl(f(t_i) + c\,g(t_i)\bigr) \Delta x_i = R(f,P,T) + c\,R(g,P,T). \]
Let $I = \int_a^b f$ and $J = \int_a^b g$, and let $\eps > 0$. Choose $\delta_1, \delta_2 > 0$ such that $\abs{R(f,P,T) - I} < \eps$ when $\operatorname{mesh} P < \delta_1$ and $\abs{R(g,P,T) - J} < \eps$ when $\operatorname{mesh} P < \delta_2$. If $\operatorname{mesh} P < \min\set{\delta_1,\delta_2}$, then
\[ \abs{R(f+cg,P,T) - (I + cJ)} \le \abs{R(f,P,T) - I} + \abs{c}\,\abs{R(g,P,T) - J} < (1 + \abs{c})\eps . \]
Since $(1 + \abs{c})\eps$ is arbitrarily small, $f + cg$ is integrable with integral $I + cJ$.
""", 1, 10, [
    r"Riemann sums are linear in $f$ for a fixed partition pair.",
], ["c3-def-riemann-integral"]))

B.append(gate("theorem", "c3-thm-integral-monotone", "Monotonicity of the integral", r"""
Let $f, g : [a,b] \to \R$ be Riemann integrable.
\begin{enumerate}
\item If $f(x) \le g(x)$ for all $x \in [a,b]$, then $\int_a^b f \le \int_a^b g$.
\item A constant function $f(x) = c$ is Riemann integrable with $\int_a^b c\,dx = c\,(b-a)$.
\item If $m \le f(x) \le M$ for all $x \in [a,b]$, then $m(b-a) \le \int_a^b f \le M(b-a)$. In particular, if $\abs{f(x)} \le M$ for all $x$ then $\abs{\int_a^b f} \le M(b-a)$.
\end{enumerate}
""", r"""
(1) Let $I = \int_a^b f$ and $J = \int_a^b g$ and suppose $I > J$. Put $\eps = (I - J)/2 > 0$ and choose $\delta > 0$ such that $\abs{R(f,P,T) - I} < \eps$ and $\abs{R(g,P,T) - J} < \eps$ whenever $\operatorname{mesh} P < \delta$ (the smaller of the two $\delta$'s given by the definition). Take any partition pair $(P,T)$ with $\operatorname{mesh} P < \delta$. Since $f(t_i) \le g(t_i)$ and $\Delta x_i > 0$, we have $R(f,P,T) \le R(g,P,T)$, so
\[ I - \eps < R(f,P,T) \le R(g,P,T) < J + \eps , \]
giving $I - J < 2\eps = I - J$, a contradiction. Hence $I \le J$.

(2) For every partition pair, $R(c,P,T) = \sum_i c\,\Delta x_i = c\,(b-a)$, so the definition of integrability is satisfied with $I = c(b-a)$ and any $\delta$.

(3) Apply (1) to the pairs $m \le f$ and $f \le M$ and use (2). If $\abs{f} \le M$, then $-M \le f \le M$, so $-M(b-a) \le \int_a^b f \le M(b-a)$.
""", 2, 15, [
    r"For a fixed partition pair, $R(f,P,T) \le R(g,P,T)$. Pass to the limit carefully: suppose $\int f > \int g$ and choose $\eps$ to be half the gap.",
], ["c3-def-riemann-integral"]))

B.append(prose("c3-darboux-sums-intro", r"""
Riemann sums depend on the tags. Darboux's idea is to remove this dependence by replacing $f(t_i)$ with the least and greatest values available on each interval. This requires $f$ to be bounded, which by the theorem above is no loss.
"""))

B.append(definition("c3-def-darboux", "Darboux sums and integrals", r"""
Let $f : [a,b] \to \R$ be bounded and let $P = \set{x_0, \dots, x_n}$ be a partition of $[a,b]$. Put
\[ m_i = \inf\set{f(t) : t \in [x_{i-1}, x_i]}, \qquad M_i = \sup\set{f(t) : t \in [x_{i-1},x_i]} . \]
The \emph{lower sum} and \emph{upper sum} of $f$ for $P$ are
\[ L(f,P) = \sum_{i=1}^n m_i\, \Delta x_i, \qquad U(f,P) = \sum_{i=1}^n M_i\, \Delta x_i . \]
For any tags $T$ we have $m_i \le f(t_i) \le M_i$, hence
\[ L(f,P) \le R(f,P,T) \le U(f,P). \]
The \emph{lower integral} and \emph{upper integral} of $f$ are
\[ \underline{I}(f) = \sup_P L(f,P), \qquad \overline{I}(f) = \inf_P U(f,P), \]
taken over all partitions $P$ of $[a,b]$. (If $\abs{f} \le M$ then all lower and upper sums lie in $[-M(b-a), M(b-a)]$, so these exist.) The bounded function $f$ is \emph{Darboux integrable} if $\underline{I}(f) = \overline{I}(f)$.

A partition $P'$ \emph{refines} $P$ if $P \subseteq P'$. The \emph{common refinement} of $P_1$ and $P_2$ is $P_1 \cup P_2$; it refines both.
"""))

B.append(gate("lemma", "c3-lem-refinement", "Refinement principle", r"""
Let $f : [a,b] \to \R$ be bounded.
\begin{enumerate}
\item If $P'$ refines $P$, then $L(f,P) \le L(f,P') \le U(f,P') \le U(f,P)$.
\item For any two partitions $P_1, P_2$ of $[a,b]$, $L(f,P_1) \le U(f,P_2)$.
\item $\underline{I}(f) \le \overline{I}(f)$.
\end{enumerate}
""", r"""
(1) The middle inequality holds because $m_i \le M_i$ on each interval. For the outer ones, since $P'$ is obtained from $P$ by adding finitely many points one at a time, it suffices (by induction on the number of added points) to treat $P' = P \cup \set{w}$ with $x_{j-1} < w < x_j$. The sums for $P$ and $P'$ have the same terms except that the $j$-th term of $P$ is replaced by two terms. Let
\[ m' = \inf_{[x_{j-1},w]} f, \qquad m'' = \inf_{[w,x_j]} f . \]
Both are infima over subsets of $[x_{j-1},x_j]$, so $m' \ge m_j$ and $m'' \ge m_j$. Hence
\[ m_j\,\Delta x_j = m_j (w - x_{j-1}) + m_j (x_j - w) \le m'(w - x_{j-1}) + m''(x_j - w), \]
and so $L(f,P) \le L(f,P')$. In the same way the suprema $M', M''$ over the two subintervals satisfy $M', M'' \le M_j$, giving $U(f,P') \le U(f,P)$.

(2) Let $P^* = P_1 \cup P_2$, which refines both. By (1),
\[ L(f,P_1) \le L(f,P^*) \le U(f,P^*) \le U(f,P_2). \]

(3) Fix $P_2$. By (2), $U(f,P_2)$ is an upper bound for all lower sums, so $\underline{I}(f) \le U(f,P_2)$. This holds for every $P_2$, so $\underline{I}(f)$ is a lower bound for all upper sums, and $\underline{I}(f) \le \overline{I}(f)$.
""", 2, 20, [
    r"For (1), add one point at a time. How do the infimum and supremum over a subinterval compare with those over the whole interval?",
    r"For (2), pass through the common refinement $P_1 \cup P_2$.",
], ["c3-def-darboux"]))

B.append(gate("theorem", "c3-thm-riemann-criterion", "Riemann's integrability criterion", r"""
A bounded function $f : [a,b] \to \R$ is Darboux integrable if and only if for every $\eps > 0$ there is a partition $P$ of $[a,b]$ with
\[ U(f,P) - L(f,P) < \eps . \]
""", r"""
Suppose $f$ is Darboux integrable and let $I = \underline{I}(f) = \overline{I}(f)$. Given $\eps > 0$, by the definitions of supremum and infimum there are partitions $P_1, P_2$ with $L(f,P_1) > I - \eps/2$ and $U(f,P_2) < I + \eps/2$. Let $P = P_1 \cup P_2$. By the refinement principle,
\[ U(f,P) - L(f,P) \le U(f,P_2) - L(f,P_1) < \eps . \]

Conversely, suppose the condition holds. Given $\eps > 0$, choose $P$ with $U(f,P) - L(f,P) < \eps$. Since $L(f,P) \le \underline{I}(f) \le \overline{I}(f) \le U(f,P)$ by the refinement principle,
\[ 0 \le \overline{I}(f) - \underline{I}(f) \le U(f,P) - L(f,P) < \eps . \]
As $\eps$ was arbitrary, $\underline{I}(f) = \overline{I}(f)$.
""", 2, 15, [
    r"For the forward direction, pick one partition with large lower sum and one with small upper sum, and combine them.",
    r"For the converse, $\underline{I}(f)$ and $\overline{I}(f)$ are trapped between $L(f,P)$ and $U(f,P)$.",
], ["c3-def-darboux", "c3-lem-refinement"]))

B.append(gate("lemma", "c3-lem-riemann-implies-darboux", "Riemann integrable implies Darboux integrable", r"""
If $f : [a,b] \to \R$ is Riemann integrable with integral $I$, then $f$ is bounded and Darboux integrable, and $\underline{I}(f) = \overline{I}(f) = I$.
""", r"""
$f$ is bounded because integrable functions are bounded, so its Darboux sums are defined. Let $\eps > 0$ and choose $\delta > 0$ with $\abs{R(f,P,T) - I} < \eps$ whenever $\operatorname{mesh} P < \delta$. Fix a partition $P = \set{x_0,\dots,x_n}$ with $\operatorname{mesh} P < \delta$.

By the definition of supremum, for each $i$ there is a $t_i \in [x_{i-1},x_i]$ with $f(t_i) > M_i - \eps/(b-a)$. With these tags $T$,
\[ R(f,P,T) > \sum_i \Bigl(M_i - \frac{\eps}{b-a}\Bigr)\Delta x_i = U(f,P) - \eps . \]
Similarly there are tags $T'$ with $f(t_i') < m_i + \eps/(b-a)$, and then $R(f,P,T') < L(f,P) + \eps$. Since both Riemann sums are within $\eps$ of $I$,
\[ U(f,P) < R(f,P,T) + \eps < I + 2\eps, \qquad L(f,P) > R(f,P,T') - \eps > I - 2\eps . \]
Therefore, using $\underline{I}(f) \le \overline{I}(f)$ from the refinement principle,
\[ I - 2\eps < L(f,P) \le \underline{I}(f) \le \overline{I}(f) \le U(f,P) < I + 2\eps . \]
Since $\eps$ was arbitrary, $\underline{I}(f) = \overline{I}(f) = I$.
""", 3, 30, [
    r"Fix a partition of small mesh. You are free to choose the tags.",
    r"Choose tags at which $f$ is within $\eps/(b-a)$ of its supremum on each interval; the Riemann sum is then within $\eps$ of the upper sum. Do the same for the infimum.",
], ["c3-thm-integrable-bounded", "c3-def-darboux", "c3-lem-refinement"]))

B.append(gate("lemma", "c3-lem-darboux-implies-riemann", "Darboux integrable implies Riemann integrable", r"""
If $f : [a,b] \to \R$ is bounded and Darboux integrable, then $f$ is Riemann integrable with integral $I = \underline{I}(f) = \overline{I}(f)$.
""", r"""
Choose $M > 0$ with $\abs{f(x)} \le M$ for all $x$. Let $\eps > 0$. By Riemann's integrability criterion there is a partition $P_1$ with $U(f,P_1) - L(f,P_1) < \eps$; let $n_1$ be the number of its intervals. Since $L(f,P_1) \le I \le U(f,P_1)$,
\[ I - \eps < L(f,P_1) \qquad\text{and}\qquad U(f,P_1) < I + \eps . \qquad (1) \]
Put $\delta = \eps/(2Mn_1)$ and let $(P,T)$ be any partition pair with $\operatorname{mesh} P < \delta$. Let $P^* = P \cup P_1$.

\emph{Comparing $U(f,P)$ with $U(f,P^*)$.} Call an interval $J = [x_{i-1},x_i]$ of $P$ \emph{cut} if some point of $P_1$ lies in the open interval $(x_{i-1},x_i)$. The open intervals of $P$ are disjoint and $P_1$ has $n_1 - 1$ points other than $a$ and $b$, so at most $n_1$ intervals of $P$ are cut. An interval of $P$ that is not cut is also an interval of $P^*$ and contributes the same term to $U(f,P)$ and $U(f,P^*)$. A cut interval $J$, with supremum $M_J$, is divided by $P^*$ into subintervals $J_1,\dots,J_k$ whose lengths $\abs{J_l}$ add up to the length $\abs{J}$, with suprema $M_{J_l} \ge -M$; its contribution to $U(f,P) - U(f,P^*)$ is
\[ M_J \abs{J} - \sum_{l} M_{J_l}\abs{J_l} = \sum_l (M_J - M_{J_l})\abs{J_l} \le 2M\abs{J} < 2M\delta . \]
Summing over the at most $n_1$ cut intervals,
\[ U(f,P) \le U(f,P^*) + 2Mn_1\delta = U(f,P^*) + \eps . \]
The same argument with infima gives $L(f,P) \ge L(f,P^*) - \eps$.

\emph{Conclusion.} Since $P^*$ refines $P_1$, the refinement principle gives $L(f,P_1) \le L(f,P^*)$ and $U(f,P^*) \le U(f,P_1)$. Combining with (1),
\[ I - 2\eps < L(f,P_1) - \eps \le L(f,P) \le R(f,P,T) \le U(f,P) \le U(f,P_1) + \eps < I + 2\eps . \]
Thus $\abs{R(f,P,T) - I} < 2\eps$ whenever $\operatorname{mesh} P < \delta$, and $f$ is Riemann integrable with integral $I$.
""", 4, 60, [
    r"Fix one partition $P_1$ with $U(f,P_1) - L(f,P_1) < \eps$. A partition $P$ of tiny mesh need not refine $P_1$; compare $P$ with $P \cup P_1$.",
    r"Only the intervals of $P$ that contain a point of $P_1$ in their interior change when passing to $P \cup P_1$, and there are at most as many of these as $P_1$ has intervals.",
    r"Each such interval changes the upper sum by at most $2M \operatorname{mesh} P$. Choose $\delta$ so that $2M n_1 \delta \le \eps$.",
], ["c3-thm-riemann-criterion", "c3-lem-refinement", "c3-def-darboux", "c3-def-riemann-integral"]))

B.append(remark("c3-rem-riemann-darboux", r"""
The two lemmas together say: \emph{$f$ is Riemann integrable if and only if it is bounded and Darboux integrable, and then the Riemann integral equals the common value of the lower and upper integrals.} From now on we say simply \emph{integrable}, and use whichever description is convenient. In particular Riemann's criterion is a criterion for integrability: a bounded $f$ is integrable if and only if for every $\eps > 0$ some partition has $U(f,P) - L(f,P) < \eps$; and $L(f,P) \le \int_a^b f \le U(f,P)$ for every partition $P$.
""", "Riemann and Darboux integrability agree"))

B.append(gate("exercise", "c3-ex-dirichlet", "The indicator function of the rationals is not integrable", r"""
Let $f : [a,b] \to \R$ be $1$ at rational points and $0$ at irrational points. Then $f$ is bounded and not Riemann integrable.
""", r"""
$f$ takes only the values $0$ and $1$, so it is bounded. Let $P$ be any partition of $[a,b]$. Each interval $[x_{i-1},x_i]$ has positive length, so it contains a rational number and an irrational number; hence $m_i = 0$ and $M_i = 1$. Therefore
\[ L(f,P) = 0, \qquad U(f,P) = \sum_i \Delta x_i = b - a \]
for every $P$, so $\underline{I}(f) = 0 < b - a = \overline{I}(f)$. Thus $f$ is not Darboux integrable, and so it is not Riemann integrable.
""", 1, 10, [
    r"Compute the lower and upper sums for an arbitrary partition.",
], ["c3-def-darboux", "c3-lem-riemann-implies-darboux"]))

B.append(gate("theorem", "c3-thm-monotone-integrable", "Monotone functions are integrable", r"""
If $f : [a,b] \to \R$ is monotone (nondecreasing or nonincreasing), then $f$ is Riemann integrable.
""", r"""
Suppose $f$ is nondecreasing; otherwise apply the result to $-f$ and use linearity. Then $f(a) \le f(x) \le f(b)$ for all $x$, so $f$ is bounded. Let $P$ be the partition of $[a,b]$ into $n$ intervals of equal length $(b-a)/n$. Since $f$ is nondecreasing, $m_i = f(x_{i-1})$ and $M_i = f(x_i)$, so
\[ U(f,P) - L(f,P) = \sum_{i=1}^n \bigl(f(x_i) - f(x_{i-1})\bigr)\frac{b-a}{n} = \bigl(f(b) - f(a)\bigr)\frac{b-a}{n}, \]
because the sum telescopes. Given $\eps > 0$, choosing $n$ large makes this less than $\eps$. By Riemann's criterion $f$ is Darboux integrable, hence Riemann integrable.
""", 2, 15, [
    r"On each interval of a partition, where does a nondecreasing function take its infimum and its supremum?",
    r"Use a partition into $n$ equal intervals; $U - L$ telescopes.",
], ["c3-thm-riemann-criterion", "c3-lem-darboux-implies-riemann", "c3-thm-integral-linear"]))

B.append(prose("c3-zero-sets-intro", r"""
Which bounded functions are integrable? The answer is in terms of how large the set of discontinuities is, and the right notion of ``small'' is the following.
"""))

B.append(definition("c3-def-zero-set", "Zero set", r"""
A set $Z \subseteq \R$ is a \emph{zero set} if for every $\eps > 0$ there is a countable (finite or countably infinite) family of open intervals $(a_i, b_i)$ such that
\[ Z \subseteq \bigcup_i (a_i, b_i) \qquad\text{and}\qquad \sum_i (b_i - a_i) \le \eps . \]
For a countably infinite family, the sum means the supremum of the sums over finite subfamilies; this is the same as the limit of the partial sums in any enumeration, since the terms are positive. A property that holds at all points outside a zero set is said to hold \emph{almost everywhere}.
"""))

B.append(gate("proposition", "c3-prop-zero-sets", "Properties of zero sets", r"""
\begin{enumerate}
\item Every subset of a zero set is a zero set.
\item The union of countably many zero sets is a zero set.
\item Every countable subset of $\R$ is a zero set.
\end{enumerate}
""", r"""
(1) A family of intervals covering $Z$ also covers any subset of $Z$.

(2) Let $Z = \bigcup_{k \in \N} Z_k$ with each $Z_k$ a zero set (a finite union is included by taking the remaining $Z_k$ empty), and let $\eps > 0$. For each $k$ choose a countable family $\mathcal{F}_k$ of open intervals covering $Z_k$ with total length at most $\eps/2^k$. The family $\mathcal{F} = \bigcup_k \mathcal{F}_k$ is a countable union of countable families, hence countable, and it covers $Z$. Consider any finitely many distinct intervals of $\mathcal{F}$. Each belongs to some $\mathcal{F}_k$, so there is a $K$ such that all of them belong to $\mathcal{F}_1 \cup \dots \cup \mathcal{F}_K$; grouping them according to one such $k$ each, the sum of their lengths is at most
\[ \sum_{k=1}^{K} \frac{\eps}{2^k} = \eps\Bigl(1 - \frac{1}{2^K}\Bigr) < \eps . \]
So the total length of $\mathcal{F}$, the supremum of such finite sums, is at most $\eps$.

(3) A single point $p$ is a zero set: $\set{p} \subseteq (p - \eps/2, p + \eps/2)$, an interval of length $\eps$. A countable set is a countable union of single points, so it is a zero set by (2).
""", 2, 20, [
    r"For a countable union, cover the $k$-th set with total length at most $\eps/2^k$.",
], ["c3-def-zero-set"]))

B.append(gate("proposition", "c3-prop-interval-not-zero", "An interval is not a zero set", r"""
If $a < b$, then $[a,b]$ is not a zero set. In fact, if finitely many open intervals $(a_1,b_1), \dots, (a_n,b_n)$ cover $[\alpha,\beta]$, where $\alpha \le \beta$, then $\sum_{i=1}^n (b_i - a_i) > \beta - \alpha$.
""", r"""
We prove the second statement by induction on $n$, for all $\alpha \le \beta$ at once. If $n = 1$, then $a_1 < \alpha \le \beta < b_1$, so $b_1 - a_1 > \beta - \alpha$. Let $n \ge 2$ and assume the statement for $n - 1$ intervals. The point $\alpha$ lies in one of the intervals; renumbering, $a_n < \alpha < b_n$. If $b_n > \beta$, then $b_n - a_n > \beta - \alpha$ and we are done since the other lengths are positive. Otherwise $\alpha < b_n \le \beta$. No point of $[b_n, \beta]$ lies in $(a_n,b_n)$, so $[b_n,\beta]$ is covered by the other $n - 1$ intervals, and by the inductive hypothesis $\sum_{i=1}^{n-1}(b_i - a_i) > \beta - b_n$. Therefore
\[ \sum_{i=1}^{n} (b_i - a_i) > (\beta - b_n) + (b_n - a_n) = \beta - a_n > \beta - \alpha . \]

Now suppose $[a,b]$ were a zero set with $a < b$. Take $\eps = (b-a)/2$ and a countable family of open intervals covering $[a,b]$ with total length at most $\eps$. Since $[a,b]$ is compact (Heine–Borel), finitely many of these intervals cover $[a,b]$; their total length is at most $\eps < b - a$, contradicting what was just proved.
""", 3, 30, [
    r"By compactness, it is enough to show that finitely many open intervals covering $[a,b]$ have total length greater than $b - a$.",
    r"Induct on the number of intervals: remove the interval containing the left endpoint and look at what remains to be covered.",
], ["c3-def-zero-set"]))

B.append(remark("c3-rem-zero-sets", r"""
So zero sets are small in a sense quite different from cardinality or topology. The rationals are dense but form a zero set. The middle-thirds Cantor set of Chapter 2 is uncountable, yet it is a zero set: at the $n$-th stage of its construction it is covered by $2^n$ closed intervals of length $3^{-n}$, and slightly enlarging these to open intervals gives total length less than $2 \cdot (2/3)^n$.
"""))

B.append(definition("c3-def-oscillation", "Oscillation", r"""
Let $f : [a,b] \to \R$ be bounded and $x \in [a,b]$. For $r > 0$ put
\[ \omega_x(r) = \sup\set{ \abs{f(s) - f(t)} : s, t \in [a,b],\ \abs{s - x} < r,\ \abs{t - x} < r } . \]
This is finite because $f$ is bounded, nonnegative, and nondecreasing in $r$ (a larger $r$ gives a supremum over a larger set). The \emph{oscillation} of $f$ at $x$ is
\[ \osc_x(f) = \inf_{r > 0} \omega_x(r) = \lim_{r \to 0^+} \omega_x(r) \ \ge 0 . \]
For $\kappa > 0$ let $D_\kappa = \set{x \in [a,b] : \osc_x(f) \ge \kappa}$, and let $D = D(f)$ be the set of points of $[a,b]$ at which $f$ is discontinuous.
"""))

B.append(gate("lemma", "c3-lem-oscillation-continuity", "Oscillation detects discontinuity", r"""
Let $f : [a,b] \to \R$ be bounded.
\begin{enumerate}
\item $f$ is continuous at $x$ if and only if $\osc_x(f) = 0$. Consequently $D(f) = \bigcup_{k \in \N} D_{1/k}$.
\item For each $\kappa > 0$ the set $D_\kappa$ is closed in $\R$, and therefore compact.
\end{enumerate}
""", r"""
(1) Suppose $f$ is continuous at $x$ and let $\eps > 0$. There is a $\delta > 0$ with $\abs{f(s) - f(x)} < \eps/2$ whenever $s \in [a,b]$, $\abs{s - x} < \delta$. For such $s, t$, $\abs{f(s) - f(t)} \le \abs{f(s) - f(x)} + \abs{f(x) - f(t)} < \eps$, so $\omega_x(\delta) \le \eps$ and $\osc_x(f) \le \eps$. As $\eps$ was arbitrary, $\osc_x(f) = 0$.

Conversely suppose $\osc_x(f) = 0$ and let $\eps > 0$. Since the infimum of the $\omega_x(r)$ is $0$, there is an $r > 0$ with $\omega_x(r) < \eps$. If $t \in [a,b]$ and $\abs{t - x} < r$, then taking $s = x$ in the definition of $\omega_x(r)$ gives $\abs{f(x) - f(t)} \le \omega_x(r) < \eps$. So $f$ is continuous at $x$.

Hence $x \in D(f)$ if and only if $\osc_x(f) > 0$, if and only if $\osc_x(f) \ge 1/k$ for some $k \in \N$; that is, $D(f) = \bigcup_k D_{1/k}$.

(2) Let $(x_n)$ be a sequence in $D_\kappa$ converging to $x \in \R$. Since $[a,b]$ is closed, $x \in [a,b]$. Let $r > 0$. Choose $n$ with $\abs{x_n - x} < r$ and put $r' = r - \abs{x_n - x} > 0$. If $\abs{s - x_n} < r'$ then $\abs{s - x} < r$, so the supremum defining $\omega_x(r)$ is over a set containing the one defining $\omega_{x_n}(r')$:
\[ \omega_x(r) \ge \omega_{x_n}(r') \ge \osc_{x_n}(f) \ge \kappa . \]
This holds for every $r > 0$, so $\osc_x(f) \ge \kappa$ and $x \in D_\kappa$. Thus $D_\kappa$ contains the limits of its convergent sequences, so it is closed; being a closed subset of the bounded set $[a,b]$, it is compact by the Heine–Borel theorem.
""", 3, 30, [
    r"For (1), unwind both definitions; in one direction take $s = x$ in the supremum.",
    r"For (2), if $x_n \to x$ with $\osc_{x_n}(f) \ge \kappa$, any interval around $x$ contains a smaller interval around some $x_n$.",
], ["c3-def-oscillation"]))

B.append(gate("lemma", "c3-lem-rl-necessity", "Integrable functions are continuous almost everywhere", r"""
If $f : [a,b] \to \R$ is Riemann integrable, then for each $\kappa > 0$ the set $D_\kappa$ is a zero set, and hence the set $D(f)$ of discontinuities of $f$ is a zero set.
""", r"""
$f$ is bounded, so its oscillation is defined. Fix $\kappa > 0$ and $\eps > 0$. By Riemann's criterion there is a partition $P = \set{x_0,\dots,x_n}$ with
\[ U(f,P) - L(f,P) = \sum_{i=1}^n (M_i - m_i)\Delta x_i < \frac{\kappa\eps}{2} . \]
Call the index $i$ \emph{bad} if the open interval $(x_{i-1},x_i)$ contains a point of $D_\kappa$. If $i$ is bad, pick $x \in D_\kappa \cap (x_{i-1},x_i)$ and $r > 0$ with $(x - r, x + r) \subseteq (x_{i-1},x_i)$. For $s,t \in (x-r,x+r)$ we have $\abs{f(s) - f(t)} \le M_i - m_i$, since both values lie in $[m_i, M_i]$. Hence
\[ \kappa \le \osc_x(f) \le \omega_x(r) \le M_i - m_i . \]
Therefore
\[ \kappa \sum_{i \text{ bad}} \Delta x_i \le \sum_{i \text{ bad}} (M_i - m_i)\Delta x_i \le U(f,P) - L(f,P) < \frac{\kappa \eps}{2}, \]
using that every term $(M_i - m_i)\Delta x_i$ is nonnegative. So the bad open intervals $(x_{i-1},x_i)$ have total length less than $\eps/2$.

Every point of $D_\kappa$ lies either in a bad open interval or in $P$. Cover the $n+1$ points of $P$ by the open intervals $\bigl(x_i - \frac{\eps}{4(n+1)},\ x_i + \frac{\eps}{4(n+1)}\bigr)$, of total length $\eps/2$. Together with the bad open intervals these form a finite family of open intervals covering $D_\kappa$ with total length less than $\eps$. Hence $D_\kappa$ is a zero set.

Finally $D(f) = \bigcup_{k} D_{1/k}$ is a countable union of zero sets, hence a zero set.
""", 4, 45, [
    r"It suffices to show each $D_\kappa$ is a zero set. Start from a partition with $U - L$ small compared to $\kappa\eps$.",
    r"If the interior of a partition interval contains a point of $D_\kappa$, then $M_i - m_i \ge \kappa$ on that interval. So such intervals have small total length.",
    r"Points of $D_\kappa$ that are partition points are finitely many; cover them separately.",
], ["c3-thm-integrable-bounded", "c3-thm-riemann-criterion", "c3-lem-riemann-implies-darboux", "c3-lem-oscillation-continuity", "c3-prop-zero-sets", "c3-def-oscillation"]))

B.append(gate("lemma", "c3-lem-rl-sufficiency", "Bounded and continuous almost everywhere implies integrable", r"""
If $f : [a,b] \to \R$ is bounded and its set $D(f)$ of discontinuities is a zero set, then $f$ is Riemann integrable.
""", r"""
Choose $M > 0$ with $\abs{f} \le M$, and let $\eps > 0$. Put $\kappa = \dfrac{\eps}{4(b-a)}$. We find a partition $P$ with $U(f,P) - L(f,P) < \eps$; by Riemann's criterion and the equivalence of Darboux and Riemann integrability this proves the lemma.

\emph{An open covering of $[a,b]$.} The set $D_\kappa \subseteq D(f)$ is a zero set, so it is covered by countably many open intervals of total length at most $\eps/(4M)$. Since $D_\kappa$ is compact, finitely many of them, $J_1, \dots, J_m$, cover $D_\kappa$; their total length is at most $\eps/(4M)$. Each $x \in [a,b] \setminus D_\kappa$ has $\osc_x(f) < \kappa$, so there is an $r_x > 0$ with $\omega_x(r_x) < \kappa$; let $I_x = (x - r_x, x + r_x)$. The open sets $J_1,\dots,J_m$ together with the $I_x$, $x \in [a,b]\setminus D_\kappa$, cover $[a,b]$.

\emph{A partition.} Since $[a,b]$ is compact, this covering has a Lebesgue number $\lambda > 0$: every subset of $[a,b]$ of diameter less than $\lambda$ lies in a single member of the covering. Let $P = \set{x_0,\dots,x_n}$ be a partition with $\operatorname{mesh} P < \lambda$. Each interval $[x_{i-1},x_i]$ has diameter $\Delta x_i < \lambda$, so it lies in some $J_j$ or in some $I_x$. Call $i$ \emph{bad} if $[x_{i-1},x_i]$ lies in some $J_j$, and \emph{good} otherwise.

\emph{Good indices.} If $i$ is good, $[x_{i-1},x_i] \subseteq I_x$ for some $x$, so $\abs{f(s) - f(t)} \le \omega_x(r_x) < \kappa$ for all $s,t \in [x_{i-1},x_i]$. Taking the supremum over $s$ and the infimum over $t$ of $f(s) - f(t)$ gives $M_i - m_i \le \kappa$. Hence
\[ \sum_{i \text{ good}} (M_i - m_i)\Delta x_i \le \kappa \sum_i \Delta x_i = \kappa (b-a) = \frac{\eps}{4} . \]

\emph{Bad indices.} For each bad $i$ choose one $j = j(i)$ with $[x_{i-1},x_i] \subseteq J_j$. Fix $j$ and write $J_j = (\alpha,\beta)$. The intervals $[x_{i-1},x_i]$ with $j(i) = j$ are partition intervals lying in $(\alpha,\beta)$; listing their indices in increasing order as $i_1 < \dots < i_k$, we have $\alpha < x_{i_1 - 1}$, $x_{i_l} \le x_{i_{l+1}-1}$, and $x_{i_k} < \beta$, so
\[ \sum_{l=1}^{k} \Delta x_{i_l} \le x_{i_k} - x_{i_1 - 1} < \beta - \alpha . \]
Summing over $j$, the total length of the bad intervals is at most the total length of $J_1,\dots,J_m$, which is at most $\eps/(4M)$. Since $M_i - m_i \le 2M$ for every $i$,
\[ \sum_{i \text{ bad}} (M_i - m_i)\Delta x_i \le 2M \cdot \frac{\eps}{4M} = \frac{\eps}{2} . \]

\emph{Conclusion.} $U(f,P) - L(f,P) \le \dfrac{\eps}{4} + \dfrac{\eps}{2} < \eps$.
""", 4, 75, [
    r"Aim for Riemann's criterion. Split the intervals of a partition into those where $f$ oscillates little and those near the points of large oscillation; the latter should have small total length.",
    r"Fix $\kappa$ proportional to $\eps$. $D_\kappa$ is a compact zero set, so finitely many open intervals of small total length cover it. Every other point has a neighbourhood on which $f$ varies by less than $\kappa$.",
    r"These open sets cover $[a,b]$. Take a partition with mesh below a Lebesgue number of the covering, so each partition interval lies in one member of the covering.",
], ["c3-thm-riemann-criterion", "c3-lem-darboux-implies-riemann", "c3-lem-oscillation-continuity", "c3-prop-zero-sets", "c3-def-oscillation", "c3-def-zero-set"]))

B.append(gate("theorem", "c3-thm-riemann-lebesgue", "Riemann–Lebesgue theorem", r"""
A function $f : [a,b] \to \R$ is Riemann integrable if and only if it is bounded and its set of discontinuities is a zero set.
""", r"""
If $f$ is Riemann integrable, it is bounded because integrable functions are bounded, and its set of discontinuities is a zero set by the lemma that integrable functions are continuous almost everywhere. Conversely, if $f$ is bounded and $D(f)$ is a zero set, then $f$ is Riemann integrable by the lemma that a bounded function continuous almost everywhere is integrable.
""", 1, 5, [
    r"Assemble the two preceding lemmas and the boundedness of integrable functions.",
], ["c3-thm-integrable-bounded", "c3-lem-rl-necessity", "c3-lem-rl-sufficiency"]))

B.append(prose("c3-rl-consequences-intro", r"""
The Riemann–Lebesgue theorem makes most questions of integrability easy: one only has to keep track of discontinuity sets.
"""))

B.append(gate("corollary", "c3-cor-continuous-integrable", "Continuous and piecewise continuous functions are integrable", r"""
Every continuous function $f : [a,b] \to \R$ is Riemann integrable. More generally, every bounded function $f : [a,b] \to \R$ with at most countably many discontinuities is Riemann integrable.
""", r"""
A continuous function on the compact interval $[a,b]$ is bounded, and its set of discontinuities is empty, hence a zero set. In the second case $f$ is bounded by assumption and $D(f)$ is countable, hence a zero set by the properties of zero sets. In both cases the Riemann–Lebesgue theorem applies.
""", 1, 5, [
    r"Check the two conditions of the Riemann–Lebesgue theorem.",
], ["c3-thm-riemann-lebesgue", "c3-prop-zero-sets"]))

B.append(gate("corollary", "c3-cor-product-integrable", "Products of integrable functions", r"""
If $f, g : [a,b] \to \R$ are Riemann integrable, then so is their product $fg$.
""", r"""
By the Riemann–Lebesgue theorem $f$ and $g$ are bounded, say $\abs{f} \le M_f$ and $\abs{g} \le M_g$, and $D(f)$, $D(g)$ are zero sets. Then $\abs{fg} \le M_f M_g$, so $fg$ is bounded. If $f$ and $g$ are both continuous at $x$, so is $fg$; hence $D(fg) \subseteq D(f) \cup D(g)$. The union of two zero sets is a zero set, and a subset of a zero set is a zero set, so $D(fg)$ is a zero set. By the Riemann–Lebesgue theorem $fg$ is integrable.
""", 2, 10, [
    r"Where can $fg$ be discontinuous?",
], ["c3-thm-riemann-lebesgue", "c3-prop-zero-sets"]))

B.append(gate("corollary", "c3-cor-composite-integrable", "Continuous functions of integrable functions", r"""
Let $f : [a,b] \to [c,d]$ be Riemann integrable and let $\varphi : [c,d] \to \R$ be continuous. Then $\varphi \circ f$ is Riemann integrable. In particular $\abs{f}$ is integrable whenever $f$ is, and
\[ \abs{\int_a^b f} \le \int_a^b \abs{f} . \]
""", r"""
$\varphi$ is continuous on a compact interval, hence bounded, so $\varphi \circ f$ is bounded. If $f$ is continuous at $x$, then $\varphi \circ f$ is continuous at $x$, as a composite of a function continuous at $x$ and a function continuous at $f(x)$. Hence $D(\varphi \circ f) \subseteq D(f)$, which is a zero set by the Riemann–Lebesgue theorem; so $D(\varphi\circ f)$ is a zero set and $\varphi \circ f$ is integrable by the same theorem.

For the last statement, let $f$ be integrable; it is bounded, say $f : [a,b] \to [-M,M]$. Applying the first part with $\varphi(y) = \abs{y}$ on $[-M,M]$ shows $\abs{f}$ is integrable. Since $-\abs{f} \le f \le \abs{f}$, monotonicity and linearity of the integral give
\[ -\int_a^b \abs{f} \le \int_a^b f \le \int_a^b \abs{f}, \]
which is the asserted inequality.
""", 2, 15, [
    r"Compare the discontinuity set of $\varphi \circ f$ with that of $f$.",
    r"For the inequality, integrate $-\abs{f} \le f \le \abs{f}$.",
], ["c3-thm-riemann-lebesgue", "c3-prop-zero-sets", "c3-thm-integral-monotone", "c3-thm-integral-linear"]))

B.append(remark("c3-rem-composite", r"""
The order of composition matters. A composite $f \circ \psi$ of an integrable $f$ with a continuous (even a homeomorphic) change of variable $\psi$ need not be integrable, because a homeomorphism can carry a zero set onto a set that is not a zero set. And a composite of two integrable functions need not be integrable.
"""))

B.append(gate("theorem", "c3-thm-integral-additive", "Additivity over intervals", r"""
Let $a < c < b$ and $f : [a,b] \to \R$. Then $f$ is Riemann integrable on $[a,b]$ if and only if its restrictions to $[a,c]$ and to $[c,b]$ are Riemann integrable, and in that case
\[ \int_a^b f = \int_a^c f + \int_c^b f . \]
""", r"""
Let $f_1, f_2$ be the restrictions of $f$ to $[a,c]$ and $[c,b]$.

\emph{Integrability.} $f$ is bounded if and only if $f_1$ and $f_2$ are both bounded. If $f$ is continuous at a point $x \in [a,c]$ then so is $f_1$, and similarly for $f_2$; thus $D(f_1) \cup D(f_2) \subseteq D(f)$. Conversely, if $x \in [a,c)$ and $f_1$ is continuous at $x$, then $f$ is continuous at $x$, because $f$ and $f_1$ agree on $[a,c)$, which contains all points of $[a,b]$ within distance $c - x$ of $x$; similarly for $x \in (c,b]$ and $f_2$. Thus $D(f) \subseteq D(f_1) \cup D(f_2) \cup \set{c}$. By the properties of zero sets, $D(f)$ is a zero set if and only if $D(f_1)$ and $D(f_2)$ both are. The Riemann–Lebesgue theorem now gives the equivalence.

\emph{The formula.} Assume all three are integrable, with integrals $I$, $I_1$, $I_2$. Let $\eps > 0$ and choose $\delta > 0$ that works in the definition of integrability for all three (the least of three $\delta$'s). Take partition pairs $(P_1,T_1)$ of $[a,c]$ and $(P_2,T_2)$ of $[c,b]$ with meshes less than $\delta$. Then $P = P_1 \cup P_2$ with tags $T = T_1 \cup T_2$ is a partition pair of $[a,b]$ with mesh less than $\delta$, its intervals being those of $P_1$ followed by those of $P_2$, and
\[ R(f,P,T) = R(f_1,P_1,T_1) + R(f_2,P_2,T_2) . \]
Hence
\[ \abs{I - I_1 - I_2} \le \abs{I - R(f,P,T)} + \abs{R(f_1,P_1,T_1) - I_1} + \abs{R(f_2,P_2,T_2) - I_2} < 3\eps . \]
Since $\eps$ was arbitrary, $I = I_1 + I_2$.
""", 3, 30, [
    r"For integrability, use the Riemann–Lebesgue theorem: compare the discontinuity sets of $f$ and of its two restrictions. The point $c$ needs separate attention.",
    r"For the formula, glue a partition pair of $[a,c]$ to one of $[c,b]$; the Riemann sums add.",
], ["c3-thm-riemann-lebesgue", "c3-prop-zero-sets", "c3-def-riemann-integral"]))

B.append(definition("c3-def-integral-conventions", "Conventions for limits of integration", r"""
If $f$ is integrable on an interval containing $p$ and $q$, we put
\[ \int_p^p f = 0, \qquad \int_q^p f = -\int_p^q f \quad (p < q). \]
By additivity over intervals, $f$ is integrable on every closed subinterval of an interval on which it is integrable, and with these conventions
\[ \int_p^q f + \int_q^s f = \int_p^s f \]
for all $p, q, s$ in that interval, in any order. (For $p \le q \le s$ this is additivity; the other orders follow by moving terms across the equation.)
"""))

B.append(gate("exercise", "c3-ex-nonnegative-zero-integral", "A nonnegative function with zero integral", r"""
Let $f : [a,b] \to \R$ be Riemann integrable with $f(x) \ge 0$ for all $x$ and $\int_a^b f = 0$. Then $f(x) = 0$ at every point $x$ where $f$ is continuous. Consequently $f = 0$ almost everywhere.
""", r"""
Suppose $f$ is continuous at $x_0$ and $f(x_0) > 0$. With $\eps = f(x_0)/2$ there is a $\delta > 0$ such that $f(t) > f(x_0)/2$ for all $t \in [a,b]$ with $\abs{t - x_0} < \delta$. The set of such $t$ contains a closed interval $[p,q]$ with $a \le p < q \le b$ (for example $p = \max\set{a, x_0 - \delta/2}$ and $q = \min\set{b, x_0 + \delta/2}$; then $p < q$ because $a < b$ and $x_0 \in [a,b]$). Let $P$ be the partition of $[a,b]$ consisting of $a, p, q, b$ (with repetitions deleted). On $[p,q]$ the infimum of $f$ is at least $f(x_0)/2$, and on the other intervals of $P$ it is at least $0$ because $f \ge 0$. Hence
\[ \int_a^b f \ \ge\ L(f,P) \ \ge\ \frac{f(x_0)}{2}\,(q - p) > 0, \]
contradicting $\int_a^b f = 0$. So $f(x_0) = 0$ at each continuity point.

The set where $f \neq 0$ is therefore contained in $D(f)$, which is a zero set by the Riemann–Lebesgue theorem. So $f = 0$ almost everywhere.
""", 2, 20, [
    r"If $f$ is positive at a point of continuity, it is bounded below by a positive constant on a whole interval.",
    r"Use a lower sum for a partition that has that interval as one of its intervals.",
], ["c3-def-darboux", "c3-lem-riemann-implies-darboux", "c3-thm-riemann-lebesgue"]))

B.append(prose("c3-ftc-intro", r"""
Integration and differentiation are inverse operations. There are two halves to this statement: differentiating an integral with respect to its upper limit recovers the integrand, and integrating a derivative recovers the function.
"""))

B.append(gate("theorem", "c3-thm-ftc", "Fundamental theorem of calculus", r"""
Let $f : [a,b] \to \R$ be Riemann integrable and define its \emph{indefinite integral}
\[ F(x) = \int_a^x f(t)\,dt, \qquad x \in [a,b] . \]
\begin{enumerate}
\item If $\abs{f} \le M$ then $\abs{F(y) - F(x)} \le M\abs{y - x}$ for all $x,y \in [a,b]$; in particular $F$ is continuous.
\item If $x \in (a,b)$ and $f$ is continuous at $x$, then $F$ is differentiable at $x$ and $F'(x) = f(x)$.
\end{enumerate}
""", r"""
$f$ is bounded since it is integrable; fix $M$ with $\abs{f} \le M$. By additivity and the conventions for limits of integration, $f$ is integrable on every closed subinterval and
\[ F(y) - F(x) = \int_x^y f \qquad \text{for all } x, y \in [a,b]. \]

(1) If $x < y$, the bound $\abs{f} \le M$ on $[x,y]$ gives $\abs{\int_x^y f} \le M(y - x)$ by monotonicity of the integral. So $\abs{F(y) - F(x)} \le M\abs{y-x}$; this is symmetric in $x,y$ and trivial for $x = y$. Given $\eps > 0$, $\abs{y - x} < \eps/(M+1)$ implies $\abs{F(y) - F(x)} < \eps$, so $F$ is continuous.

(2) Let $f$ be continuous at $x \in (a,b)$ and let $\eps > 0$. Choose $\delta > 0$ with $(x - \delta, x+\delta) \subseteq (a,b)$ and $\abs{f(t) - f(x)} < \eps$ whenever $\abs{t - x} < \delta$. Let $0 < h < \delta$. Since the constant $f(x)$ has integral $f(x)\,h$ over $[x, x+h]$, linearity gives
\[ F(x+h) - F(x) - f(x)\,h = \int_x^{x+h} \bigl(f(t) - f(x)\bigr)\,dt . \]
The integrand is bounded by $\eps$ in absolute value on $[x,x+h]$, so by monotonicity of the integral the right side has absolute value at most $\eps h$. Hence
\[ \abs{\frac{F(x+h) - F(x)}{h} - f(x)} \le \eps . \]
Now let $-\delta < h < 0$. Then $F(x+h) - F(x) = -\int_{x+h}^{x} f$, and the interval $[x+h,x]$ has length $-h$, so
\[ F(x+h) - F(x) - f(x)\,h = -\int_{x+h}^{x} \bigl(f(t) - f(x)\bigr)\,dt, \]
whose absolute value is at most $\eps\abs{h}$; dividing by $\abs{h}$ gives the same inequality. Thus the difference quotient of $F$ at $x$ is within $\eps$ of $f(x)$ for $0 < \abs{h} < \delta$, which proves $F'(x) = f(x)$.
""", 3, 30, [
    r"Start from $F(y) - F(x) = \int_x^y f$, which comes from additivity.",
    r"For (2), write $F(x+h) - F(x) - f(x)h$ as the integral of $f(t) - f(x)$ over the interval between $x$ and $x + h$, and bound the integrand using continuity of $f$ at $x$.",
], ["c3-thm-integral-additive", "c3-def-integral-conventions", "c3-thm-integral-monotone", "c3-thm-integral-linear", "c3-thm-integrable-bounded"]))

B.append(definition("c3-def-antiderivative", "Antiderivative", r"""
An \emph{antiderivative} of $f : [a,b] \to \R$ is a continuous function $G : [a,b] \to \R$ that is differentiable on $(a,b)$ with $G'(x) = f(x)$ for every $x \in (a,b)$.
"""))

B.append(gate("corollary", "c3-cor-continuous-antiderivative", "Continuous functions have antiderivatives", r"""
Every continuous function $f : [a,b] \to \R$ has an antiderivative, namely $F(x) = \int_a^x f$. Any two antiderivatives of the same function $f : [a,b] \to \R$ differ by a constant.
""", r"""
A continuous $f$ is integrable, so $F$ is defined. By the fundamental theorem of calculus $F$ is continuous on $[a,b]$, and since $f$ is continuous at every $x \in (a,b)$, $F'(x) = f(x)$ there. So $F$ is an antiderivative.

If $G_1, G_2$ are antiderivatives of $f$, then $H = G_1 - G_2$ is continuous on $[a,b]$ and $H' = f - f = 0$ on $(a,b)$. By the consequences of the mean value theorem $H$ is constant on $(a,b)$, and by continuity at $a$ and $b$ it takes the same constant value there.
""", 1, 10, [
    r"The first part is the fundamental theorem. For the second, differentiate the difference.",
], ["c3-thm-ftc", "c3-cor-continuous-integrable", "c3-def-antiderivative", "c3-cor-mvt-consequences"]))

B.append(gate("theorem", "c3-thm-antiderivative", "Antiderivative theorem", r"""
Let $f : [a,b] \to \R$ be Riemann integrable and let $G$ be an antiderivative of $f$. Then
\[ \int_a^b f(x)\,dx = G(b) - G(a) . \]
""", r"""
Let $P = \set{x_0,\dots,x_n}$ be any partition of $[a,b]$. On each interval $[x_{i-1},x_i]$ the function $G$ is continuous, and it is differentiable on $(x_{i-1},x_i)$ with derivative $f$. By the mean value theorem there is a $t_i \in (x_{i-1},x_i)$ with
\[ G(x_i) - G(x_{i-1}) = G'(t_i)\,\Delta x_i = f(t_i)\,\Delta x_i . \]
With these tags $T = \set{t_1,\dots,t_n}$ the Riemann sum telescopes:
\[ R(f,P,T) = \sum_{i=1}^n \bigl(G(x_i) - G(x_{i-1})\bigr) = G(b) - G(a) . \]
Let $I = \int_a^b f$ and $\eps > 0$. Choose $\delta > 0$ from the definition of integrability and a partition $P$ with $\operatorname{mesh} P < \delta$; with the tags just constructed,
\[ \abs{G(b) - G(a) - I} = \abs{R(f,P,T) - I} < \eps . \]
Since $\eps$ was arbitrary, $G(b) - G(a) = I$.
""", 3, 25, [
    r"Note that $f$ is not assumed continuous, so the fundamental theorem does not apply directly. Work with Riemann sums.",
    r"For any partition, the mean value theorem lets you choose tags $t_i$ with $G(x_i) - G(x_{i-1}) = f(t_i)\Delta x_i$. Then the Riemann sum telescopes.",
], ["c3-def-antiderivative", "c3-thm-mvt", "c3-def-riemann-integral"]))

B.append(remark("c3-rem-antiderivative", r"""
The hypothesis that $f$ be integrable is needed: there are differentiable functions whose derivative is unbounded, such as $x^2 \sin(1/x^2)$ (extended by $0$ at $0$) on $[-1,1]$, and an unbounded function is not Riemann integrable. Conversely, an integrable function need not have an antiderivative: a function with a jump discontinuity is not a derivative, by the intermediate value property of derivatives.
"""))

B.append(gate("theorem", "c3-thm-integration-by-parts", "Integration by parts", r"""
Let $f, g : [a,b] \to \R$ be continuous on $[a,b]$ and differentiable on $(a,b)$, and suppose there are Riemann integrable functions $u, v : [a,b] \to \R$ with $u = f'$ and $v = g'$ on $(a,b)$. Then
\[ \int_a^b f\,v = f(b)g(b) - f(a)g(a) - \int_a^b u\,g . \]
In the usual notation, $\int_a^b f g' = \bigl[fg\bigr]_a^b - \int_a^b f' g$.
""", r"""
Continuous functions are integrable and products of integrable functions are integrable, so $fv$, $ug$, and $w = ug + fv$ are integrable on $[a,b]$. The product $G = fg$ is continuous on $[a,b]$ and, by the product rule, differentiable on $(a,b)$ with
\[ G'(x) = f'(x)g(x) + f(x)g'(x) = u(x)g(x) + f(x)v(x) = w(x) . \]
So $G$ is an antiderivative of the integrable function $w$. By the antiderivative theorem and linearity of the integral,
\[ f(b)g(b) - f(a)g(a) = \int_a^b w = \int_a^b u\,g + \int_a^b f\,v , \]
which rearranges to the claim.
""", 2, 15, [
    r"What is the derivative of $fg$?",
    r"Apply the antiderivative theorem to $fg$; check first that every function you integrate is integrable.",
], ["c3-thm-antiderivative", "c3-cor-product-integrable", "c3-cor-continuous-integrable", "c3-thm-integral-linear", "c3-thm-sum-product-rule"]))

B.append(gate("theorem", "c3-thm-substitution", "Integration by substitution", r"""
Let $f : [a,b] \to \R$ be continuous. Let $g : [c,d] \to [a,b]$ be continuous on $[c,d]$ and differentiable on $(c,d)$, and suppose there is a Riemann integrable $w : [c,d] \to \R$ with $w = g'$ on $(c,d)$. Then
\[ \int_c^d f(g(u))\,w(u)\,du = \int_{g(c)}^{g(d)} f(x)\,dx , \]
where the right-hand side follows the conventions for limits of integration. In the usual notation, $\int_c^d f(g(u))\,g'(u)\,du = \int_{g(c)}^{g(d)} f$.
""", r"""
Extend $f$ to a continuous function $\tilde f$ on $[a-1,b+1]$ by $\tilde f(x) = f(a)$ for $x < a$ and $\tilde f(x) = f(b)$ for $x > b$. Let
\[ F(x) = \int_{a-1}^{x} \tilde f, \qquad x \in [a-1,b+1] . \]
By the fundamental theorem of calculus, $F$ is differentiable at every point of $(a-1,b+1)$, with $F' = \tilde f$ there; in particular $F'(x) = f(x)$ for every $x \in [a,b]$, the endpoints included.

Let $H = F \circ g : [c,d] \to \R$. It is continuous, as a composite of continuous functions. For $u \in (c,d)$, $g$ is differentiable at $u$ with values in $(a-1,b+1)$, and $F$ is differentiable at $g(u) \in [a,b]$, so by the chain rule
\[ H'(u) = F'(g(u))\,g'(u) = f(g(u))\,w(u) . \]
The function $f \circ g$ is continuous on $[c,d]$, hence integrable, and $w$ is integrable, so $(f \circ g)\,w$ is integrable. Thus $H$ is an antiderivative of the integrable function $(f\circ g)\,w$, and the antiderivative theorem gives
\[ \int_c^d f(g(u))\,w(u)\,du = H(d) - H(c) = F(g(d)) - F(g(c)) . \]
Finally, by the conventions for limits of integration, $F(q) - F(p) = \int_p^q \tilde f = \int_p^q f$ for $p, q \in [a,b]$; with $p = g(c)$, $q = g(d)$ this is the right-hand side of the claim.
""", 3, 35, [
    r"Find an antiderivative of $u \mapsto f(g(u))\,g'(u)$ using an antiderivative $F$ of $f$ and the chain rule.",
    r"One technical point: the fundamental theorem gives $F' = f$ only at interior points, while $g$ may take the values $a$ and $b$. Extending $f$ continuously to a slightly larger interval avoids the problem.",
], ["c3-thm-ftc", "c3-thm-antiderivative", "c3-thm-chain-rule", "c3-cor-continuous-integrable", "c3-cor-product-integrable", "c3-def-integral-conventions"]))

B.append(definition("c3-def-improper-integral", "Improper integrals", r"""
Let $f : [a,\infty) \to \R$ be Riemann integrable on $[a,b]$ for every $b > a$. If the limit
\[ \int_a^\infty f = \lim_{b \to \infty} \int_a^b f \]
exists in $\R$, the \emph{improper integral} of $f$ \emph{converges} and has this value; otherwise it \emph{diverges}. Similarly, if $f : (a,b] \to \R$ is integrable on $[c,b]$ for every $c \in (a,b)$, its improper integral over $(a,b]$ is $\lim_{c \to a^+} \int_c^b f$ when this limit exists; and likewise for $[a,b)$ and for $(-\infty,b]$. An integral that is improper at both ends is split at an interior point and both pieces are required to converge.
"""))

B.append(example("c3-ex-improper", r"""
On $[1,\infty)$ the function $x^{-2}$ has the antiderivative $-1/x$ on each $[1,b]$, so $\int_1^b x^{-2}\,dx = 1 - 1/b \to 1$: the improper integral converges to $1$, although the region under the graph is unbounded. On $(0,1]$ the same function gives $\int_c^1 x^{-2}\,dx = 1/c - 1 \to \infty$ as $c \to 0^+$, so that improper integral diverges. For a nonnegative $f$ the function $b \mapsto \int_a^b f$ is nondecreasing, so $\int_a^\infty f$ converges exactly when these integrals are bounded above. Improper integrals will be compared with series in the next section.
""", "Improper integrals"))

C = [
    card("c3-card-riemann-integrable", r"Define: $f : [a,b] \to \R$ is Riemann integrable with integral $I$.",
         r"For every $\eps > 0$ there is $\delta > 0$ such that $\abs{R(f,P,T) - I} < \eps$ for every partition pair $(P,T)$ with $\operatorname{mesh} P < \delta$, where $R(f,P,T) = \sum_i f(t_i)\Delta x_i$.", "c3-def-riemann-integral"),
    card("c3-card-integrable-bounded", r"Why is a Riemann integrable function bounded?",
         r"Fix a partition of small mesh. If $f$ were unbounded on one of its intervals, moving the tag in that interval alone would change the Riemann sum by more than $2$, while all such sums lie within $1$ of $I$.", "c3-thm-integrable-bounded"),
    card("c3-card-darboux", r"Define the lower and upper sums and integrals of a bounded $f$. What is the refinement principle?",
         r"$L(f,P) = \sum m_i \Delta x_i$, $U(f,P) = \sum M_i\Delta x_i$ with $m_i, M_i$ the inf and sup of $f$ on $[x_{i-1},x_i]$; $\underline{I} = \sup_P L$, $\overline{I} = \inf_P U$. Refining a partition raises $L$ and lowers $U$; hence $L(f,P_1) \le U(f,P_2)$ always.", "c3-lem-refinement"),
    card("c3-card-riemann-criterion", r"State Riemann's integrability criterion.",
         r"A bounded $f$ is integrable iff for every $\eps > 0$ there is a partition $P$ with $U(f,P) - L(f,P) < \eps$.", "c3-thm-riemann-criterion"),
    card("c3-card-zero-set", r"Define a zero set. Give three examples, one uncountable.",
         r"$Z$ is a zero set if for every $\eps > 0$ it can be covered by countably many open intervals of total length $\le \eps$. Examples: finite sets, $\Q$ (any countable set), the middle-thirds Cantor set. An interval $[a,b]$ with $a<b$ is not one.", "c3-def-zero-set"),
    card("c3-card-oscillation", r"Define the oscillation of a bounded $f$ at $x$. Two key facts?",
         r"$\osc_x(f) = \lim_{r \to 0^+} \sup\set{\abs{f(s) - f(t)} : s,t \in [a,b] \cap (x-r,x+r)}$. $f$ is continuous at $x$ iff $\osc_x(f) = 0$; and $D_\kappa = \set{x : \osc_x(f) \ge \kappa}$ is compact.", "c3-lem-oscillation-continuity"),
    card("c3-card-riemann-lebesgue", r"State the Riemann–Lebesgue theorem.",
         r"$f : [a,b] \to \R$ is Riemann integrable iff it is bounded and its set of discontinuities is a zero set.", "c3-thm-riemann-lebesgue"),
    card("c3-card-rl-idea", r"Idea of the proof that a bounded $f$ with discontinuities forming a zero set is integrable.",
         r"Cover the compact set $D_\kappa$ by finitely many intervals of small total length; elsewhere each point has a neighbourhood where $f$ varies by less than $\kappa$. A partition with mesh below a Lebesgue number of this cover has each interval of one kind or the other, so $U - L \le \kappa(b-a) + 2M \cdot(\text{small})$.", "c3-lem-rl-sufficiency"),
    card("c3-card-ftc", r"State the fundamental theorem of calculus and the antiderivative theorem.",
         r"If $f$ is integrable and $F(x) = \int_a^x f$, then $F$ is continuous and $F'(x) = f(x)$ at each point of continuity of $f$. If $f$ is integrable and $G$ is an antiderivative of $f$, then $\int_a^b f = G(b) - G(a)$ (mean value theorem on each partition interval makes a Riemann sum telescope).", "c3-thm-antiderivative"),
    card("c3-card-integrable-examples", r"Which of these are integrable on $[a,b]$: continuous functions, monotone functions, the indicator of $\Q$, the product of two integrable functions, $\varphi \circ f$ with $f$ integrable and $\varphi$ continuous?",
         r"All except the indicator of $\Q$, which has $L = 0$ and $U = b - a$ for every partition (it is discontinuous everywhere)."),
]

write("3-riemann-integration", B, C)
