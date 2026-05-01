import re

with open("overall.tex", "r") as f:
    text = f.read()

replacements = [
    (r"\\paragraph\{The IPM bottleneck\.\} Classical", r"\\subsubsection{The IPM Bottleneck}\nClassical"),
    (r"\\paragraph\{When does it work\?\} The geometric", r"\\subsubsection{When does it work?}\nThe geometric"),
    (r"\\paragraph\{Setup\.\} We empirically verify", r"\\subsubsection{Experimental Setup}\nWe empirically verify"),
    (r"\\paragraph\{Hypothesis\.\} The empirical success rate should", r"\\subsubsection{Hypothesis}\nWe hypothesize that the empirical success rate should"),
    (r"\\paragraph\{Results\.\} Three distinct regions", r"\\subsubsection{Results}\nOur results show that three distinct regions"),
    (r"\\paragraph\{Setup\.\} We construct a matrix", r"\\subsubsection{Experimental Setup}\nWe construct a matrix"),
    (r"\\paragraph\{Results\.\} Model B", r"\\subsubsection{Results}\nThe experimental results show that Model B"),
    (r"\\paragraph\{Classical matrix completion prediction\.\} In the linear", r"\\subsubsection{Classical Matrix Completion Prediction}\nIn the linear"),
    (r"\\paragraph\{Connection to implicit regularization\.\} Frobenius regularization", r"\\subsubsection{Connection to Implicit Regularization}\nFrobenius regularization"),
    (r"\\paragraph\{Hypothesis\.\} The classical Pataki bound predicts", r"\\subsubsection{Hypothesis}\nWe hypothesize that while the classical Pataki bound predicts"),
    (r"\\paragraph\{Results\.\}\n", r"\\subsubsection{Results}\n"),
    (r"\\paragraph\{Effect of precision\.\} We swept", r"\\subsubsection{Effect of Precision}\nWe swept"),
    (r"\\paragraph\{Effect of temperature\.\} Sweeping the Softmax", r"\\subsubsection{Effect of Temperature}\nSweeping the Softmax"),
    (r"\\paragraph\{Hypothesis\.\} Margin Rank, not linear rank, is", r"\\subsubsection{Hypothesis}\nOur primary hypothesis is that Margin Rank, not linear rank, is"),
    (r"\\paragraph\{How to apply it\.\} Given a target", r"\\subsubsection{Application Methodology}\nTo apply this theory, given a target"),
    (r"\\paragraph\{Failure\.\} The algorithm predicted", r"\\subsubsection{Failure of Implicit Regularization}\nThe algorithm predicted"),
    (r"\\paragraph\{Analysis\.\} This failure exposed", r"\\subsubsection{Analysis of the Failure}\nThis failure exposed"),
    (r"\\paragraph\{Resolution\.\} To compute the true Margin Rank", r"\\subsubsection{Resolution via Hard Bottleneck}\nTo correctly compute the true Margin Rank"),
    (r"\\paragraph\{Block-Diagonal\.\} Two semantic clusters", r"\\subsubsection{Block-Diagonal Motif}\nFor the block-diagonal motif, two semantic clusters"),
    (r"\\paragraph\{Identity\.\} Twenty mutually exclusive", r"\\subsubsection{Identity Motif}\nFor the identity motif, twenty mutually exclusive"),
    (r"\\paragraph\{Sparse Random\.\} High-entropy chaotic", r"\\subsubsection{Sparse Random Motif}\nFor the sparse random motif, high-entropy chaotic"),
    (r"\\paragraph\{Head 10: The Semantic Router\.\} Head 10's", r"\\subsubsection{Head 10: The Semantic Router}\nHead 10's"),
    (r"\\paragraph\{Lossless Surgical Pruning \(SVD Compression\)\.\}", r"\\subsubsection{Lossless Surgical Pruning (SVD Compression)}"),
    (r"\\paragraph\{Proxy-Driven Architectural Search\.\}", r"\\subsubsection{Proxy-Driven Architectural Search}"),
    (r"\\paragraph\{Dynamic Token Routing\.\}", r"\\subsubsection{Dynamic Token Routing}")
]

for old, new in replacements:
    text = re.sub(old, new, text)

with open("overall.tex", "w") as f:
    f.write(text)

