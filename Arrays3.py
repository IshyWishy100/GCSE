ratings = []

for i in range(5):
    rating = int(input("Enter book rating"))
    ratings.append(rating)

totalRatings = 0
highRatings = 0
for i in ratings:
    if i >= 4:
        highRatings += 1
    totalRatings += i
    
