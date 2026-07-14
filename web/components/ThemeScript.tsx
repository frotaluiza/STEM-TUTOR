const _themeScript = `
try {
  const stored = localStorage.getItem('deeptutor-theme');
  document.documentElement.classList.remove('dark', 'theme-glass', 'theme-snow');
  if (stored === 'dark') document.documentElement.classList.add('dark');
  else if (stored === 'glass') document.documentElement.classList.add('dark', 'theme-glass');
  else if (stored === 'snow') document.documentElement.classList.add('theme-snow');
  else if (stored === 'light') {}
  else {
    if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
      document.documentElement.classList.add('dark');
      localStorage.setItem('deeptutor-theme', 'dark');
    } else {
      document.documentElement.classList.add('theme-snow');
      localStorage.setItem('deeptutor-theme', 'snow');
    }
  }
} catch (e) {}
`;

export default function ThemeScript() {
  return <script id="deeptutor-theme-init" dangerouslySetInnerHTML={{ __html: _themeScript }} suppressHydrationWarning />;
}
