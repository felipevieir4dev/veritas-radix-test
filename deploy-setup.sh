#!/bin/bash

echo "🚀 Configurando deploy para Cloudflare Pages + Railway + Neon"

# 1. Frontend - Cloudflare Pages
echo "📦 Configurando frontend para Cloudflare Pages..."
cd src
npm install
npm run build

# 2. Backend - Railway
echo "🐍 Configurando backend para Railway..."
cd backend
pip install -r requirements.txt
python manage.py collectstatic --noinput

echo "✅ Setup completo!"
echo ""
echo "📋 Próximos passos:"
echo "1. Frontend (Cloudflare Pages):"
echo "   - Conecte seu repositório em https://dash.cloudflare.com/pages"
echo "   - Build command: npm run build"
echo "   - Build output: dist"
echo ""
echo "2. Backend (Railway):"
echo "   - Deploy em https://railway.app"
echo "   - Conecte seu repositório"
echo "   - Adicione variáveis de ambiente"
echo ""
echo "3. Banco de dados (Neon):"
echo "   - Crie database em https://neon.tech"
echo "   - Copie DATABASE_URL para Railway"