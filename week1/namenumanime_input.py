#learnt more inputs and outputs
name=input("Twin whats your name?").strip().title()
First, Last= name.split()
fav_num1=int(input("Whats ur first fave num"))
fav_num2=int(input("Whats ur second fave num"))
thesum= fav_num1+fav_num2
Anime=input("Whats your favourite anime?").strip().title()
print(First,",", Anime,",","is a great choice!", sep=" ",end="")
print(",",thesum,",is the sum of ur fav num is", sep=" ")
