// Build the site from the repository content (single source of truth).
// SITE_BASE_URL is set in CI to /python-dsa/ for GitHub Pages project sites.
const baseUrl = process.env.SITE_BASE_URL || '/';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Python DSA Masterclass',
  tagline: 'From your first Python program to top-tier interview readiness',
  favicon: 'img/logo.svg',

  headTags: [
    {tagName: 'meta', attributes: {property: 'og:site_name', content: 'Python DSA Masterclass'}},
    {tagName: 'meta', attributes: {property: 'og:type', content: 'website'}},
    {tagName: 'meta', attributes: {name: 'twitter:card', content: 'summary_large_image'}},
  ],

  url: 'https://ashiii27.github.io',
  baseUrl,
  organizationName: 'Ashiii27',
  projectName: 'python-dsa',
  trailingSlash: false,

  stylesheets: [
    'https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..900;1,9..144,300..900&family=Schibsted+Grotesk:wght@400..900&family=JetBrains+Mono:wght@400;500;700&display=swap',
  ],

  onBrokenLinks: 'throw',
  onBrokenAnchors: 'warn',

  markdown: {
    mermaid: true,
    format: 'detect',
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },

  themes: [
    '@docusaurus/theme-mermaid',
    [
      require.resolve('@easyops-cn/docusaurus-search-local'),
      /** @type {import('@easyops-cn/docusaurus-search-local').PluginOptions} */
      ({
        hashed: true,
        indexDocs: true,
        indexBlog: false,
        indexPages: true,
        docsRouteBasePath: ['/python', '/dsa', '/guides', '/practice'],
        docsDir: ['docs-python', 'docs-dsa', 'docs-guides', 'docs-practice'],
        docsPluginIdForPreferredVersion: 'python',
        highlightSearchTermsOnTargetPage: true,
      }),
    ],
  ],

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: false,
        blog: false,
        pages: {},
        sitemap: { changefreq: 'weekly', priority: 0.5 },
      }),
    ],
  ],

  plugins: [
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'python',
        path: 'docs-python',
        routeBasePath: 'python',
        sidebarPath: './sidebars.python.js',
      },
    ],
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'dsa',
        path: 'docs-dsa',
        routeBasePath: 'dsa',
        sidebarPath: './sidebars.dsa.js',
      },
    ],
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'guides',
        path: 'docs-guides',
        routeBasePath: 'guides',
        sidebarPath: './sidebars.guides.js',
      },
    ],
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'practice',
        path: 'docs-practice',
        routeBasePath: 'practice',
        sidebarPath: './sidebars.practice.js',
      },
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      image: 'img/og.png',
      announcementBar: {
        id: 'open-repo',
        content:
          'Built in the open — every note, problem and test lives in <a target="_blank" rel="noopener noreferrer" href="https://github.com/Ashiii27/python-dsa">one GitHub repository</a>.',
        backgroundColor: 'var(--paper-2)',
        textColor: 'var(--ink)',
        isCloseable: true,
      },
      colorMode: {
        defaultMode: 'dark',
        respectPrefersColorScheme: true,
      },
      mermaid: {
        theme: { light: 'neutral', dark: 'dark' },
      },
      navbar: {
        title: 'Python DSA Masterclass',
        logo: { alt: 'Python DSA Masterclass', src: 'img/logo.svg' },
        items: [
          {
            to: '/python',
            label: 'Python Track',
            position: 'left',
            activeBaseRegex: '/python(/|$)',
          },
          {
            to: '/dsa',
            label: 'DSA Track',
            position: 'left',
            activeBaseRegex: '/dsa(/|$)',
          },
          {
            to: '/guides/learning-path',
            label: 'Guides',
            position: 'left',
            activeBaseRegex: '/guides(/|$)',
          },
          {
            to: '/practice/top-interview-questions',
            label: 'Practice',
            position: 'left',
            activeBaseRegex: '/practice(/|$)',
          },
          {
            href: 'https://github.com/Ashiii27/python-dsa',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Learn',
            items: [
              { label: 'Python Track', to: '/python' },
              { label: 'DSA Track', to: '/dsa' },
              { label: 'Learning path', to: '/guides/learning-path' },
            ],
          },
          {
            title: 'Practice',
            items: [
              { label: 'Top interview questions', to: '/practice/top-interview-questions' },
              { label: 'Extended practice', to: '/practice/extended-practice' },
              { label: 'Revision flashcards', to: '/guides/revision-flashcards' },
            ],
          },
          {
            title: 'Repository',
            items: [
              { label: 'GitHub', href: 'https://github.com/Ashiii27/python-dsa' },
              { label: 'Contributing', href: 'https://github.com/Ashiii27/python-dsa/blob/main/CONTRIBUTING.md' },
            ],
          },
        ],
        copyright: `Python DSA Masterclass — content and site built from one open repository. © ${new Date().getFullYear()}`,
      },
      prism: {
        additionalLanguages: ['bash', 'python'],
      },
    }),
};

module.exports = config;
