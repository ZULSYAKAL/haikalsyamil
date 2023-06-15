# pyhton quiz game TEKA GENRE LAGU
print("MUSIC GENRE GUESSING GAME")
print("****************************")
print("Select a song genre for each song below")
soalan=("**Feet up on the dash, drivin' nowhere fast**\n",
          "**I feel okay when you smile,smile**\n",
          "**Somtimes, all i think about is you**\n"
        "**I do the same thing, i told you that i never would**\n\n",)

def pilih():
        print("A. Golden Hour")
        print ("B. Dandelion  ")
        print ("C. Heat Waves ")
        print ("D. Never gonna give you up ")
        print ("E. Stay ")

        
jawapan =("A","B","C","D","E")
teka=[]
score=0
bil_soalan=0

for soalan in soalan:
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print(soalan)
        pilih() # function menu pilihan jawapan
        
        guess=input("Sila pilih (A,B,C,D,E): ").upper()
        teka.append(guess)
        if guess == jawapan[bil_soalan]:
            score +=1
            print("Tahniah!jawapan anda betul!")
        else:
            print("\nMaaf! jawapan anda salah.Sila cuba lagi!")
            print(f"{jawapan[bil_soalan]} ialah jawapan yang tepat")
        bil_soalan +=1


# papar keputusan
print("\n**********************")
print("        RESULT!!!!              ")
print("**********************")

print("CORRECT ANSWER: ", end="")
for answer in jawapan:
    print("/",answer, end="")
print()

print("TEKAAN: ", end="")
for guess in teka:
     print("/",guess, end="")
print()

#kira jumlah markah
markah = (score / bil_soalan )* 100

# papar keputusan markah
print("total question:", bil_soalan)
print("Correct answer:", score)
print("Points Collected: ", round (score,2), "%")
print("**********************")
