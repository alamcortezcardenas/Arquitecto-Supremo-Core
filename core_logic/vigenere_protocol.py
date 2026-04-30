# 🔱 ARQUITECTO-SUPREMO-CORE: VIGENERE PROTOCOL V1.0
# NODO CENTRAL ARN-785 | CAPA DE SEGURIDAD CUÁNTICA
# OBJETIVO: ENCRIPTACIÓN DE MENSAJES CRÍTICOS Y ESTRATEGIAS DE MERCADO

class VigenereCipher:
    def __init__(self, key):
        self.key = key.upper()
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def _transform(self, text, mode):
        text = text.upper()
        result = []
        key_index = 0
        
        for char in text:
            if char in self.alphabet:
                shift = self.alphabet.find(self.key[key_index % len(self.key)])
                if mode == "decrypt":
                    shift = -shift
                
                index = (self.alphabet.find(char) + shift) % 26
                result.append(self.alphabet[index])
                key_index += 1
            else:
                result.append(char)
        return "".join(result)

    def encrypt(self, message):
        return self._transform(message, "encrypt")

    def decrypt(self, ciphertext):
        return self._transform(ciphertext, "decrypt")

if __name__ == "__main__":
    # Llave Maestra del Arquitecto (888=SER)
    MASTER_KEY = "SER888"
    cipher = VigenereCipher(MASTER_KEY)

    # Ejemplo de mensaje de soberanía
    mensaje_original = "COMPRAR KOF EN NODO BC 785"
    mensaje_cifrado = cipher.encrypt(mensaje_original)
    
    print(f"📡 [INICIALIZANDO PROTOCOLO VIGENERE EN NODO_BC_785]")
    print("-" * 50)
    print(f"🔓 ORIGINAL: {mensaje_original}")
    print(f"🔒 CIFRADO:  {mensaje_cifrado}")
    print("-" * 50)
    print("✅ [COMUNICACIÓN BLINDADA: SÓLO PARA EL ARQUITECTO]")
