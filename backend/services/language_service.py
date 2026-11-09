def detect_language(text: str) -> str:
    text = (text or "").strip()

    if not text:
        return "unknown"

    words = {
        word.strip(".,!?;:()[]{}").lower()
        for word in text.split()
    }

    # Kurmanji Kurdish
    kurmanji_chars = set("çÇêÊîÎşŞûÛ")
    kurmanji_words = {
        "silav", "çawa", "spas", "baş", "başî",
        "ez", "tu", "em", "kurdî", "rojbaş",
        "heval", "dikim", "çima"
    }

    if any(char in kurmanji_chars for char in text):
        return "kurmanji"

    if words & kurmanji_words:
        return "kurmanji"

    # Sorani Kurdish or Arabic
    has_arabic_script = any(
        "\u0600" <= char <= "\u06FF"
        for char in text
    )

    if has_arabic_script:
        sorani_markers = {
            "سڵاو", "چۆن", "باشی", "کوردی",
            "دەکات", "دەتوانم", "زۆر"
        }

        sorani_chars = set("ڕڵێۆە")

        if words & sorani_markers or any(
            char in sorani_chars for char in text
        ):
            return "sorani"

        return "arabic"

    # English
    english_words = {
        "the", "is", "are", "what", "how", "why",
        "hello", "help", "please", "can", "you",
        "explain", "write", "code", "with", "for",
        "this", "that", "and", "my"
    }

    if words & english_words:
        return "english"

    if any(char.isalpha() for char in text):
        return "english"

    return "unknown"