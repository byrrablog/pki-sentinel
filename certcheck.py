# ---------------------------------------------------------
# Tool: CKMS Expiry Scanner v1.2 (Interactive & Portable)
# Author: Bayron Cares
# Description: X.509 parser with portable logging
# ---------------------------------------------------------

import datetime
import logging
import os
from cryptography import x509
from cryptography.hazmat.backends import default_backend

# 1. Configuración de rutas automáticas
ruta_script = os.path.dirname(os.path.abspath(__file__))
ruta_log = os.path.join(ruta_script, 'pki_audit.log')

# 2. Configuración del Logger (Revisa que cierren todos los paréntesis)
logging.basicConfig(
    filename=ruta_log,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def analizar_certificado(ruta_archivo):
    # Limpiar la ruta por si se arrastra el archivo
    ruta_archivo = ruta_archivo.strip().replace("'", "").replace('"', "")

    if not os.path.exists(ruta_archivo):
        print(f"❌ Error: El archivo '{ruta_archivo}' no existe.")
        return

    try:
        with open(ruta_archivo, "rb") as f:
            cert_data = f.read()

        cert = x509.load_pem_x509_certificate(cert_data, default_backend())
        
        sujeto = cert.subject.rfc4514_string()
        valido_hasta = cert.not_valid_after_utc
        hoy = datetime.datetime.now(datetime.timezone.utc)
        dias_restantes = (valido_hasta - hoy).days

        # Lógica de estados
        print(f"\n[!] RESULTADO PARA: {ruta_archivo}")
        if dias_restantes < 0:
            print(f"ESTADO: ❌ EXPIRADO (Hace {abs(dias_restantes)} días)")
        elif dias_restantes < 30:
            print(f"ESTADO: ⚠️ ALERTA (Expira en {dias_restantes} días)")
        else:
            print(f"ESTADO: ✅ SEGURO ({dias_restantes} días restantes)")

        print(f"Detalle: {sujeto}")
        
        # Registrar en Log
        logging.info(f"Escaneo de {ruta_archivo} - Dias restantes: {dias_restantes}")

    except Exception as e:
        print(f"❌ Error técnico: {e}")
        logging.error(f"Error procesando {ruta_archivo}: {e}")

if __name__ == "__main__":
    print("=== PKI SENTINEL SCANNER ===")
    archivo = input("Introduce el nombre del archivo .pem (o arrástralo aquí): ")
    analizar_certificado(archivo)
    input("\nPresiona Enter para salir...")