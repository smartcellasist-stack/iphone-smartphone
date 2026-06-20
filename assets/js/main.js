/* ═══════════════════════════════════════════════════════════
   MAIN.JS — utilitários compartilhados entre páginas
   iphonesmartphone.com.br
   Vanilla JS, sem dependências. Carregar no fim do <body>.
   ═══════════════════════════════════════════════════════════ */

(function () {
  /* Scroll reveal — anima elementos com a classe .reveal ao entrar na tela.
     Extraído do index.html (era duplicado por página antes da migração). */
  const els = document.querySelectorAll(".reveal");
  if (!els.length) return;

  const io = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry, i) {
        if (entry.isIntersecting) {
          setTimeout(function () {
            entry.target.classList.add("in");
          }, i * 60);
          io.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.1 }
  );

  els.forEach(function (el) {
    io.observe(el);
  });
})();
