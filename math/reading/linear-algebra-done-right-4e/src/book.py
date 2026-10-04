"""Generate the approved manifest. Run from any working directory."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def chapter(n, title, about, requires, titles):
    sections = [dict(id=f'{n}{chr(97+i)}', number=f'{n}{chr(65+i)}', title=t) for i,t in enumerate(titles)]
    if n == 4:
        sections = [dict(id='4-polynomials', number='4', title=titles[0])]
    sections.append(dict(id=f'{n}-exercises', number='', title='Exercises'))
    return dict(id=f'c{n}', number=str(n), title=title, about=about, requires=requires, sections=sections)

book = dict(version=1, slug='linear-algebra-done-right-4e',
    title='Linear Algebra Done Right — Proof Reading Module',
    author='Sheldon Axler (source textbook); original module adaptation',
    edition='Fourth edition; source PDF revised 16 August 2026',
    about='An independently worded, proof-first adaptation following Sheldon Axler\'s Linear Algebra Done Right, fourth edition (https://linear.axler.net/LADR4e.pdf). The source is licensed under CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/); this adaptation supplies rewritten exposition and proofs, recall cards, and original optional exercises.',
    macros=r'''\newcommand{\R}{\mathbb{R}}
\newcommand{\C}{\mathbb{C}}
\newcommand{\F}{\mathbb{F}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Poly}{\mathcal{P}}
\newcommand{\Lin}{\mathcal{L}}
\newcommand{\Mat}{\mathcal{M}}
\newcommand{\Bil}{\mathcal{B}}
\newcommand{\Alt}{\mathcal{A}}
\newcommand{\dual}[1]{{#1}^{\prime}}
\newcommand{\ip}[2]{\left\langle #1,#2\right\rangle}
\newcommand{\norm}[1]{\left\lVert #1\right\rVert}
\newcommand{\abs}[1]{\left\lvert #1\right\rvert}
\DeclareMathOperator{\Span}{span}
\DeclareMathOperator{\Null}{null}
\DeclareMathOperator{\Range}{range}
\DeclareMathOperator{\Rank}{rank}
\DeclareMathOperator{\tr}{tr}
\DeclareMathOperator{\sgn}{sgn}
\DeclareMathOperator{\Vol}{volume}''',
    chapters=[
        chapter(1,'Vector Spaces','Build scalar and coordinate arithmetic, vector spaces, subspaces, and direct sums.',[],[r'Coordinates in $\R^n$ and $\C^n$','Vector Space Axioms','Subspaces and Their Sums']),
        chapter(2,'Finite-Dimensional Vector Spaces','Develop spanning lists, independence, bases, and dimension.',['c1'],['Spanning and Linear Independence','Constructing and Extending Bases','Dimension and Subspace Arithmetic']),
        chapter(3,'Linear Maps','Study kernels, images, matrices, inverses, quotients, and duality.',['c2'],['Linear Maps and Their Algebra','Kernels, Images, and the Dimension Formula','Matrix Representations and Rank','Inverses, Isomorphisms, and Basis Changes','Product Spaces and Quotient Spaces','Dual Spaces and Dual Maps']),
        chapter(4,'Polynomials','Establish scalar identities, polynomial division, roots, and factorization.',['c2'],['Scalar Identities and Polynomial Factorization']),
        chapter(5,'Eigenvalues and Eigenvectors','Analyze operators using invariant subspaces, polynomial identities, and diagonalization.',['c3','c4'],['Invariant Subspaces and Eigenvectors','Minimal Polynomials and Eigenvalue Existence','Triangular Representations','Diagonalization and Eigenvalue Bounds','Operators That Commute']),
        chapter(6,'Inner Product Spaces','Develop orthogonality, orthonormal bases, projection, and least squares.',['c5'],['Inner Products, Lengths, and Inequalities','Orthonormal Bases and Functional Representation','Orthogonal Projection, Minimization, and Pseudoinverses']),
        chapter(7,'Operators on Inner Product Spaces','Use adjoints, spectral theory, and singular values to study operators and geometry.',['c6'],['Adjoints, Self-Adjoint Operators, and Normality','Real and Complex Spectral Theorems','Positivity and Operator Square Roots','Isometries, Unitary Maps, and Matrix Factorizations','Singular Values and Singular Value Decomposition','Approximation, Polar Decomposition, and Volume']),
        chapter(8,'Operators on Complex Vector Spaces','Use generalized eigenvectors and nilpotence to obtain decompositions, Jordan bases, and trace identities.',['c6'],['Generalized Eigenvectors and Nilpotence','Decomposing into Generalized Eigenspaces','Operator Square Roots and Jordan Bases','Trace of Matrices and Operators']),
        chapter(9,'Multilinear Algebra and Determinants','Develop bilinear and alternating forms, determinants, and tensor products.',['c7','c8'],['Bilinear Forms and Quadratic Expressions','Multilinearity, Alternation, and Permutations','Determinants from Alternating Forms','Tensor Products and Their Universal Property']),
    ])
if __name__ == '__main__':
    with (ROOT/'book.json').open('w',encoding='utf-8') as f:
        json.dump(book,f,indent=1,ensure_ascii=False)
        f.write('\n')
