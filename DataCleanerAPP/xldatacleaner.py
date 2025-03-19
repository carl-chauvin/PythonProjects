import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

class DataCleanerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Limpieza de Datos")
        self.root.geometry("400x250")

        # Botón para cargar archivo
        self.btn_cargar = tk.Button(root, text="Cargar Archivo", command=self.cargar_archivo)
        self.btn_cargar.pack(pady=10)

        # Botón para limpiar datos
        self.btn_limpiar = tk.Button(root, text="Limpiar Datos", command=self.limpiar_datos, state=tk.DISABLED)
        self.btn_limpiar.pack(pady=10)

        # Botón para exportar
        self.btn_exportar = tk.Button(root, text="Exportar Datos", command=self.exportar_datos, state=tk.DISABLED)
        self.btn_exportar.pack(pady=10)

        self.df = None  # Almacena el DataFrame

    def cargar_archivo(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx;*.xls")])
        if file_path:
            try:
                if file_path.endswith(".csv"):
                    self.df = pd.read_csv(file_path)
                else:
                    self.df = pd.read_excel(file_path)

                messagebox.showinfo("Éxito", "Archivo cargado correctamente.")
                self.btn_limpiar.config(state=tk.NORMAL)
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo cargar el archivo.\n{str(e)}")

    def limpiar_datos(self):
        if self.df is not None:
            self.df.drop_duplicates(inplace=True)  # Eliminar duplicados
            self.df.fillna(0, inplace=True)  # Rellenar valores faltantes con 0
            self.df.dropna(thresh=len(self.df.columns) // 2, inplace=True)  # Eliminar filas con más del 50% de valores nulos
            self.df.columns = [col.strip().lower().replace(" ", "_") for col in self.df.columns]  # Normalizar nombres de columnas
            
            messagebox.showinfo("Éxito", "Datos limpiados correctamente.")
            self.btn_exportar.config(state=tk.NORMAL)

    def exportar_datos(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                                 filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx")])
        if file_path:
            try:
                if file_path.endswith(".csv"):
                    self.df.to_csv(file_path, index=False)
                else:
                    self.df.to_excel(file_path, index=False)

                messagebox.showinfo("Éxito", "Datos exportados correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo exportar el archivo.\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DataCleanerApp(root)
    root.mainloop()
