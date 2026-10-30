from pathlib import Path
import re

root = Path(__file__).parent / 'docs'
for page in root.glob('*.html'):
    text = page.read_text(encoding='utf-8')
    text = text.replace('http://parklab.pitt.edu/img/', './img/')
    text = re.sub(r'  <link rel="start"[^>]+>\n', '', text)
    text = re.sub(r'  <link rel=[\"\x27](?:canonical|shortlink)[^\n]+\n', '', text)
    url = 'https://thejustpark.github.io/' + ('' if page.name == 'index.html' else page.name)
    text = text.replace('http://parklab.pitt.edu/', url)
    text = text.replace('<meta property="og:image" content="./img/logo.png">', '<meta property="og:image" content="https://thejustpark.github.io/img/logo.png">')
    text = text.replace('<nav class="only-pc">', '<nav id="navigation" aria-label="Main navigation">').replace('<nav>', '<nav id="navigation" aria-label="Main navigation">')
    text = text.replace('<div id="menu" class="only-sp"><i class="icons">menu</i></div>', '<button id="menu" class="only-sp" type="button" aria-controls="navigation" aria-expanded="false">Menu</button>')
    text = text.replace('class="here"', 'class="here" aria-current="page"')
    text = text.replace('target="_blank"', 'target="_blank" rel="noopener noreferrer"')
    text = re.sub(r'(    <h1>Park Lab</h1>\s*)([^<]+)', r'\1<p class="motto">\2</p>\n', text)
    text = text.replace('</br>', '<br>').replace('&nbsp', '&nbsp;').replace('alt="HJ Park email",', 'alt="HJ Park email"')
    text = text.replace('https://scholar.googleusercontent.com/citations?view_op=medium_photo&user=lRnvneUAAAAJ&citpid=2', './img/HJ_Profile.jpg')
    text = text.replace('<title>PARK LAB</title>', '<title>PARK LAB | Software</title>' if page.stem == 'software' else '<title>PARK LAB</title>')
    text = text.replace('<embed src="CV_HJPark.pdf" width="800px" height="2100px" />', '<p><a href="./CV_HJPark_Publications.pdf">Download publications PDF</a></p>\n    <iframe class="publications-pdf" src="./CV_HJPark_Publications.pdf" title="Publications in Dr. Park’s CV"></iframe>')
    text = re.sub(r'</html>\s*</html>', '</html>', text)
    text = re.sub(r'<li>(.*?)(?=<li>|</ul>)', lambda m: '<li>' + m[1].rstrip() + ('</span>' if '<span>' in m[1] and '</span>' not in m[1] else '') + '</li>\n', text, flags=re.S) if page.stem == 'members' else text
    if page.stem == 'software':
        text = re.sub(r'(<dd>.*?)(\s*</dl>)', lambda m: m[1].rstrip() + ('' if m[1].rstrip().endswith('</dd>') else '</dd>') + m[2], text, flags=re.S)
    page.write_text(text, encoding='utf-8')

css = (root / 'style.css').read_text().replace('http://parklab.pitt.edu/img/', './img/')
css += '''
/* Responsive shared layout for GitHub Pages. */
header { height: auto; min-height: 70px; display: flex; flex-wrap: wrap; align-items: center; gap: 12px 24px; }
header h1 { float: none; flex: 0 0 180px; }
.motto { flex: 1 1 260px; font-size: 13px; color: #66717d; }
nav { float: none; margin-left: auto; }
nav ul { display: flex; flex-wrap: wrap; gap: 16px; }
nav ul li { float: none; margin: 0; }
body > section { width: min(800px, 100%); padding: 0 20px; }
body > section > section { float: none; display: flow-root; }
img { max-width: 100%; height: auto; }
button { cursor: pointer; border: 1px solid #ddd; background: white; padding: 6px 12px; border-radius: 4px; }
a:focus-visible, button:focus-visible { outline: 3px solid #1ba1ff; outline-offset: 4px; }
#members dl dt img { margin-top: 0; filter: none; }
#software > section dl { float: none; }
#software > section dl dd { float: none; width: 100%; }
.publications-pdf { width: 100%; height: 85vh; min-height: 500px; border: 1px solid #ddd; margin: 20px 0; }
@media (max-width: 768px) {
  header { position: relative; }
  header h1 { flex: 1; }
  .motto { flex: 1 0 100%; order: 3; }
  #menu { float: none; }
  nav { position: static; width: 100%; height: auto; order: 4; }
  nav.is-open { display: block; }
  nav ul { display: block; }
  nav ul li { float: none; }
  #home dl:first-of-type dt { margin-top: 0; }
  #home dt img { max-width: 100%; }
}
'''
(root / 'style.css').write_text(css, encoding='utf-8')
(root / 'script.js').write_text('''const menu = document.getElementById('menu');
const panel = document.getElementById('navigation');
if (menu && panel) {
  const closeMenu = () => { panel.classList.remove('is-open'); menu.setAttribute('aria-expanded', 'false'); };
  menu.addEventListener('click', () => {
    const open = panel.classList.toggle('is-open');
    menu.setAttribute('aria-expanded', String(open));
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && panel.classList.contains('is-open')) { closeMenu(); menu.focus(); }
  });
  window.matchMedia('(max-width: 768px)').addEventListener('change', closeMenu);
}
''', encoding='utf-8')
(root / '.nojekyll').touch()
