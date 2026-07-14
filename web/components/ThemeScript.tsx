/**
 * ThemeScript - Initializes theme from localStorage before React hydration
 * This prevents the flash of wrong theme on page load.
 *
 * Uses next/script with beforeInteractive so the script runs before hydration
 * and avoids the React 19 warning about client-rendered <script> tags.
 */
import Script from "next/script";

const THEME_SCRIPT_ID = "deeptutor-theme-init";

export default function ThemeScript() {
  return (
    <Script
      id={THEME_SCRIPT_ID}
      strategy="beforeInteractive"
      dangerouslySetInnerHTML={{
        __html: `
      try {
        const stored = localStorage.getItem('deeptutor-theme');
        document.documentElement.classList.remove('dark', 'theme-glass', 'theme-snow');
        if (stored === 'dark') {
          document.documentElement.classList.add('dark');
        } else if (stored === 'glass') {
          document.documentElement.classList.add('dark', 'theme-glass');
        } else if (stored === 'snow') {
          document.documentElement.classList.add('theme-snow');
        } else if (stored === 'light') {
          // already clean
        } else {
          if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
            document.documentElement.classList.add('dark');
            localStorage.setItem('deeptutor-theme', 'dark');
          } else {
            document.documentElement.classList.add('theme-snow');
            localStorage.setItem('deeptutor-theme', 'snow');
          }
        }
      } catch (e) {}
    `,
      }}
    />
  );
}
