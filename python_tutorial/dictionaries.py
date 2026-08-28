monthConversions = {
    "jan": "January",
    "feb": "February",
    "mar": "March",
    "apr": "April",
    "may": "May",
    "jun": "June",
    "jul": "July",
    "aug": "August",
    "Sep": "September",
    "oct": "October",
    "nov": "November",
    "dec": "December",
    }
try:
    print(monthConversions[input('Introduce un mes: ').lower()])
except KeyError:
    print('Mes no valido')

# print(monthConversions["nov"])
# print(monthConversions.get("luv", "Not a valid key"))
