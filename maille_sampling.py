import svgpathtools
import csv
import matplotlib.pyplot as plt

# Charger le fichier SVG
paths, attributes = svgpathtools.svg2paths('stent 2 maille.svg') 

# Extract cubic Bézier curve data from SVG
bezier_curves = []

for path in paths:
    for segment in path:
        if isinstance(segment, svgpathtools.path.CubicBezier):
            # Extract control points and end point of cubic Bézier curve
            control1 = (-segment.start.real, segment.start.imag)
            control2 = (-segment.control1.real, segment.control1.imag)
            control3 = (-segment.control2.real, segment.control2.imag)
            end_point = (-segment.end.real, segment.end.imag)
            
            # Store Bézier curve data as a tuple of control points and end point
            bezier_curve = (control1, control2, control3, end_point)
            bezier_curves.append(bezier_curve)

#print(len(bezier_curves))
print(len(paths))
# Save Bézier curve data to a CSV file
csv_file = 'bezier_curve_data.csv'

with open(csv_file, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Control Point 1 (x)', 'Control Point 1 (y)', 'Control Point 2 (x)', 'Control Point 2 (y)', 'Control Point 3 (x)', 'Control Point 3 (y)', 'End Point (x)', 'End Point (y)'])
    
    for bezier_curve in bezier_curves:
        csv_writer.writerow([bezier_curve[0][0], bezier_curve[0][1], bezier_curve[1][0], bezier_curve[1][1], bezier_curve[2][0], bezier_curve[2][1], bezier_curve[3][0], bezier_curve[3][1]])

print(f'Bézier curve data has been saved to {csv_file}')


# def cubic_bezier(t, p0, p1, p2, p3):
#     x = (1 - t) ** 3 * p0[0] + 3 * (1 - t) ** 2 * t * p1[0] + 3 * (1 - t) * t ** 2 * p2[0] + t ** 3 * p3[0]
#     y = (1 - t) ** 3 * p0[1] + 3 * (1 - t) ** 2 * t * p1[1] + 3 * (1 - t) * t ** 2 * p2[1] + t ** 3 * p3[1]
#     return x, y

# Plot the Bézier curves
plt.figure(figsize=(8, 8))

listeX = []
listeY = []
for bezier_curve in bezier_curves:
    # Generate points on the Bézier curve
    num_points = 100
    curve_points = []
    
    for t in range(num_points + 1):
        t /= num_points
        x = (1 - t) ** 3 * bezier_curve[0][0] + 3 * (1 - t) ** 2 * t * bezier_curve[1][0] + 3 * (1 - t) * t ** 2 * bezier_curve[2][0] + t ** 3 * bezier_curve[3][0]
        y = (1 - t) ** 3 * bezier_curve[0][1] + 3 * (1 - t) ** 2 * t * bezier_curve[1][1] + 3 * (1 - t) * t ** 2 * bezier_curve[2][1] + t ** 3 * bezier_curve[3][1]
        curve_points.append((x, y))
        listeX.append(x)
        listeY.append(y)
    # Plot the segments (points) we got from the Bézier Curve calculation
    plt.plot(*zip(*curve_points), marker='o')
    # Plot control points
    plt.plot(*zip(bezier_curve[0], bezier_curve[1], bezier_curve[2], bezier_curve[3]), marker='+', linestyle='dashed')


csv_file_maille = 'maille_bezier_curve_data.csv'
with open(csv_file_maille, 'w', newline='') as csv_file_maille:
    csv_writer = csv.writer(csv_file_maille)
    csv_writer.writerow(['X', 'Y'])
    
    for i in range (len(listeX)):
        csv_writer.writerow([listeX[i],listeY[i]])

#plt.plot(listeX, listeY,"+")
plt.show()
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Bézier Curves from SVG')
# plt.grid(True)
# plt.show()


