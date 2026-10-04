from __future__ import annotations
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from c1_common import Section

s = Section("1-preliminaries")

s.prose("prelim-intro", r"""
Analysis is written in the language of sets, functions, and quantifiers, and it is practised by proving things. This section fixes that language and the conventions of proof used in the rest of the book. Nothing here is deep; the provable items are warm-ups, meant to settle how much detail a proof should carry.
""")

s.definition("def-sets", "Sets and their notation", r"""
A \emph{set} is a collection of objects, its \emph{elements} or \emph{members}. We write $x \in S$ when $x$ is an element of $S$ and $x \notin S$ when it is not. The set with no elements is the \emph{empty set} $\varnothing$; the set whose only element is $x$ is the \emph{singleton} $\set{x}$. Three sets of numbers are taken as known, together with their arithmetic and order:
\[ \N = \set{1, 2, 3, \dots}, \qquad \Z = \set{0, 1, -1, 2, -2, \dots}, \qquad \Q = \set{a/b : a, b \in \Z,\ b \ne 0}. \]
A set $A$ is a \emph{subset} of $B$, written $A \subset B$, if every element of $A$ is an element of $B$. Two sets are \emph{equal} if they have the same elements, that is, $A = B$ exactly when $A \subset B$ and $B \subset A$. A \emph{class} is a collection of sets; the sets are the members of the class.
""")

s.definition("def-set-operations", "Operations on sets", r"""
Let $A$ and $B$ be sets.
\begin{itemize}
\item The \emph{union} $A \cup B$ consists of the elements that belong to $A$ or to $B$ (or to both).
\item The \emph{intersection} $A \cap B$ consists of the elements that belong to both $A$ and $B$.
\item The \emph{difference} $A \setminus B$ consists of the elements of $A$ that are not in $B$.
\item The \emph{symmetric difference} $A \,\Delta\, B$ consists of the elements that belong to exactly one of $A$ and $B$.
\item $A$ and $B$ are \emph{disjoint} if $A \cap B = \varnothing$.
\item The \emph{Cartesian product} $A \times B$ is the set of ordered pairs $(a, b)$ with $a \in A$ and $b \in B$.
\end{itemize}
For a class $\mathcal{C}$ of sets, $\bigcup \mathcal{C}$ is the set of elements belonging to at least one member of $\mathcal{C}$, and (when $\mathcal{C}$ is not empty) $\bigcap \mathcal{C}$ is the set of elements belonging to every member of $\mathcal{C}$.
""")

s.prose("prelim-set-equality", r"""
The standard way to prove that two sets are equal is to prove two inclusions: take an arbitrary element of the left side and show that it lies in the right side, then the reverse. The next two facts are practice in exactly that.
""")

s.result("ex-de-morgan", "exercise", "De Morgan's laws", r"""
Let $A$ and $B$ be subsets of a set $X$. Prove that
\[ X \setminus (A \cup B) = (X \setminus A) \cap (X \setminus B) \qquad\text{and}\qquad X \setminus (A \cap B) = (X \setminus A) \cup (X \setminus B). \]
""", r"""
\emph{First law.} Let $x \in X \setminus (A \cup B)$. Then $x \in X$ and $x \notin A \cup B$. If $x$ were in $A$ it would be in $A \cup B$, so $x \notin A$; likewise $x \notin B$. Hence $x \in X \setminus A$ and $x \in X \setminus B$, that is, $x \in (X \setminus A) \cap (X \setminus B)$. Conversely, let $x \in (X \setminus A) \cap (X \setminus B)$. Then $x \in X$, $x \notin A$, and $x \notin B$. An element of $A \cup B$ lies in $A$ or in $B$, and $x$ lies in neither, so $x \notin A \cup B$. Hence $x \in X \setminus (A \cup B)$.

\emph{Second law.} Let $x \in X \setminus (A \cap B)$. Then $x \in X$ and $x$ is not in both $A$ and $B$, so $x \notin A$ or $x \notin B$. In the first case $x \in X \setminus A$, in the second $x \in X \setminus B$; either way $x \in (X \setminus A) \cup (X \setminus B)$. Conversely, let $x \in (X \setminus A) \cup (X \setminus B)$. Then $x \in X$, and $x \notin A$ or $x \notin B$. In either case $x$ is not in both $A$ and $B$, so $x \notin A \cap B$, and $x \in X \setminus (A \cap B)$.
""", 1, 10, [
    r"Two sets are equal when each is a subset of the other. Take an arbitrary element of one side and chase it to the other.",
    r"Being outside $A \cup B$ means being outside $A$ \emph{and} outside $B$; being outside $A \cap B$ means being outside $A$ \emph{or} outside $B$.",
], ["def-sets", "def-set-operations"])

s.result("ex-symmetric-difference", "exercise", "Two formulas for the symmetric difference", r"""
For any sets $A$ and $B$, prove that
\[ A \,\Delta\, B = (A \setminus B) \cup (B \setminus A) = (A \cup B) \setminus (A \cap B). \]
""", r"""
An element $x$ belongs to exactly one of $A$, $B$ precisely when either ($x \in A$ and $x \notin B$) or ($x \in B$ and $x \notin A$). The first alternative says $x \in A \setminus B$ and the second says $x \in B \setminus A$, so $A \,\Delta\, B = (A \setminus B) \cup (B \setminus A)$.

For the second formula, let $x \in (A \setminus B) \cup (B \setminus A)$. If $x \in A \setminus B$ then $x \in A \subset A \cup B$, and $x \notin B$ gives $x \notin A \cap B$. If $x \in B \setminus A$ the same holds with the roles exchanged. In both cases $x \in (A \cup B) \setminus (A \cap B)$. Conversely, let $x \in (A \cup B) \setminus (A \cap B)$. Then $x \in A$ or $x \in B$, and $x$ is not in both. If $x \in A$, then $x \notin B$ (otherwise $x \in A \cap B$), so $x \in A \setminus B$. If $x \notin A$, then $x \in B$, so $x \in B \setminus A$. Hence $x \in (A \setminus B) \cup (B \setminus A)$.
""", 1, 10, [
    r"Unwind ``belongs to exactly one of $A$ and $B$'' into two cases.",
    r"For the second formula prove two inclusions, splitting into the cases $x \in A$ and $x \notin A$.",
], ["def-set-operations"])

s.definition("def-function", "Function, image, preimage", r"""
Let $X$ and $Y$ be sets. A \emph{function} (or \emph{map}) $f \colon X \to Y$ assigns to each element $x \in X$ exactly one element $f(x) \in Y$. The set $X$ is the \emph{domain} of $f$ and $Y$ is its \emph{target}. For $A \subset X$ and $C \subset Y$,
\[ f(A) = \set{f(x) : x \in A} \qquad\text{and}\qquad f^{-1}(C) = \set{x \in X : f(x) \in C} \]
are the \emph{image} of $A$ and the \emph{preimage} of $C$. The \emph{range} of $f$ is $f(X)$. The notation $f^{-1}(C)$ does not suppose that $f$ has an inverse. If $f \colon X \to Y$ and $g \colon Y \to Z$ are functions, their \emph{composite} $g \circ f \colon X \to Z$ is $x \mapsto g(f(x))$. The \emph{identity map} of $X$ is $\id_X \colon X \to X$, $x \mapsto x$.
""")

s.result("ex-images-preimages", "exercise", "Images and preimages against unions and intersections", r"""
Let $f \colon X \to Y$ be a function, let $A, B \subset X$, and let $C, D \subset Y$. Prove:
\begin{enumerate}
\item $f^{-1}(C \cup D) = f^{-1}(C) \cup f^{-1}(D)$ and $f^{-1}(C \cap D) = f^{-1}(C) \cap f^{-1}(D)$.
\item $f(A \cup B) = f(A) \cup f(B)$.
\item $f(A \cap B) \subset f(A) \cap f(B)$, and give an example in which the two sides are different.
\end{enumerate}
""", r"""
(1) For $x \in X$ we have $x \in f^{-1}(C \cup D)$ if and only if $f(x) \in C \cup D$, if and only if $f(x) \in C$ or $f(x) \in D$, if and only if $x \in f^{-1}(C)$ or $x \in f^{-1}(D)$, if and only if $x \in f^{-1}(C) \cup f^{-1}(D)$. Replacing ``or'' by ``and'' and $\cup$ by $\cap$ throughout gives the second equality.

(2) Let $y \in f(A \cup B)$. Then $y = f(x)$ for some $x \in A \cup B$. If $x \in A$ then $y \in f(A)$, and if $x \in B$ then $y \in f(B)$; so $y \in f(A) \cup f(B)$. Conversely, if $y \in f(A)$ then $y = f(x)$ with $x \in A \subset A \cup B$, so $y \in f(A \cup B)$; the same argument applies if $y \in f(B)$.

(3) Let $y \in f(A \cap B)$, say $y = f(x)$ with $x \in A \cap B$. Since $x \in A$, $y \in f(A)$; since $x \in B$, $y \in f(B)$. So $y \in f(A) \cap f(B)$. For an example of strict inclusion take $X = \set{1, 2}$, $Y = \set{0}$, $f(1) = f(2) = 0$, $A = \set{1}$, $B = \set{2}$. Then $A \cap B = \varnothing$, so $f(A \cap B) = \varnothing$, while $f(A) \cap f(B) = \set{0}$.
""", 2, 15, [
    r"Each claim is a chain of ``if and only if'' statements, or two inclusions. Write out what membership in each side means.",
    r"For the strict inclusion in (3), choose a function that sends two different points to the same value and let $A$ and $B$ be disjoint.",
], ["def-function", "def-set-operations"])

s.definition("def-equivalence-relation", "Equivalence relation", r"""
A \emph{relation} on a set $S$ is a statement $s \sim s'$ that is either true or false for each ordered pair of elements $s, s' \in S$. It is an \emph{equivalence relation} if for all $s, s', s'' \in S$:
\begin{enumerate}
\item $s \sim s$ (reflexivity);
\item if $s \sim s'$ then $s' \sim s$ (symmetry);
\item if $s \sim s'$ and $s' \sim s''$ then $s \sim s''$ (transitivity).
\end{enumerate}
""")

s.definition("def-equivalence-class", "Equivalence class, representative", r"""
Let $\sim$ be an equivalence relation on $S$. The \emph{equivalence class} of $s \in S$ is
\[ [s] = \set{s' \in S : s' \sim s}. \]
Any member of an equivalence class is called a \emph{representative} of that class.
""")

s.result("prop-classes-partition", "proposition", "Equivalence classes partition the set", r"""
Let $\sim$ be an equivalence relation on a set $S$, and let $s, t \in S$. Then:
\begin{enumerate}
\item $s \in [s]$;
\item $[s] = [t]$ if and only if $s \sim t$;
\item if $[s] \cap [t] \ne \varnothing$ then $[s] = [t]$.
\end{enumerate}
Thus every element of $S$ lies in exactly one equivalence class: the classes are nonempty, pairwise disjoint, and their union is $S$.
""", r"""
(1) By reflexivity $s \sim s$, so $s \in [s]$.

(2) Suppose $s \sim t$. If $u \in [s]$ then $u \sim s$, and with $s \sim t$ transitivity gives $u \sim t$, so $u \in [t]$. Thus $[s] \subset [t]$. By symmetry $t \sim s$, and the same argument with $s$ and $t$ exchanged gives $[t] \subset [s]$. Hence $[s] = [t]$. Conversely, suppose $[s] = [t]$. By (1), $s \in [s] = [t]$, which says $s \sim t$.

(3) Let $u \in [s] \cap [t]$. Then $u \sim s$ and $u \sim t$. By symmetry $s \sim u$, and by transitivity $s \sim t$. By (2), $[s] = [t]$.

For the last sentence: each class $[s]$ is nonempty and each $s$ lies in some class, by (1); so the union of the classes is $S$. If $s$ lies in two classes $[t]$ and $[u]$, then $[t] \cap [u] \ne \varnothing$, so $[t] = [u]$ by (3). Hence $s$ lies in exactly one class, and two different classes are disjoint.
""", 2, 15, [
    r"Each of the three parts uses one or two of the three axioms. For (2), prove two inclusions.",
    r"For (3): an element $u$ common to both classes satisfies $u \sim s$ and $u \sim t$. Combine symmetry and transitivity to get $s \sim t$, then quote (2).",
], ["def-equivalence-relation", "def-equivalence-class"])

s.example("ex-fractions-motivation", r"""
Fractions are the familiar instance. The symbols $1/2$, $2/4$, and $-3/(-6)$ are different pairs of integers and yet name one rational number: a rational number is an equivalence class of such pairs, and $1/2$ is one of its representatives. The next exercise checks that ``naming the same fraction'' really is an equivalence relation.
""", "Fractions")

s.result("ex-fraction-relation", "exercise", "Equality of fractions is an equivalence relation", r"""
Let $S = \set{(a, b) : a, b \in \Z,\ b \ne 0}$, and define $(a, b) \sim (c, d)$ to mean $ad = bc$. Prove that $\sim$ is an equivalence relation on $S$.
""", r"""
\emph{Reflexivity.} For $(a, b) \in S$ we have $ab = ba$, so $(a, b) \sim (a, b)$.

\emph{Symmetry.} If $(a, b) \sim (c, d)$ then $ad = bc$, hence $cb = da$, which says $(c, d) \sim (a, b)$.

\emph{Transitivity.} Suppose $(a, b) \sim (c, d)$ and $(c, d) \sim (e, f)$, so $ad = bc$ and $cf = de$. Multiplying the first equation by $f$ and the second by $b$ gives
\[ adf = bcf = bde, \]
so $d(af - be) = 0$. Since $d \ne 0$ and a product of integers is zero only if one of the factors is zero, $af - be = 0$, that is, $af = be$. This says $(a, b) \sim (e, f)$.
""", 2, 15, [
    r"Reflexivity and symmetry are immediate from commutativity of multiplication. Transitivity is where the hypothesis $b \ne 0$ on second coordinates is used.",
    r"From $ad = bc$ and $cf = de$ derive $d(af - be) = 0$, then cancel $d$.",
], ["def-equivalence-relation"])

s.prose("prelim-logic", r"""
\textbf{Logic and proof.} Statements are combined with ``and'', ``or'' (always inclusive), ``not'', and ``implies''. The implication ``if $P$ then $Q$'', written $P \Rightarrow Q$, is false only when $P$ is true and $Q$ is false. Its \emph{converse} is $Q \Rightarrow P$, a different statement that may fail when the original holds. Its \emph{contrapositive} is ``not $Q$ $\Rightarrow$ not $P$'', which is logically the same statement; proving the contrapositive proves the implication. ``$P$ if and only if $Q$'' asserts both $P \Rightarrow Q$ and $Q \Rightarrow P$, and both must be proved.

The quantifiers are $\forall$ (``for all'', ``for each'') and $\exists$ (``there exists''). Their order matters: ``$\forall n \in \N\ \exists m \in \N$ with $m > n$'' is true, while ``$\exists m \in \N\ \forall n \in \N$, $m > n$'' is false. To negate a quantified statement, exchange $\forall$ and $\exists$ and negate what follows: the negation of ``$\forall x\ \exists y$ such that $P(x, y)$'' is ``$\exists x$ such that $\forall y$, not $P(x, y)$''.

A \emph{proof by contradiction} of a statement $P$ assumes that $P$ is false and deduces something impossible. A statement of the form ``$\forall x \in S$, $P(x)$'' is proved by taking an arbitrary $x \in S$, about which nothing else is assumed; it is disproved by a single \emph{counterexample}.
""")

s.prose("prelim-naturals", r"""
\textbf{Two facts about $\N$ taken for granted.} We use freely the \emph{principle of induction}: if a statement about $n$ holds for $n = 1$, and holds for $n + 1$ whenever it holds for $n$, then it holds for every $n \in \N$. Equivalent to it is the \emph{least element principle}: every nonempty subset of $\N$ has a smallest element. We also use the ordinary arithmetic of $\Z$ and $\Q$, including the fact that every integer is either \emph{even} (of the form $2k$ with $k \in \Z$) or \emph{odd} (of the form $2k + 1$), and never both.
""")

s.result("ex-even-square", "exercise", "An integer with even square is even", r"""
Let $n \in \Z$. Prove that if $n^2$ is even, then $n$ is even.
""", r"""
We prove the contrapositive: if $n$ is not even, then $n^2$ is not even. Suppose $n$ is not even. Then $n$ is odd, so $n = 2k + 1$ for some $k \in \Z$, and
\[ n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1. \]
This exhibits $n^2$ as odd, and an odd integer is not even. Hence if $n^2$ is even, $n$ must be even.
""", 1, 10, [
    r"A direct proof is awkward, because knowing $n^2 = 2m$ says little about $n$. Try the contrapositive.",
    r"Assume $n = 2k + 1$ and compute $n^2$.",
])

s.result("ex-no-smallest-positive-rational", "exercise", "There is no smallest positive rational number", r"""
Prove that the set $\set{r \in \Q : r > 0}$ has no smallest element.
""", r"""
Suppose, for contradiction, that $r$ is the smallest element of $\set{r \in \Q : r > 0}$. Then $r/2$ is rational, being a quotient of rational numbers with nonzero denominator, and $r/2 > 0$ because $r > 0$. Moreover $r/2 < r$, since $r - r/2 = r/2 > 0$. So $r/2$ is a positive rational number smaller than $r$, contradicting the choice of $r$. Hence there is no smallest positive rational number.
""", 1, 10, [
    r"Argue by contradiction: suppose $r$ is the smallest one and produce a smaller one.",
], ["def-sets"])

s.remark("prelim-outro", r"""
Compare the last exercise with the least element principle: a nonempty set of natural numbers always has a smallest element, a nonempty set of positive rational numbers need not. The gaps and the crowding in $\Q$ are the subject of the next section.
""")

s.card("set-equality", r"How do you prove that two sets $A$ and $B$ are equal?",
       r"Prove $A \subset B$ and $B \subset A$: take an arbitrary element of each side and show that it lies in the other.", "def-sets")
s.card("symmetric-difference", r"Define the symmetric difference $A \,\Delta\, B$ and give a formula for it.",
       r"The elements belonging to exactly one of $A$, $B$: $A \,\Delta\, B = (A \setminus B) \cup (B \setminus A) = (A \cup B) \setminus (A \cap B)$.", "ex-symmetric-difference")
s.card("de-morgan", r"State De Morgan's laws for subsets $A, B$ of $X$.",
       r"$X \setminus (A \cup B) = (X \setminus A) \cap (X \setminus B)$ and $X \setminus (A \cap B) = (X \setminus A) \cup (X \setminus B)$.", "ex-de-morgan")
s.card("image-intersection", r"Is $f(A \cap B) = f(A) \cap f(B)$ for every function $f$?",
       r"No. Only $f(A \cap B) \subset f(A) \cap f(B)$ holds in general: a constant map on $\set{1, 2}$ with $A = \set{1}$, $B = \set{2}$ gives $\varnothing$ on the left and a point on the right. Preimages, by contrast, respect both unions and intersections.", "ex-images-preimages")
s.card("equivalence-relation", r"Define an equivalence relation on a set $S$.",
       r"A relation $\sim$ that is reflexive ($s \sim s$), symmetric ($s \sim s' \Rightarrow s' \sim s$), and transitive ($s \sim s'$ and $s' \sim s'' \Rightarrow s \sim s''$).", "def-equivalence-relation")
s.card("classes-partition", r"What do the equivalence classes of an equivalence relation on $S$ do to $S$?",
       r"They partition it: every element lies in exactly one class, and $[s] = [t]$ if and only if $s \sim t$. Two classes that meet are equal.", "prop-classes-partition")
s.card("contrapositive", r"What is the contrapositive of $P \Rightarrow Q$, and what is its converse? Which is equivalent to $P \Rightarrow Q$?",
       r"Contrapositive: not $Q$ $\Rightarrow$ not $P$, equivalent to the original. Converse: $Q \Rightarrow P$, not equivalent.")
s.card("negate-quantifiers", r"Negate: ``for every $\eps > 0$ there exists $\delta > 0$ such that $P(\eps, \delta)$''.",
       r"There exists $\eps > 0$ such that for every $\delta > 0$, $P(\eps, \delta)$ fails.")

s.write()
