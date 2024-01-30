#!/usr/bin/python3

def matrix_mul(m_a, m_b):
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    for n in range(0, len(m_a)):
        if not isinstance(m_a[n], list):
            raise TypeError("m_a must be a list of lists")
        if m_a == [] or m_a[n] == []:
            raise ValueError("m_a can't be empty")
        for i in range(0, len(m_a[n])):
            if not isinstance(m_a[n][i], (int, float)):
                raise TypeError("m_a should contain only integers or floats")
            lengtho_a = len(m_a[0])
            if len(m_a[n]) != lengtho_a:
                raise TypeError("each row of m_a must be of the same size")
    if not isinstance(m_b, list):
        raise TypeError("m_a must be a list")
    for n in range(0, len(m_b)):
        if not isinstance(m_b[n], list):
            raise TypeError("m_b must be a list of lists")
        if m_b == [] or m_b[n] == []:
            raise ValueError("m_b can't be empty")
        for i in range(0, len(m_b[n])):
            if not isinstance(m_b[n][i], (int, float)):
                raise TypeError("m_b should contain only integers or floats")
            lengtho_b = len(m_b[0])
            if len(m_b[n]) != lengtho_b:
                raise TypeError("each row of m_b must be of the same size")