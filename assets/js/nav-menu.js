(function () {
  document.documentElement.classList.add('js-nav');

  document.addEventListener('DOMContentLoaded', function () {
    const toggle = document.querySelector('.nav-toggle');

    if (!toggle) {
      return;
    }

    const nav = document.getElementById(toggle.getAttribute('aria-controls'));

    if (!nav) {
      return;
    }

    const setOpen = function (isOpen) {
      nav.classList.toggle('is-open', isOpen);
      toggle.classList.toggle('is-open', isOpen);
      toggle.setAttribute('aria-expanded', String(isOpen));
      toggle.setAttribute('aria-label', isOpen ? 'Close navigation menu' : 'Open navigation menu');
    };

    toggle.addEventListener('click', function () {
      setOpen(toggle.getAttribute('aria-expanded') !== 'true');
    });

    nav.addEventListener('click', function (event) {
      if (event.target.closest('a')) {
        setOpen(false);
      }
    });

    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape') {
        setOpen(false);
      }
    });

    const desktopQuery = window.matchMedia('(min-width: 52.01em)');
    const closeOnDesktop = function (event) {
      if (event.matches) {
        setOpen(false);
      }
    };

    if (desktopQuery.addEventListener) {
      desktopQuery.addEventListener('change', closeOnDesktop);
    } else {
      desktopQuery.addListener(closeOnDesktop);
    }
  });
}());
