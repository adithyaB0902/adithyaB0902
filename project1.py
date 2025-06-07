import tkinter as tk
import random

quotes_by_topic = {
    "Love": [
        "Love is composed of a single soul inhabiting two bodies. – Aristotle",
        "To love and be loved is to feel the sun from both sides. – David Viscott",
        "Love is when the other person’s happiness is more important than your own. – H. Jackson Brown Jr."
    ],
    "Forgiveness": [
        "Forgiveness is the fragrance the violet sheds on the heel that has crushed it. – Mark Twain",
        "The weak can never forgive. Forgiveness is the attribute of the strong. – Mahatma Gandhi",
        "Forgive others not because they deserve forgiveness, but because you deserve peace."
    ],
    "Wisdom": [
        "Knowing yourself is the beginning of all wisdom. – Aristotle",
        "Turn your wounds into wisdom. – Oprah Winfrey",
        "It is not the knowing that is difficult, but the doing. – Chinese Proverb"
    ],
    "Courage": [
        "Courage doesn’t always roar. Sometimes courage is the quiet voice at the end of the day saying, ‘I will try again tomorrow.’",
        "It takes courage to grow up and become who you really are. – E.E. Cummings",
        "Courage is resistance to fear, mastery of fear, not absence of fear. – Mark Twain"
    ],
    "Growth": [
        "Strength and growth come only through continuous effort and struggle. – Napoleon Hill",
        "Growth is painful. Change is painful. But nothing is as painful as staying stuck somewhere you don’t belong.",
        "Life is growth. If we stop growing, technically and spiritually, we are as good as dead. – Morihei Ueshiba"
    ],
    "Peace": [
        "Peace begins with a smile. – Mother Teresa",
        "You’ll never find peace of mind until you listen to your heart.",
        "Peace cannot be kept by force. It can only be achieved by understanding. – Albert Einstein"
    ]
}

all_quotes = [q for topic in quotes_by_topic.values() for q in topic]
random.shuffle(all_quotes)
quote_index = 0

root = tk.Tk()
root.title("Purple Quotes")
root.geometry("1000x500")
root.configure(bg='#6a0dad')

quote_label = tk.Label(root, text="", font=("edu SA hand", 18, "italic"), wraplength=900, justify="center", bg='#6a0dad', fg='white')
quote_label.pack(pady=60)

topic_label = tk.Label(root, text="", font=("edu SA hand", 14, "bold"), bg='#6a0dad', fg='lavender')
topic_label.pack()

def next_quote():
    global quote_index
    if quote_index >= len(all_quotes):
        quote_label.config(text="its your day make it happen")
        topic_label.config(text="")
        return
    quote = all_quotes[quote_index]
    quote_index += 1
    quote_label.config(text=quote)
    for topic, group in quotes_by_topic.items():
        if quote in group:
            topic_label.config(text=f"Topic: {topic}")
            break

next_btn = tk.Button(root, text="🎧 Next Inspiration", command=next_quote, font=("edu SA hand", 30), bg='lavender', fg='#6a0dad', relief="raised", padx=20, pady=10)
next_btn.pack(pady=20)

next_quote()
root.mainloop()