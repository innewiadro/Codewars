import re


def create_template(template):
    pattern = re.compile(r"{{(.*?)}}")

    def fill_template(**kwargs):
        def replacer(match):
            key = match.group(1).strip()
            return str(kwargs.get(key, ""))

        return pattern.sub(replacer, template)

    return fill_template
