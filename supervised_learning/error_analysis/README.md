# Error Analysis

This directory contains utilities for evaluating classification models.

## 2. Precision

`2-precision.py` implements `precision(confusion)` to compute per-class precision from a confusion matrix.

- Confusion matrix shape: `(classes, classes)`
- Rows: true labels
- Columns: predicted labels
- Output: precision per class, shape `(classes,)`
