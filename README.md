# pki-sentinel
# 🔐 PKI Sentinel – Certificate Expiry Scanner

Herramienta en Python para analizar certificados X.509 (.pem) y detectar expiraciones, orientada a tareas de monitoreo en ciberseguridad (SOC / Blue Team).

---

## 🚀 Características

* 📄 Análisis de certificados X.509
* ⏱️ Cálculo de días restantes
* 🚨 Detección de certificados expirados o próximos a expirar
* 🧾 Logging automático de auditoría
* 💻 Interfaz simple por consola

---

## 🧰 Tecnologías

* Python 3
* cryptography

---

## ⚙️ Instalación

```bash
pip install -r requirements.txt
```

---

## ▶️ Uso

```bash
python certcheck.py
```

Luego ingresa la ruta del certificado `.pem`.

---

## 📊 Ejemplo de salida

```
ESTADO: ⚠️ ALERTA (Expira en 12 días)
Detalle: CN=example.com
```

---

## 📁 Estructura

```
certcheck.py
requirements.txt
sample_cert.pem
pki_audit.log
```

---

## 🎯 Objetivo

Simular monitoreo de certificados en entornos reales de seguridad (SOC).

---

## 👤 Autor

Bayron Cares

