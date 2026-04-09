# Replace the "ANSWER HERE" for your answer

def number_to_month(month):
    
    meses = [
        "enero", "febrero", "marzo", "abril", 
        "mayo", "junio", "julio", "agosto", 
        "septiembre", "octubre", "noviembre", "diciembre"
    ]

    if month >= 1 and month <= 12:
        return meses[month - 1]
    else:
        return "error" 