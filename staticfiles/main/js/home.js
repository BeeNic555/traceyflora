document.addEventListener('DOMContentLoaded', () => {
  console.log("✅ FAQ 脚本已加载");

  const items = document.querySelectorAll('.faq-item');
  items.forEach(item => {
    const button = item.querySelector('.faq-question');
    if (button) {
      button.addEventListener('click', () => {
        item.classList.toggle('active');
      });
    }
  });
});


