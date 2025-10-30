#2.1 Congruences and Cancellation conditions


# %%
#2.2 Euler's Totient and Theorem


# %%
#2.3 Extended Euclid for Inverses

# %%
#2.4 Chinese Remainder Theorem (CRT) | Stegvis

#(rest, modulus)
ligninger = [
#(a, b) hvor x=a(mod b)
    (2, 3),  #x≡2(mod 3)
    (3, 5),  #x≡3(mod 5)
    (2, 7),  #x≡2(mod 7)
]

def utvided_euklid(a, b):
    """Finner x slik at a*x ≡ 1 (mod b)"""
    if b == 0:
        return 1, 0

    x1, y1 = utvided_euklid(b, a % b)
    x = y1
    y = x1 - (a // b) * y1

    return x, y


def los_crt(ligninger):
    #Steg 1: Regn ut N (produktet av alle modulier)
    N = 1
    for rest, modulus in ligninger:
        N *= modulus

    print(f"Steg 1: N = {N}\n")

    #Steg 2: Regn ut løsningen
    x = 0

    for i, (rest, modulus) in enumerate(ligninger, 1):
        Ni = N // modulus
        Mi, _ = utvided_euklid(Ni, modulus)
        bidrag = rest * Ni * Mi

        print(f"Ligning {i}: x ≡ {rest} (mod {modulus})")
        print(f"  N_{i} = {Ni}")
        print(f"  M_{i} = {Mi}")
        print(f"  Bidrag = {rest} × {Ni} × {Mi} = {bidrag}")
        print()
        x += bidrag

    #Steg 3: Reduser til minste positive løsning
    x = x % N

    return x, N

print("Chinese Remainder Theorem eksempel\n")
losning, N = los_crt(ligninger)


print(f"LØSNING: x = {losning}")

print()

#Verifiser løsningen
print("Verifisering:")
for rest, modulus in ligninger:
    beregnet_rest = losning % modulus
    print(f"  {losning} mod {modulus} = {beregnet_rest} (forventer {rest})")

print()
print(f"Generell løsning: x = {losning} + {N}k, der k er et heltall")


# %%




# %%


