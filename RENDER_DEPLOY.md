# Deploy no Render (Alternativa ao Railway)

## 🚀 Deploy Backend no Render

### 1. Database - Neon
1. Acesse [neon.tech](https://neon.tech)
2. Crie projeto: `veritas-radix`
3. Copie a `DATABASE_URL`

### 2. Backend - Render
1. Acesse [render.com](https://render.com)
2. **New** → **Web Service**
3. Conecte GitHub: `felipevieir4dev/veritas-radix-test`
4. **Root Directory**: `backend`
5. **Build Command**: `pip install -r requirements.txt`
6. **Start Command**: `python manage.py migrate && python manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:$PORT`

### 3. Variáveis de Ambiente (Render)
```
DEBUG=False
DJANGO_SECRET_KEY=django-insecure-sua-chave-123456789
DATABASE_URL=sua-url-do-neon
PYTHON_VERSION=3.11.0
```

### 4. Frontend - Cloudflare Pages
1. Acesse [dash.cloudflare.com/pages](https://dash.cloudflare.com/pages)
2. Conecte GitHub: `felipevieir4dev/veritas-radix-test`
3. **Build command**: `npm run build`
4. **Build output**: `dist`
5. **Root directory**: `/` (raiz)

### 5. Variáveis Frontend
```
VITE_API_URL=https://seu-app.onrender.com
NODE_ENV=production
```

## ✅ URLs Finais
- **Frontend**: https://veritas-radix-test.pages.dev
- **Backend**: https://seu-app.onrender.com
- **Database**: Neon PostgreSQL

**Render é mais simples que Railway para Django!**