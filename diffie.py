def generar_clave_publica(g, privada, p):
    return pow(g, privada, p)

def calcular_clave_compartida(clave_publica_otro, mi_privada, p):
    return pow(clave_publica_otro, mi_privada, p)

def demo_sin_mitm(p, g, a_priv, b_priv):
    A_pub = generar_clave_publica(g, a_priv, p)
    B_pub = generar_clave_publica(g, b_priv, p)

    clave_alice = calcular_clave_compartida(B_pub, a_priv, p)
    clave_bob   = calcular_clave_compartida(A_pub, b_priv, p)

    print('--- SIN ATAQUE MITM ---')
    print(f'Clave compartida Alice: {clave_alice}')
    print(f'Clave compartida Bob:   {clave_bob}')
    print(f'¿Iguales? {clave_alice == clave_bob}')
    print()

def demo_con_mitm(p, g, a_priv, b_priv, e_priv_a, e_priv_b):
    A_pub   = generar_clave_publica(g, a_priv, p)
    B_pub   = generar_clave_publica(g, b_priv, p)
    E_pub_a = generar_clave_publica(g, e_priv_a, p)
    E_pub_b = generar_clave_publica(g, e_priv_b, p)

    clave_alice_eve = calcular_clave_compartida(E_pub_a, a_priv, p)
    clave_bob_eve   = calcular_clave_compartida(E_pub_b, b_priv, p)
    clave_eve_alice = calcular_clave_compartida(A_pub, e_priv_a, p)
    clave_eve_bob   = calcular_clave_compartida(B_pub, e_priv_b, p)

    print('--- CON ATAQUE MITM (Eve en el medio) ---')
    print(f'Alice cree compartir con Bob:   {clave_alice_eve}  (en realidad comparte con Eve)')
    print(f'Bob   cree compartir con Alice: {clave_bob_eve}  (en realidad comparte con Eve)')
    print(f'Eve conoce clave con Alice:     {clave_eve_alice}')
    print(f'Eve conoce clave con Bob:       {clave_eve_bob}')
    print(f'¿Alice y Bob tienen la misma clave? {clave_alice_eve == clave_bob_eve}')
    print('¡Alice y Bob NO detectan la intrusión! Eve puede leer todo.')

def demo_diffie_hellman():
    p, g = 23, 5
    a_priv, b_priv = 6, 15
    e_priv_a, e_priv_b = 9, 3

    print(f'Parámetros públicos: p={p}, g={g}')
    print()
    demo_sin_mitm(p, g, a_priv, b_priv)
    demo_con_mitm(p, g, a_priv, b_priv, e_priv_a, e_priv_b)

if __name__ == '__main__':
    demo_diffie_hellman()