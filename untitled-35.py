  
import tkinter as tk 
def add_item():
    """
    add the text in the Entry widget to the end of the listbox
    """
    listbox1.insert(tk.END, enter1.get())
def delete_item():
    """
    delete a selected line from the listbox
    """
    try:
        # Obtenir l'index de ligne sélectionné
        index = listbox1.curselection()[0]
        listbox1.delete(index)
    except IndexError:
        pass
   
def get_list(event):
    """
    function to read the listbox selection
    and put the result in an entry widget
    """
    # Obtenir l'index de ligne sélectionné
    index = listbox1.curselection()[0]
    # Obtenir le texte de la ligne
    seltext = listbox1.get(index)
    # Supprimer le texte précédent dans enter1
    enter1.delete(0, 50)
    # Affiche maintenant le texte sélectionné
    enter1.insert(0, seltext)
def set_list(event):
    """
    """
    try:
        index = listbox1.curselection()[0]
        # Supprimer l'ancienne ligne de listbox
      #  listbox1.delete(index)
    except IndexError:
        index = tk.END
 # Insérer l'élément édité dans la listebox1 à l'index
    listbox1.insert(index, enter1.get())
def sort_list():
    """
    function to sort listbox items case insensitive
    """
    temp_list = list(listbox1.get(0, tk.END))
    temp_list.sort(key=str.lower)
    # Supprimer le contenu de la liste actuelle
    listbox1.delete(0, tk.END)
    # Liste de chargement avec données triées
    for item in temp_list:
        listbox1.insert(tk.END, item)
def save_list():
    """
    save the current listbox contents to a file
    """
    # Obtenir une liste de listbox lines
    temp_list = list(listbox1.get(0, tk.END))
    # Ajoutez une nouvelle ligne de queue à chaque ligne
    temp_list = [chem + '\n' for chem in temp_list]
    # Donner au fichier un nom différent
    fout = open("chem_data.txt", "w")
    fout.writelines(temp_list)
    fout.close()
 
def printer(event):
    print("select=",listbox1.get(listbox1.curselection()))
     
# Créer l'exemple de fichier de données
str1 = """
"""
fout = open("chem_data.txt", "w")
fout.write(str1)
fout.close()
   
#Lisez le fichier de données dans une liste
fin = open("chem_data.txt", "r")
chem_list = fin.readlines()
fin.close()
# Enlevez la nouvelle ligne de queue
chem_list = [chem.rstrip() for chem in chem_list]
   
root = tk.Tk()
root.title("Listbox Operations")
#  Créez la liste (notez que la taille est en caractères)
listbox1 = tk.Listbox(root, width=50, height=6)
listbox1.grid(row=0, column=0)
   
# Créez une barre de défilement verticale à droite de la liste
yscroll = tk.Scrollbar(command=listbox1.yview, orient=tk.VERTICAL)
yscroll.grid(row=0, column=1, sticky=tk.N+tk.S)
listbox1.configure(yscrollcommand=yscroll.set)
listbox1.bind("<<ListboxSelect>>", printer)
   
# Utilisez le widget d'entrée pour afficher / modifier la sélection
enter1 = tk.Entry(root, width=50, bg='yellow')
enter1.insert(0, '')  #Ajouter un etudiant
enter1.grid(row=1, column=0)
# Appuyez sur la touche de retour pour mettre à jour la ligne modifiée
enter1.bind('<Return>', set_list)
# Ou double-cliquez sur le bouton gauche de la souris pour mettre à jour la ligne
enter1.bind('<Double-1>', set_list)
# Bouton pour trier la liste
button1 = tk.Button(root, text='Trier la liste', command=sort_list)
button1.grid(row=2, column=0, sticky=tk.W)
# Pour sauvegarder les lignes de données de la liste dans un fichier
button2 = tk.Button(root, text='Enregistrer', command=save_list)
button2.grid(row=3, column=0, sticky=tk.W)
# Pour ajouter une ligne au listbox
button3 = tk.Button(root, text='Ajouter un etudiant ', command=add_item)
button3.grid(row=2, column=0, sticky=tk.E)
#Bouton pour supprimer une ligne de listbox
button4 = tk.Button(root, text='Supprimer un etudiant ', command=delete_item)
button4.grid(row=3, column=0, sticky=tk.E)
# Charger la liste avec les données
for item in chem_list:
    listbox1.insert(tk.END, item)
   
# left mouse click on a list item to display selection
listbox1.bind('<ButtonRelease-1>', get_list)
   
root.mainloop()
