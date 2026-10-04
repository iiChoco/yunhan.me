from __future__ import annotations
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from c1_common import Section

s = Section("1-cardinality")

s.prose("card-intro", r"""
How many real numbers are there? More than there are rational numbers, in a precise sense discovered by Cantor: the rationals can be listed in a sequence and the reals cannot. To say this we need to compare the sizes of infinite sets, and the only sensible way to compare sizes without counting is to match elements one to one. This section develops that idea and sorts the sets of analysis into countable and uncountable.
""")

s.definition("def-injection", "Injection, surjection, bijection", r"""
Let $f \colon A \to B$ be a function.
\begin{itemize}
\item $f$ is an \emph{injection} (or \emph{one-to-one}) if $f(a) = f(a')$ implies $a = a'$, for all $a, a' \in A$.
\item $f$ is a \emph{surjection} (or \emph{onto}) if for every $b \in B$ there is at least one $a \in A$ with $f(a) = b$.
\item $f$ is a \emph{bijection} if it is both an injection and a surjection.
\end{itemize}
A function $g \colon B \to A$ is an \emph{inverse} of $f$ if $g \circ f = \id_A$ and $f \circ g = \id_B$.
""")

s.result("prop-composition", "proposition", "Composites and inverses", r"""
Let $f \colon A \to B$ and $g \colon B \to C$ be functions.
\begin{enumerate}
\item If $f$ and $g$ are injections, so is $g \circ f$. If $f$ and $g$ are surjections, so is $g \circ f$. Hence a composite of bijections is a bijection.
\item $f$ is a bijection if and only if it has an inverse. The inverse is then unique, is denoted $f^{-1}$, and is itself a bijection $B \to A$.
\end{enumerate}
""", r"""
(1) Suppose $f, g$ are injections and $g(f(a)) = g(f(a'))$. Injectivity of $g$ gives $f(a) = f(a')$, and injectivity of $f$ gives $a = a'$. Suppose $f, g$ are surjections and $c \in C$. There is $b \in B$ with $g(b) = c$, and then $a \in A$ with $f(a) = b$; so $g(f(a)) = c$.

(2) Suppose $f$ is a bijection. For each $b \in B$ there is an $a \in A$ with $f(a) = b$ (surjectivity), and only one (injectivity); define $h(b)$ to be this $a$. Then $f(h(b)) = b$ for all $b \in B$ by construction. For $a \in A$, $h(f(a))$ is the unique element that $f$ sends to $f(a)$, which is $a$. So $h$ is an inverse of $f$.

Conversely, suppose $h \colon B \to A$ is an inverse of $f$. If $f(a) = f(a')$ then $a = h(f(a)) = h(f(a')) = a'$, so $f$ is injective. If $b \in B$ then $f(h(b)) = b$, so $f$ is surjective.

Uniqueness: if $h$ and $h'$ are both inverses of $f$, then for every $b \in B$, $f(h(b)) = b = f(h'(b))$, and injectivity of $f$ gives $h(b) = h'(b)$. Finally, the equations $h \circ f = \id_A$ and $f \circ h = \id_B$ say that $f$ is an inverse of $h$, so $h$ is a bijection by what was just proved.
""", 2, 15, [
    r"Part (1) is two short definition chases.",
    r"For (2), when $f$ is a bijection define $h(b)$ as the unique $a$ with $f(a) = b$ and verify both composites. For the converse, apply $h$ to an equation $f(a) = f(a')$.",
], ["def-injection", "def-function"])

s.definition("def-equal-cardinality", "Equal cardinality", r"""
Sets $A$ and $B$ have \emph{equal cardinality}, written $A \sim B$, if there is a bijection from $A$ to $B$.
""")

s.result("prop-cardinality-equivalence", "proposition", "Equal cardinality behaves like an equivalence relation", r"""
For all sets $A$, $B$, $C$: $A \sim A$; if $A \sim B$ then $B \sim A$; and if $A \sim B$ and $B \sim C$ then $A \sim C$.
""", r"""
The identity map $\id_A \colon A \to A$ is a bijection, so $A \sim A$. If $f \colon A \to B$ is a bijection, then its inverse $f^{-1} \colon B \to A$ is a bijection, so $B \sim A$. If $f \colon A \to B$ and $g \colon B \to C$ are bijections, then $g \circ f \colon A \to C$ is a bijection, so $A \sim C$.
""", 1, 5, [
    r"For each property name the bijection: an identity map, an inverse, a composite.",
], ["def-equal-cardinality", "prop-composition"])

s.definition("def-countable", "Finite, denumerable, countable, uncountable", r"""
A set $S$ is
\begin{itemize}
\item \emph{finite} if it is empty or $S \sim \set{1, \dots, n}$ for some $n \in \N$, and \emph{infinite} otherwise;
\item \emph{denumerable} if $S \sim \N$;
\item \emph{countable} if it is finite or denumerable;
\item \emph{uncountable} if it is not countable.
\end{itemize}
A bijection $\N \to S$ is a way of listing the elements of $S$ in a sequence $s_1, s_2, s_3, \dots$ in which each element appears exactly once.
""")

s.remark("rem-finite-facts", r"""
We take the elementary facts about finite sets for granted: a subset of a finite set is finite; a union of finitely many finite sets is finite; a nonempty finite set of real numbers has a largest and a smallest element; and $\N$ is infinite. Consequently a set that has an infinite subset is infinite, and a set $S$ for which there is an injection $\N \to S$ is infinite. Since a bijection carries finite sets to finite sets, a denumerable set is infinite.
""")

s.result("thm-interval-uncountable", "theorem", "No sequence exhausts an interval", r"""
Let $a < b$ be real numbers and let $(x_n)$ be any sequence of real numbers. Then there is a point $c \in [a, b]$ with $c \ne x_n$ for every $n \in \N$.
""", r"""
We construct closed intervals $I_n = [a_n, b_n]$, $n \ge 0$, with $a_n < b_n$, such that $I_0 = [a, b]$ and, for $n \ge 1$,
\[ a_{n-1} \le a_n < b_n \le b_{n-1} \qquad\text{and}\qquad x_n \notin I_n. \]
Put $a_0 = a$, $b_0 = b$. Suppose $I_{n-1}$ has been constructed, and let $d = (b_{n-1} - a_{n-1})/3 > 0$. The intervals $L = [a_{n-1}, a_{n-1} + d]$ and $R = [b_{n-1} - d, b_{n-1}]$ are disjoint, because $a_{n-1} + d < b_{n-1} - d$. So $x_n$ does not belong to both. If $x_n \notin L$ let $I_n = L$; otherwise let $I_n = R$. In either case the displayed conditions hold.

By induction, $a_m \le a_n$ and $b_n \le b_m$ whenever $m \le n$. Hence for any $m, n \ge 0$, with $k = \max(m, n)$,
\[ a_m \le a_k < b_k \le b_n. \]
So every $b_n$ is an upper bound for the nonempty set $A = \set{a_m : m \ge 0}$. By the least upper bound property $c = \lub A$ exists. For each $n \ge 0$ we have $a_n \le c$ because $c$ is an upper bound for $A$, and $c \le b_n$ because $b_n$ is an upper bound for $A$ and $c$ is the least one. Thus $c \in I_n$ for every $n \ge 0$. In particular $c \in I_0 = [a, b]$, and for each $n \ge 1$, $c \in I_n$ while $x_n \notin I_n$, so $c \ne x_n$.
""", 4, 50, [
    r"Build the point $c$ by dodging the terms of the sequence one at a time: at stage $n$, shrink to a closed subinterval that misses $x_n$.",
    r"Of the left third and the right third of a closed interval, at least one does not contain $x_n$, because they are disjoint. This gives nested intervals $[a_n, b_n]$ with $x_n \notin [a_n, b_n]$.",
    r"Let $c = \lub \set{a_n}$. Every $b_n$ is an upper bound for the $a_m$'s, so $a_n \le c \le b_n$ for all $n$.",
], ["thm-lub", "def-upper-bound", "def-interval"])

s.result("cor-r-uncountable", "corollary", "The real numbers are uncountable", r"""
$\R$ is uncountable. More generally, every interval $[a, b]$ with $a < b$ is uncountable.
""", r"""
Let $a < b$. The interval $[a, b]$ is infinite: $n \mapsto a + (b - a)/n$ is an injection of $\N$ into it. If $[a, b]$ were countable it would therefore be denumerable, and there would be a bijection $f \colon \N \to [a, b]$. Then $x_n = f(n)$ is a sequence of real numbers in which every point of $[a, b]$ occurs, contradicting the theorem that no sequence exhausts an interval. So $[a, b]$ is uncountable.

Similarly $\R$ is infinite since it contains $\N$. If $\R$ were countable there would be a bijection $f \colon \N \to \R$, and the sequence $x_n = f(n)$ would contain every real number, in particular every point of $[0, 1]$, contradicting the same theorem.
""", 1, 10, [
    r"A denumerable set is one whose elements can be written as a sequence. Quote the previous theorem.",
], ["thm-interval-uncountable", "def-countable", "rem-finite-facts"])

s.result("thm-diagonal", "theorem", "Cantor's diagonal argument", r"""
Let $\Sigma$ be the set of all sequences $\sigma = (\sigma(1), \sigma(2), \sigma(3), \dots)$ with each $\sigma(k) \in \set{0, 1}$. There is no surjection $\N \to \Sigma$, and $\Sigma$ is uncountable.
""", r"""
Let $f \colon \N \to \Sigma$ be any function, and write $f(n) = \sigma_n$. Define a sequence $\tau \in \Sigma$ by
\[ \tau(n) = 1 - \sigma_n(n) \qquad (n \in \N). \]
Each $\tau(n)$ is $0$ or $1$, so $\tau \in \Sigma$. For every $n$, the sequences $\tau$ and $\sigma_n$ differ in their $n$th term, so $\tau \ne \sigma_n = f(n)$. Hence $\tau$ is not in the range of $f$, and $f$ is not a surjection.

$\Sigma$ is infinite: for $k \in \N$ let $\delta_k$ be the sequence whose $k$th term is $1$ and whose other terms are $0$; then $k \mapsto \delta_k$ is an injection $\N \to \Sigma$. If $\Sigma$ were countable it would be denumerable, and a bijection $\N \to \Sigma$ would be a surjection, which we have shown does not exist. So $\Sigma$ is uncountable.
""", 3, 30, [
    r"Given any list $\sigma_1, \sigma_2, \dots$ of sequences, construct a single sequence that is not on the list.",
    r"Make the new sequence differ from $\sigma_n$ in the $n$th place: $\tau(n) = 1 - \sigma_n(n)$.",
], ["def-countable", "def-injection", "rem-finite-facts"])

s.remark("rem-decimals", r"""
The diagonal argument is usually applied directly to $\R$, using decimal expansions: given a list of reals in $[0, 1]$, write each as a decimal and build a number whose $n$th digit differs from the $n$th digit of the $n$th number. That proof needs the theory of decimal expansions (and care with expansions ending in repeated $9$'s), which we have not developed; the nested-interval proof above uses only the least upper bound property.
""")

s.prose("card-countable-intro", r"""
Now the other side: showing that sets are countable. The tools are a description of the infinite subsets of $\N$ and a criterion that replaces bijections by mere injections or surjections, which are much easier to produce.
""")

s.result("lem-infinite-subset-n", "lemma", "Infinite subsets of the natural numbers are denumerable", r"""
Every infinite subset $S$ of $\N$ is denumerable.
""", r"""
Define $s_1, s_2, \dots$ recursively: $s_1$ is the least element of $S$, and
\[ s_{k+1} \text{ is the least element of } S \setminus \set{s_1, \dots, s_k}. \]
These least elements exist by the least element principle, because $S \setminus \set{s_1, \dots, s_k}$ is nonempty: otherwise $S$ would be contained in a finite set and so be finite.

\emph{The sequence is strictly increasing.} Both $s_k$ and $s_{k+1}$ belong to $S \setminus \set{s_1, \dots, s_{k-1}}$, of which $s_k$ is the least element; so $s_{k+1} \ge s_k$, and $s_{k+1} \ne s_k$ by construction. Hence $s_{k+1} > s_k$. It follows that $k \mapsto s_k$ is an injection $\N \to S$, and by induction that $s_k \ge k$ for all $k$ ($s_1 \ge 1$, and $s_{k+1} > s_k \ge k$ gives $s_{k+1} \ge k + 1$).

\emph{The sequence exhausts $S$.} Let $s \in S$ and suppose $s \ne s_k$ for all $k$. Then in particular $s \in S \setminus \set{s_1, \dots, s_s}$, so its least element satisfies $s_{s+1} \le s$. But $s_{s+1} \ge s + 1$. This contradiction shows that $s = s_k$ for some $k$.

Thus $k \mapsto s_k$ is a bijection $\N \to S$.
""", 3, 30, [
    r"List the elements of $S$ in increasing order: the smallest, then the smallest of what is left, and so on. Then prove that this list is a bijection from $\N$.",
    r"Injectivity follows because the list is strictly increasing. For surjectivity, first show $s_k \ge k$; an element $s \in S$ that is never listed would satisfy $s_{s+1} \le s$.",
], ["def-countable", "rem-finite-facts"])

s.result("prop-countable-criteria", "proposition", "Criteria for countability", r"""
For a nonempty set $B$ the following are equivalent:
\begin{enumerate}
\item $B$ is countable;
\item there is a surjection $\N \to B$;
\item there is an injection $B \to \N$.
\end{enumerate}
""", r"""
$(1) \Rightarrow (2)$. If $B$ is denumerable, a bijection $\N \to B$ is a surjection. If $B$ is finite and nonempty, there is a bijection $h \colon \set{1, \dots, n} \to B$ for some $n \in \N$; define $f \colon \N \to B$ by $f(k) = h(k)$ for $k \le n$ and $f(k) = h(1)$ for $k > n$. Then $f$ is a surjection because $h$ is.

$(2) \Rightarrow (3)$. Let $f \colon \N \to B$ be a surjection. For $b \in B$ the set $f^{-1}(\set{b}) \subset \N$ is nonempty, so it has a least element; call it $g(b)$. Then $f(g(b)) = b$ for all $b$, so $g(b) = g(b')$ implies $b = f(g(b)) = f(g(b')) = b'$. Thus $g \colon B \to \N$ is an injection.

$(3) \Rightarrow (1)$. Let $g \colon B \to \N$ be an injection. Then $g$ is a bijection from $B$ onto its range $g(B) \subset \N$, so $B \sim g(B)$. If $B$ is finite it is countable. If $B$ is infinite, then $g(B)$ is infinite (a bijection carries finite sets to finite sets), so $g(B)$ is denumerable because infinite subsets of $\N$ are denumerable; hence $B \sim g(B) \sim \N$ and $B$ is denumerable.
""", 3, 30, [
    r"Prove $(1) \Rightarrow (2) \Rightarrow (3) \Rightarrow (1)$.",
    r"From a surjection $f \colon \N \to B$, get an injection the other way by sending $b$ to the \emph{least} $n$ with $f(n) = b$.",
    r"An injection $B \to \N$ identifies $B$ with a subset of $\N$, and subsets of $\N$ are finite or denumerable.",
], ["def-countable", "lem-infinite-subset-n", "prop-cardinality-equivalence", "def-injection"])

s.result("cor-subset-image-countable", "corollary", "Subsets and images of countable sets", r"""
\begin{enumerate}
\item Every subset of a countable set is countable.
\item If $A$ is countable and $f \colon A \to B$ is a surjection, then $B$ is countable.
\end{enumerate}
""", r"""
(1) Let $A \subset B$ with $B$ countable. If $A = \varnothing$ it is finite, hence countable. Otherwise $B \ne \varnothing$, so by the criteria for countability there is an injection $g \colon B \to \N$. Its restriction to $A$ is an injection $A \to \N$, so $A$ is countable by the same criteria.

(2) If $B = \varnothing$ it is countable. Otherwise $A \ne \varnothing$, since $f$ is a surjection onto a nonempty set. By the criteria there is a surjection $h \colon \N \to A$, and then $f \circ h \colon \N \to B$ is a surjection, so $B$ is countable.
""", 1, 10, [
    r"Use the criteria: restrict an injection into $\N$; compose surjections from $\N$. Treat the empty set separately.",
], ["prop-countable-criteria", "prop-composition"])

s.result("thm-nxn", "theorem", "The set of pairs of natural numbers is denumerable", r"""
$\N \times \N$ is denumerable.
""", r"""
Define $\varphi \colon \N \times \N \to \N$ by $\varphi(m, n) = 2^m(2n - 1)$.

\emph{$\varphi$ is an injection.} Suppose $2^m(2n - 1) = 2^{m'}(2n' - 1)$; exchanging the pairs if necessary, assume $m \le m'$. Dividing by $2^m$,
\[ 2n - 1 = 2^{m' - m}(2n' - 1). \]
The left side is odd. If $m' > m$ the right side is even, which is impossible; so $m' = m$. Then $2n - 1 = 2n' - 1$, so $n = n'$.

By the criteria for countability, $\N \times \N$ is countable. It is infinite, because $n \mapsto (n, 1)$ is an injection of $\N$ into it. A countable infinite set is denumerable.
""", 3, 25, [
    r"By the criteria for countability it is enough to find an injection $\N \times \N \to \N$ and to note that $\N \times \N$ is infinite.",
    r"Encode the pair $(m, n)$ as a power of $2$ times an odd number: $2^m(2n - 1)$. Use parity to show the encoding is injective.",
], ["prop-countable-criteria", "def-countable", "rem-finite-facts"])

s.remark("rem-diagonal-listing", r"""
The traditional picture of this theorem lists the pairs along the diagonals of an infinite array: $(1,1)$; $(1,2), (2,1)$; $(1,3), (2,2), (3,1)$; and so on. That listing is a bijection $\N \to \N \times \N$; the arithmetic injection above reaches the same conclusion with less bookkeeping.
""")

s.result("cor-product-countable", "corollary", "Products of countable sets", r"""
If $A$ and $B$ are countable, then $A \times B$ is countable. If $A$ and $B$ are denumerable, then $A \times B$ is denumerable.
""", r"""
If $A$ or $B$ is empty, then $A \times B$ is empty, hence countable. Otherwise, by the criteria for countability there are injections $g \colon A \to \N$ and $h \colon B \to \N$. The map $(a, b) \mapsto (g(a), h(b))$ is an injection $A \times B \to \N \times \N$: if $(g(a), h(b)) = (g(a'), h(b'))$ then $a = a'$ and $b = b'$. Composing with an injection $\N \times \N \to \N$, which exists because $\N \times \N$ is denumerable, gives an injection $A \times B \to \N$. So $A \times B$ is countable.

If $A$ and $B$ are denumerable, fix $b_0 \in B$ and a bijection $f \colon \N \to A$. Then $n \mapsto (f(n), b_0)$ is an injection $\N \to A \times B$, so $A \times B$ is infinite; being countable, it is denumerable.
""", 2, 15, [
    r"Combine injections $A \to \N$ and $B \to \N$ into an injection $A \times B \to \N \times \N$.",
], ["thm-nxn", "prop-countable-criteria", "prop-composition"])

s.result("thm-countable-union", "theorem", "A countable union of countable sets is countable", r"""
Let $A_1, A_2, A_3, \dots$ be a sequence of countable sets. Then $\bigcup_{n \in \N} A_n$ is countable. In particular the union of finitely many countable sets is countable.
""", r"""
Let $U = \bigcup_n A_n$. If $U = \varnothing$ it is countable. Otherwise let $I = \set{n \in \N : A_n \ne \varnothing}$, which is nonempty. For each $n \in I$ there is a surjection $\N \to A_n$ by the criteria for countability; choose one and call it $f_n$. Define
\[ F \colon I \times \N \to U, \qquad F(n, k) = f_n(k). \]
$F$ is a surjection: if $u \in U$ then $u \in A_n$ for some $n$, this $n$ is in $I$, and $u = f_n(k)$ for some $k$ because $f_n$ is onto $A_n$. The set $I \times \N$ is a subset of the countable set $\N \times \N$, so it is countable, and $U$ is the image of a countable set under a surjection. Hence $U$ is countable.

For finitely many countable sets $A_1, \dots, A_N$, put $A_n = \varnothing$ for $n > N$ and apply the result.
""", 3, 25, [
    r"Each nonempty $A_n$ is the range of a sequence $f_n \colon \N \to A_n$. Two indices, $n$ and the position in the $n$th sequence, describe every element of the union.",
    r"Define $F(n, k) = f_n(k)$ on a subset of $\N \times \N$ and use the fact that a surjective image of a countable set is countable. Take care of empty $A_n$.",
], ["prop-countable-criteria", "cor-subset-image-countable", "thm-nxn"])

s.remark("rem-choice", r"""
The proof chooses, for each of infinitely many sets $A_n$, one surjection $f_n$ among possibly many. Making infinitely many such choices at once is an instance of the \emph{axiom of choice}, which we use without further comment, here and in similar constructions.
""")

s.result("cor-q-denumerable", "corollary", "The integers and the rationals are denumerable", r"""
$\Z$ and $\Q$ are denumerable.
""", r"""
$\Z = \N \cup \set{0} \cup \set{-n : n \in \N}$ is a union of three countable sets (the third is in bijection with $\N$ by $n \mapsto -n$), so it is countable. It is infinite since it contains $\N$; hence it is denumerable.

$\Z \times \N$ is countable, being a product of countable sets. The map $\Z \times \N \to \Q$, $(p, q) \mapsto p/q$, is a surjection, because every rational number can be written with a positive denominator. A surjective image of a countable set is countable, so $\Q$ is countable. It is infinite since it contains $\N$; hence it is denumerable.
""", 2, 15, [
    r"Write $\Z$ as a union of three countable sets, and $\Q$ as the image of a countable set of pairs.",
    r"$(p, q) \mapsto p/q$ maps $\Z \times \N$ onto $\Q$.",
], ["thm-countable-union", "cor-product-countable", "cor-subset-image-countable"])

s.result("ex-qm-denumerable", "exercise", "Rational points of Euclidean space", r"""
Prove that for every $m \in \N$ the set $\Q^m$ of points of $\R^m$ with all coordinates rational is denumerable.
""", r"""
By induction on $m$. For $m = 1$, $\Q$ is denumerable. Suppose $\Q^m$ is denumerable. The map
\[ \Q^m \times \Q \to \Q^{m+1}, \qquad \big((x_1, \dots, x_m), x_{m+1}\big) \mapsto (x_1, \dots, x_m, x_{m+1}) \]
is a bijection: its inverse sends $(x_1, \dots, x_{m+1})$ to $\big((x_1, \dots, x_m), x_{m+1}\big)$. The product of the denumerable sets $\Q^m$ and $\Q$ is denumerable, so $\Q^{m+1} \sim \Q^m \times \Q \sim \N$.
""", 2, 15, [
    r"Induct on $m$, using that a product of two denumerable sets is denumerable.",
], ["cor-q-denumerable", "cor-product-countable", "prop-cardinality-equivalence"])

s.result("cor-irrationals-uncountable", "corollary", "The irrational numbers are uncountable", r"""
The set $\R \setminus \Q$ of irrational numbers is uncountable.
""", r"""
If $\R \setminus \Q$ were countable, then $\R = \Q \cup (\R \setminus \Q)$ would be a union of two countable sets, hence countable. But $\R$ is uncountable.
""", 1, 5, [
    r"If the irrationals were countable, what would follow for $\R = \Q \cup (\R \setminus \Q)$?",
], ["cor-r-uncountable", "cor-q-denumerable", "thm-countable-union"])

s.result("prop-infinite-contains-denumerable", "proposition", "Every infinite set contains a denumerable subset", r"""
If $S$ is an infinite set, then there is an injection $\N \to S$; equivalently, $S$ has a denumerable subset.
""", r"""
Choose $x_1, x_2, \dots$ in $S$ recursively. Since $S$ is infinite it is nonempty; choose $x_1 \in S$. If $x_1, \dots, x_n$ have been chosen, the set $S \setminus \set{x_1, \dots, x_n}$ is nonempty, for otherwise $S \subset \set{x_1, \dots, x_n}$ would be finite; choose $x_{n+1}$ in it. By construction $x_{n+1}$ differs from all earlier terms, so $x_m \ne x_n$ whenever $m \ne n$. Hence $n \mapsto x_n$ is an injection $\N \to S$, and it is a bijection from $\N$ onto its range $\set{x_n : n \in \N}$, which is therefore a denumerable subset of $S$. Conversely, if $D \subset S$ is denumerable, a bijection $\N \to D$ is an injection $\N \to S$.
""", 2, 15, [
    r"Pick elements one after another, each different from all those already picked. Why can you always continue?",
], ["def-countable", "rem-finite-facts"])

s.result("ex-hilbert-hotel", "exercise", "Removing a point from an infinite set", r"""
Let $S$ be an infinite set and $p \in S$. Prove that $S \sim S \setminus \set{p}$.
""", r"""
The set $S \setminus \set{p}$ is infinite, since otherwise $S = (S \setminus \set{p}) \cup \set{p}$ would be finite. So it contains distinct elements $x_1, x_2, x_3, \dots$ (every infinite set contains a denumerable subset). Put $x_0 = p$; then $x_0, x_1, x_2, \dots$ are distinct elements of $S$. Let $D = \set{x_n : n \ge 0}$ and define $f \colon S \to S \setminus \set{p}$ by
\[ f(x_n) = x_{n+1} \quad (n \ge 0), \qquad f(s) = s \quad (s \in S \setminus D). \]
The values lie in $S \setminus \set{p}$: $x_{n+1} \ne p$, and $s \notin D$ implies $s \ne x_0 = p$.

\emph{Injective.} Note that $f$ maps $D$ into $D$ and $S \setminus D$ into $S \setminus D$. So if $f(u) = f(v)$, then $u, v$ are both in $D$ or both outside it. If $u = x_n$ and $v = x_k$, then $x_{n+1} = x_{k+1}$ gives $n = k$, so $u = v$. If both are outside $D$, then $u = f(u) = f(v) = v$.

\emph{Surjective.} Let $t \in S \setminus \set{p}$. If $t \in D$ then $t = x_n$ with $n \ge 1$ (since $t \ne x_0$), and $t = f(x_{n-1})$. If $t \notin D$ then $t = f(t)$.
""", 3, 25, [
    r"Think of a hotel with rooms $1, 2, 3, \dots$, all occupied: one more guest can be accommodated by moving everyone up one room.",
    r"Choose distinct points $x_1, x_2, \dots$ in $S \setminus \set{p}$, set $x_0 = p$, shift $x_n \mapsto x_{n+1}$, and leave every other point fixed.",
], ["prop-infinite-contains-denumerable", "def-equal-cardinality"])

s.card("bijection", r"Define injection, surjection, bijection.",
       r"$f \colon A \to B$ is an injection if $f(a) = f(a')$ implies $a = a'$; a surjection if every $b \in B$ is $f(a)$ for some $a$; a bijection if both. Bijections are exactly the maps with an inverse.", "def-injection")
s.card("countable", r"Define: equal cardinality, denumerable, countable, uncountable.",
       r"$A \sim B$ if there is a bijection $A \to B$. Denumerable: $\sim \N$. Countable: finite or denumerable. Uncountable: not countable.", "def-countable")
s.card("r-uncountable-idea", r"Why can no sequence $(x_n)$ contain every point of $[a, b]$?",
       r"Build nested closed intervals $[a_n, b_n]$ with $x_n \notin [a_n, b_n]$ (take a left or right third). Then $c = \lub\set{a_n}$ lies in all of them, so $c \ne x_n$ for every $n$.", "thm-interval-uncountable")
s.card("diagonal", r"State the diagonal argument for sequences of $0$'s and $1$'s.",
       r"Given a list $\sigma_1, \sigma_2, \dots$, the sequence $\tau(n) = 1 - \sigma_n(n)$ differs from $\sigma_n$ in the $n$th place, so it is not on the list.", "thm-diagonal")
s.card("countable-criteria", r"Give two conditions on a nonempty set $B$ equivalent to countability.",
       r"There is a surjection $\N \to B$; there is an injection $B \to \N$.", "prop-countable-criteria")
s.card("nxn", r"Why is $\N \times \N$ denumerable?",
       r"$(m, n) \mapsto 2^m(2n - 1)$ is an injection into $\N$, and $\N \times \N$ is infinite. (Or list the pairs along diagonals.)", "thm-nxn")
s.card("countable-union", r"What can be said about a countable union of countable sets? Idea of proof?",
       r"It is countable. Choose surjections $f_n \colon \N \to A_n$; then $(n, k) \mapsto f_n(k)$ maps a subset of $\N \times \N$ onto the union.", "thm-countable-union")
s.card("q-vs-r", r"Which of $\Z$, $\Q$, $\Q^m$, $\R$, $\R \setminus \Q$, $[a, b]$ are countable?",
       r"$\Z$, $\Q$, $\Q^m$ are denumerable. $\R$, $\R \setminus \Q$, and $[a, b]$ (for $a < b$) are uncountable.", "cor-irrationals-uncountable")
s.card("hilbert", r"If $S$ is infinite and $p \in S$, how do $S$ and $S \setminus \set{p}$ compare?",
       r"They have equal cardinality: pick distinct $x_1, x_2, \dots$ in $S \setminus \set{p}$, set $x_0 = p$, and shift $x_n \mapsto x_{n+1}$, fixing everything else.", "ex-hilbert-hotel")

s.write()
