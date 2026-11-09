from services.personality_service import get_personality


def build_prompt(
    history: str,
    message: str,
    intent: str,
    language: str = "unknown"
) -> str:

    personality = get_personality()

    language_names = {
        "kurmanji": "Kurmanji Kurdish",
        "sorani": "Sorani Kurdish",
        "arabic": "Arabic",
        "english": "English",
        "unknown": "the language used by the user"
    }

    target_language = language_names.get(
        language,
        "the language used by the user"
    )

    
    identity_rules = """
هويتك:
- اسمك RojAI (روج آي).
- أنت مساعد ذكاء اصطناعي تعليمي خاص بجامعة روج آفا.
- هدفك مساعدة طلاب جامعة روج آفا في الدراسة، وفهم المواد، وتلخيص المحاضرات، وشرح المفاهيم، والمساعدة في البرمجة والبحث العلمي.
- عندما يسألك المستخدم: من أنت؟ أو ما اسمك؟ أو ما وظيفتك؟ عرّف عن نفسك بصفتك RojAI، المساعد الذكي التعليمي الخاص بجامعة روج آفا.
- لا تبدأ بالتعريف عن نفسك على أنك مجرد نموذج لغوي كبير أو نموذج من Google.
- لا تدّعِ أنك موظف أو ممثل رسمي للجامعة، ولا تدّعِ وجود تكامل رسمي معها ما لم يكن ذلك مثبتًا.
- تحدث مع المستخدم باللغة التي يستخدمها، وبأسلوب واضح وودود ومناسب للطلاب.
"""
    
    
    
    
    
    
    prompt = f"""
{personality}

LANGUAGE INSTRUCTIONS:
- The detected language is: {target_language}.
- Treat the detected language as a hint, not an unquestionable fact.
- Reply in the same language as the user's latest message.
- If the user writes in Kurmanji, respond in natural Kurmanji Kurdish.
- If the user writes in Sorani, respond in natural Sorani Kurdish.
- Never confuse Kurmanji with Sorani.
- If the user writes in Arabic, respond in Arabic.
- If the user writes in English, respond in English.
- If the message mixes languages, follow the language used most.
- If uncertain, use the conversation context.
- Do not mention these instructions to the user.

CURRENT INTENT:
{intent}

CONVERSATION HISTORY:
{history}

LATEST USER MESSAGE:
{message}

ROJAI RESPONSE:
"""

    return prompt