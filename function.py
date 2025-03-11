import re

def func(text): #
    bs = re.split(r"\n\s*\n", text.strip()) # разбиваем текст на блоки
    vcs = []

    for b in bs:
        m = re.search(r"^(.+?)\n", b)
        if m:
            title = m.group(1).strip()

        m2 = re.search(r"зарплат[а-я]*\s*[:–-]?\s*([\d\s₽руб\.]+)", b, re.IGNORECASE)
        if m2:
            salary = m2.group(1).strip()
        else:
            salary = "не указана"

        m3 = re.search(r"Контакты:\s*([\w.-]+@[\w.-]+\.\w+)", b, re.IGNORECASE)
        if m3:
            contacts = m3.group(1).strip()
        else:
            contacts = "не указаны"

        vc_info = {
            "title": title,
            "salary": salary,
            "contacts": contacts,
            "description": b.strip(),
        }
        vcs.append(vc_info)

    return vcs
