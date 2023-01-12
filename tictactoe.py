grille = {'7': ' ', '8': ' ', '9': ' ', 
             '4': ' ', '5': ' ', '6': ' ', 
             '1': ' ', '2': ' ', '3': ' '} 
 #définition des cases dans le grille# 

def Aire(grille): 
     print('┌-┬-┬-┐') 
     print('│' + grille['7'] + '│' + grille['8'] + '│' + grille['9'] + '│') 
     print('├-┼-┼-┤') 
     print('│' + grille['4'] + '│' + grille['5'] + '│' + grille['6'] + '│') 
     print('├-┼-┼-┤') 
     print('│' + grille['1'] + '│' + grille['2'] + '│' + grille['3'] + '│') 
     print('└-┴-┴-┘') 
 #grille de jeu# 

def tictactoe(): 
     tour = 'X' 
     J = 'Joueur 1' 
     compte = 0 

     for i in range(10): 
         Aire(grille) 
         print("C'est au tour du "+J+". Placer en quelle position?") 

         move = input() 

         if grille[move] == ' ': 
             grille[move] = tour 
             compte += 1 
         else: 
             print("Cette position est déjà prise.\nPlacer en quelle position?") 
             continue 

 # vérification de win # 
         if compte >= 5: 
             if grille['7'] == grille['8'] == grille['9'] != ' ': #Ligne supérieur# 
                 Aire(grille) 
                 print("\nPartie Terminée.\n") 
                 print("  " +J+ " à gagné. ") 
                 break 
             elif grille['4'] == grille['5'] == grille['6'] != ' ': #Ligne intermédiaire# 
                 Aire(grille) 
                 print("\nPartie Terminée.\n") 
                 print("  " +J+ " à gagné. ") 
                 break 
             elif grille['1'] == grille['2'] == grille['3'] != ' ': #Ligne inférieur# 
                 Aire(grille) 
                 print("\nPartie Terminée.\n") 
                 print("  " +J+ " à gagné. ") 
                 break 
             elif grille['1'] == grille['4'] == grille['7'] != ' ': #Ligne gauche# 
                 Aire(grille) 
                 print("\nPartie Terminée.\n") 
                 print("  " +J+ " à gagné. ") 
                 break 
             elif grille['2'] == grille['5'] == grille['8'] != ' ': #Ligne milieu# 
                 Aire(grille) 
                 print("\nPartie Terminée.\n") 
                 print("  " +J+ " à gagné. ") 
                 break 
             elif grille['3'] == grille['6'] == grille['9'] != ' ': #Ligne droite# 
                 Aire(grille) 
                 print("\nPartie Terminée.\n") 
                 print("  " +J+ " à gagné. ") 
                 break 
             elif grille['7'] == grille['5'] == grille['3'] != ' ': #diagonale # 
                 Aire(grille) 
                 print("\nPartie Terminée.\n") 
                 print("  " +J+ " à gagné. ") 
                 break 
             elif grille['1'] == grille['5'] == grille['9'] != ' ': #diagonale /# 
                 Aire(grille) 
                 print("\nPartie Terminée.\n") 
                 print("  " +J+ " à gagné. ") 
                 break 

         # c'est une égalité si ni le joueur 1 ou 2 ne gagne. # 
         if compte == 9: 
             print("\nPartie Terminée.\n") 
             print("C'est une égalité!!") 

         # Changement de joueur à chaque tour. # 
         if tour =='X': 
             tour = 'O' 
             J = 'Joueur 2' 
         else: 
             tour = 'X' 
             J = 'Joueur 1' 

tictactoe()
