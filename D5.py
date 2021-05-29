#highest_score in the class
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

big=student_scores[0]
for i in student_scores:
   if i>big:
     big=i
print(f"Dizinin en büyük elemanı {big} 'dır/dir ")
  
        
#Method 2

student_score=[100,120,190]
highest_score=0
for score in student_scores:
    if score > highest_score:
        highest_score=score
        
print(f"Dizinin en büyük elemanı {big} 'dır/dir ")
       