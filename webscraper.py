import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk

class WebScraperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Scraper")
        self.root.geometry("400x300")

        self.create_widgets()

    def scrape_website(self):
        url = self.url_entry.get()
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                # Modify the code below to extract the desired information from the website
                # For example, you can find all the links on the page:
                links = soup.find_all('a')
                for link in links:
                    self.result_text.insert(tk.END, link.get('href') + '\n')
            else:
                self.result_text.insert(tk.END, f"Failed to retrieve content. Status code: {response.status_code}\n")
        except Exception as e:
            self.result_text.insert(tk.END, f"Error: {e}\n")

    def create_widgets(self):
        ttk.Label(self.root, text="Enter Website URL:").pack(pady=10)
        self.url_entry = ttk.Entry(self.root, width=40)
        self.url_entry.pack(pady=10)

        scrape_button = ttk.Button(self.root, text="Scrape Website", command=self.scrape_website)
        scrape_button.pack(pady=10)

        self.result_text = tk.Text(self.root, height=10, width=40)
        self.result_text.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = WebScraperApp(root)
    root.mainloop()
