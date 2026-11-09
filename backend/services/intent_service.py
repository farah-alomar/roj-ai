def detect_intent(message: str) -> str:
    text = message.lower()

    programming = [
        "python", "java", "javascript", "c++", "c#", "html", "css",
        "sql", "api", "fastapi", "react", "flutter",
        "برمجة", "كود", "برنامج", "شفرة"
    ]

    translation = [
        "ترجم", "ترجمة", "translate"
    ]

    math = [
        "احسب", "حل", "معادلة", "تكامل", "اشتقاق", "رياضيات", "calculate"
    ]

    if any(word in text for word in programming):
        return "programming"

    if any(word in text for word in translation):
        return "translation"

    if any(word in text for word in math):
        return "math"

    return "general"