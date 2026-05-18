def _ensure_shape_dtype(value):
    # Return value paired with dtype FP32 if it is a shape.
    if _is_shape(value):
        return (value, 'f')
    # Otherwise, returns it with assuming a shape-dtype pair.
    else:
        return value