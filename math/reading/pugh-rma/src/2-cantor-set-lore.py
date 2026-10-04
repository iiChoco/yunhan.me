from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c2lib import Section

s = Section("2-cantor-set-lore")

s.p("c2-lore-intro", r"""
This section looks more closely at the Cantor set $C$ and at its surprising place among compact spaces. First we give every point of $C$ an \emph{address}, an infinite string of the symbols $0$ and $2$ recording whether the point lies in the left or the right third at each stage of the construction. Addresses make $C$ easy to compute with. Then comes a remarkable theorem: every nonempty compact metric space, whatever its shape or dimension, is a continuous image of $C$. A space-filling curve is a corollary. The section ends with two results that are stated without proof.
""")

s.d("c2-def-address", "Words, addresses, and the intervals $C_\\alpha$", r"""
A \emph{word} of length $n \ge 0$ is a finite string $\alpha = \alpha_1 \alpha_2 \dots \alpha_n$ with each $\alpha_i \in \set{0,2}$; its length is written $\abs{\alpha}$, and the empty word has length $0$. If $\alpha$, $\beta$ are words, $\alpha\beta$ is the word $\alpha$ followed by $\beta$. An \emph{address} is an infinite string $\omega = \omega_1 \omega_2 \omega_3 \dots$ with each $\omega_i \in \set{0,2}$; its \emph{truncation} $\omega|n$ is the word $\omega_1 \dots \omega_n$. Truncations $\alpha|n$ of words of length at least $n$ are defined in the same way.

For a word $\alpha$ of length $n$ put
\[ a_\alpha = \sum_{i=1}^n \frac{\alpha_i}{3^i}, \qquad C_\alpha = \big[\, a_\alpha,\ a_\alpha + 3^{-n} \,\big] . \]
For the empty word, $a_\alpha = 0$ and $C_\alpha = [0,1]$. For instance $C_0 = [0,\tfrac13]$, $C_2 = [\tfrac23,1]$, $C_{02} = [\tfrac29,\tfrac13]$.
""")

s.t("lemma", "c2-lem-address-intervals", r"The intervals of $C^n$ are the $C_\alpha$", r"""
For each $n \ge 0$:
\begin{enumerate}
\item for every word $\alpha$ of length $n$, the intervals $C_{\alpha 0}$ and $C_{\alpha 2}$ are the left and right thirds of $C_\alpha$;
\item the intervals of $C^n$ are exactly the intervals $C_\alpha$ with $\abs{\alpha} = n$; for distinct words $\alpha \ne \alpha'$ of length $n$ the intervals $C_\alpha$ and $C_{\alpha'}$ are disjoint; and the union of all of them is $C^n$.
\end{enumerate}
""", r"""
(1) Let $\abs{\alpha} = n$, so $C_\alpha = [a_\alpha, a_\alpha + 3^{-n}]$ has length $3^{-n}$. Its left third is $[a_\alpha,\ a_\alpha + 3^{-(n+1)}]$. Since $a_{\alpha 0} = a_\alpha + 0$, this is $C_{\alpha 0}$. Its right third is
\[ \big[\, a_\alpha + 3^{-n} - 3^{-(n+1)},\ a_\alpha + 3^{-n} \,\big] = \big[\, a_\alpha + 2 \cdot 3^{-(n+1)},\ a_\alpha + 2\cdot 3^{-(n+1)} + 3^{-(n+1)} \,\big] , \]
and since $a_{\alpha 2} = a_\alpha + 2 \cdot 3^{-(n+1)}$, this is $C_{\alpha 2}$.

(2) By induction on $n$. For $n = 0$ there is one word, the empty one, and $C_\alpha = [0,1]$ is the one interval of $C^0$. Suppose the statement holds for $n$. By definition the intervals of $C^{n+1}$ are the left and right thirds of the intervals of $C^n$, which by the induction hypothesis and (1) are the intervals $C_{\alpha 0}, C_{\alpha 2}$ with $\abs{\alpha} = n$, that is, the intervals $C_\beta$ with $\abs{\beta} = n+1$; and $C^{n+1}$ is their union. Let $\beta \ne \beta'$ be words of length $n+1$. If $\beta|n = \beta'|n = \alpha$, then $C_\beta$ and $C_{\beta'}$ are the two thirds of $C_\alpha$, which are disjoint. Otherwise $\beta|n \ne \beta'|n$; by (1) $C_\beta \subset C_{\beta|n}$ and $C_{\beta'} \subset C_{\beta'|n}$, and these two intervals are disjoint by the induction hypothesis.
""", 2, 20, [
    r"Compute the left and right thirds of $[a_\alpha, a_\alpha + 3^{-n}]$ and compare with the definition of $a_{\alpha 0}$, $a_{\alpha 2}$.",
    r"Then induct on $n$, following the definition of $C^{n+1}$ from $C^n$.",
], ["c2-def-address", "c2-def-cantor-set", "c2-lem-cantor-structure"])

s.t("theorem", "c2-thm-addresses", "Every point of $C$ has exactly one address", r"""
\begin{enumerate}
\item For every address $\omega$ the series $\sum_{i=1}^\infty \omega_i / 3^i$ converges; its sum $p(\omega)$ lies in $C_{\omega|n}$ for every $n$, and $p(\omega) \in C$.
\item For every $x \in C$ there is exactly one address $\omega$ with $x = p(\omega)$.
\end{enumerate}
Thus $C$ is exactly the set of numbers in $[0,1]$ that have a base-$3$ expansion using only the digits $0$ and $2$, and $p$ is a bijection from the set of addresses onto $C$.
""", r"""
Note first that $2 \cdot 3^{-i} = 3^{-(i-1)} - 3^{-i}$, so for $n < m$ the sum telescopes:
\[ \sum_{i=n+1}^m \frac{2}{3^i} = 3^{-n} - 3^{-m} . \]

(1) The partial sums of the series are the numbers $a_{\omega|n}$. They are nondecreasing in $n$, and by the identity above (with $n = 0$) they are bounded by $1$. A nondecreasing sequence bounded above converges to its least upper bound, so the series converges; call the sum $x = p(\omega)$. For $m > n$,
\[ a_{\omega|n} \le a_{\omega|m} \le a_{\omega|n} + \sum_{i=n+1}^m \frac{2}{3^i} < a_{\omega|n} + 3^{-n} . \]
Letting $m \to \infty$ gives $a_{\omega|n} \le x \le a_{\omega|n} + 3^{-n}$, that is, $x \in C_{\omega|n}$. Since $C_{\omega|n} \subset C^n$ for every $n$, $x \in \bigcap_n C^n = C$.

(2) \emph{Existence.} Let $x \in C$. For each $n$, $x \in C^n$, so by the lemma on the intervals of $C^n$ there is exactly one word $\alpha^{(n)}$ of length $n$ with $x \in C_{\alpha^{(n)}}$. Let $\beta = \alpha^{(n+1)}|n$. Then $C_{\alpha^{(n+1)}}$ is a third of $C_\beta$, so $x \in C_\beta$, and by uniqueness $\beta = \alpha^{(n)}$. So each $\alpha^{(n+1)}$ extends $\alpha^{(n)}$ by one letter. Let $\omega$ be the address whose $n$-th letter is the last letter of $\alpha^{(n)}$; by induction $\omega|n = \alpha^{(n)}$ for all $n$. Now both $x$ and $p(\omega)$ lie in $C_{\omega|n}$, an interval of length $3^{-n}$, so $\abs{x - p(\omega)} \le 3^{-n}$ for every $n$, and hence $x = p(\omega)$.

\emph{Uniqueness.} If $p(\omega) = p(\omega') = x$, then by (1) $x \in C_{\omega|n} \cap C_{\omega'|n}$ for every $n$. Intervals $C_\alpha$ for distinct words of the same length are disjoint, so $\omega|n = \omega'|n$ for every $n$, i.e. $\omega = \omega'$.
""", 4, 60, [
    r"For (1): the partial sums are the left endpoints $a_{\omega|n}$. Bound the tail $\sum_{i>n} \omega_i 3^{-i}$ by $3^{-n}$ to trap the sum in $C_{\omega|n}$.",
    r"For (2): at each stage $x$ lies in exactly one interval $C_\alpha$ of $C^n$. Show these words are consistent truncations of one address.",
    r"Both $x$ and $p(\omega)$ lie in $C_{\omega|n}$ for all $n$, and these intervals shrink to a point.",
], ["c2-def-address", "c2-lem-address-intervals", "c2-def-cantor-set"])

s.t("exercise", "c2-ex-quarter", r"$1/4$ is in the Cantor set", r"""
Show that $\tfrac14 \in C$, and that $\tfrac14$ is not an endpoint of any of the intervals of any $C^n$.
""", r"""
Consider the address $\omega = 020202\dots$, with $\omega_i = 2$ for even $i$ and $0$ for odd $i$. Its series is $\sum_{j=1}^\infty 2 \cdot 3^{-2j} = 2\sum_{j=1}^\infty 9^{-j}$. The partial sums of the geometric series are $\sum_{j=1}^m 9^{-j} = \tfrac18 (1 - 9^{-m})$, which converge to $\tfrac18$. So $p(\omega) = \tfrac14$, and $p(\omega) \in C$ because every address names a point of $C$.

The intervals of $C^n$ are the $C_\alpha = [a_\alpha, a_\alpha + 3^{-n}]$ with $\abs{\alpha} = n$, and $a_\alpha = \sum_{i \le n} \alpha_i 3^{-i}$ is an integer multiple of $3^{-n}$. So every endpoint has the form $k/3^n$ with $k$ an integer. If $\tfrac14 = k/3^n$ then $3^n = 4k$, which is impossible because $3^n$ is odd.
""", 2, 20, [
    r"Find the base-$3$ expansion of $1/4$: try a periodic address.",
    r"$\sum_{j \ge 1} 2/9^j = 1/4$. For the second part, endpoints are fractions with denominator a power of $3$.",
], ["c2-thm-addresses", "c2-lem-address-intervals"])

s.t("lemma", "c2-lem-address-distance", "Close points share long prefixes", r"""
Let $x, y \in C$ have addresses $\omega, \omega'$, and let $n \ge 0$.
\begin{enumerate}
\item If $\omega|n = \omega'|n$, then $\abs{x - y} \le 3^{-n}$.
\item If $\abs{x - y} < 3^{-n}$, then $\omega|n = \omega'|n$.
\end{enumerate}
""", r"""
(1) Both $x$ and $y$ lie in $C_{\omega|n}$, an interval of length $3^{-n}$.

(2) Suppose $\omega|n \ne \omega'|n$, and let $k \le n$ be the first index with $\omega_k \ne \omega'_k$. Let $\alpha = \omega|(k-1) = \omega'|(k-1)$. One of $x, y$ lies in $C_{\alpha 0}$ and the other in $C_{\alpha 2}$, the left and right thirds of $C_\alpha$. With $a = a_\alpha$, these are $[a,\ a + 3^{-k}]$ and $[a + 2\cdot 3^{-k},\ a + 3^{-(k-1)}]$, so any point of one is at distance at least $3^{-k}$ from any point of the other. Hence $\abs{x - y} \ge 3^{-k} \ge 3^{-n}$. By contraposition, $\abs{x-y} < 3^{-n}$ implies $\omega|n = \omega'|n$.
""", 2, 20, [
    r"If the addresses first differ at place $k$, the two points sit in the two different thirds of one interval $C_\alpha$ with $\abs{\alpha} = k-1$.",
], ["c2-thm-addresses", "c2-lem-address-intervals"])

s.p("c2-lore-surjection-prose", r"""
\textbf{The Cantor surjection theorem.} Addresses let us define maps out of $C$ by saying what to do with a string of symbols. The idea of the next theorem is to chop a compact space $M$ into finitely many small compact pieces, label the pieces by words, chop each piece into smaller pieces labeled by longer words, and so on; an address then singles out a nested sequence of pieces shrinking to a point of $M$.
""")

s.t("lemma", "c2-lem-pieces", "A compact space is a finite union of small compact pieces", r"""
Let $M$ be a nonempty compact metric space and $\eps > 0$. Then $M = K_1 \cup \dots \cup K_m$ for some finite number $m \ge 1$ of nonempty compact sets $K_i$ with $\diam K_i \le \eps$.
""", r"""
Compact sets are totally bounded, so $M = M_{\eps/2}(p_1) \cup \dots \cup M_{\eps/2}(p_m)$ for some points $p_1, \dots, p_m$, and $m \ge 1$ as $M \ne \varnothing$. Let $K_i = \set{x \in M : d(x,p_i) \le \eps/2}$ be the closed ball. It contains $p_i$, so it is nonempty; it is a closed subset of the compact space $M$, hence compact; and for $x, y \in K_i$ we have $d(x,y) \le d(x,p_i) + d(p_i,y) \le \eps$, so $\diam K_i \le \eps$. Since $K_i \supset M_{\eps/2}(p_i)$, the sets $K_i$ cover $M$.
""", 2, 15, [
    r"Total boundedness gives finitely many small open balls; replace them by closed balls.",
], ["c2-lem-compact-totally-bounded", "c2-ex-closed-ball", "c2-thm-closed-in-compact", "c2-def-diameter"])

s.t("lemma", "c2-lem-labeled-pieces", "Labeling nested pieces by words", r"""
Let $M$ be a nonempty compact metric space. Then there are integers $0 = N_0 < N_1 < N_2 < \cdots$ and, for each $k \ge 0$ and each word $\alpha$ of length $N_k$, a nonempty compact set $M_\alpha \subset M$, such that $M_\alpha = M$ for the empty word and, for every $k \ge 0$:
\begin{itemize}
\item[(a)] if $\gamma$ is a word of length $N_{k+1}$, then $M_\gamma \subset M_{\gamma|N_k}$ and $\diam M_\gamma \le 1/(k+1)$;
\item[(b)] if $\alpha$ is a word of length $N_k$, then $M_\alpha$ is the union of the sets $M_\gamma$ over all words $\gamma$ of length $N_{k+1}$ with $\gamma|N_k = \alpha$.
\end{itemize}
(The sets $M_\gamma$ for different words $\gamma$ need not be different, and need not be disjoint.)
""", r"""
The construction is recursive in $k$. Put $N_0 = 0$ and $M_\alpha = M$ for the empty word $\alpha$, the only word of length $0$; it is nonempty and compact.

Suppose that for some $k \ge 0$ the integer $N_k$ and the nonempty compact sets $M_\alpha$, $\abs{\alpha} = N_k$, have been defined. There are $2^{N_k}$ words $\alpha$ of length $N_k$, finitely many. For each of them, $M_\alpha$ is a nonempty compact metric space, so by the lemma on small compact pieces (with $\eps = 1/(k+1)$) we can write
\[ M_\alpha = K^\alpha_1 \cup \dots \cup K^\alpha_{m_\alpha}, \qquad m_\alpha \ge 1, \]
with each $K^\alpha_i$ nonempty, compact, and of diameter at most $1/(k+1)$.

The numbers $m_\alpha$ may differ from one $\alpha$ to another and need not be powers of $2$, so we pad. Since there are finitely many $\alpha$ and $2^n \ge n$ for all $n$, we can choose an integer $n \ge 1$ with $2^n \ge m_\alpha$ for every word $\alpha$ of length $N_k$. Put $N_{k+1} = N_k + n > N_k$. List the $2^n$ words of length $n$ in some fixed order as $\beta_1, \beta_2, \dots, \beta_{2^n}$. For each word $\alpha$ of length $N_k$ and each $j \in \set{1, \dots, 2^n}$ define
\[ M_{\alpha\beta_j} = K^\alpha_{\min(j,\, m_\alpha)} . \]
So the first $m_\alpha$ labels $\alpha\beta_1, \dots, \alpha\beta_{m_\alpha}$ receive the pieces $K^\alpha_1, \dots, K^\alpha_{m_\alpha}$ in order, and each of the remaining labels $\alpha\beta_j$, $m_\alpha < j \le 2^n$, receives the last piece $K^\alpha_{m_\alpha}$ again.

This defines $M_\gamma$ for every word $\gamma$ of length $N_{k+1}$, and defines it only once: such a $\gamma$ can be written as $\alpha\beta$ with $\abs{\alpha} = N_k$ and $\abs{\beta} = n$ in exactly one way, namely with $\alpha = \gamma|N_k$ the first $N_k$ letters and $\beta = \beta_j$ the last $n$ letters. Each $M_\gamma$ is one of the pieces $K^\alpha_i$, so it is nonempty and compact.

\emph{(a) holds.} If $\gamma = \alpha\beta_j$ then $M_\gamma = K^\alpha_{\min(j,m_\alpha)} \subset M_\alpha = M_{\gamma|N_k}$, and $\diam M_\gamma \le 1/(k+1)$.

\emph{(b) holds.} Fix $\alpha$ of length $N_k$. The words $\gamma$ of length $N_{k+1}$ with $\gamma|N_k = \alpha$ are exactly $\alpha\beta_1, \dots, \alpha\beta_{2^n}$. As $j$ runs through $1, \dots, 2^n$, the index $\min(j, m_\alpha)$ takes every value in $\set{1, \dots, m_\alpha}$, because $2^n \ge m_\alpha$ (the value $i$ is taken at $j = i$). Hence
\[ \bigcup_{j=1}^{2^n} M_{\alpha\beta_j} = \bigcup_{i=1}^{m_\alpha} K^\alpha_i = M_\alpha . \]

By recursion this defines $N_k$ and the sets $M_\alpha$ for all $k$, with (a) and (b) holding at every stage.
""", 4, 50, [
    r"Build the pieces stage by stage: cut each piece $M_\alpha$ of stage $k$ into finitely many nonempty compact pieces of diameter at most $1/(k+1)$, using the lemma on small compact pieces.",
    r"The numbers of sub-pieces differ from piece to piece, but the labels must be all words of one common length. Choose $n$ with $2^n$ at least every one of those numbers, and let the sub-pieces of $M_\alpha$ be labeled by $\alpha\beta$, $\abs{\beta} = n$.",
    r"There may be more labels than pieces: give the same piece to several labels. All that is needed is that every label gets a piece and every piece gets at least one label.",
], ["c2-def-address", "c2-lem-pieces", "c2-def-diameter"])

s.t("theorem", "c2-thm-cantor-surjection", "Cantor surjection theorem", r"""
Let $M$ be a nonempty compact metric space. Then there is a continuous surjection $\sigma : C \to M$ from the Cantor set onto $M$.
""", r"""
Take integers $0 = N_0 < N_1 < N_2 < \cdots$ and nonempty compact sets $M_\alpha \subset M$, for words $\alpha$ of length $N_k$, $k \ge 0$, as in the lemma on labeling nested pieces by words, with its properties (a) and (b). Note that $N_k \ge k$, since the $N_k$ are strictly increasing integers starting at $0$. For an address $\omega$ and $j \le l$ we have $(\omega|l)|j = \omega|j$.

\emph{Step 1: the map.} Let $x \in C$, and let $\omega$ be its address (each point of $C$ has exactly one). For each $k \ge 1$, property (a), applied with $k - 1$ in place of $k$ to the word $\gamma = \omega|N_k$, gives
\[ M_{\omega|N_k} \subset M_{\omega|N_{k-1}} \qquad\text{and}\qquad \diam M_{\omega|N_k} \le \frac1k . \]
So
\[ M_{\omega|N_1} \supset M_{\omega|N_2} \supset M_{\omega|N_3} \supset \cdots \]
is a decreasing sequence of nonempty compact sets whose diameters tend to $0$. By the corollary on nested compact sets shrinking to a point, their intersection is a single point; define $\sigma(x)$ to be that point. Thus $\sigma(x) \in M_{\omega|N_k}$ for every $k \ge 0$ (for $k = 0$ this says $\sigma(x) \in M$).

\emph{Step 2: $\sigma$ is onto.} Let $q \in M$. We choose, recursively, words $\gamma^{(k)}$ of length $N_k$ with
\[ q \in M_{\gamma^{(k)}} \qquad\text{and}\qquad \gamma^{(k+1)}|N_k = \gamma^{(k)} . \]
Let $\gamma^{(0)}$ be the empty word; $q \in M = M_{\gamma^{(0)}}$. Given $\gamma^{(k)}$ with $q \in M_{\gamma^{(k)}}$, property (b) says $M_{\gamma^{(k)}}$ is the union of the $M_\gamma$ with $\abs{\gamma} = N_{k+1}$ and $\gamma|N_k = \gamma^{(k)}$, so $q$ lies in one of them; let $\gamma^{(k+1)}$ be such a $\gamma$.

Since each $\gamma^{(k+1)}$ begins with $\gamma^{(k)}$, by induction $\gamma^{(l)}|N_k = \gamma^{(k)}$ whenever $k \le l$. Define an address $\omega$ as follows: for $i \ge 1$ choose any $k$ with $N_k \ge i$ (there is one, as $N_k \ge k$) and let $\omega_i$ be the $i$-th letter of $\gamma^{(k)}$; this does not depend on the choice of $k$, because for $k \le l$ the word $\gamma^{(l)}$ begins with $\gamma^{(k)}$. Then $\omega|N_k = \gamma^{(k)}$ for every $k$. Let $x = p(\omega) \in C$ be the point with address $\omega$. Then $q \in M_{\omega|N_k}$ for all $k \ge 1$, and $\sigma(x)$ is the only point of $\bigcap_{k \ge 1} M_{\omega|N_k}$, so $\sigma(x) = q$.

\emph{Step 3: $\sigma$ is continuous.} Let $x \in C$ and $\eps > 0$. Choose $k \ge 1$ with $1/k < \eps$ and let $\delta = 3^{-N_k}$. Let $y \in C$ with $\abs{x - y} < \delta$, and let $\omega$, $\omega'$ be the addresses of $x$, $y$. By the lemma that close points share long prefixes, $\omega|N_k = \omega'|N_k$. Hence $\sigma(x) \in M_{\omega|N_k}$ and $\sigma(y) \in M_{\omega'|N_k} = M_{\omega|N_k}$, and
\[ d(\sigma(x), \sigma(y)) \le \diam M_{\omega|N_k} \le \frac1k < \eps . \]
So $\sigma$ satisfies the $\eps,\delta$ condition and is continuous.
""", 4, 60, [
    r"Use the labeled pieces $M_\alpha$ and addresses: an address $\omega$ picks out the pieces $M_{\omega|N_1} \supset M_{\omega|N_2} \supset \cdots$.",
    r"These are nested nonempty compact sets with diameters tending to $0$, so they meet in exactly one point; let that be $\sigma$ of the point of $C$ with address $\omega$. For onto, follow a given $q \in M$ down through the pieces using property (b).",
    r"Continuity: points of $C$ closer than $3^{-N_k}$ have addresses agreeing in the first $N_k$ places, so their images lie in one piece of diameter at most $1/k$.",
], ["c2-lem-labeled-pieces", "c2-thm-addresses", "c2-lem-address-distance", "c2-cor-nested-diameter", "c2-thm-eps-delta", "c2-def-diameter"])

s.r("c2-rem-cantor-surjection", r"""
The theorem says that $C$ is, in a sense, the universal compact metric space: the interval, the disc, the sphere, the cube in $\R^{100}$ are all continuous images of it. The map $\sigma$ is far from one-to-one in general; a connected space such as $[0,1]$ cannot be homeomorphic to the totally disconnected $C$.
""")

s.stated("theorem", "c2-thm-peano-curve", "Peano curves exist", r"""
There is a continuous surjection $\tau : [0,1] \to B^2$ from the interval onto the closed unit disc $B^2 = \set{v \in \R^2 : \abs{v} \le 1}$. Such a map is called a \emph{Peano curve}, or space-filling curve.
""")

s.r("c2-rem-peano", r"""
This is taken on faith here, but the idea is short. By the Cantor surjection theorem there is a continuous surjection $\sigma : C \to B^2$. The complement $[0,1] \setminus C$ is a union of disjoint open intervals $(a,b)$, the removed middle thirds, whose endpoints are in $C$. Extend $\sigma$ over each such gap linearly, $\tau((1-t)a + tb) = (1-t)\sigma(a) + t\sigma(b)$ for $0 \le t \le 1$; the values stay in the disc because it is convex. The verification that $\tau$ is continuous at the points of $C$ uses the uniform continuity of $\sigma$ and is omitted. A Peano curve cannot be one-to-one: a continuous bijection from the compact interval onto the disc would be a homeomorphism, but removing an interior point disconnects the interval and does not disconnect the disc.
""")

s.d("c2-def-cantor-space", "Cantor space", r"""
A metric space is a \emph{Cantor space} if, like the standard Cantor set, it is compact, nonempty, perfect, and totally disconnected.
""")

s.stated("theorem", "c2-thm-moore-kline", "Moore–Kline: Cantor spaces are all alike", r"""
Every Cantor space is homeomorphic to the standard Cantor set $C$.
""")

s.r("c2-rem-moore-kline", r"""
This theorem is stated without proof; its proof refines the labeling of pieces used for the Cantor surjection theorem so that the pieces at each stage are disjoint clopen sets, which makes the resulting map one-to-one. It says that the four properties characterize $C$ topologically. Consequently the fat Cantor sets, the product $C \times C$, and the set of addresses with a natural metric are all homeomorphic to $C$. How a Cantor space sits inside a larger space is a subtler matter: any two Cantor spaces in the line or in the plane are equivalent by a homeomorphism of the whole line or plane, but in $\R^3$ there are "wild" Cantor sets, such as Antoine's necklace, for which this fails.
""")

s.card("c2-card-address", "What is the address of a point of the Cantor set, and what is the point with address $\\omega$?",
       r"The infinite string $\omega_1\omega_2\dots$ of symbols $0$ (left third) and $2$ (right third) recording which third the point lies in at each stage. The point is $\sum_i \omega_i/3^i$; each point of $C$ has exactly one address.",
       "c2-thm-addresses")
s.card("c2-card-ternary", "Describe $C$ in terms of base-$3$ expansions. Give a point of $C$ that is not an endpoint.",
       r"$C$ is the set of $x \in [0,1]$ having a ternary expansion with digits $0$ and $2$ only. $1/4 = 0.020202\dots_3$.",
       "c2-ex-quarter")
s.card("c2-card-address-distance", "How do addresses detect closeness in $C$?",
       r"If two addresses agree in the first $n$ places the points are within $3^{-n}$; if the points are closer than $3^{-n}$ the addresses agree in the first $n$ places.",
       "c2-lem-address-distance")
s.card("c2-card-cantor-surjection", "State the Cantor surjection theorem.",
       r"Every nonempty compact metric space $M$ is the image of the Cantor set under a continuous surjection $\sigma : C \to M$.",
       "c2-thm-cantor-surjection")
s.card("c2-card-cantor-surjection-idea", "Idea of the proof of the Cantor surjection theorem.",
       r"Divide $M$ into finitely many small compact pieces labeled by all words in $0, 2$ of one length (repeating pieces under several labels if there are too few), subdivide repeatedly with diameters $\to 0$; an address selects nested pieces meeting in one point $\sigma(x)$. Onto since the pieces cover; continuous since nearby points of $C$ share long prefixes.",
       "c2-thm-cantor-surjection")
s.card("c2-card-peano", "What is a Peano curve? Can it be one-to-one?",
       r"A continuous surjection from $[0,1]$ onto the disc (or square). No: it would be a homeomorphism (compact domain), but removing a point disconnects the interval and not the disc.",
       "c2-thm-peano-curve")
s.card("c2-card-moore-kline", "Define Cantor space and state the Moore–Kline theorem.",
       r"A compact, nonempty, perfect, totally disconnected metric space. Every Cantor space is homeomorphic to the standard Cantor set.",
       "c2-thm-moore-kline")

s.write()
