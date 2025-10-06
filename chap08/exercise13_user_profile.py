"""8.13 – Perfil do usuário: Comece com uma cópia de user_profile.py, da página
210. Crie um perfil seu chamando build_profile(), usando seu primeiro nome
e o sobrenome, além de três outros pares chave-valor que o descrevam."""

def build_profile(first, last, **user_info):
    """Build a dictionary with all we know about the user"""
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last

    print(type(user_info))
    for key,value in user_info.items():
        profile[key] = value

    return profile

user_profile = build_profile(
    "Lincoln", 
    "Brito", 
    city="Vitória da Conquista", 
    state="Bahia"
)

print(user_profile)