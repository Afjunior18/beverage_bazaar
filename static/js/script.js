// Rating

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.dropdown-menu a.dropdown-item').forEach(item => {
        item.addEventListener('click', function() {
            const ratingValue = this.getAttribute('data-value');
            document.getElementById('rating').value = ratingValue;
            document.getElementById('dropdownRating').innerText = `Rate ${ratingValue}`;
        });
    });
});
