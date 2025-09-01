(() => {
  const btn = document.getElementById('menu');
  const nav = document.getElementById('zona');
  const espaco = document.getElementById('espaco');

  if (!btn || !nav || !espaco) return;

  // Garante estado inicial fechado
  nav.classList.add('caixa-fechada');
  btn.setAttribute('aria-expanded', 'false');

  const setOpen = (open) => {
    nav.classList.toggle('caixa-aberta', open);
    nav.classList.toggle('caixa-fechada', !open);
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  };

  btn.addEventListener('click', (e) => {
    e.stopPropagation(); // evita que o clique borbulhe para o document
    const isOpen = nav.classList.contains('caixa-aberta');
    setOpen(!isOpen);
  });

  // Fecha ao clicar fora
  document.addEventListener('click', (e) => {
    if (!espaco.contains(e.target)) {
      setOpen(false);
    }
  });

  // Fecha com Esc
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      setOpen(false);
    }
  });
})();
