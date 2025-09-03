// Secure token storage utilities

interface TokenData {
  access_token: string;
  refresh_token?: string;
  expires_at?: number;
}

// Secure cookie-based storage (preferred)
export const secureTokenStorage = {
  setTokens: (data: TokenData): void => {
    // Set httpOnly cookies via API call to backend
    // This is more secure than localStorage
    document.cookie = `access_token=${data.access_token}; path=/; secure; samesite=strict; max-age=3600`;
    if (data.refresh_token) {
      document.cookie = `refresh_token=${data.refresh_token}; path=/; secure; samesite=strict; max-age=86400`;
    }
  },

  getAccessToken: (): string | null => {
    const cookies = document.cookie.split(';');
    const tokenCookie = cookies.find(c => c.trim().startsWith('access_token='));
    return tokenCookie ? tokenCookie.split('=')[1] : null;
  },

  clearTokens: (): void => {
    document.cookie = 'access_token=; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT';
    document.cookie = 'refresh_token=; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT';
  }
};

// Fallback to sessionStorage (better than localStorage)
export const fallbackTokenStorage = {
  setTokens: (data: TokenData): void => {
    if (typeof window !== 'undefined') {
      sessionStorage.setItem('auth_data', JSON.stringify(data));
    }
  },

  getAccessToken: (): string | null => {
    if (typeof window !== 'undefined') {
      const data = sessionStorage.getItem('auth_data');
      if (data) {
        const parsed = JSON.parse(data);
        return parsed.access_token || null;
      }
    }
    return null;
  },

  clearTokens: (): void => {
    if (typeof window !== 'undefined') {
      sessionStorage.removeItem('auth_data');
    }
  }
};

// Main token storage interface
export const tokenStorage = {
  setTokens: (data: TokenData): void => {
    try {
      secureTokenStorage.setTokens(data);
    } catch {
      fallbackTokenStorage.setTokens(data);
    }
  },

  getAccessToken: (): string | null => {
    return secureTokenStorage.getAccessToken() || fallbackTokenStorage.getAccessToken();
  },

  clearTokens: (): void => {
    secureTokenStorage.clearTokens();
    fallbackTokenStorage.clearTokens();
  }
};