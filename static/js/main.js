// =============================================
//  COMUNIDAD VIDA — main.js
// =============================================

document.addEventListener('DOMContentLoaded', () => {

    // --- Navbar: efecto scroll ---
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            navbar.classList.toggle('scrolled', window.scrollY > 40);
        });
    }

    // --- Navbar: marcar link activo ---
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.navbar__links a').forEach(link => {
        const linkPage = link.getAttribute('href').split('/').pop();
        if (linkPage === currentPage) link.classList.add('active');
    });

    // --- Navbar: menú hamburguesa ---
    const toggle = document.querySelector('.navbar__toggle');
    const navLinks = document.querySelector('.navbar__links');
    if (toggle && navLinks) {
        toggle.addEventListener('click', () => {
            navLinks.classList.toggle('open');
        });
        // Cerrar al hacer clic en un link
        navLinks.querySelectorAll('a').forEach(a => {
            a.addEventListener('click', () => navLinks.classList.remove('open'));
        });
    }

    // --- Animaciones al hacer scroll ---
    const animatedEls = document.querySelectorAll('.animate-on-scroll');
    if (animatedEls.length > 0) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.15 });

        animatedEls.forEach(el => observer.observe(el));
    }

    // --- Formulario de Contacto ---
    const form = document.getElementById('contact-form');
    const confirmMsg = document.getElementById('confirm-msg');

    if (form && confirmMsg) {
        form.addEventListener('submit', async (e) => {
            e.preventDefault();

            // Validación básica
            const inputs = form.querySelectorAll('input[required]');
            let valid = true;
            inputs.forEach(input => {
                if (!input.value.trim()) {
                    input.style.borderColor = 'var(--coral)';
                    valid = false;
                } else {
                    input.style.borderColor = '';
                }
            });

            if (!valid) return;

            // Mostrar estado de carga en el botón
            const submitBtn = document.getElementById('submit-btn') || form.querySelector('button[type="submit"]');
            submitBtn.textContent = 'Enviando...';
            submitBtn.disabled = true;

            form.submit();
        });
    }

});
