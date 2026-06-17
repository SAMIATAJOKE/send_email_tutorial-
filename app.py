from utils import email, my_password, modify, read_file
from build_html import build_birthday_email
from send import send_birthday_email
import os

print(email) 

def main():
    content = modify(read_file("data/Birthday_Wish_Template.txt"), "Eniola", "Samiat")
    # print(content)
    html = build_birthday_email(name="Eniola", body_text=content, sender_name="Samiat")
    # print(html)
    send_birthday_email("eniolaraheem6@gmail.com", "Happy Birthday, Eniola! 🎉", html,  "harunsamiat@gmail.com", os.getenv("my_password"))

main() 