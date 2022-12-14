var stripe_public_key = $('#id_stripe_public_key').text().slice(1,-1);
var client_secret = $('#id_client_key').text().slice(1,-1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var style = {
    base: {
        color: '000',
        fontFamily: '"Helvetice Neue", Helvetice, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4',
        }
    },
    invalid: {
        color: '#F0F8FF',
        iconColor: '#F0F8FF'
    }
};
var card = elements.create('card');
card.mount('#card-element');

card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
        <span class="icon" role="alert">
            <i class="fas fa-times"></i>
        </span>
        <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});