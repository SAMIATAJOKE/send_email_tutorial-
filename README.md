k# 🎉 Birthday Email Sender

A Python application that generates and sends personalized, beautifully formatted HTML birthday emails via Gmail SMTP.

## 📸 Output Example

![Birthday Email Screenshot](WhatsApp%20Image%202026-06-17%20at%2012.59.09%20PM.jpeg)

The email features:
- Gradient header banner with birthday emojis
- Personalized greeting with recipient's name
- Responsive HTML design that works across email clients
- Professional styling with proper spacing and typography
- Decorative footer with celebratory emojis

## ✨ Features

- **Personalized Emails**: Automatically replaces recipient and sender names in email templates
- **HTML Email Templates**: Creates beautifully styled HTML emails with inline CSS
- **Gmail Integration**: Sends emails directly via Gmail SMTP (supports App Passwords)
- **Environment Configuration**: Securely stores credentials in `.env` file
- **Customizable Templates**: Easy-to-modify text template for birthday messages
- **MIME Multi-part Support**: Includes both plain text and HTML versions for compatibility

## 📁 Project Structure

```
sendmail/
├── app.py                           # Main entry point - orchestrates the email sending
├── build_html.py                    # Converts plain text messages into styled HTML emails
├── send.py                          # Handles SMTP connection and email delivery
├── utils.py                         # Utility functions: file reading, text substitution
├── main.ipynb                       # Jupyter notebook for interactive testing
├── data/
│   ├── Birthday_Wish_Template.txt   # Template text for birthday messages
│   └── products.csv                 # Sample product data (reference)
├── .env                             # Environment variables (credentials - not in git)
└── README.md                        # This file
```

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.7+
- Gmail account with an [App Password](https://myaccount.google.com/apppasswords) (2FA enabled)

### Installation

1. **Clone or navigate to the project folder**
   ```bash
   cd sendmail
   ```

2. **Install dependencies**
   ```bash
   pip install python-dotenv
   ```

3. **Create `.env` file** in the project root:
   ```
   my_email=your-email@gmail.com
   my_password=your-app-password
   ```

   > ⚠️ **Important**: Use a Gmail App Password, not your regular password. Generate one [here](https://myaccount.google.com/apppasswords) if you have 2FA enabled.

## 🚀 Usage

### Basic Example

```python
python app.py
```

### Customization

Edit `data/Birthday_Wish_Template.txt` to customize the birthday message:
- Replace `{name}` with the recipient's name placeholder
- Replace `[Your Name]` with your name

### Sending Multiple Emails

Modify `app.py` to loop through recipients:

```python
recipients = [
    {"email": "john@example.com", "name": "John"},
    {"email": "jane@example.com", "name": "Jane"},
]

for recipient in recipients:
    content = modify(read_file("data/Birthday_Wish_Template.txt"), recipient["name"], "Your Name")
    html = build_birthday_email(name=recipient["name"], body_text=content, sender_name="Your Name")
    send_birthday_email(
        recipient["email"], 
        f"Happy Birthday, {recipient['name']}! 🎉", 
        html,
        email, 
        my_password
    )
```

## 📝 File Descriptions

### `app.py`
Main entry point that orchestrates the entire workflow:
- Reads the template from file
- Personalizes the message
- Builds the HTML email
- Sends the email via SMTP

### `build_html.py`
Converts plain text messages into professional HTML emails:
- Parses paragraphs from plain text
- Applies inline CSS styling
- Creates responsive table-based layout
- Adds decorative header and footer with emojis

### `send.py`
Handles SMTP email delivery:
- Configures Gmail SMTP settings
- Creates MIME multi-part messages
- Supports both HTML and plain text fallback
- Handles TLS encryption

### `utils.py`
Utility functions:
- `read_file()`: Reads template files
- `modify()`: Replaces placeholders with actual names
- `email`, `my_password`: Environment variables from `.env`

## 🎨 Customization Tips

### Change Email Styling
Edit the HTML template in `build_html.py`:
- Modify gradient colors: `#ff7e5f`, `#feb47b`, `#ff6a88`
- Adjust spacing: `padding:40px`
- Change fonts or text sizes

### Add Images to Email
Update the HTML in `build_html.py` to include:
```html
<img src="https://example.com/image.png" width="300" alt="Birthday Gift">
```

### Send from Different Email
Update `.env`:
```
my_email=different-email@gmail.com
my_password=app-password-for-different-email
```

## ⚙️ Technical Details

- **Email Format**: MIME multi-part (plain text + HTML)
- **SMTP Server**: Gmail (smtp.gmail.com:587)
- **Security**: TLS encryption with App Password authentication
- **Character Encoding**: UTF-8 for international characters

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| "Login failed" | Ensure you're using an App Password, not your Gmail password |
| ".env not found" | Create `.env` file in the project root with your credentials |
| Emails not styled | Check that recipient's email client supports HTML; plain text fallback is included |
| Template not found | Ensure `data/Birthday_Wish_Template.txt` path is correct |

## 📧 Sending Tips

- **Best Time**: Send emails at reasonable hours in the recipient's timezone
- **Batch Sending**: Add delays between emails to avoid rate limiting
- **Testing**: Use your own email first to verify formatting

## 🔐 Security

- **Never commit `.env`** to version control (add to `.gitignore`)
- **Use App Passwords** instead of your main Gmail password
- **Rotate credentials** regularly if shared

## 📚 Resources

- [Gmail App Passwords](https://myaccount.google.com/apppasswords)
- [Python Email MIME Documentation](https://docs.python.org/3/library/email.mime.html)
- [SMTP Protocol](https://tools.ietf.org/html/rfc5321)

## 📄 License

This project is open source and available for personal use.

---

**Made with ❤️ for special birthday celebrations!**
