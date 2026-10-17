import tkinter as tk
from contatto import Contatto
from rubrica import AddressBook

rubrica = AddressBook()


def get_number():
    nome_cognome = blocco_nome.get().strip()
    numero = blocco_numero.get().strip()

    persona = Contatto(nome_cognome, numero)

    if persona.check_all():
        rubrica.add_contact(persona)
        contact_block.insert(tk.END, persona.putting_together())

        blocco_nome.delete(0, tk.END)
        blocco_numero.delete(0, tk.END)

        spazio_assenza.config(text="")
    else:
        spazio_assenza.config(
            text="Inserisci nome e numero valido"
        )
        blocco_nome.delete(0, tk.END)
        blocco_numero.delete(0, tk.END)


def search_contact():
    nome_cercato = spazio_ricerca.get().strip().lower()

    contact_block.selection_clear(0, tk.END)
    spazio_assenza.config(text="")

    trovato = False

    for indice, contatto in enumerate(rubrica.contacts):
        if nome_cercato and nome_cercato == contatto.nome.lower():
            contact_block.selection_set(indice)
            contact_block.see(indice)
            trovato = True
            break

    if not trovato:
        spazio_assenza.config(text="Contatto non trovato")


def close_app():
    rubrica.close()
    root.destroy()

def activation_button(event):
    bottone_elimina_contatto.config(state=tk.NORMAL)

def contact_elimination():
    indice_da_eliminare=contact_block.curselection()
    if indice_da_eliminare:
        indice=indice_da_eliminare[0]
        rubrica.delete_contact(rubrica.contacts[indice])
        contact_block.delete(indice)
        rubrica.contacts.pop(indice)
        contact_block.selection_clear(0, tk.END)
        bottone_elimina_contatto.config(state=tk.DISABLED)


def reset_button(event):
    print("Siamo qui")
    widget=root.winfo_containing(event.x_root, event.y_root)
    widget_event=event.widget
    if widget_event==bottone_elimina_contatto:
        return
    if widget!=contact_block or isinstance(widget_event, (tk.Entry,tk.Button)):
        contact_block.selection_clear(0, tk.END)
        bottone_elimina_contatto.config(state=tk.DISABLED)



# Finestra principale
root = tk.Tk()
root.title("Rubrica Moderna")
root.geometry("950x800")
root.configure(background="#F4F6F9")
root.protocol("WM_DELETE_WINDOW", close_app)


# Header superiore
header_frame = tk.Frame(
    root,
    bg="#1E293B",
    height=70
)
header_frame.pack(fill=tk.X)

titolo = tk.Label(
    header_frame,
    bg="#1E293B",
    fg="white",
    text="GESTIONE RUBRICA",
    font=("Segoe UI", 16, "bold"),
    pady=18
)
titolo.pack()


# Contenitore principale
main_container = tk.Frame(
    root,
    bg="#F4F6F9"
)
main_container.pack(
    fill=tk.BOTH,
    expand=True,
    padx=25,
    pady=20
)


# COLONNA SINISTRA: lista contatti
colonna_sinistra = tk.Frame(
    main_container,
    bg="white",
    bd=0,
    highlightbackground="#E2E8F0",
    highlightthickness=1
)
colonna_sinistra.pack(
    side=tk.LEFT,
    fill=tk.BOTH,
    expand=True,
    padx=(0, 15)
)

contact_list_label = tk.Label(
    colonna_sinistra,
    bg="white",
    fg="#1E293B",
    font=("Segoe UI", 12, "bold"),
    text="I MIEI CONTATTI"
)
contact_list_label.pack(
    anchor=tk.W,
    padx=20,
    pady=(20, 10)
)

contact_block = tk.Listbox(
    colonna_sinistra,
    bg="#F8FAFC",
    fg="#334155",
    font=("SF Pro Display", 11),
    selectbackground="#3B82F6",
    selectforeground="white",
    bd=0,
    highlightthickness=0,
    activestyle="none"
)
contact_block.pack(
    fill=tk.BOTH,
    expand=True,
    padx=20,
    pady=(0, 20)
)

# Carica nella Listbox i contatti recuperati dal database
for contatto in rubrica.contacts:
    contact_block.insert(
        tk.END,
        contatto.putting_together()
    )


# COLONNA DESTRA: azioni
colonna_destra = tk.Frame(
    main_container,
    bg="#F4F6F9",
    width=350
)
colonna_destra.pack(
    side=tk.RIGHT,
    fill=tk.Y
)


# Card aggiungi contatto
card_aggiungi = tk.Frame(
    colonna_destra,
    bg="white",
    highlightbackground="#E2E8F0",
    highlightthickness=1
)
card_aggiungi.pack(
    fill=tk.X,
    pady=(0, 15),
    ipadx=15,
    ipady=15
)

aggiungi_numero = tk.Label(
    card_aggiungi,
    bg="white",
    font=("Segoe UI", 11, "bold"),
    fg="#1E293B",
    text="➕ AGGIUNGI NUOVO CONTATTO"
)
aggiungi_numero.pack(
    anchor=tk.W,
    padx=15,
    pady=(10, 15)
)

tk.Label(
    card_aggiungi,
    bg="white",
    fg="#64748B",
    font=("Segoe UI", 9, "bold"),
    text="Nome e Cognome"
).pack(
    anchor=tk.W,
    padx=15
)

blocco_nome = tk.Entry(
    card_aggiungi,
    font=("Segoe UI", 11),
    bg="#F8FAFC",
    fg="#1E293B",
    bd=0,
    highlightbackground="#CBD5E1",
    highlightthickness=1
)
blocco_nome.pack(
    fill=tk.X,
    padx=15,
    pady=(5, 12),
    ipady=6
)

tk.Label(
    card_aggiungi,
    bg="white",
    fg="#64748B",
    font=("Segoe UI", 9, "bold"),
    text="Numero di Telefono"
).pack(
    anchor=tk.W,
    padx=15
)

blocco_numero = tk.Entry(
    card_aggiungi,
    font=("Segoe UI", 11),
    bg="#F8FAFC",
    fg="#1E293B",
    bd=0,
    highlightbackground="#CBD5E1",
    highlightthickness=1
)
blocco_numero.pack(
    fill=tk.X,
    padx=15,
    pady=(5, 15),
    ipady=6
)

bottone_aggiungi_numero = tk.Button(
    card_aggiungi,
    text="Salva Contatto",
    command=get_number,
    bg="#3B82F6",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    relief=tk.FLAT,
    cursor="hand2",
    activebackground="#2563EB",
    activeforeground="white"
)
bottone_aggiungi_numero.pack(
    fill=tk.X,
    padx=15,
    ipady=8
)


# Card cerca contatto
card_cerca = tk.Frame(
    colonna_destra,
    bg="white",
    highlightbackground="#E2E8F0",
    highlightthickness=1
)
card_cerca.pack(
    fill=tk.X,
    ipadx=15,
    ipady=15
)

cerca_contatto = tk.Label(
    card_cerca,
    bg="white",
    fg="#1E293B",
    font=("Segoe UI", 11, "bold"),
    text="🔍 CERCA CONTATTO"
)
cerca_contatto.pack(
    anchor=tk.W,
    padx=15,
    pady=(10, 15)
)

spazio_ricerca = tk.Entry(
    card_cerca,
    font=("Segoe UI", 11),
    bg="#F8FAFC",
    fg="#1E293B",
    bd=0,
    highlightbackground="#CBD5E1",
    highlightthickness=1
)
spazio_ricerca.pack(
    fill=tk.X,
    padx=15,
    pady=(0, 8),
    ipady=6
)

# Label usata per mostrare messaggi all'utente
spazio_assenza = tk.Label(
    card_cerca,
    font=("Segoe UI", 9),
    bg="white",
    fg="#EF4444",
    justify="center",
    text=""
)
spazio_assenza.pack(
    fill=tk.X,
    padx=15,
    pady=(0, 8)
)

bottone_ricerca = tk.Button(
    card_cerca,
    text="Cerca",
    command=search_contact,
    font=("Segoe UI", 10, "bold"),
    fg="white",
    relief=tk.FLAT,
    bg="#475569",
    cursor="hand2",
    activebackground="#334155",
    activeforeground="white"
)
bottone_ricerca.pack(
    fill=tk.X,
    padx=15,
    ipady=8
)

card_elimina = tk.Frame(
    colonna_destra,
    bg="white",
    highlightbackground="#E2E8F0",
    highlightthickness=1
)
card_elimina.pack(
    fill=tk.X,
    ipadx=15,
    ipady=15,
    pady=(15, 0) # Un po' di stacco dalla card sopra
)

elimina_titolo = tk.Label(
    card_elimina,
    bg="white",
    fg="#1E293B",
    font=("Segoe UI", 11, "bold"),
    text="🗑️ GESTIONE CONTATTO"
)
elimina_titolo.pack(
    anchor=tk.W,
    padx=15,
    pady=(10, 15)
)

bottone_elimina_contatto = tk.Button(
    card_elimina,
    text="Elimina Contatto Selezionato",
    command=contact_elimination,  # Qui poi collegheremo la tua funzione di eliminazione
    font=("Segoe UI", 10, "bold"),
    fg="white",
    relief=tk.FLAT,
    bg="#EF4444",  # Un bel rosso moderno per indicare l'azione di eliminazione
    cursor="hand2",
    activebackground="#DC2626",
    activeforeground="white",
    state=tk.DISABLED
)
bottone_elimina_contatto.pack(
    fill=tk.X,
    padx=15,
    ipady=8
)
contact_block.bind("<<ListboxSelect>>",activation_button)
root.bind("<Button-1>",reset_button,add="+")



# Avvio dell'interfaccia
root.mainloop()