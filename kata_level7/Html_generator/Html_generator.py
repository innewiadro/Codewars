class HTMLGen:
    @staticmethod
    def a(text): return f"<a>{text}</a>"

    @staticmethod
    def b(text): return f"<b>{text}</b>"

    @staticmethod
    def p(text): return f"<p>{text}</p>"

    @staticmethod
    def body(text): return f"<body>{text}</body>"

    @staticmethod
    def div(text): return f"<div>{text}</div>"

    @staticmethod
    def span(text): return f"<span>{text}</span>"

    @staticmethod
    def title(text): return f"<title>{text}</title>"

    @staticmethod
    def comment(text): return f"<!--{text}-->"