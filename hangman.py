import random



hangman_sträng_lista =("boll","äpple","träd","motorbåt","skor","arbetsplats","pythonprogrammering")
max_gissningar = 10


def seperate_line():
    print("-"*80)


def main():
    print("Välkommen till spelet Hangman!")
    print("Gör någon av valet nedan")
    
    seperate_line()
   
    while True:
        print("[1] Spela")
        print("[2] Regler")
        print("[3] Avsluta")
        try:
            spelarens_val = int(input("Ditt val: ")or 0)
        except ValueError:
            print("Ogiltigt inmatning. Var god ange ett tal mellan 1-3")
            continue

        datorns_val = random.choice(hangman_sträng_lista)

        if spelarens_val == 1:
            spela(datorns_val, max_gissningar)
        elif spelarens_val== 2:
            regler()
        elif spelarens_val == 3:
            print("Tack för att du spelade")
            break



def spela(datorns_val,max_gissningar): 
    antal_bokstaver = len(datorns_val)
    streck_sträng = "_"* antal_bokstaver
    print(f"Ditt ord består av {antal_bokstaver} bokstäver{streck_sträng}. Du har {max_gissningar} gissningar kvar!")

    rätt_gissningar = set()
    fel_gissning = []
    antal_gissningar = 0

    while True:
        användarens_bokstäver = input("Gissa på en bokstav: ")
        seperate_line()

        if användarens_bokstäver in datorns_val:
            print(f"Bra jobbat bokstaven {användarens_bokstäver} finns med i ordet")
            rätt_gissningar.add(användarens_bokstäver)
            streck_sträng = "".join([bokstav if bokstav in rätt_gissningar else "-" for bokstav in datorns_val])
            if streck_sträng == datorns_val:
                print(f"Grattis, du svarade rätt på ordet {streck_sträng}")
                break
            seperate_line()
        else:
            print(f"Tyvärr så finns inte bokstaven {användarens_bokstäver} med i ordet ")
            fel_gissning.append(användarens_bokstäver)
            antal_gissningar +=1

            seperate_line()
        
        
        print("Nuvarande gissning:",streck_sträng)
        print("Din gissning på bokstäver:",fel_gissning)
        print(f"Antal gissningar kvar {max_gissningar - antal_gissningar}")
        if antal_gissningar == max_gissningar:
            print(f"Tyvärr du har inga gissningar kvar, det rätta ordet va {datorns_val} ")
            seperate_line()
            break
    
  
def regler():
        print("Spelaren ska gissa en bokstav i taget, och datorn ger feedback om bokstaven finns i ordet eller inte")
        print("Spelet fortsätter tills spelaren har gissat hela ordet eller har gjort tillräckligt många felaktiga gissningar.")
        seperate_line()
        input("Tryck på Enter för att komma tillbaka till startsidan.")
        seperate_line()
     
        
        
        
        
    

    

main()
