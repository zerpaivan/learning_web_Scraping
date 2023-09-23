import re
the_regex= re.compile(r'[A-Za-z0-9\._+]+@[A-Za-z]+\.(com|org|edu|net)')
texto = '''
nana@gmail.com
jesus@hotmail.net
lalita@outlook.com'''
mo = the_regex.findall(texto)
print(mo)

# -------------------
print('*************************************')
x_regex = re.compile(r'(?:agente) (\w)\w*')
cadena = 'La agente Maria y el agente Jesus se lograron infiltrar'

nuevacadena = x_regex.sub(r'xxx', cadena)

print(nuevacadena)

texto3 = 'ana COME ManGo'
res_str = re.sub(r'[A-Z]', lambda x:x.group().lower() if x is not None else None, texto3)
print(res_str)

# excluir una palabra de la busqueda
texto = "Este es un ejemplo de texto. Quiero excluir la palabra 'ejemplo'."
patron = r"\bejemplo\b"

# Buscar todas las palabras que no coincidan con el patrón
resultado = re.findall(rf"\b(?!{patron})\w+\b", texto)

print(resultado)
