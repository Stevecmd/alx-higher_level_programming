def add_tuple(tuple_a=(), tuple_b=()):
    """Add two tuples."""
    """Ensure both tuples have at least 2 elements by padding with zeros if necessary"""
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    """Return a tuple with the sum of corresponding elements from tuple_a and tuple_b"""
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
