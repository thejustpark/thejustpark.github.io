module.exports = {
  head: [
    [
      'link', {
        rel: 'icon',
        href: '/img/favicon.png'
      }
    ]
  ],
  base: '/',
  dest: 'dist',
  title: 'Park lab',
  description: 'Human Genetics at University of Pittsburgh',
  locales: {
    '/': {
      lang: 'en'
    }
  },
  meta: [
    {
      charset: 'utf-8'
    },
    {
      name: 'viewport',
      content: 'width=device-width, initial-scale=1'
    }
  ],
  themeConfig: {
    logo: '/img/logo.png',
    nav: [
      {
        text: 'Home',
        link: '/'
      },
      {
        text: 'Publications',
        link: '/publications'
      },
      {
        text: 'Members',
        link: '/members'
      },
      {
        text: 'Software',
        link: '/software'
      },
      // {
      //   text: 'News',
      //   link: '/news'
      // },
      // {
      //   text: 'Contact',
      //   link: '/contact'
      // },
      {
        text: 'GitHub',
        link: 'https://github.com/thejustpark'
      }
    ]
  }
}