class TranslationAgent:

    def translate_content(self, content, language="English"):

        return {
            "language": language,
            "content": f"[{language} version] {content}"
        }
