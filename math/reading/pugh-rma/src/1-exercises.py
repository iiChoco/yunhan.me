from __future__ import annotations
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from c1_common import Section

s = Section("1-exercises")


def ex(id: str, title: str, tex: str, proof: str, d: int, m: int, hints: list[str], uses: list[str]) -> None:
    s.result(id, "exercise", title, tex, proof, d, m, hints, uses)
    s.blocks[-1]["optional"] = True


s.prose("exercises-intro", r"""
The exercises below are extra credit and may be taken in any order; none of them is a gate, and the chapter clears on its theorems alone. Each can be solved from what this chapter has proved, and the items listed under an exercise are the ones worth having in mind.
""")

# ---------------------------------------------------------------- least upper bounds
ex("ex-sup-of-subset", "Suprema of subsets and of bounded sets", r"""
\begin{enumerate}
\item Let $A \subset B \subset \R$ with $A \ne \varnothing$ and $B$ bounded above. Prove that $\lub A$ and $\lub B$ exist and that $\lub A \le \lub B$.
\item Let $S \subset \R$ be nonempty and bounded. Prove that $\glb S \le \lub S$, with equality if and only if $S$ consists of a single point.
\item Let $S \subset \R$ be nonempty and bounded above, and suppose $\lub S \notin S$. Prove that $S$ is infinite.
\end{enumerate}
""", r"""
(1) Let $M$ be an upper bound for $B$. Every $a \in A$ lies in $B$, so $a \le M$: thus $A$ is bounded above, and it is nonempty by hypothesis. $B$ is nonempty because it contains $A$. By the least upper bound property both $\lub A$ and $\lub B$ exist. Since $\lub B$ is an upper bound for $B$, it is an upper bound for the subset $A$; and $\lub A$ is the least upper bound of $A$, so $\lub A \le \lub B$.

(2) Both bounds exist by the least upper bound property and the greatest lower bound property. Pick any $s \in S$. Then $\glb S \le s$ because $\glb S$ is a lower bound, and $s \le \lub S$ because $\lub S$ is an upper bound; hence $\glb S \le \lub S$. If $\glb S = \lub S = m$, then every $s \in S$ satisfies $m \le s \le m$, so $S = \set{m}$. Conversely, if $S = \set{m}$ then $m$ is both an upper and a lower bound, and no smaller number is an upper bound (it would be less than $m \in S$) and no larger number a lower bound; so $\lub S = \glb S = m$.

(3) Let $M = \lub S$ and suppose $S$ is finite. A nonempty finite set of real numbers has a largest element $m$, and $m \in S$. Then $m$ is an upper bound for $S$, so $M \le m$ because $M$ is the least upper bound; and $m \le M$ because $M$ is an upper bound and $m \in S$. Hence $M = m \in S$, contradicting the hypothesis. So $S$ is infinite.
""", 1, 15, [
    r"Everything here is an unwinding of the definitions of upper bound, least upper bound, and greatest lower bound; in (3) use that a nonempty finite set of reals has a largest element.",
], ["def-upper-bound", "thm-lub", "cor-glb", "rem-finite-facts"])

ex("ex-lub-approximation", "Characterising the least upper bound", r"""
Let $S \subset \R$ be nonempty and bounded above, and let $M$ be an upper bound for $S$.
\begin{enumerate}
\item Prove that $M = \lub S$ if and only if for every $\eps > 0$ there is an $s \in S$ with $s > M - \eps$.
\item Deduce that there is a sequence $(s_n)$ of elements of $S$ with $s_n \to \lub S$.
\end{enumerate}
""", r"""
(1) Suppose $M = \lub S$ and let $\eps > 0$. Since $M - \eps < M$, the number $M - \eps$ is not an upper bound for $S$ (if it were, the least upper bound would satisfy $M \le M - \eps$). So some $s \in S$ fails $s \le M - \eps$, that is, $s > M - \eps$.

Conversely, suppose that for every $\eps > 0$ some $s \in S$ satisfies $s > M - \eps$. By hypothesis $M$ is an upper bound. Let $M'$ be any upper bound for $S$, and suppose $M' < M$. Put $\eps = M - M' > 0$; there is an $s \in S$ with $s > M - \eps = M'$, contradicting that $M'$ is an upper bound. Hence $M \le M'$ for every upper bound $M'$, and $M = \lub S$.

(2) Let $M = \lub S$. For each $n \in \N$ apply (1) with $\eps = 1/n$ and choose $s_n \in S$ with $s_n > M - 1/n$. Since $s_n \le M$ as well, $\abs{s_n - M} = M - s_n < 1/n$. Given $\eps > 0$, the Archimedean property gives $N \in \N$ with $1/N < \eps$, and for $n \ge N$ we get $\abs{s_n - M} < 1/n \le 1/N < \eps$. So $s_n \to M$.
""", 1, 15, [
    r"If $M$ is the least upper bound, then $M - \eps$ is not an upper bound; say what that means. For the converse, suppose an upper bound $M' < M$ existed and choose $\eps$ to be the gap.",
    r"For (2), choose $s_n$ with $\eps = 1/n$ and use the Archimedean property to make $1/n$ small.",
], ["def-upper-bound", "thm-archimedean", "def-convergence"])

ex("ex-lub-of-sum-and-negative", "Suprema of sums and of negatives", r"""
Let $A, B \subset \R$ be nonempty and bounded above, and put
\[ A + B = \set{a + b : a \in A,\ b \in B}, \qquad -A = \set{-a : a \in A}. \]
Prove that $\lub (A + B) = \lub A + \lub B$ and that $\glb (-A) = -\lub A$.
""", r"""
Write $\alpha = \lub A$ and $\beta = \lub B$.

\emph{The sum.} For $a \in A$ and $b \in B$ we have $a \le \alpha$ and $b \le \beta$, so $a + b \le \alpha + \beta$. Thus $A + B$ is nonempty and bounded above by $\alpha + \beta$; its least upper bound $\gamma = \lub (A + B)$ exists and $\gamma \le \alpha + \beta$.

For the reverse inequality let $\eps > 0$. Since $\alpha - \eps/2 < \alpha$ is not an upper bound for $A$, there is an $a \in A$ with $a > \alpha - \eps/2$; likewise there is a $b \in B$ with $b > \beta - \eps/2$. Then $a + b \in A + B$, so
\[ \alpha + \beta - \eps < a + b \le \gamma, \]
that is, $\alpha + \beta \le \gamma + \eps$. This holds for every $\eps > 0$, so by the $\eps$-principle $\alpha + \beta \le \gamma$. Hence $\gamma = \alpha + \beta$.

\emph{The negative.} For every $a \in A$, $a \le \alpha$ gives $-\alpha \le -a$; so $-\alpha$ is a lower bound for $-A$, which is nonempty. Let $\ell$ be any lower bound for $-A$. Then $\ell \le -a$, that is, $a \le -\ell$, for every $a \in A$; so $-\ell$ is an upper bound for $A$, and $\alpha \le -\ell$, that is, $\ell \le -\alpha$. Thus $-\alpha$ is the greatest lower bound of $-A$.
""", 2, 20, [
    r"One inequality is immediate: $\lub A + \lub B$ is an upper bound for $A + B$. For the other, show that $\lub A + \lub B - \eps$ is not an upper bound, for every $\eps > 0$.",
    r"Pick $a \in A$ within $\eps/2$ of $\lub A$ and $b \in B$ within $\eps/2$ of $\lub B$, then finish with the $\eps$-principle.",
], ["def-upper-bound", "thm-lub", "cor-glb", "prop-eps-principle"])

ex("ex-nested-intervals", "Nested intervals", r"""
Let $I_n = [a_n, b_n]$, $n \in \N$, be closed intervals with $a_n \le b_n$ and $I_{n+1} \subset I_n$ for every $n$.
\begin{enumerate}
\item Prove that $\bigcap_{n \in \N} I_n$ is nonempty.
\item Prove that if $b_n - a_n \to 0$, then $\bigcap_{n \in \N} I_n$ consists of exactly one point $c$, and $a_n \to c$ and $b_n \to c$.
\item Prove or disprove: the conclusion of (1) holds for nested open intervals $(a_n, b_n)$ with $a_n < b_n$.
\end{enumerate}
""", r"""
(1) Since $a_{n+1}$ and $b_{n+1}$ belong to $I_{n+1} \subset I_n$, we have $a_n \le a_{n+1}$ and $b_{n+1} \le b_n$ for every $n$. By induction, $a_m \le a_n$ and $b_n \le b_m$ whenever $m \le n$. Hence for any $m, n \in \N$, with $k = \max(m, n)$,
\[ a_m \le a_k \le b_k \le b_n. \]
So every $b_n$ is an upper bound for the nonempty set $\set{a_m : m \in \N}$, and by the least upper bound property $c = \lub \set{a_m : m \in \N}$ exists. For each $n$, $a_n \le c$ because $c$ is an upper bound, and $c \le b_n$ because $b_n$ is an upper bound and $c$ is the least one. Thus $c \in I_n$ for every $n$, and $c \in \bigcap_n I_n$.

(2) Suppose $b_n - a_n \to 0$, and let $c, c'$ both lie in every $I_n$. Then $a_n \le c, c' \le b_n$, so $\abs{c - c'} \le b_n - a_n$ for every $n$. Given $\eps > 0$ there is an $n$ with $b_n - a_n < \eps$, hence $\abs{c - c'} < \eps$. By the $\eps$-principle, $c = c'$. So the intersection is the single point $c$ found in (1).

For the convergence, let $\eps > 0$ and choose $N$ with $b_n - a_n < \eps$ for $n \ge N$. For such $n$, $a_n \le c \le b_n$ gives $\abs{a_n - c} = c - a_n \le b_n - a_n < \eps$ and $\abs{b_n - c} = b_n - c \le b_n - a_n < \eps$. Hence $a_n \to c$ and $b_n \to c$.

(3) False. The open intervals $J_n = (0, 1/n)$ are nested, since $1/(n+1) < 1/n$. If $x$ belonged to every $J_n$, then $x > 0$ and $x < 1/n$ for all $n \in \N$; but by the Archimedean property there is an $n$ with $1/n < x$. So $\bigcap_n J_n = \varnothing$.
""", 3, 30, [
    r"The left endpoints increase and the right endpoints decrease, and every right endpoint is above every left endpoint. Which number should lie in all the intervals?",
    r"Let $c = \lub \set{a_n}$ and check $a_n \le c \le b_n$ for every $n$. In (2), two common points are within $b_n - a_n$ of each other for every $n$.",
    r"For (3), think about $(0, 1/n)$.",
], ["thm-lub", "def-upper-bound", "def-interval", "def-convergence", "prop-eps-principle", "thm-archimedean"])

ex("ex-irrational-arithmetic", "Arithmetic with irrational numbers", r"""
\begin{enumerate}
\item Let $r \in \Q$ and let $x$ be irrational. Prove that $r + x$ is irrational, and that $rx$ is irrational if $r \ne 0$.
\item Prove that $\sqrt{2} + \sqrt{3}$ is irrational.
\item Prove or disprove: the sum of two irrational numbers is irrational.
\end{enumerate}
""", r"""
(1) Suppose $r + x = s$ with $s \in \Q$. Then $x = s - r$ is a difference of rational numbers, hence rational, contrary to hypothesis. Suppose $r \ne 0$ and $rx = s \in \Q$. Then $x = s/r$ is a quotient of rational numbers with nonzero denominator, hence rational, again a contradiction.

(2) By the existence of square roots there are positive real numbers $\sqrt{2}$ and $\sqrt{3}$ with squares $2$ and $3$. Suppose $r = \sqrt{2} + \sqrt{3}$ were rational. Then $r > 0$, and $\sqrt{3} = r - \sqrt{2}$. Squaring,
\[ 3 = r^2 - 2r\sqrt{2} + 2, \qquad\text{so}\qquad \sqrt{2} = \frac{r^2 - 1}{2r}, \]
which is a rational number because $r$ is rational and $2r \ne 0$. But then $\sqrt{2}$ would be a rational number whose square is $2$, and there is none. Hence $\sqrt{2} + \sqrt{3}$ is irrational.

(3) False. The number $\sqrt{2}$ is irrational, since its square is $2$ and no rational has square $2$; by (1) with $r = -1$, so is $-\sqrt{2}$. Their sum is $0 \in \Q$.
""", 2, 20, [
    r"In (1), solve for $x$. In (2), suppose the sum is rational, isolate one square root, and square.",
    r"From $\sqrt{3} = r - \sqrt{2}$ you get $\sqrt{2}$ as a rational expression in $r$.",
], ["thm-sqrt2-irrational", "thm-square-roots", "def-real-number", "rem-field-on-faith"])

# ---------------------------------------------------------------- sequences
ex("ex-abs-and-sqrt-limits", "Limits of absolute values and of square roots", r"""
Let $(a_n)$ be a sequence of real numbers with $a_n \to a$.
\begin{enumerate}
\item Prove that $\abs{a_n} \to \abs{a}$.
\item Show that the converse fails: give a sequence $(a_n)$ such that $(\abs{a_n})$ converges but $(a_n)$ does not.
\item Suppose $a_n \ge 0$ for every $n$. Prove that $a \ge 0$ and that $\sqrt{a_n} \to \sqrt{a}$.
\end{enumerate}
""", r"""
(1) By the inequality $\big|\abs{a_n} - \abs{a}\big| \le \abs{a_n - a}$, any $N$ that makes $\abs{a_n - a} < \eps$ for $n \ge N$ also makes $\big|\abs{a_n} - \abs{a}\big| < \eps$ for $n \ge N$.

(2) Let $a_n = (-1)^n$. Then $\abs{a_n} = 1$ for every $n$, and the constant sequence converges to $1$. If $(a_n)$ converged, it would be a Cauchy sequence; but $\abs{a_{n+1} - a_n} = 2$ for every $n$, so the Cauchy condition fails for $\eps = 2$. Hence $(a_n)$ does not converge.

(3) Since $a_n \ge 0$ for all $n$, the limit satisfies $a \ge 0$ because limits respect weak inequalities. All square roots below exist and are nonnegative.

\emph{Case $a = 0$.} Let $\eps > 0$ and choose $N$ with $a_n = \abs{a_n - 0} < \eps^2$ for $n \ge N$. For such $n$, if $\sqrt{a_n} \ge \eps$ then, both numbers being nonnegative, $a_n = (\sqrt{a_n})^2 \ge \eps^2$, which is false; so $\abs{\sqrt{a_n} - 0} = \sqrt{a_n} < \eps$.

\emph{Case $a > 0$.} Then $\sqrt{a} > 0$. For every $n$,
\[ (\sqrt{a_n} - \sqrt{a})(\sqrt{a_n} + \sqrt{a}) = a_n - a, \qquad \sqrt{a_n} + \sqrt{a} \ge \sqrt{a} > 0, \]
so $\abs{\sqrt{a_n} - \sqrt{a}} = \dfrac{\abs{a_n - a}}{\sqrt{a_n} + \sqrt{a}} \le \dfrac{\abs{a_n - a}}{\sqrt{a}}$. Given $\eps > 0$, choose $N$ with $\abs{a_n - a} < \eps\sqrt{a}$ for $n \ge N$; then $\abs{\sqrt{a_n} - \sqrt{a}} < \eps$ for $n \ge N$.
""", 2, 25, [
    r"For (1) use $\big|\abs{x} - \abs{y}\big| \le \abs{x - y}$. For (2) try a sequence that alternates.",
    r"For (3), separate $a = 0$ from $a > 0$; in the second case write $\sqrt{a_n} - \sqrt{a} = \dfrac{a_n - a}{\sqrt{a_n} + \sqrt{a}}$ and bound the denominator below by $\sqrt{a}$.",
], ["def-convergence", "prop-triangle-inequality", "thm-square-roots", "lem-convergent-cauchy", "def-cauchy", "prop-limit-order", "rem-square-compare"])

ex("ex-fast-cauchy", "Rapidly shrinking steps, and not so rapidly", r"""
\begin{enumerate}
\item Let $(a_n)$ be a sequence of real numbers with $\abs{a_{n+1} - a_n} \le 2^{-n}$ for every $n \in \N$. Prove that $(a_n)$ converges.
\item Prove or disprove: if $a_{n+1} - a_n \to 0$, then $(a_n)$ is a Cauchy sequence.
\end{enumerate}
""", r"""
(1) Two preliminary facts. First, $2^n \ge n$ for all $n \in \N$: $2^1 \ge 1$, and $2^{n+1} = 2 \cdot 2^n \ge 2n \ge n + 1$. Second, for $n < m$,
\[ \sum_{k=n}^{m-1} 2^{-k} = 2^{1-n} - 2^{1-m}, \]
by induction on $m$: for $m = n + 1$ both sides equal $2^{-n}$, and adding $2^{-m}$ to $2^{1-n} - 2^{1-m}$ gives $2^{1-n} - 2^{-m} = 2^{1-n} - 2^{1-(m+1)}$.

Now let $n < m$. Applying the triangle inequality $m - n - 1$ times,
\[ \abs{a_m - a_n} \le \sum_{k=n}^{m-1} \abs{a_{k+1} - a_k} \le \sum_{k=n}^{m-1} 2^{-k} = 2^{1-n} - 2^{1-m} < 2^{1-n} = \frac{2}{2^n} \le \frac{2}{n}. \]
Given $\eps > 0$, the Archimedean property gives $N \in \N$ with $1/N < \eps/2$. For $m, n \ge N$ with $m \ne n$ we may assume $n < m$ by symmetry, and then $\abs{a_m - a_n} < 2/n \le 2/N < \eps$; for $m = n$ the difference is $0$. So $(a_n)$ is a Cauchy sequence, and it converges because Cauchy sequences converge.

(2) False. Let $a_n = \sqrt{n}$. Since $(\sqrt{n+1} - \sqrt{n})(\sqrt{n+1} + \sqrt{n}) = 1$,
\[ 0 < a_{n+1} - a_n = \frac{1}{\sqrt{n+1} + \sqrt{n}} < \frac{1}{\sqrt{n}}. \]
Given $\eps > 0$, choose $N \in \N$ with $N > 1/\eps^2$. For $n \ge N$ we have $n > 1/\eps^2 = (1/\eps)^2$; as $\sqrt{n}$ and $1/\eps$ are positive, comparing squares gives $\sqrt{n} > 1/\eps$, so $1/\sqrt{n} < \eps$ and $\abs{a_{n+1} - a_n} < \eps$. Thus $a_{n+1} - a_n \to 0$.

But $(a_n)$ is not bounded: given any $M \ge 0$, choose $n \in \N$ with $n > M^2$; comparing squares of nonnegative numbers, $\sqrt{n} > M$. Cauchy sequences are bounded, so $(a_n)$ is not a Cauchy sequence.
""", 3, 30, [
    r"For (1), estimate $\abs{a_m - a_n}$ by a sum of consecutive steps and sum the geometric bound; to see the bound is eventually below $\eps$ note $2^n \ge n$.",
    r"For (2), the condition only controls consecutive terms. Look for a sequence whose steps shrink but which wanders off to infinity; $\sqrt{n}$ is one.",
    r"A Cauchy sequence is bounded. Show $\sqrt{n}$ is not, using the Archimedean property.",
], ["def-cauchy", "thm-cauchy-complete", "lem-cauchy-bounded", "thm-archimedean", "prop-triangle-inequality", "thm-square-roots", "rem-square-compare"])

ex("ex-bolzano-weierstrass", "Monotone subsequences and the Bolzano–Weierstrass theorem", r"""
A \emph{subsequence} of a sequence $(a_n)$ is a sequence of the form $(a_{n_k})_{k \in \N}$ where $n_1 < n_2 < n_3 < \cdots$ are natural numbers.
\begin{enumerate}
\item Prove that every sequence of real numbers has a monotone subsequence.
\item Deduce that every bounded sequence of real numbers (one whose set of terms $\set{a_n : n \in \N}$ is bounded) has a convergent subsequence.
\end{enumerate}
""", r"""
(1) Call an index $m \in \N$ a \emph{peak} of $(a_n)$ if $a_m \ge a_n$ for every $n > m$. Let $P$ be the set of peaks.

\emph{Case A: $P$ is infinite.} Define $m_1$ as the least element of $P$ and, given $m_k$, define $m_{k+1}$ as the least element of $P \setminus \set{1, \dots, m_k}$. This set is nonempty: otherwise $P \subset \set{1, \dots, m_k}$ would be finite. By the least element principle the definition makes sense, and $m_{k+1} > m_k$. Since $m_k$ is a peak and $m_{k+1} > m_k$, we have $a_{m_k} \ge a_{m_{k+1}}$ for every $k$, and by induction $a_{m_j} \ge a_{m_k}$ whenever $j \le k$. So $(a_{m_k})$ is a nonincreasing subsequence.

\emph{Case B: $P$ is finite.} Then there is an $n_1 \in \N$ greater than every peak: take $n_1 = 1$ if $P = \varnothing$, and otherwise $n_1 = 1 + \max P$. Suppose $n_k$ has been chosen with $n_k$ greater than every peak. Then $n_k$ is not a peak, so there is an $n_{k+1} > n_k$ with $a_{n_{k+1}} > a_{n_k}$; and $n_{k+1}$ is again greater than every peak. This defines $n_1 < n_2 < \cdots$ with $a_{n_k} < a_{n_{k+1}}$ for all $k$, hence $a_{n_j} \le a_{n_k}$ for $j \le k$ by induction. So $(a_{n_k})$ is a nondecreasing subsequence.

(2) Let the set of terms be bounded above by $U$ and below by $L$. By (1) there is a monotone subsequence $(a_{n_k})$. Its set of terms $\set{a_{n_k} : k \in \N}$ is a subset of $\set{a_n : n \in \N}$, so it is bounded above by $U$ and below by $L$. If the subsequence is nondecreasing it is bounded above, and if nonincreasing it is bounded below; in either case it converges, because bounded monotone sequences converge.
""", 4, 60, [
    r"Call $m$ a peak if $a_m$ is at least as large as every later term. There are either infinitely many peaks or finitely many; treat the two cases separately.",
    r"Infinitely many peaks, listed in increasing order, give a nonincreasing subsequence. If there are finitely many, start after the last one: an index that is not a peak is followed by a strictly larger term.",
    r"For (2), a subsequence of a bounded sequence is bounded, and a bounded monotone sequence converges.",
], ["def-monotone", "prop-monotone-convergence", "def-convergence", "prelim-naturals", "rem-finite-facts"])

# ---------------------------------------------------------------- euclidean space
ex("ex-polarisation-pythagoras", "The inner product is determined by lengths", r"""
Let $V$ be an inner product space and $x, y \in V$.
\begin{enumerate}
\item Prove the \emph{polarisation identity} $\inner{x}{y} = \dfrac{\abs{x + y}^2 - \abs{x - y}^2}{4}$.
\item Prove that $\abs{x + y}^2 = \abs{x}^2 + \abs{y}^2$ if and only if $\inner{x}{y} = 0$.
\item Suppose $y \ne 0$ and $\abs{x + y} = \abs{x} + \abs{y}$. Prove that $x = cy$ for some $c \ge 0$.
\end{enumerate}
""", r"""
By bilinearity and symmetry of the inner product,
\[ \abs{x + y}^2 = \inner{x + y}{x + y} = \abs{x}^2 + 2\inner{x}{y} + \abs{y}^2, \qquad \abs{x - y}^2 = \abs{x}^2 - 2\inner{x}{y} + \abs{y}^2. \]

(1) Subtracting the second expansion from the first gives $\abs{x + y}^2 - \abs{x - y}^2 = 4\inner{x}{y}$.

(2) By the first expansion, $\abs{x + y}^2 = \abs{x}^2 + \abs{y}^2$ holds exactly when $2\inner{x}{y} = 0$, that is, when $\inner{x}{y} = 0$.

(3) Squaring the hypothesis and using the first expansion,
\[ \abs{x}^2 + 2\inner{x}{y} + \abs{y}^2 = \abs{x + y}^2 = (\abs{x} + \abs{y})^2 = \abs{x}^2 + 2\abs{x}\abs{y} + \abs{y}^2, \]
so $\inner{x}{y} = \abs{x}\abs{y}$. In particular $\abs{\inner{x}{y}} = \abs{x}\abs{y}$, and since $y \ne 0$ the equality case of the Cauchy–Schwarz inequality gives $x = cy$ for some $c \in \R$. Then $\inner{x}{y} = c\inner{y}{y} = c\abs{y}^2$, while $\abs{x}\abs{y} = \abs{cy}\abs{y} = \abs{c}\abs{y}^2$ because the length is a norm. Hence $c\abs{y}^2 = \abs{c}\abs{y}^2$, and $\abs{y}^2 > 0$ by positive definiteness, so $c = \abs{c} \ge 0$.
""", 2, 20, [
    r"Expand $\abs{x \pm y}^2 = \inner{x \pm y}{x \pm y}$ by bilinearity; everything follows from the two expansions.",
    r"In (3), squaring the hypothesis gives $\inner{x}{y} = \abs{x}\abs{y}$, which is the equality case of Cauchy–Schwarz. Then compute $\inner{x}{y}$ with $x = cy$ to see the sign of $c$.",
], ["def-inner-product", "rem-square-compare", "ex-cs-equality", "prop-inner-product-norm", "thm-cauchy-schwarz"])

# ---------------------------------------------------------------- cardinality
ex("ex-finite-subsets-and-functions", "Finite subsets of N, and functions on N", r"""
\begin{enumerate}
\item Prove that the set $\mathcal{F}$ of all finite subsets of $\N$ is denumerable.
\item Prove that the set $\N^{\N}$ of all functions $\N \to \N$ is uncountable.
\end{enumerate}
""", r"""
(1) For $n \in \N$ let $\mathcal{P}_n$ be the class of all subsets of $\set{1, \dots, n}$. We show by induction that each $\mathcal{P}_n$ is countable. $\mathcal{P}_1 = \set{\varnothing, \set{1}}$ is finite. Suppose $\mathcal{P}_n$ is countable. A subset $T$ of $\set{1, \dots, n + 1}$ either does not contain $n + 1$, in which case $T \in \mathcal{P}_n$, or contains it, in which case $T = T' \cup \set{n + 1}$ with $T' = T \setminus \set{n + 1} \in \mathcal{P}_n$. Hence $\mathcal{P}_{n+1} = \mathcal{P}_n \cup g(\mathcal{P}_n)$, where $g(T') = T' \cup \set{n + 1}$. The class $g(\mathcal{P}_n)$ is the image of the countable class $\mathcal{P}_n$ under the surjection $g \colon \mathcal{P}_n \to g(\mathcal{P}_n)$, so it is countable, and a union of two countable sets is countable. This completes the induction.

Every finite subset $T$ of $\N$ lies in some $\mathcal{P}_n$: if $T = \varnothing$ take $n = 1$; otherwise $T$ is a nonempty finite set of real numbers and has a largest element $n$, so $T \subset \set{1, \dots, n}$. Hence $\mathcal{F} = \bigcup_{n \in \N} \mathcal{P}_n$ is a countable union of countable sets, so it is countable. It is infinite, because $n \mapsto \set{n}$ is an injection $\N \to \mathcal{F}$. A countable infinite set is denumerable.

(2) Let $\Sigma$ be the set of sequences $\N \to \set{0, 1}$ and define $\Psi \colon \Sigma \to \N^{\N}$ by $\Psi(\sigma)(k) = \sigma(k) + 1$, which takes values in $\set{1, 2} \subset \N$. If $\Psi(\sigma) = \Psi(\tau)$ then $\sigma(k) + 1 = \tau(k) + 1$ for every $k$, so $\sigma = \tau$: $\Psi$ is an injection. Suppose $\N^{\N}$ were countable. Then its subset $\Psi(\Sigma)$ would be countable and nonempty, so by the criteria for countability there would be an injection $h \colon \Psi(\Sigma) \to \N$, and $h \circ \Psi \colon \Sigma \to \N$ would be an injection, making $\Sigma$ countable. But $\Sigma$ is uncountable by the diagonal argument. Hence $\N^{\N}$ is uncountable.
""", 3, 30, [
    r"For (1), every finite subset of $\N$ lies inside some $\set{1, \dots, n}$. How many subsets does $\set{1, \dots, n}$ have, and what does a countable union of countable sets give?",
    r"Show by induction that the subsets of $\set{1, \dots, n}$ form a countable class: each subset of $\set{1, \dots, n + 1}$ is a subset of $\set{1, \dots, n}$ with or without $n + 1$ added.",
    r"For (2), the sequences of $0$'s and $1$'s inject into $\N^{\N}$ (add $1$ to every term), and they are uncountable.",
], ["def-countable", "rem-finite-facts", "thm-countable-union", "cor-subset-image-countable", "thm-diagonal", "prop-countable-criteria", "prop-composition", "def-injection"])

ex("ex-algebraic-numbers-countable", "Algebraic numbers are countable; transcendental numbers exist", r"""
A real number $x$ is \emph{algebraic} if $a_0 + a_1 x + \dots + a_n x^n = 0$ for some $n \ge 0$ and integers $a_0, \dots, a_n$ that are not all zero; otherwise $x$ is \emph{transcendental}. Prove that the set $\mathcal{A}$ of algebraic numbers is denumerable, and that the set of transcendental numbers is uncountable (in particular, nonempty). You may use the fact from algebra that a polynomial with real coefficients that are not all zero has only finitely many real roots.
""", r"""
For $n \ge 0$ let $\Z^{n+1}$ be the set of $(n+1)$-tuples of integers. It is a subset of $\Q^{n+1}$, the set of points of $\R^{n+1}$ with rational coordinates, which is denumerable; so $\Z^{n+1}$ is countable, and so is its subset $P_n = \Z^{n+1} \setminus \set{(0, \dots, 0)}$. Put $A_k = P_{k-1}$ for $k \in \N$; then $P = \bigcup_{k \in \N} A_k$, the set of all integer tuples that are not all zero, is a countable union of countable sets, hence countable. It is nonempty.

For a tuple $a = (a_0, \dots, a_n) \in P$ let $Z(a) = \set{x \in \R : a_0 + a_1 x + \dots + a_n x^n = 0}$. By the fact quoted in the statement, $Z(a)$ is finite, hence countable. Since $P$ is countable and nonempty, the criteria for countability give a surjection $\varphi \colon \N \to P$. Every algebraic $x$ lies in $Z(a)$ for some $a \in P$, and $a = \varphi(k)$ for some $k$; conversely each $Z(\varphi(k))$ consists of algebraic numbers, since $\varphi(k)$ is a tuple of integers that are not all zero. So
\[ \mathcal{A} = \bigcup_{k \in \N} Z(\varphi(k)), \]
a countable union of countable sets. Hence $\mathcal{A}$ is countable. It contains $\Q$, since a rational $p/q$ with $q \ne 0$ is a root of $-p + qx$; so $\mathcal{A}$ is infinite, hence denumerable.

If the set $\R \setminus \mathcal{A}$ of transcendental numbers were countable, then $\R = \mathcal{A} \cup (\R \setminus \mathcal{A})$ would be a union of two countable sets, hence countable, which it is not. So the transcendental numbers are uncountable, and in particular there are some.
""", 3, 40, [
    r"Each nonzero polynomial has finitely many roots, so it suffices to show that there are only countably many integer polynomials. Encode a polynomial by its tuple of coefficients.",
    r"Tuples of integers of length $n + 1$ form a countable set (they sit inside $\Q^{n+1}$), and the union over all $n$ is still countable. Then take the union of the root sets.",
    r"Transcendental numbers: if they were countable, so would $\R$ be.",
], ["ex-qm-denumerable", "cor-subset-image-countable", "thm-countable-union", "prop-countable-criteria", "cor-r-uncountable", "def-countable", "rem-finite-facts", "cor-q-denumerable"])

ex("ex-removing-a-countable-set", "Removing a countable set from an uncountable one", r"""
Let $S$ be an uncountable set and let $C \subset S$ be countable. Prove that $S \setminus C \sim S$. Deduce that $\R \setminus \Q \sim \R$ and that $[0, 1] \setminus \Q \sim \R$.
""", r"""
If $S \setminus C$ were countable, then $S = C \cup (S \setminus C)$ would be a union of two countable sets, hence countable; so $S \setminus C$ is uncountable, in particular infinite. Therefore $S \setminus C$ contains a denumerable subset $D$.

The set $C \cup D$ is countable, as a union of two countable sets, and infinite, since it has the infinite subset $D$; so it is denumerable. Thus $C \cup D \sim \N$ and $\N \sim D$, and composing bijections gives a bijection $g \colon C \cup D \to D$.

Define $h \colon S \to S \setminus C$ by
\[ h(s) = \begin{cases} g(s) & \text{if } s \in C \cup D, \\ s & \text{if } s \in S \setminus (C \cup D). \end{cases} \]
The values lie in $S \setminus C$: if $s \in C \cup D$ then $g(s) \in D \subset S \setminus C$, and if $s \notin C \cup D$ then $s \notin C$.

\emph{Injective.} $h$ maps $C \cup D$ into $D$ and $S \setminus (C \cup D)$ into itself, and these two target sets are disjoint because $D \subset C \cup D$. So if $h(u) = h(v)$, then $u$ and $v$ lie in the same one of the two pieces. On $C \cup D$, $h = g$ is injective; on $S \setminus (C \cup D)$, $h$ is the identity. Either way $u = v$.

\emph{Surjective.} Let $t \in S \setminus C$. If $t \in D$, then $t = g(s)$ for some $s \in C \cup D$ because $g$ is onto $D$, and $h(s) = t$. If $t \notin D$, then $t \notin C$ and $t \notin D$, so $t \in S \setminus (C \cup D)$ and $h(t) = t$.

Hence $h$ is a bijection and $S \sim S \setminus C$.

\emph{Applications.} $\R$ is uncountable and $\Q$ is countable, so $\R \setminus \Q \sim \R$. The interval $[0, 1]$ is uncountable and $[0, 1] \cap \Q$ is countable, being a subset of $\Q$; so $[0, 1] \setminus \Q = [0, 1] \setminus ([0, 1] \cap \Q) \sim [0, 1]$, and $[0, 1] \sim \R$ because every closed interval has the cardinality of the line.
""", 3, 35, [
    r"Compare with the exercise on removing a single point from an infinite set. There, a denumerable subset absorbed the extra point; here it must absorb all of $C$.",
    r"Pick a denumerable $D \subset S \setminus C$. Then $C \cup D$ is denumerable too, so there is a bijection $C \cup D \to D$. Use it on $C \cup D$ and the identity elsewhere.",
], ["prop-infinite-contains-denumerable", "thm-countable-union", "rem-finite-facts", "def-countable", "prop-cardinality-equivalence", "prop-composition", "cor-r-uncountable", "cor-q-denumerable", "cor-intervals", "cor-subset-image-countable", "def-equal-cardinality", "ex-hilbert-hotel"])

ex("ex-sequences-of-reals", "The set of all real sequences has the cardinality of the line", r"""
For a set $A$ let $A^{\N}$ denote the set of all functions $\N \to A$, that is, of all sequences with terms in $A$. Let $\Sigma = \set{0, 1}^{\N}$ be the set of sequences of $0$'s and $1$'s.
\begin{enumerate}
\item Prove that if $A \sim B$ then $A^{\N} \sim B^{\N}$.
\item Prove that $\Sigma^{\N} \sim \Sigma$.
\item Conclude that $\R^{\N} \sim \R$, and then that $\R \times \R \sim \R$.
\end{enumerate}
""", r"""
(1) Let $f \colon A \to B$ be a bijection with inverse $f^{-1}$. Define $F \colon A^{\N} \to B^{\N}$ by $F(\alpha) = f \circ \alpha$ and $G \colon B^{\N} \to A^{\N}$ by $G(\beta) = f^{-1} \circ \beta$. Then $G(F(\alpha)) = f^{-1} \circ f \circ \alpha = \alpha$ and $F(G(\beta)) = f \circ f^{-1} \circ \beta = \beta$, so $G$ is an inverse of $F$ and $F$ is a bijection.

(2) Since $\N \times \N$ is denumerable there is a bijection $\N \times \N \to \N$; let $\psi \colon \N \to \N \times \N$ be its inverse. An element of $\Sigma^{\N}$ is a sequence $s = (s_1, s_2, \dots)$ with each $s_m \in \Sigma$. Define $\Phi \colon \Sigma^{\N} \to \Sigma$ by
\[ \Phi(s)(k) = s_m(n) \qquad\text{where } \psi(k) = (m, n), \]
which takes values in $\set{0, 1}$, and $\Psi \colon \Sigma \to \Sigma^{\N}$ by $\Psi(\tau) = (\tau_1, \tau_2, \dots)$ with $\tau_m(n) = \tau(\psi^{-1}(m, n))$. For $s \in \Sigma^{\N}$ and $m, n \in \N$, writing $k = \psi^{-1}(m, n)$ so that $\psi(k) = (m, n)$,
\[ \Psi(\Phi(s))_m(n) = \Phi(s)(k) = s_m(n), \]
so $\Psi(\Phi(s)) = s$. For $\tau \in \Sigma$ and $k \in \N$ with $\psi(k) = (m, n)$,
\[ \Phi(\Psi(\tau))(k) = \tau_m(n) = \tau(\psi^{-1}(m, n)) = \tau(k), \]
so $\Phi(\Psi(\tau)) = \tau$. Hence $\Phi$ is a bijection.

(3) By the theorem on the cardinality of the continuum, $\R \sim \Sigma$. By (1), $\R^{\N} \sim \Sigma^{\N}$; by (2), $\Sigma^{\N} \sim \Sigma$; and $\Sigma \sim \R$. Equal cardinality is transitive, so $\R^{\N} \sim \R$.

For the last claim, $x \mapsto (x, 0)$ is an injection $\R \to \R \times \R$, and $(x, y) \mapsto (x, y, 0, 0, 0, \dots)$ is an injection $\R \times \R \to \R^{\N}$. Composing the latter with a bijection $\R^{\N} \to \R$ gives an injection $\R \times \R \to \R$. By the Schroeder–Bernstein theorem, $\R \times \R \sim \R$.
""", 4, 60, [
    r"Write $\R$ as $\Sigma$, the set of $0$-$1$ sequences, and ask what a sequence of $0$-$1$ sequences is: a $0$-$1$ array indexed by $\N \times \N$.",
    r"A bijection $\N \to \N \times \N$ turns an array indexed by $\N \times \N$ into a single sequence. Write down the map in both directions and check the composites.",
    r"For $\R \times \R$, sandwich it between $\R$ and $\R^{\N}$ with two injections and use Schroeder–Bernstein.",
], ["thm-continuum", "thm-nxn", "prop-composition", "prop-cardinality-equivalence", "thm-schroeder-bernstein", "def-card-le", "def-equal-cardinality", "def-set-operations"])

ex("ex-condensation-point", "An uncountable set has a condensation point", r"""
Let $S \subset \R$ be uncountable. Prove that there is a point $x \in S$ such that for every $\eps > 0$ the set $S \cap (x - \eps, x + \eps)$ is uncountable. Prove, moreover, that all but countably many points of $S$ have this property.
""", r"""
Let $T$ be the set of points $x \in S$ for which there is some $\eps > 0$ with $S \cap (x - \eps, x + \eps)$ countable. We show that $T$ is countable.

Let $J$ be the set of pairs $(p, q) \in \Q \times \Q$ with $p < q$ and $S \cap (p, q)$ countable. Since $\Q \times \Q$ is countable, so is its subset $J$. Let $x \in T$, with $\eps > 0$ such that $S \cap (x - \eps, x + \eps)$ is countable. By density of the rationals there are $p, q \in \Q$ with $x - \eps < p < x$ and $x < q < x + \eps$. Then $x \in (p, q)$ and $(p, q) \subset (x - \eps, x + \eps)$, so $S \cap (p, q)$ is a subset of a countable set, hence countable, and $(p, q) \in J$. Thus
\[ T \subset \bigcup_{(p, q) \in J} \big(S \cap (p, q)\big). \]
If $J = \varnothing$ this shows $T = \varnothing$. Otherwise the criteria for countability give a surjection $\varphi \colon \N \to J$; writing $\varphi(k) = (p_k, q_k)$ and $A_k = S \cap (p_k, q_k)$, the right-hand side is $\bigcup_{k \in \N} A_k$, a countable union of countable sets, hence countable. So $T$ is countable.

Since $S$ is uncountable and $T$ is countable, $S \setminus T$ is uncountable: otherwise $S = T \cup (S \setminus T)$ would be countable. In particular $S \setminus T \ne \varnothing$. Any $x \in S \setminus T$ is a point of $S$ for which no $\eps > 0$ makes $S \cap (x - \eps, x + \eps)$ countable: for every $\eps > 0$, $S \cap (x - \eps, x + \eps)$ is uncountable. All points of $S$ except those of the countable set $T$ have this property.
""", 3, 45, [
    r"Argue about the \emph{bad} points: those $x \in S$ with $S \cap (x - \eps, x + \eps)$ countable for some $\eps$. Show there are only countably many of them.",
    r"Each bad point lies in an interval $(p, q)$ with rational endpoints on which $S$ is countable. There are only countably many rational intervals.",
    r"The bad points are covered by countably many countable sets. The rest of $S$ is uncountable, hence nonempty.",
], ["thm-density-rationals", "cor-product-countable", "cor-q-denumerable", "cor-subset-image-countable", "thm-countable-union", "prop-countable-criteria", "def-interval", "def-countable"])

ex("ex-uncountable-sum", "Uncountably many positive numbers cannot have a finite sum", r"""
Let $S \subset (0, \infty)$ be uncountable. Prove that for every $M \in \R$ there is a finite subset $F \subset S$ whose elements add up to more than $M$.
""", r"""
For $n \in \N$ let $S_n = \set{s \in S : s \ge 1/n}$. Every $s \in S$ is positive, so by the Archimedean property there is an $n \in \N$ with $1/n < s$, and then $s \in S_n$. Hence $S = \bigcup_{n \in \N} S_n$. If every $S_n$ were countable, $S$ would be a countable union of countable sets, hence countable; so some $S_n$ is uncountable, in particular infinite. An infinite set contains a denumerable subset, so there is an injection $\N \to S_n$, $k \mapsto s_k$; the $s_k$ are distinct elements of $S$, each at least $1/n$.

Let $M \in \R$. By the Archimedean property there is an $N \in \N$ with $N > nM$. Let $F = \set{s_1, \dots, s_N}$, a finite subset of $S$ with $N$ distinct elements. Then
\[ \sum_{k=1}^{N} s_k \ge N \cdot \frac{1}{n} > M. \]
""", 3, 25, [
    r"Sort the elements of $S$ by size: $S_n = \set{s \in S : s \ge 1/n}$. Could every $S_n$ be countable?",
    r"Some $S_n$ is uncountable, hence infinite. Add up enough of its elements.",
], ["thm-archimedean", "thm-countable-union", "prop-infinite-contains-denumerable", "def-countable", "rem-finite-facts"])

# ---------------------------------------------------------------- the skeleton of calculus
ex("ex-composition-and-reciprocal", "Composites and reciprocals of continuous functions", r"""
\begin{enumerate}
\item Let $D, E \subset \R$, let $f \colon D \to \R$ be continuous at $c \in D$ with $f(D) \subset E$, and let $g \colon E \to \R$ be continuous at $f(c)$. Prove that $g \circ f \colon D \to \R$ is continuous at $c$.
\item Let $f \colon D \to \R$ be continuous at $c \in D$, with $f(x) \ne 0$ for every $x \in D$. Prove that $1/f \colon D \to \R$ is continuous at $c$.
\item Let $p$ and $q$ be polynomials and $D = \set{x \in \R : q(x) \ne 0}$. Deduce that the rational function $p/q \colon D \to \R$ is continuous.
\end{enumerate}
""", r"""
(1) Let $\eps > 0$. By continuity of $g$ at $f(c)$ there is an $\eta > 0$ such that $y \in E$ and $\abs{y - f(c)} < \eta$ imply $\abs{g(y) - g(f(c))} < \eps$. By continuity of $f$ at $c$, applied with $\eta$ in place of $\eps$, there is a $\delta > 0$ such that $x \in D$ and $\abs{x - c} < \delta$ imply $\abs{f(x) - f(c)} < \eta$. For such $x$, the point $y = f(x)$ lies in $E$ and satisfies $\abs{y - f(c)} < \eta$, so $\abs{g(f(x)) - g(f(c))} < \eps$.

(2) Let $\eps > 0$. Since $\abs{f(c)}/2 > 0$, there is a $\delta_1 > 0$ such that $x \in D$ and $\abs{x - c} < \delta_1$ imply $\abs{f(x) - f(c)} < \abs{f(c)}/2$, and then, by the inequality $\abs{f(c)} - \abs{f(x)} \le \abs{f(c) - f(x)}$,
\[ \abs{f(x)} \ge \abs{f(c)} - \abs{f(x) - f(c)} > \frac{\abs{f(c)}}{2}. \]
There is also a $\delta_2 > 0$ such that $x \in D$ and $\abs{x - c} < \delta_2$ imply $\abs{f(x) - f(c)} < \eps\abs{f(c)}^2/2$. Let $\delta = \min(\delta_1, \delta_2)$. For $x \in D$ with $\abs{x - c} < \delta$,
\[ \abs{\frac{1}{f(x)} - \frac{1}{f(c)}} = \frac{\abs{f(c) - f(x)}}{\abs{f(x)}\,\abs{f(c)}} < \frac{\eps\abs{f(c)}^2}{2} \cdot \frac{2}{\abs{f(c)}} \cdot \frac{1}{\abs{f(c)}} = \eps. \]

(3) Polynomials are continuous on $\R$, so their restrictions to $D$ are continuous on $D$, and $q(x) \ne 0$ for every $x \in D$. By (2), $1/q$ is continuous at every point of $D$, and then $p/q = p \cdot (1/q)$ is continuous at every point of $D$ as a product of continuous functions.
""", 2, 25, [
    r"For (1), feed the $\delta$ of $g$ (call it $\eta$) into the definition of continuity of $f$ as its $\eps$.",
    r"For (2), $\dfrac{1}{f(x)} - \dfrac{1}{f(c)} = \dfrac{f(c) - f(x)}{f(x)f(c)}$; first make $\abs{f(x)} > \abs{f(c)}/2$ near $c$, as in the quotient limit law for sequences.",
], ["def-continuity", "prop-triangle-inequality", "prop-continuity-algebra", "cor-polynomials", "prop-limit-quotient"])

ex("ex-rational-valued-constant", "Continuous functions with only rational values, or no zeros", r"""
\begin{enumerate}
\item Let $I$ be an interval (of any of the kinds defined in this chapter) and let $f \colon I \to \R$ be continuous with $f(x) \in \Q$ for every $x \in I$. Prove that $f$ is constant.
\item Let $f \colon [a, b] \to \R$ be continuous with $f(x) \ne 0$ for every $x \in [a, b]$. Prove that either $f(x) > 0$ for all $x \in [a, b]$ or $f(x) < 0$ for all $x \in [a, b]$.
\end{enumerate}
""", r"""
Both parts use that an interval $I$ contains every point between two of its points. Each kind of interval defined in this chapter is the set of real numbers $t$ satisfying at most two conditions: a lower one, of the form $a < t$ or $a \le t$ (none for an interval unbounded below), and an upper one, of the form $t < b$ or $t \le b$ (none for an interval unbounded above). Let $x, y \in I$ with $x < t < y$. If $I$ has a lower condition, then $x$ satisfies it, and $a < x < t$ or $a \le x < t$ gives $a < t$, so $t$ satisfies it as well; if $I$ has an upper condition, then $y$ satisfies it, and $t < y < b$ or $t < y \le b$ gives $t < b$. Hence $t \in I$. It follows that $[x, y] \subset I$ whenever $x < y$ lie in $I$, and the restriction of $f$ to $[x, y]$ is continuous.

(1) Suppose $f$ is not constant: there are $x, y \in I$ with $f(x) \ne f(y)$, and by exchanging names we may assume $x < y$. By the corollary on density of the irrationals there is an irrational number $\gamma$ strictly between $f(x)$ and $f(y)$. The intermediate value theorem, applied to the restriction of $f$ to $[x, y]$, gives a $c \in (x, y)$ with $f(c) = \gamma \notin \Q$, contradicting the hypothesis. So $f$ is constant.

(2) Suppose there are $x, y \in [a, b]$ with $f(x) > 0$ and $f(y) < 0$; then $x \ne y$, and $0$ lies strictly between $f(x)$ and $f(y)$. Applying the intermediate value theorem to the restriction of $f$ to the closed interval with endpoints $x$ and $y$ gives a point $c$ with $f(c) = 0$, contrary to hypothesis. So the values of $f$ are either all positive or all negative (none is zero).
""", 2, 15, [
    r"If $f$ took two different values, the intermediate value theorem would force it to take every value in between. What kind of value lies in between?",
    r"Between any two distinct real numbers there is an irrational number.",
], ["thm-ivt", "cor-density-irrationals", "def-interval", "def-continuity"])

ex("ex-odd-degree-root", "A polynomial of odd degree has a real root", r"""
Let $p(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_0$ with real coefficients, $a_n \ne 0$, and $n$ odd. Prove that $p(c) = 0$ for some $c \in \R$.
""", r"""
Dividing all coefficients by $a_n$ does not change the roots, so we may assume $a_n = 1$ and write $p(x) = x^n + q(x)$ with $q(x) = a_{n-1} x^{n-1} + \dots + a_0$. Put $A = \abs{a_{n-1}} + \dots + \abs{a_0}$ and $K = \max(1, 2A)$, so $K \ge 1$ and $K \ge 2A$.

Let $x \in \R$ with $\abs{x} = K$. Since $\abs{x} \ge 1$, for $0 \le k \le n - 1$ we have $\abs{x}^{n-1} = \abs{x}^k \cdot \abs{x}^{n-1-k} \ge \abs{x}^k$, because $\abs{x}^{n-1-k}$ is a product of numbers $\ge 1$ (or is $1$). By the triangle inequality applied repeatedly and $\abs{uv} = \abs{u}\abs{v}$,
\[ \abs{q(x)} \le \sum_{k=0}^{n-1} \abs{a_k}\,\abs{x}^k \le A\,\abs{x}^{n-1} \le \frac{\abs{x}}{2}\,\abs{x}^{n-1} = \frac{K^n}{2}, \]
using $A \le K/2 = \abs{x}/2$.

Since $n$ is odd, $(-K)^n = -K^n$, and $K^n > 0$. Therefore
\[ p(K) = K^n + q(K) \ge K^n - \abs{q(K)} \ge \frac{K^n}{2} > 0, \qquad p(-K) = -K^n + q(-K) \le -K^n + \abs{q(-K)} \le -\frac{K^n}{2} < 0. \]
The polynomial $p$ is continuous on $[-K, K]$, and $p(-K) < 0 < p(K)$, so by the intermediate value theorem there is a $c \in (-K, K)$ with $p(c) = 0$.
""", 3, 35, [
    r"Show that $p$ takes a positive value and a negative value, then use the intermediate value theorem. For large $\abs{x}$ the leading term dominates the rest.",
    r"Normalise $a_n = 1$. For $\abs{x} \ge 1$ every lower power $\abs{x}^k$ is at most $\abs{x}^{n-1}$, so the lower terms are at most $A\abs{x}^{n-1}$ with $A$ the sum of their absolute coefficients. Choose $\abs{x} \ge 2A$ to make this at most $\abs{x}^n/2$.",
], ["thm-ivt", "cor-polynomials", "prop-triangle-inequality"])

ex("ex-injective-is-monotone", "A continuous injection on an interval is strictly monotone", r"""
Let $a < b$ and let $f \colon [a, b] \to \R$ be continuous and injective. Prove that $f$ is \emph{strictly monotone}: either $f(x) < f(y)$ whenever $a \le x < y \le b$, or $f(x) > f(y)$ whenever $a \le x < y \le b$. Deduce that $f([a, b])$ is the closed interval with endpoints $f(a)$ and $f(b)$.
""", r"""
\emph{A lemma.} Let $a \le a' < b' \le b$ with $f(a') < f(b')$, and let $x \in (a', b')$. We claim $f(a') < f(x) < f(b')$. By injectivity $f(x) \ne f(a')$ and $f(x) \ne f(b')$. Suppose $f(x) < f(a')$. Then $f(x) < f(a') < f(b')$, and the restriction of $f$ to $[x, b']$ is continuous, so by the intermediate value theorem there is a $c \in (x, b')$ with $f(c) = f(a')$; but $c > x > a'$, so $c \ne a'$, contradicting injectivity. Suppose instead $f(x) > f(b')$. Then $f(a') < f(b') < f(x)$, and the intermediate value theorem on $[a', x]$ gives a $c \in (a', x)$ with $f(c) = f(b')$, where $c < x < b'$, again contradicting injectivity. This proves the lemma.

\emph{Case $f(a) < f(b)$.} (The two values differ by injectivity.) Let $a \le x < y \le b$; we show $f(x) < f(y)$. If $x = a$ and $y = b$ this is the hypothesis. If $x = a$ and $y < b$, the lemma with $(a', b') = (a, b)$ gives $f(a) < f(y)$. If $x > a$, the lemma with $(a', b') = (a, b)$ gives $f(x) < f(b)$; if $y = b$ we are done, and otherwise $x < y < b$ and the lemma with $(a', b') = (x, b)$, which applies because $f(x) < f(b)$, gives $f(x) < f(y)$. So $f$ is strictly increasing.

\emph{Case $f(a) > f(b)$.} The function $-f$ is continuous (a constant multiple of $f$) and injective, with $(-f)(a) < (-f)(b)$. By the first case $-f$ is strictly increasing, so $f(x) > f(y)$ whenever $x < y$: $f$ is strictly decreasing.

\emph{The range.} If $f$ is strictly increasing then $f(a) \le f(x) \le f(b)$ for every $x \in [a, b]$, so the minimum value of $f$ is $f(a)$ and the maximum is $f(b)$, and by the corollary on the range of a continuous function on a closed interval, $f([a, b]) = [f(a), f(b)]$. If $f$ is strictly decreasing, the same argument gives $f([a, b]) = [f(b), f(a)]$.
""", 3, 40, [
    r"Suppose $f(a) < f(b)$. If some $x$ between $a$ and $b$ had $f(x) < f(a)$ or $f(x) > f(b)$, the intermediate value theorem would produce a repeated value.",
    r"Prove first: whenever $a' < b'$ with $f(a') < f(b')$, every $x \in (a', b')$ has $f(a') < f(x) < f(b')$. Then apply it twice to compare $f(x)$ and $f(y)$ for $x < y$.",
    r"Handle $f(a) > f(b)$ by replacing $f$ with $-f$. For the range, use the corollary on the range of a continuous function on a closed interval.",
], ["thm-ivt", "cor-range-interval", "prop-continuity-algebra", "def-continuity", "def-injection"])

s.write()
