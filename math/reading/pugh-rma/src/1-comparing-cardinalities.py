from __future__ import annotations
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from c1_common import Section

s = Section("1-comparing-cardinalities")

s.prose("comp-intro", r"""
To show that two sets have equal cardinality one must produce a bijection, and explicit bijections can be awkward: try writing one down between $[0, 1]$ and $(0, 1)$. Injections are far easier to find. The Schroeder–Bernstein theorem says that injections in both directions are enough. With it, cardinalities can be compared like numbers, and the cardinality of $\R$ can be pinned down exactly.
""")

s.definition("def-card-le", "Comparing cardinalities", r"""
For sets $A$ and $B$ we write $A \preceq B$, and say that $A$ has \emph{cardinality less than or equal to} that of $B$, if there is an injection $A \to B$. We write $A \prec B$ if $A \preceq B$ and there is no bijection $A \to B$.
""")

s.result("prop-card-le-basic", "proposition", "First properties of the comparison", r"""
For all sets $A$, $B$, $C$:
\begin{enumerate}
\item if $A \subset B$ then $A \preceq B$; in particular $A \preceq A$;
\item if $A \sim B$ then $A \preceq B$ and $B \preceq A$;
\item if $A \preceq B$ and $B \preceq C$ then $A \preceq C$.
\end{enumerate}
""", r"""
(1) The inclusion map $A \to B$, $a \mapsto a$, is an injection.

(2) A bijection $f \colon A \to B$ is an injection $A \to B$, and its inverse is a bijection, hence an injection, $B \to A$.

(3) If $f \colon A \to B$ and $g \colon B \to C$ are injections, then $g \circ f \colon A \to C$ is an injection, since a composite of injections is an injection.
""", 1, 5, [
    r"Name the injection in each case: an inclusion, a bijection or its inverse, a composite.",
], ["def-card-le", "prop-composition"])

s.result("thm-schroeder-bernstein", "theorem", "Schroeder–Bernstein theorem", r"""
If there are injections $f \colon A \to B$ and $g \colon B \to A$, then there is a bijection $A \to B$. In symbols: if $A \preceq B$ and $B \preceq A$, then $A \sim B$.
""", r"""
Define subsets $C_0, C_1, C_2, \dots$ of $A$ by
\[ C_0 = A \setminus g(B), \qquad C_{n+1} = g(f(C_n)) \quad (n \ge 0), \]
and let $C = \bigcup_{n \ge 0} C_n$. If $a \in A \setminus C$ then $a \notin C_0$, so $a \in g(B)$; since $g$ is injective there is exactly one $b \in B$ with $g(b) = a$, which we denote $g^{-1}(a)$. Define
\[ h \colon A \to B, \qquad h(a) = \begin{cases} f(a) & \text{if } a \in C, \\ g^{-1}(a) & \text{if } a \in A \setminus C. \end{cases} \]

\emph{$h$ is injective.} Let $a, a' \in A$ with $h(a) = h(a')$. If both are in $C$, then $f(a) = f(a')$ and $a = a'$ because $f$ is injective. If both are outside $C$, then $g^{-1}(a) = g^{-1}(a')$, and applying $g$ gives $a = a'$. The remaining case, $a \in C$ and $a' \notin C$ (or the reverse), cannot occur: we would have $f(a) = g^{-1}(a')$, so $a' = g(f(a))$; but $a \in C_n$ for some $n$, so $a' \in g(f(C_n)) = C_{n+1} \subset C$, contrary to $a' \notin C$.

\emph{$h$ is surjective.} Let $b \in B$ and consider $g(b) \in A$. If $g(b) \notin C$, then $h(g(b)) = g^{-1}(g(b)) = b$. If $g(b) \in C$, then $g(b) \in C_n$ for some $n$, and $n \ne 0$ because $C_0$ contains no point of $g(B)$. So $g(b) \in C_n = g(f(C_{n-1}))$, that is, $g(b) = g(f(a))$ for some $a \in C_{n-1}$. Since $g$ is injective, $b = f(a)$, and since $a \in C$, $h(a) = f(a) = b$.

Thus $h$ is a bijection from $A$ to $B$.
""", 4, 75, [
    r"The bijection will use $f$ on part of $A$ and the inverse of $g$ on the rest. The inverse of $g$ is only available on $g(B)$, so the points of $A \setminus g(B)$ must be sent by $f$.",
    r"Once $C_0 = A \setminus g(B)$ is sent by $f$, the points $g(f(C_0))$ can no longer be sent by $g^{-1}$ without a collision, so they must go by $f$ too; and so on. Let $C_{n+1} = g(f(C_n))$ and $C = \bigcup_n C_n$.",
    r"Define $h = f$ on $C$ and $h = g^{-1}$ on $A \setminus C$. For injectivity the mixed case leads to $a' = g(f(a)) \in C$. For surjectivity, split according to whether $g(b) \in C$.",
], ["def-card-le", "def-injection"])

s.remark("rem-ancestors", r"""
There is a picture behind the set $C$. Call $b$ the \emph{parent} of $g(b)$ and $a$ the parent of $f(a)$, and trace the ancestry of a point of $A$ backwards as far as it goes. The set $C$ consists of the points of $A$ whose ancestry stops, after finitely many steps, at a point of $A$ with no parent. Those points are matched by $f$; all the others (ancestry stopping in $B$, or never stopping) are matched by $g^{-1}$.
""")

s.result("cor-sandwich", "corollary", "Sandwich principle", r"""
If $A \subset B \subset C$ and $A \sim C$, then $B \sim C$ (and hence also $A \sim B$).
""", r"""
The inclusion $B \to C$ is an injection. Let $\varphi \colon C \to A$ be a bijection. Since $A \subset B$, we may regard $\varphi$ as a map $C \to B$, and it is still an injection. By the Schroeder–Bernstein theorem, $B \sim C$. Since $A \sim C$ and $C \sim B$, also $A \sim B$.
""", 2, 10, [
    r"Find injections $B \to C$ and $C \to B$ and apply the Schroeder–Bernstein theorem.",
], ["thm-schroeder-bernstein", "prop-cardinality-equivalence"])

s.result("ex-open-interval-r", "exercise", "An open interval has the cardinality of the line", r"""
Let $a < b$ be real numbers. Prove that $(a, b) \sim \R$ by exhibiting bijections $(a, b) \to (-1, 1)$ and $(-1, 1) \to \R$.
""", r"""
\emph{$(a, b) \sim (-1, 1)$.} Let $\alpha(x) = \dfrac{2(x - a)}{b - a} - 1$. If $a < x < b$ then $0 < \dfrac{x - a}{b - a} < 1$, so $-1 < \alpha(x) < 1$. The map $\beta(u) = a + \dfrac{(u + 1)(b - a)}{2}$ sends $(-1, 1)$ into $(a, b)$, because $0 < (u + 1)/2 < 1$ for $-1 < u < 1$, and a direct substitution gives $\beta(\alpha(x)) = x$ and $\alpha(\beta(u)) = u$. So $\alpha \colon (a, b) \to (-1, 1)$ has an inverse and is a bijection.

\emph{$(-1, 1) \sim \R$.} Define
\[ g \colon (-1, 1) \to \R, \quad g(x) = \frac{x}{1 - \abs{x}}, \qquad\qquad h \colon \R \to (-1, 1), \quad h(y) = \frac{y}{1 + \abs{y}}. \]
$g$ is defined because $1 - \abs{x} > 0$ for $\abs{x} < 1$, and $h$ takes values in $(-1, 1)$ because $\abs{h(y)} = \dfrac{\abs{y}}{1 + \abs{y}} < 1$.

For $x \in (-1, 1)$: $\abs{g(x)} = \dfrac{\abs{x}}{1 - \abs{x}}$, so $1 + \abs{g(x)} = \dfrac{1}{1 - \abs{x}}$ and
\[ h(g(x)) = \frac{x}{1 - \abs{x}} \cdot (1 - \abs{x}) = x. \]
For $y \in \R$: $\abs{h(y)} = \dfrac{\abs{y}}{1 + \abs{y}}$, so $1 - \abs{h(y)} = \dfrac{1}{1 + \abs{y}}$ and
\[ g(h(y)) = \frac{y}{1 + \abs{y}} \cdot (1 + \abs{y}) = y. \]
So $h$ is an inverse of $g$, and $g$ is a bijection.

The composite $g \circ \alpha \colon (a, b) \to \R$ is a bijection.
""", 2, 25, [
    r"An affine map $x \mapsto cx + d$ carries any open interval onto $(-1, 1)$. Then you need a bijection from $(-1, 1)$ onto $\R$ that can be written with the field operations and the absolute value.",
    r"Try $g(x) = x/(1 - \abs{x})$, and prove it is a bijection by checking that $y \mapsto y/(1 + \abs{y})$ is its inverse.",
], ["prop-composition", "def-equal-cardinality", "def-abs", "def-interval"])

s.result("cor-intervals", "corollary", "All intervals have the cardinality of the line", r"""
Let $a < b$. Each of the intervals $(a, b)$, $[a, b)$, $(a, b]$, $[a, b]$ has the same cardinality as $\R$.
""", r"""
We know $(a, b) \sim \R$. Let $J$ be any of $[a, b)$, $(a, b]$, $[a, b]$. Then $(a, b) \subset J \subset \R$, and the sandwich principle (with $A = (a, b)$, $B = J$, $C = \R$) gives $J \sim \R$.
""", 1, 10, [
    r"Each of these intervals lies between $(a, b)$ and $\R$. Use the sandwich principle.",
], ["cor-sandwich", "ex-open-interval-r"])

s.result("prop-surjection-injection", "proposition", "Surjections reverse to injections", r"""
Let $A$ and $B$ be sets with $B \ne \varnothing$. There is a surjection $A \to B$ if and only if there is an injection $B \to A$. Consequently, if there are surjections $A \to B$ and $B \to A$, then $A \sim B$.
""", r"""
Suppose $f \colon A \to B$ is a surjection. For each $b \in B$ the set $f^{-1}(\set{b})$ is nonempty; choose an element $g(b)$ in it (this uses the axiom of choice). Then $f(g(b)) = b$ for all $b \in B$, so $g(b) = g(b')$ implies $b = f(g(b)) = f(g(b')) = b'$. Thus $g \colon B \to A$ is an injection.

Suppose $g \colon B \to A$ is an injection, and fix $b_0 \in B$. Define $f \colon A \to B$ as follows: if $a \in g(B)$, let $f(a)$ be the unique $b \in B$ with $g(b) = a$; if $a \notin g(B)$, let $f(a) = b_0$. Then $f(g(b)) = b$ for every $b \in B$, so $f$ is a surjection.

For the consequence, suppose there are surjections $A \to B$ and $B \to A$. Since $B \ne \varnothing$ and some map from $A$ is onto $B$, also $A \ne \varnothing$. The first paragraph, applied to the surjection $A \to B$, gives an injection $B \to A$; applied to the surjection $B \to A$ (with the roles of the two sets exchanged), it gives an injection $A \to B$. The Schroeder–Bernstein theorem gives $A \sim B$.
""", 2, 20, [
    r"From a surjection $f$, choose one point in each set $f^{-1}(\set{b})$. From an injection $g$, undo $g$ on its range and send everything else to a fixed point.",
], ["thm-schroeder-bernstein", "def-injection"])

s.definition("def-power-set", "Power set", r"""
The \emph{power set} of a set $S$ is the class $\mathcal{P}(S)$ of all subsets of $S$, including $\varnothing$ and $S$ itself.
""")

s.result("thm-cantor", "theorem", "Cantor's theorem", r"""
For every set $S$ there is no surjection $S \to \mathcal{P}(S)$. Consequently $S \prec \mathcal{P}(S)$.
""", r"""
Let $f \colon S \to \mathcal{P}(S)$ be any function, and let
\[ T = \set{s \in S : s \notin f(s)}. \]
Then $T \in \mathcal{P}(S)$. Suppose $T = f(t)$ for some $t \in S$. If $t \in T$, then by the definition of $T$, $t \notin f(t) = T$, a contradiction. If $t \notin T$, then $t \notin f(t)$, so $t$ satisfies the condition defining $T$ and $t \in T$, again a contradiction. Hence $T$ is not in the range of $f$, and $f$ is not a surjection.

The map $s \mapsto \set{s}$ is an injection $S \to \mathcal{P}(S)$, so $S \preceq \mathcal{P}(S)$. A bijection $S \to \mathcal{P}(S)$ would be a surjection, and there is none; hence $S \prec \mathcal{P}(S)$.
""", 3, 30, [
    r"This is the diagonal argument in general form. Given $f \colon S \to \mathcal{P}(S)$, build a subset of $S$ that differs from each $f(s)$ in how it treats the point $s$ itself.",
    r"Let $T = \set{s \in S : s \notin f(s)}$ and ask whether $t \in T$ when $f(t) = T$.",
], ["def-power-set", "def-card-le"])

s.remark("rem-no-largest", r"""
So there is no largest cardinality: $\N \prec \mathcal{P}(\N) \prec \mathcal{P}(\mathcal{P}(\N)) \prec \cdots$. The remaining results of this section locate $\R$ in this hierarchy: it sits exactly at $\mathcal{P}(\N)$.
""")

s.result("ex-power-set-sequences", "exercise", "Subsets are binary sequences", r"""
Let $\Sigma$ be the set of all sequences $\sigma \colon \N \to \set{0, 1}$. Prove that $\mathcal{P}(\N) \sim \Sigma$, and that $\mathcal{P}(\Q) \sim \mathcal{P}(\N)$.
""", r"""
\emph{$\mathcal{P}(\N) \sim \Sigma$.} For $T \subset \N$ define $\chi_T \in \Sigma$ by $\chi_T(n) = 1$ if $n \in T$ and $\chi_T(n) = 0$ if $n \notin T$. For $\sigma \in \Sigma$ define $Z(\sigma) = \set{n \in \N : \sigma(n) = 1}$. Then $Z(\chi_T) = \set{n : n \in T} = T$, and $\chi_{Z(\sigma)}(n) = 1$ exactly when $\sigma(n) = 1$, so $\chi_{Z(\sigma)} = \sigma$ because both sequences take only the values $0$ and $1$. Thus $T \mapsto \chi_T$ has the inverse $Z$ and is a bijection.

\emph{$\mathcal{P}(\Q) \sim \mathcal{P}(\N)$.} Since $\Q$ is denumerable there is a bijection $\varphi \colon \Q \to \N$. Define $\Phi \colon \mathcal{P}(\Q) \to \mathcal{P}(\N)$ by $\Phi(T) = \varphi(T)$ and $\Psi \colon \mathcal{P}(\N) \to \mathcal{P}(\Q)$ by $\Psi(U) = \varphi^{-1}(U)$. Because $\varphi$ is injective, $\varphi^{-1}(\varphi(T)) = T$; because $\varphi$ is surjective, $\varphi(\varphi^{-1}(U)) = U$. So $\Psi$ is an inverse of $\Phi$, and $\Phi$ is a bijection.
""", 2, 20, [
    r"A subset of $\N$ is described by answering, for each $n$, the question ``is $n$ in it?''.",
    r"For the second part, a bijection $\varphi \colon \Q \to \N$ carries subsets to subsets; check that $T \mapsto \varphi(T)$ and $U \mapsto \varphi^{-1}(U)$ are inverse to each other.",
], ["def-power-set", "cor-q-denumerable", "prop-composition"])

s.result("ex-r-into-power-set", "exercise", "The line injects into the power set of the rationals", r"""
Prove that $x \mapsto \set{r \in \Q : r < x}$ is an injection $\R \to \mathcal{P}(\Q)$. Conclude that $\R \preceq \mathcal{P}(\N)$.
""", r"""
Write $L(x) = \set{r \in \Q : r < x}$. Let $x \ne y$ be real numbers; by trichotomy we may assume $x < y$. By density of the rationals there is $r \in \Q$ with $x < r < y$. Then $r \in L(y)$ and $r \notin L(x)$, so $L(x) \ne L(y)$. Hence $L$ is an injection $\R \to \mathcal{P}(\Q)$.

Composing $L$ with a bijection $\mathcal{P}(\Q) \to \mathcal{P}(\N)$, which exists by the previous exercise, gives an injection $\R \to \mathcal{P}(\N)$.
""", 2, 15, [
    r"If $x < y$, you need a rational that belongs to one of the two sets and not the other. Which theorem supplies it?",
], ["thm-density-rationals", "ex-power-set-sequences", "def-card-le"])

s.result("ex-sequences-into-r", "exercise", "Binary sequences inject into the line", r"""
Let $\Sigma$ be the set of sequences $\sigma \colon \N \to \set{0, 1}$. For $\sigma \in \Sigma$ and $k \ge 0$ put
\[ s_k(\sigma) = \sum_{j=1}^{k} \frac{2\sigma(j)}{3^j} \quad (s_0(\sigma) = 0), \qquad \Phi(\sigma) = \lub \set{s_k(\sigma) : k \ge 0}. \]
Prove that $\Phi(\sigma)$ is a well-defined real number and that $\Phi \colon \Sigma \to \R$ is an injection. You may use the finite geometric sum $\sum_{j=n+1}^{k} \dfrac{2}{3^j} = \dfrac{1}{3^n} - \dfrac{1}{3^k}$ for $0 \le n \le k$.
""", r"""
\emph{Well defined.} Each term $2\sigma(j)/3^j$ is $\ge 0$ and $\le 2/3^j$. So $s_k(\sigma)$ is nondecreasing in $k$, and by the geometric sum with $n = 0$, $s_k(\sigma) \le 1 - 3^{-k} < 1$. The set $\set{s_k(\sigma) : k \ge 0}$ is nonempty and bounded above, so its least upper bound exists.

\emph{Injective.} Let $\sigma \ne \tau$ in $\Sigma$, and let $n$ be the least index with $\sigma(n) \ne \tau(n)$; exchanging names if necessary, $\sigma(n) = 0$ and $\tau(n) = 1$. Since $\sigma(j) = \tau(j)$ for $j < n$, the number $c = s_{n-1}(\sigma) = s_{n-1}(\tau)$ is common to both.

For $k \ge n$, using $\sigma(n) = 0$ and the geometric sum,
\[ s_k(\sigma) = c + \sum_{j=n+1}^{k} \frac{2\sigma(j)}{3^j} \le c + \frac{1}{3^n} - \frac{1}{3^k} \le c + \frac{1}{3^n}, \]
and for $k < n$, $s_k(\sigma) \le s_{n-1}(\sigma) = c$ because the partial sums are nondecreasing. So $c + 3^{-n}$ is an upper bound for $\set{s_k(\sigma)}$, and $\Phi(\sigma) \le c + 3^{-n}$.

On the other hand, using $\tau(n) = 1$,
\[ \Phi(\tau) \ge s_n(\tau) = c + \frac{2}{3^n} > c + \frac{1}{3^n} \ge \Phi(\sigma). \]
Hence $\Phi(\sigma) \ne \Phi(\tau)$.
""", 4, 45, [
    r"The digits $0$ and $2$ in base $3$ are used so that two different sequences cannot produce the same number (as $0.0111\dots = 0.1000\dots$ would in base $2$).",
    r"Look at the first index $n$ where $\sigma$ and $\tau$ differ, say $\sigma(n) = 0$, $\tau(n) = 1$. Bound $\Phi(\sigma)$ from above and $\Phi(\tau)$ from below in terms of the common partial sum $c = s_{n-1}$.",
    r"Everything after place $n$ contributes at most $\sum_{j > n} 2/3^j \le 3^{-n}$ to $\sigma$, while place $n$ alone contributes $2/3^n$ to $\tau$.",
], ["thm-lub", "def-upper-bound"])

s.result("thm-continuum", "theorem", "The cardinality of the continuum", r"""
$\R \sim \mathcal{P}(\N)$. Hence also $\R \sim \Sigma$, the set of sequences of $0$'s and $1$'s, and $\N \prec \R$.
""", r"""
By the exercise on the injection $x \mapsto \set{r \in \Q : r < x}$, $\R \preceq \mathcal{P}(\N)$. In the other direction, $\mathcal{P}(\N) \sim \Sigma$, and $\Sigma \preceq \R$ by the previous exercise; composing a bijection $\mathcal{P}(\N) \to \Sigma$ with an injection $\Sigma \to \R$ gives $\mathcal{P}(\N) \preceq \R$. By the Schroeder–Bernstein theorem, $\R \sim \mathcal{P}(\N)$. Since $\mathcal{P}(\N) \sim \Sigma$, also $\R \sim \Sigma$.

Finally, $\N \subset \R$ gives $\N \preceq \R$. If there were a bijection $\N \to \R$, composing it with a bijection $\R \to \mathcal{P}(\N)$ would give a bijection, in particular a surjection, $\N \to \mathcal{P}(\N)$, contradicting Cantor's theorem. So $\N \prec \R$.
""", 2, 20, [
    r"You have injections in both directions between $\R$ and $\mathcal{P}(\N)$ from the preceding exercises. Which theorem finishes?",
], ["thm-schroeder-bernstein", "ex-r-into-power-set", "ex-sequences-into-r", "ex-power-set-sequences", "thm-cantor", "prop-card-le-basic"])

s.remark("rem-continuum-hypothesis", r"""
This gives a second proof that $\R$ is uncountable, independent of the nested-interval argument. Whether some set $S$ satisfies $\N \prec S \prec \R$ is the subject of the \emph{continuum hypothesis}, which asserts that there is none; it can be neither proved nor refuted from the usual axioms of set theory. Nothing in analysis depends on it.
""")

s.card("card-le", r"What does $A \preceq B$ mean?",
       r"There is an injection $A \to B$. (For $B \ne \varnothing$, equivalently a surjection $B \to A$.)", "def-card-le")
s.card("schroeder-bernstein", r"State the Schroeder–Bernstein theorem.",
       r"If there are injections $f \colon A \to B$ and $g \colon B \to A$, then there is a bijection $A \to B$.", "thm-schroeder-bernstein")
s.card("sb-idea", r"How is the bijection in the Schroeder–Bernstein theorem built?",
       r"Let $C_0 = A \setminus g(B)$, $C_{n+1} = g(f(C_n))$, $C = \bigcup C_n$. Use $f$ on $C$ and $g^{-1}$ on $A \setminus C$.", "thm-schroeder-bernstein")
s.card("intervals", r"Why does $[a, b]$ have the same cardinality as $\R$?",
       r"$(a, b) \sim \R$ by an explicit bijection such as $x \mapsto x/(1 - \abs{x})$ on $(-1, 1)$, and $(a, b) \subset [a, b] \subset \R$; the sandwich principle (from Schroeder–Bernstein) does the rest.", "cor-intervals")
s.card("cantor", r"State Cantor's theorem and the set used in its proof.",
       r"There is no surjection $S \to \mathcal{P}(S)$. Given $f$, the set $T = \set{s \in S : s \notin f(s)}$ is not in its range.", "thm-cantor")
s.card("continuum", r"What is the cardinality of $\R$ in terms of $\N$?",
       r"$\R \sim \mathcal{P}(\N)$: $x \mapsto \set{r \in \Q : r < x}$ injects $\R$ into $\mathcal{P}(\Q) \sim \mathcal{P}(\N)$, binary sequences inject into $\R$ via $\sum 2\sigma(j)/3^j$, and Schroeder–Bernstein combines them.", "thm-continuum")

s.write()
