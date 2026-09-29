const lightbox = document.querySelector('dialog.cs-lightbox');
if (lightbox) {
  const image = lightbox.querySelector('img');
  for (const button of document.querySelectorAll('[data-full]')) {
    button.addEventListener('click', () => {
      image.src = button.dataset.full;
      image.alt = button.querySelector('img').alt;
      lightbox.showModal();
    });
  }
  lightbox.addEventListener('click', event => { if (event.target !== image) lightbox.close(); });
}
