// Tipos globais para o projeto

declare module '*.css' {
  const content: Record<string, string>;
  export default content;
}

declare module '*.scss' {
  const content: Record<string, string>;
  export default content;
}

declare module '*.svg' {
  const content: string;
  export default content;
}

declare module '*.png' {
  const content: string;
  export default content;
}

declare module '*.jpg' {
  const content: string;
  export default content;
}

declare module '*.jpeg' {
  const content: string;
  export default content;
}

declare module '*.gif' {
  const content: string;
  export default content;
}

declare module '*.webp' {
  const content: string;
  export default content;
}

// Variáveis de ambiente
interface ImportMetaEnv {
  readonly VITE_API_URL: string;
  readonly VITE_FRONTEND_URL: string;
  readonly VITE_GEMINI_API_KEY: string;
  readonly VITE_OPENAI_API_KEY: string;
  readonly VITE_UNSPLASH_ACCESS_KEY: string;
  readonly NODE_ENV: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}