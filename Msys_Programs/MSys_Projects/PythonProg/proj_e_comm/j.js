// Add to cart button event listener
const addToCartButtons = document.querySelectorAll('.product-card button');

addToCartButtons.forEach((button) => {
	button.addEventListener('click', () => {
		alert('Product added to cart!');
	});
});
