from math import gcd
from sympy import mod_inverse


def get_keys():
    value_p = value_q = None
    print('=' * 150 + '\nRecomendamos números primos com 3 dígitos ou mais. Você pode escolher um de sua preferência.')    
    while value_p is None or not check_prime(value_p) or not value_p >= 100:
        try:
            value_p = int(input('Digite um número primo para o valor de P: '))
            if not check_prime(value_p):
                print(f'{value_p} não é primo. Tente novamente...')
            elif not value_p >= 100:
                print('Por motivo de maior segurança, digite um número com 3 dígitos ou mais.')
        except ValueError:
            print('Entrada invalida. Digite apenas números inteiros...')

    while value_q is None or not check_prime(value_q) or value_q == value_p or not value_q >= 100:
        try:
            value_q = int(input('Agora digite um número primo para o valor de Q: '))
            if not check_prime(value_q):
                print(f'{value_q} não é primo. Tente novamente...')
            elif value_q == value_p:
                print('Q e P não podem ser iguais. Tente novamente...')
            elif not value_p >= 100:
                print('Por motivo de maior segurança, digite um número com 3 dígitos ou mais.')
                            
        except ValueError:
            print('Entrada Invalida. Digite apenas números inteiros...')
            
    value_n = value_p * value_q
    value_z = (value_p-1)*(value_q-1)
    print(f'Ótimo, temos os seguintes valores: P = {value_p}; Q = {value_q}; N = {value_n} e Z = {value_z}')

    return value_p, value_q, value_n, value_z


def check_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False        
    return True


def euclides(value_z, value_p, value_q, value_n):
    print('=' *150)
    print('Números primos entre si são números que possuem somente o número 1 como divisor comum entre si.')
    while True:
        try:
            value_e = int(input('Digite um número para E, onde E,Z sejam primos entre si: '))
            if value_e in {value_p, value_q, value_n, value_z}:
                print(f'O valor de E não pode ser igual ao P, Q, N ou Z. Tente novamente.')
            
            elif value_e <= 100:
                print('Por motivo de maior segurança, digite um número com 3 dígitos ou mais.')
            
            else:
                dividend = value_e
                divisor = value_z

                while divisor != 0:
                    rest = dividend % divisor
                    dividend = divisor
                    divisor = rest
                MDC = dividend

                if MDC != 1:
                    print('Não são primos entre si, tente novamente.')
                    continue

                else:
                    print(f'O máximo divisor comum entre E e Z é: {MDC}, portanto, são primos entre si.')
                
                return value_e
        
        except:
            print('Entrada invalida. Digite apenas números inteiros...')


def mod(value_e, value_z):
    print('=' * 150 + '\nVamos encontrar o valor de D agora! Só um instante...')
    value_d = mod_inverse(value_e, value_z)
    print(f'O valor de D é: {value_d}')
    return value_d


def get_message():
    while True:
        pure_message = input('Digite aqui o seu texto claro: ')

        if not len(pure_message) >= 2:
            print('Por favor, digite pelos menos 2 caracteres.')

        else:
            return pure_message
    

def encrypt(pure_message):
    print('=' * 150)
    print('Precisaremos da chave pública para criptografar a mensagem.')

    while True:
        try:
            key_e = int(input('Digite aqui o valor de E: '))
            key_n = int(input('Digite aqui o valor de N: '))
            
            ascii_message = []
            for i in pure_message:
                ascii_message.append(ord(i))

            encrypted_ascii = []
            for i in ascii_message:
                encrypted_ascii.append((i ** key_e) % key_n)
                
            print(f'Você quer transmitir a mensagem: {pure_message}')
            print(f'A mensagem criptografada é: {encrypted_ascii}')
                    
            return encrypted_ascii
        
        except ValueError:
            print('Entrada Inválida. Digite apenas números inteiros...')


def decrypt():
    print('=' * 150)
    while True:
        try:
            encrypted_message = input('Digite o texto criptografado. Por ex.: [XXXX, XXXX, XXXX, XXXX, XXXX]: ')
            if not encrypted_message.startswith('[') or not encrypted_message.endswith(']'):
                print('Entrada inválida. Por favor, digite o seu texto criptografado em formato de lista: ')
                continue

            else:
                key_d = int(input('Vamos precisar que você digite a sua chave privada para descriptografar a mensagem.\nDigite o valor de D: '))
                key_n = int(input('Agora digite o valor de N: '))

                decrypted_ascii = []
                for i in eval(encrypted_message):
                    decrypted_ascii.append((i ** key_d) % key_n)

                decrypted_message = ''
                for ascii in decrypted_ascii:
                    decrypted_message += chr(ascii)
                    
                print(f'Sua mensagem em texto claro é: {decrypted_message}')
                break
                
        except ValueError:
            print('Entrada inválida. Digite apenas números inteiros...')


def main():
    print('='*150 + '\nBEM VINDO AO SISTEMA DE CRIPTOGRAFIA BASEADO EM RSA\n' + 150*'=' )

    while True:
        choice = input('Digite CRIPTOGRAFAR para criptografar um texto ou DESCRIPTOGRAFAR para descriptografar um texto ou SAIR para finalizar o programa: ')
        choice = choice.lower()
        
        if choice in {'c', 'criptografar'}:
            value_p, value_q, value_n, value_z = get_keys()
            value_e = euclides(value_z, value_p, value_q, value_n)
            value_d = mod(value_e, value_z)
            print('=' * 150 + f'\n • Sua chave privada é: {value_d, value_n}\n • Sua chave pública é: {value_e, value_n}')
            print('=' * 150)
            pure_message = get_message()
              
            encrypted_ascii = encrypt(pure_message)

            print('=' * 150)
            choice_decrypted = input('Você deseja descriptografar a mensagem que você acabou de criptografar? (sim para continuar ou qualquer tecla para finalizar): ')
            if choice_decrypted.lower() in {'s', 'sim'}:
                decrypt()
                  
            else:
                print('Programa finalizado!')

        elif choice in {'d', 'descriptografar'}:
            decrypt()
                

        elif choice in {'s', 'sair'}:
            print('Programa finalizado')
            break
            
        else:
            print('Entrada inválida. Tente novamente para continuarmos.')

if __name__ == '__main__':
    main()
