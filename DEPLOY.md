# Deploy Guide - Cloudflare Pages + Railway + Neon

## 🏗️ Arquitetura de Deploy

- **Frontend**: Cloudflare Pages (React + Vite)
- **Backend**: Railway (Django + PostgreSQL)
- **Database**: Neon (PostgreSQL gerenciado)

## 🚀 Deploy Automático

Execute o script de setup:
```bash
chmod +x deploy-setup.sh
./deploy-setup.sh
```

## 📋 Deploy Manual

### 1. Database - Neon

1. Acesse [neon.tech](https://neon.tech)
2. Crie novo projeto: `veritas-radix`
3. Copie a `DATABASE_URL`

### 2. Backend - Railway

1. Acesse [railway.app](https://railway.app)
2. Conecte repositório GitHub
3. Selecione pasta `backend/`
4. Adicione variáveis de ambiente:

```env
DEBUG=False
DJANGO_SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://user:pass@host:port/db
GEMINI_API_KEY=your-gemini-key
OPENAI_API_KEY=your-openai-key
UNSPLASH_ACCESS_KEY=your-unsplash-key
ALLOWED_HOST=veritas-radix-backend-production.up.railway.app
```

### 3. Frontend - Cloudflare Pages

1. Acesse [dash.cloudflare.com/pages](https://dash.cloudflare.com/pages)
2. Conecte repositório GitHub
3. Configurações:
   - **Build command**: `npm run build`
   - **Build output**: `dist`
   - **Root directory**: `/` (raiz do projeto)

4. Variáveis de ambiente:
```env
VITE_API_URL=https://veritas-radix-backend-production.up.railway.app
VITE_FRONTEND_URL=https://veritas-radix.pages.dev
NODE_ENV=production
```

## 🔧 Configurações Importantes

### Railway (Backend)
- Arquivo `railway.toml` configurado
- Arquivo `nixpacks.toml` para build
- Arquivo `Procfile` para start
- CORS configurado para Cloudflare Pages

### Cloudflare Pages (Frontend)
- Arquivo `wrangler.toml` configurado
- Build com Vite otimizado
- Variáveis de ambiente configuradas

### Neon (Database)
- PostgreSQL 15
- Conexão via `DATABASE_URL`
- Migrations automáticas no deploy

## 🌐 URLs de Produção

- **Frontend**: https://veritas-radix.pages.dev
- **Backend**: https://veritas-radix-backend-production.up.railway.app
- **Database**: Neon PostgreSQL (privado)

## ✅ Verificação

Após deploy, teste:
1. Frontend carregando
2. Login funcionando
3. API respondendo
4. Database conectado