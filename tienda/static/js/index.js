//REPLACE WITH YOUR PUBLIC KEY AVAILABLE IN: https://www.mercadopago.com/developers/panel
const mp = new MercadoPago('TEST-cf063386-7146-4a85-92b9-6cfcd9119ac1');

function loadCardForm() {
    const productCost = document.getElementById('amount').value;
    const productDescription = document.getElementById('product-description').innerText;

    const cardForm = mp.cardForm({
        amount: productCost,
        autoMount: true,
        form: {
            id: "form-checkout",
            cardholderName: {
                id: "form-checkout__cardholderName",
                placeholder: "Holder name",
            },
            cardholderEmail: {
                id: "form-checkout__cardholderEmail",
                placeholder: "E-mail",
            },
            cardNumber: {
                id: "form-checkout__cardNumber",
                placeholder: "Card number",
            },
            cardExpirationMonth: {
                id: "form-checkout__cardExpirationMonth",
                placeholder: "MM",
            },
            cardExpirationYear: {
                id: "form-checkout__cardExpirationYear",
                placeholder: "YY",
            },
            securityCode: {
                id: "form-checkout__securityCode",
                placeholder: "Security code",
            },
            installments: {
                id: "form-checkout__installments",
                placeholder: "Installments",
            },
            identificationType: {
                id: "form-checkout__identificationType",
            },
            identificationNumber: {
                id: "form-checkout__identificationNumber",
                placeholder: "Identification number",
            },
            issuer: {
                id: "form-checkout__issuer",
                placeholder: "Issuer",
            },
        },
        callbacks: {
            onFormMounted: error => {
                if (error) 
                    return console.warn("Form Mounted handling error: ", error);
                console.log("Form mounted");
            },
            onSubmit: event => {
                event.preventDefault();
            
                const {
                    paymentMethodId,
                    issuerId,
                    cardholderEmail: email,
                    amount,
                    token,
                    installments,
                    identificationNumber,
                    identificationType,
                } = cardForm.getCardFormData();
            
                fetch("/process_payment", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        token,
                        issuerId,
                        paymentMethodId,
                        transactionAmount: Number(amount),
                        installments: Number(installments),
                        description: productDescription,
                        payer: {
                            email,
                            identification: {
                                type: identificationType,
                                number: identificationNumber,
                            },
                        },
                    }),
                })
                .then(response => {
                    return response.json();
                })
                .then(result => {
                    document.getElementById("payment-status").innerText = result.status;
                    document.getElementById("payment-detail").innerText = result.message;
                    $('.container__payment').fadeOut(500);
                    setTimeout(() => { $('.container__result').show(500).fadeIn(); }, 500);
                })
                .catch(error => {
                    alert("Unexpected error\n"+JSON.stringify(error));
                });;
            },
            onFetching: (resource) => {
              console.log("Fetching resource: ", resource);
              const payButton = document.getElementById("form-checkout__submit");
              payButton.setAttribute('disabled', true);
              return () => {
                payButton.removeAttribute("disabled");
              };
            },
        },
    });
};

//Handle transitions
document.getElementById('checkout-btn').addEventListener('click', function(){ 
    $('.container__cart').fadeOut(500);
    setTimeout(() => { 
        loadCardForm();
        $('.container__payment').show(500).fadeIn(); 
    }, 500);
});
document.getElementById('go-back').addEventListener('click', function(){ 
    $('.container__payment').fadeOut(500);
    setTimeout(() => { $('.container__cart').show(500).fadeIn(); }, 500);
});

