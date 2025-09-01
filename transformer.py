import re
from datetime import datetime

def transform_text(input_text: str) -> str:
    text = input_text
    # 1. Redact phone numbers
    text = re.sub(r'\b\d{5}[- ]?\d{5}\b', '[REDACTED]', text)

    # 2. Convert dates YYYY-MM-DD → human readable
    def replace_date(match):
        date_str = match.group()
        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            day = date_obj.day
            suffix = "th" if 11 <= day <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
            return f"{day}{suffix} {date_obj.strftime('%B %Y')}"
        except ValueError:
            return date_str

    text = re.sub(r'\b\d{4}-\d{2}-\d{2}\b', replace_date, text)

    # 3. Easter egg
    text = text.replace("Python", "🐍")

    return text


if __name__ == "__main__":
    user_input = input("Enter a paragraph: ")
    print("\nTransformed text:\n")
    print(transform_text(user_input))
