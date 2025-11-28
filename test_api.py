#!/usr/bin/env python3
# Script para probar disponibilidad de modelos Gemini

import time
from langchain_google_genai import ChatGoogleGenerativeAI

API_KEY = "AIzaSyCzx74nncs7Qs5ITaNOVh9pcDv-mhn8DZM"

def test_model(model_name):
    """Prueba un modelo específico"""
    print(f"\n Probando modelo: {model_name}")
    try:
        chat_model = ChatGoogleGenerativeAI(
            model=model_name,
            google_api_key=API_KEY,
            temperature=0.7
        )
        
        # Prueba rápida
        response = chat_model.invoke("Hola, responde solo con 'OK'")
        print(f"✅ ÉXITO! Modelo {model_name} funciona")
        print(f"📝 Respuesta: {response.content[:50]}...")
        return True
        
    except Exception as e:
        error_str = str(e)
        if "404" in error_str:
            print(f" Modelo {model_name} NO EXISTE")
        elif "429" in error_str or "quota" in error_str.lower():
            print(f" Modelo {model_name} existe pero CUOTA EXCEDIDA")
            print(" Espera unos minutos e intenta de nuevo")
        else:
            print(f" Error en {model_name}: {error_str[:60]}...")
        return False

def main():
    print(" Testeando modelos disponibles de Google Gemini...")
    
    # Lista de modelos a probar
    models_to_test = [
        "gemini-2.0-flash-exp",
        "gemini-1.5-flash", 
        "gemini-1.5-pro",
        "gemini-pro",
        "text-bison-001",
        "chat-bison-001"
    ]
    
    working_models = []
    
    for model in models_to_test:
        success = test_model(model)
        if success:
            working_models.append(model)
        
        # Pausa pequeña entre pruebas
        time.sleep(1)
    
    print("\n" + "="*50)
    print(" RESUMEN DE RESULTADOS:")
    print("="*50)
    
    if working_models:
        print(f" Modelos que funcionan ({len(working_models)}):")
        for model in working_models:
            print(f"   • {model}")
    else:
        print(" Ningún modelo funciona actualmente")
        print(" Posibles causas:")
        print("   • Cuota del API excedida")
        print("   • API Key inválida")
        print("   • Problemas temporales del servicio")
    
    print("\n Recursos útiles:")
    print("   • Consola Google AI: https://ai.google.dev/")
    print("   • Límites de cuota: https://ai.google.dev/gemini-api/docs/rate-limits")

if __name__ == "__main__":
    main()