import math

# noktaların tanımlanması
nokta = [(1, 2), (3, 4), (5, 6), (7, 8)]

# öklid mesafesi için bir fonksiyon yazma
def euclideanDistance(nokta1, nokta2):
    x1, y1 = nokta1
    x2, y2 = nokta2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# mesafelerin hesaplanması
mesafeler = []
for i in range(len(nokta)):
    for z in range(i + 1, len(nokta)):
        mesafe = euclideanDistance(nokta[i], nokta[z])
        mesafeler.append(mesafe)

#  minimum mesafe
min_mesafe = min(distances)
print("Minimum mesafe:", min_mesafe)
