# SPDX-License-Identifier: Apache-2.0

import numpy as np
from onnxconverter_common.tree_ensemble import *  # noqa


def _process_process_tree_attributes(attrs):
    # Spark may store attributes as range and not necessary list.
    # ONNX does not support this type of attribute value.
    update = {}
    wrong_types = []
    for k, v in attrs.items():
        if isinstance(v, (str, list, int, float, np.ndarray)):
            continue
        if isinstance(v, range):
            update[k] = list(v)
            continue
        wrong_types.append(f"Unexpected type {type(v)} for attribute {k!r}.")
    if len(wrong_types) > 0:
        raise TypeError("Unexpected type for one or several attributes:\n" + "\n".join(wrong_types))
    if update:
        attrs.update(update)

