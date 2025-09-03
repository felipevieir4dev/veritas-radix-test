#!/usr/bin/env python
"""
Script para aplicar correções de segurança e performance no backend.
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'veritas_radix.settings')
django.setup()

from django.core.management import execute_from_command_line

def apply_fixes():
    """Aplica todas as correções necessárias."""
    print("🔧 Aplicando correções de segurança e performance...")
    
    # 1. Criar migrações para mudanças no modelo
    print("📝 Criando migrações...")
    execute_from_command_line(['manage.py', 'makemigrations'])
    
    # 2. Aplicar migrações
    print("🗄️ Aplicando migrações...")
    execute_from_command_line(['manage.py', 'migrate'])
    
    # 3. Coletar arquivos estáticos
    print("📦 Coletando arquivos estáticos...")
    execute_from_command_line(['manage.py', 'collectstatic', '--noinput'])
    
    print("✅ Correções aplicadas com sucesso!")
    print("\n📋 Resumo das correções:")
    print("- URLs padronizadas (removido /v1/)")
    print("- Estrutura de dados alinhada com frontend")
    print("- Django REST Framework atualizado para versão segura")
    print("- Sanitização de entrada implementada")
    print("- Índices de performance adicionados")
    print("\n🚀 Backend pronto para uso!")

if __name__ == '__main__':
    apply_fixes()