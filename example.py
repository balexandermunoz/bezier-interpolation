from bezier_interpolation import cubic_interpolation, quadratic_interpolation

c_data = {"x": [1, 2, 3], "y": [-1, -5, 3]}
c_data = list(zip(c_data["x"], c_data["y"]))
c_interpolated_data = cubic_interpolation(c_data)
print(c_interpolated_data)
# Returns: [[1, -1], [1.3, -3.3], [1.6 -5.6], [2, -5], [2.3, -4.3], [2.6, -0.6], [3, 3]]

q_data = [(1, 1), (2, 4), (3, 9)]
q_interpolated_data = quadratic_interpolation(q_data)
print(q_interpolated_data)
# Returns:  [[1, 1], [1.5, 2.5], [2, 4], [2.5, 5.5], [3, 9]]
