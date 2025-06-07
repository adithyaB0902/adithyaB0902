import tkinter as tk
import random
import pygame

# Initialize pygame mixer for music
pygame.mixer.init()
pygame.mixer.music.load("coffee-lofi-lofi-music-340017.mp3")
pygame.mixer.music.play(-1)

# Quotes dictionary
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

happy_messages = [
    "Keep smiling, it makes you attractive!", "You’re doing great, keep going!", "Today is your fresh start!",
    "Positive vibes only 🌈", "You're someone's reason to smile!", "Shine bright like the whole universe is yours!",
    "Be the sunshine in someone’s cloudy day!", "Life is better when you're laughing.",
    "Smile more, worry less 💜", "You are magic. Don’t ever apologize for the fire in you!",
    "Let your smile change the world!", "Celebrate every tiny victory.", "Turn the pain into power.",
    "Gratitude turns what we have into enough.", "The best is yet to come!", "Surround yourself with what makes you happy."
] * 4  # Makes approx. 50 messages

all_quotes = [q for topic in quotes_by_topic.values() for q in topic]
random.shuffle(all_quotes)
quote_index = 0
msg_index = 0

root = tk.Tk()
root.title("Aesthetic Purple Quotes")
root.geometry("1000x600")
root.configure(bg='#6a0dad')

# Labels
quote_label = tk.Label(root, text="", font=("Comic Sans MS", 18, "italic"), wraplength=900,
                       justify="center", bg='#6a0dad', fg='white')
quote_label.pack(pady=40)

happy_label = tk.Label(root, text="", font=("Verdana", 14, "bold"), bg='#6a0dad', fg='lavender')
happy_label.pack()

# Button with animation
def pulse():
    current_color = next_btn.cget("bg")
    next_color = 'thistle' if current_color == 'lavender' else 'lavender'
    next_btn.config(bg=next_color)
    root.after(800, pulse)

next_btn = tk.Button(root, text="🎧 Next Inspiration", font=("Helvetica", 16), bg='lavender',
                     fg='#6a0dad', relief="raised", padx=20, pady=10)
next_btn.pack(pady=20)
pulse()

# Animation function for fade-in effect
def fade_in_text(label, text, step=0):
    if step == 0:
        label.config(text="")  # clear first

    if step <= len(text):
        label.config(text=text[:step])
        root.after(20, fade_in_text, label, text, step + 1)

def next_quote():
    global quote_index, msg_index

    if quote_index >= len(all_quotes):
        fade_in_text(quote_label, "It's your day — make it happen! 💫")
    else:
        fade_in_text(quote_label, all_quotes[quote_index])
        quote_index += 1

    fade_in_text(happy_label, happy_messages[msg_index])
    msg_index = (msg_index + 1) % len(happy_messages)

next_btn.config(command=next_quote)
next_quote()

root.mainloop()
