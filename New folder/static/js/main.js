(function () {
    const header = document.querySelector(".site-header");
    const navToggle = document.querySelector(".nav-toggle");
    const navLinks = document.getElementById("navLinks");
    const toTop = document.getElementById("toTop");
    const toast = document.getElementById("toast");
    const form = document.getElementById("contactForm");
    const ticker = document.getElementById("ticker");
    const year = document.getElementById("year");
    const themeToggle = document.getElementById("themeToggle");
    const root = document.documentElement;

    // Theme (remembered per browser)
    if (themeToggle) {
        const applyTheme = (theme) => {
            root.setAttribute("data-theme", theme);
            themeToggle.querySelector("i").className = theme === "dark" ? "fas fa-sun" : "fas fa-moon";
            themeToggle.setAttribute("aria-label", theme === "dark" ? "Switch to light theme" : "Switch to dark theme");
            const meta = document.querySelector('meta[name="theme-color"]');
            if (meta) meta.setAttribute("content", theme === "dark" ? "#0b1120" : "#f6f8fc");
        };
        let saved = null;
        try { saved = localStorage.getItem("theme"); } catch (e) {}
        applyTheme(saved || "dark");
        themeToggle.addEventListener("click", () => {
            const next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
            applyTheme(next);
            try { localStorage.setItem("theme", next); } catch (e) {}
        });
    }

    if (year) year.textContent = new Date().getFullYear();

    // Duplicate ticker content so the loop is seamless
    if (ticker) ticker.innerHTML += ticker.innerHTML;

    // Mobile nav
    if (navToggle && navLinks) {
        const setOpen = (open) => {
            navLinks.classList.toggle("open", open);
            navToggle.setAttribute("aria-expanded", String(open));
            navToggle.querySelector("i").className = open ? "fas fa-xmark" : "fas fa-bars";
        };
        navToggle.addEventListener("click", () => setOpen(!navLinks.classList.contains("open")));
        navLinks.querySelectorAll("a").forEach((a) => a.addEventListener("click", () => setOpen(false)));
    }

    // Header + back-to-top on scroll
    const onScroll = () => {
        if (header) header.classList.toggle("scrolled", window.scrollY > 20);
        if (toTop) toTop.classList.toggle("show", window.scrollY > 600);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    if (toTop) toTop.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));

    // Smooth scroll with header offset
    document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
        anchor.addEventListener("click", (e) => {
            const id = anchor.getAttribute("href");
            if (!id || id === "#") return;
            const target = document.querySelector(id);
            if (!target) return;
            e.preventDefault();
            const top = id === "#top" ? 0 : target.getBoundingClientRect().top + window.scrollY - 72;
            window.scrollTo({ top, behavior: "smooth" });
        });
    });

    // Scroll-spy
    if (navLinks) {
        const spy = new IntersectionObserver(
            (entries) => {
                entries.forEach((entry) => {
                    if (!entry.isIntersecting) return;
                    navLinks.querySelectorAll("a:not(.nav-cta)").forEach((a) =>
                        a.classList.toggle("active", a.getAttribute("href") === "#" + entry.target.id)
                    );
                });
            },
            { rootMargin: "-45% 0px -50% 0px" }
        );
        document.querySelectorAll("main section[id]").forEach((s) => spy.observe(s));
    }

    // Reveal on scroll
    const reveal = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("visible");
                    reveal.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.12 }
    );
    document.querySelectorAll(".reveal").forEach((el) => reveal.observe(el));

    // Toast
    let toastTimer;
    function showToast(message, type) {
        if (!toast) return;
        const icon = type === "success" ? "fa-circle-check" : type === "error" ? "fa-circle-exclamation" : "fa-circle-info";
        toast.innerHTML = '<i class="fas ' + icon + '"></i><span></span>';
        toast.querySelector("span").textContent = message;
        toast.className = "toast show " + (type || "");
        clearTimeout(toastTimer);
        toastTimer = setTimeout(() => toast.classList.remove("show"), 4500);
    }

    // Contact form -> Flask /api/contact
    if (form) {
        form.addEventListener("submit", async (e) => {
            e.preventDefault();
            const payload = {
                name: form.name.value.trim(),
                email: form.email.value.trim(),
                subject: form.subject.value.trim(),
                message: form.message.value.trim(),
            };
            if (!payload.name || !payload.email || !payload.message) {
                showToast("Please fill in your name, email and message.", "error");
                return;
            }
            if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(payload.email)) {
                showToast("Please enter a valid email address.", "error");
                return;
            }

            const btn = form.querySelector('button[type="submit"]');
            const original = btn.innerHTML;
            btn.disabled = true;
            btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';

            try {
                const res = await fetch("/api/contact", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(payload),
                });
                const data = await res.json();
                if (!res.ok) throw new Error(data.error || "Failed to send");
                showToast(data.message, "success");
                form.reset();
            } catch (err) {
                showToast(err.message || "Could not send. Please try again or email me directly.", "error");
            } finally {
                btn.disabled = false;
                btn.innerHTML = original;
            }
        });
    }
})();
