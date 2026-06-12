"""Tkinter user interface for the weather app."""

import tkinter as tk
from tkinter import messagebox

from weather_app.weather_client import WeatherLookupError, fetch_weather_report


class WeatherApp:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.root = tk.Tk()
        self.city_entry: tk.Entry
        self.result_label: tk.Label
        self._build_window()

    def run(self) -> None:
        self.root.mainloop()

    def _build_window(self) -> None:
        self.root.geometry("320x300")
        self.root.minsize(320, 300)
        self.root.maxsize(420, 420)
        self.root.title("Clima")
        self.root.configure(background="light blue")

        title_label = tk.Label(
            self.root,
            text="Verificador de Clima",
            font=("Comic Sans MS", 20),
            bg="light blue",
        )
        title_label.pack(pady=10)

        city_prompt_label = tk.Label(
            self.root,
            text="Qual local?",
            font=("Arial", 10),
            bg="light blue",
        )
        city_prompt_label.pack(pady=10)

        self.city_entry = tk.Entry(self.root)
        self.city_entry.pack()
        self.city_entry.bind("<Return>", lambda _event: self.show_weather_report())

        search_button = tk.Button(
            self.root,
            text="Ver clima",
            command=self.show_weather_report,
            bg="dark red",
            fg="white",
        )
        search_button.pack(pady=10)

        self.result_label = tk.Label(
            self.root,
            text="",
            justify=tk.LEFT,
            bg="light blue",
            font=("Arial", 15),
        )
        self.result_label.pack()

        footer_label = tk.Label(
            self.root,
            text="feito por preyzin",
            font=("Comic Sans MS", 8),
            bg="light blue",
            fg="purple",
        )
        footer_label.pack(side="bottom", pady=10)

    def show_weather_report(self) -> None:
        city = self.city_entry.get()

        try:
            report = fetch_weather_report(city, self.api_key)
        except WeatherLookupError as exc:
            messagebox.showerror("Erro", str(exc))
            return

        self.result_label.config(
            text=(
                f"Cidade: {report.city}\n"
                f"Temperatura: {report.temperature_celsius}°C\n"
                f"Descrição: {report.description}"
            )
        )
