import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Conectarea la baza de date SQLite
conn = sqlite3.connect('feedback.db')

# Crearea tabelului pentru stocarea feedback-ului
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS feedback
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             rating1 INT,
             rating2 INT,
             rating3 INT,
             rating4 INT,
             comment TEXT)''')

# Crearea ferestrei principale a programului
root = tk.Tk()
root.title("Chestionar de satisfactie")

# Crearea etichetelor și casetelor de selectare pentru evaluare
rating_label = ttk.Label(root, text="Evaluati serviciile noastre:")
rating_label.pack(side=tk.TOP, pady=10)

rating_var = tk.IntVar()
rating_frame = ttk.Frame(root)
rating_frame.pack(side=tk.TOP)

for i in range(1, 6):
    rating_btn = ttk.Radiobutton(rating_frame, text=str(i), variable=rating_var, value=i)
    rating_btn.pack(side=tk.LEFT, padx=5)

#incercarea mea
# Crearea etichetelor și casetelor de selectare pentru evaluare
rating2_label = ttk.Label(root, text="Pe o scara de la 1 la 5, cat de probabil este sa recomanzi magazinul nostru prietenilor tai sau familiei tale?")
rating2_label.pack(side=tk.TOP, pady=10)

rating2_var = tk.IntVar()
rating2_frame = ttk.Frame(root)
rating2_frame.pack(side=tk.TOP)

for i in range(1, 6):
    rating2_btn = ttk.Radiobutton(rating2_frame, text=str(i), variable=rating2_var, value=i)
    rating2_btn.pack(side=tk.LEFT, padx=5)
#intrebarea 3
rating3_label = ttk.Label(root, text="Pe o scara de la 1 la 5, cat de usor a fost sa gasesti ceea ce cautai in magazinul nostru?")
rating3_label.pack(side=tk.TOP, pady=10)

rating3_var = tk.IntVar()
rating3_frame = ttk.Frame(root)
rating3_frame.pack(side=tk.TOP)

for i in range(1, 6):
    rating3_btn = ttk.Radiobutton(rating3_frame, text=str(i), variable=rating3_var, value=i)
    rating3_btn.pack(side=tk.LEFT, padx=5)


#intrebarea 4
rating4_label = ttk.Label(root, text="De unde a-ti auzit de magazinul nostru?")
rating4_label.pack(side=tk.TOP, pady=10)

rating4_var = tk.IntVar()
rating4_frame = ttk.Frame(root)
rating4_frame.pack(side=tk.TOP)


rating4_btn = ttk.Radiobutton(rating4_frame, text="Social media", variable=rating4_var, value=1)
rating4_btn.pack(side=tk.LEFT, padx=5)
rating4_btn = ttk.Radiobutton(rating4_frame, text="Prieteni/familie", variable=rating4_var, value=2)
rating4_btn.pack(side=tk.LEFT, padx=5)
rating4_btn = ttk.Radiobutton(rating4_frame, text="Reclame", variable=rating4_var, value=3)
rating4_btn.pack(side=tk.LEFT, padx=5)


# Crearea etichetei și casetei de text pentru comentariu
comment_label = ttk.Label(root, text="Lasati un comentariu (optional):")
comment_label.pack(side=tk.TOP, pady=10)

comment_text = tk.Text(root, height=5)
comment_text.pack(side=tk.TOP, padx=10, pady=5)

# Funcția pentru trimiterea feedback-ului și stocarea acestuia în baza de date
def send_feedback():
    rating = rating_var.get()
    rating2 = rating2_var.get()
    rating3 = rating3_var.get()
    rating4 = rating4_var.get()

    comment = comment_text.get("1.0", tk.END)

    if rating == 0:
        messagebox.showerror("Eroare", "Va rugam sa selectati o evaluare.")
        return

    c.execute("INSERT INTO feedback (rating, rating2, rating3, rating4, comment) VALUES (?, ?)", (rating,rating2,rating3,rating4, comment))
    conn.commit()
    messagebox.showinfo("Multumim!", "Feedback-ul dvs. a fost inregistrat.")

    # Resetarea casetelor de selectare și de text după trimiterea feedback-ului
    rating_var.set(0)
    comment_text.delete("1.0", tk.END)

# Crearea butonului de trimitere a feedback-ului
submit_button = ttk.Button(root, text="Trimite feedback-ul", command=send_feedback)
submit_button.pack(side=tk.TOP, pady=10)

# Pornirea buclei principale a ferestrei
root.mainloop()

# Închiderea conexiunii la baza de date la închiderea programului
conn.close()
