from bezier_interpolation import cubic_interpolation, quadratic_interpolation

data = {"x": [1, 2, 3], "y": [-1, -5, 3]}
data = list(zip(data["x"], data["y"]))
c_interpolated_data = cubic_interpolation(data)
print(c_interpolated_data)

q_interpolated_data = quadratic_interpolation(data)
print(q_interpolated_data)